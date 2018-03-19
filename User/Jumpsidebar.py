import sublime
import sublime_plugin

# focus_side_bar

class JumpsidebarCommand(sublime_plugin.TextCommand):
    def run(self, window):
        if not self.view.window().is_sidebar_visible():
            self.view.window().set_sidebar_visible(True)
        self.view.window().run_command('reveal_in_side_bar')
        self.view.window().run_command('focus_side_bar')



