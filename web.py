import tkinter as tk
import webbrowser

class WebsiteOpenerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Website Opener")

        self.label = tk.Label(master, text="https://www.facebook.com/:")
        self.label.pack()

        self.entry = tk.Entry(master, width=40)
        self.entry.pack()

        self.open_button = tk.Button(master, text="Open Website", command=self.open_website)
        self.open_button.pack()

    def open_website(self):
        url = self.entry.get()
        if url:
            webbrowser.open_new(url)

def main():
    root = tk.Tk()
    app = WebsiteOpenerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
