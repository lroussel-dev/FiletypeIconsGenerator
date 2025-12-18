#!/usr/bin/env python3

"""
File Icon Generator
===================

This script generates SVG icons for file extensions using customizable templates.
It supports automatic font size adjustment based on extension length and allows
for aliases to be defined for extensions.

Usage:
    python3 generate_icons.py [OPTIONS]

Options:
    --check              Check for duplicates in aliases and extensions.
    --force              Overwrite existing files.
    --output-dir DIR     Output directory for the icons (default: current directory).
    --template FILE      SVG template file to use. If not specified, all templates
                        in the templates directory will be used.

Examples:
    python3 generate_icons.py
    python3 generate_icons.py --check
    python3 generate_icons.py --template templates/template_solid.svg
    python3 generate_icons.py --force
"""

import json
import os
import argparse


def load_template(template_file):
    """
    Load an SVG template from a file.
    
    Args:
        template_file (str): The path to the template file.
    
    Returns:
        str: The content of the SVG template.
    """
    with open(template_file, "r") as f:
        return f.read()


def get_font_size(extension_length, custom_size=None):
    """
    Determine the font size based on the length of the extension.
    
    Args:
        extension_length (int): The length of the extension.
        custom_size (int, optional): The custom font size.
    
    Returns:
        int: The font size.
    """
    if custom_size is not None:
        return custom_size
    
    # Font size based on the length of the extension
    if extension_length <= 3:
        return 10
    elif extension_length == 4:
        return 9
    elif extension_length == 5:
        return 8
    elif extension_length == 6:
        return 7
    elif extension_length == 7:
        return 6
    elif extension_length == 8:
        return 5
    else:
        return 4


def generate_icon(extension, color, output_dir, template_svg, font_size=None, force=False):
    """
    Generate an SVG icon for a given extension with a specific color.
    
    Args:
        extension (str): The file extension (e.g., "PDF", "DOC").
        color (str): The color in hexadecimal (e.g., "#FF0000").
        output_dir (str): The output directory for the icons.
        template_svg (str): The SVG template to use.
        font_size (int, optional): The font size.
        force (bool, optional): If True, overwrite existing files.
    """
    filename = f"{extension.lower()}.svg"
    filepath = os.path.join(output_dir, filename)
    
    # Check if the file already exists
    if os.path.exists(filepath) and not force:
        print(f"File {filename} already exists, it will not be overwritten.")
        return
    
    # Determine the font size
    if font_size is None:
        font_size = get_font_size(len(extension))
    
    # Generate the SVG content
    svg_content = template_svg.format(color=color, extension=extension, font_size=font_size)
    
    # Write the file
    with open(filepath, "w") as f:
        f.write(svg_content)
    
    print(f"Icon generated: {filename}")


def generate_icons_from_json(json_file, output_dir, template_file="template_solid.svg", force=False):
    """
    Generate icons from a JSON file containing extension/color pairs.
    
    Args:
        json_file (str): The path to the JSON file.
        output_dir (str): The output directory for the icons.
        template_file (str): The SVG template file to use.
        force (bool, optional): If True, overwrite existing files.
    """
    # Load the SVG template
    template_svg = load_template(template_file)
    
    # Read the JSON file
    with open(json_file, "r") as f:
        data = json.load(f)
    
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Generate the icons
    for extension, config in data.items():
        # Check if the configuration is a string (color) or an object (with aliases)
        if isinstance(config, str):
            color = config
            generate_icon(extension, color, output_dir, template_svg, force=force)
        elif isinstance(config, dict):
            color = config.get("color", "#000000")  # Default color if not specified
            font_size = config.get("font_size")  # Custom font size
            generate_icon(extension, color, output_dir, template_svg, font_size, force)
            
            # Generate icons for aliases
            aliases = config.get("aliases", [])
            for alias in aliases:
                generate_icon(alias, color, output_dir, template_svg, font_size, force)


