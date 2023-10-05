def on_item_interacted_copper_ingot():
    global on
    on = not (on)
    if on:
        grab()
    else:
        release()
player.on_item_interacted(COPPER_INGOT, on_item_interacted_copper_ingot)

def grab():
    player.execute("tag " + str(target) + " add g")
    player.execute("title @s actionbar §6" + str(target))
    player.execute("playsound mob.guardian.hit")

def release():
    player.execute("tag @e remove g")
    if launch:
        mobs.apply_effect(RESISTANCE, mobs.target(ALL_ENTITIES), 1, 255)
        player.execute("summon ender_crystal ^0 ^2 ^2")
        player.execute("event entity @e[type=ender_crystal] minecraft:crystal_explode")

on = False
target: TargetSelector = None
launch = False
launch = False
gameplay.set_game_rule(MOB_GRIEFING, not (launch))
target = mobs.target(ALL_ENTITIES)
target.add_rule("c", "1")
target.add_rule("name", "!" + player.name())
grabbed = mobs.target(ALL_ENTITIES)
grabbed.add_rule("tag", "g")
while True:
    mobs.teleport_to_position(grabbed, pos_local(0, 2, 3))
