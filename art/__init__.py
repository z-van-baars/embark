import pygame
import utilities
import spritesheet

pygame.init()
pygame.display.set_mode([0, 0])

image_dict = {}

#NPCs
m_villager_image_1 = pygame.image.load("art/npc/villagers/male_villager_1.png").convert()
m_villager_image_2 = pygame.image.load("art/npc/villagers/male_villager_2.png").convert()
m_villager_image_3 = pygame.image.load("art/npc/villagers/male_villager_3.png").convert()
m_villager_image_4 = pygame.image.load("art/npc/villagers/male_villager_4.png").convert()
male_villager_images = [m_villager_image_1, m_villager_image_2, m_villager_image_3, m_villager_image_4]
for each in male_villager_images:
    each.set_colorkey(utilities.colors.key)
image_dict['Male Villager'] = male_villager_images
guard_image = pygame.image.load("art/npc/guard.png").convert()
guard_image.set_colorkey(utilities.colors.key)
image_dict['Guard'] = [guard_image]

merchant_image = pygame.image.load("art/npc/merchant.png").convert()
merchant_image.set_colorkey(utilities.colors.key)
image_dict['Merchant'] = [merchant_image]

lord_image = pygame.image.load("art/npc/lord.png").convert()
lord_image.set_colorkey(utilities.colors.key)
image_dict['Lord'] = [lord_image]

sage_image_1 = pygame.image.load("art/npc/sage_1.png").convert()
sage_image_2 = pygame.image.load("art/npc/sage_2.png").convert()
sage_image_3 = pygame.image.load("art/npc/sage_3.png").convert()
sage_images = [sage_image_1, sage_image_2, sage_image_3]
for each in sage_images:
  each.set_colorkey(utilities.colors.key)
image_dict['Sage'] = sage_images

# Structures
wall_topper_right = pygame.image.load("art/structures/wall_top_right.png").convert()
wall_topper_right.set_colorkey(utilities.colors.key)
image_dict["Wall Top Right"] = [wall_topper_right]
wall_topper_left = pygame.image.load("art/structures/wall_top_left.png").convert()
wall_topper_left.set_colorkey(utilities.colors.key)
image_dict["Wall Top Left"] = [wall_topper_left]
wall_topper = pygame.image.load("art/structures/wall_top.png").convert()
wall_topper.set_colorkey(utilities.colors.key)
image_dict["Wall Top Bottom"] = [wall_topper]

wall_topper_full = pygame.image.load("art/structures/wall_top_full.png").convert()
wall_topper_full.set_colorkey(utilities.colors.key)
image_dict["Wall Top Full"] = [wall_topper_full]

wall_topper_tall = pygame.image.load("art/structures/wall_top_tall.png").convert()
wall_topper_tall.set_colorkey(utilities.colors.key)
image_dict["Wall Top Tall"] = [wall_topper_tall]

wall_topper_large = pygame.image.load("art/structures/wall_top_2_2.png").convert()
wall_topper_large.set_colorkey(utilities.colors.key)
image_dict["Wall Top Large"] = [wall_topper_large]

