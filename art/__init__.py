import pygame
import utilities
import spritesheet

pygame.init()
pygame.display.set_mode([0, 0])

#NPCs
m_villager_image_1 = pygame.image.load("art/npc/villagers/male_villager_1.png").convert()
m_villager_image_2 = pygame.image.load("art/npc/villagers/male_villager_2.png").convert()
m_villager_image_3 = pygame.image.load("art/npc/villagers/male_villager_3.png").convert()
m_villager_image_4 = pygame.image.load("art/npc/villagers/male_villager_4.png").convert()
male_villager_images = [m_villager_image_1, m_villager_image_2, m_villager_image_3, m_villager_image_4]
for each in male_villager_images:
    each.set_colorkey(utilities.colors.key)
guard_image = pygame.image.load("art/npc/guard.png").convert()
guard_image.set_colorkey(utilities.colors.key)

merchant_image = pygame.image.load("art/npc/merchant.png").convert()
merchant_image.set_colorkey(utilities.colors.key)


# Structures
stone_wall_image = pygame.image.load("art/structures/walls/wall.png").convert()

house_interior_wall = pygame.image.load("art/structures/walls/house_interior_1.png")

vertical_palisade_1 = pygame.image.load("art/structures/walls/v_palisade_1.png").convert()
vertical_palisade_2 = pygame.image.load("art/structures/walls/v_palisade_2.png").convert()
vertical_palisade_1.set_colorkey(utilities.colors.key)
vertical_palisade_2.set_colorkey(utilities.colors.key)
vertical_palisade_images = [vertical_palisade_1, vertical_palisade_2]

horizontal_palisade_1 = pygame.image.load("art/structures/walls/h_palisade_1.png").convert()
horizontal_palisade_2 = pygame.image.load("art/structures/walls/h_palisade_2.png").convert()
horizontal_palisade_3 = pygame.image.load("art/structures/walls/h_palisade_3.png").convert()
horizontal_palisade_1.set_colorkey(utilities.colors.key)
horizontal_palisade_2.set_colorkey(utilities.colors.key)
horizontal_palisade_3.set_colorkey(utilities.colors.key)
horizontal_palisade_images = [horizontal_palisade_1, horizontal_palisade_2, horizontal_palisade_3]
ul_palisade = pygame.image.load("art/structures/walls/ul_palisade_corner.png").convert()
ul_palisade.set_colorkey(utilities.colors.key)
ur_palisade = pygame.image.load("art/structures/walls/ur_palisade_corner.png").convert()
ur_palisade.set_colorkey(utilities.colors.key)
ll_palisade = pygame.image.load("art/structures/walls/ll_palisade_corner.png").convert()
ll_palisade.set_colorkey(utilities.colors.key)
lr_palisade = pygame.image.load("art/structures/walls/lr_palisade_corner.png").convert()
lr_palisade.set_colorkey(utilities.colors.key)

chest_image = pygame.image.load("art/structures/chest.png").convert()
chest_open_image = pygame.image.load("art/structures/chest_open.png").convert()
chest_image.set_colorkey(utilities.colors.key)
chest_open_image.set_colorkey(utilities.colors.key)

signpost_image = pygame.image.load("art/structures/signpost.png").convert()
signpost_image.set_colorkey(utilities.colors.key)

forge_image = pygame.image.load("art/structures/forge.png").convert()
forge_image.set_colorkey(utilities.colors.key)

anvil_image = pygame.image.load("art/structures/anvil.png").convert()
anvil_image.set_colorkey(utilities.colors.key)

door_image = pygame.image.load("art/structures/door.png").convert()
door_image.set_colorkey(utilities.colors.key)

vert_door_image = pygame.Surface([20, 40])
horiz_gate_image = pygame.Surface([40, 20])

