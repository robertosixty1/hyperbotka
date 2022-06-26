#!/bin/env python3

import discord
from dotenv import load_dotenv
from os import getenv

load_dotenv()
TOKEN = getenv("DISCORD_TOKEN")
ADM = getenv("GUILD_ADM")
ABOUT = getenv("GUILD_ABOUT_CHANNEL")

def list_to_string(l):
    string = ""
    for i in l:
        string += i + " "
    return string

### BEGIN COMMANDS ###

class Command():
    command: str
    message: str
    def __init__(self, command, message):
        self.command = command
        self.message = message

commands = [
    Command("addcmd"      , "Added command:\n    >>> %@"),
    Command("ping"        , "Pong!"),
    Command("help"        , "Available commands:\n    %help"),
    Command("cpp"         , "**Rust**"),
    Command("rust"        , "https://rustrecoveryfoundation.neocities.org/"),
    Command("python"      , "Loading..."),
    Command("anime"       , "Kids are not supposed no play around on hanime.tv"),
    Command("riir"        , "Have you considered rewriting %1 in rust?"),
    Command("whoami"      , "Of course you are %sender"),
    Command("killme"      , "%sender was killed"),
    Command("about"       , f"%about"),
    Command("crunchyroll" , "%sender Are you serious? I just can't understand how can somebody pay for that shit, it is an buggy website (BUGGY) that requires you to pay to watch anime, it is just like... are you joking? That's unbealiveable, or even more specifically, that's unbearable."),
    Command("amogus"      , "%sender STOP POSTING ABOUT AMONG US! I'M TIRED OF SEEING IT! MY FRIENDS ON TIKTOK SEND ME MEMES, ON DISCORD IT'S FUCKING MEMES! I was in a server, right? and ALL OF THE CHANNELS were just among us stuff. I-I showed my champion underwear to my girlfriend and t-the logo I flipped it and I said \"hey babe, when the underwear is sus HAHA DING DING DING DING DING DING DING DI DI DING\" I fucking looked at a trashcan and said \"THAT'S A BIT SUSSY\" I looked at my penis I think of an astronauts helmet and I go \"PENIS? MORE LIKE PENSUS\" AAAAAAAAAAAAAAHGESFG"),
    Command("hentai"      , "%sender It wasn't THAT extreme, I was only drawing ass, but I covered up the drawing in time. The problem was that I had a ahem reference photos... on my phone... and my teacher totally saw.... WHAT DO I DO THIS IS SO EMBARRASSING 😭😭😭"),
    Command("megumin"    , """%sender Megumin's cuteness is a miracle of the universe, it behooves you to create as many little megumins as humanly possible.

With back-to-back pregnancies every 10.5 months and assuming she hits menopause around age 51, you could get around 43 births out of her.

Statistically some of those will be twins, with the rate generally increasing with age and height/weight. Using data from https://www.cdc.gov/nchs/products/databriefs/db80.htm you'd get an average twinning rate of 44.1 per 1000 births. It would be on the low side initially, but as her body fat percentage rose from pregnancy it would even out. With those numbers you'd expect to get 2 sets of twins, but if she has a family history of twins that could rise to around 4-5.

If you gave her certain fertility drugs (specifically gonadotropins), that would increase the chances of multiple birth substantially to 3 in 10, with around 5 percent of those being triplets or more. In that case, you'd expect 13 sets of twins, with one of them potentially being triplets instead.

So you should have 45 children with Megumin if you do it naturally, and 57 children if you use fertility drugs."""),
    Command("oniichan", "%sender Gasps Onii-chaaaaan jump onto and hugs Ｏ(≧∇≦)Ｏ I missed you sniffs () fuah I love your boy smell Onii-chan (w) , Huh? Don't sniff you? Don't be silly Onii-chan I love you why can't I show my affection? (─‿‿─)♡ Hahaha your face is red. Woah Onii-chan why are you pushing me on to the bed? ヽ(°〇°)ﾉ Kyaaaaa don't tickle me Onii-chan haha counter ataaaaack pushes you down ヽ(>∀<☆)ノ. Hehehe I win! Onii-chan your face is really red now, Hmmh smirks (=-ω-=) perhaps you're falling in love with me? Chuuuuu (ﾉ´ з )ノ kisses you Woah O-onii-chan w-what are you d-doing?! H-hyyaaaaa don't take off my panties! D-dont look at my private spot! (/▽＼) Ah Ah Don't lick me there it's dirty! Ahhhhhh fuah ah ah (//ω//) O-onii-chan a-are you going to put it in? O-ok i'm ready. (／。＼) Heeeee I-it hurts. ~(>_<~) SWow dwon ah ah MMMH O-onii-chan I Lwve yoouuuuu! AHHHHHHH MMMHHH AH Hah Hah hah O-ONIII-CHAAANN you baka why did you do it inside? ヽ(д´)ノ W-well if it felt good for you i'm happy, b-but make sure you take responsibility. (ღ˘⌣˘ღ)"),
    Command("gigachad", "%sender I'm a man. A real man that gets his cocked suck. I do not eat pussy. I make sure a woman understands that I'm a dom and she is a sub. A real goddamn man. And it hurts to see emasculation in other men. This is frame."),
    Command("touhou", "%sender STOP SAYING TOUHOU IS ANIME! I'M TIRED OF SEEING IT! MY FRIENDS ON TIKTOK SEND ME JAPANESE GOBLIN, ON DISCORD MEMORIES OF PHANTASM! I was in a server, right? and ALL OF THE CHANNELS were just asking \"what anime are these\". I-I showed my Marisa Figurine to my girlfriend and t-the big eyes I looked at it and I said \"hey babe, when the Touhou is anime HAHA Shiranai wa sonna mahou Omoi wa tsutaetara kowarechau Anata to wa chigau kara Hito no kokoro made kantan ni nusumanaide\" I fucking looked at a apple and said \"THAT'S A BAD APPLE\" I looked at Remelia I think of two zero zero eight three four and I go \"HEY MISTER, WANNA HAVE S-\" AAAAAAAAAAAAAAHGESFG"),
    Command("tsundere", "%sender Oh senpai, hey! I didn't know you walked this way. We're right in front of your house? I-I wasn't looking or anything, I just happened to be walking by! It'd be creepy to know where you live, s-stupid! What was I walking by for? OKAY! I had to give you something! L-listen, Don't get the wrong idea, I was just up at 4 am cooking like schoolgirls do and it happened to be your favorite and I thought maybe you'd like some since I had extra! BE GRATEFUL! UGHHIUGH! Uhh, how did I know it was your favorite? Well I... aaaAAAAAAAHHH!"),
    Command("hedied", "%1 Rest in piss! Was never miss!")
]

