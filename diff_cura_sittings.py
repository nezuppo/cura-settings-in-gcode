#!/usr/bin/env python3

import sys
from difflib import unified_diff

import cura_settings_in_gcode as cs

def main():
    import argparse

    parser = argparse.ArgumentParser(description='compare cura settings in gcode files line by line')
    parser.add_argument('cura_gcode_file1')
    parser.add_argument('cura_gcode_file2')
    args = parser.parse_args()

    settings1 = cs.cura_settings_in_gcode(args.cura_gcode_file1).splitlines(keepends=True)
    settings2 = cs.cura_settings_in_gcode(args.cura_gcode_file2).splitlines(keepends=True)

    sys.stdout.writelines(
        unified_diff(
            settings1,
            settings2,
            fromfile=args.cura_gcode_file1,
            tofile=args.cura_gcode_file2,
            n=max(len(settings1), len(settings2))
        )
    )

if __name__ == '__main__':
    main()

