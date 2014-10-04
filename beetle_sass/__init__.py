from os import sep as path_separator

import sass


class SassRenderer(object):
    def __init__(self, include_path):
        self.include_path = include_path
        if not include_path.endswith(path_separator):
            self.include_path += path_separator

    def render(self, source):
        # Chop of the include path and replace the file extension
        destination = source[len(self.include_path):-4] + 'css'
        return destination, sass.compile(filename=source).encode('UTF-8')


def register(context, plugin_config):
    sass_extensions = ['sass', 'scss']
    sass_renderer = SassRenderer(context.config.folders['include'])
    context.includer.add(sass_extensions, sass_renderer.render)
