import sublime, sublime_plugin
import os
from glob import iglob

class SelectColorSchemeCommand(sublime_plugin.WindowCommand):
    def run(self):
        color_schemes = self.get_color_schemes()

        def on_done(index):
            if index >= 0:
                self.set_color_scheme(color_schemes[index][1])

        self.window.show_quick_panel(color_schemes, on_done)

    # [[name, path]...]
    def get_color_schemes(self):
        pattern = os.path.join(sublime.packages_path(), '*', '*.tmTheme')
        color_schemes = []
        for filepath in iglob(pattern):
            name = os.path.basename(filepath)
            path = filepath.replace(sublime.packages_path(), 'Packages')
            color_schemes.append([name, path])
        return color_schemes

    def set_color_scheme(self, color_scheme_path):
        self.load_settings().set('color_scheme', color_scheme_path)
        sublime.save_settings('Preferences.sublime-settings')

    def load_settings(self):
        return sublime.load_settings('Preferences.sublime-settings')