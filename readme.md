# Assets Manager

## Dart Assets Generator

This repository contains a simple Python script for generating Dart code that defines static asset variables based on the contents of a specified folder.

## Usage

Place your `asset_manager.py` file in the root directory of your project.

### Make sure

1. Your project sturcture suits the `asset_manager.py` script.

- ensure all assets (animations, images, svgs) are in the `assets` folder in the root directory.
- the `assets` folder must contain only folders and no file.
- mind the names of your folders and files becuase the name is used in writing the generated code.
- use `snake_cases` only for naming both folders and files.
- precede all folders you want the script to ignore with 'ignore' example: `ignore_this_folder`, in this case, `this_folder` will be ignored.

### or

2. You tweak the `asset_manager.py` script to suit your project structure.

### After satisfying the requirements above

- Run the script 🎉.
