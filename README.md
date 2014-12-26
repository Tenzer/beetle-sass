# Beetle-Sass

[SASS](http://sass-lang.com/) rendering for the [Beetle](https://github.com/cknv/beetle) static site generator.

This plugin both works as a content renderer plugin and an includer handler, so any `.sass` or `.scss` files in your content or include folder will be rendered to CSS files when this plugin is enabled.

Note however that you need to specify the destination file name in the YAML for a SASS file in the content folder, where as files in the include folder simply will have their file extension replaced with `.css`.

You can specify one extra argument to the plugin in your `config.yaml` file: `output_style` which is then sent to the SASS compiler to specify how you want it to output the final CSS. If you for instance want a compressed/minified output you should add `output_style: compressed` to your configuration file. The available options are `nested` (the default), `expanded`, `compact` and `compressed`.
