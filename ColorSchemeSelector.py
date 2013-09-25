import sublime, sublime_plugin
import os
from glob import iglob
from random import choice

class SelectColorSchemeCommand(sublime_plugin.WindowCommand):
    DEFUALT_COLOR_SCHEMES = [
        "All Hallow's Eve",
        "Amy",
        "Blackboard",
        "Cobalt",
        "Dawn",
        "Eiffel",
        "Espresso Libre",
        "IDLE",
        "LAZY",
        "Mac Classic",
        "MagicWB (Amiga)",
        "Monokai Bright",
        "Monokai",
        "Pastels on Dark",
        "Slush & Poppies",
        "Solarized (Dark)",
        "Solarized (Light)",
        "SpaceCadet",
        "Sunburst",
        "Twilight",
        "Zenburnesque",
        "iPlastic"
    ]

    def run(self, **kwargs):
        color_schemes = self.DEFUALT_COLOR_SCHEMES

        def on_done(index):
            if index >= 0:
                self.set_color_scheme(self.path_to_color_scheme(color_schemes[index]))

        if 'random' in kwargs:
            self.set_color_scheme(self.path_to_color_scheme(choice(color_schemes)))
        elif 'direction' in kwargs:
            self.move_color_scheme(kwargs['direction'], color_schemes)
        else:
            self.window.show_quick_panel(color_schemes, on_done)

    def path_to_color_scheme(self, name):
        return "Packages/Color Scheme - Default/%s.tmTheme" % name

    def move_color_scheme(self, direction, color_schemes):
        current_scheme = self.load_settings().get('color_scheme')
        current_index = [self.path_to_color_scheme(c) for c in color_schemes].index(current_scheme)
        if direction == 'previous':
            index = current_index - 1
        elif direction == 'next':
            index = current_index + 1 if current_index < len(color_schemes) else 0
        else:
            raise ValueError
        self.set_color_scheme(self.path_to_color_scheme(color_schemes[index]))

    def set_color_scheme(self, color_scheme_path):
        self.load_settings().set('color_scheme', color_scheme_path)
        sublime.save_settings('Preferences.sublime-settings')
        sublime.status_message('SelectColorScheme: ' + color_scheme_path)

    def load_settings(self):
        return sublime.load_settings('Preferences.sublime-settings')
