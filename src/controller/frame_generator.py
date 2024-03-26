def generate_frames(
    login,
    logout,
    equipments,
    history,
    value,
):
    login.grid_remove()
    logout.grid_remove()
    equipments.grid_remove()
    history.grid_remove()

    if value == "Student Login":
        login.grid(row=0, column=0, sticky="nswe")
    elif value == "Student Logout":
        logout.grid(row=0, column=0, sticky="nswe")
    elif value == "Manage Equipments":
        equipments.grid(row=0, column=0, sticky="nswe")
    elif value == "Return History":
        history.grid(row=0, column=0, sticky="nswe")
    else:
        raise Exception("Not in the menu")
