#!/usr/bin/python
''' Craige's Keep Builder

This creates a keep with:

* A moat
* An outer wall
* An inner wall
* Lighting
* Doors
* Streets
* More to come
'''

# Import Minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block as block

MC = minecraft.Minecraft.create()

MC.postToChat("Someone's building Craige's Keep!")

# --------------------------------------
# Define Functions
# --------------------------------------


def createwalls(size, baseheight, height, material, battlements, walkway, stairs, streets):
    ''' Create 4 walls with a specified width, height and material.
    Battlements and walkways can also be added to the top edges.
    '''

    # Put the walls on solid foundations
    MC.setBlocks(
        -size, 0, -size, size, baseheight - 1, size,
        block.BEDROCK.id
        )

    if stairs is True:
        createstairs(size, baseheight)

    # Create a nice court yard of grass
    MC.setBlocks(
        -size, baseheight, -size, size, baseheight, size,
        block.GRASS.id
        )

    MC.setBlocks(
        -size, baseheight, -size, size, baseheight + height, -size,
        material
        )
    MC.setBlocks(
        -size, baseheight, -size, -size, baseheight + height, size,
        material
        )
    MC.setBlocks(
        size, baseheight, size, -size, baseheight + height, size,
        material
        )
    MC.setBlocks(
        size, baseheight, size, size, baseheight + height, -size,
        material
        )

    # Add battlements to top edge
    if battlements is True:
        for pos in range(0, (2 * size) + 1, 2):
            MC.setBlock(size, baseheight + height + 1, (pos - size), material)
            MC.setBlock(-size, baseheight + height + 1, (pos - size), material)
            MC.setBlock((pos - size), baseheight + height + 1, size, material)
            MC.setBlock((pos - size), baseheight + height + 1, -size, material)
        # Keep the corner lights on!
        MC.setBlock(-size, baseheight + height + 2, -size, block.FENCE.id)
        MC.setBlock(-size, baseheight + height + 2, size, block.FENCE.id)
        MC.setBlock(size, baseheight + height + 2, -size, block.FENCE.id)
        MC.setBlock(size, baseheight + height + 2, size, block.FENCE.id)
        MC.setBlock(
            -size, baseheight + height + 3, -size, block.GLOWSTONE_BLOCK.id
            )
        MC.setBlock(
            -size, baseheight + height + 3, size, block.GLOWSTONE_BLOCK.id
            )
        MC.setBlock(
            size, baseheight + height + 3, -size, block.GLOWSTONE_BLOCK.id
            )
        MC.setBlock(
            size, baseheight + height + 3, size, block.GLOWSTONE_BLOCK.id
            )

    # Add wooden walkways
    if walkway is True:
        MC.setBlocks(
            -size + 1, baseheight + height - 1, size - 1,
            size - 1, baseheight + height - 1, size - 1,
            block.WOOD_PLANKS
            )
        MC.setBlocks(
            -size + 1, baseheight + height - 1, -size + 1,
            size - 1, baseheight + height - 1, -size + 1,
            block.WOOD_PLANKS
            )
        MC.setBlocks(
            -size + 1, baseheight + height - 1, -size + 1,
            -size + 1, baseheight + height - 1, size - 1,
            block.WOOD_PLANKS
            )
        MC.setBlocks(
            size - 1, baseheight + height - 1, -size + 1,
            size - 1, baseheight + height - 1, size - 1,
            block.WOOD_PLANKS.id
            )

    # Door
    MC.setBlocks(0, baseheight + 1, size, 0, baseheight + 2, size, block.AIR)
    MC.setBlock(0, baseheight + 1, size, block.FENCE_GATE.id)

    if streets is True:
        createstreets(size, baseheight)


def createlandscape(moatwidth, moatdepth, islandwidth):
    ''' Create the grounds and moat '''
    # Set upper half to air
    MC.setBlocks(-128, 1, -128, 128, 128, 128, block.AIR)
    # Set lower half of world to dirt with a layer of grass
    MC.setBlocks(-128, -1, -128, 128, -1, 128, block.DIRT)
    MC.setBlocks(-128, 0, -128, 128, 0, 128, block.GRASS)
    # Create water moat
    MC.setBlocks(
        -moatwidth, 0, -moatwidth, moatwidth, -moatdepth, moatwidth,
        block.WATER.id
        )
    # Create island inside moat
    MC.setBlocks(
        -islandwidth, 1, -islandwidth, islandwidth, 1, islandwidth,
        block.GRASS.id
        )
    # Put the island on solid foundations
    MC.setBlocks(
        -islandwidth, 0, -islandwidth, islandwidth, -moatdepth, islandwidth,
        block.BEDROCK.id
        )


