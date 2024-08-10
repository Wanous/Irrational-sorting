from math import log10,ceil
from random import randint 

# Codes de couleur ANSI
class colors:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"

class irrational_sorting:
    def __init__(self,master,list,file):

        self.master = master
        self.I_number = self.irrationnel(file)
        self.list = list
        self.interval = ceil(log10(len(self.list))) # ⌈ log10(n) ⌉
        self.Indice_I = 0
        self.iteration = 1
        self.number_range = 25
        self.decimals_counter = 0

    def irrationnel (self,file):
        '''Fonction to get the decimals of an irrational in a .bin file
            parameter : 
                file(str) : path of the file
        '''
        if file[len(file)-3:] == 'bin' :
            with open(file, 'rb') as fichier:
                I = fichier.read()
                I = I.hex()
            return I
        else :
            with open(file, 'r') as fichier:
                I = fichier.read()
            return I
                
    def liste_aleatoire(self,longueur,intervalle):
        liste=[]
        for n in range(longueur):
            liste.append(randint(intervalle[0],intervalle[1]))
        return liste

    def verification_tri(self):
        for e in range(len(self.list)):   
            for element in self.list[:e]: 
                if self.list[e]<element:  
                    return False      
        return True

    def sorting(self):

        i1 = self.Indice_I
        i2 = i1 + self.interval

        Indice_1 = int(self.I_number[i1 : i2])
        Indice_2 = int(self.I_number[i2 : i2 + self.interval])

            
        try :
            self.list[Indice_1],self.list[Indice_2]=self.list[Indice_2],self.list[Indice_1]
            print(colors.GREEN + f'iteration {self.iteration} : {self.list}' + colors.RESET,end=' ')
            self.master.draw_data(self.list, ["green" if x == Indice_1 or x == Indice_2 else "#b472e0" for x in range(len(self.list))])
            self.master.digits_label.config(fg="green") 
  
        except IndexError : 
            print(colors.RED + f'iteration {self.iteration} : {self.list}' + colors.RESET ,end=' ')
            self.master.digits_label.config(fg="black") 
            pass
        
        print(f'< {Indice_1} | {Indice_2} >')

        self.decimals_counter += self.interval*2
        self.master.decimals_counter['text'] = "Decimals used : " + str(self.decimals_counter)
  
        new_text = ''.join([f' {i}' for i in self.I_number[i1-self.number_range:i1]]) + f' < {Indice_1} | {Indice_2} >' + ''.join([f' {i}' for i in self.I_number[i2 + self.interval:i2 + self.interval + self.number_range]]) 
        self.master.digits_label['text'] = new_text
        self.Indice_I += self.interval*2
        self.iteration+=1





    

