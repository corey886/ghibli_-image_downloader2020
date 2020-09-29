import wget


def doww(urlaa):
    filename = wget.download(urlaa)


if __name__ == '__main__':

    rame = []
    '''rame.append('chihiro')
    rame.append('ged')
    rame.append('ponyo')
    rame.append('karigurashi')
    rame.append('kokurikozaka')
    rame.append('kazetachinu')
    rame.append('kaguyahime')'''
    rame.append('marnie')

    for ee in rame:
        for rr in range(1, 51):
            cc = str(rr)
            # print(cc.zfill(3))
            doww('http://www.ghibli.jp/gallery/'+ee+cc.zfill(3)+'.jpg')
