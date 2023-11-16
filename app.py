# main.py
import flet as ft
from card import Card

DELTA_WIDTH: int = 80
DELTA_HEIGHT: int = 160

def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#E1E5ED"

    button: ft.Container = Card()
    page.add(button)
    page.update()

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
