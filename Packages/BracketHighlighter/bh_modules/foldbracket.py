import bh_plugin
import sublime


class FoldBrackets(bh_plugin.BracketPluginCommand):
    def run(self, edit, name):
        """
        Fold the content between the bracket
        """

        content = sublime.Region(self.left.end, self.right.begin)
        new_content = [content]
        if content.size() > 0:
            if self.view.fold(content) is False:
                new_content = self.view.unfold(content)
        self.selection = new_content


def plugin():
    return FoldBrackets
