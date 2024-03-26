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
import tkinter.filedialog as fd
import tkinter.messagebox as mb


class Notepad:
    """
    The Notepad GUI generator
    """

    __root: tk.Tk = tk.Tk()
    """
    The root (main) GUI window frame
    """

    __width: int = 300
    """
    The default window width
    """

    __height: int = 300
    """
    The default window height
    """

    __text_area: tk.Text = tk.Text(master=__root)
    """
    The text area
    """

    __menu_bar: tk.Menu = tk.Menu(master=__root)
    """
    The menu bar
    """

    __file_menu: tk.Menu = tk.Menu(master=__menu_bar, tearoff=0)
    """
    The file menu
    """

    __edit_menu: tk.Menu = tk.Menu(master=__menu_bar, tearoff=0)
    """
    The edit menu
    """

    __help_menu: tk.Menu = tk.Menu(master=__menu_bar, tearoff=0)
    """
    The help menu
    """

    __scrollbar: tk.Scrollbar = tk.Scrollbar(master=__text_area)
    """
    The scrollbar
    """

    __file: str | None
    """
    The file to be saved as .txt file
    """

    # noinspection PyBroadException
    def __init__(self, **kwargs):
        """
        Initializes the Notepad class

        :param kwargs: the key arguments
        """
        # Set icon
        try:
            self.__root.wm_iconbitmap("./assets/notepad.ico")
        except Exception:
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
        self.__text_area.grid(sticky=tk.N + tk.E + tk.S + tk.W)

        # To open a new file
        self.__file_menu.add_command(label="New", command=self.__new_file)

        # To open an existing file
        self.__file_menu.add_command(label="Open", command=self.__open_file)

        # To save the current file
        self.__file_menu.add_command(label="Save", command=self.__save_file)

        # To create a line inn the dialog box
        self.__file_menu.add_separator()
        self.__file_menu.add_command(label="Exit", command=self.__quit_application)
        self.__menu_bar.add_cascade(label="File", menu=self.__file_menu)

        # To give the feature of cut, copy, & paste
        self.__edit_menu.add_command(label="Cut", command=self.__cut)
        self.__edit_menu.add_command(label="Copy", command=self.__copy)
        self.__edit_menu.add_command(label="Paste", command=self.__paste)

        # To give the feature of editing
        self.__menu_bar.add_cascade(label="Edit", menu=self.__edit_menu)

        # To create the feature of description of the notepad
        self.__help_menu.add_command(label="About Notepad", command=self.__show_about)
        self.__menu_bar.add_cascade(label="Help", menu=self.__help_menu)

        self.__root.config(menu=self.__menu_bar)
        self.__scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Scrollbar will adjust automatically according to content
        self.__scrollbar.config(command=self.__text_area.yview)
        self.__text_area.config(yscrollcommand=self.__scrollbar.set)

    def __quit_application(self) -> None:
        """
        Closes the application

        :return: None - "void" function
        """
        self.__root.destroy()

    # noinspection PyMethodMayBeStatic
    def __show_about(self) -> None:
        """
        Shows the "about" message box

        :return: None - "void" function
        """
        mb.showinfo("Notepad", "Written by Patrick L. Branson")

    def __open_file(self) -> None:
        """
        Opens the file

        :return: None - "void" function
        """
        self.__file = fd.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                                             ("Text Documents", "*.txt")])
        if self.__file == "":
            # No file to open
            self.__file = None
        else:
            # Try to open the file & sets the window title
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__text_area.delete(index1=1.0, index2=tk.END)

            file = open(file=self.__file, mode="r")
            self.__text_area.insert(1.0, file.read())

            file.close()

    def __new_file(self) -> None:
        """
        Creates a new file

        :return: None - "void" function
        """
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__text_area.delete(index1=1.0, index2=tk.END)

    def __save_file(self) -> None:
        """
        Saves the file

        :return: None - "void" function
        """
        if self.__file is None:
            # Saves as a new File
            self.__file = fd.asksaveasfilename(initialfile="Untitled.txt",
                                               defaultextension=".txt",
                                               filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            if self.__file == "":
                self.__file = None
            else:
                # Try to save the file
                file = open(file=self.__file, mode="w")
                file.write(self.__text_area.get(index1=1.0, index2=tk.END))
                file.close()

                # Change the window title
                self.__root.title(os.path.basename(self.__file) + " - Notepad")

        else:
            file = open(file=self.__file, mode="w")
            file.write(self.__text_area.get(index1=1.0, index2=tk.END))
            file.close()

    def __cut(self) -> None:
        """
        Creates the "cut" command

        :return: None - "void" function
        """
        self.__text_area.event_generate("<<Cut>>")

    def __copy(self):
        """
        Creates the "copy" command

        :return: None - "void" function
        """
        self.__text_area.event_generate("<<Copy>>")

    def __paste(self):
        """
        Creates the "paste" command

        :return: None - "void" function
        """
        self.__text_area.event_generate("<<Paste>>")

    def run(self):
        """
        Runs the "mainloop" addition

        :return: None - "void" function
        """
        self.__root.mainloop()


if __name__ == "__main__":
    notepad = Notepad(width=600, height=400)
    notepad.run()
