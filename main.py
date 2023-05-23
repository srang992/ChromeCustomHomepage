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

    lv = ft.ListView(expand=1, spacing=10, padding=10)

    content = ft.Column(
            [
                PageHeader(),
                SearchBar(),
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

    def on_resize(_):
        if 640 < page.width <= 1080:
            if page.controls:
                page.controls.pop()
            page.controls.append(content)
        elif page.width <= 640:
            if page.controls:
                page.controls.pop()
            page.controls.append(lv)
        else:
            if page.controls:
                page.controls.pop()
            page.controls.append(content)

        page.update()

    page.on_resize = on_resize

    page.add(
        content
    )


ft.app(
    target=main,
    view=ft.WEB_BROWSER,
    assets_dir="assets"
)
