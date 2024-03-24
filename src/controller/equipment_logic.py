from src.model import (
    fetch_equipments,
    insert_equipment,
    update_equipment,
    delete_equipment,
    equipment_id_exists,
    equipment_name_exists,
)


def insert_equipment_data(id, name, quantity):
    insert_equipment(id, name, quantity)
