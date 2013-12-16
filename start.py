#
# cocos2d
# http://cocos2d.org
#
# This code is so you can run the samples without installing the package
import sys
import os
import random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#

import cocos
from cocos.actions import *

ranNum = random.randint(50,200)
# A color layer  is a Layer with the a color attribute
class HelloWorld(cocos.layer.ColorLayer):
    def __init__(self):
        # blueish color
        super( HelloWorld, self ).__init__( 136,169,220,ranNum)

        # a cocos.text.Label is a wrapper of pyglet.text.Label
        # with the benefit of being a CocosNode
        label = cocos.text.Label('Be-Ok',
            font_name='Mono',
            font_size=12,
            color=(100,100,100,255),
            anchor_x='center', anchor_y='center')
        daLabel = cocos.text.Label('A Adventure Horror game by BroBeur Studios',
            font_name='Mono',
            font_size=12,
            anchor_x='center', anchor_y='center')

        # set the label in the center of the screen
        label.position = 300,400
	daLabel.position = 250, 300
        self.add( daLabel )
        self.add( label )
        
        # similar to cocos.text.Label, a cocos.sprite.Sprite
        # is a subclass of pyglet.sprite.Sprite with the befits of
        # being a CocosNode.
        sprite = cocos.sprite.Sprite('02.png')
        DaSprite = cocos.sprite.Sprite('11.png')
        
        # sprite in the center of the screen (default is 0,0)
        sprite.position = 300,300
        DaSprite.position = 300,200
        
        # sprite scale attribute starts with 3 (default 1 )
        sprite.scale = 1
        DaSprite.scale = 1
        
        # add the sprite as a child, but with z=1 (default is z=0).
        # this means that the sprite will be drawn on top of the label
        self.add( sprite, z=1 )
        self.add( DaSprite, z=0 ) 

        # create a ScaleBy action that lasts 2 seconds
        scale = ScaleBy(100, duration=20)
        
        # tell the label to scale and scale back and repeat these 2 actions forever
        label.do( Repeat( scale + Reverse( scale) ) )
        
        # tell the sprite to scaleback and then scale, and repeat these 2 actions forever
        sprite.do( Repeat( Reverse(scale) + scale ) )

if __name__ == "__main__":
    # director init takes the same arguments as pyglet.window
    cocos.director.director.init()

    # We create a new layer, an instance of HelloWorld
    hello_layer = HelloWorld ()
    
    # tell the layer to perform a Rotate action in 10 seconds.
    hello_layer.do( RotateBy(90, duration=60) )


    # A scene that contains the layer hello_layer
    main_scene = cocos.scene.Scene (hello_layer)

    # And now, start the application, starting with main_scene
    cocos.director.director.run (main_scene)

    # or you could have written, without so many comments:
    #      director.run( cocos.scene.Scene( HelloWorld() ) )