def check_aliases(json_file="extensions.json"):
    """
    Check for duplicates in aliases and extensions.
    
    Args:
        json_file (str): The path to the JSON file.
    """
    # Read the JSON file
    with open(json_file, "r") as f:
        data = json.load(f)
    
    # Collect all main extensions
    main_extensions = set(data.keys())
    
    # Collect all aliases
    all_aliases = set()
    aliases_map = {}
    
    for extension, config in data.items():
        # Check if the configuration is an object (with aliases)
        if isinstance(config, dict):
            aliases_list = config.get("aliases", [])
            for alias in aliases_list:
                # Check if the alias is already a main extension
                if alias in main_extensions:
                    print(f"⚠️  Alias '{alias}' for extension '{extension}' is already defined as a main extension.")
                # Check if the alias is already an alias for another extension
                if alias in all_aliases:
                    print(f"⚠️  Alias '{alias}' for extension '{extension}' is already an alias for extension '{aliases_map[alias]}'.")
                else:
                    all_aliases.add(alias)
                    aliases_map[alias] = extension
    
    # Check main extensions that are also aliases
    extensions_in_aliases = main_extensions.intersection(all_aliases)
    
    print("\n📋 List of aliases:")
    for alias, extension in aliases_map.items():
        print(f"  - {alias} → {extension}")
    
    print(f"\n✅ Total: {len(main_extensions)} extensions and {len(all_aliases)} aliases.")
    
    # Ask the user if they want to remove main extensions that are also aliases
    if extensions_in_aliases:
        print(f"\n⚠️  Main extensions that are also aliases: {', '.join(extensions_in_aliases)}")
        response = input("Do you want to remove these main extensions that are also aliases? (yes/no): ").strip().lower()
        if response == "yes":
            # Remove main extensions that are also aliases
            for extension in extensions_in_aliases:
                if extension in data:
                    del data[extension]
            
            # Save the updated JSON file
            with open(json_file, "w") as f:
                json.dump(data, f, indent=4)
            
            print(f"✅ Main extensions that are also aliases have been removed.")
        else:
            print("❌ No changes made.")
    else:
        print("\n✅ No main extensions that are also aliases found.")


def generate_all_templates(json_file="extensions.json", templates_dir="templates", force=False):
    """
    Generate icons for all templates in the templates directory.
    
    Args:
        json_file (str): The path to the JSON file.
        templates_dir (str): The directory containing the templates.
        force (bool, optional): If True, overwrite existing files.
    """
    # Check if the templates directory exists
    if not os.path.exists(templates_dir):
        print(f"Directory {templates_dir} does not exist.")
        return
    
    # List all files in the templates directory
    template_files = [f for f in os.listdir(templates_dir) if f.startswith("template_") and f.endswith(".svg")]
    
    if not template_files:
        print(f"No templates found in directory {templates_dir}.")
        return
    
    # Generate icons for each template
    for template_file in template_files:
        template_name = template_file.replace("template_", "").replace(".svg", "")
        output_dir = os.path.join("icons", template_name)
        template_path = os.path.join(templates_dir, template_file)
        
        print(f"Generating icons with template {template_name}...")
        generate_icons_from_json(json_file, output_dir, template_path, force)


def main():
    """
    Main function to parse arguments and generate icons.
    """
    # Configure the argument parser
    parser = argparse.ArgumentParser(description="Generate icons for file extensions.")
    parser.add_argument("json_file", nargs="?", default="extensions.json", help="Path to the JSON file containing extension/color pairs (default: extensions.json).")
    parser.add_argument("--output-dir", default=".", help="Output directory for the icons (default: current directory).")
    parser.add_argument("--template", default=None, help="SVG template file to use. If not specified, all templates in the templates directory will be used.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files.")
    parser.add_argument("--check", action="store_true", help="Check for duplicates in aliases and extensions.")
    
    args = parser.parse_args()
    
    # If the check option is specified, check for duplicates
    if args.check:
        check_aliases(args.json_file)
    else:
        # If a template is specified, generate icons with that template
        if args.template:
            generate_icons_from_json(args.json_file, args.output_dir, args.template, args.force)
        else:
            # Otherwise, generate icons for all templates in the templates directory
            generate_all_templates(args.json_file, force=args.force)


if __name__ == "__main__":
    main()