import flet as ft
from components.others.icon_control.custom_icon import CustomIcon


class BookmarkCard(ft.UserControl):
    def __init__(self, icon, text, icon_size, color=None, url=None):
        super().__init__()
        self.icon = icon
        self.text = text
        self.icon_size = icon_size
        self.color = color
        self.url = url

    def build(self):
        return ft.Container(
            content=ft.ElevatedButton(
                content=ft.Row(
                    [
                        CustomIcon(
                            icon=self.icon,
                            size=self.icon_size,
                            color=self.color
                        ),
                        ft.Text(self.text, size=16, font_family="Alkatra")
                    ],
                    # wrap=True,
                    width=200
                ),
                style=ft.ButtonStyle(
                    padding=18,
                    shape=ft.RoundedRectangleBorder(radius=5),
                ),
                url=self.url
            ),
        )
