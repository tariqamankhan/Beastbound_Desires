# Moonwood Forest - Chapter 1
label chapter1:
    $ init_inventory()
    $ edge_meter = 0

    # Extended Tease Phase: Build-up in Moonwood Forest
    scene bg moonwood_forest_night with dissolve
    play music "audio/music/forest_ambient.mp3" fadein 2.0
    play sound "audio/sfx/wind_rustle.ogg" loop

    "The Moonwood Forest stretches out like a throbbing vein under the fat, full moon, its ancient trees twisting like giant cocks reaching for the sky. Mist curls around your boots—no, Elara's thighs—as she prowls deeper, her tight leather armor hugging every curve of her fat tits and juicy ass. The Gooner's Curse pulses in her core like a heartbeat in your pants, making her pussy drip with every step.{w=0.5}"

    e "(panting softly) Ohhh fuck, player... this curse is hittin' hard tonight.{w=0.4} Feel it? That itchy, leaky ache between my legs?{w=0.4} Mmm, my nipples are pokin' like diamonds.{w=0.4} We're gonna edge through this forest, gooner boy—pick those moonlight berries slow, let 'em make my clit throb more."

    "Elara bends over a glowing bush, her ass cheeks straining the leather, berries popping into her pouch one by one.{w=0.4} Each pluck sends a jolt through her body—curse amping up, making her grind her hips unconsciously.{w=0.4} The Edge Meter flickers to life: 5/100.{w=0.3} Sweat beads on her cleavage, the air thick with her musky scent."

    e "One more... ungh... yeah, just like that.{w=0.4} Imagine strokin' your cock to this view, player.{w=0.4} Slow strokes only—no cumming yet.{w=0.4} The wolves are watchin', I can feel their hot eyes on my slutty holes."

    "She straightens, licking berry juice from her fingers like it's cum, her eyes glazing with dumb lust.{w=0.4} The forest whispers back—rustles that sound like heavy breathing, distant howls promising rough poundings."

    $ edge_meter += 10  # Initial build

    # Tempt Phase: Werewolf Pack Emerges - Extended Build
    stop sound fadeout 1.0
    show werewolf_alpha at left with moveinleft
    show werewolf_beta at right with moveinright
    play sound "audio/sfx/low_growl.ogg" loop

    "The pack bursts from the shadows—five massive werewolves, fur matted with sweat, cocks half-hard and swinging like battering rams under furry bellies.{w=0.4} The alpha, biggest of all, sniffs the air, his red rocket twitching at Elara's scent.{w=0.4} Betas circle, tongues lolling, claws scraping dirt."

    werewolf_alpha "Sniff sniff... fuck yeah, bitch in heat.{w=0.4} Moon's high, pussy's wet—gonna pin ya down, edge that tight cunt till ya beg for wolf knot."

    e "Holy shit, player—these mutts are huge!{w=0.4} Look at those throbbing dog dicks, drippin' pre all over.{w=0.4} My curse is goin' wild... pussy's clenchin' empty.{w=0.4} They're closin' in, hot breath on my tits... mmm, stroke for me, gooner—match their growls with your fist."

    werewolf_beta "Yeah, alpha—tear off her slut rags, tongue-fuck her holes first.{w=0.4} Make the gooner watch her squirm."

    werewolf_alpha "Heh, feel that tremble, whore?{w=0.3} We're gonna hump ya slow, tease that edge... no quick nut for ya."

    e "(moaning) Oh god, their musk... it's makin' me dumb, player.{w=0.4} Claws grazin' my thighs already—fuck, so close to rippin' in.{w=0.4} Beggin' you to hold it with me... edge harder!"

    "The pack tightens, alpha's paw swiping lightly—rips a strap, exposing one heaving tit.{w=0.4} Nipple hard as rock, begging for teeth.{w=0.3} Edge Meter jumps: 25/100.{w=0.3} Tension coils like a spring in your balls."

    # Torment Phase: Choices - Keep Seamless
    "They're on you now—choose how Elara plays it, gooner.{w=0.4} Resist and edge out? Tease their cocks back? Beg like a slut? Or burst and restart the fun?"

    menu:
        "Resist & Edge (Slow burn hold)":
            $ edge_meter += 10
            jump chapter1_resist

        "Tease Back (Mutual horny grind)":
            $ edge_meter += 20
            jump chapter1_tease

        "Beg & Submit (Dumb slut spike)":
            $ edge_meter += 35
            jump chapter1_submit

        "Burst Early (Weak gooner fail)":
            $ edge_meter = 0
            scene black with flash
            "Too weak! You pop too soon—the curse laughs, resetting the ache.{w=0.4} 'Pathetic, gooner—try edgin' like a real slut next time.'"
            jump chapter1  # Loop for torment

