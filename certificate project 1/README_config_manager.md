# User Configuration Manager

A simple Python module for managing user settings (like theme, language, notifications, etc.) stored as key-value pairs in a dictionary. Supports adding, updating, deleting, and viewing settings, with all keys and values automatically normalized to lowercase.

## Features

- Add new settings, with protection against overwriting existing keys
- Update existing settings safely (won't create new keys by mistake)
- Delete settings by key
- View all current settings in a readable, formatted list
- Keys and values are automatically lowercased for consistency

## Requirements

- Python 3.6+ (uses f-strings)
- No external dependencies

## File

`Build a User Configuration Manager.py`

> Note: Because the filename contains spaces, it can't be directly imported with a normal `import` statement. Either run the script directly, or rename the file (e.g. to `config_manager.py`) if you want to import its functions into another script.

## Usage

Example usage if run directly, or copied into another script:

```python
settings = {
    "theme": "light",
    "language": "english",
    "notifications": "enabled"
}

# Add a new setting
print(add_setting(settings, ("font_size", "medium")))
# Setting 'font_size' added with value 'medium' successfully!

# Try adding a setting that already exists
print(add_setting(settings, ("theme", "dark")))
# Setting 'theme' already exists! Cannot add a new setting with this name.

# Update an existing setting
print(update_setting(settings, ("theme", "dark")))
# Setting 'theme' updated to 'dark' successfully!

# Try updating a setting that doesn't exist
print(update_setting(settings, ("volume", "high")))
# Setting 'volume' does not exist! Cannot update a non-existing setting.

# Delete a setting
print(delete_setting(settings, "notifications"))
# Setting 'notifications' deleted successfully!

# View all settings
print(view_settings(settings))
```

## Functions

| Function | Description |
|---|---|
| `add_setting(settings, setting)` | Adds a new `(key, value)` pair to `settings`. Fails if the key already exists. |
| `update_setting(settings, setting)` | Updates an existing `(key, value)` pair. Fails if the key does not exist. |
| `delete_setting(settings, key)` | Removes a setting by key. Returns a message if the key isn't found. |
| `view_settings(settings)` | Returns a formatted string listing all current settings, with each key capitalized. |

### Parameter notes

- `setting` (used in `add_setting` and `update_setting`) is expected to be a tuple or list of `(key, value)`.
- `key` (used in `delete_setting`) is a plain string.
- All keys and values are lowercased internally before being stored or compared, so lookups are case-insensitive.

## Example output of `view_settings`

```
Current User Settings:
Theme: light
Language: english
Notifications: enabled
```

## Notes / Limitations

- `add_setting` and `update_setting` expect exactly a 2-item tuple/list (`key, value = setting`) — passing anything else will raise a `ValueError`.
- No validation is done on allowed setting names or values (e.g. no check that `"theme"` is one of `"light"`/`"dark"`); any string key/value is accepted.
- Settings are stored only in memory (the `test_settings` dictionary) — there is no persistence to a file or database.
