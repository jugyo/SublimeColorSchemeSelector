import sublime, sublime_plugin
import os
from glob import iglob
from random import choice

class SelectColorSchemeCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        color_schemes = sublime.find_resources("*.tmTheme")

        def on_done(index):
            if index >= 0:
                self.set_color_scheme(color_schemes[index])

        if 'random' in kwargs:
            self.set_color_scheme(choice(color_schemes))
        elif 'direction' in kwargs:
            self.move_color_scheme(color_schemes, kwargs['direction'])
        else:
            items = [[os.path.basename(_), _] for _ in color_schemes]
            if int(sublime.version()) > 3000:
                self.window.show_quick_panel(items, on_done, 0, self.current_scheme_index(color_schemes), on_done)
            else:
                self.window.show_quick_panel(items, on_done, 0, self.current_scheme_index(color_schemes))

    def path_to_color_scheme(self, name):
        return "Packages/Color Scheme - Default/%s.tmTheme" % name

    def move_color_scheme(self, color_schemes, direction):
        current_index = self.current_scheme_index(color_schemes)
        if direction == 'previous':
            index = current_index - 1
        elif direction == 'next':
            index = current_index + 1 if current_index < len(color_schemes) else 0
        else:
            raise ValueError
        self.set_color_scheme(color_schemes[index])

    def current_scheme_index(self, color_schemes):
        current_scheme = self.load_settings().get('color_scheme')
        return [c for c in color_schemes].index(current_scheme)

    def set_color_scheme(self, color_scheme_path):
        self.load_settings().set('color_scheme', color_scheme_path)
        sublime.save_settings('Preferences.sublime-settings')
        sublime.status_message('SelectColorScheme: ' + color_scheme_path)

    def load_settings(self):
        return sublime.load_settings('Preferences.sublime-settings')
