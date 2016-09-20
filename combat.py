import pygame
import ui
import random
import utilities

pygame.init()
pygame.display.set_mode([0, 0])


def fight_tick(screen, player, enemy):
    player.time_since_last_attack += 1
    enemy.time_since_last_attack += 1
    if player.time_since_last_attack > player.speed * 10:
        player.time_since_last_attack = 0
        accuracy_roll_1 = utilities.roll_dice(2, player.accuracy)
        accuracy_roll_2 = utilities.roll_dice(2, player.accuracy)
        accuracy_roll = min(accuracy_roll_1, accuracy_roll_2)
        if accuracy_roll < player.accuracy:
            strike(player, enemy)
    if enemy.time_since_last_attack > enemy.speed * 10:
        enemy.time_since_last_attack = 0
        accuracy_roll_1 = utilities.roll_dice(2, enemy.accuracy)
        accuracy_roll_2 = utilities.roll_dice(2, enemy.accuracy)
        accuracy_roll = min(accuracy_roll_1, accuracy_roll_2)
        if accuracy_roll < enemy.accuracy:
            strike(enemy, player)


def strike(attacker, defender):
    attacker.fight_frame = 1
    damage_roll_1 = utilities.roll_dice(1, attacker.attack)
    damage_roll_2 = utilities.roll_dice(1, attacker.attack)
    damage_roll = max(damage_roll_1, damage_roll_2)

    damage = damage_roll
    if attacker.equipped_weapon:
        damage = damage + attacker.equipped_weapon.attack

    defender.health -= damage_roll
    if defender.health <= 0:
        # defender.healthbar.active = False
        defender.expire()
        attacker.fighting = False
        #attacker.healthbar.active = False
    ui.HitBox(attacker.current_map, defender.sprite.rect.x, defender.sprite.rect.y, damage_roll, attacker.my_type)

# Let’s define a function for N repeated rolls of random(S+1), returning a number from 0 to N*S:


