# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401
from libqtile import widget

from libqtile import bar, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os



mod = "mod4"
terminal = "urxvt"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "b", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "n", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),desc="Spawn a command using a prompt widget"),

    # My Custom Keys
    Key([mod], "space", lazy.spawn("rofi -modi drun -show drun"), desc="rofi"),
    Key([mod], "Right", lazy.screen.next_group(), desc="Next Workspace"),
    Key([mod], "Left", lazy.screen.prev_group(), desc="Previous Workspace"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle Focused Floating"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layout_theme = {"border_width": 1,
                "margin": 18,
                "border_focus": "#ECBFBD",
                "border_normal": "#2D293B"
                }


layouts = [
    # layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    layout.Max(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Iosevka Nerd Font Bold',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active='#000000',
                    inactive='#FFFFFF',
                    background="#A4B9EF",
                    rounded=False,
                    highlight_color='#000000',
                    highlight_method='border',
                    this_current_screen_border ='#000000',
                    this_screen_border ='#000000',
                    disable_drag=True,
                ),
                 widget.TextBox(
                    text='',
                    foreground='#A4B9EF',
                    background='#EADDA0',
                    font='Iosevka Nerd Font Mono',
                    fontsize=20,
                    padding=0,
                ),
                widget.WindowName(
                    background="#EADDA0",
                    foreground="#3E4058",
                ),
                 widget.TextBox(
                    text='',
                    foreground='#C6AAE8',
                    background='#EADDA0',
                    font='Iosevka Nerd Font Mono',
                    fontsize=20,
                    padding=0,
                ),
                widget.Mpd2(
                    background="#C6AAE8",
                    foreground="#3E4058",
                    mouse_buttons={1: 'toggle', 3: 'stop', 4: 'previous', 5: 'next'},
                    play_states={'pause': '⏸', 'play': '▶', 'stop': '■'},
                ),
                widget.TextBox(
                    text='',
                    foreground='#B3E1A3',
                    background='#C6AAE8',
                    font='Iosevka Nerd Font Mono',
                    fontsize=20,
                    padding=0,
                ),
                widget.Volume(
                    background="#B3E1A3",
                    foreground="#3E4058",
                    fmt="VOL {}"
                ),
                widget.TextBox(
                    text='',
                    foreground='#E28C8C',
                    background='#B3E1A3',
                    font='Iosevka Nerd Font Mono',
                    fontsize=20,
                    padding=0,
                ),
                widget.Memory(
                    background="#E28C8C",
                    foreground="#3E4058",
                    fmt="{}",
                    padding=4,
                ),
                widget.TextBox(
                    text='',
                    foreground='#9DDDCB',
                    background='#E28C8C',
                    font='Iosevka Nerd Font Mono',
                    fontsize=20,
                    padding=0,
                ),
                widget.Systray(
                    background='#9DDDCB',
                    icon_size=20,
                ),
                widget.TextBox(
                    text=' ',
                    foreground='#EADDA0',
                    background='#9DDDCB',
                    font='Iosevka Nerd Font Mono',
                    fontsize=20,
                    padding=0,
                ),
                widget.Clock(
                    fmt=" {} ",
                    background="#EADDA0",
                    foreground="#3E4058",
                    format='%a %I:%M %p',
                ),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
], **layout_theme)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

autostart = [
    "feh --bg-fill ~/Pictures/catpuccin/minimalistic/black5_unicat.png",
    "udiskie &",
    "nm-applet &",
    "dunst &",
    "mpd &",
    "/usr/lib/polkit-kde-authentication-agent-1 &",
]

for x in autostart:
    os.system(x)
