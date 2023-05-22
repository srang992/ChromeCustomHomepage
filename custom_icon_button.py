import flet as ft


class CustomIconButton(ft.UserControl):
    def __init__(self, icon: str, color: str = None, url=None):
        super().__init__()
        self.icon = icon
        self.color = color
        self.url = url

    def build(self):
        return ft.Container(
            content=ft.Image(
                src=self.icon,
                width=24,
                height=24,
                color=self.color,
            ),
            url=self.url,
        )
