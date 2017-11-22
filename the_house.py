#!/usr/bin/python2.7

''' the_house.py
Produces a house for us in Minecraft.
'''

import mcpi.minecraft as minecraft
import mcpi.block as block

MC = minecraft.Minecraft.create()

POS = MC.player.getTilePos()

# House dimensions
HOUSE_FLOOR_SLAB_X = list(range(3, 20))
HOUSE_FLOOR_SLAB_Z = list(range(-1, 8))
HOUSE_FLOOR_WOOD_X = list(range(7, 20))
HOUSE_FLOOR_WOOD_Z = list(range(8, 12))
HOUSE_FLOOR_DECK_X = list(range(7, 20))
HOUSE_FLOOR_DECK_Z = list(range(12, 16))

# Grounds
GROUNDS_Y = POS.y - 1
GROUNDS_X1 = POS.x - 10
GROUNDS_Z1 = POS.z - 10
GROUNDS_X2 = POS.x + 27
GROUNDS_Z2 = POS.z + 27

# Set blocks
CLEAR = block.AIR.id
GROUNDS = block.GRASS.id
HOUSE_FLOOR_SLAB_BLOCK = block.STONE.id
HOUSE_FLOOR_WOOD_BLOCK = block.WOOD_PLANKS.id, 3
HOUSE_FLOOR_DECK_BLOCK = block.WOOD_PLANKS.id, 4

def clear_space():
    ''' Clear a space for the house by setting it to AIR '''
    MC.setBlocks(
        GROUNDS_X1,
        GROUNDS_Y,
        GROUNDS_Z1,
        GROUNDS_X2,
        GROUNDS_Y + 100,
        GROUNDS_Z2,
        CLEAR
        )

def build_grounds():
    ''' Build the grounds and gardens '''
    # Fill in the grounds
    MC.setBlocks(
        GROUNDS_X1,
        GROUNDS_Y,
        GROUNDS_Z1,
        GROUNDS_X2,
        GROUNDS_Y,
        GROUNDS_Z2,
        GROUNDS
        )

def build_floor():
    ''' Build all the floors '''
    # Build the slab
    MC.setBlocks(
        POS.x + HOUSE_FLOOR_SLAB_X[0],
        GROUNDS_Y,
        POS.z + HOUSE_FLOOR_SLAB_Z[0],
        POS.x + HOUSE_FLOOR_SLAB_X[-1],
        GROUNDS_Y,
        POS.z + HOUSE_FLOOR_SLAB_Z[-1],
        HOUSE_FLOOR_SLAB_BLOCK
        )
    # Build the wooden floor
    MC.setBlocks(
        POS.x + HOUSE_FLOOR_WOOD_X[0],
        GROUNDS_Y,
        POS.z + HOUSE_FLOOR_WOOD_Z[0],
        POS.x + HOUSE_FLOOR_WOOD_X[-1],
        GROUNDS_Y,
        POS.z + HOUSE_FLOOR_WOOD_Z[-1],
        HOUSE_FLOOR_WOOD_BLOCK
        )
    # Build the wooden deck
    MC.setBlocks(
        POS.x + HOUSE_FLOOR_DECK_X[0],
        GROUNDS_Y,
        POS.z + HOUSE_FLOOR_DECK_Z[0],
        POS.x + HOUSE_FLOOR_DECK_X[-1],
        GROUNDS_Y,
        POS.z + HOUSE_FLOOR_DECK_Z[-1],
        HOUSE_FLOOR_DECK_BLOCK
        )

def build_walls():
    ''' Build all the walls'''
    # Build the slab walls
    MC.setBlocks(
        POS.x + HOUSE_FLOOR_SLAB_X[0],
        GROUNDS_Y + 1,
        POS.z + HOUSE_FLOOR_SLAB_Z[0],
        POS.x + HOUSE_FLOOR_SLAB_X[-1],
        GROUNDS_Y + 4,
        POS.z + HOUSE_FLOOR_SLAB_Z[-1],
        HOUSE_FLOOR_SLAB_BLOCK
        )
    # Clear inside the slab walls
    MC.setBlocks(
        POS.x + HOUSE_FLOOR_SLAB_X[0] + 1,
        GROUNDS_Y + 1,
        POS.z + HOUSE_FLOOR_SLAB_Z[0] + 1,
        POS.x + HOUSE_FLOOR_SLAB_X[-1] - 1,
        GROUNDS_Y + 4,
        POS.z + HOUSE_FLOOR_SLAB_Z[-1] - 1,
        CLEAR
        )
    # Clear the interior slab wall
    MC.setBlocks(
        POS.x + HOUSE_FLOOR_SLAB_X[0] + 5,
        GROUNDS_Y + 1,
        POS.z + HOUSE_FLOOR_SLAB_Z[0] + 8,
        POS.x + HOUSE_FLOOR_SLAB_X[-1] - 1,
        GROUNDS_Y + 4,
        POS.z + HOUSE_FLOOR_SLAB_Z[0] + 8,
        CLEAR
        )

clear_space()
build_grounds()
build_floor()
build_walls()
