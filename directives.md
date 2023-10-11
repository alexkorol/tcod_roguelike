Here is a summary of the key steps to add items and an inventory system:

Create an Item class that inherits from Entity to represent items. Give it a Consumable component.

Create Consumable and HealingConsumable classes to define item behaviors.

Add an Inventory component that contains items. Give this to the Player.

Generate items in the dungeon using place_entities().

Create a PickupAction to add items to inventory.

Create DropItem action to drop items.

Create InventoryEventHandler to display inventory.

Create InventoryActivateHandler and InventoryDropHandler subclasses to handle using and dropping items.

Add keybindings to open the inventory and drop menus.

Call Consumable's consume() method when an item is used to remove it from the inventory.

Handle Impossible exceptions to prevent errors like using items at full health.

The key steps are:

Creating Item/Consumable classes
Giving Player an Inventory
Defining actions to pick up and drop items
Creating inventory menu handlers
Removing used items from the inventory