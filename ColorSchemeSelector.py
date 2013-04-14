import sublime, sublime_plugin
import os
from glob import iglob
from random import choice

class SelectColorSchemeCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        color_schemes = self.get_color_schemes()

        def on_done(index):
            if index >= 0:
                self.set_color_scheme(color_schemes[index][1])
        
        if 'random' in kwargs:
            self.set_color_scheme(choice(color_schemes)[1])
        elif 'random' in kwargs:
            self.move_color_scheme(kwargs['direction'], color_schemes)
        else:
            self.window.show_quick_panel(color_schemes, on_done)

    def move_color_scheme(self, direction, color_schemes):
        current_scheme = self.load_settings().get('color_scheme')
        current_index = [c[1] for c in color_schemes].index(current_scheme)
        if direction == 'previous':
            index = current_index - 1
        elif direction == 'next':
            index = current_index + 1 if current_index < len(color_schemes) else 0
        else:
            raise ValueError
        self.set_color_scheme(color_schemes[index][1])

    # [[name, path]...]
    def get_color_schemes(self):
        color_schemes = []
        for root, dirs, files in os.walk(sublime.packages_path()):
            for fl in files:
                if fl.endswith('.tmTheme'):
                    name = os.path.basename(fl).replace('.tmTheme', '')
                    filepath = os.path.join(root, fl)
                    path = filepath.replace(sublime.packages_path(), 'Packages')
                    color_schemes.append([name, path])
        return color_schemes

    def set_color_scheme(self, color_scheme_path):
        self.load_settings().set('color_scheme', color_scheme_path)
        sublime.save_settings('Preferences.sublime-settings')
        sublime.status_message('SelectColorScheme: ' + color_scheme_path)

    def load_settings(self):
        return sublime.load_settings('Preferences.sublime-settings')
