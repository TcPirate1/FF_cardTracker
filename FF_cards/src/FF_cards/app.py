"""
Python mobile app that tracks your card collection
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class HelloWorld(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        # Where the image will be displayed
        self.image_view = toga.ImageView(style=Pack(height=300, padding=5))

        camera_button = toga.Button(
            "Take Photo",
            on_press=self.take_photo,
            style=Pack(padding=5)
        )

        # gallery_button = toga.Button(
        #     "Pick from Gallery",
        #     on_press=self.select_from_gallery,
        #     style=Pack(padding=5)
        # )

        button_box = toga.Box(style=Pack(direction=ROW, padding=5))
        button_box.add(camera_button)
        # button_box.add(gallery_button)

        main_box.add(button_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    async def take_photo(self, widget):
        try:
            if not self.camera.has_permission:
                await self.camera.request_permission()
                
            image = await self.camera.take_photo()
            
            if image:
                self.image_view.image = image

        except NotImplementedError:
            await self.main_window.dialog(
                toga.InfoDialog(
                "Error",
                "Gallery access is not yet implemented on this platform"
                )
            )

        except PermissionError:
            self.main_window.dialog(
                toga.InfoDialog(
                    "Error",
                    "This app does not have permission to use the camera"
                )
            )

def main():
    return HelloWorld()
