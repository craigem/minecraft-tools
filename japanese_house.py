import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

# House dimensions
house_x = list(range(3, 20))
house_z = list(range(-1, 12))
# Floor
grounds_y = pos.y - 1
floor_y = pos.y
verandah_size = 1

# Set blocks
grounds = block.GRASS.id
flooring = block.DOUBLE_WOODEN_SLAB.id, 5
poles = block.WOOD.id, 1
panels = block.WOOL.id
stairs = block.WOODEN_SLAB.id, 5
#stairs = block.STAIRS_WOOD.id, 2, 1
stairsEast = block.STAIRS_WOOD.id, 0
stairsWest = block.STAIRS_WOOD.id, 1
stairsSouth = block.STAIRS_WOOD.id, 2
stairsNorth = block.STAIRS_WOOD.id, 3
roofSlab = block.WOODEN_SLAB.id
roofCorners = block.DOUBLE_WOODEN_SLAB.id, 0
capstone = block.STONE_SLAB.id, 0


def clear_space():
    # Clear a space by setting it to AIR
    mc.setBlocks(
        pos.x + house_x[0] - verandah_size - 3,
        floor_y,
        pos.z + house_z[0] - verandah_size - 3,
        pos.x + house_x[-1] + verandah_size + 3,
        floor_y + 100,
        pos.z + house_z[-1] + verandah_size + 3,
        block.AIR.id
        )


def build_grounds():
    # Build the grounds and gardens
    mc.setBlocks(
        pos.x + house_x[0] - verandah_size - 3,
        grounds_y,
        pos.z + house_z[0] - verandah_size - 3,
        pos.x + house_x[-1] + verandah_size + 3,
        grounds_y,
        pos.z + house_z[-1] + verandah_size + 3,
        grounds
        )


def build_floor():
    # Build the floor and the verandah
    mc.setBlocks(
        pos.x + house_x[0] - verandah_size, floor_y, pos.z + house_z[0] - verandah_size,
        pos.x + house_x[-1] + verandah_size, floor_y, pos.z + house_z[-1] + verandah_size,
        flooring
        )


def house_posts():
    # Set out the house poles by making the entire walls poles, the carve away
    # what we don't need later.
    post_y_bottom = floor_y + 1
    post_y_top = floor_y + 4
    # West posts:
    mc.setBlocks(
        pos.x + house_x[0], post_y_bottom, pos.z + house_z[0],
        pos.x + house_x[0], post_y_top, pos.z + house_z[-1],
        poles
        )
    # East posts:
    mc.setBlocks(
        pos.x + house_x[-1], post_y_bottom, pos.z + house_z[0],
        pos.x + house_x[-1], post_y_top, pos.z + house_z[-1],
        poles
        )
    # North posts:
    mc.setBlocks(
        pos.x + house_x[0], post_y_bottom, pos.z + house_z[0],
        pos.x + house_x[-1], post_y_top, pos.z + house_z[0],
        poles
        )
    # South posts:
    mc.setBlocks(
        pos.x + house_x[0], post_y_bottom, pos.z + house_z[-1],
        pos.x + house_x[-1], post_y_top, pos.z + house_z[-1],
        poles
        )


