# User Guide for "Plugin Example 2"

## Introduction

**Plugin Example 2** is designed to add new character customization options for RPG Maker MZ. It enhances the default customization system by providing more control over character appearance and attributes.

## Features

- **Enhanced Character Customization**: More options for character appearance and attributes.
- **User-Friendly Interface**: Intuitive controls for easy customization.
- **Seamless Integration**: Works with existing character systems.
- **Fully Compatible**: Specifically designed for RPG Maker MZ.

## Screenshots

![Character Customization](https://via.placeholder.com/800x400?text=Character+Customization)

![Interface Options](https://via.placeholder.com/800x400?text=Interface+Options)

![Custom Characters](https://via.placeholder.com/800x400?text=Custom+Characters)

## Installation Instructions

1. **Download**: Get the plugin file from the official website.
2. **Installation**: Place the file in the `js/plugins` folder of your RPG Maker project.
3. **Activation**: Enable the plugin via the RPG Maker plugin manager.
4. **Configuration**: Customize the settings as needed in the plugin manager.

## Plugin Commands / Script Calls

Here is an example of a script call to use a plugin feature:

```javascript
// Example: Apply custom appearance to a character
const characterId = 2; // Character ID
const appearanceId = 3; // Custom appearance ID

const character = $gameMap.event(characterId);
if (character) {
    character.setCustomAppearance(appearanceId);
    console.log(`Character ID ${characterId} now has appearance ID ${appearanceId}.`);
} else {
    console.error("Character not found!");
}
```

This example demonstrates how to apply a custom appearance to a character. Make sure the IDs match those in your project.

## Demo

A project demo is available, showcasing all the features of **Plugin Example 2**. It includes examples of enhanced character customization options.

[Download the demo](https://example.com/plugin2/demo)

## Version History

- **v0.9.0** (12/01/2024): [Download](https://example.com/plugin2/v0.9.0)
- **v1.0.0** (01/15/2025): [Download](https://example.com/plugin2/v1.0.0)

## Authors

- **Jane Smith**: [Profile](https://example.com/janesmith)
- **Alex Johnson**: [Profile](https://example.com/alexj)

## Status

This plugin is currently in **Stable** status and is ready for production use.

## License

- **Name**: MIT
- **Details**: [View the license](https://choosealicense.com/licenses/mit/)
- **Additional Terms**:
  - Credit appreciated: Yes
  - Adult content allowed: No
  - Free copy required: No

## Notes

This plugin is a **free** resource available for both commercial and non-commercial use.

Compatible with RPG Maker MZ.

Plugin parameters are available in English.

---
