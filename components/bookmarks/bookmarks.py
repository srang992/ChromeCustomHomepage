import flet as ft
from components.bookmarks.bookmark_card import BookmarkCard
import custom_icons
from utils import *


class Bookmarks(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return ft.Column(
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
                        BookmarkCard(
                            icon=custom_icons.streamlit,
                            text="MP4 to GIF",
                            icon_size=24,
                            url=mp4_to_gif_url
                        ),
                    ],
                    width=700,
                    wrap=True,
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
