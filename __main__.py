
folder_name = "generated_files"

username = input("\n\t Roblox username: ")
rank = input("\t USME rank: ")
print(f"\n\tCreating the ET guideline for {username}....")

text = f"""
# credits to whybarana for the first version of this guideline - code made by S1 

Greetings and welcome to my ET. I am your host "{username}". You may refer to me as {rank} and {rank} only. UNDERSTOOD?  

I will now explain phases.
T-Phase, Training Phase. This means, a training is going on and the  trainer would like some silence from his tranees.
To speak, you must simply yell out "PTS" or "Permission to speak, {rank}?" and the trainer will either grant/deny.

S-Phase, silent phase. This will not be necessary in the Basic Traning, but all tranees will keep complete silence while in S-Phase.
You may only use "E-PTS" or "EMERGENCY, Permission to speak, {rank}" Usually it is because they have to go AFK, or they have to leave, or there is a shooter, ect.

IS THAT UNDERSTOOD?

T-PHASE IS NOW ACTIVE, MAKE SURE TO USE PTS TO SPEAK.

I will now go over the marching commmands.
SFL, OM! - Single File Line, On March! Meaning, you will form a single file line behind me, when i say "MARCH!"
MARCH - You will now form a single file line behind me.
PREPARE, - Which means, prepare to march.
FORWARD, - Turn your bodies forward.
MARCH! - Self explanatory.
HALT- You will stop.
STS! - You will form a line, shoulder-to-shouler.
IS THAT UNDERSTOOD?

* Hell pits: *

WELCOME TO HELL PITS.
I WILL NOW GO OVER SOME SIMPLE RULES
1) NO CHEATING. (You cant cheat much in this.)
2) NO WHINING. 
60 SECONDS FOR THE SMALL PIT.
IS THAT UNDERSTOOD?
START ON MY SHOT.

* O-Obby: *

WELCOME TO O-OBBY.
I WILL NOW GO OVER SOME SIMPLE RULES
1) NO CHEATING.
2) NO SKIPPING.
3) NO WHINING.
90 SECONDS TO DO THE WHOLE OBBY
IS THAT UNDERSTOOD?
START ON MY SHOT.

* Towers: *

WELCOME TO TOWERS.
I WILL NOW GO OVER SOME SIMPLE RULES
1) NO CHEATING.
2) NO SKIPPING A TOWER.
3) YOU MUST DO ALL 3 TOWERS.
4) START FROM THE SMALLEST TOWER.
120 SECONDS TO DO ALL 3
IS THAT UNDERSTOOD?
START ON MY SHOT.

* U-Obby: *

WELCOME TO U-OBBY.
I WILL NOW GO OVER SOME SIMPLE RULES
1) NO CHEATING.
2) NO SKIPPING. 
3) NO WHINING.
120 SECONDS TO DO IT ALL
IS THAT UNDERSTOOD?
START ON MY SHOT.

Welcome to classroom!

I will now explain sthe main rules of USAF.

1) No emotes, faces, or roleplaying.
Emotes: /e dance, /e wave, etc.
Faces: :), :(, :/, etc.
Roleplaying: *punches*, *kicks*, *dies*, etc.

2) Always respect USAF personnel, no matter rank, religion, or division.

3) Never walk on the grass at West Point.

4) No murder/attempted murder/mass murder.

I will now explain Officers Ascension Course.

To progress past the rank of SGM and to become a commissioned Officer, you must apply for OAC, or Officers Ascension Course. 
To join, you must have a dizzy account and pass the application,
which is posted in the USAF server when open. When accepted into OAC, you will receive the rank of Warrant Officer.
After, you will be able to complete requirements to progress throughout the ranks.
 It is recommended you join a division to be able to progress through the ranks past SGM because it will make the process easier and is required for higher ranks.

To gain access to more events, please join the USAF server if you are able to, so you can get notifications for events, and tryouts for divisions.

Questions time, any one got questions that they would like me to answer?
"""



f = open(f"{folder_name}/et_guideline_rank={rank}.txt", "w")
f.write(text)
f.close()
