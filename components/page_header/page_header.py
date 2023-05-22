import flet as ft
import custom_icons


class PageHeader(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return ft.Column(
            [
                ft.Image(custom_icons.my_logo, width=200, height=100),
                ft.Text("Workspace", size=18, font_family="Courgette", color=ft.colors.GREY),
            ],
            spacing=5,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