wood_fence_horiz = pygame.image.load("art/structures/walls/wood_fence_lr.png").convert()
wood_fence_horiz.set_colorkey(utilities.colors.key)
image_dict["Wood Fence H"] = [wood_fence_horiz]
wood_fence_vert = pygame.image.load("art/structures/walls/wood_fence_ud.png").convert()
wood_fence_vert.set_colorkey(utilities.colors.key)
image_dict["Wood Fence V"] = [wood_fence_vert]
wood_fence_upper_left = pygame.image.load("art/structures/walls/wood_fence_ul.png").convert()
wood_fence_upper_left.set_colorkey(utilities.colors.key)
image_dict["Wood Fence UL"] = [wood_fence_upper_left]
wood_fence_upper_right = pygame.image.load("art/structures/walls/wood_fence_ur.png").convert()
wood_fence_upper_right.set_colorkey(utilities.colors.key)
image_dict["Wood Fence UR"] = [wood_fence_upper_right]
wood_fence_lower_left = pygame.image.load("art/structures/walls/wood_fence_dl.png").convert()
wood_fence_lower_left.set_colorkey(utilities.colors.key)
image_dict["Wood Fence LL"] = [wood_fence_lower_left]
wood_fence_lower_right = pygame.image.load("art/structures/walls/wood_fence_dr.png").convert()
wood_fence_lower_right.set_colorkey(utilities.colors.key)
image_dict["Wood Fence LR"] = [wood_fence_lower_right]
wood_fence_down = pygame.image.load("art/structures/walls/wood_fence_dt.png").convert()
wood_fence_down.set_colorkey(utilities.colors.key)
image_dict["Wood Fence Down"] = [wood_fence_down]
wood_fence_up = pygame.image.load("art/structures/walls/wood_fence_ut.png").convert()
wood_fence_up.set_colorkey(utilities.colors.key)
image_dict["Wood Fence Up"] = [wood_fence_up]
wood_fence_left = pygame.image.load("art/structures/walls/wood_fence_l.png").convert()
wood_fence_left.set_colorkey(utilities.colors.key)
image_dict["Wood Fence Left"] = [wood_fence_left]
wood_fence_right = pygame.image.load("art/structures/walls/wood_fence_r.png").convert()
wood_fence_right.set_colorkey(utilities.colors.key)
image_dict["Wood Fence Right"] = [wood_fence_right]
wood_fence_4_way = pygame.image.load("art/structures/walls/wood_fence_4way.png").convert()
wood_fence_4_way.set_colorkey(utilities.colors.key)
image_dict["Wood Fence 4 Way"] = [wood_fence_4_way]
wood_fence_vert_right = pygame.image.load("art/structures/walls/wood_fence_udr.png").convert()
wood_fence_vert_right.set_colorkey(utilities.colors.key)
image_dict["Wood Fence VR"] = [wood_fence_vert_right]
wood_fence_vert_left = pygame.image.load("art/structures/walls/wood_fence_udl.png").convert()
wood_fence_vert_left.set_colorkey(utilities.colors.key)
image_dict["Wood Fence VL"] = [wood_fence_vert_left]
wood_fence_horiz_up = pygame.image.load("art/structures/walls/wood_fence_lru.png").convert()
wood_fence_horiz_up.set_colorkey(utilities.colors.key)
image_dict["Wood Fence HU"] = [wood_fence_horiz_up]
wood_fence_horiz_down = pygame.image.load("art/structures/walls/wood_fence_lrd.png").convert()
wood_fence_horiz_down.set_colorkey(utilities.colors.key)
image_dict["Wood Fence HD"] = [wood_fence_horiz_down]

stone_wall = pygame.image.load("art/structures/walls/interior_stone_wall_1.png").convert()
image_dict["Stone Wall"] = [stone_wall]
stone_wall_tall = pygame.image.load("art/structures/walls/interior_stone_wall_tall.png").convert()
image_dict["Stone Wall Tall"] = [stone_wall_tall]
stone_wall_chains = pygame.image.load("art/structures/walls/interior_stone_wall_tall_chains.png").convert()
image_dict["Stone Wall Chains"] = [stone_wall_chains]
stone_wall_torch = pygame.image.load("art/structures/walls/interior_stone_wall_tall_torch.png").convert()
image_dict["Stone Wall Torch"] = [stone_wall_chains]

house_interior_wall = pygame.image.load("art/structures/walls/house_interior_1.png").convert()
image_dict["House Interior Wall"] = [house_interior_wall]
house_interior_wall_tall = pygame.image.load("art/structures/walls/house_interior_1_tall.png").convert()
image_dict["House Interior Wall Tall"] = [house_interior_wall_tall]
house_interior_wall_wide = pygame.image.load("art/structures/walls/house_interior_1_wide.png").convert()
image_dict["House Interior Wall Wide"] = [house_interior_wall_wide]

vertical_palisade_1 = pygame.image.load("art/structures/walls/v_palisade_1.png").convert()
vertical_palisade_2 = pygame.image.load("art/structures/walls/v_palisade_2.png").convert()
vertical_palisade_1.set_colorkey(utilities.colors.key)
vertical_palisade_2.set_colorkey(utilities.colors.key)

vertical_palisade_images = [vertical_palisade_1, vertical_palisade_2]
image_dict["Palisade Vertical"] = vertical_palisade_images

horizontal_palisade_1 = pygame.image.load("art/structures/walls/h_palisade_1.png").convert()
horizontal_palisade_2 = pygame.image.load("art/structures/walls/h_palisade_2.png").convert()
horizontal_palisade_3 = pygame.image.load("art/structures/walls/h_palisade_3.png").convert()
horizontal_palisade_1.set_colorkey(utilities.colors.key)
horizontal_palisade_2.set_colorkey(utilities.colors.key)
horizontal_palisade_3.set_colorkey(utilities.colors.key)
horizontal_palisade_images = [horizontal_palisade_1, horizontal_palisade_2, horizontal_palisade_3]
image_dict["Palisade Horizontal"] = horizontal_palisade_images
ul_palisade = pygame.image.load("art/structures/walls/ul_palisade_corner.png").convert()
ul_palisade.set_colorkey(utilities.colors.key)
image_dict["UL Palisade"] = [ul_palisade]
ur_palisade = pygame.image.load("art/structures/walls/ur_palisade_corner.png").convert()
ur_palisade.set_colorkey(utilities.colors.key)
image_dict["UR Palisade"] = [ur_palisade]
ll_palisade = pygame.image.load("art/structures/walls/ll_palisade_corner.png").convert()
ll_palisade.set_colorkey(utilities.colors.key)
image_dict["LL Palisade"] = [ll_palisade]
lr_palisade = pygame.image.load("art/structures/walls/lr_palisade_corner.png").convert()
lr_palisade.set_colorkey(utilities.colors.key)
image_dict["LR Palisade"] = [lr_palisade]

