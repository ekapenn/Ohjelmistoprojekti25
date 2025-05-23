#Sallitut arvot
sallit_tavoite= ["laihduttaa", "lisätä massaa", "pitää kunnon kunnossa"]
sallit_taso= ["aloittelija", "keski", "edistynyt"]
sallit_mieltymys= ["cardio", "voimaharjoittelu", "venyttely"]

#Kysytään käyttäjän nimen
nimi = input("Mikä sinun nimesi?: ")
#alkutervehdys
print(f"Hei,{nimi}!\nValtsee mikä treeniohjelma sinulle sopii\nja paljonko täytyy juoda sinulle vettä.")

#ekakysymys ja tavoite, ja muuntaa vastauksen pieniksi kirjaimiksi 
while True:
    tavoite = input("\nMikä sinun tavoite?\nlaihduttaa / lisätä massaa  / pitää kunnon kunnossa: ").lower()
    if tavoite in sallit_tavoite: #syötteen tarkistaminen
        break
    print("Tarkista syöttö: vain annetuista vaihtoehdoista") #virheilmoitus

#tokakysymys-taso
while True:
    taso = input("Mikä taso sinulla juuri nyt?\naloittelija / keski / edistynyt: ").lower()
    if taso in sallit_taso: #syötteen tarkistaminen
        break
    print("Tarkista syöttö: vain annetuista vaihtoehdoista") #virheilmoitus
#kolmaskysymys-mieltymys
while True:
    mieltymys= input("Mitä eniten tykkäät\ncardio / voimaharjoittelu / venyttely: ").lower()
    if mieltymys in sallit_mieltymys: #syötteen tarkistaminen
        break
    print("Tarkista syöttö: vain annetuista vaihtoehdoista") #virheilmoitus

#neljäskysymys-paino
while True:
    try:
        paino = float(input("Mikä on sinun paino?: "))
        if paino <= 0: #tarkastetaan, että paino on suurempi kuin nolla
            print("Paino piti olla myönteinen luku. Syötä uudelleen.")
            continue
        elif paino > 200: #luku ei voi olla isompi kuin 200 muuten on se virhellinen 
            continue
        break
    except ValueError:
        print("Syötä luku. Esim, 70.")# jos vastaus on väärä, nätetään tämä viesti

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
    suositus = "Treenit, 3-4 kertaa viikossa"

#Lasketaan, kuinka paljon vettä tarvitaan
vesi= paino * 0.03 #perusjuoman juomiseen, 30 ml 1kg painoa kohti = 0,03 litraa/kg.
trenivesi= 0.5 if tavoite in ["laihduttaa", "lisätä massaa" ] else 0.0 #jos tavoite on aktiivinen lisätään vielä 0,5 litraa liikuntaa varten.
yleisvesi = vesi + trenivesi #vesimäärä yhteensä

#tulos
print("\n" + "=" * 57) #kehyksen yläreuna
print("{:^57}".format ("TULOS")) #Tämä tulostaa keskelle sanan
print(f"Nimi: {nimi}")
print(f"Taso: {taso}")
print(f"Treeniohjelma: {suositus}") #lopullinen suositus
print(f"Suositellaan juoda vettä: {yleisvesi:.2f}l/päivä")
print("\n" + "=" * 57) #kehyksen alareuna
