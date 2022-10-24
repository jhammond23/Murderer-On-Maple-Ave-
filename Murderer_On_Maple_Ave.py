import random
import time

events = []


def game():
    intro()
    ready = valid_input('\n         Are you ready to catch a murderer? '
                        '\n', ['yes', 'no'])
    if ready == 'yes':
        intro_sequence()
    else:
        return
    to_store_path_choice()
    play_again()


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        write(f'Sorry, the option {option} is invalid. Try agian! \n')


def write(string, delay=0):
    print(string)
    time.sleep(delay)


def intro():
    print('          *******************************')
    print('          *        Welcome to...        *')
    print('          *  The Murderer On Maple Ave  *')
    print('          *******************************')


def intro_sequence():
    write('\n\n  "GET UP!"', 3)
    write('  "GEEEEET UP! I\'m tired of waiting on you."', 3)
    write('  "You have to go with me." \n', 3)
    write('Awoken by a small, annoying, yet all too familiar voice, ', 3)
    write('you slowly and reluctantly begin to open your eyes.', 3)
    wake_up_question = input('Half asleep and confused, you mumble: ').lower()
    if "who" in wake_up_question:
        write(' \n  "I\'m your little sister, dumb dumb," She spits.', 3)
    elif "where" in wake_up_question:
        if "go" in wake_up_question:
            write(' \n  "We have to go to the store."', 3)
        else:
            write(' \n  "We\'re at our house, dumb dumb," '
                  'Spits your younger sister.', 3)
    elif "what" in wake_up_question:
        if "doing" in wake_up_question:
            write(' "We have to go to the store."', 3)
        else:
            write(' \n  "Huh..." sighed your sister.', 3)
    else:
        write('  "You\'re not making any sense," '
              'Spits your younger sister.', 3)
    write('  "Just c\'mon! We have to go pick up some food for '
          'Mom\'s \'big\' party tonight." \n', 4)
    write('As your mind starts to become a little less sleep '
          'ridden, you remember ', 4)
    write('the party that your little sister, Megan, is mockily '
          'referring to.\n', 4)
    write('  "Mom says that since Mr. Hank and the Garcia twins '
          'went missing, ', 4)
    write('  I\'m not \'old\' enough to go anywhere by '
          'myself..." \n\n', 6)
    print('Slowly climbing out of bed, the sad reminder of your '
          'missing childhood friends, ')
    write('Daniel and Maria Garcia, envelopes your thoughts. \n\n', 6)
    print('As you\'re trying to put your shoes on, Megan '
          'continues to pepper you ')
    write('with things you need to grab at the store. \n', 4)
    write('  "...also some chips... and... UGH. I forgot Mom said '
          'her new \'bOyFRienD\' is coiming tonight." \n', 6)
    print('Your reminder of sadness turns to concern, as neither '
          'you, nor your sister, ')
    write('particularly \'like\' this oddly edgy, mystery man. \n\n', 6)


def to_store_path_choice():
    write('As the two of you are getting in the car, Megan says, \n', 4)
    write('  "We have 3 hours until the party. We should take Maple '
          'Ave, not Dickerson St. ', 4)
    path_choice = valid_input('  Dickerson is shorter, but there will '
                              'probably be construction traffic. So which '
                              'way do you wanna go?" '
                              '\n\n', ['dickerson', 'maple'])
    if path_choice == 'dickerson':
        write(' \n "Ugh. Whatever, Dumb Dumb. If we\'re late, '
              'I\'m blaming it on you." \n\n', 4)
        events.append("dickerson")
        short_path()
    else:
        write(' \n "I\'m glad we can finally agree on something. '
              'Just drive fast." \n\n', 4)
        events.append('maple')
        go_to_store()


def short_path():
    print('On the car ride to the store, you\'re slowed down by '
          'traffic caused by a construction zone.')
    write('A minute passes by and the traffic still hasn\'t moved. '
          'Then you hear your sister say, \n', 6)
    write('  "Woah, wait a minute... Isn\'t that Mr. Hank\'s '
          'jacket he always wore?" \n', 6)
    print('Concentrated, she points to a thick, woodsy edge of '
          'the contruction zone where, sure enough, ')
    print('an old, brown, slim-fit jacket hung empty on a tree, '
          'just like the one that the missing Mr. Hank used to wear.')
    write('You don\'t believe your eyes and try to play if off as '
          'just some leaves, but Megan insists you go check it out. \n', 9)
    write('  "I swear, that is HIS jacket. Go get it!" Megan '
          'forcefully said. \n', 6)
    print('You respond with: ')
    check_jacket = valid_input('   1.) find a safe place to stop, then go '
                               'check it out \n'
                               '   2.) keep drving to the store '
                               '\n\n', ['1', '2'])
    if '1' in check_jacket:
        safe_place_to_stop()
    else:  # '2' in check_jacket:
        write('  "You never do anything I want!" Megan yelled. She turns '
              'away angrily and remains silent for the rest of '
              'the ride. \n', 4)
        events.append('maple')
        go_to_store()