def wall_panels():
    panel_y_bottom = floor_y + 1
    panel_y_top = floor_y + 3
    # West Panels
    mc.setBlocks(
        pos.x + house_x[0], panel_y_bottom, pos.z + house_z[1],
        pos.x + house_x[0], panel_y_top, pos.z + house_z[3],
        panels
        )
    mc.setBlocks(
        pos.x + house_x[0], panel_y_bottom, pos.z + house_z[5],
        pos.x + house_x[0], panel_y_top, pos.z + house_z[7],
        panels
        )
    mc.setBlocks(
        pos.x + house_x[0], panel_y_bottom, pos.z + house_z[9],
        pos.x + house_x[0], panel_y_top, pos.z + house_z[11],
        panels
        )
    # East Panels
    mc.setBlocks(
        pos.x + house_x[-1], panel_y_bottom, pos.z + house_z[1],
        pos.x + house_x[-1], panel_y_top, pos.z + house_z[3],
        panels
        )
    mc.setBlocks(
        pos.x + house_x[-1], panel_y_bottom, pos.z + house_z[5],
        pos.x + house_x[-1], panel_y_top, pos.z + house_z[7],
        panels
        )
    mc.setBlocks(
        pos.x + house_x[-1], panel_y_bottom, pos.z + house_z[9],
        pos.x + house_x[-1], panel_y_top, pos.z + house_z[11],
        panels
        )
    # North Panels
    mc.setBlocks(
        pos.x + house_x[1], panel_y_bottom, pos.z + house_z[0],
        pos.x + house_x[3], panel_y_top, pos.z + house_z[0],
        panels
        )
    mc.setBlocks(
        pos.x + house_x[5], panel_y_bottom, pos.z + house_z[0],
        pos.x + house_x[7], panel_y_top, pos.z + house_z[0],
        panels
        )
    mc.setBlocks(
        pos.x + house_x[9], panel_y_bottom, pos.z + house_z[0],
        pos.x + house_x[11], panel_y_top, pos.z + house_z[0],
        panels
        )
    mc.setBlocks(
        pos.x + house_x[13], panel_y_bottom, pos.z + house_z[0],
        pos.x + house_x[15], panel_y_top, pos.z + house_z[0],
        panels
        )
    # South panels:
    mc.setBlocks(
        pos.x + house_x[1], panel_y_bottom, pos.z + house_z[-1],
        pos.x + house_x[3], panel_y_top, pos.z + house_z[-1],
        panels
        )
    mc.setBlocks(
        pos.x + house_x[5], panel_y_bottom, pos.z + house_z[-1],
        pos.x + house_x[7], panel_y_top, pos.z + house_z[-1],
        panels
        )
    mc.setBlocks(
        pos.x + house_x[9], panel_y_bottom, pos.z + house_z[-1],
        pos.x + house_x[11], panel_y_top, pos.z + house_z[-1],
        panels
        )
    mc.setBlocks(
        pos.x + house_x[13], panel_y_bottom, pos.z + house_z[-1],
        pos.x + house_x[15], panel_y_top, pos.z + house_z[-1],
        panels
        )
    mc.setBlocks(
        pos.x + house_x[1], panel_y_bottom, pos.z + house_z[-1],
        pos.x + house_x[3], panel_y_top, pos.z + house_z[-1],
        panels
        )


def door():
    mc.setBlocks(
        pos.x + 3, pos.y + 1, pos.z + 5,
        pos.x + 3, pos.y + 2, pos.z + 5,
        block.AIR.id
        )


def verandah_stairs():
    # Define the stairs as area and let everything running later clobber it.
    mc.setBlocks(
        pos.x + house_x[0] - verandah_size - 1,
        floor_y,
        pos.z + house_z[0] - verandah_size - 1,
        pos.x + house_x[-1] + verandah_size + 1,
        floor_y,
        pos.z + house_z[-1] + verandah_size + 1,
        stairs
        )


