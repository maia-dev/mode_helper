import sys
import argparse

def parse_args(args):
    parser = argparse.ArgumentParser(
        description='A visual menu for i3wm modes'
    )

    parser.add_argument('-p','--pass-directory',
                        nargs = 1,
                        help = 'Overrides pass directory.',
    )
    parser.add_argument('-s', '--shortcuts',
                        nargs = 2,
                        metavar = 'STRING',
                        help = "Defines the shortcuts and it's \
                        descriptions.",
    )
    parser.add_argument('-c', '--config',
                        nargs = 1,
                        metavar = 'CONFIGFILE',
                        help = 'Specifies an alternate configuration \
                        file path.',
    )
    parser.add_argument('-t','--target-directory',
                        nargs = 1,
                        metavar = 'TARGET-PASS-DIR',
                        help = 'Target passwordstore directory.',
    )
    parser.add_argument('-T', '--template',
                        action='store_true',
                        help = 'Generates a template for the i3wm mode.',
    )
    parser.add_argument('-n','--notification',
                        action='store_true',
                        help = 'Enable notification.',
    )
    parser.add_argument('-r', '--r-shortcuts',
                        action='store_true',
                        help = 'Prints the recommended shortcuts.',
    )
    parser.add_argument('-g', '--gen-config',
                        action='store_true',
                        help = 'Creates the default config in the \
                        current directory.',
    )

    args = parser.parse_args(args)
    arg_dict = create_arg_dict(args)

    return arg_dict


def create_arg_dict(args):
    try:
        shortcuts_dict = get_shortcuts_dict(args.shortcuts)

        config = args.config[0] if args.config != None else False
        pass_dir = args.pass_directory[0] if args.pass_directory != None else False
        target_dir = args.target_directory[0] if args.target_directory != None else False

        arg_dict = { "config": config,
                     "notification": args.notification,
                     "pass_dir": pass_dir,
                     "r_shortcuts": args.r_shortcuts,
                     "shortcuts": shortcuts_dict,
                     "target_dir": target_dir,
                     "template": args.template,
                     "gen_config": args.gen_config,
        }

        return arg_dict
    except Exception as err:
        sys.exit(err)
        pass


def get_shortcuts_dict(shortcuts_list):
    shortcuts_dict = None
    if shortcuts_list != None:
        shortcuts = shortcuts_list[0].split(' ')
        descriptions = shortcuts_list[1].split(' ')
        if len(shortcuts) == len(descriptions):
            shortcuts_dict = dict(zip(shortcuts,descriptions))
        else:
            raise ValueError(
                'Error: Diferent number of shortcuts and descriptions')
    else:
        shortcuts = None

    return shortcuts_dict
