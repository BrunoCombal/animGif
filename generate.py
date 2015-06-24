#!/usr/bin/python

import cairo
import PIL

def example1():
    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, 390, 60)
    cr=cairo.Context(ims)

    cr.set_source_rgb(0,0,0)
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(40)

    cr.move_to(10, 50)
    cr.show_text("Hello world!!!")

    ims.write_to_png("image.png")


def cloud_anim():
    outName="anim"
    WW=956
    HH=375
    animStep=20
    startOffset=-500
    
    imgList=[]
    for ii in range(0,WW, animStep):
        ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, WW, HH)
        cr=cairo.Context(ims)

        cr.set_source_rgb(200,200,200)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(100)

        cr.move_to(ii+startOffset, int(HH/2.0))
        cr.show_text("Meteorology")
        ims.write_to_png( "{0}_{1:04d}.png".format(outName, ii) )

    # do animation
    # convert -delay 20 -loop 0 -dispose Background anim_*.png animation.gif
    # high quality: remove alpha channel
    # convert -bordercolor white -background white -alpha remove -layers OptimizePlus -delay 10 anim_*.png animation.gif
        
if __name__=="__main__":
    cloud_anim()

    #end of script
