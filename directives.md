 Here are the key files to update and example fixes:

entity.py:

- Move Item and Inventory classes back into this module 

```python
class Item:
  # Item class code

class Inventory:
  # Inventory class code
```

entity_factories.py:

- Update to create Items with Consumables rather than Abilities

```python 
health_potion = Item(
  consumable=HealingConsumable(4) 
)
```

components/consumable.py:

- New module to contain Consumable component

```python
class Consumable:
  def consume(self):
    # Consume logic
    
class HealingConsumable(Consumable):
  # Healing logic
```

actions.py: 

- New ItemAction class

```python
class ItemAction(Action):
  # Item action logic  
```

input_handlers.py:

- Use ItemActions instead of InventoryActions

```python
return ItemAction(player, item) 
```

engine.py:

- Render MessageLog 

```python 
self.message_log.render(console)
```

main.py:

- Pass MessageLog to Engine

```python
engine = Engine(player, message_log) 
```

Let me know if you need any clarification or have additional examples you want to walk through!