import enemy
import hero

player = hero.Hero(0,0,0)
enemy_unit = enemy.Enemy(0,0,0)

def stats(character):
    if character == player:
        char = "Герой"
    else:
        char = "Враг"

    print(f"Какое имя вы хотите дать персонажу {char}?")
    character.name = input()
    print(f"Введите количество здоровья персонажа {char}:")
    character.health = int(input())
    print(f"Введите силу атаки персонажа {char}:")
    character.attack_power = int(input())


def main():
    while player.is_alive() and enemy_unit.is_alive():
        player.attack(enemy_unit)
        if enemy_unit.is_alive():
            enemy_unit.attack(player)


stats(player)
stats(enemy_unit)
main()
