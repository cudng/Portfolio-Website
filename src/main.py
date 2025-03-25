import flet as ft
from flet.core.text_style import TextThemeStyle
import logging


def main(page: ft.Page):
    # Set the page title and initial configurations
    page.title = "My Portfolio"
    page.padding = 20

    # Placeholder for the main content that will update based on navigation
    content = ft.Column(
        controls=[
            ft.Text("Welcome to My Portfolio!", style=TextThemeStyle.HEADLINE_MEDIUM),
            ft.Text("This is the homepage of your portfolio website.")
        ],
        expand=True,
    )

    # Navigation click handler to update content area
    def nav_click(e):
        # Use the data property to identify which navigation option was clicked
        if e.control.selected_index == 0:
            content.controls = [
                ft.Text("Welcome to My Portfolio!", style=TextThemeStyle.HEADLINE_MEDIUM),
                ft.Text("This is the homepage of your portfolio website.")
            ]
        elif e.control.selected_index == 1:
            content.controls = [
                ft.Text("About Me", style=TextThemeStyle.HEADLINE_MEDIUM),
                ft.Text("A brief introduction about yourself, your background, and skills.")
            ]
        elif e.control.selected_index == 2:
            content.controls = [
                ft.Text("Projects", style=TextThemeStyle.HEADLINE_MEDIUM),
                ft.Text("List or showcase your projects here with images, descriptions, and links.")
            ]
        elif e.control.selected_index == 3:
            content.controls = [
                ft.Text("Contact",  style=TextThemeStyle.HEADLINE_MEDIUM),
                ft.Text("Include your contact information or a contact form here.")
            ]
        # Refresh the content area
        page.update()

    # Navigation rail for sidebar navigation
    nav = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.HOME, label="Home", data="home"),
            ft.NavigationRailDestination(icon=ft.Icons.INFO, label="About", data="about"),
            ft.NavigationRailDestination(icon=ft.Icons.WORK, label="Projects", data="projects"),
            ft.NavigationRailDestination(icon=ft.Icons.CONTACT_MAIL, label="Contact", data="contact")
        ],
        on_change=lambda e: nav_click(e),
    )

    # Create a responsive layout with a row: Navigation on the left and content on the right
    layout = ft.Row(
        controls=[
            nav,
            ft.VerticalDivider(width=1),
            content
        ],
        expand=True,
    )

    page.add(layout)

# Run the Flet app
ft.app(target=main, view=ft.WEB_BROWSER)

