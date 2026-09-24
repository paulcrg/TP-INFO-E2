def head_tail(choix,nombre,chemin):
    if choix == 'head':
        n = 0
    elif choix == 'tail':
        n = -1
    else:
        raise ValueError
    if nombre < 0:
        raise ValueError
    try:
        with open(chemin,'r+',encoding = 'utf8') as fichier:
            for i in range(nombre):
                if n == 0:
                    fichier.readline()
                elif n ==-1:
                    fichier.readline(-1)
    except:
        return -1

print(head_tail('head',15,'dic.txt'))






if __name__ == 'main':
    head_tail(head,15,'dic.txt')