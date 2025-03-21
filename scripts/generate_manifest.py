import os
import json
from pathlib import Path

plugins_dir = Path('plugins')
manifest = []

for plugin_dir in plugins_dir.iterdir():
    if plugin_dir.is_dir():
        json_file = plugin_dir / 'plugin.json'
        if json_file.exists():
            with open(json_file) as f:
                data = json.load(f)
                data['path'] = str(plugin_dir)
                manifest.append(data)

with open('manifest.json', 'w') as f:
    json.dump(manifest, f, indent=2)