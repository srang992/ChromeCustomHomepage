import flet as ft

import custom_icons
from search_bar import SearchBar
from social_icons import SocialIcons
from utils import *
from bookmark_card import BookmarkCard


def main(page: ft.Page):
    page.title = "Subhradeep's Custom Homepage"
    page.fonts = fonts
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(
        ft.Column(
            [
                ft.Column(
                    [
                        ft.Image(custom_icons.my_logo, width=200, height=100),
                        ft.Text("Workspace", size=18, font_family="Courgette", color=ft.colors.GREY),
                    ],
                    spacing=5,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                SearchBar(),
                ft.Column(
                    [
                        ft.Text("Socials:", size=15, font_family="Courgette"),
                        SocialIcons(),
                    ],
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.Column(
                    [
                        ft.Text("Bookmarks:", size=15, font_family="Courgette"),
                        ft.Row(
                            [
                                BookmarkCard(
                                    icon=custom_icons.chatgpt,
                                    text="ChatGPT",
                                    icon_size=24,
                                    url=chatgpt_url
                                ),
                                BookmarkCard(
                                    icon=custom_icons.youtube,
                                    text="YouTube",
                                    icon_size=24,
                                    color="#CD201F",
                                    url=youtube_url
                                ),
                                BookmarkCard(
                                    icon=custom_icons.medium_editor,
                                    text="Medium Drafts",
                                    icon_size=24,
                                    url=medium_editor_url
                                ),
                                BookmarkCard(
                                    icon=custom_icons.gmail,
                                    text="Gmail",
                                    icon_size=24,
                                    url=gmail_url
                                ),
                                BookmarkCard(
                                    icon=custom_icons.analyticsvidhya,
                                    text="AnalyticsVidhya Editor",
                                    icon_size=24,
                                    url=analyticsvidhya_editor_url
                                ),
                                BookmarkCard(
                                    icon=custom_icons.flet_icon,
                                    text="Flet Docs",
                                    icon_size=24,
                                    url=flet_url
                                ),
                            ],
                            width=500,
                            wrap=True,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                    ],
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
            ],
            spacing=40,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


ft.app(
    target=main,
    view="web_browser",
    assets_dir="./assets"
)
