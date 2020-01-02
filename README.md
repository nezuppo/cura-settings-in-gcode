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
  - |+
    [general]
    version = 4
    name = Fine #2
    definition = custom

    [metadata]
    quality_type = normal
    type = quality_changes
    position = 0

    [values]
    skirt_line_count = 10

  - |+
    [general]
    version = 4
    name = Fine #2
    definition = fdmprinter

    [metadata]
    quality_type = normal
    type = quality_changes
    position = 1

    [values]

  - |+
    [general]
    version = 4
    name = Fine #2
    definition = fdmprinter

    [metadata]
    quality_type = normal
    type = quality_changes
    position = 2

    [values]

  - |+
    [general]
    version = 4
    name = Fine #2
    definition = fdmprinter

    [metadata]
    quality_type = normal
    type = quality_changes
    position = 3

    [values]

  - |+
    [general]
    version = 4
    name = Fine #2
    definition = fdmprinter

    [metadata]
    quality_type = normal
    type = quality_changes
    position = 4

    [values]

  - |+
    [general]
    version = 4
    name = Fine #2
    definition = fdmprinter

    [metadata]
    quality_type = normal
    type = quality_changes
    position = 5

    [values]

  - |+
    [general]
    version = 4
    name = Fine #2
    definition = fdmprinter

    [metadata]
    quality_type = normal
    type = quality_changes
    position = 6

    [values]

  - |+
    [general]
    version = 4
    name = Fine #2
    definition = fdmprinter

    [metadata]
    quality_type = normal
    type = quality_changes
    position = 7

    [values]

  global_quality: |+
    [general]
    version = 4
    name = Fine #2
    definition = custom

    [metadata]
    quality_type = normal
    type = quality_changes

    [values]
    adhesion_type = skirt
    layer_height_0 = 0.15
    support_enable = True

...
```
