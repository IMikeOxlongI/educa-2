    #co potřbuji:
    #jednoduchý svět -  brno
    #lore - průběh života v brně
    #nepřátelé - lidé okolo
    #mechaniku - náhodně při tvém životě potkáváš divnolidi so žijí v brně
    # poš = poškození
    # HPP = Počet životů hráč
    # atack = útok
    # Prachy = peníze hráče
    # hp = životy protivníka (prostě toho NPC)
    # útok = útok portivníka
    # nal = nálada hráče
    # nemoc = postupně bude odebírat hráči zdaví
import random
import time
poš=10;HPP=100;Prachy=200;nal=45;nemoc=0
den = 1
print("Situace se má tak že jsi obyvatel brna a v této hře budeš zažívat dobrodružství spojené s tím.\nTvím cílem je přežít celí týden.")
jmeno=input("Jak ti mám říkat?")
print(f"\nTěšímě {jmeno}")
print("Já jsem pivson, ale můžeš mi říkat i pivečko\nBudu tě provádět touto hrou stvořenou Jiřím Pölzerem")
input(f"\nPokud by jsi chtěl {jmeno}? Chceš? ")
print("Ať si odpověděl cokoliv budu tě provízet")
print("Cílem je mýt co nejvíce od všeho, jako například životů,peněz a věcí atd.")
print("Princip ovládání je jednduchý.\nPro tbou vybraný tah budeš muset vypsat co bude u toho vypsané.\nJednoduché jako facka že?\nTak vzhůru do hry.\nVšech text který je v () jsou tvoje poznámky(Jsou jen pro tvojí informaci).\nDruhá postava o tom neví(říkáš si to sám pro sebe), nebo je to informace od pivečka.")
klacek = 15
Boxer = 20
BaseballPálka = 30
Teleskop =40

HraJede = True


Inventář = {
    "Žvíkačky": "Máš jen jednu😢",
    "Klacek": "poškození 12",
    
}

#volám žvíkačku tak,že => Inventář["Žvíkačky"]
def Bezďák(poš,HPP,nal,Prachy,nemoc):       #funkce na komunikaci s vezdomovcem
    penize = ""                                 #proměná pro přepočet kolik peněz dávám bezdomovci
    # print(hp=50)                              #nevím jestli využiji (do budoucna nejspíš ano)
    # print("()")
    # print(útok=30)
    #print("Zbaň - rezaví nůž, (možnost otravy)")
    odp=input("Dobrý den pane\n neměl by jte pro mě drobák?\nPro ano Y\nPro ne N")
    print("(Vypadá celkem dobře)")
    if odp == "Y":
        print("Ano něco by se našlo")
        sum=input("(Hmm kolik bych mu měl dát)\n(napiš ČÍSLO kolik mu chceš dát)")
        sum=int(sum)
        if sum > Prachy:
            print("Nelze nemáš tolik (Zadej menší částku, tolik kolik máš)")
            print(f"{Prachy} tolik mu můžeš maximálně dát!")
            sum=input("(Hmm kolik bych mu měl dát)\nnapiš číslo kolik mu chceš dát,tentokrák kolik mu můžeš dát prosím")
            penize == Prachy-sum
            Prachy == Prachy-sum
            print("Tu něco máte")
            print(f"dal jsi mu {Prachy} korun")
            if Prachy>150:
                print("Pane\nJeto pro mě hodně peněz.\nJestli by jste měl zájem.\nMohl bych vám udělat dobře\n...\nJestli chápete\n(Tato ance vám zvíší dobrou náladu)")
                roz=input("Měl by jste teda zájem?\nY porano\nN pro ne")
                if roz=="Y":
                    print("Dobře")
                    print("Ale nemůžeme tady")
                    print("(Odcházíš někam s hesky vypadajícím bezdomovcem a udělá ti dobrě)")
                    print("(Nálada zvíšena o 40)")
                    nal==nal+30
                else:
                    print("")
            else:
                print("")
        else:
            print("")
    else:
        print("Tak děkuji pane")        
    #hp = hp - atack
    # if hp < 5:
    #     print("Ty holomku")
    # else:
    #     print("")
    return(poš,HPP,nal,Prachy,nemoc)

