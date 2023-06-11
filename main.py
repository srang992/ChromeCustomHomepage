import flet as ft

from components.page_header.page_header import PageHeader
from components.search_bar.search_bar import SearchBar
from components.bookmarks.bookmarks import Bookmarks
from components.socials.socials import Socials
from utils import *


def main(page: ft.Page):
    page.title = "Subhradeep's Custom Homepage"
    page.fonts = fonts

    lv = ft.ListView(expand=1, spacing=10, padding=12)

    content = ft.Column(
            [
                PageHeader(),
                SearchBar(page),
                Socials(),
                Bookmarks(),
            ],
            spacing=35,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    lv.controls.append(
        content
    )

    page.add(
        lv
    )


ft.app(
    target=main,
    view=ft.WEB_BROWSER,
    port=8500,
    assets_dir="assets",
)
