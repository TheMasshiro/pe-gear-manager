def generate_frames(
    active_users,
    sign_in,
    sign_out,
    add_equipment,
    inventory_buttons,
    inventory_search,
    history,
    separator,
    value,
):
    active_users.grid_remove()

    sign_in.grid_remove()
    sign_out.grid_remove()

    add_equipment.grid_remove()
    inventory_buttons.grid_remove()
    inventory_search.grid_remove()

    history.grid_remove()

    if value == "Active Users":
        active_users.grid(row=0, column=0, padx=(200, 20), pady=30, sticky="n")
        separator.grid(row=0, column=0, padx=(0, 960), pady=0, sticky="n")
    elif value == "Sign In/Out":
        sign_in.grid(row=0, column=0, padx=(225, 10), pady=30, sticky="n")
        sign_out.grid(row=0, column=1, padx=(10, 70), pady=30, sticky="n")
        separator.grid(row=0, column=0, padx=(0, 290), pady=0, sticky="n")
    elif value == "Add Equipments":
        add_equipment.grid(
                row=0, column=0, padx=(235, 10), pady=30, sticky="n"
            )
        inventory_buttons.grid(
                row=0, column=1, padx=(30, 200), pady=(70, 100), sticky="s"
            )
        inventory_search.grid(
                row=0, column=1, padx=(30, 200), pady=(30, 100), sticky="n"
            )
        separator.grid(row=0, column=0, padx=(0, 370), pady=0, sticky="n")
    elif value == "Return History":
        history.grid(row=0, column=0, padx=(200, 20), pady=30, sticky="n")
        separator.grid(row=0, column=0, padx=(0, 960), pady=0, sticky="n")
    else:
        raise Exception("Not in the menu")
