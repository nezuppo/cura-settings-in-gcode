#!/usr/bin/env python3

import re
import json
import yaml
import configparser
from collections import defaultdict

def _represent_str(dumper, instance):
    if "\n" in instance:
        return dumper.represent_scalar('tag:yaml.org,2002:str', instance, style='|')
    else:
        return dumper.represent_scalar('tag:yaml.org,2002:str', instance)
yaml.add_representer(str, _represent_str)

def get_generator(file):
    """
    get generator and skip to end of gcode
    """

    reprog_generator = re.compile(r'^ *; *Generated with +(?P<generator>.+)$')
    reprog_eog = re.compile(r'^ *; *End of Gcode *$')

    generator = None
    for line in file:
        if reprog_eog.search(line):
            break

        match = reprog_generator.search(line)
        if match is not None:
            generator = match.group('generator').rstrip()

    return generator

def get_settings(file):
    reprog_setting = re.compile(r'^ *; *(?P<id>SETTING_\d+) (?P<str>.+)$')
    settings = defaultdict(str)
    for line in file:
        match = reprog_setting.search(line)
        if match is None:
            break

        settings[match.group('id')] += match.group('str')

    reprog_replace = re.compile(r'\\\\n')
    for id, raw_str in settings.items():
        settings[id] = json.loads(
            reprog_replace.sub(r'\\n', raw_str)
        )

    return dict(settings)

def init2dict(settings):
    if isinstance(settings, dict):
        converted = {}
        for name, sub_settings in settings.items():
            converted[name] = init2dict(sub_settings)
        return converted
    if isinstance(settings, list):
        converted = []
        for sub_settings in settings:
            converted.append(init2dict(sub_settings))
        return converted
    if isinstance(settings, str):
        config = configparser.ConfigParser()
        config.read_string(settings)

        converted = {}
        for section_name, section_proxy in config.items():
            if section_name == 'DEFAULT' and dict(section_proxy) == {}:
                continue
            converted[section_name] = dict(section_proxy)

        return converted

    raise Exception(settings, type(settings))

def cura_settings_in_gcode(filename):
    with open(filename) as file:
        generator = get_generator(file)
        settings = get_settings(file)

    settings = init2dict(settings)

#
    """ <
    str_settings = ''
    str_settings += 'X-Generator: {}\n'.format(generator if generator else 'unknown')
    str_settings += 'Content-Type: application/x-yaml\n'
    str_settings += '\n'
    str_settings += yaml.dump(settings, default_flow_style=False)
    """

    str_settings = ''.join([
        'X-Generator: {}\n'.format(generator if generator else 'unknown'),
        'Content-Type: application/x-yaml\n',
        '\n'
    ])
    str_settings += yaml.dump(settings, default_flow_style=False)

    return str_settings

def main():
    import argparse

    parser = argparse.ArgumentParser(description='extract cura settings from gcode file')
    parser.add_argument('cura_gcode_file')
    args = parser.parse_args()

    str_settings = cura_settings_in_gcode(args.cura_gcode_file)
    print(str_settings, end='')

if __name__ == '__main__':
    main()
