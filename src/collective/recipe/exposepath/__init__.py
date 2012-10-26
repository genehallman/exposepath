from zc.recipe.egg.egg import Egg
import json
import logging
import os

class Recipe(object):
    def __init__(self, buildout, name, options):
        self.log = logging.getLogger(name)
        self.buildout = buildout
        self.options = options
        self.name = name
        output = {}
        paths = self._get_working_set()
        output['json-path'] = json.dumps(paths, indent=4)
        if options['format']:
            format_str = options.get('format')
            output['formatted-path'] = "\n  ".join("'%s'," % path if path.startswith("/") else format_str % path for path in paths)
        self.options.update(output)

    def install(self):
        return tuple()

    def update(self):
        self.install()

    def _get_working_set(self):
        relative_path = self.options.get('relative-paths', '')
        if relative_path.lower() == 'true':
            relative_path = self.buildout['buildout']['directory']

        egg = Egg(self.buildout, self.options['recipe'], self.options)
        extra_paths = self.options.get('extra-paths', '').split('\n')

        ws = egg.working_set()[1]
        retval = [dist.location for dist in ws]
        retval.extend(extra_paths)

        if relative_path:
            eggs_dir = self.buildout['buildout'].get('eggs-directory', '.')
            base_dir = self.buildout['buildout'].get('directory', '.')
            common = os.path.commonprefix([eggs_dir, base_dir])
            rel_eggs_dir = eggs_dir.replace(common, '.')
            for i, loc in enumerate(retval):
                if loc.startswith(os.path.realpath(eggs_dir)):
                    retval[i] = loc.replace(os.path.realpath(eggs_dir), rel_eggs_dir)
                elif loc.startswith(os.path.realpath(base_dir)):
                    retval[i] = loc.replace(os.path.realpath(base_dir), '.')
        return retval
