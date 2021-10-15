#https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)

#!/bin/bash
say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=$*&tl=en"; }
#say $*
say " Hi. Welcome to Pi's kitchen. What food ingredients would you want?"

arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav ingredients.wav
python3 ingredient.py ingredients.wav

say "Got it! What taste would you like?"

arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav taste.wav
python3 taste.py taste.wav
python3 recommend.py

say "Great! Here are dishes I recommend for you. When you've like to choose one dish, you can wave your hand at the top of the sensor to get the detail recipe."
cat recipes.txt |while read line
do
    echo $line;
    say $line
    python3 gesture.py
    if [ $? == 20 ]
    then
        echo $line
        say "Here is the recipe of "$line
        x=`python3 read_recipe.py $line`
        say "${x}"
        exit
    fi
done

say "Thank you for visiting Pi's kitchen. Have a nice meal."