chest_image = pygame.image.load("art/structures/chest.png").convert()
chest_open_image = pygame.image.load("art/structures/chest_open.png").convert()
chest_image.set_colorkey(utilities.colors.key)
chest_open_image.set_colorkey(utilities.colors.key)
image_dict["Chest"] = [chest_image]
image_dict["Open Chest"] = [chest_open_image]

signpost_image = pygame.image.load("art/structures/signpost.png").convert()
signpost_image.set_colorkey(utilities.colors.key)
image_dict["Signpost"] = [signpost_image]

forge_image = pygame.image.load("art/structures/forge.png").convert()
forge_image.set_colorkey(utilities.colors.key)
image_dict["Forge"] = [forge_image]

anvil_image = pygame.image.load("art/structures/anvil.png").convert()
anvil_image.set_colorkey(utilities.colors.key)
image_dict["Anvil"] = [anvil_image]

door_image = pygame.image.load("art/structures/door.png").convert()
door_image.set_colorkey(utilities.colors.key)
image_dict["Door"] = [door_image]

vert_door_image = pygame.Surface([20, 40])
image_dict["Vert Gate"] = [vert_door_image]
horiz_gate_image = pygame.Surface([40, 20])
image_dict["Horiz Gate"] = [horiz_gate_image]

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
image_dict["House Small Thatch"] = small_thatch_house_images
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
image_dict["House Small Shingle"] = small_shingle_house_images

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
image_dict["House Medium Shingle"] = medium_shingle_house_images
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
image_dict["House Medium Thatch"] = medium_thatch_house_images

large_shingle_house_image = pygame.image.load("art/structures/houses/large_house_1.png").convert()
large_shingle_house_image.set_colorkey(utilities.colors.key)
image_dict["House Large Shingle"] = [large_shingle_house_image]

stairs_up_image = pygame.image.load("art/structures/stairs_up.png").convert()
stairs_up_image.set_colorkey(utilities.colors.key)
image_dict["Stairs Up"] = [stairs_up_image]
stairs_down_image = pygame.image.load("art/structures/stairs_down.png").convert()
image_dict["Stairs Down"] = [stairs_down_image]

dungeon_entrance = pygame.image.load("art/structures/dungeon/dungeon_entrance.png").convert()
dungeon_entrance.set_colorkey(utilities.colors.key)
image_dict["Dungeon Entrance"] = [dungeon_entrance]

#Furniture
desk_backward_image = pygame.image.load("art/structures/furniture/desk_backward.png").convert()
desk_forward_image = pygame.image.load("art/structures/furniture/desk_forward.png").convert()
narrow_bookshelf_short_empty_image = pygame.image.load("art/structures/furniture/narrow_bookshelf_short_empty.png").convert()
wardrobe_narrow_short_image = pygame.image.load("art/structures/furniture/wardrobe_narrow_short.png").convert()
wardrobe_narrow_tall_image = pygame.image.load("art/structures/furniture/wardrobe_narrow_tall.png").convert()
wardrobe_short_image = pygame.image.load("art/structures/furniture/wardrobe_short.png").convert()
wide_bookshelf_short_empty_image = pygame.image.load("art/structures/furniture/wide_bookshelf_short_empty.png").convert()

