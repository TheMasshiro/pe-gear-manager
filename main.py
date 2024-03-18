import view.view as view

if __name__ == "__main__":
    app = view.App()
    app.after(0, lambda: app.wm_state('zoomed'))
    app.mainloop()
