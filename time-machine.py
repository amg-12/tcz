time_machine = False

def on_forever():
    while time_machine:
        gameplay.time_set(Math.round((270 - player.get_orientation()) * 66.666))
loops.forever(on_forever)

def on_item_interacted_clock():
    global time_machine
    time_machine = not (time_machine)
    player.execute("title @s actionbar Time Machine: " + ("" + str(time_machine)))
player.on_item_interacted(CLOCK, on_item_interacted_clock)
