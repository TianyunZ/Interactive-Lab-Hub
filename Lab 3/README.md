# Chatterboxes
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Additional Parts

As mentioned during the class, we ordered additional mini microphone for Lab 3. Also, a new part that has finally arrived is encoder! Please remember to pick them up from the TA.

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.
### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using a USB microphone, and the speaker on your webcamera. (Originally we intended to use the microphone on the web camera, but it does not seem to work on Linux.) In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)

The file is called google_tts_greeting.sh

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

One thing you might need to pay attention to is the audio input setting of Pi. Since you are plugging the USB cable of your webcam to your Pi at the same time to act as speaker, the default input might be set to the webcam microphone, which will not be working for recording.

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

The file is called ask_for_zipcode.sh

Bonus Activity:

If you are really excited about Speech to Text, you can try out [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) and [voice2json](http://voice2json.org/install.html)
There is an included [dspeech](./dspeech) demo  on the Pi. If you're interested in trying it out, we suggest you create a seperarate virutal environment for it . Create a new Python virtual environment by typing the following commands.

```
pi@ixe00:~ $ virtualenv dspeechexercise
pi@ixe00:~ $ source dspeechexercise/bin/activate
(dspeechexercise) pi@ixe00:~ $ 
```

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*
<img src="storyboard.jpg" alt="setup" width="800">



Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

\*\***Please describe and document your process.**\*\*
- Once the Pi is turned on, it will ask the user what kind of ingredients she/he wants to have today.
- The user will speak out names of ingredients she/he wants to eat.
- The Pi will ask for what kind of taste the user wants.
- The user will speak out the taste.
- The Pi will search and recommond recipe for the user based on her/his choices, and show the recipe on the screen.
- The pi will ask the user whether to continue.
- If the user wants to continue, the dialogue will loop, otherwise, it will end.

### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*


https://user-images.githubusercontent.com/50896698/136033695-fbc98fe4-c786-4443-8a53-dba0b31a3743.mp4

The user tends to say a whole sentence, instead of words of ingredients and tastes. I think it's more difficult for Pi to recogonize. And the solution may be give the user some instructions at the beginning.

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...
2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?
3. Make a new storyboard, diagram and/or script based on these reflections.

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

Here is the script of the interaction between a user and the system.

- Pi: say "Hi. Welcome to Pi's kitchen. What food ingredients would you want?"
- User: say words or sentences including one or several food ingredients.
- Pi: say "Got it! What taste would you like?"
- User: say the taste
- Pi:
-- Say "Great! Here are dishes I recommend for you. When you've like to choose one dish, you can wave your hand at the top of the sensor to get the detail recipe.".
-- say dish name one by one, with a 3-second interval among each other.
- User: Wave hands on the sensor when they want to choose a dish
- Pi: say "Here is the recipe of [the name of the dish]", following with the detailed recipe.
- Pi: say "Thank you for visiting Pi's kitchen. Have a nice meal."

![storyboard2](https://user-images.githubusercontent.com/50896698/137568532-1671f1a4-20ee-4a4d-b721-c3e3f83ddf4a.jpg)


*Include videos or screencaptures of both the system and the controller.*

(The control logic is written in the program, so I only recorded the Pi in my video.)

https://user-images.githubusercontent.com/50896698/137434172-bf2ca426-9d38-42a5-8db3-3172f96af075.mp4


## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

https://user-images.githubusercontent.com/50896698/137503630-c0008ea2-7b3f-4a37-840a-5327c6bae21a.mp4

https://user-images.githubusercontent.com/50896698/137526877-1f92ad47-d5e9-4f8b-a25a-86a5d65e0109.mp4


Answer the following:

### What worked well about the system and what didn't?
\*\**your answer here*\*\*

The system can record and recognize users' voices most of time. And based on users' words, it can give reasonable recommendation recipes. And the guesture sensor works well to detect users' wave.

However, the microphone does not work very well, and users have to speak loudly and near to the microphone to make sure their voice be recorded clearly.

### What worked well about the controller and what didn't?

\*\**your answer here*\*\*

I wrote the whole logic using SHELL and Python. The advantages are it is manual operation free and automatical. It can suggest dishes based on ingredients and tastes provided by users.

However, the disadvantages is that the recipes are limited, because those are needed to add by myself. And this process cost more time than I expected. And the voice detection function is not sensitive enough to recognise low voice. 


### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

\*\**your answer here*\*\*

I think I can use more voice control features in the interactions between users and product, since it is more convinient for users to use when they are not available to touch the product. Also, I need to consider more about user senarios, for example, in the case of cooking, users are tend to not touch the machine because their hands can be wet, and they don't want to see the screen for recipes, because it is not convinient. So that I can use more voice control and gesture control instead of pressing and touching.

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

\*\**your answer here*\*\*

The system can record audio spectrums of [unk] words, and use them to train models and get more accurate recognition performance. And it can also record ingredients and tastes that are not in the recipe dataset but spoken out by users, so that to enlarge the recipe dataset. Also, the system can record audio spectrum of each user and to recognize different users' voices better.

There can be a sensor to detect current temprature, and the system can suggest recipe based on the temperature. For example, when it is cold, the system will recommend more hot dishes.
