# -------------------------------------------------------------------
# Furuikeya Settings
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Basic Informations
version: 'Furuikeya 0.1'
description: 'Furuikeya is a procedural protocol designed to create haikus from Twitter.'
strings: 'config/strings_en.yml'
arguments: 
- [ ['-k', '--kigo'], {'help' : 'the kigo of the haiku to generate'} ]
- [ ['-n', '--number'], {'type' : 'int', 'help' : 'haikus to generate', 'default': '1'} ]
- [ ['-s', '--saijiki'], {'action' : 'store_true'} ]

# Generic Settings
settings:
    twitter:
        consumer_key: 'YOUR_CONSUMER_KEY'
        consumer_secret: 'YOUR_CONSUMER_SECRET'
        oauth_token: 'YOUR_OAUTH_TOKEN'
        oauth_secret: 'YOUR_OAUTH_SECRET'
    saijiki: 'config/saijiki.txt'
    sonorities: 'config/sonority.txt'
    nltk_data: 'config/'
    pickle: 'english.pickle'
