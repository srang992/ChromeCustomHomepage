import flet as ft

from components.page_header.page_header import PageHeader
from components.search_bar.search_bar import SearchBar
from components.bookmarks.bookmarks import Bookmarks
from components.socials.socials import Socials
from utils import *


def main(page: ft.Page):
    page.title = "Subhradeep's Custom Homepage"
    page.fonts = fonts
    page.padding = 12
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    content = ft.Column(
        [
            PageHeader(),
            SearchBar(page),
            Socials(),
            Bookmarks(),
        ],
        spacing=35,
        expand=True,
        scroll=ft.ScrollMode.HIDDEN,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(
        content
    )


ft.app(
    target=main,
    view=ft.WEB_BROWSER,
    port=8500,
    assets_dir="assets",
)
