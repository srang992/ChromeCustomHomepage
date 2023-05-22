import flet as ft


class CustomIcon(ft.UserControl):
    def __init__(self, icon, size, color=None):
        super().__init__()
        self.icon = icon
        self.size = size
        self.color = color

    def build(self):
        return ft.Image(
            src=self.icon,
            width=self.size,
            height=self.size,
            color=self.color
        )
