from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

i=0
while True:
    i = i+1
    mc.postToChat("第"+str(i)+"次")
    time.sleep(1)