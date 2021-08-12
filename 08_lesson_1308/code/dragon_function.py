def enemy_create():
    global health
    health = 100


def enemy_is_alive():
    return health > 0


def enemy_get_damage(damage):
    global health
    health -= damage
    if health < 0:
        health = 0


def game():
    enemy_create()
    finish = False
    while not finish:
        print(f'My health is {health}. Hit me!')
        hit = int(input())
        enemy_get_damage(hit)
        if not enemy_is_alive():
            finish = True
    print('You won!')