def DealerZelenéhoListu(poš,HPP,nal,Prachy,nemoc):
    odp=input("Zdar.\nNemáš oheň?\nMám pro mám\nCokoliv jiného, pro nemám")
    if odp == "Mám":
        odp = input("Díky moc\nHele nechceš trávu?\n Fakt kvalitu, purple madgentu!\nSkvělej materíál toto.\n(Tato akce ti zlepší náladu)\nPro vyjádření zájmu napiš Y \na pokud nezájmu tak N")
        if odp == "Y":
            print("Dobře Dobře ...")
            time.sleep(2)
            print("Hele za gram to je 120")
            odp=input("Máš na to prachy?\nY pro ano\nN pro ne")
            if Prachy>120:
                print("")
            else:
                print("Nemůžu si to dovolit")
                if odp == "Y":
                    print("Super")
                    time.sleep(2)
                    print("Tu to máš")
           
        else:
            print("")  
    else:
        print("Tak nic no")
        print("(Dealer Zeleného Listu odchází a máš na nějakou dobu pokoj)")
    return(poš,HPP,nal,Prachy,nemoc)

def Katolik(poš,HPP,nal,Prachy,nemoc,Inventář):
    print("Pozdrav pánbůh")
    print("Mohu si s tebou na chvíli popovídat?")
    odp = input("Věříš v ježíše krysta\nY pro ano\nN pro ne\n")
    if odp == "N":
        print("Porč ne?")
        odp=input("Je to přece náš spasitel.\nY pro Něco na tom bude\nN pro A co já s tím\n")
        if odp=="Y":
            odp=input("Ano pane..\nNechěl by jste tady knížečku o bohu?\nY pro ano\nN pro ne\n")
            if odp=="Y":
                Inventář["Knížečka o bohu"] = "Zjímavá kniha o bohu"
            else:
                print("Škoda no.")
    print("Katolík odchází")
    return(poš,HPP,nal,Prachy,nemoc,Inventář)

def Zloděj(poš,HPP,nal,Prachy,nemoc,Inventář):
    print("Zloděj\nPoškození 10")
    print("Hej ty!\nDej mi svoje prníze")
    odp=input("Y pro Jo tady máš moje peníze(-200)\nN pro Nic ti nedám!")
    if odp=="Y":
        Prachy=Prachy-200
        print("No vidíš jak to jde jednoduše.")
    else:
        print("Tak z tebe ty peníze dostanu jinak.")
        print("Budeš se být se Zlodějem... toje jedíná zbraň je ovšem ale jen klacek s poškozením 12...")
        input("Opravu se mu nechceš vzdát a dát mu peníze?")

    return(poš,HPP,nal,Prachy,nemoc,Inventář)

def Milionář(nal,Prachy):
        print("(Potkal jis bohotáho muže co chce s tebou mluvit)")
        print("Dopbrý den pane\nMám pro vás nabídku\n když mi tady počkáte 5 min. s tímto kuvříkem tak vám dám 500 kč!")
        odp=input("Máte zájem?\nY pro ano\nN pro ne")
        if odp == "Y":
            print("Dobře tu to máte, za chvíli jsem tady...")
            time.sleep(120)
            print("Jak dlouho mu to ještě bude trvat😡")
            time.sleep(180)
            print("Jsem tady")
            print("Jelikož toto byl cosiální experiment tak tady máte 1000 kč")
            print("(máš radost)")
            Prachy=Prachy+1000
            nal=nal+20
        else:
            print("No nic no...\nTohle měl být sociální experimen kdo byy mi pomohl a kdo ne.\njelikož jste nepomohl tak jste ztratil možnost vyhrát 1000Kč!")
        return(nal,Prachy)
        
while (den<6):
    print(f"Den {den}")
    cis=random.randint(1,5)
    if cis == 1:
        Bezďák(poš,HPP,nal,Prachy,nemoc)
    elif cis==2:
        DealerZelenéhoListu(poš,HPP,nal,Prachy,nemoc)
    elif cis==3:
        Katolik(poš,HPP,nal,Prachy,nemoc,Inventář)
    elif cis==4:
        Zloděj(poš,HPP,nal,Prachy,nemoc,Inventář)
    else:
        Milionář(nal,Prachy)

      
      
        
    HraJede = False    
    den = den+1

print(f"Toto jsou tvoje staty jakým si prošel tuto hru.\nPeníze - {Prachy}\nzdraví - {HPP}%\nRozvíjejí cí se smrtelná nemoc - {nemoc}\nInventář . {Inventář}")
