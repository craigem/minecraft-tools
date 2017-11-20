#!/usr/bin/python2.7

''' theHouse.py
Produces a house for us in Minecraft.
'''

import mcpi.minecraft as minecraft
import mcpi.block as block

MC = minecraft.Minecraft.create()

POS = MC.player.getTilePos()

# House dimensions
HOUSE_SLAB_X = list(range(3, 20))
HOUSE_SLAB_Z = list(range(-1, 8))

# Grounds
GROUNDS_Y = POS.y - 1
GROUNDS_X1 = POS.x - 10
GROUNDS_Z1 = POS.z - 10
GROUNDS_X2 = POS.x + 27
GROUNDS_Z2 = POS.z + 27

# Set blocks
CLEAR = block.AIR.id
GROUNDS = block.GRASS.id
SLAB = block.STONE.id

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
        POS.x + HOUSE_SLAB_X[0],
        GROUNDS_Y,
        POS.z + HOUSE_SLAB_Z[0],
        POS.x + HOUSE_SLAB_X[-1],
        GROUNDS_Y,
        POS.z + HOUSE_SLAB_Z[-1],
        SLAB
        )
    # Build the wooden floor
    MC.setBlocks(
        POS.x + HOUSE_SLAB_X[0],
        GROUNDS_Y,
        POS.z + HOUSE_SLAB_Z[0],
        POS.x + HOUSE_SLAB_X[-1],
        GROUNDS_Y,
        POS.z + HOUSE_SLAB_Z[-1],
        SLAB
        )

clear_space()
build_grounds()
build_floor()
