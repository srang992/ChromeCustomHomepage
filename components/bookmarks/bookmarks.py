import flet as ft
from components.bookmarks.bookmark_card import BookmarkCard
import custom_icons
from ionicons_python.ionicons_icons import youtube_icon
from ionicons_python.extra_icons import chatgpt_icon, streamlit_icon, gmail_icon
from utils import *


class Bookmarks(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return ft.Column(
            [
                ft.Text("Bookmarks:", size=15, font_family="Courgette"),
                ft.ResponsiveRow(
                    [
                        BookmarkCard(
                            icon=chatgpt_icon,
                            text="ChatGPT",
                            icon_size=24,
                            url=chatgpt_url,
                            col=col_dict,
                        ),
                        BookmarkCard(
                            icon=youtube_icon,
                            text="YouTube",
                            icon_size=24,
                            color="#CD201F",
                            url=youtube_url,
                            col=col_dict,
                        ),
                        BookmarkCard(
                            icon=custom_icons.medium_editor,
                            text="Medium Drafts",
                            icon_size=24,
                            url=medium_editor_url,
                            col=col_dict,
                        ),
                        BookmarkCard(
                            icon=gmail_icon,
                            text="Gmail",
                            icon_size=24,
                            url=gmail_url,
                            col=col_dict,
                        ),
                        BookmarkCard(
                            icon=custom_icons.analyticsvidhya,
                            text="AnalyticsVidhya Editor",
                            icon_size=24,
                            url=analyticsvidhya_editor_url,
                            col=col_dict,
                        ),
                        BookmarkCard(
                            icon=custom_icons.flet_icon,
                            text="Flet Docs",
                            icon_size=24,
                            url=flet_url,
                            col=col_dict,
                        ),
                        BookmarkCard(
                            icon=streamlit_icon,
                            text="MP4 to GIF",
                            icon_size=24,
                            url=mp4_to_gif_url,
                            col=col_dict,
                        ),
                    ],
                    spacing=7,
                    run_spacing={"sm": 7},
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            spacing=10,
            width=950,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
