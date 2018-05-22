from termcolor import colored as c
from replit import clear
clear()
list1 = ['artless', 'bawdy', 'beslubbering', 'bootless', 'churlish', 'cockered', 'clouted', 'craven', 'currish', 'dankish', 'dissembling', 'droning', 'errant', 'fawning', 'fobbing', 'froward', 'frothing', 'gleeking', 'goatish', 'gorbellied', 'impertinent', 'infectious', 'jarring', 'loggerheaded', 'lumpish', 'mammering', 'mangled', 'mewling', 'paunchy', 'pribbling', 'puking', 'puny', 'quailing', 'rank', 'reeky', 'roguish', 'ruttish', 'saucy', 'spleeny', 'spongy', 'surly', 'tottering', 'unmuzzled', 'vain', 'venomed', 'villainous', 'warped', 'wayward', 'weedy', 'yeaty']
list2 = ['base-court', 'bat-fowling', 'beef-witted', 'beetle-headed', 'boil-brained', 'clapper-clawed', 'clay-brained', 'common-kissing', 'crook-pated', 'dismal-dreaming', 'dizzy-eyed', 'doghearted', 'dread-bolted', 'earth-vexing', 'elf-skinned', 'fat-kidneyed', 'fen-sucked', 'flap-mouthed', 'fly-bitten', 'folly-fallen', 'fool-born', 'full-gorged', 'guts-griping', 'half-faced', 'hasty-witted', 'hedge-born', 'hell-hated', 'idle-headed', 'ill-nurtured', 'knotty-pated', 'milk-livered', 'motley-minded', 'onion-eyed', 'plume-plucked', 'pottle-deep', 'pox-marked', 'reeling-ripe', 'rough-hewn', 'rude-growing', 'rump-fed', 'shard-borne', 'sheep-biting', 'spur-galled', 'swag-bellied', 'tardy-gaited', 'tickle-brained', 'toad-spotted', 'urchin-snouted', 'weather-bitten']
list3 = ['apple-john', 'baggage', 'barnacle', 'bladder', 'boar-pig', 'bugbear', 'bum-bailey', 'canker-blossom', 'clack-dish', 'clotpole', 'coxcomb', 'codpiece', 'death-token', 'dewberry', 'flap-dragon', 'flax-wench', 'flirt-gill', 'foot-licker', 'fustilarian', 'giglet', 'gudgeon', 'haggard', 'harpy', 'hedge-pig', 'horn-beast', 'hugger-mugger', 'jolthead', 'lewdster', 'lout', 'maggot-pie', 'malt-worm', 'mammet', 'measle', 'minnow', 'miscreant', 'moldwarp', 'mumble-news', 'nut-hook', 'pigeon-egg', 'pignut', 'puttock', 'pumpion', 'ratsbane', 'scut', 'skainsmate', 'strumpet', 'varlet', 'vassal', 'whey-face', 'wagtail']

def aOrAn(string):
  vowels = ['a', 'e', 'i', 'o', 'u']
  if string[0] in vowels:
    return True

import random
times = int(input("How many insults would thou like?\t"))
print(c("Did you like this? Make sure to upvote it in the \"I built this (bots).\" If you want more, make sure to check out the Shipper I have also posted on \"I built this (bots).\" Make sure to upvote it too! And although, it's not that advanced, (only 4500 lines), check out my version of Alexa (also on \"I built this (bots)).\"", "green", attrs = ['dark']))
for count in range(times):
  part1 = random.choice(list1)
  part2 = random.choice(list2)
  part3 = random.choice(list3)
  
  if aOrAn(part1):
    print("\nThou art an %s %s %s." % (part1, part2, part3))
  
  else:
    print("\nThou art a %s %s %s." % (part1, part2, part3))

print()
print(c("Did you like this? Make sure to upvote it in the \"I built this (bots).\" If you want more, make sure to check out the Shipper I have also posted on \"I built this (bots).\" Make sure to upvote it too! And although, it's not that advanced, (only 4500 lines), check out my version of Alexa (also on \"I built this (bots)).\"", "red", attrs = ['dark']))