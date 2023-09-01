import flet as ft
import flet_fastapi
import os
from components.page_header.page_header import PageHeader
from components.search_bar.search_bar import SearchBar
from components.bookmarks.bookmarks import Bookmarks
from components.socials.socials import Socials
from utils import *


async def main(page: ft.Page):
    page.title = "Subhradeep's Custom Homepage"
    page.fonts = fonts
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    ref_search_field = ft.Ref[ft.TextField]()

    async def on_keyboard(e: ft.KeyboardEvent):
        if e.key == "/":
            ref_search_field.current.focus()
        await page.update_async()

    content = ft.Column(
        [
            PageHeader(),
            ft.Container(
                SearchBar(
                    page,
                    ref_search_field
                ),
                padding=5
            ),
            Socials(),
            Bookmarks(),
        ],
        spacing=35,
        expand=True,
        scroll=ft.ScrollMode.HIDDEN,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.on_keyboard_event = on_keyboard

    await page.add_async(
        content
    )


app = flet_fastapi.app(main, assets_dir=os.path.abspath("assets"))
