# cura-settings-in-gcode
Extract cura settings from gcode file.

# Usage
See help message.
```
$ cura-settings-in-gcode.py --help
usage: cura-settings-in-gcode.py [-h] cura_gcode_file

extract cura settings from gcode file

positional arguments:
  cura_gcode_file

optional arguments:
  -h, --help       show this help message and exit
```

# Example
```
$ cura-settings-in-gcode.py ./example.gcode
X-Generator: Cura_SteamEngine 4.4.1
Content-Type: application/x-yaml

SETTING_3:
  extruder_quality:
  - general:
      definition: custom
      name: 'Fine #2'
      version: '4'
    metadata:
      position: '0'
      quality_type: normal
      type: quality_changes
    values:
      skirt_line_count: '10'
  - general:
      definition: fdmprinter
      name: 'Fine #2'
      version: '4'
    metadata:
      position: '1'
      quality_type: normal
      type: quality_changes
    values: {}
  - general:
      definition: fdmprinter
      name: 'Fine #2'
      version: '4'
    metadata:
      position: '2'
      quality_type: normal
      type: quality_changes
    values: {}
  - general:
      definition: fdmprinter
      name: 'Fine #2'
      version: '4'
    metadata:
      position: '3'
      quality_type: normal
      type: quality_changes
    values: {}
  - general:
      definition: fdmprinter
      name: 'Fine #2'
      version: '4'
    metadata:
      position: '4'
      quality_type: normal
      type: quality_changes
    values: {}
  - general:
      definition: fdmprinter
      name: 'Fine #2'
      version: '4'
    metadata:
      position: '5'
      quality_type: normal
      type: quality_changes
    values: {}
  - general:
      definition: fdmprinter
      name: 'Fine #2'
      version: '4'
    metadata:
      position: '6'
      quality_type: normal
      type: quality_changes
    values: {}
  - general:
      definition: fdmprinter
      name: 'Fine #2'
      version: '4'
    metadata:
      position: '7'
      quality_type: normal
      type: quality_changes
    values: {}
  global_quality:
    general:
      definition: custom
      name: 'Fine #2'
      version: '4'
    metadata:
      quality_type: normal
      type: quality_changes
    values:
      adhesion_type: skirt
      layer_height_0: '0.15'
      support_enable: 'True'
```
