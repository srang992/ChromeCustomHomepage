import flet as ft
import custom_icons


class SearchBar(ft.UserControl):

    search_field = ft.Ref[ft.TextField]()
    clear_text = ft.Ref[ft.IconButton]()

    def __init__(self):
        super().__init__()

    def on_press_enter(self, _):
        search_text = "+".join([word for word in self.search_field.current.value.split(" ")])
        if not search_text:
            self.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text("The search bar shouldn't be empty!"),
                    open=True
                ),
            )
            self.update()
        else:
            self.page.launch_url(f"https://www.google.com/search?q={search_text}")

    def on_click_cancel(self, _):
        self.search_field.current.value = None
        self.clear_text.current.visible = False
        self.update()

    def on_textfield_change(self, _):
        if self.search_field.current.value:
            self.clear_text.current.visible = True
        else:
            self.clear_text.current.visible = False
        self.update()

    def build(self):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Image(custom_icons.google, width=24, height=24),
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
