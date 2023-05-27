import flet as ft
import custom_icons


class PageHeader(ft.UserControl):

    theme_icon = ft.Ref[ft.IconButton]()
    dark_icon = "dark_mode_outlined"
    light_icon = "light_mode_outlined"

    def __init__(self, page):
        super().__init__()
        self.page = page

    def on_click_button(self, _):
        self.page.theme_mode = "light" if self.page.theme_mode == "dark" else "dark"
        self.theme_icon.current.icon = self.light_icon if self.page.theme_mode == "light" else self.dark_icon
        self.update()
        self.page.update()

    def build(self):
        return ft.Column(
            [
                ft.Image(custom_icons.my_logo, width=200, height=100),
                ft.Row(
                    [
                        ft.IconButton(
                            icon=self.dark_icon if self.page.theme_mode == "dark" else self.light_icon,
                            ref=self.theme_icon,
                            on_click=self.on_click_button
                        ),
                        ft.Text("Workspace", size=18, font_family="Courgette", color=ft.colors.GREY),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ],
            spacing=5,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
