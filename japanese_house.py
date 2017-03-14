#!/usr/bin/python2.7

''' japanese_house.py
Produces a Minecraft interpretation of a classic Japanese house. Presently it
only produces the single configuration that is little more than an empty shell.
'''

import mcpi.minecraft as minecraft
import mcpi.block as block

MC = minecraft.Minecraft.create()

POS = MC.player.getTilePos()

# House dimensions
HOUSE_X = list(range(3, 20))
HOUSE_Z = list(range(-1, 12))
# Floor
GROUNDS_Y = POS.y - 1
FLOOR_Y = POS.y
LOWER_ROOF_Y = FLOOR_Y + 4
VERANDAH_SIZE = 1

# Set blocks
GROUNDS = block.GRASS.id
FLOORING = block.DOUBLE_WOODEN_SLAB.id, 5
POLES = block.WOOD.id, 1
PANELS = block.WOOL.id
STAIRS = block.WOODEN_SLAB.id, 5
ROOF_STAIRS_EAST = block.STAIRS_WOOD.id, 0
ROOF_STAIRS_WEST = block.STAIRS_WOOD.id, 1
ROOF_STAIRS_SOUTH = block.STAIRS_WOOD.id, 2
ROOF_STAIRS_NORTH = block.STAIRS_WOOD.id, 3
ROOF_SLAB = block.WOODEN_SLAB.id
ROOF_CORNERS = block.DOUBLE_WOODEN_SLAB.id, 0
CAPSTONE = block.STONE_SLAB.id, 0
LIGHT_POST = block.FENCE.id
EXTERIOR_LIGHT = block.GLOWSTONE_BLOCK.id
EXT_LIGHT_BASE = block.WOODEN_SLAB.id, 8


def clear_space():
    ''' Clear a space for the house by setting it to AIR '''
    MC.setBlocks(
        POS.x + HOUSE_X[0] - VERANDAH_SIZE - 3,
        FLOOR_Y,
        POS.z + HOUSE_Z[0] - VERANDAH_SIZE - 3,
        POS.x + HOUSE_X[-1] + VERANDAH_SIZE + 3,
        FLOOR_Y + 100,
        POS.z + HOUSE_Z[-1] + VERANDAH_SIZE + 3,
        block.AIR.id
        )


def build_grounds():
    ''' Build the grounds and gardens '''
    MC.setBlocks(
        POS.x + HOUSE_X[0] - VERANDAH_SIZE - 3,
        GROUNDS_Y,
        POS.z + HOUSE_Z[0] - VERANDAH_SIZE - 3,
        POS.x + HOUSE_X[-1] + VERANDAH_SIZE + 3,
        GROUNDS_Y,
        POS.z + HOUSE_Z[-1] + VERANDAH_SIZE + 3,
        GROUNDS
        )


def build_floor():
    ''' Build the floor and the verandah '''
    MC.setBlocks(
        POS.x + HOUSE_X[0] - VERANDAH_SIZE,
        FLOOR_Y,
        POS.z + HOUSE_Z[0] - VERANDAH_SIZE,
        POS.x + HOUSE_X[-1] + VERANDAH_SIZE,
        FLOOR_Y,
        POS.z + HOUSE_Z[-1] + VERANDAH_SIZE,
        FLOORING
        )


def house_posts():
    ''' Set out the house poles by making the entire walls poles, the carve
    away what we don't need later.
    '''
    post_y_bottom = FLOOR_Y + 1
    post_y_top = FLOOR_Y + 4
    # West posts:
    MC.setBlocks(
        POS.x + HOUSE_X[0], post_y_bottom, POS.z + HOUSE_Z[0],
        POS.x + HOUSE_X[0], post_y_top, POS.z + HOUSE_Z[-1],
        POLES
        )
    # East posts:
    MC.setBlocks(
        POS.x + HOUSE_X[-1], post_y_bottom, POS.z + HOUSE_Z[0],
        POS.x + HOUSE_X[-1], post_y_top, POS.z + HOUSE_Z[-1],
        POLES
        )
    # North posts:
    MC.setBlocks(
        POS.x + HOUSE_X[0], post_y_bottom, POS.z + HOUSE_Z[0],
        POS.x + HOUSE_X[-1], post_y_top, POS.z + HOUSE_Z[0],
        POLES
        )
    # South posts:
    MC.setBlocks(
        POS.x + HOUSE_X[0], post_y_bottom, POS.z + HOUSE_Z[-1],
        POS.x + HOUSE_X[-1], post_y_top, POS.z + HOUSE_Z[-1],
        POLES
        )


