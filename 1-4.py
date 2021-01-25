from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
 
x = 200
y = 200
z = 200

mc.player.setTilePos(x,y,z)
time.sleep(2)
            
x = x -50
y = y -50
z = z -50
mc.player.setTilePos(x,y,z)
time.sleep(2)

x = x -50
y = y -50
z = z -50
mc = Minecraft.create(x,y,z)