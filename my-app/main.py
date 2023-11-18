import flet as ft

#  https://flet.dev/docs/guides/python/testing-on-android/


def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))


ft.app(main)