chair_forward_image = pygame.image.load("art/structures/furniture/chair_1.png").convert()
chair_backward_image = pygame.image.load("art/structures/furniture/chair_2.png").convert()
empty_table_image = pygame.image.load("art/structures/furniture/table_empty.png").convert()
table_image_1 = pygame.image.load("art/structures/furniture/table_1.png").convert()
table_image_2 = pygame.image.load("art/structures/furniture/table_2.png").convert()
table_image_3 = pygame.image.load("art/structures/furniture/table_3.png").convert()
table_image_4 = pygame.image.load("art/structures/furniture/table_4.png").convert()
barrel_vertical_image = pygame.image.load("art/structures/furniture/barrel_1.png").convert()
barrel_horizontal_image = pygame.image.load("art/structures/furniture/barrel_2.png").convert()
pot_image_1 = pygame.image.load("art/structures/furniture/pot_1.png").convert()
pot_image_2 = pygame.image.load("art/structures/furniture/pot_2.png").convert()
pot_image_3 = pygame.image.load("art/structures/furniture/pot_3.png").convert()
pot_image_4 = pygame.image.load("art/structures/furniture/pot_4.png").convert()
wardrobe_image = pygame.image.load("art/structures/furniture/wardrobe_1.png").convert()
narrow_bookshelf_empty_image = pygame.image.load("art/structures/furniture/narrow_bookshelf_empty.png").convert()
narrow_bookshelf_image_1 = pygame.image.load("art/structures/furniture/narrow_bookshelf_1.png").convert()
narrow_bookshelf_image_2 = pygame.image.load("art/structures/furniture/narrow_bookshelf_2.png").convert()
narrow_bookshelf_image_3 = pygame.image.load("art/structures/furniture/narrow_bookshelf_3.png").convert()
narrow_bookshelf_image_4 = pygame.image.load("art/structures/furniture/narrow_bookshelf_4.png").convert()
wide_bookshelf_empty_image = pygame.image.load("art/structures/furniture/wide_bookshelf_empty.png").convert()
wide_bookshelf_image_1 = pygame.image.load("art/structures/furniture/wide_bookshelf_1.png").convert()
wide_bookshelf_image_2 = pygame.image.load("art/structures/furniture/wide_bookshelf_2.png").convert()
wide_bookshelf_image_3 = pygame.image.load("art/structures/furniture/wide_bookshelf_3.png").convert()
wide_bookshelf_image_4 = pygame.image.load("art/structures/furniture/wide_bookshelf_4.png").convert()
wide_bookshelf_image_5 = pygame.image.load("art/structures/furniture/wide_bookshelf_5.png").convert()
wide_bookshelf_image_6 = pygame.image.load("art/structures/furniture/wide_bookshelf_6.png").convert()
wood_crate_1_image = pygame.image.load("art/structures/furniture/wood_crate_1.png").convert()


furniture_images = [chair_forward_image,
                    chair_backward_image,
                    empty_table_image,
                    table_image_1,
                    table_image_2,
                    table_image_3,
                    table_image_4,
                    barrel_vertical_image,
                    barrel_horizontal_image,
                    pot_image_1,
                    pot_image_2,
                    pot_image_3,
                    pot_image_4,
                    wardrobe_image,
                    narrow_bookshelf_empty_image,
                    narrow_bookshelf_image_1,
                    narrow_bookshelf_image_2,
                    narrow_bookshelf_image_3,
                    narrow_bookshelf_image_4,
                    wide_bookshelf_empty_image,
                    wide_bookshelf_image_1,
                    wide_bookshelf_image_2,
                    wide_bookshelf_image_3,
                    wide_bookshelf_image_4,
                    wide_bookshelf_image_5,
                    wide_bookshelf_image_6,
                    wood_crate_1_image,
                    desk_backward_image,
                    desk_forward_image,
                    narrow_bookshelf_short_empty_image,
                    wardrobe_narrow_short_image,
                    wardrobe_narrow_tall_image,
                    wardrobe_short_image,
                    wide_bookshelf_short_empty_image
                    ]
for each in furniture_images:
    each.set_colorkey(utilities.colors.key)

image_dict["Chair Forward"] = [chair_forward_image]
image_dict["Chair Backward"] = [chair_backward_image]
image_dict["Wood Crate"] = [wood_crate_1_image]
image_dict["Pot"] = [pot_image_1,
                     pot_image_2,
                     pot_image_3,
                     pot_image_4]
image_dict["Barrel Horizontal"] = [barrel_horizontal_image]
image_dict["Barrel Vertical"] = [barrel_vertical_image]
image_dict["Table Empty"] = [empty_table_image]
image_dict["Table"] = [table_image_1,
                       table_image_2,
                       table_image_3,
                       table_image_4]
image_dict["Desk Forward"] = [desk_forward_image]
image_dict["Desk Backward"] = [desk_backward_image]
image_dict["Bookshelf Narrow Empty"] = [narrow_bookshelf_empty_image]
image_dict["Bookshelf Short Narrow Empty"] = [narrow_bookshelf_short_empty_image]
image_dict["Bookshelf Wide Empty"] = [wide_bookshelf_empty_image]
image_dict["Bookshelf Short Wide Empty"] = [wide_bookshelf_short_empty_image]
image_dict["Wardrobe"] = [wardrobe_image]
image_dict["Wardrobe Tall Narrow"] = [wardrobe_narrow_tall_image]
image_dict["Wardrobe Short Narrow"] = [wardrobe_narrow_short_image]
image_dict["Wardrobe Short"] = [wardrobe_short_image]

