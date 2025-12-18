# File Icon Generator

<span align="center">
<img src="./docs/jpg_page.svg">
<img src="./docs/jpg_solid_rounded.svg">
<img src="./docs/jpg_solid_squared.svg">
</span>

This script generates SVG icons for file extensions using customizable templates. The icons are generated with colors and font sizes adapted to the length of the extension.
 
> ⚠️ Hi there ! This code was generated with the help of the `Mistral Vibe CLI`. Even if I reviewed and test the code, tell me if you see anything wrong !

## Features

- **Automatic Generation**: Generate icons for file extensions from a JSON file.
- **Customizable Templates**: Use SVG as templates to decline icons with different styles.
- **Aliases**: Support for aliases for extensions (e.g., DOC and DOCX).
- **Dynamic Font Size**: Automatically adjust the font size based on the length of the extension.
- **Customization**: Allow specifying a custom font size for each extension.

## TO-DO (Not sorted)
- [ ] **More font placeholder** : font-family and font color
- [ ] Change all **default settings** (default font, size, etc.)
- [ ] More **basic templates**
- [ ] **Convert SVG to PNG** (with custom size)

## Commands Examples

```bash
# Generate icons for all templates
python3 generate_icons.py

# Generate icons with a specific template.
python3 generate_icons.py -t templates/template_other.svg

# Generate icons with a custom JSON file. 
python3 generate_icons.py -j custom_extensions.json

# Generate icons in a specific output directory
python3 generate_icons.py -o /path/to/directory

# Check for duplicates in aliases and extensions
python3 generate_icons.py -c

# Overwrite existing files
python3 generate_icons.py -f
```

## Summary
1. [Installation](#installation)
1. [How to use](#how-to-use)
1. [JSON](#json-file)
1. [Templates](#templates)
1. [Font Size](#font-size)
1. [Contribution](#contribution)
1. [License](./LICENSE)


## How to use

### Generate icons for all templates

To generate icons for all extensions with all available templates, simply run:

```bash
python3 generate_icons.py
```

This will use the default `extensions.json` file and generate icons for all templates in the `templates` directory. The icons will be saved in the `icons/` directory with subdirectories corresponding to each template.

### Generate icons with a specific template

To generate icons with only a specific template, use the `-t` or `--template` option:

```bash
python3 generate_icons.py -t templates/template_solid.svg
```

By default, the icons will be saved in the `icons/` directory with a subdirectory corresponding to the template name. For example, if you use the `template_solid.svg` template, the icons will be saved in the `icons/solid/` directory.

### Generate icons with a custom JSON file

To use a custom JSON file, specify the path to the file using the `-j` or `--json` option:

```bash
python3 generate_icons.py -j my_file.json
```

### Generate icons in a specific output directory

To specify a different output directory, use the `-o` or `--output-dir` option:

```bash
python3 generate_icons.py -o /path/to/directory
```

This will override the default directory structure and save the icons in the specified directory.

### Check for duplicates in aliases and extensions

To check for duplicates in aliases and extensions, use the `-c` or `--check` option:

```bash
python3 generate_icons.py -c
```

### Overwrite existing files

To overwrite existing files, use the `-f` or `--force` option:

```bash
python3 generate_icons.py -f
```

## JSON File

The `extensions.json` file contains the file extensions and their colors. Here is an example structure:

```json
{
    "7Z": "#FFD600",
    "AIFF": "#FF5722",
    "APK": "#4CAF50",
    "APP": "#4CAF50",
    "ARW": "#7B1FA2",
    "AVI": "#D32F2F",
    "AZURE": "#0078D4",
    "BIN": "#616161",
    "BMP": "#7B1FA2",
    "BZ2": "#FFD600",
    "CC": "#673AB7",
    "CLASS": "#795548",
    "CONFIG": "#616161",
    "CPP": {
        "color": "#673AB7",
        "aliases": ["CC", "CP", "CXX", "C++"]
    },
    ...
}
```

### Supported Formats

1. **Simple Format**: A string representing the color.
   ```json
   "PDF": "#444CE7"
   ```

2. **Advanced Format**: An object with a color, aliases, and a custom font size.
   ```json
   "DOC": {
       "color": "#2B579A",
       "aliases": ["DOCX", "DOCM", "DOT", "DOTX", "DOTM"],
       "font_size": 10
   }
   ```

### Available Fields

- **color**: The color in hexadecimal (e.g., "#FF0000").
- **aliases**: A list of aliases for the extension (e.g., ["DOCX", "DOCM"]).
- **font_size**: The custom font size (optional).

## Templates

SVG templates are stored in the `templates/` directory. Each template must have a name starting with `template_` and ending with `.svg`. Templates must contain the following placeholders:

- `{color}`: The color of the icon.
- `{extension}`: The text of the extension.
- `{font_size}`: The font size.

### Example Template

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 40 40" fill="none">
    <path fill="{color}" d="M4 4a4 4 0 0 1 4-4h16l12 12v24a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4z"/>
    <path fill="#fff" d="m24 0 12 12h-8a4 4 0 0 1-4-4z" opacity=".3"/>
    <text x="20" y="35" font-family="Arial, sans-serif" font-size="{font_size}" font-weight="bold" fill="#fff" text-anchor="middle">{extension}</text>
</svg>
```

## Font Size

The font size is automatically adjusted based on the length of the extension:

- 3 letters or less: 10 pt
- 4 letters: 9 pt
- 5 letters: 8 pt
- 6 letters: 7 pt
- 7 letters: 6 pt
- 8 letters: 5 pt
- 9 letters or more: 4 pt

You can also specify a custom font size for a specific extension using the `font_size` field in the JSON file.

## Contribution

If you would like to contribute to this project, you can:

- Add new SVG templates
- Improve the script to add new features.
- Fix bugs or improve the documentation.

Feel free to pull request !

### Project Structure

```
.
├── generate_icons.py          # Main script to generate icons
├── extensions.json            # JSON file containing all extensions and their colors
├── templates/                 # Directory containing SVG templates
│   ├── template_solid.svg     # One basic template. Add yours !
│   └── ...
└── icons/                     # Directory containing the generated icons
    ├── solid/                 # Sorted by template name.
    └── ...

```

## License

This project is licensed under the GNU GPLv3 License. See [LICENSE](./LICENSE) to review the full text.