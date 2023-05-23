import flet as ft

from components.page_header.page_header import PageHeader
from components.search_bar.search_bar import SearchBar
from components.bookmarks.bookmarks import Bookmarks
from components.socials.socials import Socials
from utils import *


def main(page: ft.Page):
    page.title = "Subhradeep's Custom Homepage"
    page.fonts = fonts
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(
        ft.Column(
            [
                PageHeader(),
                SearchBar(),
                Socials(),
                Bookmarks(),
            ],
            spacing=40,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


ft.app(
    target=main,
    view=ft.WEB_BROWSER,
    assets_dir="assets"
)