altar_regular = pygame.image.load("art/structures/dungeon/altar_1.png").convert()
altar_regular.set_colorkey(utilities.colors.key)
image_dict["Altar"] = [altar_regular]
altar_empty_1 = pygame.image.load("art/structures/dungeon/altar_empty.png").convert()
altar_empty_1.set_colorkey(utilities.colors.key)
image_dict["Altar Empty"] = [altar_empty_1]
altar_empty_2 = pygame.image.load("art/structures/dungeon/altar_empty_2.png").convert()
altar_empty_2.set_colorkey(utilities.colors.key)
image_dict["Altar Empty Writing"] = [altar_empty_2]
candelabra_image = pygame.image.load("art/structures/dungeon/candelabra_1.png").convert()
candelabra_image.set_colorkey(utilities.colors.key)
image_dict["Candelabra"] = [candelabra_image]

pot_images = [pot_image_1,
              pot_image_2,
              pot_image_3,
              pot_image_4]
table_images = [table_image_1,
                table_image_2,
                table_image_3,
                table_image_4]

narrow_bookshelf_images = [narrow_bookshelf_image_1,
                           narrow_bookshelf_image_2,
                           narrow_bookshelf_image_3,
                           narrow_bookshelf_image_4]
image_dict["Bookshelf"] = narrow_bookshelf_images

wide_bookshelf_images = [wide_bookshelf_image_1,
                         wide_bookshelf_image_2,
                         wide_bookshelf_image_3,
                         wide_bookshelf_image_4,
                         wide_bookshelf_image_5,
                         wide_bookshelf_image_6]
image_dict["Bookshelf Wide"] = wide_bookshelf_images


#Flora
pine_tree_images = [pygame.image.load("art/flora/trees/pine/pine_1.png").convert(),
                    pygame.image.load("art/flora/trees/pine/pine_2.png").convert(),
                    pygame.image.load("art/flora/trees/pine/pine_3.png").convert(),
                    pygame.image.load("art/flora/trees/pine/pine_4.png").convert(),
                    pygame.image.load("art/flora/trees/pine/pine_5.png").convert(),
                    pygame.image.load("art/flora/trees/pine/pine_6.png").convert()]
for each in pine_tree_images:
    each.set_colorkey(utilities.colors.key)
image_dict["Pine Tree"] = pine_tree_images

small_oak_regular_images = [pygame.image.load("art/flora/trees/oak/small/1.png").convert(),
                            pygame.image.load("art/flora/trees/oak/small/2.png").convert(),
                            pygame.image.load("art/flora/trees/oak/small/3.png").convert(),
                            pygame.image.load("art/flora/trees/oak/small/4.png").convert(),
                            pygame.image.load("art/flora/trees/oak/small/5.png").convert(),
                            pygame.image.load("art/flora/trees/oak/small/6.png").convert()]
image_dict["Small Oak Tree"] = small_oak_regular_images


small_oak_bare_images = [pygame.image.load("art/flora/trees/oak/small/bare_1.png").convert(),
                         pygame.image.load("art/flora/trees/oak/small/bare_2.png").convert(),
                         pygame.image.load("art/flora/trees/oak/small/bare_3.png").convert(),
                         pygame.image.load("art/flora/trees/oak/small/bare_4.png").convert(),
                         pygame.image.load("art/flora/trees/oak/small/bare_5.png").convert(),
                         pygame.image.load("art/flora/trees/oak/small/bare_6.png").convert()]
image_dict["Small Bare Oak Tree"] = small_oak_bare_images

small_oak_yellow_images = [pygame.image.load("art/flora/trees/oak/small/yellow_1.png").convert(),
                           pygame.image.load("art/flora/trees/oak/small/yellow_2.png").convert(),
                           pygame.image.load("art/flora/trees/oak/small/yellow_3.png").convert()]
image_dict["Small Yellow Oak Tree"] = small_oak_yellow_images

small_oak_brown_images = [pygame.image.load("art/flora/trees/oak/small/brown_1.png").convert(),
                          pygame.image.load("art/flora/trees/oak/small/brown_2.png").convert(),
                          pygame.image.load("art/flora/trees/oak/small/brown_3.png").convert()]

small_oak_red_images = [pygame.image.load("art/flora/trees/oak/small/red_1.png").convert(),
                        pygame.image.load("art/flora/trees/oak/small/red_2.png").convert(),
                        pygame.image.load("art/flora/trees/oak/small/red_3.png").convert()]

small_oak_orange_images = [pygame.image.load("art/flora/trees/oak/small/orange_1.png").convert(),
                           pygame.image.load("art/flora/trees/oak/small/orange_2.png").convert(),
                           pygame.image.load("art/flora/trees/oak/small/orange_3.png").convert()]

image_dict["Small Fall Oak Tree"] = (small_oak_brown_images +
                                     small_oak_orange_images +
                                     small_oak_red_images +
                                     small_oak_yellow_images)

master_small_oak_image_list = (small_oak_regular_images +
                               small_oak_yellow_images +
                               small_oak_red_images +
                               small_oak_brown_images +
                               small_oak_orange_images +
                               small_oak_bare_images)

