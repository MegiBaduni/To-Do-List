import json
from datetime import datetime

# Funksioni për ngarkim të detyrave nga një skedar
def ngarko_detyrat():
    try:
        with open('detyrat.json', 'r') as skedar:
            return json.load(skedar)
    except FileNotFoundError:
        return []

# Funksioni për ruajtjen e detyrave në një skedar
def ruaj_detyrat(detyrat):
    with open('detyrat.json', 'w') as skedar:
        json.dump(detyrat, skedar, indent=4)

# Funksioni për shtimin e një detyre
def shto_detyre(detyrat):
    emri_detyres = input("Vendos emrin e detyrës: ")
    data = input("Vendos datën (VVVV-MM-DD): ")
[]
    detyra_e_re = {
        'emri': emri_detyres,
        'data_vencimit': data_vencimit,
        'prioriteti': input("Vendos prioritetin (Lartë/Mesëm/Poshtë): "),
        'e_kryer': False
    }
    detyrat.append(detyra_e_re)
    print("Detyra u shtua me sukses!")

# Funksioni për shfaqjen e të gjitha detyrave
def shfaq_detyrat(detyrat):
    if not detyrat:
        print("Nuk u gjetën detyra.")
    else:
        print("\n------- Detyrat -------")
        for indeksi, detyra in enumerate(detyrat, start=1):
            gjendja = "E kryer" if detyra['e_kryer'] else "Jo e kryer"
            print(f"{indeksi}. {detyra['emri']} - Vencim: {detyra['data_vencimit']} - Prioritet: {detyra['prioriteti']} - Gjendja: {gjendja}")
        print("---------------------")

# Funksioni për shënimin e një detyre si e kryer
def kryej_detyren(detyrat):
    shfaq_detyrat(detyrat)
    if detyrat:
        try:
            indeksi_detyre = int(input("Vendosni numrin e detyrës për t'i shënuar si të kryer: ")) - 1
            detyrat[indeksi_detyre]['e_kryer'] = True
            print("Detyra u shënuar si e kryer!")
        except (ValueError, IndexError):
            print("Numër i pavlefshëm për detyrën.")

# Funksioni kryesor
def kryesor():
    detyrat = ngarko_detyrat()

    while True:
        print("\n===== Lista e Detyrave =====")
        print("1. Shto Detyrë")
        print("2. Shiko Detyrat")
        print("3. Shëno Detyrën si të Kryer")
        print("4. Dil")
        zgjedhja = input("Vendos zgjedhjen tënde: ")

        if zgjedhja == '1':
            shto_detyre(detyrat)
        elif zgjedhja == '2':
            shfaq_detyrat(detyrat)
        elif zgjedhja == '3':
            kryej_detyren(detyrat)
        elif zgjedhja == '4':
            ruaj_detyrat(detyrat)
            print("Mirupafshim!")
            break
        else:
            print("Zgjedhje e pavlefshme. Ju lutem vendosni një opsion të vlefshëm.")

if __name__ == "__main__":
    kryesor()
