import os
import configparser

from mode_helper import cliui

#TODO: make the config import from;
#        1) standard system-wide directory
#        2) ~/.mode_helper.cfg  (DONE)
#        3) from command -c  (DONE)

def get_config(alt_config,pass_dir):
    config = configparser.ConfigParser()

    alt_config = "" if alt_config == False else alt_config

    config.read([os.path.expanduser('~/.mode_helper.cfg'),
                 alt_config])

    if pass_dir != False:
        config.set('pass','directory',pass_dir)
    return config

def gen_default_conf():
    config = configparser.RawConfigParser()
    config.add_section('pass')
    config.set('pass','directory',os.path.expanduser('~/.password-store/'))

    if os.path.isfile('.mode_helper.cfg'):
            if not cliui.override_file():
                raise IOError(
                    'Error: Config file already exists in this directory!')

    with open('.mode_helper.cfg','w') as configfile:
        config.write(configfile)

    if not os.path.isfile('.mode_helper.cfg'):
        raise IOError('Error: File not created!')

    return 0
