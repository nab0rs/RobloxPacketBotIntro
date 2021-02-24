import requests, random

cookie = ""
gameid = 6395046576


for x in range(1):
    with requests.session() as session:
        try:
            br = random.randint(10000, 100000)
            session.cookies['.ROBLOSECURITY'] = cookie
            s = session.post(f'https://assetgame.roblox.com/game/PlaceLauncher.ashx?request=RequestGame&browserTrackerId={br}&placeId={gameid}&isPlayTogetherGame=false', headers={'User-Agent':'Roblox\Winlet'})
            req = session.post(s.json()['joinScriptUrl'])
            print(req.text)
        except:
            pass

input()
