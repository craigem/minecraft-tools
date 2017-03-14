#!/usr/bin/python2.7

''' dome_base.py
Produces a dome base for Minecraft.
'''

import mcpi.minecraft as minecraft
import mcpi.block as block

MC = minecraft.Minecraft.create()

POS = MC.player.getTilePos()
