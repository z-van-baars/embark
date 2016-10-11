import pygame
import ui
import random
import utilities

pygame.init()
pygame.display.set_mode([0, 0])


def strike(attacker, defender):
    damage_roll_1 = utilities.roll_dice(1, attacker.strength)
    damage_roll_2 = utilities.roll_dice(1, attacker.strength)
    damage_roll = max(damage_roll_1, damage_roll_2)

    damage = damage_roll
    damage = damage + attacker.melee_damage

    defender.health -= damage
    ui.HitBox(attacker.current_map, defender.sprite.rect.x, defender.sprite.rect.y, damage, attacker.my_type)




