import flet as ft
from ionicons_python.extra_icons import google_color_icon


class SearchBar(ft.UserControl):
    clear_text = ft.Ref[ft.IconButton]()

    def __init__(self, page, ref_search_field=None):
        super().__init__()
        self.page = page
        if ref_search_field is None:
            self.search_field = ft.Ref[ft.TextField]()
        else:
            self.search_field = ref_search_field

    async def on_press_enter(self, _):
        search_text = "+".join([word for word in self.search_field.current.value.split(" ")])
        if not search_text:
            self.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text("The search bar shouldn't be empty!"),
                    open=True
                ),
            )
            await self.update_async()
        else:
            await self.page.launch_url_async(f"https://www.google.com/search?q={search_text}")

    async def on_click_cancel(self, _):
        self.search_field.current.value = None
        self.clear_text.current.visible = False
        await self.update_async()

    async def on_textfield_change(self, _):
        if self.search_field.current.value:
            self.clear_text.current.visible = True
        else:
            self.clear_text.current.visible = False
        await self.update_async()

    def build(self):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Image(google_color_icon, width=28, height=28),
                    ft.TextField(
                        border=ft.InputBorder.NONE,
                        ref=self.search_field,
                        on_submit=self.on_press_enter,
                        hint_text="Search in Google",
                        hint_style=ft.TextStyle(font_family="Alkatra", color=ft.colors.with_opacity(0.7, "grey")),
                        on_change=self.on_textfield_change,
                        text_style=ft.TextStyle(font_family="Alkatra"),
                        expand=True,
                        autofocus=True,
                    ),
                    ft.IconButton(
                        ft.icons.CLOSE,
                        on_click=self.on_click_cancel,
                        ref=self.clear_text,
                        visible=False
                    )
                ],
            ),
            shadow=ft.BoxShadow(
                blur_style=ft.ShadowBlurStyle.OUTER,
                blur_radius=5,
                color=ft.colors.with_opacity(0.5, "grey")
            ),
            width=400,
            border_radius=10,
            padding=ft.padding.only(left=18, top=6, right=6, bottom=6),
        )
