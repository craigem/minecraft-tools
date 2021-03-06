#!/usr/bin/python2.7

''' sphere.py
Produces a sphere in Minecraft.
The bottom half is cobblestone and grass. The top half is air and glass.

If run while at ground level, it will produce what looks like a dome on level
ground.
'''

import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to the Minecraft server
MC = minecraft.Minecraft.create()

# Get the platers current position
POS = MC.player.getTilePos()

# Set the sphere radius
RADIUS = 21
DOME = block.GLASS.id

# Set the blocks to use
DOME_GROUND = block.GRASS.id
AIR = block.AIR.id
GLASS = block.GLASS.id


def build_sphere():
    ''' Clears a level space and builds a dome over the top '''
    for x_plot in range(-RADIUS, RADIUS):
        for z_plot in range(-RADIUS, RADIUS):
            # Build the lower hemisphere:
            for y_plot in range(-RADIUS, 0):
                plot = x_plot ** 2 + y_plot ** 2 + z_plot ** 2
                # Set the ground blocks
                if plot < (RADIUS - 1) ** 2 and y_plot == - 1:
                    MC.setBlock(
                        POS.x + x_plot, POS.y + y_plot, POS.z + z_plot,
                        DOME_GROUND
                        )
                # Set the subterranean blocks
                elif plot < RADIUS ** 2:
                    MC.setBlock(
                        POS.x + x_plot, POS.y + y_plot, POS.z + z_plot,
                        block.COBBLESTONE.id
                        )
            # Build the upper hemisphere
            for y_plot in range(0, RADIUS):
                plot = x_plot ** 2 + y_plot ** 2 + z_plot ** 2
                # Clear the space with an air block
                if plot < (RADIUS - 1) ** 2:
                    MC.setBlock(
                        POS.x + x_plot, POS.y + y_plot, POS.z + z_plot, AIR
                        )
                # Build the dome
                elif plot > (RADIUS - 1) ** 2 and plot < RADIUS ** 2:
                    MC.setBlock(
                        POS.x + x_plot, POS.y + y_plot, POS.z + z_plot, GLASS
                        )


build_sphere()
