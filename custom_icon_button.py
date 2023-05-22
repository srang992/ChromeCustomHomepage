import flet as ft


class CustomIconButton(ft.UserControl):
    def __init__(self, icon: str, color: str = None, on_click=None):
        super().__init__()
        self.icon = icon
        self.color = color
        self.on_click = on_click

    def build(self):
        if self.icon.endswith("svg") or self.icon.endswith("png"):
            return ft.Container(
                content=ft.Image(
                    src=self.icon,
                    width=24,
                    height=24,
                    color=self.color,
                ),
                on_click=self.on_click
            )
        else:
            return ft.IconButton(
                icon=self.icon,
                icon_color=self.color,
                on_click=self.on_click
            )
