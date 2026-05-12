def are_you_playing_banjo(name):
    l = name.lower()
    x = (l.find("r"))
    if x ==-1:
        return name + " does not play banjo" 
    else :
        return name + "plays banjo"

