import pandas as pd 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 

daneFilmy=pd.read_csv("KolokwiumNr2/movie.csv")
#print(daneFilmy)
najrzadziej=daneFilmy.dtypes.value_counts().tail(1)
najrzadziej=najrzadziej.index.values


def get_statistical_params(daneFilmy,najrzadziej):
    daneFilmy=daneFilmy.select_dtypes(include=najrzadziej)
    print(daneFilmy.describe().T)
    print(type(daneFilmy))
    print(najrzadziej)


#get_statistical_params(daneFilmy,najrzadziej)

def sort_column(daneFilmy):
    print(daneFilmy.sort_index(ascending=True,axis = 1))

#sort_column(daneFilmy)


def get_last_n_sums(iloscWierszy, daneFilmy):
    wartosci_numeryczne=['float16', 'float32', 'float64','int16', 'int32', 'int64']
    wartosci =  daneFilmy.select_dtypes(include=wartosci_numeryczne).tail(iloscWierszy)
    wartosci = wartosci.sum()
    print(wartosci)


iloscWierszy = 12
#get_last_n_sums(iloscWierszy, daneFilmy)


def wykres(daneFilmy):
    x = 3 # Nazwisko Murawski
    y = 21*5 #Numer inexu 155082 
    z = 4 # Imie Sebastian
    rozmiar = daneFilmy['imdb_score'].count()
    ksztalt = 's'
    #print(rozmiar)
    kolor = np.random.randint(x,4*x,rozmiar)
    osX = daneFilmy['actor_1_facebook_likes']
    osY = daneFilmy['actor_2_facebook_likes']
    osZ = daneFilmy['actor_3_facebook_likes']
    #print(osX)
    #print(osY)
    #print(osZ)
    fig = plt.figure()
    ax = fig.gca( projection = '3d' )
    ax.scatter(osX,osY,osZ, label="Wykres", c=kolor,marker=ksztalt)
    ax.set_xlabel('actor_1_facebook_likes')
    ax.set_ylabel('actor_2_facebook_likes')
    ax.set_zlabel('actor_3_facebook_likes')
    sredniaOX= osX.mean()
    sredniaOY= osY.mean()
    sredniaOZ= osZ.mean()
    odchylenieOX= osX.std()
    odchylenieOY= osY.std()
    odchylenieOZ= osZ.std()
    #print(odchylenieOX)
    #print(odchylenieOY)
    #print(odchylenieOZ)
    ax.set_xlim(sredniaOX-odchylenieOX,sredniaOX+odchylenieOX)
    ax.set_ylim(sredniaOY-odchylenieOY,sredniaOY+odchylenieOY)
    ax.set_zlim(sredniaOZ-odchylenieOZ,sredniaOZ+odchylenieOZ)
    #print(sredniaOX)
    #print(sredniaOY)
    #print(sredniaOZ)
    plt.title("Wykres Aktorzy")
    plt.show()

wykres(daneFilmy)


