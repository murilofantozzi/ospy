import flet
from flet import *
from functools import partial
import time

# Sidebar Class


class ModernNavBar(UserControl):
    def __init__(self):
        super().__init__()

    def UserData(self, initials: str, name: str, description: str):
        return Container(
            content=Row(
                controls=[
                    Container(
                        width=42,
                        height=42,
                        bgcolor='bluegrey900',
                        alignment=alignment.center,
                        border_radius=8,
                        content=Text(
                            value=initials,
                            size=20,
                            weight="bold",
                        ),
                    ),
                    Column(
                        spacing=1,
                        alignment="center",
                        controls=[
                            Text(
                                value=name,
                                size=11,
                                weight='bold',
                                opacity=1,
                                animate_opacity=200
                            ),
                            Text(
                                value=description,
                                size=9,
                                weight="w400",
                                color="white54",
                                opacity=1,
                                animate_opacity=200
                            ),
                        ]
                    )
                ]
            )
        )

    def ContainedIcon(self, icon_name: str, text: str):
        return Container(
            width=180,
            height=45,
            border_radius=10,
            on_hover=None,
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=18,
                        icon_color='white54',
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=7),
                            },
                            overlay_color={"": "transparent"},
                        ),
                    ),
                    Text(
                        value=text,
                        color="white54",
                        size=11,
                        opacity=1,
                        animate_opacity=200,
                    )
                ]
            ),
        )

    def build(self):
        return Container(
            width=200,
            height=580,
            padding=padding.only(top=10),
            content=Column(
                controls=[
                    self.UserData("LI", 'Line Indent', 'Software Eginner'),
                    Divider(height=5, color="transparent"),
                    self.ContainedIcon(icons.SEARCH, "Search"),
                ]
            ),

        )


# Main Function
def main(page: Page):
    # Title
    page.title = 'Flet Modern Sidebar'

    # alignemnts
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    # add class to page
    page.add(
        Container(
            width=200,
            height=580,
            bgcolor='black',
            border_radius=10,
            animate=animation.Animation(500, 'decelerate'),
            alignment=alignment.center,
            padding=10,
            content=ModernNavBar()
        )
    )

    page.update()

    # run
if __name__ == "__main__":
    flet.app(target=main)
