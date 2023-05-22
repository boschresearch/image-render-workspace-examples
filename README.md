# Example Configurations for the Image-Render automation system

**Check out the `stable` branch for the latest stable version**

This repository contains example configurations for the `image-render` automation system. It currently contains the following configuration examples:

- `modify`: Examples for all Catharsys Blender modifiers with documentation in the configuration files.
- `tpl/pyact-01`: Example configuration to call a custom python action generated with `cathy install template std-action-python`.
- `usecase/load-modify-save`: Use-case example for loading object into Blender file, modifying it and saving resultant Blender file instead of rendering.
- `usecase/loop-randomize`: Use-case example for randomizing a Blender scene setup with a `loop` construct.
- `vars`: Configurations to show the use of pre-defined Catharsys variables.

See the repository `image-render-setup` for more information and documentation on the `image-render` automation system.

## Purpose of the project

This software is a research prototype, originally developed for use in rendering automation.

The software is not ready for production use. It has neither been developed nor tested for a specific use case. However, the license conditions of the applicable Open Source licenses allow you to adapt the software to your needs. Before using it in a safety relevant setting, make sure that the software fulfills your requirements and adjust it according to any applicable safety standards (e.g. ISO 26262).

## Contributing to the project

Please read the conditions you need to comply with in order to contribute to this project in the [CONTRIBUTING](CONTRIBUTING.md) file. 

## License

The `image-render-workspace-examples` package is licenced under the CC-BY-4.0 license. See the [LICENSE](LICENSE.md) file for more details.
