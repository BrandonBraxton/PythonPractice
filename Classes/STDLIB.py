from collections import OrderedDict

fav_lang = OrderedDict()

fav_lang['Opal'] = "NONE"
fav_lang['brandon'] = 'java'
fav_lang['scott'] = 'python'
fav_lang['dani'] = 'javascript'

for name, language in fav_lang.items():
    print(name.title() + "'s fave language is " + language.title())