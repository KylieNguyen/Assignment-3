from mcpi.minecraft import Minecraft

# Assignment 3 main file
# Feel free to modify, and/or to add other modules/classes in this or other files

mc = Minecraft.create("127.0.0.1",51966)
message = "Hello world"
mc.postToChat(message)