def format_message(message, args, context) -> str:
    final_message = ""
    i = 0
    while i < len(message):
        if message[i] == "%":
            if len(message) != (i + 1):
                if message[i+1].isnumeric():
                    i += 1
                    a = message[i]
                    try:
                        final_message += args[int(a)]
                    except: pass
                else:
                    if len(message) != (i + 1):
                        i += 1
                        f = ""
                        ret = ""
                        while not message[i].isspace():
                            f += message[i]
                            if len(message) != (i + 1):
                                i += 1
                            else:
                                break
                        if f == "help":
                            for c in commands:
                                ret += "!" + c.command + " "
                        elif f == "sender":
                            ret += f"<@{context.author.id}>"
                        elif f == "@":
                            for a in args[1:]:
                                ret += a + "  "
                        elif f == "adm":
                            ret += f"<@{ADM}>"
                        elif f == "about":
                            ret += f"<#{ABOUT}>"
                        final_message += ret
                        final_message += " "
            else:
                final_message += message[i]
        else:
            final_message += message[i]
        i += 1
    return final_message

### END COMMANDS ###

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(context):
    if context.author == client.user:
        return

    if context.content.startswith("!"):
        args = context.content.split()
        command = args[0][1:]
        send = True

        for c in commands:
            if c.command == command:
                if command == "addcmd":
                    if context.author.id == int(ADM):
                        if len(args) >= 3:
                            m = list_to_string(args[2:])
                            cmd = args[1]
                            commands.append(Command(cmd, m))
                    else:
                        await context.channel.send(format_message("Only %adm XD", args, context))
                        send = False
                if send:
                    try:
                        await context.channel.send(format_message(c.message, args, context))
                    except discord.errors.HTTPException:
                        await context.channel.send("ERROR: Uh oh! That was a bad request, please try again ok! (Maybe arguments are missing?)")

client.run(TOKEN)
