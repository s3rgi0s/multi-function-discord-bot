import time
import os
#controlla o installa le dipendenze
os.system("pip install selenium")
os.system("pip install simple_colors")

import simple_colors
from sergio import *

nomeServer = input("inserisci lo username: ")             # implementala nella interfaccia
passwordServer = input("inserisci la password: ")         # implementala nella interfaccia
#marco gay
connessioneAlServer(driver, nomeServer, passwordServer)   # implementala nella interfaccia
accendiIlServer()                                         # implementala nella interfaccia
# esciDaAternos()                                         # implementala nella interfaccia
#marconano
#ciao