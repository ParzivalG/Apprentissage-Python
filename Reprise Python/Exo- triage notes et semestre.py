notes=[[12, 5,  11] ,
[18, 17, 16],
[-1, 9, -1],
[8, 12, 15],
[2, 4, 5],
[10, 10, 11],
[7, 7, 5],
[20, 20, 20],
[14, -1, -1],
[15, 18, 13],
[12, 11, -1],
[-1, 5, -1]]


def moyenne(trimestre):
    moyenne = 0
    trimestre -= 1
    nb_trimestre = (0,1,2)
    nb_eleve = 0
    for eleve in notes:
        nb_eleve += 1
        if trimestre in nb_trimestre:
            if eleve[trimestre] != -1:
                moyenne += eleve[trimestre]
        else:
            print('Bad information!')
    return (moyenne / nb_eleve)

print(moyenne(1))