for each in master_small_oak_image_list:
    each.set_colorkey(utilities.colors.key)


large_oak_regular_images = [pygame.image.load("art/flora/trees/oak/large/1.png").convert(),
                            pygame.image.load("art/flora/trees/oak/large/2.png").convert(),
                            pygame.image.load("art/flora/trees/oak/large/3.png").convert(),
                            pygame.image.load("art/flora/trees/oak/large/4.png").convert(),
                            pygame.image.load("art/flora/trees/oak/large/5.png").convert(),
                            pygame.image.load("art/flora/trees/oak/large/6.png").convert()]
image_dict["Large Oak Tree"] = large_oak_regular_images


large_oak_bare_images = [pygame.image.load("art/flora/trees/oak/large/bare_1.png").convert(),
                         pygame.image.load("art/flora/trees/oak/large/bare_2.png").convert(),
                         pygame.image.load("art/flora/trees/oak/large/bare_3.png").convert()]

image_dict["Large Bare Oak Tree"] = large_oak_bare_images
large_oak_bare_dark_images = [pygame.image.load("art/flora/trees/oak/large/bare_4.png").convert(),
                              pygame.image.load("art/flora/trees/oak/large/bare_5.png").convert(),
                              pygame.image.load("art/flora/trees/oak/large/bare_6.png").convert(),
                              pygame.image.load("art/flora/trees/oak/large/bare_7.png").convert()]
image_dict["Large Dark Bare Oak Tree"] = large_oak_bare_dark_images
large_oak_yellow_images = [pygame.image.load("art/flora/trees/oak/large/yellow_1.png").convert(),
                           pygame.image.load("art/flora/trees/oak/large/yellow_2.png").convert(),
                           pygame.image.load("art/flora/trees/oak/large/yellow_3.png").convert()]
image_dict["Large Yellow Oak Tree"] = large_oak_yellow_images

large_oak_brown_images = [pygame.image.load("art/flora/trees/oak/large/brown_1.png").convert(),
                          pygame.image.load("art/flora/trees/oak/large/brown_2.png").convert(),
                          pygame.image.load("art/flora/trees/oak/large/brown_3.png").convert()]

large_oak_red_images = [pygame.image.load("art/flora/trees/oak/large/red_1.png").convert(),
                        pygame.image.load("art/flora/trees/oak/large/red_2.png").convert(),
                        pygame.image.load("art/flora/trees/oak/large/red_3.png").convert()]

large_oak_orange_images = [pygame.image.load("art/flora/trees/oak/large/orange_1.png").convert(),
                           pygame.image.load("art/flora/trees/oak/large/orange_2.png").convert(),
                           pygame.image.load("art/flora/trees/oak/large/orange_3.png").convert()]

image_dict["Large Fall Oak Tree"] = (large_oak_brown_images +
                                     large_oak_orange_images +
                                     large_oak_red_images +
                                     large_oak_yellow_images)
master_large_oak_image_list = (large_oak_regular_images +
                               large_oak_yellow_images +
                               large_oak_red_images +
                               large_oak_brown_images +
                               large_oak_orange_images +
                               large_oak_bare_images +
                               large_oak_bare_dark_images)

for each in master_large_oak_image_list:
    each.set_colorkey(utilities.colors.key)









wheat_image_1 = pygame.image.load("art/flora/wheat/wheat_1.png").convert()
wheat_image_1.set_colorkey(utilities.colors.key)
wheat_image_2 = pygame.image.load("art/flora/wheat/wheat_2.png").convert()
wheat_image_2.set_colorkey(utilities.colors.key)
wheat_image_3 = pygame.image.load("art/flora/wheat/wheat_3.png").convert()
wheat_image_3.set_colorkey(utilities.colors.key)
wheat_image_4 = pygame.image.load("art/flora/wheat/wheat_4.png").convert()
wheat_image_4.set_colorkey(utilities.colors.key)
wheat_image_5 = pygame.image.load("art/flora/wheat/wheat_5.png").convert()
wheat_image_5.set_colorkey(utilities.colors.key)
wheat_image_6 = pygame.image.load("art/flora/wheat/wheat_6.png").convert()
wheat_image_6.set_colorkey(utilities.colors.key)
wheat_images = [wheat_image_1,
                wheat_image_2,
                wheat_image_3]

#creatures
cow_spritesheet = spritesheet.Spritesheet("art/creatures/cow.png")
skeleton_image = pygame.image.load("art/creatures/skeleton.png").convert()
skeleton_image.set_colorkey(utilities.colors.key)
grievebeast_image = pygame.image.load("art/creatures/grievebeast.png").convert()
grievebeast_image.set_colorkey(utilities.colors.key)
doompaw_image = pygame.image.load("art/creatures/doompaw.png").convert()
doompaw_image.set_colorkey(utilities.colors.key)
shadebrute_spritesheet = spritesheet.Spritesheet("art/creatures/shadebrute.png")
cindermask_image = pygame.image.load("art/creatures/cindermask.png").convert()
cindermask_image.set_colorkey(utilities.colors.key)