small_thatch_house_image_1 = pygame.image.load("art/structures/houses/small_thatch_house_1.png").convert()
small_thatch_house_image_2 = pygame.image.load("art/structures/houses/small_thatch_house_2.png").convert()
small_thatch_house_image_3 = pygame.image.load("art/structures/houses/small_thatch_house_3.png").convert()
small_thatch_house_image_4 = pygame.image.load("art/structures/houses/small_thatch_house_4.png").convert()
small_thatch_house_image_5 = pygame.image.load("art/structures/houses/small_thatch_house_5.png").convert()
small_thatch_house_image_1.set_colorkey(utilities.colors.key)
small_thatch_house_image_2.set_colorkey(utilities.colors.key)
small_thatch_house_image_3.set_colorkey(utilities.colors.key)
small_thatch_house_image_4.set_colorkey(utilities.colors.key)
small_thatch_house_image_5.set_colorkey(utilities.colors.key)
small_thatch_house_images = [small_thatch_house_image_1,
                             small_thatch_house_image_2,
                             small_thatch_house_image_3,
                             small_thatch_house_image_4,
                             small_thatch_house_image_5]
small_shingle_house_image_1 = pygame.image.load("art/structures/houses/small_shingle_house_1.png").convert()
small_shingle_house_image_2 = pygame.image.load("art/structures/houses/small_shingle_house_2.png").convert()
small_shingle_house_image_3 = pygame.image.load("art/structures/houses/small_shingle_house_3.png").convert()
small_shingle_house_image_4 = pygame.image.load("art/structures/houses/small_shingle_house_4.png").convert()
small_shingle_house_image_5 = pygame.image.load("art/structures/houses/small_shingle_house_5.png").convert()
small_shingle_house_image_1.set_colorkey(utilities.colors.key)
small_shingle_house_image_2.set_colorkey(utilities.colors.key)
small_shingle_house_image_3.set_colorkey(utilities.colors.key)
small_shingle_house_image_4.set_colorkey(utilities.colors.key)
small_shingle_house_image_5.set_colorkey(utilities.colors.key)
small_shingle_house_images = [small_shingle_house_image_1,
                              small_shingle_house_image_2,
                              small_shingle_house_image_3,
                              small_shingle_house_image_4,
                              small_shingle_house_image_5]

medium_shingle_house_image_1 = pygame.image.load("art/structures/houses/medium_shingle_house_1.png").convert()
medium_shingle_house_image_2 = pygame.image.load("art/structures/houses/medium_shingle_house_2.png").convert()
medium_shingle_house_image_3 = pygame.image.load("art/structures/houses/medium_shingle_house_3.png").convert()
medium_shingle_house_image_4 = pygame.image.load("art/structures/houses/medium_shingle_house_4.png").convert()
medium_shingle_house_image_1.set_colorkey(utilities.colors.key)
medium_shingle_house_image_2.set_colorkey(utilities.colors.key)
medium_shingle_house_image_3.set_colorkey(utilities.colors.key)
medium_shingle_house_image_4.set_colorkey(utilities.colors.key)
medium_shingle_house_images = [medium_shingle_house_image_1,
                               medium_shingle_house_image_2,
                               medium_shingle_house_image_3,
                               medium_shingle_house_image_4]
medium_thatch_house_image_1 = pygame.image.load("art/structures/houses/medium_thatch_house_1.png").convert()
medium_thatch_house_image_2 = pygame.image.load("art/structures/houses/medium_thatch_house_2.png").convert()
medium_thatch_house_image_3 = pygame.image.load("art/structures/houses/medium_thatch_house_3.png").convert()
medium_thatch_house_image_4 = pygame.image.load("art/structures/houses/medium_thatch_house_4.png").convert()
medium_thatch_house_image_1.set_colorkey(utilities.colors.key)
medium_thatch_house_image_2.set_colorkey(utilities.colors.key)
medium_thatch_house_image_3.set_colorkey(utilities.colors.key)
medium_thatch_house_image_4.set_colorkey(utilities.colors.key)
medium_thatch_house_images = [medium_thatch_house_image_1,
                              medium_thatch_house_image_2,
                              medium_thatch_house_image_3,
                              medium_thatch_house_image_4]

large_shingle_house_image = pygame.image.load("art/structures/houses/large_house_1.png").convert()
large_shingle_house_image.set_colorkey(utilities.colors.key)

#Flora
tree_image_1 = pygame.image.load("art/tree/large_tree_1.png")
tree_image_2 = pygame.image.load("art/tree/large_tree_2.png")
tree_image_3 = pygame.image.load("art/tree/large_tree_3.png")
tree_image_4 = pygame.image.load("art/tree/large_tree_4.png")
tree_image_5 = pygame.image.load("art/tree/large_tree_5.png")
tree_image_6 = pygame.image.load("art/tree/large_tree_6.png")
tree_image_1.set_colorkey(utilities.colors.key)
tree_image_2.set_colorkey(utilities.colors.key)
tree_image_3.set_colorkey(utilities.colors.key)
tree_image_4.set_colorkey(utilities.colors.key)
tree_image_5.set_colorkey(utilities.colors.key)
tree_image_6.set_colorkey(utilities.colors.key)
pine_tree_images = [tree_image_1, tree_image_2, tree_image_3, tree_image_4, tree_image_5, tree_image_6]

