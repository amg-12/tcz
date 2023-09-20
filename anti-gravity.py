def on_item_interacted_slimeball():
    global time
    mobs.clear_effect(mobs.target(LOCAL_PLAYER))
    time = gameplay.time_query(DAY_TIME)
    # more reliable than built-in `pause` function:
    while gameplay.time_query(DAY_TIME) < time + 3:
        continue
    mobs.apply_effect(LEVITATION, mobs.target(LOCAL_PLAYER), 600, 6)
player.on_item_interacted(SLIMEBALL, on_item_interacted_slimeball)

def on_item_interacted_netherite_ingot():
    mobs.clear_effect(mobs.target(LOCAL_PLAYER))
player.on_item_interacted(NETHERITE_INGOT, on_item_interacted_netherite_ingot)

time = 0
mobs.give(mobs.target(LOCAL_PLAYER), SLIMEBALL, 1)
mobs.give(mobs.target(LOCAL_PLAYER), NETHERITE_INGOT, 1)