def safe_place_to_stop():
    print('You wait a couple minutes for traffic to subside, then find '
          'a nearby street to turn onto.')
    write('As you find a parking spot next to the nearby woods, Megan '
          'turns to you and says, \n', 6)
    write('  "Uhhhm... I\'m not going through the woods. There\'s '
          'probably millions of spiders in there. YOU go check '
          'it out, Dumb Dumb." \n\n', 6)
    will_you_leave_megan = valid_input('You sit there for a moment, but then '
                                       'decide to: \n'
                                       '   1.) Agree and go into the woods '
                                       'alone to grab the jacket \n'
                                       '   2.) Make Megan go with you to grab'
                                       ' the jacket \n\n', ['1', '2'])
    if "1" in will_you_leave_megan:
        check_jacket_alone()
    else:   # elif "2" in will_you_leave_megan:
        check_jacket_together()


def check_jacket_alone():
    print('You agree and decide to go find the coat by yourself. '
          'After warning your sister to be safe and stay in the car, ')
    print('you enter the woods and head toward the construction zone. '
          'The overgrown timber makes it difficult to navigate to ')
    write('the jacket. As you brush a spider off your shirt, you '
          'think to yourself it was probably a good decision to let '
          'your sister stay. \n', 16)
    print('After about 5 minutes of traversing through the thicket, '
          'you find the woodsy tree line bordering the construction zone. ')
    print('Sure enough, the slim-fit, brown jacket is draped over a '
          'branch. Not knowing what to do, you call the police to inform '
          'them of your finding. ')
    write('To your suprise, you\'re met with an unthankful, worried voice '
          'from the officer on the phone, barking orders to, "stay out '
          'of the woods." \n', 16)
    write('Surprised at the unwelcomed conversation, you snatch the '
          'lifeless, brown jacket and quickly start off back to '
          'your car. \n', 4)
    events.append("jacket")
    write('As the car slowly becomes visible, you realize your car doors '
          'are thrown open and your sister is gone. \n', 4)
    events.append("megan_missing")
    print('Heart racing, your mind immediately begins thinking the worst. '
          'Half terrified of what your mom will say, yet half trying '
          'to convince ')
    print('yourself, you pull out your phone, but can\'t decide whether '
          'to call your mom or drive to the store a couple blocks ')
    write('away to check if she just walked there to get a start on '
          'your shopping. \n', 16)
    print('After a moment of heavy contemplation, you decide to: ')
    megan_missing = valid_input('   1.) call your mom and tell her '
                                'everything \n'
                                '   2.) drive to the nearby store to see if '
                                'she had walked there \n', ['1', '2'])
    if "1" in megan_missing:
        call_mom()
    else:   # elif "2" in megan_missing:
        go_to_store()


def check_jacket_together():
    write('Regardless of Megan\'s wishes, you make her go '
          'with you. \n', 4)
    print('After about 5 minutes of traversing through the thicket, '
          'you find the woodsy tree line bordering the construction zone. ')
    print('Sure enough, the slim-fit, brown jacket is draped over a '
          'branch. Not knowing what to do, you call the police to '
          'inform them of your finding. ')
    write('To your suprise, you\'re met with an unthankful, worried '
          'voice from the officer on the phone, barking orders to, '
          '"stay out of the woods." \n', 16)
    write('Surprised at the unwelcomed conversation, you decide to '
          'leave the lifeless, brown jacket and quickly start '
          'off back to your car. \n', 4)
    write('After a few more minutes of navigating back to your car, '
          'you finally see the car peaking over the brush at you, '
          'just as you left it. \n', 4)
    print('You both hop in the car and head to go and grab your '
          'groceries like you had intended to in the first place. \n')
    events.append('store')
    go_to_store()