#creatures
skeleton_image = pygame.image.load("art/creatures/skeleton.png").convert()
skeleton_image.set_colorkey(utilities.colors.key)
grievebeast_image = pygame.image.load("art/creatures/grievebeast.png").convert()
grievebeast_image.set_colorkey(utilities.colors.key)
shadebrute_spritesheet = spritesheet.Spritesheet("art/creatures/shadebrute.png")

#weapons
axe_spritesheet = spritesheet.Spritesheet("art/weapons/melee/axe.png")
sword_spritesheet = spritesheet.Spritesheet("art/weapons/melee/sword.png")
bow_spritesheet = spritesheet.Spritesheet("art/weapons/ranged/bow.png")
mace_spritesheet = spritesheet.Spritesheet("art/weapons/melee/mace.png")
spear_spritesheet = spritesheet.Spritesheet("art/weapons/melee/spear.png")
dagger_spritesheet = spritesheet.Spritesheet("art/weapons/melee/dagger.png")

#projectiles
arrow_image = pygame.image.load("art/weapons/projectiles/arrow.png")
arrow_image.set_colorkey(utilities.colors.key)

#ui
inventory_background = pygame.image.load("art/ui_elements/inventory/inventory_window.png")
small_left_arrow_deselected_image = pygame.image.load("art/ui_elements/inventory/small_left_arrow_deselected.png")
small_left_arrow_selected_image = pygame.image.load("art/ui_elements/inventory/small_left_arrow_selected.png")
small_right_arrow_deselected_image = pygame.image.load("art/ui_elements/inventory/small_right_arrow_deselected.png")
small_right_arrow_selected_image = pygame.image.load("art/ui_elements/inventory/small_right_arrow_selected.png")
equip_deselected_image = pygame.image.load("art/ui_elements/inventory/equip_deselected.png")
equip_selected_image = pygame.image.load("art/ui_elements/inventory/equip_selected.png")
stats_selected_image = pygame.image.load("art/ui_elements/inventory/stats_selected.png")
stats_deselected_image = pygame.image.load("art/ui_elements/inventory/stats_deselected.png")

weapon_icon = pygame.image.load("art/ui_elements/inventory/icon_weapon.png")
old_bow_icon = pygame.image.load("art/ui_elements/inventory/icon_bow.png")
shield_icon = pygame.image.load("art/ui_elements/inventory/icon_shield.png")
spell_icon = pygame.image.load("art/ui_elements/inventory/icon_spell.png")
armor_icon = pygame.image.load("art/ui_elements/inventory/icon_armor.png")

sword_icon = pygame.image.load("art/ui_elements/inventory/icons/icon_sword.png")
spear_icon = pygame.image.load("art/ui_elements/inventory/icons/icon_spear.png")
dagger_icon = pygame.image.load("art/ui_elements/inventory/icons/icon_dagger.png")
bow_icon = pygame.image.load("art/ui_elements/inventory/icons/icon_bow.png")
mace_icon = pygame.image.load("art/ui_elements/inventory/icons/icon_mace.png")
axe_icon = pygame.image.load("art/ui_elements/inventory/icons/icon_axe.png")

boots_icon = pygame.image.load("art/ui_elements/inventory/icons/icon_boots.png")

