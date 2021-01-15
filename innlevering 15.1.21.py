brett = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
#selvsigende
spillet_foregår = True
vinner = None

spiller = "X" #x starter fordi han er kulest, alle vet det. 0 gang = losers, fight me

def spill(): #funksjonen for selve spillet

  vis_brett() #må vise brettet, blir litt vanskelig uten, men kan fortsatt gå, nesten som magnus

  while spillet_foregår: #først kjører den en tur, deretter skjekker den om spillet er slutt, så bytter den spiller, hvis spillet foregår ikke er true slutter spillet
    en_tur(spiller)

    om_spillet_er_slutt()

    bytt_spiller()
  
  if vinner == "X" or vinner == "O": # skriver ut vinneren
    print(vinner + " vant.")
  elif vinner == None:
    print("Likt.")

def vis_brett(): #viser brettet, idk hva mere du vil ha meg til å si
  print("\n")
  print(brett[0] + " | " + brett[1] + " | " + brett[2] + "     1 | 2 | 3")
  print(brett[3] + " | " + brett[4] + " | " + brett[5] + "     4 | 5 | 6")
  print(brett[6] + " | " + brett[7] + " | " + brett[8] + "     7 | 8 | 9")
  print("\n")

def en_tur(player): # her kjører den en tur, ganske kult ngl

  print(player + " sin tur.")
  posisjon = input("Velg en posisjon fra 1-9: ")
  
#nå skjekker den om posisjonen er false eller ikke
  valid = False
  while not valid:

    while posisjon not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      posisjon = input("Velg en posisjon fra 1-9: ")

    posisjon = int(posisjon) - 1

    if brett[posisjon] == "-":
      valid = True
    else:
      print("har du øyne?")

  brett[posisjon] = player #skriver ned hvem som gjorde hva, you know

  vis_brett() #ekstremt kult hvis jeg kunne sagt det selv


def om_spillet_er_slutt():#hvis spillet er slutt vil en av dem slå ut
  sjekk_etter_vinner()
  likt()

def sjekk_etter_vinner():
  global vinner #globaliserer vinneren
#spilleren har vunnet på en av disse måtene
  rad_vinner = sjekk_rader()
  kolonne_vinner = sjekk_kolonner()
  diagonal_vinner = sjekk_diagonaler()
#finner vinneren og skriver den ned
  if rad_vinner:
    vinner = rad_vinner
    
  elif kolonne_vinner:
    vinner = kolonne_vinner
    
  elif diagonal_vinner:
    vinner = diagonal_vinner
#hvis det ikke er noen vinner  
  else:
    vinner = None

#nå skjekker vi alle tre mulige måtene en spiller kan vinne på, kunne slått dem sammen, men det hadde vært mye rot
def sjekk_rader():

  global spillet_foregår #nesten på vær eneste funksjon får jeg tak i spillet_foregår, fordi den stopper hele spillet hvis den er false
#alle disse er mulige kombinasjoner for at en spiller vant
  rad_1 = brett[0] == brett[1] == brett[2] != "-"
  rad_2 = brett[3] == brett[4] == brett[5] != "-"
  rad_3 = brett[6] == brett[7] == brett[8] != "-"

  if rad_1 or rad_2 or rad_3:
    spillet_foregår = False #stopper spillet

  if rad_1:#finner spilleren som vant
    return brett[0] 

  elif rad_2:
    return brett[3] 

  elif rad_3:
    return brett[6] 

  else:
    return None

#samme som ved rader, les kommentarene der
def sjekk_kolonner():
    
  global spillet_foregår
  
  kolonne_1 = brett[0] == brett[3] == brett[6] != "-"
  kolonne_2 = brett[1] == brett[4] == brett[7] != "-"
  kolonne_3 = brett[2] == brett[5] == brett[8] != "-"
      #waldo
  if kolonne_1 or kolonne_2 or kolonne_3:
    spillet_foregår = False
    
  if kolonne_1:
    return brett[0] 

  elif kolonne_2:
    return brett[1] 

  elif kolonne_3:
    return brett[2] 

  else:
    return None

#også samme som radder, les kommentarene der
def sjekk_diagonaler():

  global spillet_foregår

  diagonal_1 = brett[0] == brett[4] == brett[8] != "-"
  diagonal_2 = brett[2] == brett[4] == brett[6] != "-"
          #42 ;-)
  if diagonal_1 or diagonal_2:
    spillet_foregår = False

  if diagonal_1:
    return brett[0] 

  elif diagonal_2:
    return brett[2]

  else:
    return None

#Hvis det er likt setter man spillet_foregår til false så stopper hele spillet
def likt():

  global spillet_foregår

  if "-" not in brett:
    spillet_foregår = False
    return True

  else:
    return False

#for hver runde må man bytte spiller, da skjekker jeg om hvem spilleren er også bytter jeg
def bytt_spiller():

  global spiller

  if spiller == "X":
    spiller = "O"

  elif spiller == "O":
    spiller = "X"

#start spill
spill()
#6 material no cap