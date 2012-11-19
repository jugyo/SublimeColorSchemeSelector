import sublime, sublime_plugin
import os

class SelectThemeCommand(sublime_plugin.WindowCommand):
    def run(self):
        themes = self.get_themes()

        def on_done(index):
            if index < 0:
              return
            theme = themes[index]
            self.set_theme(theme)

        self.window.show_quick_panel(themes, on_done)

    def get_themes(self):
        settings = sublime.load_settings('Preferences.sublime-settings')
        current_theme = settings.get('color_scheme')
        files = os.listdir(os.path.join(sublime.packages_path(), 'Color Scheme - Default'))
        files = filter(lambda f: f.endswith('tmTheme'), files)
        return files

    def set_theme(self, theme):
        theme_path = os.path.join("Packages", "Color Scheme - Default", theme)
        settings = sublime.load_settings('Preferences.sublime-settings')
        settings.set('color_scheme', theme_path)
        sublime.save_settings('Preferences.sublime-settings')
