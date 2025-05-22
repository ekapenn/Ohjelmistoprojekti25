sallit_tavoite= ["laihduttaa", "lisätä massaa", "pitää kunnon kunnossa"]
sallit_taso= ["aloittelija", "keski", "edistynyt"]
sallit_mieltymys= ["cardio", "voimaharjoittelu", "venyttely"]

#alkutervehdys
print("Hei!\nValtsee mikä treeniohjelma sinulle sopii\nja paljonko täytyy juoda sinulle vettä ")
#ekakysymys ja tavoite, ja muuntaa vastauksen pieniksi kirjaimiksi 
while True:
    tavoite = input("\nMikä sinun tavoite?\nlaihduttaa / lisätä massaa  / pitää kunnon kunnossa: ").lower()
    if tavoite in sallit_tavoite:
        break
    print("Tarkista syöttö: vain annetuista vaihtoehdoista")

#tokakysymys-taso
while True:
    taso = input("Mikä taso sinulla juuri nyt\naloittelija / keski / edistynyt: ").lower()
    if taso in sallit_taso:
        break
    print("Tarkista syöttö: vain annetuista vaihtoehdoista")
#kolmaskysymys-mieltymys
while True:
    mieltymys= input("Mitä eniten tykkäät\ncardio / voimaharjoittelu / venyttely: ").lower()
    if mieltymys in sallit_mieltymys:
        break
    print("Tarkista syöttö: vain annetuista vaihtoehdoista")

#kysymys mika paino ja jos vastaus on väärin sitten näytetään try ja expect käytäen
while True:
    try:
        paino = float(input("Mikä on sinun paino?: "))
        if paino <= 0:
            print("Paino piti olla myönteinen luku. Syötä uudelleen.")
            continue
        elif paino > 200: #luku ei voi olla isompi kuin 200 muuten on se virhellinen 
            continue
        break
    except ValueError:
        print("Syötä luku. Esim, 70.")

#treenin suositus
suositus= ""
#treenin suositus jos halutaan laihduttaa 
if tavoite == "laihduttaa" and  taso== "aloittelija" and mieltymys in["cardio", "voimaharjoittelu", "venyttely"]:
    suositus = "Treenit + 15min cardio, 2-5 kerta viikossa"
elif tavoite == "laihduttaa" and  taso== "keski" and mieltymys in["cardio", "voimaharjoittelu", "venyttely"]:
    suositus = "Treenit + 20min cardio, 2-4 kerta viikossa"
elif tavoite == "laihduttaa" and  taso== "edistynyt" and mieltymys in["cardio", "voimaharjoittelu", "venyttely"]:
    suositus = "Treenit + 30min cardio, 3-4 kerta viikossa"
#treenit suositus jos halutaan lisätä massaa   
if tavoite == "lisätä massaa" and  taso== "aloittelija" and mieltymys in["voimaharjoittelu", "venyttely"]:
    suositus = "Voimaharjoittelu, 2-4 kertaa viikossa"
elif tavoite == "lisätä massaa" and  taso== "keski" and mieltymys in["voimaharjoittelu", "venyttely"]:
    suositus = "Voimaharjoittelu, 3-4 kertaa viikossa"
elif tavoite == "lisätä massaa" and  taso== "edistynyt" and mieltymys in["cardio", "voimaharjoittelu", "venyttely"]:
    suositus = "Voimaharjoittelu, 3-4 kertaa viikossa"
#treenit suositus jos on edistynyt
if tavoite == "pitää kunnon kunnossa" and  taso== "aloittelija" and mieltymys in["cardio", "voimaharjoittelu", "venyttely"]:
    suositus = "Treenit + 20min cardio, 2-4 kerta viikossa"
elif tavoite == "pitää kunnon kunnossa" and  taso== "keski" and mieltymys in["cardio", "voimaharjoittelu", "venyttely"]:
    suositus = "Treenit + 30min cardio, 2-4 kerta viikossa"
elif tavoite == "pitää kunnon kunnossa" and  taso== "edistynyt" and mieltymys in["cardio", "voimaharjoittelu", "venyttely"]:
    suositus = "Voimaharjoittelu, 3-4 kertaa viikossa"

#lasketaan paljonko piti juoda vetta painon ja treenin mukaan. 
vesi= paino * 0.03
trenivesi= 0.5 if tavoite in ["laihduttaa", "lisätä massaa" ] else 0.0
yleisvesi = vesi + trenivesi

#vastaukset
print("\n" + "=" * 57)
print("{:^57}".format ("TULOS"))
print("\n")
print(f"Treeniohjelma: {suositus}")
print(f"Suositellaan juoda vettä: {yleisvesi:.2f}l/päivä")
print("\n" + "=" * 57)
