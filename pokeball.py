#!/usr/bin/python2.7

''' dome_base.py
Produces a dome base for Minecraft.
'''

import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to the Minecraft server
MC = minecraft.Minecraft.create()

# Get the platers current position
POS = MC.player.getTilePos()

# Set the sphere radius
RADIUS = 21

# Set the blocks to use
DOME_TOP = block.CONCRETE.id, 14
DOME_WALL = block.CONCRETE.id, 15
DOME_BOTTOM = block.CONCRETE.id
DOME_GROUND = block.CONCRETE.id
AIR = block.AIR.id


def build_dome():
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
                        POS.x + x_plot, POS.y + y_plot, POS.z + z_plot, DOME_BOTTOM
                        )

            # Build the upper hemisphere
            for y_plot in range(-1, RADIUS):
                plot = x_plot ** 2 + y_plot ** 2 + z_plot ** 2
                # Build the base of the dome
                if y_plot < 2:
                    if plot > (RADIUS - 1) ** 2 and plot < RADIUS ** 2:
                        MC.setBlock(
                            POS.x + x_plot, POS.y + y_plot, POS.z + z_plot,
                            DOME_WALL
                            )
                # Build the dome
                elif plot > (RADIUS - 1) ** 2 and plot < RADIUS ** 2:
                    MC.setBlock(
                        POS.x + x_plot, POS.y + y_plot, POS.z + z_plot, DOME_TOP
                        )
                # Clear the space with an air block
                elif plot < (RADIUS - 1) ** 2:
                    MC.setBlock(
                        POS.x + x_plot, POS.y + y_plot - 3, POS.z + z_plot, AIR
                        )


build_dome()
