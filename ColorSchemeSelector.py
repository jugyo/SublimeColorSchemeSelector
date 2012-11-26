import sublime, sublime_plugin
import os

class SelectColorSchemeCommand(sublime_plugin.WindowCommand):
    def run(self):
        color_schemes = self.get_color_schemes()

        def on_done(index):
            if index >= 0:
                self.set_color_scheme(color_schemes[index])

        self.window.show_quick_panel(color_schemes, on_done)

    def get_color_schemes(self):
        current_color_scheme = self.load_settings().get('color_scheme')
        files = filter(lambda f: f.endswith('tmTheme'), os.listdir(self.color_scheme_dir()))
        return files

    def set_color_scheme(self, color_scheme):
        color_scheme_file = os.path.join(self.color_scheme_dir(), color_scheme)
        self.load_settings().set('color_scheme', color_scheme_file)
        sublime.save_settings('Preferences.sublime-settings')

    def color_scheme_dir(self):
        return os.path.join(sublime.packages_path(), "Color Scheme - Default")

    def load_settings(self):
        return sublime.load_settings('Preferences.sublime-settings')