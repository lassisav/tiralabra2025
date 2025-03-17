def gift_wrapping(pisteet):
    # Jos alle 4 pistettä, palauta kaikki pisteet.
    if len(pisteet) < 4:
        return pisteet

    # Etsitään vasemmanpuoleisin piste, tasatilanteessa ylin.
    vasen = vasemman_etsinta(pisteet)
    
    # Haetaan lista verhon indekseistä
    verho = toistoalgoritmi(pisteet, vasen)

    # Luodaan lista verhon pisteistä palautettavaksi.
    palautus = []
    for i in range(len(verho)): # pylint: disable=consider-using-enumerate
        palautus.append(pisteet[verho[i]])
    
    return palautus

def toistoalgoritmi(pisteet, vasen):
    # Luodaan tyhjä palautuslista
    palautus = []
    
    # Tehdään vasemmanpuoleisimmasta pisteestä ensimmäinen lähtöpiste
    lahto = vasen

    # Loopataan kunnes verho on löydetty
    while(True):
        
        # Lisätään tunnettu lähtöpiste palautuslistaan
        palautus.append(lahto)

        # Etsitään maalipiste, jossa kolmen pisteen (lähtö, keski, maali) kulma kääntyy vastapäivään kaikilla keskipisteillä.
        # Jos löytyy keskipiste, jolle ym. ei päde, tehdään siitä maalipiste, ja jatketaan iteraatiota. Iteroinnin lopussa olevan maalipisteen on oltava verhon seuraava piste.
        maali = (lahto + 1) % len(pisteet) # Aloitetaan oletuksesta, että seuraava piste on listalla lähtöpisteestä seuraava.

        for i in range(len(pisteet)): # pylint: disable=consider-using-enumerate
            if(suunta(pisteet[lahto], pisteet[i], pisteet[maali]) == 2):
                maali = i

        # Maalipiste on nyt verhon seuraava vastapäiväinen piste lähtöpisteen jälkeen.
        # Tehdään maalipisteestä seuraava lähtöpiste.
        lahto = maali

        #Kun lähtöpisteeksi saadaan alkuperäinen lähtöpiste, on verho valmis.
        if (lahto == vasen):
            return palautus

def vasemman_etsinta(pisteet):
    vasen = 0
    for i in range(1, len(pisteet)):
        if pisteet[i][0] < pisteet[vasen][0]:
            vasen = i
        elif pisteet[i][0] == pisteet[vasen][0]:
            if pisteet[i][1] < pisteet[vasen][1]:
                vasen = i
    return vasen

def suunta(lahto, keski, maali):
    arvo = (keski[1] - lahto[1]) * (maali[0] - keski[0]) - (keski[0] - lahto[0]) * (maali[1] - keski[1])

    if arvo == 0:
        return 0 # Pisteet ovat kolineaariset
    elif arvo > 0:
        return 1 # Pisteet kulkevat myötäpäivään
    else:
        return 2 # Pisteet kulkevat vastapäivään