# terrain
dirt_tile_image = pygame.image.load("art/tiles/dirt_1.png")
flagstone_tile_image = pygame.image.load("art/tiles/flagstone_1.png")
wood_tile_1_image = pygame.image.load("art/tiles/wood_1.png")
wood_tile_2_image = pygame.image.load("art/tiles/wood_2.png")
wood_tile_3_image = pygame.image.load("art/tiles/wood_3_large.png")
grass_tile_1_image = pygame.image.load("art/tiles/grass_1.png")
grass_tile_2_image = pygame.image.load("art/tiles/grass_2.png")
grass_tile_3_image = pygame.image.load("art/tiles/grass_3.png")
grass_tile_4_image = pygame.image.load("art/tiles/grass_4.png")
grass_tile_5_image = pygame.image.load("art/tiles/grass_5.png")
marble_tile_1_image = pygame.image.load("art/tiles/marble_1.png")
stone_block_tile_image = pygame.image.load("art/tiles/stone_block.png")
stone_floor_tile_gray_image = pygame.image.load("art/tiles/stone_floor.png")
stone_floor_tile_brown_image = pygame.image.load("art/tiles/stone_floor_brown.png")
water_tile_image = pygame.image.load("art/tiles/water_1.png")
dirt_path_elbow_1 = pygame.image.load("art/tiles/dirt_path_elbow_1.png")
dirt_path_elbow_2 = pygame.image.load("art/tiles/dirt_path_elbow_2.png")
dirt_path_elbow_3 = pygame.image.load("art/tiles/dirt_path_elbow_3.png")
dirt_path_elbow_4 = pygame.image.load("art/tiles/dirt_path_elbow_4.png")
dirt_path_horizontal_1 = pygame.image.load("art/tiles/path_horizontal_1.png")
dirt_path_horizontal_2 = pygame.image.load("art/tiles/path_horizontal_2.png")
dirt_path_horizontal_3 = pygame.image.load("art/tiles/path_horizontal_3.png")
dirt_path_vertical_1 = pygame.image.load("art/tiles/path_vertical_1.png")
dirt_path_vertical_2 = pygame.image.load("art/tiles/path_vertical_2.png")
dirt_path_vertical_3 = pygame.image.load("art/tiles/path_vertical_3.png")
dirt_path_vertical_4 = pygame.image.load("art/tiles/path_vertical_4.png")
dirt_path_t_up = pygame.image.load("art/tiles/dirt_path_t_up.png")
dirt_path_t_down = pygame.image.load("art/tiles/dirt_path_t_down.png")
dirt_path_t_left = pygame.image.load("art/tiles/dirt_path_t_left.png")
dirt_path_t_right = pygame.image.load("art/tiles/dirt_path_t_right.png")
dirt_path_4_way = pygame.image.load("art/tiles/dirt_path_4_way.png")
paths = [dirt_path_elbow_1,
         dirt_path_elbow_2,
         dirt_path_elbow_3,
         dirt_path_elbow_4,
         dirt_path_horizontal_1,
         dirt_path_horizontal_2,
         dirt_path_horizontal_3,
         dirt_path_vertical_1,
         dirt_path_vertical_2,
         dirt_path_vertical_3,
         dirt_path_vertical_4,
         dirt_path_t_up,
         dirt_path_t_down,
         dirt_path_t_left,
         dirt_path_t_right,
         dirt_path_4_way]

for each in paths:
    each.set_colorkey(utilities.colors.key)

tile_images = {"Dirt": dirt_tile_image,
               "Flagstone": flagstone_tile_image,
               "Wood 1": wood_tile_1_image,
               "Wood 2": wood_tile_2_image,
               "Wood 3": wood_tile_3_image,
               "Grass 1": grass_tile_1_image,
               "Grass 2": grass_tile_2_image,
               "Grass 3": grass_tile_3_image,
               "Grass 4": grass_tile_4_image,
               "Grass 5": grass_tile_5_image,
               "Marble 1": marble_tile_1_image,
               "Stone Block": stone_block_tile_image,
               "Stone Floor Grey": stone_floor_tile_gray_image,
               "Stone Floor Brown": stone_floor_tile_brown_image,
               "Dirt Path Horizontal": dirt_path_horizontal_1,
               "Dirt Path Vertical": dirt_path_vertical_1,
               "Dirt Path Elbow LD": dirt_path_elbow_4,
               "Dirt Path Elbow LU": dirt_path_elbow_1,
               "Dirt Path Elbow RD": dirt_path_elbow_3,
               "Dirt Path Elbow RU": dirt_path_elbow_2,
               "Dirt Path T UP": dirt_path_t_up,
               "Dirt Path T Down": dirt_path_t_down,
               "Dirt Path T Left": dirt_path_t_left,
               "Dirt Path T Right": dirt_path_t_right,
               "Dirt Path 4 Way": dirt_path_4_way,
               "Water": water_tile_image}