#corpses
cindermask_corpse = pygame.image.load("art/creatures/corpses/corpse_cindermask.png").convert()
skeleton_corpse = pygame.image.load("art/creatures/corpses/corpse_skeleton.png").convert()
cindermask_corpse.set_colorkey(utilities.colors.key)
skeleton_corpse.set_colorkey(utilities.colors.key)

image_dict["Cindermask Corpse"] = [cindermask_corpse]
image_dict["Skeleton Corpse"] = [skeleton_corpse]
image_dict["Shadebrute Corpse"] = [skeleton_corpse]
image_dict["Grievebeast Corpse"] = [skeleton_corpse]
image_dict["Doompaw Corpse"] = skeleton_corpse

#weapons
axe_spritesheet = spritesheet.Spritesheet("art/weapons/melee/axe.png")
sword_spritesheet = spritesheet.Spritesheet("art/weapons/melee/sword.png")
bow_spritesheet = spritesheet.Spritesheet("art/weapons/ranged/bow.png")
mace_spritesheet = spritesheet.Spritesheet("art/weapons/melee/mace.png")
spear_spritesheet = spritesheet.Spritesheet("art/weapons/melee/spear.png")
dagger_spritesheet = spritesheet.Spritesheet("art/weapons/melee/dagger.png")

#projectiles
arrow_image = pygame.image.load("art/weapons/projectiles/arrow.png").convert()
arrow_image.set_colorkey(utilities.colors.key)
blue_fireball_spritesheet = spritesheet.Spritesheet("art/weapons/projectiles/blue_fireball_spritesheet.png")

#ui
npc_edit_window = pygame.image.load("art/ui_elements/npc_editor/npc_edit_window.png").convert()

edit_dialogue_deselected = pygame.image.load("art/ui_elements/npc_editor/edit_dialogue_deselected.png").convert()
edit_dialogue_selected = pygame.image.load("art/ui_elements/npc_editor/edit_dialogue_selected.png").convert()
edit_gold_deselected = pygame.image.load("art/ui_elements/npc_editor/edit_gold_deselected.png").convert()
edit_gold_selected = pygame.image.load("art/ui_elements/npc_editor/edit_gold_selected.png").convert()
edit_items_deselected = pygame.image.load("art/ui_elements/npc_editor/edit_items_deselected.png").convert()
edit_items_selected = pygame.image.load("art/ui_elements/npc_editor/edit_items_selected.png").convert()
edit_name_deselected = pygame.image.load("art/ui_elements/npc_editor/edit_name_deselected.png").convert()
edit_name_selected = pygame.image.load("art/ui_elements/npc_editor/edit_name_selected.png").convert()
edit_quests_deselected = pygame.image.load("art/ui_elements/npc_editor/edit_quests_deselected.png").convert()
edit_quests_selected = pygame.image.load("art/ui_elements/npc_editor/edit_quests_selected.png").convert()
edit_stock_deselected = pygame.image.load("art/ui_elements/npc_editor/edit_stock_deselected.png").convert()
edit_stock_selected = pygame.image.load("art/ui_elements/npc_editor/edit_stock_selected.png").convert()






inventory_background = pygame.image.load("art/ui_elements/inventory/inventory_window.png").convert()
equip_deselected_image = pygame.image.load("art/ui_elements/inventory/equip_deselected.png").convert()
equip_deselected_image.set_colorkey(utilities.colors.key)
equip_selected_image = pygame.image.load("art/ui_elements/inventory/equip_selected.png").convert()
equip_selected_image.set_colorkey(utilities.colors.key)
stats_selected_image = pygame.image.load("art/ui_elements/inventory/stats_selected.png").convert()
stats_deselected_image = pygame.image.load("art/ui_elements/inventory/stats_deselected.png").convert()

weapon_icon = pygame.image.load("art/ui_elements/inventory/icon_weapon.png").convert()
old_bow_icon = pygame.image.load("art/ui_elements/inventory/icon_bow.png").convert()
shield_icon = pygame.image.load("art/ui_elements/inventory/icon_shield.png").convert()
spell_icon = pygame.image.load("art/ui_elements/inventory/icon_spell.png").convert()
armor_icon = pygame.image.load("art/ui_elements/inventory/icon_armor.png").convert()

