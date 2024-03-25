#  Copyright 2024 Patrick L. Branson
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os

import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd


class Notepad:
    """

    """

    __root: tk.Tk = tk.Tk()
    """
    
    """

    __width: int = 300
    """
    
    """

    __height: int = 300
    """
    
    """

    __text_area: tk.Text = tk.Text(master=__root)
    """
    
    """

    __menu_bar: tk.Menu = tk.Menu(master=__root)
    """
    
    """

    __file_menu: tk.Menu = tk.Menu(master=__menu_bar, tearoff=0)
    """
    
    """

    __edit_menu: tk.Menu = tk.Menu(master=__menu_bar, tearoff=0)
    """
    
    """

    __help_menu: tk.Menu = tk.Menu(master=__menu_bar, tearoff=0)
    """
    
    """

    __scroll_bar: tk.Scrollbar = tk.Scrollbar(master=__text_area)
    """
    
    """

    __file: None
    """
    
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        # Set icon
        try:
            self.__root.wm_iconbitmap("./assets/notepad.ico")
        except:
            pass

        # Set window size (the default is 300x300)
        try:
            self.__width = kwargs["width"]
        except KeyError:
            pass

        try:
            self.__height = kwargs["height"]
        except KeyError:
            pass

        # Sets the window text
        self.__root.title("Untitled - Notepad")

        # Center the window
        screen_width: int = self.__root.winfo_screenwidth()
        screen_height: int = self.__root.winfo_screenheight()

        # For the left-align and right (top) align
        left_align = (screen_width / 2) - (self.__width / 2)
        top_align = (screen_height / 2) - (self.__height / 2)

        self.__root.geometry("%dx%d+%d+%d" % (self.__width, self.__height, left_align, top_align))

        # To make the text area auto resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.__text_area.grid()

    def __quit_application(self):
        self.__root.destroy()

    def __show_about(self):
        mb.showinfo("Notepad", "Times New Roman")

    def __open_file(self):
        pass

    def __new_file(self):
        pass

    def __save_file(self):
        pass

    def __cut(self):
        self.__text_area.event_generate("<<Cut>>")

    def __copy(self):
        self.__text_area.event_generate("<<Copy>>")

    def __paste(self):
        self.__text_area.event_generate("<<Paste>>")

    def run(self):
        self.__root.mainloop()


if __name__ == "__main__":
    notepad = Notepad(width=600, height=400)
    notepad.run()