def createkeep(size, baseheight, levels):
    ''' Create a keep with a specified number
    of floor levels and a roof
    '''
    height = (levels * 7) + 5

    createwalls(size, baseheight, height, block.STONE_BRICK, True, True, True, False)

    # put the keep on solid foundations
    MC.setBlocks(
        -size, 0, -size, size, baseheight - 1, size,
        block.BEDROCK.id
        )

    # ground floor
    MC.setBlocks(
        -size, baseheight, -size, size, baseheight, size,
        block.STONE_BRICK.id
        )

    # floors
    for level in range(1, levels + 1):
        MC.setBlocks(
            -size + 1, (level * 7) + baseheight, -size + 1,
            size - 1, (level * 7) + baseheight, size - 1,
            block.WOOD_PLANKS.id
            )

    # windows
    for level in range(0, levels + 1):
        createwindows(0, (level * 7) + baseheight + 2, size, "N")
        createwindows(0, (level * 7) + baseheight + 2, -size, "S")
        createwindows(-size, (level * 7) + baseheight + 2, 0, "W")
        createwindows(size, (level * 7) + baseheight + 2, 0, "E")

    # let there be interior lights!
    for level in range(0, levels):
        MC.setBlock(0, (level * 7) + baseheight + 6, 0, block.FENCE.id)
        MC.setBlock(0, (level * 7) + baseheight + 5, 0, block.GLOWSTONE_BLOCK.id)

    # Inner gate
    MC.setBlocks(
        0, baseheight + 1, size -18, 0, baseheight + 2, size -18, block.AIR
        )

    # Outer gate
    MC.setBlocks(
        0, baseheight + 1, size +16, 0, baseheight + 2, size + 16, block.AIR
        )


def createwindows(pos_x, pos_y, pos_z, cardinal):

    if cardinal == "N" or cardinal == "S":
        pos_z1 = pos_z
        pos_z2 = pos_z
        pos_x1 = pos_x - 2
        pos_x2 = pos_x + 2

    if cardinal == "E" or cardinal == "W":
        pos_z1 = pos_z - 2
        pos_z2 = pos_z + 2
        pos_x1 = pos_x
        pos_x2 = pos_x

    MC.setBlocks(pos_x1, pos_y, pos_z1, pos_x1, pos_y + 1, pos_z1, block.AIR)
    MC.setBlocks(pos_x2, pos_y, pos_z2, pos_x2, pos_y + 1, pos_z2, block.AIR)

    if cardinal == "N":
        facing = 3
    if cardinal == "S":
        facing = 2
    if cardinal == "W":
        facing = 0
    if cardinal == "E":
        facing = 1

    MC.setBlock(pos_x1, pos_y - 1, pos_z1, 109, facing)
    MC.setBlock(pos_x2, pos_y - 1, pos_z2, 109, facing)


def createstairs(size, baseheight):
    ''' Build a set of stairs '''
    # Build the foundations for a stairway to heaven
    MC.setBlocks(
        -1, 0, size + 1, 1, baseheight - 1, size + 1,
        block.BEDROCK.id
        )
    MC.setBlocks(
        -1, 0, size + 2, 1, baseheight - 2, size + 2,
        block.BEDROCK.id
        )
    MC.setBlocks(
        -1, 0, size + 3, 1, baseheight - 3, size + 3,
        block.BEDROCK.id
        )
    MC.setBlocks(
        -1, 0, size + 4, 1, baseheight - 4, size + 4,
        block.BEDROCK.id
        )
    MC.setBlocks(
        -1, 0, size + 5, 1, baseheight - 5, size + 5,
        block.BEDROCK.id
        )
    MC.setBlocks(
        -1, 0, size + 6, 1, baseheight - 6, size + 6,
        block.BEDROCK.id
        )
    MC.setBlocks(
        -1, 0, size + 7, 1, baseheight - 7, size + 7,
        block.BEDROCK.id
        )
    MC.setBlocks(
        -1, 0, size + 8, 1, baseheight - 7, size + 8,
        block.BEDROCK.id
        )

    # Build a stairway to heaven
    MC.setBlocks(
        -1, baseheight, size + 1, 1, baseheight, size + 1,
        block.STONE_BRICK_STAIRS.id
        )
    MC.setBlocks(
        -1, baseheight - 1, size + 2, 1, baseheight - 1, size + 2,
        block.STONE_BRICK_STAIRS.id
        )
    MC.setBlocks(
        -1, baseheight - 2, size + 3, 1, baseheight - 2, size + 3,
        block.STONE_BRICK_STAIRS.id
        )
    MC.setBlocks(
        -1, baseheight - 3, size + 4, 1, baseheight - 3, size + 4,
        block.STONE_BRICK_STAIRS.id
        )
    MC.setBlocks(
        -1, baseheight - 4, size + 5, 1, baseheight - 4, size + 5,
        block.STONE_BRICK_STAIRS.id
        )
    MC.setBlocks(
        -1, baseheight - 5, size + 6, 1, baseheight - 5, size + 6,
        block.STONE_BRICK_STAIRS.id
        )
    MC.setBlocks(
        -1, baseheight - 6, size + 7, 1, baseheight - 6, size + 7,
        block.STONE_BRICK_STAIRS.id
        )
    MC.setBlocks(
        -1, baseheight - 7, size + 8, 1, baseheight - 7, size + 8,
        block.STONE_BRICK_STAIRS.id
        )


def createstreets(size, baseheight):
    ''' Build a set of stairs '''
    # Build the gate streets
    MC.setBlocks(
        -1, baseheight, size - 1, 1, baseheight, 0,
        block.STONE_BRICK.id
        )


# --------------------------------------


# --------------------------------------
#
# Main Script
#
# --------------------------------------

print "Creating ground and moat"
createlandscape(77, 10, 67)

print "Create outer walls"
createwalls(65, 1, 7, block.STONE_BRICK, True, True, False, True)

print "Create inner walls"
createwalls(33, 9, 8, block.STONE_BRICK, True, True, True, True)

print "Create Keep with 4 levels"
createkeep(5, 17, 4)

print "Position player on Keep's walkway"
MC.player.setPos(0, 75, 4)
