import os
import sys
from mode_helper.args import parse_args
from mode_helper.config import get_config, gen_default_conf
from mode_helper.gui import draw_window

#TODO: get rid of sys.exit(msg), make a good structure instead

def main():
    print(sys.argv[1:])

    arg_dict = parse_args(sys.argv[1:])

    for k,v in arg_dict.items():
       print("{}: {}".format(k,v))

    #if -g: generates the config file and exits
    if arg_dict['gen_config'] != False:
        try:
            gen_default_conf()
            msg = 'Configuration file created: {}/.mode_helper.cfg'.format(
                os.getcwd())
        except Exception as err:
            msg = err
        sys.exit(msg)
    else:

        config = get_config(alt_config = arg_dict['config'],
                            pass_dir = arg_dict['pass_dir'])

        if arg_dict['shortcuts'] or arg_dict['target_dir']:
            if arg_dict['shortcuts']:
                #TODO: add the esc/ret to the end
                shortcuts = arg_dict['shortcuts']
            else:
                #TODO: generate shortcuts from target_dir
                shortcuts = {}

            draw_window(shortcuts,config)

        if arg_dict['r_shortcuts'] or arg_dict['template']:
            #TODO: generate the outputs here
            pass


    return 0
