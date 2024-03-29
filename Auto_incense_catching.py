import discord
import random
import chime
import time

ID = #928926662991687692 #Please include channel id #pkms

list_pkms = ['staravia',
'foongus',
'galarian meowth',
'bulbasaur',
'rotomu',
'Koratta',
'ivysaur',
'venusaur',
'charmander',
'charmeleon',
'charizard',
'squirtle',
'wartortle',
'blastoise',
'caterpie',
'metapod',
'butterfree',
'weedle',
'kakuna',
'beedrill',
'pidgey',
'pidgeotto',
'pidgeot',
'rattata',
'raticate',
'spearow',
'fearow',
'ekans',
'arbok',
'pikachu',
'raichu',
'sandshrew',
'sandslash',
'nidoran ',
'nidorina',
'nidoqueen',
'nidorino',
'nidoking',
'clefairy',
'clefable',
'vulpix',
'ninetales',
'jigglypuff',
'wigglytuff',
'zubat',
'golbat',
'oddish',
'gloom',
'vileplume',
'paras',
'parasect',
'venonat',
'venomoth',
'diglett',
'dugtrio',
'meowth',
'persian',
'psyduck',
'golduck',
'mankey',
'primeape',
'growlithe',
'arcanine',
'poliwag',
'poliwhirl',
'poliwrath',
'abra',
'kadabra',
'alakazam',
'machop',
'machoke',
'machamp',
'bellsprout',
'weepinbell',
'victreebel',
'tentacool',
'tentacruel',
'geodude',
'graveler',
'golem',
'ponyta',
'rapidash',
'slowpoke',
'slowbro',
'magnemite',
'magneton',
'farfetch\'d',
'doduo',
'dodrio',
'seel',
'dewgong',
'grimer',
'muk',
'shellder',
'cloyster',
'gastly',
'haunter',
'gengar',
'onix',
'drowzee',
'hypno',
'krabby',
'kingler',
'voltorb',
'electrode',
'exeggcute',
'exeggutor',
'cubone',
'marowak',
'hitmonlee',
'hitmonchan',
'lickitung',
'koffing',
'weezing',
'rhyhorn',
'rhydon',
'chansey',
'tangela',
'kangaskhan',
'horsea',
'seadra',
'goldeen',
'seaking',
'staryu',
'starmie',
'mr. mime',
'mr. rime',
'scyther',
'jynx',
'electabuzz',
'magmar',
'pinsir',
'tauros',
'magikarp',
'gyarados',
'lapras',
'ditto',
'eevee',
'vaporeon',
'jolteon',
'flareon',
'porygon',
'omanyte',
'omastar',
'kabuto',
'kabutops',
'aerodactyl',
'snorlax',
'articuno',
'zapdos',
'moltres',
'dratini',
'dragonair',
'dragonite',
'mewtwo',
'mew',
'bidoof',
'chikorita',
'bayleef',
'meganium',
'cyndaquil',
'quilava',
'typhlosion',
'totodile',
'croconaw',
'feraligatr',
'sentret',
'furret',
'hoothoot',
'noctowl',
'ledyba',
'ledian',
'spinarak',
'ariados',
'crobat',
'chinchou',
'lanturn',
'pichu',
'cleffa',
'igglybuff',
'togepi',
'togetic',
'natu',
'xatu',
'mareep',
'flaaffy',
'ampharos',
'bellossom',
'marill',
'azumarill',
'sudowoodo',
'politoed',
'hoppip',
'skiploom',
'jumpluff',
'aipom',
'sunkern',
'sunflora',
'yanma',
'wooper',
'quagsire',
'espeon',
'umbreon',
'murkrow',
'slowking',
'misdreavus',
'unown',
'wobbuffet',
'girafarig',
'pineco',
'forretress',
'dunsparce',
'gligar',
'steelix',
'snubbull',
'granbull',
'qwilfish',
'scizor',
'shuckle',
'heracross',
'sneasel',
'teddiursa',
'ursaring',
'slugma',
'magcargo',
'swinub',
'piloswine',
'corsola',
'remoraid',
'octillery',
'delibird',
'mantine',
'skarmory',
'houndour',
'houndoom',
'kingdra',
'phanpy',
'donphan',
'porygon2',
'stantler',
'smeargle',
'tyrogue',
'hitmontop',
'smoochum',
'elekid',
'magby',
'miltank',
'blissey',
'raikou',
'entei',
'suicune',
'larvitar',
'pupitar',
'tyranitar',
'lugia',
'ho-oh',
'celebi',
'treecko',
'grovyle',
'sceptile',
'torchic',
'combusken',
'blaziken',
'mudkip',
'marshtomp',
'swampert',
'poochyena',
'mightyena',
'zigzagoon',
'linoone',
'wurmple',
'silcoon',
'beautifly',
'cascoon',
'dustox',
'lotad',
'lombre',
'ludicolo',
'seedot',
'nuzleaf',
'shiftry',
'taillow',
'swellow',
'wingull',
'pelipper',
'ralts',
'kirlia',
'gardevoir',
'surskit',
'masquerain',
'shroomish',
'breloom',
'slakoth',
'vigoroth',
'slaking',
'nincada',
'ninjask',
'shedinja',
'whismur',
'loudred',
'exploud',
'makuhita',
'hariyama',
'azurill',
'nosepass',
'skitty',
'delcatty',
'sableye',
'mawile',
'aron',
'lairon',
'aggron',
'meditite',
'medicham',
'electrike',
'manectric',
'plusle',
'minun',
'volbeat',
'illumise',
'roselia',
'gulpin',
'swalot',
'carvanha',
'sharpedo',
'wailmer',
'wailord',
'numel',
'camerupt',
'torkoal',
'spoink',
'grumpig',
'spinda',
'trapinch',
'vibrava',
'flygon',
'cacnea',
'cacturne',
'swablu',
'altaria',
'zangoose',
'seviper',
'lunatone',
'solrock',
'barboach',
'whiscash',
'corphish',
'crawdaunt',
'baltoy',
'claydol',
'lileep',
'cradily',
'anorith',
'armaldo',
'feebas',
'milotic',
'castform',
'rainy castform',
'sunny castform',
'kecleon',
'shuppet',
'banette',
'duskull',
'dusclops',
'tropius',
'chimecho',
'absol',
'wynaut',
'snorunt',
'glalie',
'spheal',
'sealeo',
'walrein',
'clamperl',
'huntail',
'gorebyss',
'relicanth',
'luvdisc',
'bagon',
'shelgon',
'salamence',
'beldum',
'metang',
'metagross',
'regirock',
'regice',
'registeel',
'latias',
'latios',
'kyogre',
'groudon',
'rayquaza',
'jirachi',
'turtwig',
'grotle',
'torterra',
'chimchar',
'monferno',
'infernape',
'piplup',
'prinplup',
'empoleon',
'starly',
'staravia',
'staraptor',
'bibarel',
'kricketot',
'kricketune',
'shinx',
'luxio',
'luxray',
'budew',
'roserade',
'cranidos',
'rampardos',
'shieldon',
'bastiodon',
'burmy',
'wormadam',
'trash wormadam',
'sandy wormadam',
'mothim',
'combee',
'vespiquen',
'pachirisu',
'buizel',
'floatzel',
'cherubi',
'cherrim',
'shellos',
'gastrodon',
'ambipom',
'drifloon',
'drifblim',
'buneary',
'lopunny',
'mismagius',
'honchkrow',
'glameow',
'purugly',
'chingling',
'stunky',
'skuntank',
'bronzor',
'bronzong',
'bonsly',
'mime jr.',
'happiny',
'chatot',
'spiritomb',
'gible',
'gabite',
'garchomp',
'munchlax',
'riolu',
'lucario',
'hippopotas',
'hippowdon',
'skorupi',
'drapion',
'croagunk',
'toxicroak',
'carnivine',
'finneon',
'lumineon',
'mantyke',
'snover',
'abomasnow',
'weavile',
'magnezone',
'lickilicky',
'rhyperior',
'tangrowth',
'electivire',
'magmortar',
'togekiss',
'yanmega',
'leafeon',
'glaceon',
'gliscor',
'mamoswine',
'porygon-z',
'gallade',
'probopass',
'dusknoir',
'froslass',
'rotom',
'uxie',
'mesprit',
'azelf',
'dialga',
'palkia',
'heatran',
'regigigas',
'giratina',
'cresselia',
'phione',
'manaphy',
'darkrai',
'shaymin',
'arceus',
'victini',
'snivy',
'servine',
'serperior',
'tepig',
'pignite',
'emboar',
'oshawott',
'dewott',
'samurott',
'patrat',
'watchog',
'lillipup',
'herdier',
'stoutland',
'purrloin',
'liepard',
'pansage',
'simisage',
'pansear',
'simisear',
'panpour',
'simipour',
'munna',
'musharna',
'pidove',
'tranquill',
'unfezant',
'blitzle',
'zebstrika',
'roggenrola',
'boldore',
'gigalith',
'woobat',
'swoobat',
'drilbur',
'excadrill',
'audino',
'timburr',
'gurdurr',
'conkeldurr',
'tympole',
'palpitoad',
'seismitoad',
'throh',
'sawk',
'sewaddle',
'swadloon',
'leavanny',
'venipede',
'whirlipede',
'scolipede',
'cottonee',
'whimsicott',
'petilil',
'lilligant',
'basculin',
'sandile',
'krokorok',
'krookodile',
'darumaka',
'darmanitan',
'alakazam-mega',
'maractus',
'dwebble',
'crustle',
'scraggy',
'scrafty',
'sigilyph',
'yamask',
'cofagrigus',
'tirtouga',
'carracosta',
'archen',
'archeops',
'trubbish',
'garbodor',
'zorua',
'zoroark',
'minccino',
'cinccino',
'gothita',
'gothorita',
'gothitelle',
'solosis',
'duosion',
'reuniclus',
'ducklett',
'swanna',
'vanillite',
'vanillish',
'vanilluxe',
'deerling',
'sawsbuck',
'emolga',
'karrablast',
'escavalier',
'foongus',
'amoonguss',
'frillish',
'jellicent',
'alomomola',
'joltik',
'galvantula',
'ferroseed',
'ferrothorn',
'klink',
'klang',
'klinklang',
'tynamo',
'eelektrik',
'eelektross',
'elgyem',
'beheeyem',
'litwick',
'lampent',
'chandelure',
'axew',
'fraxure',
'haxorus',
'cubchoo',
'beartic',
'cryogonal',
'shelmet',
'accelgor',
'stunfisk',
'mienfoo',
'mienshao',
'druddigon',
'golett',
'golurk',
'pawniard',
'bisharp',
'bouffalant',
'rufflet',
'braviary',
'vullaby',
'mandibuzz',
'heatmor',
'durant',
'deino',
'zweilous',
'hydreigon',
'larvesta',
'volcarona',
'cobalion',
'terrakion',
'virizion',
'tornadus',
'thundurus',
'reshiram',
'zekrom',
'landorus',
'kyurem',
'keldeo',
'mewtwo-megay',
'meloetta',
'genesect',
'chespin',
'quilladin',
'chesnaught',
'fennekin',
'braixen',
'delphox',
'froakie',
'frogadier',
'greninja',
'bunnelby',
'diggersby',
'fletchling',
'fletchinder',
'talonflame',
'scatterbug',
'spewpa',
'vivillon',
'litleo',
'pyroar',
'flabebe',
'floette',
'florges',
'skiddo',
'gogoat',
'pancham',
'pangoro',
'furfrou',
'espurr',
'meowstic',
'honedge',
'doublade',
'aegislash',
'spritzee',
'aromatisse',
'swirlix',
'slurpuff',
'inkay',
'malamar',
'binacle',
'barbaracle',
'skrelp',
'dragalge',
'clauncher',
'clawitzer',
'helioptile',
'heliolisk',
'tyrunt',
'tyrantrum',
'amaura',
'aurorus',
'sylveon',
'hawlucha',
'dedenne',
'carbink',
'goomy',
'sliggoo',
'goodra',
'klefki',
'phantump',
'trevenant',
'pumpkaboo',
'gourgeist',
'minior-core',
'bergmite',
'avalugg',
'noibat',
'noivern',
'xerneas',
'yveltal',
'zygarde',
'diancie',
'hoopa',
'hoopa unbound',
'volcanion',
'rowlet',
'dartrix',
'decidueye',
'litten',
'torracat',
'incineroar',
'popplio',
'brionne',
'primarina',
'pikipek',
'trumbeak',
'toucannon',
'yungoos',
'gumshoos',
'grubbin',
'charjabug',
'vikavolt',
'crabrawler',
'crabominable',
'oricorio',
'lycanroc-midnight',
'lycanroc-dusk',
'cutiefly',
'ribombee',
'rockruff',
'lycanroc',
'turtonator',
'wishiwashi',
'wishiwashi-school',
'mareanie',
'toxapex',
'mudbray',
'mudsdale',
'dewpider',
'araquanid',
'fomantis',
'lurantis',
'morelull',
'shiinotic',
'salandit',
'salazzle',
'stufful',
'bewear',
'bounsweet',
'steenee',
'tsareena',
'comfey',
'oranguru',
'passimian',
'wimpod',
'golisopod',
'sandygast',
'palossand',
'pyukumuku',
'type: null',
'silvally',
'minior',
'komala',
'togedemaru',
'mimikyu',
'bruxish',
'drampa',
'dhelmise',
'jangmo-o',
'hakamo-o',
'kommo-o',
'tapu koko',
'tapu lele',
'tapu bulu',
'tapu fini',
'cosmog',
'cosmoem',
'solgaleo',
'lunala',
'nihilego',
'buzzwole',
'pheromosa',
'xurkitree',
'celesteela',
'kartana',
'guzzlord',
'necrozma',
'zarude',
'magearna',
'marshadow',
'poipole',
'naganadel',
'stakataka',
'blacephalon',
'zeraora',
'meltan',
'melmetal',
'grookey',
'thwackey',
'rillaboom',
'scorbunny',
'raboot',
'cinderace',
'sobble',
'drizzile',
'inteleon',
'skwovet',
'greedent',
'rookidee',
'corvisquire',
'corviknight',
'blipbug',
'dottler',
'orbeetle',
'nickit',
'thievul',
'gossifleur',
'eldegoss',
'wooloo',
'dubwool',
'chewtle',
'drednaw',
'yamper',
'boltund',
'rolycoly',
'carkol',
'coalossal',
'applin',
'flapple',
'appletun',
'silicobra',
'sandaconda',
'cramorant',
'arrokuda',
'barraskewda',
'toxel',
'toxtricity',
'sizzlipede',
'centiskorch',
'clobbopus',
'grapploct',
'sinistea',
'polteageist',
'hatenna',
'hattrem',
'hatterene',
'impidimp',
'morgrem',
'grimmsnarl',
'obstagoon',
'perrserker',
'cursola',
'sirfetchd',
'mrrime',
'runerigus',
'milcery',
'alcremie',
'falinks',
'pincurchin',
'snom',
'frosmoth',
'stonjourner',
'eiscue',
'indeedee',
'morpeko',
'cufant',
'copperajah',
'dracozolt',
'arctozolt',
'dracovish',
'arctovish',
'duraludon',
'dreepy',
'drakloak',
'dragapult',
'zacian',
'zacian-crowned',
'zamazenta',
'zamazenta-crowned',
'eternatus',
'alolan dugtrio',
'alolan grimer',
'alolan muk',
'alolan geodude',
'alolan graveler',
'alolan golem',
'alolan rattata',
'alolan raticate',
'alolan raichu',
'alolan marowak',
'alolan meowth',
'alolan persian',
'alolan exeggutor',
'Alolan Vulpix',
'alolan ninetales',
'alolan sandshrew',
'alolan sandslash',
'pa\'u oricorio',
'sensu oricorio',
'pom-pom oricorio',
'shadow lugia',
'red-striped basculin',
'blue-striped basculin',
'zygarde',
'10% zygarde',
'complete zygarde',
'deoxys',
'defense deoxys',
'speed deoxys',
'attack deoxys',
'farfetch\'d',
'regieleki',
'snowy castform',
'regidrago',
'calyrex',
'urshifu',
'glastrier',
'galarian slowbro',
'galarian sandslash',
'galarian sandshrew',
'galarian ponyta',
'galarian rapidash',
'galarian zigzagoon',
'galarian linoone',
'galarian darmanitan',
'galarian darumaka',
'alolan ninetales',
'alolan vulpix',
]