def go_to_store():
    if "megan_missing" in events:
        print('Screeching to a hault, you quickly hop out of your car '
              'in search of Megan. As you run around the store, ')
        print('people begin to stare with curiosity. The manager, '
              'a family friend of yours, flags you down and cheerfully '
              'asks, \n')
        answer_to_manager = input('   "Hey, you! What\'re you up to today? '
                                  'What\'s all this runnin\' about?" \n\n'
                                  'You respond with, \n').lower()
        write('As you explain the situation to him, the previously cheerful'
              ' expression quickly fades to worry. ', 4)
        print('   "Oh no... Well, I\'m awfully sorry, but your sister hasn\'t '
              'been in here today. Your mom\'s boyfriend ')
        print('   was just here, though. He said he was headed '
              'to your place," he says as a matter of factly. '
              '"I\'m sorry! ')
        write('   I wish i could\'ve been more help." \n', 16)
        print('You hurriedly thank him and head back to your car, hoping '
              'to see Megan sitting in the front seat, ')
        print('just like nothing had happened. Becoming dishearted at the '
              'sight of an empty passenger seat, you contemplate ')
        write('your next best option. Should you call your mom? \n\n ', 16)
        print('Though, something just felt \'off\'. The store manager '
              'mentioned seeing your mom\'s boyfriend right before ')
        print('Megan went missing. The store is close enough by to '
              'entertain the thought... You start wondering that, ')
        print('yeah, he may be odd, but is he \'that\' kind of odd? '
              'You remember Mom mentioning he was on probation, ')
        write('but taking his new girlfriend\'s daughter didn\'t seem '
              'like something he would do. \n', 20)
        post_store_choice = valid_input('Sitting in the driver\'s seat, '
                                        'after some serious contemplating, '
                                        'you decide to: \n'
                                        '   1.) Call your mom and tell her '
                                        'everything that has happened \n'
                                        '   2.) Head home and see if Mom\'s '
                                        'boyfriend is there \n\n', ['1', '2'])
        if "1" in post_store_choice:
            call_mom()
        else:   # elif "2" in post_store_choice:
            check_at_home()
    else:
        print('Pulling into the store parking lot, you\'re met with a '
              'wide open parking lot. In fact, there is only ')
        write('three other vehicles here. \n', 6)
        go_inside = valid_input('As you step out of the car, Megan asks '
                                'if she can stay outside. You consider it '
                                'for a moment, then: \n'
                                '   1. tell her she can stay in the car. \n'
                                '   2. tell her she has to come inside with '
                                'you. \n', ['1', '2'])
        if "1" in go_inside:
            events.append("store_alone")
            print('You make your way inside and start grabbing groceries. '
                  'After about ten minutes of shopping, you head towards ')
            write('the checkout. \n', 6)
            print('Suddenly, you hear a scream coming from outside. Shocked, '
                  'you squint at the window to see a man breaking into ')
            write('your car. \n', 6)
            print('You leave your cart and run outside to rescue your sister. '
                  'As you\'re running closer, you recognize the aggressor ')
            write('as the missing Mr. Hank! \n', 6)
            write('Stunned at the situation, you still barrel towards him '
                  'at top speed and tackle him. \n', 4)
            fight_scene()
        else:   # elif "2" in go_inside:
            write('   "Ugh. You suck, Dumb Dumb. You\'re no fun." \n', 3)
            print('You and Megan both go inside to grab stuff for your '
                  'mom\'s party. When you ask Megan to list the items she ')
            print('had mentioned while you were getting ready to leave '
                  'the house, she, instead of answering, turns her head ')
            write('and ignores you. A moment of silence goes by and '
                  'she sassily says, \n', 16)
            write('   "What\'re you gonna do? Send me to the car?" \n', 3)
            store_argument = valid_input('Upset with her attitude, you: \n'
                                         '   1.) Let her have her way and send'
                                         ' her back to the car. \n'
                                         '   2.) Make her stay in the store '
                                         'with you. \n', ['1', '2'])
            if "1" in store_argument:
                print('\n You tell her she can go back to the car and wait '
                      'until you finish shopping. You then call your mom '
                      'and she ')
                write('tells you what items you need to grab for the party '
                      'tonight. \n', 12)
                print('As you finish up your shopping, you head towards the '
                      'checkout and hear a scream. Startled, you peer '
                      'out the ')
                write('window toward you car and see someone trying '
                      'to break in, with Megan in the passenger '
                      'seat! \n', 12)
                print('You leave your cart and run outside to rescue your '
                      'sister. As you\'re running closer, you recognize '
                      'the aggressor ')
                write('as the missing Mr. Hank! \n', 10)
                write('Stunned at the situation, you still barrel '
                      'towards him '
                      'at top speed and tackle him. \n', 6)
                events.append('store_alone')
                fight_scene()
            else:   # elif "2" in store_argument:
                events.append("store_items")
                print('Megan then decides to slient for the rest of the trip. '
                      'So, you call your mom and ask her what items '
                      'she needs ')
                write('for the party. \n', 10)
                print('After grabbing everything and checking out, you and '
                      'megan head back to the empty car to go home. ')
                write('Seeing as how you didn\'t have issues on the first '
                      'drive down, you decide to, again, take Maple Ave. ', 12)
                long_path()


