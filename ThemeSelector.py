import sublime, sublime_plugin
import os

class SelectThemeCommand(sublime_plugin.WindowCommand):
    def run(self):
        themes = self.get_themes()

        def on_done(index):
            if index >= 0:
                self.set_theme(themes[index])

        self.window.show_quick_panel(themes, on_done)

    def get_themes(self):
        current_theme = self.load_settings().get('color_scheme')
        files = filter(lambda f: f.endswith('tmTheme'), os.listdir(self.theme_dir()))
        return files

    def set_theme(self, theme):
        theme_file = os.path.join(self.theme_dir(), theme)
        self.load_settings().set('color_scheme', theme_file)
        sublime.save_settings('Preferences.sublime-settings')

    def theme_dir(self):
        return os.path.join(sublime.packages_path(), "Color Scheme - Default")

    def load_settings(self):
        return sublime.load_settings('Preferences.sublime-settings')