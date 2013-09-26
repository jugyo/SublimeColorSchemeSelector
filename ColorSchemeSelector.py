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
            self.move_color_scheme(kwargs['direction'])
        else:
            self.window.show_quick_panel(color_schemes, on_done, 0, self.current_scheme_index(), on_done)

    def path_to_color_scheme(self, name):
        return "Packages/Color Scheme - Default/%s.tmTheme" % name

    def move_color_scheme(self, direction):
        current_index = self.current_scheme_index()
        if direction == 'previous':
            index = current_index - 1
        elif direction == 'next':
            index = current_index + 1 if current_index < len(self.DEFUALT_COLOR_SCHEMES) else 0
        else:
            raise ValueError
        self.set_color_scheme(self.path_to_color_scheme(self.DEFUALT_COLOR_SCHEMES[index]))

    def current_scheme_index(self):
        current_scheme = self.load_settings().get('color_scheme')
        return [self.path_to_color_scheme(c) for c in self.DEFUALT_COLOR_SCHEMES].index(current_scheme)

    def set_color_scheme(self, color_scheme_path):
        self.load_settings().set('color_scheme', color_scheme_path)
        sublime.save_settings('Preferences.sublime-settings')
        sublime.status_message('SelectColorScheme: ' + color_scheme_path)

    def load_settings(self):
        return sublime.load_settings('Preferences.sublime-settings')
