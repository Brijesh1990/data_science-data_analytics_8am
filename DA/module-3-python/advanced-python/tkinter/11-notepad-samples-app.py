import tkinter as tk
from tkinter import filedialog, messagebox, font


class Notepad:
    def __init__(self, window):
        self.window = window
        self.window.title("Untitled - Notepad")
        self.window.geometry("900x600")
        self.window.minsize(600, 400)

        self.current_file = None
        self.is_modified = False

        # --------------------------------------------------
        # Default Font
        # --------------------------------------------------
        self.text_font = font.Font(
            family="Consolas",
            size=12
        )

        # --------------------------------------------------
        # Menu Bar
        # --------------------------------------------------
        menubar = tk.Menu(window)

        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)

        file_menu.add_command(
            label="New",
            accelerator="Ctrl+N",
            command=self.new_file
        )

        file_menu.add_command(
            label="Open...",
            accelerator="Ctrl+O",
            command=self.open_file
        )

        file_menu.add_command(
            label="Save",
            accelerator="Ctrl+S",
            command=self.save_file
        )

        file_menu.add_command(
            label="Save As...",
            accelerator="Ctrl+Shift+S",
            command=self.save_as
        )

        file_menu.add_separator()

        file_menu.add_command(
            label="Exit",
            command=self.exit_app
        )

        menubar.add_cascade(
            label="File",
            menu=file_menu
        )

        # Edit Menu
        edit_menu = tk.Menu(menubar, tearoff=0)

        edit_menu.add_command(
            label="Undo",
            accelerator="Ctrl+Z",
            command=self.undo
        )

        edit_menu.add_command(
            label="Redo",
            accelerator="Ctrl+Y",
            command=self.redo
        )

        edit_menu.add_separator()

        edit_menu.add_command(
            label="Cut",
            accelerator="Ctrl+X",
            command=self.cut
        )

        edit_menu.add_command(
            label="Copy",
            accelerator="Ctrl+C",
            command=self.copy
        )

        edit_menu.add_command(
            label="Paste",
            accelerator="Ctrl+V",
            command=self.paste
        )

        edit_menu.add_separator()

        edit_menu.add_command(
            label="Select All",
            accelerator="Ctrl+A",
            command=self.select_all
        )

        edit_menu.add_command(
            label="Find",
            accelerator="Ctrl+F",
            command=self.find_text
        )

        menubar.add_cascade(
            label="Edit",
            menu=edit_menu
        )

        # Format Menu
        format_menu = tk.Menu(menubar, tearoff=0)

        self.word_wrap = tk.BooleanVar(value=True)

        format_menu.add_checkbutton(
            label="Word Wrap",
            variable=self.word_wrap,
            command=self.toggle_word_wrap
        )

        format_menu.add_separator()

        format_menu.add_command(
            label="Increase Font",
            command=self.increase_font
        )

        format_menu.add_command(
            label="Decrease Font",
            command=self.decrease_font
        )

        menubar.add_cascade(
            label="Format",
            menu=format_menu
        )

        # Help Menu
        help_menu = tk.Menu(menubar, tearoff=0)

        help_menu.add_command(
            label="About Notepad",
            command=self.about
        )

        menubar.add_cascade(
            label="Help",
            menu=help_menu
        )

        window.config(menu=menubar)

        # --------------------------------------------------
        # Text Area Frame
        # --------------------------------------------------
        text_frame = tk.Frame(window)
        text_frame.pack(
            fill="both",
            expand=True
        )

        # Scrollbar
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(
            side="right",
            fill="y"
        )

        # Text Editor
        self.text_area = tk.Text(
            text_frame,
            font=self.text_font,
            undo=True,
            wrap="word",
            padx=10,
            pady=10,
            bg="white",
            fg="black",
            insertbackground="black",
            selectbackground="#0078D7",
            yscrollcommand=scrollbar.set
        )

        self.text_area.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.config(
            command=self.text_area.yview
        )

        # --------------------------------------------------
        # Status Bar
        # --------------------------------------------------
        self.status_bar = tk.Label(
            window,
            text="Ln 1, Col 1",
            anchor="e",
            bg="#eeeeee",
            fg="#333333",
            padx=10
        )

        self.status_bar.pack(
            side="bottom",
            fill="x"
        )

        # --------------------------------------------------
        # Events
        # --------------------------------------------------
        self.text_area.bind(
            "<<Modified>>",
            self.on_text_modified
        )

        self.text_area.bind(
            "<KeyRelease>",
            self.update_status
        )

        self.text_area.bind(
            "<ButtonRelease-1>",
            self.update_status
        )

        self.window.protocol(
            "WM_DELETE_WINDOW",
            self.exit_app
        )

        # Keyboard shortcuts
        window.bind("<Control-n>", lambda event: self.new_file())
        window.bind("<Control-o>", lambda event: self.open_file())
        window.bind("<Control-s>", lambda event: self.save_file())
        window.bind(
            "<Control-Shift-S>",
            lambda event: self.save_as()
        )

        window.bind("<Control-z>", lambda event: self.undo())
        window.bind("<Control-y>", lambda event: self.redo())

        window.bind("<Control-f>", lambda event: self.find_text())

        # Initial cursor position
        self.update_status()

    # ------------------------------------------------------
    # File Functions
    # ------------------------------------------------------

    def new_file(self):
        if not self.check_unsaved():
            return

        self.text_area.delete("1.0", tk.END)

        self.current_file = None
        self.is_modified = False

        self.update_title()

    def open_file(self):
        if not self.check_unsaved():
            return

        file_path = filedialog.askopenfilename(
            title="Open File",
            filetypes=[
                ("Text Files", "*.txt"),
                ("Python Files", "*.py"),
                ("All Files", "*.*")
            ]
        )

        if not file_path:
            return

        try:
            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                content = file.read()

            self.text_area.delete(
                "1.0",
                tk.END
            )

            self.text_area.insert(
                "1.0",
                content
            )

            self.current_file = file_path
            self.is_modified = False

            self.text_area.edit_modified(False)

            self.update_title()

        except Exception as error:
            messagebox.showerror(
                "Error",
                f"Could not open file.\n\n{error}"
            )

    def save_file(self):
        if self.current_file is None:
            return self.save_as()

        try:
            content = self.text_area.get(
                "1.0",
                tk.END
            )

            with open(
                self.current_file,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(content)

            self.is_modified = False
            self.text_area.edit_modified(False)

            self.update_title()

        except Exception as error:
            messagebox.showerror(
                "Error",
                f"Could not save file.\n\n{error}"
            )

    def save_as(self):
        file_path = filedialog.asksaveasfilename(
            title="Save As",
            defaultextension=".txt",
            filetypes=[
                ("Text Files", "*.txt"),
                ("Python Files", "*.py"),
                ("All Files", "*.*")
            ]
        )

        if not file_path:
            return False

        try:
            content = self.text_area.get(
                "1.0",
                tk.END
            )

            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(content)

            self.current_file = file_path
            self.is_modified = False

            self.text_area.edit_modified(False)

            self.update_title()

            return True

        except Exception as error:
            messagebox.showerror(
                "Error",
                f"Could not save file.\n\n{error}"
            )

            return False

    # ------------------------------------------------------
    # Edit Functions
    # ------------------------------------------------------

    def undo(self):
        try:
            self.text_area.edit_undo()
        except tk.TclError:
            pass

    def redo(self):
        try:
            self.text_area.edit_redo()
        except tk.TclError:
            pass

    def cut(self):
        self.text_area.event_generate(
            "<<Cut>>"
        )

    def copy(self):
        self.text_area.event_generate(
            "<<Copy>>"
        )

    def paste(self):
        self.text_area.event_generate(
            "<<Paste>>"
        )

    def select_all(self):
        self.text_area.tag_add(
            "sel",
            "1.0",
            "end"
        )

        self.text_area.mark_set(
            "insert",
            "1.0"
        )

        self.text_area.see(
            "insert"
        )

    # ------------------------------------------------------
    # Find
    # ------------------------------------------------------

    def find_text(self):
        find_window = tk.Toplevel(self.window)

        find_window.title("Find")
        find_window.geometry("350x120")
        find_window.resizable(False, False)

        tk.Label(
            find_window,
            text="Find:"
        ).pack(
            side="left",
            padx=10,
            pady=20
        )

        search_entry = tk.Entry(
            find_window,
            width=25
        )

        search_entry.pack(
            side="left",
            pady=20
        )

        search_entry.focus()

        def search():
            self.text_area.tag_remove(
                "found",
                "1.0",
                tk.END
            )

            word = search_entry.get()

            if not word:
                return

            start = "1.0"

            while True:
                position = self.text_area.search(
                    word,
                    start,
                    stopindex=tk.END
                )

                if not position:
                    break

                end = f"{position}+{len(word)}c"

                self.text_area.tag_add(
                    "found",
                    position,
                    end
                )

                start = end

            self.text_area.tag_config(
                "found",
                background="yellow",
                foreground="black"
            )

        tk.Button(
            find_window,
            text="Find",
            command=search
        ).pack(
            side="left",
            padx=10
        )

        search_entry.bind(
            "<Return>",
            lambda event: search()
        )

    # ------------------------------------------------------
    # Formatting
    # ------------------------------------------------------

    def toggle_word_wrap(self):
        if self.word_wrap.get():
            self.text_area.config(
                wrap="word"
            )
        else:
            self.text_area.config(
                wrap="none"
            )

    def increase_font(self):
        current_size = self.text_font.cget("size")

        self.text_font.configure(
            size=current_size + 2
        )

    def decrease_font(self):
        current_size = self.text_font.cget("size")

        if current_size > 6:
            self.text_font.configure(
                size=current_size - 2
            )

    # ------------------------------------------------------
    # Modified / Status
    # ------------------------------------------------------

    def on_text_modified(self, event=None):
        if self.text_area.edit_modified():
            self.is_modified = True

            self.update_title()

            self.text_area.edit_modified(False)

        self.update_status()

    def update_status(self, event=None):
        cursor_position = self.text_area.index(
            tk.INSERT
        )

        line, column = cursor_position.split(".")

        self.status_bar.config(
            text=f"Ln {line}, Col {int(column) + 1}"
        )

    def update_title(self):
        if self.current_file:
            file_name = self.current_file.split("/")[-1]
        else:
            file_name = "Untitled"

        if self.is_modified:
            self.window.title(
                f"*{file_name} - Notepad"
            )
        else:
            self.window.title(
                f"{file_name} - Notepad"
            )

    # ------------------------------------------------------
    # Unsaved Changes
    # ------------------------------------------------------

    def check_unsaved(self):
        if not self.is_modified:
            return True

        answer = messagebox.askyesnocancel(
            "Notepad",
            "Do you want to save changes?"
        )

        if answer is None:
            return False

        if answer:
            return self.save_file()

        return True

    # ------------------------------------------------------
    # Exit
    # ------------------------------------------------------

    def exit_app(self):
        if self.check_unsaved():
            self.window.destroy()

    # ------------------------------------------------------
    # About
    # ------------------------------------------------------

    def about(self):
        messagebox.showinfo(
            "About Notepad",
            "Simple Notepad\n\n"
            "Built with Python Tkinter\n"
            "No database required."
        )


# ----------------------------------------------------------
# Start Application
# ----------------------------------------------------------

window = tk.Tk()

app = Notepad(window)

window.mainloop()
