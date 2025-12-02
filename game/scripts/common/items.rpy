# Inventory helpers using a simple dictionary
init python:
    def init_inventory():
        global inventory
        inventory = {
            "werewolf_essence": False,
            "infernus_coal": False,
            "siren_shell": False,
            "clockwork_core": False,
        }

    def add_item(item_key):
        global inventory
        inventory[item_key] = True

    def has_item(item_key):
        return inventory.get(item_key, False)