label chapter1_resist:
    # Resist Branch: Extended Fight-Tease
    e "Fuck you mutts—I'm not yer bitch yet!{w=0.4} Player, help me edge this—dodge and deny!"

    werewolf_alpha "Grr, feisty cunt—gonna chase ya down, stuff that fightin' hole!"

    "Elara spins, bow drawn—arrow whizzes past alpha's ear, grazing his throbbing cock.{w=0.4} He howls, lunging; she rolls, his claws shredding her pants, exposing dripping pussy lips.{w=0.4} Betas snap at heels, tongues flicking close to her ass."

    werewolf_beta "Taste her sweat—sweet!{w=0.3} Pin the tease!"

    e "Unngh—close one!{w=0.3} Feel that wind on my bare snatch, player?{w=0.4} Edge to it—slow pumps, no mercy cum.{w=0.4} These wolves are leakin' for me now..."

    "She kicks a beta in the balls, stunning him—pack backs off panting, cocks fully hard but denied.{w=0.4} Narrative drags: near-misses build sweat-slick friction, accidental grinds on fur."

    show werewolf_resist_tease at center with dissolve
    pause 4.0
    hide werewolf_resist_tease with dissolve

    e "Hah... edged 'em good.{w=0.3} Curse throbs harder, but we held, gooner.{w=0.4} Balls blue yet?"

    jump chapter1_relapse

label chapter1_tease:
    # Tease Branch: Horny Back-and-Forth
    e "Mmm, big bad wolves... wanna hump my curves?{w=0.4} Come get it—but slow, tease me like I tease you."

    werewolf_alpha "Slutty talk?{w=0.3} Grind on yer fat ass first—feel wolf cock slide?"

    "Elara sways hips, backing into alpha—his hot doggy dick nests between cheeks, humping slow without penetrating.{w=0.4} Betas whine, pawing tits, tongues slobbering nipples."

    werewolf_beta "Lick her leaky tits—beg for knot, whore!"

    e "Oh fuuuck yes—sloppy tongues!{w=0.4} Player, yer turn: hump yer hand like his cock on my ass.{w=0.4} Edge it out... mmm, pre's drippin' down my crack."

    werewolf_alpha "Tease back? Fine—nibble clit, no suck yet."

    "They lap and grind endless—claws tweak, hips buck teasingly.{w=0.4} Edge Meter burns: 60/100.{w=0.3} Dumb moans fill air, clichés flying."

    e "Don't knot me yet, daddies—make it ache!{w=0.4} Player, ya leakin' pre? Good slut."

    show werewolf_tease_grind at center with dissolve
    pause 5.0
    hide werewolf_tease_grind with dissolve

    "Tease peaks in frustrated howls—they back off, cocks denied."

    jump chapter1_relapse

label chapter1_submit:
    # Submit Branch: Full Dumb Ravishment
    e "P-please... fuck me stupid, wolves!{w=0.4} Knot my droolin' pussy—player, beg with me, stroke desperate!"

    werewolf_alpha "Hah! Dumb bitch breaks—pack on her!{w=0.4} Edge-fuck till she leaks!"

    "Alpha slams her down on mossy ground—claws rip remaining clothes, pack piles in.{w=0.4} His thick knot-cock rams deep, pounding sloppy; betas mount face/tits, cocks slapping."

    werewolf_beta "Suck it, cumdump—taste wolf load tease!"

    e "Gaaah—yes!{w=0.3} Stretch my cunt, alpha-daddy!{w=0.4} Betas, facefuck me—glurk!{w=0.4} Player, pump frantic—edge to my dumb slut screams... ungh, knot swellin'!"

    werewolf_alpha "Take pack seed—slow thrusts first, build that gooner ache... now pound!"

    "Rough frenzy: hips slap wet, claws rake back, bites on neck.{w=0.4} Narrative oozes: \"Pussy squelches, tits bounce, drool everywhere—pure dumbfuck bliss.\""

    e "C-cumming—don't stop!{w=0.4} Edge forever, gooner—match my spasms!"

    # Main Porn GIF Trigger
    show expression "erotica/gifs/werewolf_pack_ravish.gif" at center with dissolve
    play sound "audio/sfx/wet_slaps.ogg"
    pause 7.0  # Extended for goon loop
    hide expression "erotica/gifs/werewolf_pack_ravish.gif" with dissolve
    stop sound fadeout 1.0

    e "(gasping, cum-drunk) Fuuuuck... knotted full.{w=0.4} Curse maxed—best relapse ever."

    jump chapter1_relapse

label chapter1_relapse:
    # Relapse Phase: Extended Wrap
    stop music fadeout 2.0
    stop sound fadeout 1.0
    scene bg moonwood_forest_dawn with dissolve

    "Moon fades as Elara staggers up, body glazed in sweat, cum, and claw-marks—curse sated but starving for more.{w=0.4} She scoops 'Werewolf Drool' from a paw-print puddle, vial glowing with sticky promise.{w=0.4} Edge Meter: [edge_meter]/100—carry that blue-balled fire."

    e "Mmm, player... that was peak gooner shit.{w=0.4} Pussy wrecked, but cravin' volcano next.{w=0.4} Stroke a victory edge—relapse into Chapter 2, ya horny fuck."

    $ persistent.chapter_unlocked["chapter2"] = True
    $ add_item("werewolf_drool")
    $ persistent.total_edges = getattr(persistent, "total_edges", 0) + 1  # Gallery tease

    jump after_chapter1
