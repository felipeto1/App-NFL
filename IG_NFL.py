# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 16:19:03 2015

@author: Felipe
"""

from Analise_NFL import VaiFazer,AgendasRivais,Vitorias,Agendas,Times,Standings2,PredS,nfc,afc,Afc,Nfc

import sys
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QDialog, QApplication, QPushButton, QLineEdit, QFormLayout

class PicButton(QAbstractButton):
    def __init__(self, pixmap, parent=None):
        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()
        
class Escolha(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Escolha, self).__init__(parent) # esse self tem que ter o nome da classe ali senão da bug
        self.func() #to chamando a outra funçao no init
        
    def func(self):
        spc=QtGui.QLabel('                  ') #label
        
        self.Afc=PicButton(QPixmap("logo-afc.png")) 
        self.Afc.resize(20,20)

        self.Nfc=PicButton(QPixmap("logo-nfc.png")) 
        self.Nfc.resize(20,20)
        
        self.letras=PicButton(QPixmap("Apresentação1.jpg")) 
        self.letras.resize(20,20)
        
        
        self.baltimore=PicButton(QPixmap("Baltimore_Ravens_helmet_rightface.png")) 
        self.baltimore.resize(20,20)
        self.connect(self.baltimore, SIGNAL("clicked()"),self.abre_baltimore)        
        
        self.cincinatti=PicButton(QPixmap("Cincinnati_Bengals_helmet_rightface.png")) 
        self.cincinatti.resize(20,20)
        self.connect(self.cincinatti, SIGNAL("clicked()"),self.abre_cincinatti)        
        
        self.cleveland=PicButton(QPixmap("Browns Helmet.png")) 
        self.cleveland.resize(20,20)
        self.connect(self.cleveland, SIGNAL("clicked()"),self.abre_cleveland)        

        self.pittsburgh=PicButton(QPixmap("Pittsburgh_Steelers_helmet_rightface.png")) 
        self.pittsburgh.resize(20,20)
        self.connect(self.pittsburgh, SIGNAL("clicked()"),self.abre_pittsburgh)        

        self.chicago=PicButton(QPixmap("Chicago Helmet.png")) 
        self.chicago.resize(20,20)
        self.connect(self.chicago, SIGNAL("clicked()"),self.abre_chicago)        

        self.detroit=PicButton(QPixmap("Detroit_Lions_Helmet.png")) 
        self.detroit.resize(20,20)
        self.connect(self.detroit, SIGNAL("clicked()"),self.abre_detroit)        

        self.greenbay=PicButton(QPixmap("Green Bay Packers Helmet - Copia.png")) 
        self.greenbay.resize(20,20)
        self.connect(self.greenbay, SIGNAL("clicked()"),self.abre_greenbay)        

        self.minnessota=PicButton(QPixmap("Minessota Helmet.png")) 
        self.minnessota.resize(20,20)
        self.connect(self.minnessota, SIGNAL("clicked()"),self.abre_minnessota)        

        self.houston=PicButton(QPixmap("Houston helmet.png")) 
        self.houston.resize(20,20)
        self.connect(self.houston, SIGNAL("clicked()"),self.abre_houston)        

        self.indianapolis=PicButton(QPixmap("Colts_helmet.png")) 
        self.indianapolis.resize(20,20)
        self.connect(self.indianapolis, SIGNAL("clicked()"),self.abre_indianapolis)        

        self.jacksonville=PicButton(QPixmap("JacksonvilleJaguars_HLQ0100a_2013_SCC_SRGB.png")) 
        self.jacksonville.resize(20,20)
        self.connect(self.jacksonville, SIGNAL("clicked()"),self.abre_jacksonville)        

        self.atlanta=PicButton(QPixmap("Atlanta_Falcons_helmet.png")) 
        self.atlanta.resize(20,20)
        self.connect(self.atlanta, SIGNAL("clicked()"),self.abre_atlanta)        

        self.carolina=PicButton(QPixmap("Panthers-Helmet.png")) 
        self.carolina.resize(20,20)
        self.connect(self.carolina, SIGNAL("clicked()"),self.abre_carolina)        

        self.tampabay=PicButton(QPixmap("bucs helmet.png")) 
        self.tampabay.resize(20,20)
        self.connect(self.tampabay, SIGNAL("clicked()"),self.abre_tampabay)        

        self.neworleans=PicButton(QPixmap("new-orleans-saints-helmet.png")) 
        self.neworleans.resize(20,20)
        self.connect(self.neworleans, SIGNAL("clicked()"),self.abre_neworleans)        

        self.tennessee=PicButton(QPixmap("Tennessee-titans-Helmet-logo.png")) 
        self.tennessee.resize(20,20)
        self.connect(self.tennessee, SIGNAL("clicked()"),self.abre_tennessee)        

        self.buffalo=PicButton(QPixmap("Buffalo_Bills_helmet_rightface.png")) 
        self.buffalo.resize(20,20)
        self.connect(self.buffalo, SIGNAL("clicked()"),self.abre_buffalo)        

        self.miami=PicButton(QPixmap("Miami Helmet.png")) 
        self.miami.resize(20,20)
        self.connect(self.miami, SIGNAL("clicked()"),self.abre_miami)        

        self.newengland=PicButton(QPixmap("New_England_Patriots_helmet_rightface.png")) 
        self.newengland.resize(20,20)
        self.connect(self.newengland, SIGNAL("clicked()"),self.abre_newengland)        

        self.jets=PicButton(QPixmap("New_York_Jets_helmet_rightface.png")) 
        self.jets.resize(20,20)
        self.connect(self.jets, SIGNAL("clicked()"),self.abre_jets)        

        self.dallas=PicButton(QPixmap("dallas-cowboys-helmet-logo.png")) 
        self.dallas.resize(20,20)
        self.connect(self.dallas, SIGNAL("clicked()"),self.abre_dallas)        

        self.giants=PicButton(QPixmap("New_York_Giants_helmet_rightface.png")) 
        self.giants.resize(20,20)
        self.connect(self.giants, SIGNAL("clicked()"),self.abre_giants)        

        self.philadelphia=PicButton(QPixmap("eagles helmet.png")) 
        self.philadelphia.resize(20,20)
        self.connect(self.philadelphia, SIGNAL("clicked()"),self.abre_philadelphia)        

        self.washington=PicButton(QPixmap("Washington_Redskins_helmet_rightface.png")) 
        self.washington.resize(20,20)
        self.connect(self.washington, SIGNAL("clicked()"),self.abre_washington)        

        self.denver=PicButton(QPixmap("Denver Broncos Helmet.png")) 
        self.denver.resize(20,20)
        self.connect(self.denver, SIGNAL("clicked()"),self.abre_denver)        

        self.kc=PicButton(QPixmap("Kansas_City_Chiefs_helmet.png")) 
        self.kc.resize(20,20)
        self.connect(self.kc, SIGNAL("clicked()"),self.abre_kc)        

        self.sd=PicButton(QPixmap("Chargers-Helmet.png")) 
        self.sd.resize(20,20)
        self.connect(self.sd, SIGNAL("clicked()"),self.abre_sd)        

        self.oakland=PicButton(QPixmap("OAKLAND-RAIDERS-HELMET-BUCS-STYLE1.png")) 
        self.oakland.resize(20,20)
        self.connect(self.oakland, SIGNAL("clicked()"),self.abre_oakland)        

        self.arizona=PicButton(QPixmap("Arizona_Cardinals_Helmet_rt_face.png")) 
        self.arizona.resize(20,20)
        self.connect(self.arizona, SIGNAL("clicked()"),self.abre_arizona)        

        self.seattle=PicButton(QPixmap("Seattle_Seahawks_helmet_rightface.png")) 
        self.seattle.resize(20,20)
        self.connect(self.seattle, SIGNAL("clicked()"),self.abre_seattle)        

        self.sf=PicButton(QPixmap("49ers-helmet.png")) 
        self.sf.resize(20,20)
        self.connect(self.sf, SIGNAL("clicked()"),self.abre_sf)        

        self.rams=PicButton(QPixmap("Rams_helmet.png")) 
        self.rams.resize(20,20)
        self.connect(self.rams, SIGNAL("clicked()"),self.abre_rams)        


        grid = QtGui.QGridLayout()
        grid.setSpacing(20)  
        
        
        grid.addWidget(self.letras,1, 3, 1, 3)        
        grid.addWidget(self.Afc, 2, 0) #colocando os itens no layout
        grid.addWidget(spc, 2, 1)
        grid.addWidget(spc, 2, 2)
        grid.addWidget(spc, 2, 3)
        grid.addWidget(spc, 2, 4)
        grid.addWidget(self.Nfc, 2, 5)
        grid.addWidget(spc, 2, 6)
        grid.addWidget(spc, 2, 7)
        grid.addWidget(spc, 2, 8)
        grid.addWidget(self.baltimore, 3, 0) #colocando os itens no layout
        grid.addWidget(self.cincinatti, 3, 1)
        grid.addWidget(self.cleveland, 3, 2)
        grid.addWidget(self.pittsburgh, 3, 3)
        grid.addWidget(spc, 3, 4)
        grid.addWidget(self.chicago, 3, 5)
        grid.addWidget(self.detroit, 3, 6)
        grid.addWidget(self.greenbay, 3, 7)
        grid.addWidget(self.minnessota, 3, 8)
        grid.addWidget(self.houston, 4, 0) #colocando os itens no layout
        grid.addWidget(self.indianapolis, 4, 1)
        grid.addWidget(self.jacksonville, 4, 2)
        grid.addWidget(self.tennessee, 4, 3)
        grid.addWidget(spc, 4, 4)
        grid.addWidget(self.atlanta, 4, 5)
        grid.addWidget(self.carolina, 4, 6)
        grid.addWidget(self.neworleans, 4, 7)
        grid.addWidget(self.tampabay, 4, 8)
        grid.addWidget(self.buffalo, 5, 0) #colocando os itens no layout
        grid.addWidget(self.miami, 5, 1)
        grid.addWidget(self.newengland, 5, 2)
        grid.addWidget(self.jets, 5, 3)
        grid.addWidget(spc, 5, 4)
        grid.addWidget(self.dallas, 5, 5)
        grid.addWidget(self.giants, 5, 6)
        grid.addWidget(self.philadelphia, 5, 7)
        grid.addWidget(self.washington, 5, 8)
        grid.addWidget(self.denver, 6, 0) #colocando os itens no layout
        grid.addWidget(self.kc, 6, 1)
        grid.addWidget(self.oakland, 6, 2)
        grid.addWidget(self.sd, 6, 3)
        grid.addWidget(spc, 6, 4)
        grid.addWidget(self.arizona, 6, 5)
        grid.addWidget(self.seattle, 6, 6)
        grid.addWidget(self.sf, 6, 7)
        grid.addWidget(self.rams, 6, 8)
        grid.addWidget(spc, 7, 4)

        self.setLayout(grid)
        
        self.setGeometry(0, 30, 350, 300)
        self.setWindowTitle('NFL - Find My Route')
        self.setWindowIcon(QtGui.QIcon('NFL logo.png'))
        self.showMaximized()
                
        self.show()
        
    def abre_baltimore(self):
        Meu_Time.escolha=0
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_cincinatti(self):
        Meu_Time.escolha=1
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_cleveland(self):
        Meu_Time.escolha=2
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_pittsburgh(self):
        Meu_Time.escolha=3
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_chicago(self):
        Meu_Time.escolha=4
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_detroit(self):
        Meu_Time.escolha=5
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_greenbay(self):
        Meu_Time.escolha=6
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_minnessota(self):
        Meu_Time.escolha=7
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_houston(self):
        Meu_Time.escolha=8
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_indianapolis(self):
        Meu_Time.escolha=9
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_jacksonville(self):
        Meu_Time.escolha=10
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_tennessee(self):
        Meu_Time.escolha=11
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_atlanta(self):
        Meu_Time.escolha=12
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
    
    def abre_carolina(self):
        Meu_Time.escolha=13
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_neworleans(self):
        Meu_Time.escolha=14
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_tampabay(self):
        Meu_Time.escolha=15
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_buffalo(self):
        Meu_Time.escolha=16
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_miami(self):
        Meu_Time.escolha=17
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_newengland(self):
        Meu_Time.escolha=18
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_jets(self):
        Meu_Time.escolha=19
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_dallas(self):
        Meu_Time.escolha=20
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_giants(self):
        Meu_Time.escolha=21
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_philadelphia(self):
        Meu_Time.escolha=22
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_washington(self):
        Meu_Time.escolha=23
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_denver(self):
        Meu_Time.escolha=24
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_kc(self):
        Meu_Time.escolha=25
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_oakland(self):
        Meu_Time.escolha=26
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_sd(self):
        Meu_Time.escolha=27
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_arizona(self):
        Meu_Time.escolha=28
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_seattle(self):
        Meu_Time.escolha=29
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_sf(self):
        Meu_Time.escolha=30
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    def abre_rams(self):
        Meu_Time.escolha=31
        variavel=Meu_Time() # atribuindo a classe a variavel "variavel"
        variavel.exec()
        
    
class Meu_Time(QtGui.QWidget):
    escolha=None    
    listatimes=[['Baltimore Ravens','Baltimore Wallpaper.jpg',270,100,'yellow'],['Cincinnati Bengals','Cincinatii Wallpaper.jpg',25,150,'black'],['Cleveland Browns','Cleveland Wallpaper.jpg',35,200,'black'],['Pittsburgh Steelers','Pittsburgh Wallpaper',59,240,'white'],['Chicago Bears','Chicago Wallpaper.jpg',240,100,'DarkOrange'],['Detroit Lions','Detroit Wallpaper.jpg',210,200,'white'],['Green Bay Packers','GB Wallpaper.jpg',120,150,'yellow'],['Minnesota Vikings','Minessota Wallpaper.jpg',280,190,'yellow'],['Houston Texans','Houston Wallpaper.jpg',255,150,'red'],['Indianapolis Colts','Indianapolis Wallpaper.jpg',230,125,'white'],['Jacksonville Jaguars','Jacksonville Wallpaper.jpg',190,150,'orange'],['Tennessee Titans','Tennessee Wallpaper.jpg',230,200,'red'],['Atlanta Falcons','Atlanta Wallpaper.jpg',0,100,'black'],['Carolina Panthers','Carolina Wallpaper.jpg',220,200,'black'],['New Orleans Saints','NO Wallpaper.jpg',45,100,'black'],['Tampa Bay Buccaneers','TB Wallpaper',0,200,'black'],['Buffalo Bills','Buffalo Wallpaper.jpg',230,150,'red'],['Miami Dolphins','Miami Wallpaper.jpg',200,200,'orange'],['New England Patriots','New England Wallpaper.jpg',240,70,'red'],['New York Jets','Jets Wallpaper.jpg',120,100,'white'],['Dallas Cowboys','Dallas Wallpaper.jpg',240,170,'black'],['New York Giants','Giants Wallpaper.jpg',240,200,'white'],['Philadelphia Eagles','Philadelphia Wallpaper.jpg',120,120,'white'],['Washington Redskins','Washington Wallpaper.jpg',0,150,'yellow'],['Denver Broncos','Denver Wallpaper.jpg',240,160,'orange'],['Kansas City Chiefs','KC Wallpaper',0,100,'black'],['Oakland Raiders','Oakland Wallpaper.jpg',240,0,'black'],['San Diego Chargers','SD Wallpaper.jpg',200,250,'yellow'],['Arizona Cardinals','Arizona Wallpaper.jpg',0,100,'black'],['Seattle Seahawks','Seattle Wallpaper.jpg',230,150,'black'],['San Francisco 49ers','SF Wallpaper.jpg',0,200,'black'],['St. Louis Rams','Rams Wallpaper.jpg',240,210,'beige']]
    minhalista=[]
    quebonito=None
    Nfc=[]
    Afc=[]
    Standings=[]
    Agendas=[]
    def __init__(self, parent=None):
        super(Meu_Time, self).__init__(parent) # esse self tem que ter o nome da classe ali senão da bug
        self.analiseNFL()        
        
        
    def func(self):
        
        
        self.time=PicButton(QPixmap(self.listatimes[self.escolha][1])) 
        self.time.resize(0,0) 
        
        self.rotulo=QtGui.QLabel(self.listatimes[self.escolha][0])
        self.rotulo.setStyleSheet('color: %s'%(self.listatimes[self.escolha][4]))
        font = QtGui.QFont("Courier", 40, QtGui.QFont.Bold)
        self.rotulo.setFont(font)
        
        for i in self.Standings:
            for k in i[1]:
                if k[0]==self.timeusuario[0]:
                    self.semana=int(k[1])+int(k[2])+int(k[3])
                    self.vitorias=QtGui.QLabel(k[1]+'-'+k[2]+'-'+k[3])
                    self.vitorias.setStyleSheet('color: %s'%(self.listatimes[self.escolha][4]))
                    font = QtGui.QFont("Courier", 30, QtGui.QFont.Bold)
                    self.vitorias.setFont(font)
        
        self.minhaagenda = QtGui.QPushButton('', self)
        self.minhaagenda.setToolTip('Clique para ver a Agenda do Seu Time')
        self.minhaagenda.resize(self.minhaagenda.sizeHint())
        self.connect(self.minhaagenda, SIGNAL("clicked()"),self.abreagenda)
        self.minhaagenda.setIcon(QIcon('Agenda.jpg'))
        self.minhaagenda.setIconSize(QtCore.QSize(180,80))
#        
        self.standings = QtGui.QPushButton('', self)
        self.standings.setToolTip('Clique para ver a Classificação do Seu Time')
        self.standings.resize(self.standings.sizeHint())
        self.connect(self.standings, SIGNAL("clicked()"),self.abrestandings)
        self.standings.setIcon(QIcon('Standings.jpg'))
        self.standings.setIconSize(QtCore.QSize(180,80))
        
        self.previsão = QtGui.QPushButton('', self)
        self.previsão.setToolTip('Clique para ver a Previsão do Seu Time')
        self.previsão.resize(self.previsão.sizeHint())
        self.connect(self.previsão, SIGNAL("clicked()"),self.abreprevisão)
        self.previsão.setIcon(QIcon('Previsões.jpg'))
        self.previsão.setIconSize(QtCore.QSize(180,80))
        
        self.playoffs = QtGui.QPushButton('', self)
        self.playoffs.setToolTip('Clique para ver os Playoffs')
        self.playoffs.resize(self.playoffs.sizeHint())
        if self.semana<16:
            self.playoffs.setIcon(QIcon('provisorios.jpg'))
            self.connect(self.playoffs, SIGNAL("clicked()"),self.abreplayoffs)
        if self.semana==16:
            self.playoffs.setIcon(QIcon('playoffs.jpg'))
            self.connect(self.playoffs, SIGNAL("clicked()"),self.abreplayoffs)
        self.playoffs.setIconSize(QtCore.QSize(180,80))     

        self.minhalista=self.listatimes[self.escolha]
        spc=QtGui.QLabel('          ') #label
        
        grid = QtGui.QGridLayout()
        grid.setSpacing(6)  
        
        grid.addWidget(self.time, 0, 0, 7, 3) #colocando os itens no layout
        grid.addWidget(spc, 0, 4)
        grid.addWidget(self.rotulo, 1, 5, 1, 7)
        grid.addWidget(spc, 3, 6)
        grid.addWidget(spc, 4, 4)
        grid.addWidget(self.minhaagenda, 4, 5)
        grid.addWidget(spc, 6, 4)
        grid.addWidget(self.standings, 4, 6)
        grid.addWidget(spc, 7, 4)
        grid.addWidget(self.previsão, 5, 5)
        grid.addWidget(self.playoffs, 5, 6)
        grid.addWidget(self.vitorias, 2, 6)
            
        self.setLayout(grid)

        self.setGeometry(100, 150, 350, 300)
        self.setWindowTitle('NFL - Find My Route - '+self.listatimes[self.escolha][0])
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 400)
        if self.listatimes[self.escolha][0]!='Oakland Raiders': 
            gradient.setColorAt(0.0, QColor.fromHsv(self.listatimes[self.escolha][2], 255, self.listatimes[self.escolha][3]))
            gradient.setColorAt(1.0, QColor.fromHsv(self.listatimes[self.escolha][2], 220, 60))     
        if self.listatimes[self.escolha][0]=='Oakland Raiders': 
            gradient.setColorAt(0.0, QColor.fromHsv(self.listatimes[self.escolha][2], 10, 180))
            gradient.setColorAt(1.0, QColor.fromHsv(self.listatimes[self.escolha][2], 10, 120))
    
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)
        self.show()
        
    def abreagenda(self):
        Ag=escolheAgenda()
        Ag.exec()
        
    def abrestandings(self):
        self.timeusuario=[self.listatimes[self.escolha][0]]
        St=escolheStandings()
        Standings.timeusuario=self.timeusuario
        St.exec()
        
    def abreprevisão(self):
        Pr=Prev()
        Pr.exec()
        
    def abreplayoffs(self):
        Pr=Prev()
        Pr.exec()
        
    def analiseNFL(self):
        versus=[]
        self.timeusuario=[self.listatimes[self.escolha][0]]
        Standings.timeusuario=self.timeusuario
        escolheStandings.timeusuario=self.timeusuario
        escolheAgenda.timeusuario=self.timeusuario
        Agenda.timeusuario=self.timeusuario
        divisaoStandings.timeusuario=self.timeusuario
        for i in Agendas:
            if i[0]==self.timeusuario:
                for k in i:
                    if k!=i[0] and k!=i[2]: # análise do time
                        versus.append(k) # salva os times que irão enfrentar o time escolhido nessa lista
        meutime=[]
        for i in Times:
            if self.timeusuario[0]==i[0][0]: #salva as informações importantes do time escolhido
                meutime.append([i[0][2],i[0][3],i[0][6],i[1][0]])
                
        for i in Standings2:
            if i[0]==[meutime[0][0],meutime[0][1]]:
                for k in i[1]:
                    if k[0]==self.timeusuario[0]:
                        meutime.append([int(k[1]),int(k[2]),int(k[3])])
        for i in PredS:
            if i[0]==[meutime[0][0],meutime[0][1]]:
                for k in i[1]:
                    if k[0]==self.timeusuario[0]:
                        meutime.append([int(k[1]),int(k[2]),int(k[3])])                
                        
        passei=0
        wildcard=0
        if meutime[0][0]=="NFC":
            for i in nfc:
                if i == nfc[0]:
                    for k in i:
                        if k[0]==self.timeusuario[0]:
                            passei=1
                if i == nfc[1]:
                    for l in i:
                        if l==i[0] or l==i[0]:
                            if l[0]==self.timeusuario[0]:
                                wildcard=1
        if meutime[0][0]=="AFC":
            for i in afc:
                if i == afc[0]:
                    for k in i:
                        if k[0]==self.timeusuario[0]:
                            passei=1
                if i == afc[1]:
                    for l in i:
                        if l==i[0] or l==i[0]:
                            if l[0]==self.timeusuario[0]:
                                wildcard=1  
                        
        listpassei=[]
        if passei==1:
            for i in Standings2:
                if i[0]==[meutime[0][0],meutime[0][1]]:
                    for k in i[1]:
                        if k[0]!=self.timeusuario[0]:
                            listpassei.append(k[0])
            AmeaçasDiv=[]
            numerinhos=[]
            for i in VaiFazer:
                for k in listpassei:
                    kleine=[]
                    if i[0]==k:
                        kleine.append(k)
                        kleine.append(-meutime[1][0]+i[1]+1)
                        AmeaçasDiv.append(kleine)
                        numerinhos.append(-meutime[1][0]+i[1]+1)
            quantasvit=max(numerinhos)
            jafui=0
            for ç in AmeaçasDiv:
                if (ç[1]==max(numerinhos) and jafui==0):
                    jafui+=1
                    MinhaMaiorAmeaça=ç[0]
        
        listnempasseidiv=[]
        listnempasseiconf=[]
        if passei==0:
            for i in Standings2:
                if i[0]==[meutime[0][0],meutime[0][1]]:
                    for k in i[1]:
                        if k[0]!=self.timeusuario[0]:
                            listnempasseidiv.append(k[0])
            if meutime[0][0]=='NFC':
                for i in nfc[1]:
                    listnempasseiconf.append(i[0])
            if meutime[0][0]=='AFC':
                for i in afc[1]:
                    listnempasseiconf.append(i[0])
                    
            AmeaçasDiv=[]
            AmeaçasConf=[]
            numerinhosdiv=[]
            numerinhosconf=[]
            for i in VaiFazer:
                for k in listnempasseidiv:
                    kleine=[]
                    if i[0]==k:
                        kleine.append(k)
                        kleine.append(-meutime[1][0]+i[1]+1)
                        AmeaçasDiv.append(kleine)
                        numerinhosdiv.append(-meutime[1][0]+i[1]+1)
            for i in VaiFazer:
                for k in listnempasseiconf:
                    kleine=[]
                    if i[0]==k:
                        kleine.append(k)
                        kleine.append(-meutime[1][0]+i[1]+1)
                        AmeaçasConf.append(kleine)
                        numerinhosconf.append(-meutime[1][0]+i[1]+1)
            #print(max(numerinhosdiv))
            if max(numerinhosdiv)<=max(numerinhosconf):
                quantasvit=max(numerinhosdiv)
                jafui=0
                for ç in AmeaçasDiv:
                    #print(ç[1])
                    if (ç[1]==max(numerinhosdiv) and jafui==0):
                        jafui+=1
                        MinhaMaiorAmeaça=ç[0]
                        
                    
            if max(numerinhosdiv)>max(numerinhosconf):
                quantasvit=max(numerinhosconf)
                jafui=0
                for ç in AmeaçasConf:
                    if (ç[1]==max(numerinhosconf) and jafui==0):
                        jafui+=1
                        MinhaMaiorAmeaça=ç[0]
                        
        tudo=[]              
        for i in versus[0]: #analisa a agend do time e cria uma lista com as informaçoes importantes de cada time q o time escolhido enfrentará
            lista=[]
            if '@' in i:
                po=i.split("@")
                for l in Times:
                    if po[1]==l[0][1]:
                        lista.append(l)
                        lista.append('@')
            else:
                for j in Times:
                    if i==j[0][1]:
                        lista.append(j)
            tudo.append([lista,int(0)])
        if len(tudo)==18:
            tudo.pop()
        for i in tudo:
            for k in Vitorias:
                if len(i[0])!=0:
                    if k[0]==self.timeusuario[0]:
                        for g in k:
                            if g == k[1]:
                                for b in range(len(g)):
                                    #print(k[0],g[b])
                                    if (g[b]=="W" and len(tudo[b])==2):
                                        tudo[b].append("W")
                                    if (g[b]=="L" and len(tudo[b])==2):
                                        tudo[b].append("L")
                                    if (g[b]=="T" and len(tudo[b])==2):
                                        tudo[b].append("T")
                                
                            
        for i in tudo: #sistema de pontuação
            if len(i[0])==2: 
                i[1]+=int(i[0][0][1][0]) # jogos fora de casa, somam pontuação
            if len(i[0])==1:
                i[1]-=int(meutime[0][3]) #jogos em casa subtrai pontuação
            if len(i[0])!=0:
             #   if i[0][0][0][2]==meutime[0][0]: #se for da mesma conferencia/
              #      i[1]-=2
               # if (i[0][0][0][3]==meutime[0][1] and i[0][0][0][2]==meutime[0][0]):
                #    i[1]-=5 # se for da mesma divisão
                dist=int(meutime[0][2])-int(i[0][0][0][6])
                i[1]+=dist # difereças de rankiamento
                               
        analise=[]            
        for i in tudo:
            if len(i[0])!=0:
                if len(i[0])==2:
                    analise.append([i[0][0][0][0],i[1],len(i)])
                else:
                    analise.append([i[0][0][0][0],i[1],len(i)])
                    #quantas vitórias são necessárias para ir para os playoffs
        if quantasvit<0:
            quantasvit=0
            
        numeros=[]
        wins=[]
        for i in analise:
            numeros.append(i[1])
        while len(numeros)>0:
            for k in analise:
                if float(k[1])==min(numeros):
                    wins.append(k)
                    #print(k)
                    numeros.remove(float(k[1]))
                    analise.remove(k)
                    break
            
        predição=[]
        predição=wins
        conta=0
        for k in wins:
            if conta<quantasvit:
                if len(k[0])!=0:
                    if (k[2]!=3): 
                        k.append("W")    
                        conta+=1
            
        for i in range(len(wins)):
            if (wins[i][2]==2 and len(wins[i])!=4):
                wins[i].append("L")
        
                                    
        for i in tudo:
            if len(i[0])!=0:
                if len(i[0])==2:
                    for k in wins:
                        if (k[1]==i[1] and k[0]==i[0][0][0][0]):
                            k[0]="@"+k[0]
                      
        for i in wins:
            if len(i)==3:
                for k in tudo:
                    if len(k)==3:
                        if k[0][0][0][0]==i[0]:
                            i.append(k[2])
                        if k[0][0][0][0]!=i[0]:
                            if i[0]=="@"+k[0][0][0][0]:
                                i.append(k[2])
        umalista=[]
        for i in tudo:
            momo=[]
            lololo=None
            if len(i[0])!=0:
                if len(i[0])==2:
                    lololo="@"+i[0][0][0][0]
                if len(i[0])==1:
                    lololo=i[0][0][0][0]
                #if len(i)==2:    
                momo.append([lololo])
                #if len(i)==3:    
                    #momo.append([lololo,i[2]])
            else:
                momo.append("BYE WEEK")
            umalista.append(momo)
                
        for i in range(len(umalista)):
            for k in wins:
                if umalista[i][0][0]==k[0]:
                    umalista[i].append(k[3])
           
        quebonito=[]         
        for i in umalista:
            if len(i)==2:
                quebonito.append([i[0][0],i[1]]) #AQUI TÃO AS W E L
            else:
                quebonito.append("BYE WEEK")
                
        self.Standings=Standings2        
        self.Afc=Afc       
        self.Nfc=Nfc
        self.quebonito=quebonito
        self.Agendas=AgendasRivais
        self.MinhaMaiorAmeaça=MinhaMaiorAmeaça
        for i in quebonito:
            print(i)
        self.func() #to chamando a outra funçao no init
        
class escolheAgenda(QtGui.QWidget):
    timeusuario=None
    def __init__(self, parent=None):
        super(escolheAgenda, self).__init__(parent) # esse self tem que ter o nome da classe ali senão da bug
        self.ag()
    def ag(self):
        
        self.meutime = QtGui.QPushButton('', self)
        self.meutime.setToolTip('Clique para ver a agenda do Seu Time')
        self.connect(self.meutime, SIGNAL("clicked()"),self.abremeutime)
        self.meutime.setIcon(QIcon('minhaagenda.jpg'))
        self.meutime.setIconSize(QtCore.QSize(150,50))  
        
        self.afcn = QtGui.QPushButton('', self)
        self.afcn.setToolTip('Clique para ver a agenda da AFC North')
        self.connect(self.afcn, SIGNAL("clicked()"),self.abreafcn)
        self.afcn.setIcon(QIcon('AFC North.jpg'))
        self.afcn.setIconSize(QtCore.QSize(150,50)) 
        
        self.afcs = QtGui.QPushButton('', self)
        self.afcs.setToolTip('Clique para ver a agenda da AFC South')
        self.connect(self.afcs, SIGNAL("clicked()"),self.abreafcs)
        self.afcs.setIcon(QIcon('AFC South.jpg'))
        self.afcs.setIconSize(QtCore.QSize(150,50)) 
        
        self.afcw = QtGui.QPushButton('', self)
        self.afcw.setToolTip('Clique para ver a agenda da AFC West')
        self.connect(self.afcw, SIGNAL("clicked()"),self.abreafcw)
        self.afcw.setIcon(QIcon('AFC West.jpg'))
        self.afcw.setIconSize(QtCore.QSize(150,50)) 
        
        self.afce = QtGui.QPushButton('', self)
        self.afce.setToolTip('Clique para ver a agenda da AFC East')
        self.connect(self.afce, SIGNAL("clicked()"),self.abreafce)
        self.afce.setIcon(QIcon('AFC East.jpg'))
        self.afce.setIconSize(QtCore.QSize(150,50)) 
        
        self.nfcn = QtGui.QPushButton('', self)
        self.nfcn.setToolTip('Clique para ver a agenda da NFC North')
        self.connect(self.nfcn, SIGNAL("clicked()"),self.abrenfcn)
        self.nfcn.setIcon(QIcon('NFC North.jpg'))
        self.nfcn.setIconSize(QtCore.QSize(150,50)) 
        
        self.nfcs = QtGui.QPushButton('', self)
        self.nfcs.setToolTip('Clique para ver a agenda da NFC South')
        self.connect(self.nfcs, SIGNAL("clicked()"),self.abrenfcs)
        self.nfcs.setIcon(QIcon('NFC South.jpg'))
        self.nfcs.setIconSize(QtCore.QSize(150,50)) 
        
        self.nfcw = QtGui.QPushButton('', self)
        self.nfcw.setToolTip('Clique para ver a agenda da NFC West')
        self.connect(self.nfcw, SIGNAL("clicked()"),self.abrenfcw)
        self.nfcw.setIcon(QIcon('NFC West.jpg'))
        self.nfcw.setIconSize(QtCore.QSize(150,50)) 
        
        self.nfce = QtGui.QPushButton('', self)
        self.nfce.setToolTip('Clique para ver a agenda da NFC East')
        self.connect(self.nfce, SIGNAL("clicked()"),self.abrenfce)
        self.nfce.setIcon(QIcon('NFC East.jpg'))
        self.nfce.setIconSize(QtCore.QSize(150,50)) 
        
        self.time = QtGui.QPushButton('', self)
        self.time.setToolTip('Clique para voltar a página do seu time')
        self.connect(self.time, SIGNAL("clicked()"),self.abremeeutime)
        self.time.setIcon(QIcon('meu time.jpg'))
        self.time.setIconSize(QtCore.QSize(150,50))
        
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)  
        
        self.spc=QtGui.QLabel('Agendas')  
        self.spc.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font = QtGui.QFont("Courier", 90, QtGui.QFont.Bold)
        self.spc.setFont(font)
        
        self.ma=QtGui.QLabel('Minha Agenda')  
        self.ma.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font = QtGui.QFont("Courier", 40, QtGui.QFont.Bold)
        self.ma.setFont(font)
        
        self.da=QtGui.QLabel('Agendas das Divisões')  
        self.da.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font = QtGui.QFont("Courier", 40, QtGui.QFont.Bold)
        self.da.setFont(font)
        
        spc=QtGui.QLabel('     ')
        
        grid.addWidget(self.spc,1, 1, 1, 3)        
        grid.addWidget(self.meutime, 3, 2) #colocando os itens no layout
        grid.addWidget(self.afcn, 5, 1)
        grid.addWidget(self.afcs, 6, 1)
        grid.addWidget(self.afce, 7, 1)
        grid.addWidget(self.afcw, 8, 1)
        grid.addWidget(self.nfcn, 5, 3)
        grid.addWidget(self.nfcs, 6, 3)
        grid.addWidget(self.nfce, 7, 3)
        grid.addWidget(self.nfcw, 8, 3)
        grid.addWidget(spc, 9, 2)
        grid.addWidget(self.time, 10, 2)


        self.setLayout(grid)
        
        self.setGeometry(550, 60, 350, 300)
        self.setWindowTitle('NFL - Find My Route - %s - Agenda'%(Meu_Time.listatimes[Meu_Time.escolha][0]))
        self.setWindowIcon(QtGui.QIcon('NFL logo.png'))
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 400)
        if Meu_Time.listatimes[Meu_Time.escolha][0]!='Oakland Raiders': 
            gradient.setColorAt(0.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 255, Meu_Time.listatimes[Meu_Time.escolha][3]))
            gradient.setColorAt(1.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 220, 60))     
        if Meu_Time.listatimes[Meu_Time.escolha][0]=='Oakland Raiders': 
            gradient.setColorAt(0.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 10, 180))
            gradient.setColorAt(1.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 10, 120))
    
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)
                
        self.show()
        
    def abremeutime(self):
        Agenda.meutime=True
        Agenda.conf=None
        Agenda.divisão=None
        Ag=Agenda()
        Ag.exec()
        
    def abrenfcn(self):
        Agenda.meutime=False
        Agenda.conf="NFC"
        Agenda.divisão="N"
        Ag=Agenda()
        Ag.exec()
        
    def abrenfcs(self):
        Agenda.meutime=False
        Agenda.conf="NFC"
        Agenda.divisão="S"
        Ag=Agenda()
        Ag.exec()
        
    def abrenfce(self):
        Agenda.meutime=False
        Agenda.conf="NFC"
        Agenda.divisão="E"
        Ag=Agenda()
        Ag.exec()
        
    def abrenfcw(self):
        Agenda.meutime=False
        Agenda.conf="NFC"
        Agenda.divisão="W"
        Ag=Agenda()
        Ag.exec()
        
    def abreafcn(self):
        Agenda.meutime=False
        Agenda.conf="AFC"
        Agenda.divisão="N"
        Ag=Agenda()
        Ag.exec()
        
    def abreafcs(self):
        Agenda.meutime=False
        Agenda.conf="AFC"
        Agenda.divisão="S"
        Ag=Agenda()
        Ag.exec()
        
    def abreafcw(self):
        Agenda.meutime=False
        Agenda.conf="AFC"
        Agenda.divisão="W"
        Ag=Agenda()
        Ag.exec()
        
    def abreafce(self):
        Agenda.meutime=False
        Agenda.conf="AFC"
        Agenda.divisão="E"
        Ag=Agenda()
        Ag.exec()
        
    def abremeeutime(self):
        self.close
        mt=Meu_Time()
        mt.exec()
        
class Agenda(QtGui.QWidget):
    conf=None
    meutime=False
    timeusuario=None
    divisão=None
    def __init__(self, parent=None):
        super(Agenda, self).__init__(parent) # esse self tem que ter o nome da classe ali senão da bug
        self.ag()
    def ag(self):
        
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)  
        
        if self.meutime==True:
            self.spc=QtGui.QLabel('Agenda '+Meu_Time.listatimes[Meu_Time.escolha][0])  
            self.spc.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
            font = QtGui.QFont("Courier", 20, QtGui.QFont.Bold)
            self.spc.setFont(font)
            grid.addWidget(self.spc, 1, 1, 1, 3)
            espaço=QtGui.QLabel('   ')
            grid.addWidget(espaço, 2, 1)
            coluna=1
            conta=4
            for x in range(1,18):
                self.time2=QtGui.QLabel('Semana %s'%(x))  
                self.time2.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                font = QtGui.QFont("Courier", 10, QtGui.QFont.Bold)
                self.time2.setFont(font)
                grid.addWidget(self.time2, conta, coluna)
                conta+=1
            coluna+=1
            grid.addWidget(espaço, 2, coluna)
            for i in AgendasRivais:
                    if i[0]==self.timeusuario[0]:
                        conta=3
                        self.time2=QtGui.QLabel(i[0])  
                        self.time2.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                        font = QtGui.QFont("Courier", 15, QtGui.QFont.Bold)
                        self.time2.setFont(font)
                        grid.addWidget(self.time2, conta, coluna)
                        conta+=1
                        for l in i[1]:
                            if len(l)==2:
                                self.time1=QtGui.QLabel(l[0])  
                                self.time1.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                                font = QtGui.QFont("Courier", 9, QtGui.QFont.Normal)
                                self.time1.setFont(font)
                                grid.addWidget(self.time1, conta, coluna)
                                conta+=1
                            else:
                                self.time1=QtGui.QLabel(l)  
                                self.time1.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                                font = QtGui.QFont("Courier", 9, QtGui.QFont.Normal)
                                self.time1.setFont(font)
                                grid.addWidget(self.time1, conta, coluna)
                                conta+=1
                        coluna+=1
                        grid.addWidget(espaço, conta, coluna)
                        coluna+=1
            
        if self.meutime==False:
            self.spc=QtGui.QLabel('Agenda '+self.conf+'-'+self.divisão)  
            self.spc.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
            font = QtGui.QFont("Courier", 40, QtGui.QFont.Bold)
            self.spc.setFont(font)
            grid.addWidget(self.spc, 1, 4, 1, 6)
            
        if self.conf!=None:
            espaço=QtGui.QLabel('   ')
            coluna=1
            conta=4
            for x in range(1,18):
                self.time2=QtGui.QLabel('Semana %s'%(x))  
                self.time2.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                font = QtGui.QFont("Courier", 10, QtGui.QFont.Bold)
                self.time2.setFont(font)
                grid.addWidget(self.time2, conta, coluna)
                conta+=1
            coluna+=1
            grid.addWidget(espaço, 2, coluna)
            coluna+=1
            for i in AgendasRivais:
                for k in Times:
                    if i[0]==k[0][0]:
                        if (k[0][2]==self.conf and k[0][3]==self.divisão):
                            conta=3
                            self.time2=QtGui.QLabel(i[0])  
                            self.time2.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                            font = QtGui.QFont("Courier", 15, QtGui.QFont.Bold)
                            self.time2.setFont(font)
                            grid.addWidget(self.time2, conta, coluna)
                            conta+=1
                            for l in i[1]:
                                if len(l)==2:
                                    self.time1=QtGui.QLabel(l[0])  
                                    self.time1.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                                    font = QtGui.QFont("Courier", 9, QtGui.QFont.Normal)
                                    self.time1.setFont(font)
                                    grid.addWidget(self.time1, conta, coluna)
                                    conta+=1
                                else:
                                    self.time1=QtGui.QLabel(l)  
                                    self.time1.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                                    font = QtGui.QFont("Courier", 9, QtGui.QFont.Normal)
                                    self.time1.setFont(font)
                                    grid.addWidget(self.time1, conta, coluna)
                                    conta+=1
                            coluna+=1
                            grid.addWidget(espaço, conta, coluna)
                            coluna+=1
                                
        grid.addWidget(espaço, 7, 1)

        self.setLayout(grid)
        
        self.setGeometry(70, 110, 350, 300)
        self.setWindowTitle('NFL - Find My Route - %s - Agenda'%(Meu_Time.listatimes[Meu_Time.escolha][0]))
        self.setWindowIcon(QtGui.QIcon('NFL logo.png'))
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 400)
        if Meu_Time.listatimes[Meu_Time.escolha][0]!='Oakland Raiders': 
            gradient.setColorAt(0.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 255, Meu_Time.listatimes[Meu_Time.escolha][3]))
            gradient.setColorAt(1.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 220, 60))     
        if Meu_Time.listatimes[Meu_Time.escolha][0]=='Oakland Raiders': 
            gradient.setColorAt(0.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 10, 180))
            gradient.setColorAt(1.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 10, 120))
    
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)
                
        self.show()
        
class escolheStandings(QtGui.QWidget):
    timeusuario=None
    def __init__(self, parent=None):
        super(escolheStandings, self).__init__(parent) # esse self tem que ter o nome da classe ali senão da bug
        self.st()
    def st(self):
        grid = QtGui.QGridLayout()
        grid.setSpacing(6)  
        
        self.meutime = QtGui.QPushButton('', self)
        self.meutime.setToolTip('Clique para ver as Divisões da NFL')
        self.connect(self.meutime, SIGNAL("clicked()"),self.abremeutime)
        self.meutime.setIcon(QIcon('meu time.jpg'))
        self.meutime.setIconSize(QtCore.QSize(150,50))         
        
        self.spc=QtGui.QLabel('Standings') 
#        self.spc=QtGui.QLabel(Meu_Time.listatimes[Meu_Time.escolha][0])
        self.spc.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font = QtGui.QFont("Courier", 80, QtGui.QFont.Bold)
        self.spc.setFont(font) 
        
        self.divisão = QtGui.QPushButton('', self)
        self.divisão.setToolTip('Clique para ver as Divisões da NFL')
        self.divisão.resize(self.divisão.sizeHint())
        self.connect(self.divisão, SIGNAL("clicked()"),self.abrestandings)
        self.divisão.setIcon(QIcon('Divisão.jpg'))
        self.divisão.setIconSize(QtCore.QSize(200,150))
        
        self.conferencia = QtGui.QPushButton('', self)
        self.conferencia.setToolTip('Clique para ver as Conferências da NFL')
        self.conferencia.resize(self.conferencia.sizeHint())
        self.connect(self.conferencia, SIGNAL("clicked()"),self.abreconf)
        for i in Times:
            if i[0][0]==self.timeusuario[0]:
                if i[0][2] == 'AFC':
                    self.conferencia.setIcon(QIcon('Conf Afc.jpg'))
                if i[0][2] == 'NFC': 
                    self.conferencia.setIcon(QIcon('Conf Nfc.jpg'))
        self.conferencia.setIconSize(QtCore.QSize(200,150))
        
        espaço=QtGui.QLabel('                  ')


        grid.addWidget(self.spc, 1, 1, 1, 3)
        grid.addWidget(espaço, 3, 0)
        grid.addWidget(self.divisão, 3, 1)
        grid.addWidget(espaço, 3, 3)
        grid.addWidget(self.conferencia, 3, 3)
        grid.addWidget(espaço, 4, 4)
        grid.addWidget(self.meutime, 4, 2)
        grid.addWidget(espaço, 5, 4)
        
        self.setLayout(grid)
        self.setGeometry(250, 230, 100, 100)
        self.setWindowTitle('NFL - Find My Route - %s - Standings'%(Meu_Time.listatimes[Meu_Time.escolha][0]))
        self.setWindowIcon(QtGui.QIcon('NFL logo.png'))
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 400)
        if Meu_Time.listatimes[Meu_Time.escolha][0]!='Oakland Raiders': 
            gradient.setColorAt(0.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 255, Meu_Time.listatimes[Meu_Time.escolha][3]))
            gradient.setColorAt(1.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 220, 60))     
        if Meu_Time.listatimes[Meu_Time.escolha][0]=='Oakland Raiders': 
            gradient.setColorAt(0.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 10, 180))
            gradient.setColorAt(1.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 10, 120))
    
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)
                
        self.show()
        
    def abrestandings(self):
        St=divisaoStandings()
        St.exec()
        
    def abreconf(self):
        St=Standings()
        St.exec()
        
    def abremeutime(self):
        self.close
        mt=Meu_Time()
        mt.exec()
        
        
        
class Standings(QtGui.QWidget):
    timeusuario='s'
    def __init__(self, parent=None):
        super(Standings, self).__init__(parent) # esse self tem que ter o nome da classe ali senão da bug
        self.st()
    def st(self):
        
        grid = QtGui.QGridLayout()
        grid.setSpacing(6)  
        
        
#        self.spc=QtGui.QLabel(Meu_Time.listatimes[Meu_Time.escolha][0])  
#        self.spc.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
#        font = QtGui.QFont("Courier", 40, QtGui.QFont.Bold)
#        self.spc.setFont(font)       
#        
#        grid.addWidget(self.spc, 2, 1)
        espaço=QtGui.QLabel('                  ')
        
        
        self.spc=QtGui.QLabel('Standings') 
#        self.spc=QtGui.QLabel(Meu_Time.listatimes[Meu_Time.escolha][0])
        self.spc.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font = QtGui.QFont("Courier", 30, QtGui.QFont.Bold)
        self.spc.setFont(font) 
        
        
        titulo1=QtGui.QLabel('Time')
        titulo1.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font2 = QtGui.QFont("Courier", 15, QtGui.QFont.Bold)
        titulo1.setFont(font2)  
        
        
        titulo2=QtGui.QLabel('W')
        titulo2.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font2 = QtGui.QFont("Courier", 15, QtGui.QFont.Bold)
        titulo2.setFont(font2)
        
        titulo3=QtGui.QLabel('L')
        titulo3.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font2 = QtGui.QFont("Courier", 15, QtGui.QFont.Bold)
        titulo3.setFont(font2)
        
        titulo4=QtGui.QLabel('T')
        titulo4.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font2 = QtGui.QFont("Courier", 15, QtGui.QFont.Bold)
        titulo4.setFont(font2)
        
        titulo5=QtGui.QLabel('Time')
        titulo5.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 15, QtGui.QFont.Bold)
        titulo5.setFont(font4)    
            
        titulo6=QtGui.QLabel('W')
        titulo6.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 15, QtGui.QFont.Bold)
        titulo6.setFont(font4)
                
        titulo7=QtGui.QLabel('L')
        titulo7.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 15, QtGui.QFont.Bold)
        titulo7.setFont(font4)
        
        titulo8=QtGui.QLabel('T')
        titulo8.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 15, QtGui.QFont.Bold)
        titulo8.setFont(font4)
        
        passou=QtGui.QLabel('Lider Div.')
        passou.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        passou.setFont(font4)
        
        wild=QtGui.QLabel('WildCard')
        wild.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        wild.setFont(font4)
        
        passou2=QtGui.QLabel('Lider Div.')
        passou2.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        passou2.setFont(font4)
        
        wild2=QtGui.QLabel('WildCard')
        wild2.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        wild2.setFont(font4)
        
        passou3=QtGui.QLabel('Lider Div.')
        passou3.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        passou3.setFont(font4)
        
        wild3=QtGui.QLabel('WildCard')
        wild3.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        wild3.setFont(font4)
        
        passou4=QtGui.QLabel('Lider Div.')
        passou4.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        passou4.setFont(font4)
        
        wild4=QtGui.QLabel('WildCard')
        wild4.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        wild4.setFont(font4)
        
        passou5=QtGui.QLabel('Lider Div.')
        passou5.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        passou5.setFont(font4)
        
        passou6=QtGui.QLabel('Lider Div.')
        passou6.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        passou6.setFont(font4)
        
        passou7=QtGui.QLabel('Lider Div.')
        passou7.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        passou7.setFont(font4)
        
        passou8=QtGui.QLabel('Lider Div.')
        passou8.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        passou8.setFont(font4)
        
        self.meutime = QtGui.QPushButton('', self)
        self.meutime.setToolTip('Clique para ver as Divisões da NFL')
        self.connect(self.meutime, SIGNAL("clicked()"),self.abremeutime)
        self.meutime.setIcon(QIcon('meu time.jpg'))
        self.meutime.setIconSize(QtCore.QSize(150,50)) 
        
       



        
        self.Afc=PicButton(QPixmap("mini-logo-afc.png")) 
        self.Afc.resize(20,20)

        self.Nfc=PicButton(QPixmap("mini-logo-nfc.png")) 
        self.Nfc.resize(20,20)
        
        
        grid.addWidget(self.spc, 1, 7)
        grid.addWidget(self.Afc, 2, 0)
        grid.addWidget(self.Nfc, 2, 8)
        grid.addWidget(espaço, 3, 0)
        grid.addWidget(titulo1, 3, 1)
        grid.addWidget(titulo2, 3, 4)
        grid.addWidget(titulo3, 3, 5)
        grid.addWidget(titulo4, 3, 6)
        grid.addWidget(espaço, 3, 7)
        grid.addWidget(titulo5, 3, 9)
        grid.addWidget(espaço, 3, 11)
        grid.addWidget(titulo6, 3, 12)
        grid.addWidget(titulo7, 3, 13)
        grid.addWidget(titulo8, 3, 14)
        grid.addWidget(passou, 4, 0)
        grid.addWidget(passou2, 5, 0)
        grid.addWidget(passou3, 6, 0)
        grid.addWidget(passou4, 7, 0)
        grid.addWidget(wild, 8, 0)
        grid.addWidget(wild2, 9, 0)
        grid.addWidget(passou5, 4, 8)
        grid.addWidget(passou6, 5, 8)
        grid.addWidget(passou7, 6, 8)
        grid.addWidget(passou8, 7, 8)
        grid.addWidget(wild3, 8, 8)
        grid.addWidget(wild4, 9, 8)
        grid.addWidget(self.meutime, 21, 7)
        
        for i in range(0,16):
            if Afc[i][0] != self.timeusuario[0]:
                ide0=QtGui.QLabel(Afc[i][0])
                ide0.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                font3 = QtGui.QFont("Courier", 14, QtGui.QFont.Normal)
                ide0.setFont(font3)    
                
                ide1=QtGui.QLabel(Afc[i][1])
                ide1.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                font3 = QtGui.QFont("Courier", 14, QtGui.QFont.Normal)
                ide1.setFont(font3)
                
                ide2=QtGui.QLabel(Afc[i][2])
                ide2.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                font3 = QtGui.QFont("Courier", 14, QtGui.QFont.Normal)
                ide2.setFont(font3)
                
                ide3=QtGui.QLabel(Afc[i][3])
                ide3.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                font3 = QtGui.QFont("Courier", 14, QtGui.QFont.Normal)
                ide3.setFont(font3)
                
                grid.addWidget(ide0, i+4, 1)
                grid.addWidget(ide1, i+4, 4)
                grid.addWidget(ide2, i+4, 5)
                grid.addWidget(ide3, i+4, 6)
                                
            if Afc[i][0] == self.timeusuario[0]:
                    print('plow')
                    ide0=QtGui.QLabel(Afc[i][0])
                    ide0.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                    font3 = QtGui.QFont("Courier", 14, QtGui.QFont.Bold)
                    ide0.setFont(font3)    
                    
                    ide1=QtGui.QLabel(Afc[i][1])
                    ide1.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                    font3 = QtGui.QFont("Courier", 14, QtGui.QFont.Bold)
                    ide1.setFont(font3)
                    
                    ide2=QtGui.QLabel(Afc[i][2])
                    ide2.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                    font3 = QtGui.QFont("Courier", 14, QtGui.QFont.Bold)
                    ide2.setFont(font3)
                    
                    ide3=QtGui.QLabel(Afc[i][3])
                    ide3.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                    font3 = QtGui.QFont("Courier", 14, QtGui.QFont.Bold)
                    ide3.setFont(font3)
                    
                    grid.addWidget(ide0, i+4, 1)
                    grid.addWidget(ide1, i+4, 4)
                    grid.addWidget(ide2, i+4, 5)
                    grid.addWidget(ide3, i+4, 6)
                    
        for i in range(0,16):
            if Nfc[i][0] != self.timeusuario[0]:
                ide0=QtGui.QLabel(Nfc[i][0])
                ide0.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                font3 = QtGui.QFont("Courier", 14, QtGui.QFont.Normal)
                ide0.setFont(font3)    
                
                ide1=QtGui.QLabel(Nfc[i][1])
                ide1.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                font3 = QtGui.QFont("Courier", 14, QtGui.QFont.Normal)
                ide1.setFont(font3)
                
                ide2=QtGui.QLabel(Nfc[i][2])
                ide2.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                font3 = QtGui.QFont("Courier", 14, QtGui.QFont.Normal)
                ide2.setFont(font3)
                
                ide3=QtGui.QLabel(Nfc[i][3])
                ide3.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                font3 = QtGui.QFont("Courier", 14, QtGui.QFont.Normal)
                ide3.setFont(font3)
                
                grid.addWidget(ide0, i+4, 9)
                grid.addWidget(ide1, i+4, 12)
                grid.addWidget(ide2, i+4, 13)
                grid.addWidget(ide3, i+4, 14)
                
            if Nfc[i][0] == self.timeusuario[0]:
                    ide0=QtGui.QLabel(Nfc[i][0])
                    ide0.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                    font3 = QtGui.QFont("Courier", 14, QtGui.QFont.Bold)
                    ide0.setFont(font3)    
                    
                    ide1=QtGui.QLabel(Nfc[i][1])
                    ide1.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                    font3 = QtGui.QFont("Courier", 14, QtGui.QFont.Bold)
                    ide1.setFont(font3)
                    
                    ide2=QtGui.QLabel(Nfc[i][2])
                    ide2.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                    font3 = QtGui.QFont("Courier", 14, QtGui.QFont.Bold)
                    ide2.setFont(font3)
                    
                    ide3=QtGui.QLabel(Nfc[i][3])
                    ide3.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                    font3 = QtGui.QFont("Courier", 14, QtGui.QFont.Bold)
                    ide3.setFont(font3)
                    
                    grid.addWidget(ide0, i+4, 9)
                    grid.addWidget(ide1, i+4, 12)
                    grid.addWidget(ide2, i+4, 13)
                    grid.addWidget(ide3, i+4, 14)
                    
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 400)
        if Meu_Time.listatimes[Meu_Time.escolha][0]!='Oakland Raiders': 
            gradient.setColorAt(0.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 255, Meu_Time.listatimes[Meu_Time.escolha][3]))
            gradient.setColorAt(1.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 220, 60))     
        if Meu_Time.listatimes[Meu_Time.escolha][0]=='Oakland Raiders': 
            gradient.setColorAt(0.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 10, 180))
            gradient.setColorAt(1.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 10, 120))
    
        p.setBrush(QPalette.Window, QBrush(gradient))
                    
        self.square = QtGui.QFrame(self)
        self.square.setGeometry(50, 50, (self.width()-50), (self.height()-50))
        #self.square.setLayout(grid)
        self.square.setPalette(p)
        self.setLayout(grid)
        self.setGeometry(30, 30, 100, 100)
        self.setWindowTitle('NFL - Find My Route - %s - Standings'%(Meu_Time.listatimes[Meu_Time.escolha][0]))
        self.setWindowIcon(QtGui.QIcon('NFL logo.png'))
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 400)
        if Meu_Time.listatimes[Meu_Time.escolha][0]!='Oakland Raiders': 
            gradient.setColorAt(0.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 255, Meu_Time.listatimes[Meu_Time.escolha][3]))
            gradient.setColorAt(1.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 220, 60))     
        if Meu_Time.listatimes[Meu_Time.escolha][0]=='Oakland Raiders': 
            gradient.setColorAt(0.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 10, 180))
            gradient.setColorAt(1.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 10, 120))
    
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)
                
        self.show()
        
    def abremeutime(self):
        self.close
        Mr=Meu_Time()
        Mr.exec()
        
class divisaoStandings(QtGui.QWidget):
    timeusuario='s'
    def __init__(self, parent=None):
        super(divisaoStandings, self).__init__(parent) # esse self tem que ter o nome da classe ali senão da bug
        self.st()
    def st(self):
        
        grid = QtGui.QGridLayout()
        grid.setSpacing(6)  
        
        
#        self.spc=QtGui.QLabel(Meu_Time.listatimes[Meu_Time.escolha][0])  
#        self.spc.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
#        font = QtGui.QFont("Courier", 40, QtGui.QFont.Bold)
#        self.spc.setFont(font)       
#        
#        grid.addWidget(self.spc, 2, 1)
        espaço=QtGui.QLabel('                  ')
        
#        self.meutime = QtGui.QPushButton('', self)
#        self.meutime.setToolTip('Clique para ver as Divisões da NFL')
#        self.connect(self.meutime, SIGNAL("clicked()"),self.abremeutime)
#        self.meutime.setIcon(QIcon('meu time.jpg'))
#        self.meutime.setIconSize(QtCore.QSize(150,50)) 
#        
        
        self.spc=QtGui.QLabel('Standings') 
#        self.spc=QtGui.QLabel(Meu_Time.listatimes[Meu_Time.escolha][0])
        self.spc.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font = QtGui.QFont("Courier", 30, QtGui.QFont.Bold)
        self.spc.setFont(font) 
        
        
        passou=QtGui.QLabel('Lider Div.')
        passou.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        passou.setFont(font4)
        
        wild=QtGui.QLabel('WildCard')
        wild.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        wild.setFont(font4)
        
        passou2=QtGui.QLabel('Lider Div.')
        passou2.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        passou2.setFont(font4)
        
        wild2=QtGui.QLabel('WildCard')
        wild2.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        wild2.setFont(font4)
        
        passou3=QtGui.QLabel('Lider Div.')
        passou3.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        passou3.setFont(font4)
        
        wild3=QtGui.QLabel('WildCard')
        wild3.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        wild3.setFont(font4)
        
        passou4=QtGui.QLabel('Lider Div.')
        passou4.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        passou4.setFont(font4)
        
        wild4=QtGui.QLabel('WildCard')
        wild4.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        wild4.setFont(font4)
        
        passou5=QtGui.QLabel('Lider Div.')
        passou5.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        passou5.setFont(font4)
        
        passou6=QtGui.QLabel('Lider Div.')
        passou6.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        passou6.setFont(font4)
        
        passou7=QtGui.QLabel('Lider Div.')
        passou7.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        passou7.setFont(font4)
        
        passou8=QtGui.QLabel('Lider Div.')
        passou8.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font4 = QtGui.QFont("Courier", 7, QtGui.QFont.Light)
        passou8.setFont(font4)
        

        
        self.Afc=PicButton(QPixmap("mini-logo-afc.png")) 
        self.Afc.resize(20,20)

        self.Nfc=PicButton(QPixmap("mini-logo-nfc.png")) 
        self.Nfc.resize(20,20)
        
        
        grid.addWidget(self.spc, 1, 6)
        grid.addWidget(self.Afc, 2, 0)
        grid.addWidget(self.Nfc, 2, 7)
        grid.addWidget(passou, 4, 0)
        grid.addWidget(passou2, 10, 0)
        grid.addWidget(passou3, 16, 0)
        grid.addWidget(passou4, 22, 0)
        grid.addWidget(passou5, 4, 7)
        grid.addWidget(passou6, 10, 7)
        grid.addWidget(passou7, 16, 7)
        grid.addWidget(passou8, 22, 7)
               
        contador=3
        contadornfc=3
        for i in range(len(Standings2)):
            if Standings2[i][0][0]=='AFC':
                ide0=QtGui.QLabel(Standings2[i][0][0]+'-'+Standings2[i][0][1])
                ide0.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                font3 = QtGui.QFont("Courier", 14, QtGui.QFont.Bold)
                ide0.setFont(font3)   
                
                grid.addWidget(ide0, contador, 1)
                contador+=1
                
                for k in Standings2[i][1]:
                    if k[0]!=self.timeusuario[0]:
                
                        ide1=QtGui.QLabel(k[0])
                        ide1.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                        font3 = QtGui.QFont("Courier", 12, QtGui.QFont.Normal)
                        ide1.setFont(font3)
                        
                        ide2=QtGui.QLabel(k[1])
                        ide2.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                        font3 = QtGui.QFont("Courier", 12, QtGui.QFont.Normal)
                        ide2.setFont(font3)
                        
                        ide3=QtGui.QLabel(k[2])
                        ide3.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                        font3 = QtGui.QFont("Courier", 12, QtGui.QFont.Normal)
                        ide3.setFont(font3)
                        
                        ide4=QtGui.QLabel(k[3])
                        ide4.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                        font3 = QtGui.QFont("Courier", 12, QtGui.QFont.Normal)
                        ide4.setFont(font3)
                        
                        grid.addWidget(ide1, contador, 1)
                        grid.addWidget(ide2, contador, 4)
                        grid.addWidget(ide3, contador, 5)
                        grid.addWidget(ide4, contador, 6)
                        contador+=1
                        
                    if k[0]==self.timeusuario[0]:
                
                        ide1=QtGui.QLabel(k[0])
                        ide1.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                        font3 = QtGui.QFont("Courier", 13, QtGui.QFont.Bold)
                        ide1.setFont(font3)
                        
                        ide2=QtGui.QLabel(k[1])
                        ide2.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                        font3 = QtGui.QFont("Courier", 13, QtGui.QFont.Bold)
                        ide2.setFont(font3)
                        
                        ide3=QtGui.QLabel(k[2])
                        ide3.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                        font3 = QtGui.QFont("Courier", 13, QtGui.QFont.Bold)
                        ide3.setFont(font3)
                        
                        ide4=QtGui.QLabel(k[3])
                        ide4.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                        font3 = QtGui.QFont("Courier", 13, QtGui.QFont.Bold)
                        ide4.setFont(font3)
                        
                        grid.addWidget(ide1, contador, 1)
                        grid.addWidget(ide2, contador, 4)
                        grid.addWidget(ide3, contador, 5)
                        grid.addWidget(ide4, contador, 6)
                        contador+=1
                
                espação=QtGui.QLabel(' ')
                
                grid.addWidget(espação, contador, 1)
                contador+=1
                
            if Standings2[i][0][0]=='NFC':
                ide0=QtGui.QLabel(Standings2[i][0][0]+'-'+Standings2[i][0][1])
                ide0.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                font3 = QtGui.QFont("Courier", 14, QtGui.QFont.Bold)
                ide0.setFont(font3)  
                
                grid.addWidget(ide0, contadornfc, 8)
                contadornfc+=1
                
                for k in Standings2[i][1]:
                    if k[0]!=self.timeusuario[0]:
                        ide1=QtGui.QLabel(k[0])
                        ide1.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                        font3 = QtGui.QFont("Courier", 12, QtGui.QFont.Normal)
                        ide1.setFont(font3)
                        
                        ide2=QtGui.QLabel(k[1])
                        ide2.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                        font3 = QtGui.QFont("Courier", 12, QtGui.QFont.Normal)
                        ide2.setFont(font3)
                        
                        ide3=QtGui.QLabel(k[2])
                        ide3.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                        font3 = QtGui.QFont("Courier", 12, QtGui.QFont.Normal)
                        ide3.setFont(font3)
                        
                        ide4=QtGui.QLabel(k[3])
                        ide4.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                        font3 = QtGui.QFont("Courier", 12, QtGui.QFont.Normal)
                        ide4.setFont(font3)
                        
                        grid.addWidget(ide1, contadornfc, 8)
                        grid.addWidget(ide2, contadornfc, 11)
                        grid.addWidget(ide3, contadornfc, 12)
                        grid.addWidget(ide4, contadornfc, 13)
                        contadornfc+=1
                        
                    if k[0]==self.timeusuario[0]:
                        ide1=QtGui.QLabel(k[0])
                        ide1.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                        font3 = QtGui.QFont("Courier", 13, QtGui.QFont.Bold)
                        ide1.setFont(font3)
                        
                        ide2=QtGui.QLabel(k[1])
                        ide2.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                        font3 = QtGui.QFont("Courier", 13, QtGui.QFont.Bold)
                        ide2.setFont(font3)
                        
                        ide3=QtGui.QLabel(k[2])
                        ide3.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                        font3 = QtGui.QFont("Courier", 13, QtGui.QFont.Bold)
                        ide3.setFont(font3)
                        
                        ide4=QtGui.QLabel(k[3])
                        ide4.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
                        font3 = QtGui.QFont("Courier", 13, QtGui.QFont.Bold)
                        ide4.setFont(font3)
                        
                        grid.addWidget(ide1, contadornfc, 8)
                        grid.addWidget(ide2, contadornfc, 11)
                        grid.addWidget(ide3, contadornfc, 12)
                        grid.addWidget(ide4, contadornfc, 13)
                        contadornfc+=1
                
                espação=QtGui.QLabel(' ')
    
                grid.addWidget(espação, contadornfc, 8)
                contadornfc+=1
                
        
                
        self.setLayout(grid)
        self.setGeometry(30, 30, 100, 100)
        self.setWindowTitle('NFL - Find My Route - %s - Standings'%(Meu_Time.listatimes[Meu_Time.escolha][0]))
        self.setWindowIcon(QtGui.QIcon('NFL logo.png'))
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 400)
        if Meu_Time.listatimes[Meu_Time.escolha][0]!='Oakland Raiders': 
            gradient.setColorAt(0.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 255, Meu_Time.listatimes[Meu_Time.escolha][3]))
            gradient.setColorAt(1.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 220, 60))     
        if Meu_Time.listatimes[Meu_Time.escolha][0]=='Oakland Raiders': 
            gradient.setColorAt(0.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 10, 180))
            gradient.setColorAt(1.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 10, 120))
    
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)
                
        self.show()
        
    def abremeutime(self):
        self.close
        Mr=Meu_Time()
        Mr.exec()
        
class Prev(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Prev, self).__init__(parent) # esse self tem que ter o nome da classe ali senão da bug
        self.pr()
    def pr(self):
        
        grid = QtGui.QGridLayout()
        grid.setSpacing(20)  
        
        self.spc=QtGui.QLabel(Meu_Time.listatimes[Meu_Time.escolha][0])  
        self.spc.setStyleSheet('color: %s'%(Meu_Time.listatimes[Meu_Time.escolha][4]))
        font = QtGui.QFont("Courier", 40, QtGui.QFont.Bold)
        self.spc.setFont(font)        
        
        
        #grid.addWidget(self.letras,1, 3, 1, 3)        
        #grid.addWidget(self.Afc, 2, 0) #colocando os itens no layout
        grid.addWidget(self.spc, 2, 1)


        self.setLayout(grid)
        
        self.setGeometry(70, 110, 350, 300)
        self.setWindowTitle('NFL - Find My Route - %s - Previsão'%(Meu_Time.listatimes[Meu_Time.escolha][0]))
        self.setWindowIcon(QtGui.QIcon('NFL logo.png'))
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 400)
        if Meu_Time.listatimes[Meu_Time.escolha][0]!='Oakland Raiders': 
            gradient.setColorAt(0.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 255, Meu_Time.listatimes[Meu_Time.escolha][3]))
            gradient.setColorAt(1.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 220, 60))     
        if Meu_Time.listatimes[Meu_Time.escolha][0]=='Oakland Raiders': 
            gradient.setColorAt(0.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 10, 180))
            gradient.setColorAt(1.0, QColor.fromHsv(Meu_Time.listatimes[Meu_Time.escolha][2], 10, 120))
    
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)
                
        self.show()
    

def main():   
    app = QtGui.QApplication(sys.argv)
    ex = Escolha()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 

        