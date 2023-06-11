import flet as ft
from components.others.buttons.custom_icon_button import CustomIconButton
import custom_icons
from ionicons_python.ionicons_icons import twitter_icon, github_icon, linkedin_icon, medium_icon
from utils import *


class Socials(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return ft.Column(
            [
                ft.Text("Socials:", size=15, font_family="Courgette"),
                ft.Container(
                    content=ft.Row(
                        [
                            CustomIconButton(
                                icon=twitter_icon,
                                color=ft.colors.BLUE_ACCENT,
                                url=twitter_url,
                            ),
                            CustomIconButton(
                                icon=github_icon,
                                color=ft.colors.BLUE_ACCENT,
                                url=github_url,
                            ),
                            CustomIconButton(
                                icon=linkedin_icon,
                                color="#0A66C2",
                                url=linkedin_url,
                            ),
                            CustomIconButton(
                                icon=medium_icon,
                                color=ft.colors.GREEN,
                                url=medium_url,
                            ),
                            CustomIconButton(
                                icon=custom_icons.analyticsvidhya,
                                url=analyticsvidhya_url,
                            ),
                        ],
                        spacing=25,
                        wrap=True
                    ),
                ),
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