def wall_panels():
    ''' Build the wall panels for the ground floor '''
    panel_y_bottom = FLOOR_Y + 1
    panel_y_top = FLOOR_Y + 3
    # West Panels
    MC.setBlocks(
        POS.x + HOUSE_X[0], panel_y_bottom, POS.z + HOUSE_Z[1],
        POS.x + HOUSE_X[0], panel_y_top, POS.z + HOUSE_Z[3],
        PANELS
        )
    MC.setBlocks(
        POS.x + HOUSE_X[0], panel_y_bottom, POS.z + HOUSE_Z[5],
        POS.x + HOUSE_X[0], panel_y_top, POS.z + HOUSE_Z[7],
        PANELS
        )
    MC.setBlocks(
        POS.x + HOUSE_X[0], panel_y_bottom, POS.z + HOUSE_Z[9],
        POS.x + HOUSE_X[0], panel_y_top, POS.z + HOUSE_Z[11],
        PANELS
        )
    # East Panels
    MC.setBlocks(
        POS.x + HOUSE_X[-1], panel_y_bottom, POS.z + HOUSE_Z[1],
        POS.x + HOUSE_X[-1], panel_y_top, POS.z + HOUSE_Z[3],
        PANELS
        )
    MC.setBlocks(
        POS.x + HOUSE_X[-1], panel_y_bottom, POS.z + HOUSE_Z[5],
        POS.x + HOUSE_X[-1], panel_y_top, POS.z + HOUSE_Z[7],
        PANELS
        )
    MC.setBlocks(
        POS.x + HOUSE_X[-1], panel_y_bottom, POS.z + HOUSE_Z[9],
        POS.x + HOUSE_X[-1], panel_y_top, POS.z + HOUSE_Z[11],
        PANELS
        )
    # North Panels
    MC.setBlocks(
        POS.x + HOUSE_X[1], panel_y_bottom, POS.z + HOUSE_Z[0],
        POS.x + HOUSE_X[3], panel_y_top, POS.z + HOUSE_Z[0],
        PANELS
        )
    MC.setBlocks(
        POS.x + HOUSE_X[5], panel_y_bottom, POS.z + HOUSE_Z[0],
        POS.x + HOUSE_X[7], panel_y_top, POS.z + HOUSE_Z[0],
        PANELS
        )
    MC.setBlocks(
        POS.x + HOUSE_X[9], panel_y_bottom, POS.z + HOUSE_Z[0],
        POS.x + HOUSE_X[11], panel_y_top, POS.z + HOUSE_Z[0],
        PANELS
        )
    MC.setBlocks(
        POS.x + HOUSE_X[13], panel_y_bottom, POS.z + HOUSE_Z[0],
        POS.x + HOUSE_X[15], panel_y_top, POS.z + HOUSE_Z[0],
        PANELS
        )
    # South panels:
    MC.setBlocks(
        POS.x + HOUSE_X[1], panel_y_bottom, POS.z + HOUSE_Z[-1],
        POS.x + HOUSE_X[3], panel_y_top, POS.z + HOUSE_Z[-1],
        PANELS
        )
    MC.setBlocks(
        POS.x + HOUSE_X[5], panel_y_bottom, POS.z + HOUSE_Z[-1],
        POS.x + HOUSE_X[7], panel_y_top, POS.z + HOUSE_Z[-1],
        PANELS
        )
    MC.setBlocks(
        POS.x + HOUSE_X[9], panel_y_bottom, POS.z + HOUSE_Z[-1],
        POS.x + HOUSE_X[11], panel_y_top, POS.z + HOUSE_Z[-1],
        PANELS
        )
    MC.setBlocks(
        POS.x + HOUSE_X[13], panel_y_bottom, POS.z + HOUSE_Z[-1],
        POS.x + HOUSE_X[15], panel_y_top, POS.z + HOUSE_Z[-1],
        PANELS
        )
    MC.setBlocks(
        POS.x + HOUSE_X[1], panel_y_bottom, POS.z + HOUSE_Z[-1],
        POS.x + HOUSE_X[3], panel_y_top, POS.z + HOUSE_Z[-1],
        PANELS
        )