def lower_roof():
    # Build the lower roof
    lowerRoofCorners = block.WOOD_PLANKS.id, 0
    lowerRoofStairsEast = block.STAIRS_WOOD.id, 0
    lowerRoofStairsWest = block.STAIRS_WOOD.id, 1
    lowerRoofStairsSouth = block.STAIRS_WOOD.id, 2
    lowerRoofStairsNorth = block.STAIRS_WOOD.id, 3
    lowerRoofSlab = block.WOODEN_SLAB.id
    lowerRoof_y = floor_y + 4
    # Inner row
    # Set a wood block on each corner
    # North West corner
    mc.setBlock(
        pos.x + house_x[0] - 1, lowerRoof_y, pos.z + house_z[0] - 1,
        lowerRoofCorners
        )
    # South West corner
    mc.setBlock(
        pos.x + house_x[0] - 1, lowerRoof_y, pos.z + house_z[-1] + 1,
        lowerRoofCorners
        )
    # North East corner
    mc.setBlock(
        pos.x + house_x[-1] + 1, lowerRoof_y, pos.z + house_z[0] - 1,
        lowerRoofCorners
        )
    # South East corner
    mc.setBlock(
        pos.x + house_x[-1] + 1, lowerRoof_y, pos.z + house_z[-1] + 1,
        lowerRoofCorners
        )
    # Set outward facing stairs in between
    # Western roofing stairs
    mc.setBlocks(
        pos.x + house_x[0] - 1, lowerRoof_y, pos.z + house_z[0],
        pos.x + house_x[0] - 1, lowerRoof_y, pos.z + house_z[-1],
        lowerRoofStairsWest
        )
    # Northern roofing stairs
    mc.setBlocks(
        pos.x + house_x[0], lowerRoof_y, pos.z + house_z[0] - 1,
        pos.x + house_x[-1], lowerRoof_y, pos.z + house_z[0] - 1,
        lowerRoofStairsNorth
        )
    # Eastern roofing stairs
    mc.setBlocks(
        pos.x + house_x[-1] + 1, lowerRoof_y, pos.z + house_z[0],
        pos.x + house_x[-1] + 1, lowerRoof_y, pos.z + house_z[-1],
        lowerRoofStairsEast
        )
    # Southern roofing stairs
    mc.setBlocks(
        pos.x + house_x[0], lowerRoof_y, pos.z + house_z[-1] + 1,
        pos.x + house_x[-1], lowerRoof_y, pos.z + house_z[-1] + 1,
        lowerRoofStairsSouth
        )
    # Middle row
    # Set a wood block on each corner
    # North West corner
    mc.setBlock(
        pos.x + house_x[0] - 2, lowerRoof_y, pos.z + house_z[0] - 2,
        lowerRoofCorners
        )
    # South West corner
    mc.setBlock(
        pos.x + house_x[0] - 2, lowerRoof_y, pos.z + house_z[-1] + 2,
        lowerRoofCorners
        )
    # North East corner
    mc.setBlock(
        pos.x + house_x[-1] + 2, lowerRoof_y, pos.z + house_z[0] - 2,
        lowerRoofCorners
        )
    # South East corner
    mc.setBlock(
        pos.x + house_x[-1] + 2, lowerRoof_y, pos.z + house_z[-1] + 2,
        lowerRoofCorners
        )
    # Set single wood slabs in between
    # Western roofing slabs
    mc.setBlocks(
        pos.x + house_x[0] - 2, lowerRoof_y, pos.z + house_z[0] - 1,
        pos.x + house_x[0] - 2, lowerRoof_y, pos.z + house_z[-1] + 1,
        lowerRoofSlab
        )
    # Northern roofing slabs
    mc.setBlocks(
        pos.x + house_x[0] - 1 , lowerRoof_y, pos.z + house_z[0] - 2,
        pos.x + house_x[-1] + 1, lowerRoof_y, pos.z + house_z[0] - 2,
        lowerRoofSlab
        )
    # Eastern roofing slabs
    mc.setBlocks(
        pos.x + house_x[-1] + 2, lowerRoof_y, pos.z + house_z[0] - 1,
        pos.x + house_x[-1] + 2, lowerRoof_y, pos.z + house_z[-1] + 1,
        lowerRoofSlab
        )
    # Southern roofing slabs
    mc.setBlocks(
        pos.x + house_x[0] - 1, lowerRoof_y, pos.z + house_z[-1] + 2,
        pos.x + house_x[-1] + 1, lowerRoof_y, pos.z + house_z[-1] + 2,
        lowerRoofSlab
        )
    # Upper row
    # Set a wood block on each corner
    # North West corner
    upperRow_y = lowerRoof_y + 1
    mc.setBlock(
        pos.x + house_x[0], upperRow_y, pos.z + house_z[0],
        lowerRoofSlab
        )
    # South West corner
    mc.setBlock(
        pos.x + house_x[0], upperRow_y, pos.z + house_z[-1],
        lowerRoofSlab
        )
    # North East corner
    mc.setBlock(
        pos.x + house_x[-1], upperRow_y, pos.z + house_z[0],
        lowerRoofSlab
        )
    # South East corner
    mc.setBlock(
        pos.x + house_x[-1], upperRow_y, pos.z + house_z[-1],
        lowerRoofSlab
        )
    # Set single wood slabs in between
    # Western roofing slabs
    mc.setBlocks(
        pos.x + house_x[0], upperRow_y, pos.z + house_z[1],
        pos.x + house_x[0], upperRow_y, pos.z + house_z[-2],
        lowerRoofStairsWest
        )
    # Northern roofing slabs
    mc.setBlocks(
        pos.x + house_x[1], upperRow_y, pos.z + house_z[0],
        pos.x + house_x[-2], upperRow_y, pos.z + house_z[0],
        lowerRoofStairsNorth
        )
    # Eastern roofing slabs
    mc.setBlocks(
        pos.x + house_x[-1], upperRow_y, pos.z + house_z[1],
        pos.x + house_x[-1], upperRow_y, pos.z + house_z[-2],
        lowerRoofStairsEast
        )
    # Southern roofing slabs
    mc.setBlocks(
        pos.x + house_x[1], upperRow_y, pos.z + house_z[-1],
        pos.x + house_x[-2], upperRow_y, pos.z + house_z[-1],
        lowerRoofStairsSouth
        )

