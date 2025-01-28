import csv 
import random 
import string

def llegir_dades_csv(nom_arxiu):
    estudiants =[]
    with open (nom_arxiu, mode='r', encoding='utf-8') as fitxer:
        lector = csv.DictReader(fitxer)       
        for fila in lector:
            estudiants.append(fila)
    return estudiants

def generar_mail(nom,cognoms):
    email = f"{nom}.{cognoms}@insgabrielamistral.cat".lower().replace(" ","")
    return(email)

def generar_contrasenya():
    caracters = string.ascii_letters + string.digits + string.punctuation
    contrasenya= "".join(random.choice(caracters) for _ in range(1,11))
    return(contrasenya)
    
# Funció 
def escriure_csv(estudiants, nom_arxiu): 
    with open(nom_arxiu, mode='w', newline='', encoding='utf-8') as fitxer:
        camps = list(estudiants[0].keys()) + ['email', 'contrasenya']
        escriptor = csv.DictWriter(fitxer, fieldnames=camps)
        escriptor.writeheader()
        for estudiant in estudiants: 
            estudiant['email'] = generar_mail(estudiant['nom'], estudiant['cognoms'])
            estudiant['contrasenya'] = generar_contrasenya()
            escriptor.writerow(estudiant)
        
#nom del programa dels estudiants
nom_arxiu_entrada = "estudiants_nous.csv"
estudiants = llegir_dades_csv(nom_arxiu_entrada)
for estudiant in estudiants:
    estudiant["email"] = generar_mail(estudiant["nom"], estudiant["cognoms"])
    estudiant["contrasenya"]= generar_contrasenya
    
print(estudiants)

nom_arxiu_sortida = "estudiants_alta.csv"
escriure_csv(estudiants, nom_arxiu_sortida)

print(estudiants)