import tkinter as tk
import threading
import random
import time


class Variables:
    """
    This class is used to store variables that will be updated.
    """
    def __init__(self, variable1: int = 0, variable2: int = 0, variable3: int = 0):
        """
        This method is used to initialize the variables.
        :param variable1:
        :param variable2:
        :param variable3:
        """
        self.variable1 = variable1
        self.variable2 = variable2
        self.variable3 = variable3

    def update_random(self):
        """
        This method is used to update the variables with random values.
        :return:
        """
        while True:
            self.variable1 = random.randint(0, 1000000)
            self.variable2 = random.randint(0, 1000000)
            self.variable3 = random.randint(-1000000, 0)
            time.sleep(0.33333333333333333)


class Application(tk.Tk):
    """
    This class is used to create the GUI.
    """
    def __init__(self, our_variables: Variables):
        super().__init__()
        self.title("Variables Display Demo")
        self.our_variables = our_variables
        self.updating = False
        self.minsize(400, 400)
        self.create_grid()

    def create_grid(self):
        """
        This method is used to create the tkinter GUI grid.
        :return:
        """
        for i in range(3):  # Rows
            self.grid_rowconfigure(i, weight=1)
            for j in range(3):  # Columns
                self.grid_columnconfigure(j, weight=1)
                if j == 1:  # Center column
                    frame = tk.Frame(self, bd=2, relief="groove", width=100, height=100)
                    frame.grid(row=i, column=j, sticky="nsew", padx=10, pady=10)

                    if i == 0:  # Frame 1
                        frame.grid_columnconfigure(0, weight=1)  # for center alignment
                        frame.grid_columnconfigure(1, weight=1)  # for center alignment

                        label_var1 = tk.Label(frame, text="Variable1 = ", font=("Helvetica", 12))
                        label_var1.grid(row=0, column=0)

                        self.label_var1_value = tk.Label(frame, text=str(self.our_variables.variable1),
                                                         font=("Helvetica", 12))
                        self.label_var1_value.grid(row=0, column=1)

                    elif i == 1:  # Frame 2
                        frame.grid_columnconfigure((0, 1), weight=1)  # for center alignment
                        frame.grid_rowconfigure((0, 1), weight=1)  # for center alignment

                        label_var2 = tk.Label(frame, text="Variable2 = ", font=("Helvetica", 12))
                        label_var2.grid(row=0, column=0)

                        self.label_var2_value = tk.Label(frame, text=str(self.our_variables.variable2),
                                                         font=("Helvetica", 12))
                        self.label_var2_value.grid(row=0, column=1)

                        label_var3 = tk.Label(frame, text="Variable3 = ", font=("Helvetica", 12))
                        label_var3.grid(row=1, column=0)

                        self.label_var3_value = tk.Label(frame, text=str(self.our_variables.variable3),
                                                         font=("Helvetica", 12))
                        self.label_var3_value.grid(row=1, column=1)

                    elif i == 2:  # Frame 3
                        button_frame = tk.Frame(frame)
                        button_frame.place(relx=0.5, rely=0.6, anchor="center")

                        start_button = tk.Button(button_frame, text="Display RT",
                                                 command=self.start_command, font=("Helvetica", 13))
                        start_button.grid(row=0, column=0, padx=10)

                        stop_button = tk.Button(button_frame, text="Stop RT", command=self.stop_command,
                                                font=("Helvetica", 13))
                        stop_button.grid(row=0, column=1, padx=10)

    def update_display(self):
        """
        This method is used to update the display.
        :return:
        """
        if self.updating:
            self.label_var1_value.config(text=str(self.our_variables.variable1))
            self.label_var2_value.config(text=str(self.our_variables.variable2))
            self.label_var3_value.config(text=str(self.our_variables.variable3))
            self.after(1000, self.update_display)  # Schedule next update

    def start_command(self):
        """
        This method is used to start updating the display.
        :return:
        """
        self.updating = True
        self.update_display()

    def stop_command(self):
        """
        This method is used to stop updating the display.
        :return:
        """
        self.updating = False


if __name__ == "__main__":
    """ This is the main method of this program. """
    our_variables = Variables(5, 10, 15)

    thread = threading.Thread(target=our_variables.update_random, daemon=True)
    thread.start()

    app = Application(our_variables)
    app.mainloop()