def good(hint, match):
    for i in range(len(match)):
        if hint[i] == "_":
            continue
        if (hint[i] != match[i]):
            return False
    return True

def find(message, name, tempar):
    final = []
    for i in range (len(tempar)):
        if len(name) != len(tempar[i]):
            continue
        print(name + " " + tempar[i])
        if (good(name, tempar[i])):
            final.append(tempar[i])
    return final


client = discord.Client()

@client.event
async def on_ready():
    print('Main user activated: {0.user}'.format(client))

@client.event
async def on_message(message):
    channel = client.get_channel(ID)
    next_incense = False
    if (message.content.startswith('!start') and message.channel.id == ID):
        while True:
            msg = (await channel.history(limit=1).flatten())[0]
            hint = msg.content
            while not hint.startswith('The'):
                msg = (await channel.history(limit=1).flatten())[0]
                hint = msg.content
                st = str(msg.author)

                if msg.author == client.user:
                    await msg.delete()
                    continue
                    
                if hint.startswith("Whoa there"):
                    await msg.delete()
                    for i in range(1, 6):
                        chime.success()
                        time.sleep(1)
                    continue

                if st != "Pokétwo#8236":
                    continue
                
                if hint.startswith('That'):
                    await msg.delete()
                    continue

                if len(hint) > 0:
                    continue

                embed = msg.embeds[0].to_dict()
                footer = embed["footer"]['text'][35:][0]

                # print(footer)

                if footer == "0":
                    next_incense = True

                await channel.send("p!h")

                time.sleep(1)
                msg = (await channel.history(limit=1).flatten())[0]
                hint = msg.content
                st = str(msg.author)

            size = len(hint)
            name = hint[15:size - 1]
            name = name.replace("\_", "_")
            name = name.lower()
            name = name.replace("é", "e")
            if name.count('\u2642') > 0:
                name = name.replace("\u2642", " ")
                name = name[:-1]
            if name.count('\u2640') > 0:
                name = name.replace("\u2640", " ")
                name = name[:-1]
            # name = name.replace("\u2642", " ")
            # name = name.replace("\u2640", " ")
            hlen = len(name)
            await channel.send(hlen)
            await channel.send('finding...')
            await channel.send(name)
                #############################
            final = find(message, name, list_pkms)
                # if terminate:
                #     continue
            await channel.send(len(final))
            for i in range (len(final)):
                await channel.send("p!c " + final[i])
            if next_incense:
                time.sleep(1.5)
                await channel.send("p!buy incense")
                next_incense = False
    if (message.content.startswith('!stop') and message.channel.id == ID):
        exit(0)

client.run("##################################", bot=False)