def upper_level():
    # Build the mezzanine level
    # The floor of the mezzanine level
    upperLevel_y = floor_y + 5
    mc.setBlocks(
        pos.x + house_x[1], upperLevel_y, pos.z + house_z[1],
        pos.x + house_x[-2], upperLevel_y, pos.z + house_z[-2],
        block.DOUBLE_WOODEN_SLAB.id, 1
        )
    # The upper floor wall
    mc.setBlocks(
        pos.x + house_x[1], upperLevel_y + 1, pos.z + house_z[1],
        pos.x + house_x[-2], upperLevel_y + 1, pos.z + house_z[-2],
        poles
        )
    # The upper floor roof
    mc.setBlocks(
        pos.x + house_x[1] - 2, upperLevel_y + 2, pos.z + house_z[1] - 2,
        pos.x + house_x[-2] + 2, upperLevel_y + 2, pos.z + house_z[-2] + 2,
        roofSlab
        )
    # The upper floor roof stairs
    mc.setBlocks(
        pos.x + house_x[1], upperLevel_y + 2, pos.z + house_z[1],
        pos.x + house_x[-2], upperLevel_y + 2, pos.z + house_z[-2],
        stairsNorth
        )
    # Clear the upper floor
    mc.setBlocks(
        pos.x + house_x[2], upperLevel_y + 1, pos.z + house_z[2],
        pos.x + house_x[-3], upperLevel_y + 2, pos.z + house_z[-3],
        block.AIR.id
        )
    # Add the decorative corner blocks
    # Northwest corner
    mc.setBlock(
        pos.x + house_x[1], upperLevel_y + 2, pos.z + house_z[1], roofCorners
        )
    mc.setBlock(
        pos.x + house_x[0], upperLevel_y + 2, pos.z + house_z[0], roofCorners
        )
    mc.setBlock(
        pos.x + house_x[0] - 1, upperLevel_y + 2, pos.z + house_z[0] - 1, roofCorners
        )
    # Southwest corner
    mc.setBlock(
        pos.x + house_x[1], upperLevel_y + 2, pos.z + house_z[-2], roofCorners
        )
    mc.setBlock(
        pos.x + house_x[0], upperLevel_y + 2, pos.z + house_z[-1], roofCorners
        )
    mc.setBlock(
        pos.x + house_x[0] - 1, upperLevel_y + 2, pos.z + house_z[-1] + 1, roofCorners
        )
    # Northeast corner
    mc.setBlock(
        pos.x + house_x[-2], upperLevel_y + 2, pos.z + house_z[1],roofCorners
        )
    mc.setBlock(
        pos.x + house_x[-1], upperLevel_y + 2, pos.z + house_z[0], roofCorners
        )
    mc.setBlock(
        pos.x + house_x[-1] + 1, upperLevel_y + 2, pos.z + house_z[0] - 1, roofCorners
        )
    # Southeast corner
    mc.setBlock(
        pos.x + house_x[-2], upperLevel_y + 2, pos.z + house_z[-2],roofCorners
        )
    mc.setBlock(
        pos.x + house_x[-1], upperLevel_y + 2, pos.z + house_z[-1], roofCorners
        )
    mc.setBlock(
        pos.x + house_x[-1] + 1, upperLevel_y + 2, pos.z + house_z[-1] + 1, roofCorners
        )
    # Build the upper panels
    mc.setBlocks(
        pos.x + house_x[2], upperLevel_y + 1, pos.z + house_z[4],
        pos.x + house_x[-3], upperLevel_y + 5, pos.z + house_z[5],
        panels
        )
    mc.setBlocks(
        pos.x + house_x[2], upperLevel_y + 1, pos.z + house_z[-6],
        pos.x + house_x[-3], upperLevel_y + 5, pos.z + house_z[-5],
        panels
        )
    # Build the upper posts
    mc.setBlocks(
        pos.x + house_x[2], upperLevel_y + 1, pos.z + house_z[2],
        pos.x + house_x[-3], upperLevel_y + 2, pos.z + house_z[2],
        poles
        )
    mc.setBlocks(
        pos.x + house_x[2], upperLevel_y + 1, pos.z + house_z[3],
        pos.x + house_x[-3], upperLevel_y + 3, pos.z + house_z[3],
        poles
        )
    mc.setBlocks(
        pos.x + house_x[2], upperLevel_y + 1, pos.z + house_z[6],
        pos.x + house_x[-3], upperLevel_y + 6, pos.z + house_z[6],
        poles
        )
    mc.setBlocks(
        pos.x + house_x[2], upperLevel_y + 1, pos.z + house_z[-4],
        pos.x + house_x[-3], upperLevel_y + 3, pos.z + house_z[-4],
        poles
        )
    mc.setBlocks(
        pos.x + house_x[2], upperLevel_y + 1, pos.z + house_z[-3],
        pos.x + house_x[-3], upperLevel_y + 2, pos.z + house_z[-3],
        poles
        )
    # Clear the upper floor
    mc.setBlocks(
        pos.x + house_x[3], upperLevel_y + 1, pos.z + house_z[2],
        pos.x + house_x[-4], upperLevel_y + 6, pos.z + house_z[-3],
        block.AIR.id
        )
    # Put the north roof on
    mc.setBlocks(
        pos.x + house_x[1], upperLevel_y + 3, pos.z + house_z[2],
        pos.x + house_x[-2], upperLevel_y + 3, pos.z + house_z[2],
        stairsNorth
        )
    mc.setBlocks(
        pos.x + house_x[1], upperLevel_y + 4, pos.z + house_z[3],
        pos.x + house_x[-2], upperLevel_y + 4, pos.z + house_z[3],
        stairsNorth
        )
    mc.setBlocks(
        pos.x + house_x[1], upperLevel_y + 5, pos.z + house_z[4],
        pos.x + house_x[-2], upperLevel_y + 5, pos.z + house_z[4],
        stairsNorth
        )
    mc.setBlocks(
        pos.x + house_x[1], upperLevel_y + 6, pos.z + house_z[5],
        pos.x + house_x[-2], upperLevel_y + 6, pos.z + house_z[5],
        stairsNorth
        )
    # Put the South roof on
    mc.setBlocks(
        pos.x + house_x[1], upperLevel_y + 3, pos.z + house_z[-3],
        pos.x + house_x[-2], upperLevel_y + 3, pos.z + house_z[-3],
        stairsSouth
        )
    mc.setBlocks(
        pos.x + house_x[1], upperLevel_y + 4, pos.z + house_z[-4],
        pos.x + house_x[-2], upperLevel_y + 4, pos.z + house_z[-4],
        stairsSouth
        )
    mc.setBlocks(
        pos.x + house_x[1], upperLevel_y + 5, pos.z + house_z[-5],
        pos.x + house_x[-2], upperLevel_y + 5, pos.z + house_z[-5],
        stairsSouth
        )
    mc.setBlocks(
        pos.x + house_x[1], upperLevel_y + 6, pos.z + house_z[-6],
        pos.x + house_x[-2], upperLevel_y + 6, pos.z + house_z[-6],
        stairsSouth
        )
    # Set the capstone
    mc.setBlocks(
        pos.x + house_x[0], upperLevel_y + 7, pos.z + house_z[6],
        pos.x + house_x[-1], upperLevel_y + 7, pos.z + house_z[6],
        capstone
        )


def interior_torches():
    # Set the interior torches
    torch_y = floor_y + 3
    northWallTorch = block.TORCH.id, 1
    mc.setBlock(
         pos.x + house_x[4] -5, torch_y, pos.z, northWallTorch
         )


clear_space()
build_grounds()
verandah_stairs()
build_floor()
house_posts()
wall_panels()
lower_roof()
upper_level()
interior_torches()
door()