def long_path():
    if "store_items" in events:
        events.append("boring")
        write('You, again, uneventfully drive home to deliver the '
              'groceries to your mom. \n', 4)
        check_at_home()
    elif "dickerson" in events:
        print('As you head home, you see that the road construction has '
              'blocked Dickerson st, the road you previously came down. ')
        write('So, you take the only other, longer option, Maple ave. \n', 6)
        print('Your foot pushes a little too hard on the gas pedal, '
              'as you forget about everything else in the world. Your sister ')
        print('is missing on YOUR account. You can\'t help but feel '
              'guilty because, she was right. Maple ave is MUCH faster... ')
        write('and all this could have been avoided hadn\'t we just '
              'drove down this road instead. \n', 16)
        print('Blinded by your thoughts, you notice there is a cop '
              'car trailing you with their lights on. ')
        write('Well #@!#. You look down and see you\'re going 25mph '
              'over the speed limit. Actually... maybe the officer '
              'can help! \n', 9)
        print('You excitedly pull over to the right side of the road, '
              'followed by the flashing lights. '
              'As the officer approaches your ')
        write('vehicle, you connect an eerily similar voice with an '
              'interaction you had earlier that day. \n', 9)
        print('   "Well, well, well! If it isn\'t the nosy, trespassing '
              'kid," barked an all too familiar voice. ')
        write('   "How many other laws have you broken today, ki-" \n', 6)
        write('He stops mid-sentence as he sees the same brown jacket '
              'you described to him during your call to the police.')
        print('   "AHHHH, NOT ONLY do we have trespassing and speeding here, '
              'but we ALSO have TAMPERING OF EVIDENCE!" \n')
        print('He yelled, turning blue in the face. He rips open your '
              'back door and grabs the brown jacket like it was '
              'his all along.')
        write('The offier quickly returned to his car and took off. '
              'No "goodbye," no "stay here," nothing. \n', 20)
        print('Almost too stunned to move, you decided your reason '
              'for heading home outweighed waiting around for a bit. ')
        write('A little more cautious of your speed, you drove home '
              'down the clear stretch of road. \n\n', 9)
        events.append("officer")
        check_at_home()
    else:
        events.append("maple")
        print('As you drive down Maple Ave, you realize Megan was right. '
              'This street was EMPTY. Nothing interesting to see at all. ')
        write('In fact, this road was kinda boring and uneventful. \n', 9)
        write('After a short while, you arrive at the store to grab '
              'some groceries. ', 4)
        go_to_store()


def call_mom():
    if "megan_missing" in events:
        print('You decide it\'s best to call your mom and explain '
              'the situation. Even through the phone you can sense '
              'the dismay ')
        write('settle in your mom\'s tone. She mumbles with an anxious, '
              'shaky voice, \n', 10)
        print('   "But... we were just at the store. I waited in '
              'the car while he went inside. I heard a kid screaming, but I '
              'did\'t ')
        write('   think much of it." \n', 9)
        write('You decide it\'s best to run home and explain the '
              'situation in person and show her the coat you found. ', 4)
        events.append("called_mom")
        long_path()


def check_at_home():
    if "megan_missing" in events:
        print('Upon arriving at home, Mom rushes out of the front '
              'door and begins to hammer you with questions about her '
              'missing daughter. ')
        write('You learn that she has been with her boyfriend for '
              'the whole morning, which wipes your suspicion of him '
              'partaking in this. \n', 9)
        print('As you explain the strange interaction with the police '
              'officer, you also mention the call you had with the '
              'officer as well. ')
        print('Your mom points out two abnormal points in your story. First, '
              'the fact that you found a missing man\'s coat. ')
        write('Second, the officer wasn\'t helpful in either interactions '
              'you had with him that day. \n', 16)
        write('Your mom tries calling the police station, but the call went '
              'straight to the answering machine. \n', 4)
        look_for_megan()
    elif "boring" in events:
        write('After arriving at home, you sit around, with plenty of time'
              ' left, and wait for the party to begin. \n', 4)
        end_scene()


