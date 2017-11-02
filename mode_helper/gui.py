import gi
import os
import subprocess
import signal

gi.require_version('Gtk','3.0')
from gi.repository import Gtk, Gdk

class Window(Gtk.Window):
    def __init__(self, shortcuts, config):

        Gtk.Window.__init__(self, title='mode_helper')

        #set size and position on screen
        screen = Gdk.Screen.get_default()
        window_height = calc_window_height(len(shortcuts),
                                           int(config['gui']['line_height']))
        i3_bar_height = int(config['gui']['i3_bar_height'])
        bottom_px = screen.get_height() - i3_bar_height - window_height

        self.set_default_size(screen.get_width(),
                              window_height)
        self.move(0,bottom_px)
        self.set_decorated(False)

        #loading some css from data
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(b".background{\
        background-color: rgba(32,36,44,0.999);}")
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        #setting up grid
        grid = Gtk.Grid(column_homogeneous=True,
                        row_homogeneous=False)
        self.add(grid)

        curr_row = 0
        curr_col = 0
        for i,(s,d) in enumerate(shortcuts.items()):
             button = Gtk.Button("")

             label = Gtk.Label()
             label.set_markup("<span font_desc='Ubuntu 10'><span foreground='#80da25'>{}</span><span foreground='#458588'> -> </span><span>{}</span></span>".format(s,d))

             #set button label and alignment
             for child in button.get_children():
                 child.set_label(label.get_label())
                 child.set_halign(Gtk.Align.START)
                 child.set_use_markup(True)

             button.set_relief(Gtk.ReliefStyle.NONE)

             #if s == "Ret/Esc":
             #    grid.attach(button,4, curr_row+1,1,1)
             #    self.move(0,bottom_px-20)
             #else:
             grid.attach(button,curr_col % 5, curr_row,1,1)

             curr_col +=1
             if (i+1) % 5 == 0:
                 curr_row +=1


#calculates the height of the windows by spliting the number of
# shortcuts/description in x lines of 5 columns and multiplying
# by the line_height
def calc_window_height(num_elements, line_height = 30):
    lines = 0
    #this is a hack for weird beheviour (not showing 1 line windows)
    if num_elements <= 10:
        lines = 2
    else:
        for element in range(0,num_elements):
            if element % 5 == 0:
                lines += 1
    return lines * line_height

def kill_window_if_exists():
    p = subprocess.Popen(['ps','-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()
    found = 0
    for line in out.splitlines():
        if 'mode_helper' in str(line):
            if found < 1:
                found +=1
                pid = int(line.split(None,1)[0])
            else:
                os.kill(pid, signal.SIGKILL)

def draw_window(shortcuts,config):

    kill_window_if_exists()

    win = Window(shortcuts,config)
    win.connect('delete-event', Gtk.main_quit)
    win.show_all()
    Gtk.main()