sword_icon = pygame.image.load("art/ui_elements/inventory/icons/icon_sword.png").convert()
spear_icon = pygame.image.load("art/ui_elements/inventory/icons/icon_spear.png").convert()
dagger_icon = pygame.image.load("art/ui_elements/inventory/icons/icon_dagger.png").convert()
bow_icon = pygame.image.load("art/ui_elements/inventory/icons/icon_bow.png").convert()
mace_icon = pygame.image.load("art/ui_elements/inventory/icons/icon_mace.png").convert()
axe_icon = pygame.image.load("art/ui_elements/inventory/icons/icon_axe.png").convert()

boots_icon = pygame.image.load("art/ui_elements/inventory/icons/icon_boots.png").convert()

# terrain
dirt_tile_image = pygame.image.load("art/tiles/dirt_1.png").convert()
flagstone_tile_image = pygame.image.load("art/tiles/flagstone_1.png").convert()
flagstone_tile_2_image = pygame.image.load("art/tiles/flagstone_2.png").convert()
brown_cobblestones_image = pygame.image.load("art/tiles/brown_cobblestones.png").convert()
wood_tile_1_image = pygame.image.load("art/tiles/wood_1.png").convert()
wood_tile_1_large_image = pygame.image.load("art/tiles/wood_1_large.png").convert()
wood_tile_2_image = pygame.image.load("art/tiles/wood_2.png").convert()
wood_tile_3_image = pygame.image.load("art/tiles/wood_3_large.png").convert()
grass_tile_1_image = pygame.image.load("art/tiles/grass_1.png").convert()
grass_tile_2_image = pygame.image.load("art/tiles/grass_2.png").convert()
grass_tile_3_image = pygame.image.load("art/tiles/grass_3.png").convert()
grass_tile_4_image = pygame.image.load("art/tiles/grass_4.png").convert()
grass_tile_5_image = pygame.image.load("art/tiles/grass_5.png").convert()
marble_tile_1_image = pygame.image.load("art/tiles/marble_1.png").convert()
stone_block_tile_image = pygame.image.load("art/tiles/stone_block.png").convert()
stone_block_tile_image_2 = pygame.image.load("art/tiles/stone_block_2.png").convert()
stone_floor_tile_gray_image = pygame.image.load("art/tiles/stone_floor.png").convert()
stone_floor_tile_brown_image = pygame.image.load("art/tiles/stone_floor_brown.png").convert()
water_tile_image = pygame.image.load("art/tiles/water_1.png").convert()
dirt_path_elbow_1 = pygame.image.load("art/tiles/dirt_path_elbow_1.png").convert()
dirt_path_elbow_2 = pygame.image.load("art/tiles/dirt_path_elbow_2.png").convert()
dirt_path_elbow_3 = pygame.image.load("art/tiles/dirt_path_elbow_3.png").convert()
dirt_path_elbow_4 = pygame.image.load("art/tiles/dirt_path_elbow_4.png").convert()
dirt_path_horizontal_1 = pygame.image.load("art/tiles/path_horizontal_1.png").convert()
dirt_path_horizontal_2 = pygame.image.load("art/tiles/path_horizontal_2.png").convert()
dirt_path_horizontal_3 = pygame.image.load("art/tiles/path_horizontal_3.png").convert()
dirt_path_vertical_1 = pygame.image.load("art/tiles/path_vertical_1.png").convert()
dirt_path_vertical_2 = pygame.image.load("art/tiles/path_vertical_2.png").convert()
dirt_path_vertical_3 = pygame.image.load("art/tiles/path_vertical_3.png").convert()
dirt_path_vertical_4 = pygame.image.load("art/tiles/path_vertical_4.png").convert()
dirt_path_t_up = pygame.image.load("art/tiles/dirt_path_t_up.png").convert()
dirt_path_t_down = pygame.image.load("art/tiles/dirt_path_t_down.png").convert()
dirt_path_t_left = pygame.image.load("art/tiles/dirt_path_t_left.png").convert()
dirt_path_t_right = pygame.image.load("art/tiles/dirt_path_t_right.png").convert()
dirt_path_4_way = pygame.image.load("art/tiles/dirt_path_4_way.png").convert()
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
               "Brown Cobblestones": brown_cobblestones_image,
               "Flagstone": flagstone_tile_image,
               "Flagstone 2": flagstone_tile_2_image,
               "Wood 1": wood_tile_1_image,
               "Wood 1 Large": wood_tile_1_large_image,
               "Wood 2": wood_tile_2_image,
               "Wood 3": wood_tile_3_image,
               "Grass 1": grass_tile_1_image,
               "Grass 2": grass_tile_2_image,
               "Grass 3": grass_tile_3_image,
               "Grass 4": grass_tile_4_image,
               "Grass 5": grass_tile_5_image,
               "Marble 1": marble_tile_1_image,
               "Stone Block": stone_block_tile_image,
               "Stone Block 2": stone_block_tile_image_2,
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
