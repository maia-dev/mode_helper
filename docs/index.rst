===========
mode_helper
===========

Name
====
    mode_helper - A visual menu for i3wm modes.

Description
===========
    A visual helper for i3wm modes, inspired by spacemacs.
    This package was designed to be used as an interface for
    passwordstore but can be used to create menus for any mode.

Usage
=====
    mode_helper [-c CONFIGFILE] [-s SHORTCUTS DESCRIPTIONS]
                [-n] [-t] [-r] [-p PATH] [-h] [-t TARGET-PASS-DIR]

Options
=======

    **-c**
        Specifies an alternate configuration file path.

    **-s** <shortcuts string> <descriptions string>
        Defines the shortcuts and it's descriptions, both string must have the same
        number of elements.

    **-n**
        Enables notification.

    **-T**
        Generate a template for the i3wm mode with the correct shortcuts.

    **-r**
        Prints the recommended shortcuts to use.

    **-p**
        Overrides pass directory path (should be defined in the config file).
        defaults to ~/.password-store

    **-t**
        Specifies the target password-store directory (relative to password-store path).

    **-g**
        Creates the default configuration file in the current directory

    **-h --help**
        Display the help menu

Examples
========

    mode_helper -s "s1 s2" "d1 d2"
       generates a window that displays the s1 -> d1; s2 -> d2 shortcuts.

    mode_helper linux/
       generates a windows with the shortcuts for the directory pass/linux.
