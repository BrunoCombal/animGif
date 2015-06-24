#!/bin/bash

# create the animation slides: anim_###.png
./generate.py

# now put background: animbck_###.png, animfrg_###.png
for ii in anim_*.png
do
    index=`echo ${ii%.png} | sed 's/anim_//'`
    echo $ii $index
    convert -composite rsrc/sky_background.png ${ii} animbck_${index}.png
    convert -composite animbck_${index}.png rsrc/cloud_foreground.png animfrg_${index}.png
    rm -f ${ii}
    rm -f animbck_${index}.png
done

convert -bordercolor white -background white -alpha remove -layers OptimizePlus -delay 10 animfrg_*.png out/animation.gif
rm -f animfrg_*.png


# end of script
