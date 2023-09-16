while True:
    mobs.execute(mobs.entities_by_type(SNOWBALL_PROJECTILE_MOB),
        pos(0, 0, 0),
        "summon lightning_bolt")