def door():
    ''' Every home needs a door, lets carve one right here, in the centre of
    the west side
    '''
    MC.setBlocks(
        POS.x + 3, POS.y + 1, POS.z + 5,
        POS.x + 3, POS.y + 2, POS.z + 5,
        block.AIR.id
        )


def verandah_stairs():
    ''' Define the stairs as area and let everything running later clobber it.
    '''
    MC.setBlocks(
        POS.x + HOUSE_X[0] - VERANDAH_SIZE - 1,
        FLOOR_Y,
        POS.z + HOUSE_Z[0] - VERANDAH_SIZE - 1,
        POS.x + HOUSE_X[-1] + VERANDAH_SIZE + 1,
        FLOOR_Y,
        POS.z + HOUSE_Z[-1] + VERANDAH_SIZE + 1,
        STAIRS
        )


def lower_roof():
    ''' Build the lower roof '''
    # Inner row
    # Set a wood block on each corner
    # North West corner
    MC.setBlock(
        POS.x + HOUSE_X[0] - 1, LOWER_ROOF_Y, POS.z + HOUSE_Z[0] - 1,
        ROOF_CORNERS
        )
    # South West corner
    MC.setBlock(
        POS.x + HOUSE_X[0] - 1, LOWER_ROOF_Y, POS.z + HOUSE_Z[-1] + 1,
        ROOF_CORNERS
        )
    # North East corner
    MC.setBlock(
        POS.x + HOUSE_X[-1] + 1, LOWER_ROOF_Y, POS.z + HOUSE_Z[0] - 1,
        ROOF_CORNERS
        )
    # South East corner
    MC.setBlock(
        POS.x + HOUSE_X[-1] + 1, LOWER_ROOF_Y, POS.z + HOUSE_Z[-1] + 1,
        ROOF_CORNERS
        )
    # Set outward facing stairs in between
    # Western roofing stairs
    MC.setBlocks(
        POS.x + HOUSE_X[0] - 1, LOWER_ROOF_Y, POS.z + HOUSE_Z[0],
        POS.x + HOUSE_X[0] - 1, LOWER_ROOF_Y, POS.z + HOUSE_Z[-1],
        ROOF_STAIRS_WEST
        )
    # Northern roofing stairs
    MC.setBlocks(
        POS.x + HOUSE_X[0], LOWER_ROOF_Y, POS.z + HOUSE_Z[0] - 1,
        POS.x + HOUSE_X[-1], LOWER_ROOF_Y, POS.z + HOUSE_Z[0] - 1,
        ROOF_STAIRS_NORTH
        )
    # Eastern roofing stairs
    MC.setBlocks(
        POS.x + HOUSE_X[-1] + 1, LOWER_ROOF_Y, POS.z + HOUSE_Z[0],
        POS.x + HOUSE_X[-1] + 1, LOWER_ROOF_Y, POS.z + HOUSE_Z[-1],
        ROOF_STAIRS_EAST
        )
    # Southern roofing stairs
    MC.setBlocks(
        POS.x + HOUSE_X[0], LOWER_ROOF_Y, POS.z + HOUSE_Z[-1] + 1,
        POS.x + HOUSE_X[-1], LOWER_ROOF_Y, POS.z + HOUSE_Z[-1] + 1,
        ROOF_STAIRS_SOUTH
        )
    # Middle row
    # Set a wood block on each corner
    # North West corner
    MC.setBlock(
        POS.x + HOUSE_X[0] - 2, LOWER_ROOF_Y, POS.z + HOUSE_Z[0] - 2,
        ROOF_CORNERS
        )
    # South West corner
    MC.setBlock(
        POS.x + HOUSE_X[0] - 2, LOWER_ROOF_Y, POS.z + HOUSE_Z[-1] + 2,
        ROOF_CORNERS
        )
    # North East corner
    MC.setBlock(
        POS.x + HOUSE_X[-1] + 2, LOWER_ROOF_Y, POS.z + HOUSE_Z[0] - 2,
        ROOF_CORNERS
        )
    # South East corner
    MC.setBlock(
        POS.x + HOUSE_X[-1] + 2, LOWER_ROOF_Y, POS.z + HOUSE_Z[-1] + 2,
        ROOF_CORNERS
        )
    # Set single wood slabs in between
    # Western roofing slabs
    MC.setBlocks(
        POS.x + HOUSE_X[0] - 2, LOWER_ROOF_Y, POS.z + HOUSE_Z[0] - 1,
        POS.x + HOUSE_X[0] - 2, LOWER_ROOF_Y, POS.z + HOUSE_Z[-1] + 1,
        ROOF_SLAB
        )
    # Northern roofing slabs
    MC.setBlocks(
        POS.x + HOUSE_X[0] - 1, LOWER_ROOF_Y, POS.z + HOUSE_Z[0] - 2,
        POS.x + HOUSE_X[-1] + 1, LOWER_ROOF_Y, POS.z + HOUSE_Z[0] - 2,
        ROOF_SLAB
        )
    # Eastern roofing slabs
    MC.setBlocks(
        POS.x + HOUSE_X[-1] + 2, LOWER_ROOF_Y, POS.z + HOUSE_Z[0] - 1,
        POS.x + HOUSE_X[-1] + 2, LOWER_ROOF_Y, POS.z + HOUSE_Z[-1] + 1,
        ROOF_SLAB
        )
    # Southern roofing slabs
    MC.setBlocks(
        POS.x + HOUSE_X[0] - 1, LOWER_ROOF_Y, POS.z + HOUSE_Z[-1] + 2,
        POS.x + HOUSE_X[-1] + 1, LOWER_ROOF_Y, POS.z + HOUSE_Z[-1] + 2,
        ROOF_SLAB
        )
    # Upper row
    # Set a wood block on each corner
    # North West corner
    upper_row_y = LOWER_ROOF_Y + 1
    MC.setBlock(
        POS.x + HOUSE_X[0], upper_row_y, POS.z + HOUSE_Z[0],
        ROOF_SLAB
        )
    # South West corner
    MC.setBlock(
        POS.x + HOUSE_X[0], upper_row_y, POS.z + HOUSE_Z[-1],
        ROOF_SLAB
        )
    # North East corner
    MC.setBlock(
        POS.x + HOUSE_X[-1], upper_row_y, POS.z + HOUSE_Z[0],
        ROOF_SLAB
        )
    # South East corner
    MC.setBlock(
        POS.x + HOUSE_X[-1], upper_row_y, POS.z + HOUSE_Z[-1],
        ROOF_SLAB
        )
    # Set single wood slabs in between
    # Western roofing slabs
    MC.setBlocks(
        POS.x + HOUSE_X[0], upper_row_y, POS.z + HOUSE_Z[1],
        POS.x + HOUSE_X[0], upper_row_y, POS.z + HOUSE_Z[-2],
        ROOF_STAIRS_WEST
        )
    # Northern roofing slabs
    MC.setBlocks(
        POS.x + HOUSE_X[1], upper_row_y, POS.z + HOUSE_Z[0],
        POS.x + HOUSE_X[-2], upper_row_y, POS.z + HOUSE_Z[0],
        ROOF_STAIRS_NORTH
        )
    # Eastern roofing slabs
    MC.setBlocks(
        POS.x + HOUSE_X[-1], upper_row_y, POS.z + HOUSE_Z[1],
        POS.x + HOUSE_X[-1], upper_row_y, POS.z + HOUSE_Z[-2],
        ROOF_STAIRS_EAST
        )
    # Southern roofing slabs
    MC.setBlocks(
        POS.x + HOUSE_X[1], upper_row_y, POS.z + HOUSE_Z[-1],
        POS.x + HOUSE_X[-2], upper_row_y, POS.z + HOUSE_Z[-1],
        ROOF_STAIRS_SOUTH
        )


