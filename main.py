import flet as ft

def main(page: ft.Page):
    page.title = "Mi app Flet"
    page.add(ft.Text("Hola desde Flet!"))

ft.app(target=main)
