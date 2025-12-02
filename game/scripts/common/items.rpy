# Item and inventory handling

init python:
    def has_item(item):
        return inventory.get(item, False)

    def reset_inventory():
        global inventory
        inventory = {"werewolf_essence": False, "infernal_core": False}
