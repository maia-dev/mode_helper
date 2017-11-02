import os
import sys
from mode_helper.args import parse_args
from mode_helper.config import get_config, gen_default_conf

def main():
    print(sys.argv[1:])

    arg_dict = parse_args(sys.argv[1:])

    for k,v in arg_dict.items():
       print("{}: {}".format(k,v))

    #if -g generates the config file and exits
    if arg_dict['gen_config'] != False:
        try:
            gen_default_conf()
            msg = 'Configuration file created: {}/.mode_helper.cfg'.format(
                os.getcwd())
        except Exception as err:
            msg = err

        sys.exit(msg)

    config = get_config(alt_config = arg_dict['config'],
                        pass_dir = arg_dict['pass_dir'])

    print("pass_dir: {}".format(config['pass']['directory']))

    return 0
