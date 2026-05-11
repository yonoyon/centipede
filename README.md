This program is still very much a WIP - don't be surprised if you find some weird stuff in the code.

In this game, you must solve a centipede. In other words, permute a list into correct order.
Two game modes are available, those being sandbox and levels.

The core idea behind it was to recreate a thought experiment of mine. Imagine a centipede with an x amount of segments.
Each segment has one pair of legs - say we swapped the segments around now. To help the centipede
move again, we must put the segments back into correct order, also making sure that the legs remain
oriented correctly. Something something group theory, parity.

To solve it, you must input moves, those being very simple. 
All you have to do is input position (i) and direction (sign). Here's what an example solve 
would look like with the "adjacent swap - sign flip" move type.

[-2, 4, 3, -1]  ~ 4-  
[-2, 4, 1, -3]  ~ 2+  
[-2, -1, -4, -3] ~ 3+  
[-2, -1, 3, 4] ~ 2-  
[1, 2, 3, 4] -> solved!

Thanks for reading. Have fun!
