import flet as ft

def main(page: ft.Page):
    # Set the page title and initial configurations
    page.title = "My Portfolio"
    page.padding = 20

    # Placeholder for the main content that will update based on navigation
    content = ft.Column(
        controls=[
            ft.Text("Welcome to My Portfolio!", style="headlineMedium")
        ],
        expand=True,
    )

    # Navigation click handler to update content area
    def nav_click(e):
        # Use the data property to identify which navigation option was clicked
        if e.control.data == "home":
            content.controls = [
                ft.Text("Welcome to My Portfolio!", style="headlineMedium"),
                ft.Text("This is the homepage of your portfolio website.")
            ]
        elif e.control.data == "about":
            content.controls = [
                ft.Text("About Me", style="headlineMedium"),
                ft.Text("A brief introduction about yourself, your background, and skills.")
            ]
        elif e.control.data == "projects":
            content.controls = [
                ft.Text("Projects", style="headlineMedium"),
                ft.Text("List or showcase your projects here with images, descriptions, and links.")
            ]
        elif e.control.data == "contact":
            content.controls = [
                ft.Text("Contact", style="headlineMedium"),
                ft.Text("Include your contact information or a contact form here.")
            ]
        # Refresh the content area
        page.update()

    # Navigation rail for sidebar navigation
    nav = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        destinations=[
            ft.NavigationRailDestination(icon=ft.icons.HOME, label="Home", data="home"),
            ft.NavigationRailDestination(icon=ft.icons.INFO, label="About", data="about"),
            ft.NavigationRailDestination(icon=ft.icons.WORK, label="Projects", data="projects"),
            ft.NavigationRailDestination(icon=ft.icons.CONTACT_MAIL, label="Contact", data="contact")
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
ft.app(target=main)

