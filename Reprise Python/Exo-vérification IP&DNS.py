#Le projet va consister a simuler un système informatique constitué de differents periphérique.

#Les différents périphérique pourront etre soit des ordinateurs, des serveurs ou des imprimantes.

#Chaque peripherique disposera d'une adresse IP ainsi que d'un DNS. Chaque peripherique pourra communiquer avec les autres peripheriques.

#Description des communications :
#- Tous peripherique peut demander l'adresse ip par le biai d'un DNS et inversement.
#- Tous peripherique peut demander le type d'un peripherique via une adresse ip ou un nom DNS ( savoir si c'est un pc, une imprimante ou un serveur)
#- Les ordinateurs peuvent envoyer des demandes d'impression a une imprimants
#- Les ordinateurs peuvent demander a recuperer des informations aux serveurs (du genre donne moi la liste des imprimantes sur le reseaux, les liste des pc sur le reseaux par exemple)



class Machine:
    def __init__(self, types, ipadd, domain):
        self.types = types
        self.ipadd = ipadd
        self.domain = domain

def comm(secure):
    if secure.domain == "Mondomaine":
        print ("Device on DNS!")
    else:
        print ("Device not on domain and can't communicate")

def commIP(masque1, masque2):
    if masque1.ipadd[:8] == masque2.ipadd[:8]:
        print ("IP @ communicate")
    else:
        print ("IP @ not on same network")


Computer1 = Machine("PC", "192.168.0.9", "Mondomaine")

Computer2 = Machine("PC", "192.168.0.10", "Autredomaine")


Serveur1 = Machine("Server", "192.168.1.2", "Mondomaine")

Serveur2 = Machine("server", "192.169.124.2", "Mondomaine")


Imp1 = Machine("Imprimante", "192.168.2.12", "Mondomaine")

Imp2 = Machine("Imprimante", "192.168.2.15", "Autredomaine")


print (comm(Computer1))
print (comm(Computer2))

print (commIP(Computer1,Imp2))
print (commIP(Computer1,Serveur2))
