import subprocess
import os
class mqtt:
    temperatura=0
    listaTemp=[]
    tempOra=0
    tempMin=0
    def __init__(self):
        self.temperatura=0
    def connect_and_take(self):
        self.temperatura=os.system("mosquitto_sub -h \"broker.shiftr.io\" -u \"calvino00\" -P \"0123456789\" -t calvino-08/temperatura")
        #Aggiunta a liste
        self.listaTemp.append(self.temperatura)
    def ultimaOra(self):
        self.tempOra=0
        for i in range(1,721):
            self.tempOra=self.listaTemp[-i]+self.tempOra
        self.tempOra=self.tempOra/720
        return self.tempOra
    def ultimoMinuto(self):
        self.tempMin=0
        for i in range(1,13):
            self.tempMin=self.listaTemp[-i]+self.tempMin
        self.tempMin=self.tempMin/12
        return self.tempMin
    def ultimiDieciMin(self):
        self.tempDieci=0
        for i in range(1,121):
            self.tempDieci=self.listaTemp[-i]+self.tempDieci
        self.tempDieci=self.tempDieci/120
        return self.tempDieci