def look_for_megan():
    write('With no other options, you all three decide to go to the '
          'spot where Megan was taken. \n', 6)
    print('On your drive down Dickerson St, you concentratedly '
          'point to the spot you found the coat, not unlike Megan ')
    print('had just earlier that day. As you\'re looking at the '
          'woodsy edge, you notice an awfully ')
    write('familiar looking man standing around the tree the coat '
          'was hanging from. \n', 16)
    write('   "Uhmm... Do you see that man walking over there?" '
          'Your mom asks wide-eyed as she points to the mystery man. \n', 6)
    write('You keep silent, praying you were both imagining things. '
          'Now a little faster, you continue pushing towards your'
          ' parking spot. \n', 6)
    print('Upon arriving at your old parking spot, you find two other '
          'vehicles: the cop car you had saw previously and what looks like ')
    print('Mr. Hank\'s old truck. Now confused and curious, all '
          'three of you hop out of your car and barrel towards the old '
          'truck. \n')
    write('Looking inside the window, you see what looks like the '
          'missing Daniel and Maria Garcia\'s matching bracelets. \n', 16)
    print('At that moment, you hear some rustling from the bushes '
          'behind you and a man jumps out, grabs ahold of your arm. ')
    write('Without hesitation, you begin to fight your mystery '
          'attacker. \n', 10)
    fight_scene()


def fight_scene():
    hank_health = 100
    while hank_health > 0:
        hit = (random.randrange(10, 50, 10))
        hank_health -= hit
        rand_fight_action = random.randrange(1, 8)
        lines(rand_fight_action, hit, hank_health)


def lines(rand_fight_action, hit, hank_health):
    if hank_health <= 0:
        hank_health = 0
    if hank_health == 0:
        post_fight()
    if rand_fight_action == 1:
        one = valid_input('Grabbing the attacker, you: \n'
                          '1.) Throw a quick punch \n'
                          '2.) Try to shove him to the ground \n', ['1', '2'])
        if "1" in one:
            print(f'Quickly, you land a jab, dealing {hit} damage. ')
        else:   # elif "2" in one:
            print(f'You push as hard as you can, shoving him to '
                  'the ground, doing {hit} damage. ')
        write(f'Your attacker now has {hank_health} hit points left. \n', 4)
    elif rand_fight_action == 2:
        two = valid_input('A small distance is created between you. '
                          'You choose to: \n'
                          '1.) pick up a nearby stick to hit with \n'
                          '2.) close the gap with a running punch '
                          '\n', ['1', '2'])
        if "1" in two:
            print(f'You pick up the stick and swing it like a bat, '
                  'hitting him with it. You kick him doing {hit} damage. ')
        else:   # elif '2' in two:
            print(f'You run at the attacker and throw a wicked '
                  'running punch, dealing {hit} damage. ')
        write(f'Your attacker now has {hank_health} hit points left. \n', 4)
    elif rand_fight_action == 3:
        three = valid_input('The attacker grabs onto you. Without much to do, '
                            'you: \n'
                            '1.) Grab the nearby rock to hit him with \n'
                            '2.) Bite his arm to make him let go '
                            '\n', ['1', '2'])
        if "1" in three:
            print(f'You quickly bend down, grab a rock, then '
                  'smack him with it, doing {hit} damage. ')
        else:   # elif '2' in three:
            print(f'Without thinking, you bit his arm as hard as '
                  'you can, doing {hit} damage. Your mouth is filled '
                  'with a nasty, unbathed taste. ')
        write(f'Your attacker now has {hank_health} '
              'hit points left. \n', 4)
    elif rand_fight_action == 4:
        four = valid_input('Now in close combat, you either throw a: \n'
                           '1.) punch to the stomach \n'
                           '2.) a kick to the legs \n', ['1', '2'])
        if '1' in four:
            print(f'You throw a puch to the stomach as hard as '
                  'you can, doing {hit} damage. ')
        else:   # elif '2' in four:
            print(f'Presented with a perfect opportunity, you '
                  'throw a kick to his legs, knocking him to '
                  'the ground, dealing {hit} damage. ')
        write(f'Your attacker now has {hank_health} hit points left. \n', 4)
    elif rand_fight_action == 5:
        five = valid_input('Beginning to second guess his actions, it '
                           'looks like your attacker tries to get away. '
                           'You react by: \n'
                           '1.) chasing him down and tackling him \n'
                           '2.) Throwing a rock at him to knock him '
                           'down \n', ['1', '2'])
        if '1' in five:
            print(f'You sprint after him, tackling him to the ground, '
                  'doing {hit} damage. ')
        else:   # elif '2' in five:
            print(f'You throw a rock and it hits the man, knocking '
                  'him down and doing {hit} damage. ')
        write(f'Your attacker now has {hank_health} hit points left. \n', 4)
    elif rand_fight_action == 6:
        six = valid_input('The attacker hits you, knocking you to the '
                          'ground. From there, you: \n'
                          '1.) get back up and throw a punch \n'
                          '2.) kick the attacker\'s legs out from '
                          'under him \n', ['1', '2'])
        if "1" in six:
            print(f'You stand back up and throw a punch, '
                  'doing {hit} damage. ')
        else:   # elif '2' in six:
            print(f'Laying on the ground, you kick his legs, '
                  'dealing {hit} damage. ')
        write(f'Your attacker now has {hank_health} hit '
              'points left. \n', 4)


