from src.view import App

if __name__ == "__main__":
    app = App()
    app.after(0, lambda: app.wm_state("zoomed"))
    app.mainloop()
