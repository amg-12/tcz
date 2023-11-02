def on_on_chat():
    player.execute("/give @s slime_ball 1 0 {\"keep_on_death\": {}}")
player.on_chat("give", on_on_chat)

def on_travelled_fall():
    mobs.apply_effect(LEVITATION, on, 600, 6)
player.on_travelled(FALL, on_travelled_fall)

def on_item_interacted_slimeball():
    mobs.clear_effect(on)
player.on_item_interacted(SLIMEBALL, on_item_interacted_slimeball)

def on_forever():
    mobs.clear_effect(off)
loops.forever(on_forever)

off: TargetSelector = None
on: TargetSelector = None
on = mobs.target(LOCAL_PLAYER)
on.add_rule("hasitem", "{item=slime_ball,location=slot.weapon.mainhand}")
off = mobs.target(LOCAL_PLAYER)
off.add_rule("hasitem",
    "{item=slime_ball,location=slot.weapon.mainhand,quantity=0}")
