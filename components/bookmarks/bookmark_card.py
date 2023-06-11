import flet as ft
from custom_flet.components.custom_icon import CustomIcon


class BookmarkCard(ft.UserControl):

    bookmark_card_content = ft.Ref[ft.Row]()

    def __init__(self, icon, text, icon_size, color=None, url=None, col=None):
        super().__init__()
        self.icon = icon
        self.text = text
        self.icon_size = icon_size
        self.color = color
        self.url = url
        self.col = col

    def build(self):
        return ft.ElevatedButton(
            content=ft.Row(
                [
                    CustomIcon(
                        icon=self.icon,
                        size=self.icon_size,
                        color=self.color
                    ),
                    ft.Text(self.text, size=16, font_family="Alkatra", no_wrap=False)
                ],
            ),
            style=ft.ButtonStyle(
                padding=18,
                shape=ft.RoundedRectangleBorder(radius=5),
            ),
            url=self.url,
            col=self.col,
        )