def upper_level():
    ''' Build the mezzanine level '''
    # The floor of the mezzanine level
    upper_level_y = FLOOR_Y + 5
    MC.setBlocks(
        POS.x + HOUSE_X[1], upper_level_y, POS.z + HOUSE_Z[1],
        POS.x + HOUSE_X[-2], upper_level_y, POS.z + HOUSE_Z[-2],
        block.DOUBLE_WOODEN_SLAB.id, 1
        )
    # The upper floor wall
    MC.setBlocks(
        POS.x + HOUSE_X[1], upper_level_y + 1, POS.z + HOUSE_Z[1],
        POS.x + HOUSE_X[-2], upper_level_y + 1, POS.z + HOUSE_Z[-2],
        POLES
        )
    # The upper floor roof
    MC.setBlocks(
        POS.x + HOUSE_X[1] - 2, upper_level_y + 2, POS.z + HOUSE_Z[1] - 2,
        POS.x + HOUSE_X[-2] + 2, upper_level_y + 2, POS.z + HOUSE_Z[-2] + 2,
        ROOF_SLAB
        )
    # The upper floor roof stairs
    MC.setBlocks(
        POS.x + HOUSE_X[1], upper_level_y + 2, POS.z + HOUSE_Z[1],
        POS.x + HOUSE_X[-2], upper_level_y + 2, POS.z + HOUSE_Z[-2],
        ROOF_STAIRS_NORTH
        )
    # Clear the upper floor
    MC.setBlocks(
        POS.x + HOUSE_X[2], upper_level_y + 1, POS.z + HOUSE_Z[2],
        POS.x + HOUSE_X[-3], upper_level_y + 2, POS.z + HOUSE_Z[-3],
        block.AIR.id
        )
    # Add the decorative corner blocks
    # Northwest corner
    MC.setBlock(
        POS.x + HOUSE_X[1], upper_level_y + 2, POS.z + HOUSE_Z[1], ROOF_CORNERS
        )
    MC.setBlock(
        POS.x + HOUSE_X[0], upper_level_y + 2, POS.z + HOUSE_Z[0], ROOF_CORNERS
        )
    MC.setBlock(
        POS.x + HOUSE_X[0] - 1, upper_level_y + 2, POS.z + HOUSE_Z[0] - 1,
        ROOF_CORNERS
        )
    # Southwest corner
    MC.setBlock(
        POS.x + HOUSE_X[1], upper_level_y + 2, POS.z + HOUSE_Z[-2], ROOF_CORNERS
        )
    MC.setBlock(
        POS.x + HOUSE_X[0], upper_level_y + 2, POS.z + HOUSE_Z[-1], ROOF_CORNERS
        )
    MC.setBlock(
        POS.x + HOUSE_X[0] - 1, upper_level_y + 2, POS.z + HOUSE_Z[-1] + 1,
        ROOF_CORNERS
        )
    # Northeast corner
    MC.setBlock(
        POS.x + HOUSE_X[-2], upper_level_y + 2, POS.z + HOUSE_Z[1], ROOF_CORNERS
        )
    MC.setBlock(
        POS.x + HOUSE_X[-1], upper_level_y + 2, POS.z + HOUSE_Z[0], ROOF_CORNERS
        )
    MC.setBlock(
        POS.x + HOUSE_X[-1] + 1, upper_level_y + 2, POS.z + HOUSE_Z[0] - 1,
        ROOF_CORNERS
        )
    # Southeast corner
    MC.setBlock(
        POS.x + HOUSE_X[-2], upper_level_y + 2, POS.z + HOUSE_Z[-2],
        ROOF_CORNERS
        )
    MC.setBlock(
        POS.x + HOUSE_X[-1], upper_level_y + 2, POS.z + HOUSE_Z[-1],
        ROOF_CORNERS
        )
    MC.setBlock(
        POS.x + HOUSE_X[-1] + 1, upper_level_y + 2, POS.z + HOUSE_Z[-1] + 1,
        ROOF_CORNERS
        )
    # Build the upper panels
    MC.setBlocks(
        POS.x + HOUSE_X[2], upper_level_y + 1, POS.z + HOUSE_Z[4],
        POS.x + HOUSE_X[-3], upper_level_y + 5, POS.z + HOUSE_Z[5],
        PANELS
        )
    MC.setBlocks(
        POS.x + HOUSE_X[2], upper_level_y + 1, POS.z + HOUSE_Z[-6],
        POS.x + HOUSE_X[-3], upper_level_y + 5, POS.z + HOUSE_Z[-5],
        PANELS
        )
    # Build the upper posts
    MC.setBlocks(
        POS.x + HOUSE_X[2], upper_level_y + 1, POS.z + HOUSE_Z[2],
        POS.x + HOUSE_X[-3], upper_level_y + 2, POS.z + HOUSE_Z[2],
        POLES
        )
    MC.setBlocks(
        POS.x + HOUSE_X[2], upper_level_y + 1, POS.z + HOUSE_Z[3],
        POS.x + HOUSE_X[-3], upper_level_y + 3, POS.z + HOUSE_Z[3],
        POLES
        )
    MC.setBlocks(
        POS.x + HOUSE_X[2], upper_level_y + 1, POS.z + HOUSE_Z[6],
        POS.x + HOUSE_X[-3], upper_level_y + 6, POS.z + HOUSE_Z[6],
        POLES
        )
    MC.setBlocks(
        POS.x + HOUSE_X[2], upper_level_y + 1, POS.z + HOUSE_Z[-4],
        POS.x + HOUSE_X[-3], upper_level_y + 3, POS.z + HOUSE_Z[-4],
        POLES
        )
    MC.setBlocks(
        POS.x + HOUSE_X[2], upper_level_y + 1, POS.z + HOUSE_Z[-3],
        POS.x + HOUSE_X[-3], upper_level_y + 2, POS.z + HOUSE_Z[-3],
        POLES
        )
    # Clear the upper floor
    MC.setBlocks(
        POS.x + HOUSE_X[3], upper_level_y + 1, POS.z + HOUSE_Z[2],
        POS.x + HOUSE_X[-4], upper_level_y + 6, POS.z + HOUSE_Z[-3],
        block.AIR.id
        )
    # Put the north roof on
    MC.setBlocks(
        POS.x + HOUSE_X[1], upper_level_y + 3, POS.z + HOUSE_Z[2],
        POS.x + HOUSE_X[-2], upper_level_y + 3, POS.z + HOUSE_Z[2],
        ROOF_STAIRS_NORTH
        )
    MC.setBlocks(
        POS.x + HOUSE_X[1], upper_level_y + 4, POS.z + HOUSE_Z[3],
        POS.x + HOUSE_X[-2], upper_level_y + 4, POS.z + HOUSE_Z[3],
        ROOF_STAIRS_NORTH
        )
    MC.setBlocks(
        POS.x + HOUSE_X[1], upper_level_y + 5, POS.z + HOUSE_Z[4],
        POS.x + HOUSE_X[-2], upper_level_y + 5, POS.z + HOUSE_Z[4],
        ROOF_STAIRS_NORTH
        )
    MC.setBlocks(
        POS.x + HOUSE_X[1], upper_level_y + 6, POS.z + HOUSE_Z[5],
        POS.x + HOUSE_X[-2], upper_level_y + 6, POS.z + HOUSE_Z[5],
        ROOF_STAIRS_NORTH
        )
    # Put the South roof on
    MC.setBlocks(
        POS.x + HOUSE_X[1], upper_level_y + 3, POS.z + HOUSE_Z[-3],
        POS.x + HOUSE_X[-2], upper_level_y + 3, POS.z + HOUSE_Z[-3],
        ROOF_STAIRS_SOUTH
        )
    MC.setBlocks(
        POS.x + HOUSE_X[1], upper_level_y + 4, POS.z + HOUSE_Z[-4],
        POS.x + HOUSE_X[-2], upper_level_y + 4, POS.z + HOUSE_Z[-4],
        ROOF_STAIRS_SOUTH
        )
    MC.setBlocks(
        POS.x + HOUSE_X[1], upper_level_y + 5, POS.z + HOUSE_Z[-5],
        POS.x + HOUSE_X[-2], upper_level_y + 5, POS.z + HOUSE_Z[-5],
        ROOF_STAIRS_SOUTH
        )
    MC.setBlocks(
        POS.x + HOUSE_X[1], upper_level_y + 6, POS.z + HOUSE_Z[-6],
        POS.x + HOUSE_X[-2], upper_level_y + 6, POS.z + HOUSE_Z[-6],
        ROOF_STAIRS_SOUTH
        )
    # Set the CAPSTONE
    MC.setBlocks(
        POS.x + HOUSE_X[0], upper_level_y + 7, POS.z + HOUSE_Z[6],
        POS.x + HOUSE_X[-1], upper_level_y + 7, POS.z + HOUSE_Z[6],
        CAPSTONE
        )


