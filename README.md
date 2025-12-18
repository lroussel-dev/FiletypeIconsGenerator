# File Icon Generator

<span text-align="center">
<img src="./docs/jpg_page.svg">
<img src="./docs/jpg_solid_rounded.svg">
<img src="./docs/jpg_solid_squared.svg">
</span>

**Searching huge icons pack can be exhausting**. Sometimes you don't have the money to pay designers, 
sometimes you need a particular extension never used by everybody, you don't like the color of one of the icon, etc.

So I decided to make a simple generator from SVG template. Everybody can make any extension with any color from any SVG file.

> ⚠️ The code was mainly generated with the help of the `Mistral Vibe CLI`. Even if I had fully reviewed and tested the code, tell me if you see anything wrong ! 

## Examples [here](https://lroussel-dev.github.io/FiletypeIconsGenerator/)

## Features

- **🤖 Automatic Generation**: Generate file extension icons from a JSON configuration file
- **🎨 Customizable Templates**: Use SVG templates to style icons with different visual themes
- **🔄 Alias Support**: Handle file extension aliases *(e.g., DOC and DOCX)*
- **📏 Dynamic Font Sizing**: Automatically adjust text size based on extension length
- **⚙️ Advanced Customization**: Specify custom font sizes for individual extensions *(and more in the future !)*

## Summary
1. [TO-DO](#to-do)
1. [Quick Start](#quick-start)
1. [How to use](#how-to-use)
1. [JSON](#json-file)
1. [Templates](#templates)
1. [Font Size](#font-size)
1. [Contribution](#contribution)
1. [License](./LICENSE)

## TO-DO
This list is not sorted by priority. It's just a memo for myself !
- [ ] **More font placeholder** : font-family and font color
- [ ] Change all **default settings** (default font, size, etc.)
- [ ] More **basic templates**
- [ ] **Convert SVG to PNG** (with custom size)
- [ ] Generate only **one icon**

## Quick Start

```bash
# Generate icons for all templates
python generate_icons.py

# Generate icons with a specific template.
python generate_icons.py -t templates/template_other.svg

# Generate icons with a custom JSON file. 
python generate_icons.py -j custom_extensions.json

# Generate icons in a specific output directory
python generate_icons.py -o /path/to/directory

# Check for duplicates in aliases and extensions
python generate_icons.py -c

# Overwrite existing files
python generate_icons.py -f

python generate_icons.py -t templates/template_solid_rounded.svg -j json/commons.json -o docs/images
```


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

## README.md

Write by love by human, with the correction of a robot ❤️