def post_fight():
    if "megan_missing" in events:
        write('As you land the last blow on your attacker, he falls '
              'to the ground, knocked out.', 4)
        print('\n\n   "...MR. HANK?!" Yelled your mom as she '
              'fumbled over her words, looking at the man lying '
              'on the ground in front of her. ')
        write('   "We actually just got attacked by a someone '
              'who was... well... WE ALL THOUGHT WAS DEAD!" She '
              'said harshly. \n', 9)
        write('At the precise end of her sentance, the cop '
              'from earlier came out of the woods with Megan '
              'lying limp in his arms. \n', 4)
        write('   "She\'s gonna be alright," says the cop as he '
              'gently marched out of the brush. \n', 4)
        write('   "MEGAN! Everyone yelled as your family ran '
              'towards the woodsy timber line. ', 4)
        print('Confused in cop\'s roll in the situation, '
              'everyone starts asking questions, only to have '
              'the officer respond with, \n')
        print('   "I know y\'all have many questions, but I '
              'can\'t answer everything right now. I can '
              'understand if you\'re upset with me, ')
        print('   but I\'ve been on the edge of cracking this case '
              'for a month now. What matters is your sister '
              'is safe and you ')
        write('   caught Mr. Hank. He won\'t be able to hurt '
              'anyone, anymore. You guys are safe." \n', 20)
        write('Megan slowly turns her head to you, looks at '
              'you and says, \n', 4)
        write('   "Thanks for saving me, Dumb Dumb," she '
              'says with a small, but thankful smile. \n\n', 4)
        events.append("megan_found")
        end_scene()
    elif "store_alone" in events:
        write('As you hit the mystery man one last time, the '
              'attacker falls to the ground, knocked out. ', 4)
        write('Almost immediately, you recognize your agressor '
              'as the missing Mr. Hank! \n', 4)
        write('   "Mr. Hank?! What was he doing trying to '
              'attack us? I thought he was dead!" Yelled your '
              'sister. \n', 4)
        print('You call the cops and explain the situation. '
              'The officer hangs up quickly and speeds over. ')
        print('Upon arrival, he explains how he had been '
              'suspecting Mr. Hank the whole time. '
              'He was worried Hank would ')
        write('try to make a move on anyone snooping around, '
              'so he tried keeping the case quiet. \n', 16)
        print('Tough, the officer thanks you and your sister '
              'for helping and takes Mr. Hank away in handcuffs. \n')
        write('   "Thanks, Dumb Dumb," Megan said with a smile. '
              '"You saved me."', 12)
        events.append("store_ending")
        play_again()


def end_scene():
    if "megan_found" in events:
        write('Congratulations! You finished the game. '
              'You found the most entertaining ending, ending #1. ', 4)
    elif "boring" in events:
        write('Congratulations! You finished the game. '
              'You found the most boring ending, ending #2. ', 4)
    elif "store_ending" in events:
        write('Congratulations! You finished the game. '
              'Megan is safe. You found ending #3.', 4)
    play_again()


def play_again():
    answer = valid_input('\n *** Would you like to play again? *** '
                         '\n', ['yes', 'no'])
    if "yes" in answer:
        game()


game()