def exterior_lights():
    ''' Build and place the exterior lights '''
    # North West corner
    # Set the light post
    MC.setBlock(
        POS.x + HOUSE_X[0] - 2, LOWER_ROOF_Y - 1, POS.z + HOUSE_Z[0] - 2,
        LIGHT_POST
        )
    # Set the light
    MC.setBlock(
        POS.x + HOUSE_X[0] - 2, LOWER_ROOF_Y - 2, POS.z + HOUSE_Z[0] - 2,
        EXTERIOR_LIGHT
        )
    # South West corner
    # Set the light post
    MC.setBlock(
        POS.x + HOUSE_X[0] - 2, LOWER_ROOF_Y - 1, POS.z + HOUSE_Z[-1] + 2,
        LIGHT_POST
        )
    # Set the light
    MC.setBlock(
        POS.x + HOUSE_X[0] - 2, LOWER_ROOF_Y - 2, POS.z + HOUSE_Z[-1] + 2,
        EXTERIOR_LIGHT
        )
    # North East corner
    # Set the light post
    MC.setBlock(
        POS.x + HOUSE_X[-1] + 2, LOWER_ROOF_Y - 1, POS.z + HOUSE_Z[0] - 2,
        LIGHT_POST
        )
    # Set the light
    MC.setBlock(
        POS.x + HOUSE_X[-1] + 2, LOWER_ROOF_Y - 2, POS.z + HOUSE_Z[0] - 2,
        EXTERIOR_LIGHT
        )
    # South East corner
    # Set the light post
    MC.setBlock(
        POS.x + HOUSE_X[-1] + 2, LOWER_ROOF_Y - 1, POS.z + HOUSE_Z[-1] + 2,
        LIGHT_POST
        )
    # Set the light
    MC.setBlock(
        POS.x + HOUSE_X[-1] + 2, LOWER_ROOF_Y - 2, POS.z + HOUSE_Z[-1] + 2,
        EXTERIOR_LIGHT
        )


def interior_torches():
    ''' Set the interior torches '''
    torch_y = FLOOR_Y + 3
    wall_torch_n = block.TORCH.id, 1
    MC.setBlock(
        POS.x + HOUSE_X[4] - 5, torch_y, POS.z, wall_torch_n
        )


clear_space()
build_grounds()
verandah_stairs()
build_floor()
house_posts()
wall_panels()
lower_roof()
upper_level()
exterior_lights()
interior_torches()
door()
