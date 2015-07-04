# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 23:59:17 2015

@author: Felipe
"""

times=open("Times.csv","r") #abrindo times
agendas=open("agendas.csv","r") #abrindo agendas
standings=open("standings.csv","r")
wit=open("vitorias.csv","r")
wit=wit.readlines()
times=times.readlines() 
agendas=agendas.readlines()
standings=standings.readlines()
witt=[]
for i in wit:
    a=i.split("\n")
    witt.append(a[0])
    
wiitt=[]
for i in witt:
    p=i.split(",")
    wiitt.append(p)
Vitorias=[]
for i in wiitt:
    pequeno=[]
    for k in i:       
        if k != i[0]:
            pequeno.append(k)
    Vitorias.append([i[0],pequeno])                

stan=[]
Times=[]
Agendas=[]
tim=[]
for i in times: #split em times
    i=i.split(",")
    tim.append(i)
for i in standings: #split em times
    i=i.split(",")
    stan.append(i)
istandings=[]
for i in stan:
    pedra=[]
    if len(i)==2:
        for p in i:
            if p==i[1]:
                o=p.split("\n")
                pedra.append(o[0])
            if p==i[0]:
                pedra.append(p)
    if len(i)==4:
        for k in i:
            if k==i[3]:
                o=k.split("\n")
                pedra.append(o[0])
            if (k==i[0] or k==i[1] or k==i[2]):
                pedra.append(k)
    istandings.append(pedra)
x=0
Standings=[]
xtandings=[] 
PredS=[]
   
while x <40:
    ç=[]
    y=0
    while y<5:
        ç.append(istandings[x])
        x+=1
        y+=1
    xtandings.append(ç)
    
for i in xtandings:
    jota=[]
    for k in i:
        if k==i[0]:
            lima=k
        else:
            jota.append(k)
    Standings.append([lima,jota])
    PredS.append([lima,jota])

for i in tim: #strip em times e separando a homefield advantage
    sem=[]
    casa=[]
    for k in i:
        if k == i[7]:
            a=i[7].split('\n')
            casa.append(a[0])
        else:
            sem.append(k)
    Times.append([sem,casa])
    
agnd=[]
for i in agendas:  #split em agendas
    i=i.split(",")
    agnd.append(i)
for i in agnd:
    sem=[]
    uno=[]
    for k in i:
        if k == i[0]: #strip em agendas
            uno.append(k)
        if k == i[17]:
            a=k.split("\n")
            sem.append(a[0])
        if (k!=i[0] and k!=i[17]):
            sem.append(k)
    Agendas.append([uno,sem,int(0)])
    
for i in Standings:
    mae=0
    little=[]
    listinha=[]
    for k in i:
        mae=0
        trocou=0
        little=[]
        listinha=[]
        if k==i[1]:
            for j in k:
                little.append(j[1])
            while mae<4:
                for l in range(len(k)):
                    if (k[l][1]==max(little) and k[l] not in listinha):
                        listinha.append(k[l])
                        little.remove(max(little))
                        break
                mae+=1
            for zx in range(len(listinha)):
                for xz in range(len(listinha)):
                    if (int(listinha[zx][1])==int(listinha[xz][1]) and zx!=xz and trocou==0):
                        if int(listinha[zx][3])>int(listinha[xz][3]):
                            aa=listinha[zx]
                            bb=listinha[xz]
                            del listinha[zx]
                            listinha.insert(zx,aa)
                            del listinha[xz]
                            listinha.insert(xz,bb)
                        if int(listinha[zx][3])<int(listinha[xz][3]):
                            aa=listinha[xz]
                            bb=listinha[zx]
                            del listinha[zx]
                            listinha.insert(zx,aa)
                            del listinha[xz]
                            listinha.insert(xz,bb)
                            trocou+=1
                            break
                        break

    i.pop()
    i.append(listinha)

listaenorme=[]
for pololo in Times:
    versus=[]
    
    timeusuario=pololo[0][0] # escolha do time
    for i in Agendas:
        if i[0][0]==timeusuario:
            for k in i:
                if k!=i[0] and k!=i[2]: # análise do time
                    versus.append(k) # salva os times que irão enfrentar o time escolhido nessa lista
    
    for i in Times:
        if timeusuario==i[0][0]: #salva as informações importantes do time escolhido
            muutime=[i[0][2],i[0][3],i[0][6],i[1][0]]
            
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
    
    for i in tudo: #sistema de pontuação
        if len(i[0])==2: 
            i[1]+=int(i[0][0][1][0])# jogos fora de casa, somam pontuação
        if len(i[0])==1:
            i[1]-=int(muutime[3]) #jogos em casa subtrai pontuação
        if len(i[0])!=0:
         #   if i[0][0][0][2]==meutime[0][0]: #se for da mesma conferencia/
          #      i[1]-=2
           # if (i[0][0][0][3]==meutime[0][1] and i[0][0][0][2]==meutime[0][0]):
            #    i[1]-=5 # se for da mesma divisão
            dist=int(muutime[2])-int(i[0][0][0][6])
            i[1]+=dist # difereças de rankiamento
                           
    analise=[]            
    for i in tudo:
        if len(i[0])!=0:
            if len(i[0])==2:
                analise.append([i[0][0][0][0],i[1]])
            else:
                analise.append([i[0][0][0][0],i[1]])
                
    vitorias=0
    derrotas=0    
    empates=0    
    for i in predição:    
        if len(i)!=1:        
            i.pop()
    for i in predição:    
        if i[1]<0:        
            i.append("W")  
            vitorias+=1
        if i[1]>0:        
            i.append("L")
            derrotas+=1
        if i[1]==0:
            i.append("T")
            empates+=1
    quantasW=vitorias #quantas vitórias são necessárias para ir para os playoffs
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
    for i in range(quantasW):
        wins[i].append("W")    
    for i in wins:
        if len(i)==2:
            i.append("L")
                                
    for i in tudo:
        if len(i[0])!=0:
            if len(i[0])==2:
                for k in wins:
                    if (k[1]==i[1] and k[0]==i[0][0][0][0]):
                        k[0]="@"+k[0]
    
    umalista=[]
    for i in tudo:
        momo=[]
        lololo=None
        if len(i[0])!=0:
            if len(i[0])==2:
                lololo="@"+i[0][0][0][0]
            if len(i[0])==1:
                lololo=i[0][0][0][0]
            momo.append([lololo,i[1]])
        else:
            momo.append("BYE WEEK")
        umalista.append(momo)
        
    for i in range(len(umalista)):
        for k in wins:
            if umalista[i][0][0]==k[0]:
                umalista[i].append(k[2])
                       
    quebonito=[]         
    for i in umalista:
        if len(i)==2:
            quebonito.append([i[0][0],i[1]]) #AQUI TÃO AS W E L
        else:
            quebonito.append("BYE WEEK")  
            
    listaenorme.append([timeusuario,predição,vitorias,derrotas,empates,quebonito])
    
for i in PredS:
    for k in i:
        if k == i[1]:
            for g in k:
                for l in listaenorme:
                    if g[0]==l[0]:
                        del g[1]
                        g.insert(1,l[2])
                        del g[2]
                        g.insert(2,l[3])
                        
standings2=open("standings.csv","r")
standings2=standings2.readlines()
stan2=[]
for i in standings2: #split em times
    i=i.split(",")
    stan2.append(i)
istandings2=[]
for i in stan2:
    pedra=[]
    if len(i)==2:
        for p in i:
            if p==i[1]:
                o=p.split("\n")
                pedra.append(o[0])
            if p==i[0]:
                pedra.append(p)
    if len(i)==4:
        for k in i:
            if k==i[3]:
                o=k.split("\n")
                pedra.append(o[0])
            if (k==i[0] or k==i[1] or k==i[2]):
                pedra.append(k)
    istandings2.append(pedra)
x2=0
Standings2=[]
xtandings2=[] 

   
while x2 <40:
    ç=[]
    y2=0
    while y2<5:
        ç.append(istandings2[x2])
        x2+=1
        y2+=1
    xtandings2.append(ç)
    
for i in xtandings2:
    jota=[]
    for k in i:
        if k==i[0]:
            lima=k
        else:
            jota.append(k)
    Standings2.append([lima,jota])

for i in PredS:
    mae=0
    little=[]
    listinha=[]
    for k in i:
        mae=0
        trocou=0
        little=[]
        listinha=[]
        if k==i[1]:
            for j in k:
                little.append(j[1])
            while mae<4:
                for l in range(len(k)):
                    if (k[l][1]==max(little) and k[l] not in listinha):
                        listinha.append(k[l])
                        little.remove(max(little))
                        break
                mae+=1
            for zx in range(len(listinha)):
                for xz in range(len(listinha)):
                    if (int(listinha[zx][1])==int(listinha[xz][1]) and zx!=xz and trocou==0):
                        
                        if int(listinha[zx][3])>int(listinha[xz][3]):
                            aa=listinha[zx]
                            bb=listinha[xz]
                            del listinha[zx]
                            listinha.insert(zx,aa)
                            del listinha[xz]
                            listinha.insert(xz,bb)
                        if int(listinha[zx][3])<int(listinha[xz][3]):
                            aa=listinha[xz]
                            bb=listinha[zx]
                            del listinha[zx]
                            listinha.insert(zx,aa)
                            del listinha[xz]
                            listinha.insert(xz,bb)
                            trocou+=1
                            break
                        break

    i.pop()
    i.append(listinha)

for i in Standings2:
    mae=0
    little=[]
    listinha=[]
    for k in i:
        mae=0
        trocou=0
        little=[]
        listinha=[]
        if k==i[1]:
            for j in k:
                little.append(j[1])
            while mae<4:
                for l in range(len(k)):
                    if (k[l][1]==max(little) and k[l] not in listinha):
                        listinha.append(k[l])
                        little.remove(max(little))
                        break
                mae+=1
            for zx in range(len(listinha)):
                for xz in range(len(listinha)):
                    if (int(listinha[zx][1])==int(listinha[xz][1]) and zx!=xz and trocou==0):
                        
                        if int(listinha[zx][3])>int(listinha[xz][3]):
                            aa=listinha[zx]
                            bb=listinha[xz]
                            del listinha[zx]
                            listinha.insert(zx,aa)
                            del listinha[xz]
                            listinha.insert(xz,bb)
                        if int(listinha[zx][3])<int(listinha[xz][3]):
                            aa=listinha[xz]
                            bb=listinha[zx]
                            del listinha[zx]
                            listinha.insert(zx,aa)
                            del listinha[xz]
                            listinha.insert(xz,bb)
                            trocou+=1
                            break
                        break

    i.pop()
    i.append(listinha)
nfc2=[]
afc2=[]
champsnfc2=[]
losnfc2=[]
champsafc2=[]
losafc2=[]


for i in PredS:
    if i [0][0]=="NFC":
        for k in i[1]:
            if k==i[1][0]:
                champsnfc2.append(k)
            else:
                losnfc2.append(k)
    if i[0][0]=="AFC":
        for l in i[1]:
            if l==i[1][0]:    
                champsafc2.append(l)
            else:
                losafc2.append(l)

littlechampsafc2=[]
for i in champsafc2:
    littlechampsafc2.append(i[1])
            
for i in range(1):
    mae=0
    trocou=0
    listinha=[]
    while mae<4:
        for l in range(0,len(champsafc2)):
            if len(listinha)<4:
                if (champsafc2[l][1]==max(littlechampsafc2) and champsafc2[l] not in listinha):
                    listinha.append(champsafc2[l])
                    littlechampsafc2.remove(max(littlechampsafc2))
                    break
                mae+=1
    for u in champsafc2:
        if u not in listinha:
            listinha.append(u)
    while trocou<300:
        for zx in range(len(listinha)):
            for xz in range(len(listinha)):
                if (int(listinha[zx][1])==int(listinha[xz][1]) and zx!=xz):
                    if (listinha[zx][3]<listinha[xz][3] and xz>zx):
                        aa=listinha[xz]
                        bb=listinha[zx]
                        del listinha[zx]
                        listinha.insert(zx,aa)
                        del listinha[xz]
                        listinha.insert(xz,bb)
                        trocou+=1
                    else:
                        trocou+=4000
                else:
                    trocou+=4000
champsafc2=[]
for i in listinha:
    champsafc2.append(i)
littlechampsnfc2=[]
for i in champsnfc2:
    littlechampsnfc2.append(i[1])
            
for i in range(1):
    mae=0
    trocou=0
    listinha=[]
    while mae<4:
        for l in range(0,len(champsnfc2)):
            if len(listinha)<4:
                if (champsnfc2[l][1]==max(littlechampsnfc2) and champsnfc2[l] not in listinha):
                    listinha.append(champsnfc2[l])
                    littlechampsnfc2.remove(max(littlechampsnfc2))
                    break
                mae+=1
    for u in champsnfc2:
        if u not in listinha:
            listinha.append(u)
    
    while trocou<300:
        for zx in range(len(listinha)):
            for xz in range(len(listinha)):
                if (int(listinha[zx][1])==int(listinha[xz][1]) and zx!=xz):
                    if (listinha[zx][3]<listinha[xz][3] and xz>zx):
                        aa=listinha[xz]
                        bb=listinha[zx]
                        del listinha[zx]
                        listinha.insert(zx,aa)
                        del listinha[xz]
                        listinha.insert(xz,bb)
                        trocou+=1
                    else:
                        trocou+=4000
                else:
                    trocou+=4000
champsnfc2=[]
for i in listinha:
    champsnfc2.append(i)
    
littlelosnfc2=[]
for i in losnfc2:
    littlelosnfc2.append(i[1])
            
for i in range(1):
    mae=0
    trocou=0
    listinha=[]
    while mae<1000:
        for l in range(0,len(losnfc2)):
            if len(listinha)<12:
                if (losnfc2[l][1]==max(littlelosnfc2) and losnfc2[l] not in listinha):
                    listinha.append(losnfc2[l])
                    littlelosnfc2.remove(max(littlelosnfc2))
                    break
                mae+=1
            if len(listinha)==12:
                mae+=404040404
    for u in losnfc2:
        if u not in listinha:
            listinha.append(u)
    while trocou<300:
        for zx in range(len(listinha)):
            for xz in range(len(listinha)):
                if (int(listinha[zx][1])==int(listinha[xz][1]) and zx!=xz):
                    if (listinha[zx][3]<listinha[xz][3] and xz>zx):
                        aa=listinha[xz]
                        bb=listinha[zx]
                        del listinha[zx]
                        listinha.insert(zx,aa)
                        del listinha[xz]
                        listinha.insert(xz,bb)
                        trocou+=1
                    else:
                        trocou+=4000
                else:
                    trocou+=4000
losnfc2=[]
for i in listinha:
    losnfc2.append(i)
    
littlelosafc2=[]
for i in losafc2:
    littlelosafc2.append(i[1])
            
for i in range(1):
    mae=0
    trocou=0
    listinha=[]
    while mae<1000:
        for l in range(0,len(losafc2)):
            if len(listinha)<12:
                if (losafc2[l][1]==max(littlelosafc2) and losafc2[l] not in listinha):
                    listinha.append(losafc2[l])
                    littlelosafc2.remove(max(littlelosafc2))
                    break
                mae+=1
            if len(listinha)==12:
                mae+=404040404
    for u in losafc2:
        if u not in listinha:
            listinha.append(u)
    while trocou<300:
        for zx in range(len(listinha)):
            for xz in range(len(listinha)):
                if (int(listinha[zx][1])==int(listinha[xz][1]) and zx!=xz):
                    if (listinha[zx][3]<listinha[xz][3] and xz>zx):
                        aa=listinha[xz]
                        bb=listinha[zx]
                        del listinha[zx]
                        listinha.insert(zx,aa)
                        del listinha[xz]
                        listinha.insert(xz,bb)
                        trocou+=1
                    else:
                        trocou+=4000
                else:
                    trocou+=4000
losafc2=[]
for i in listinha:
    losafc2.append(i)
    
afc2.append(champsafc2)
afc2.append(losafc2)
nfc2.append(champsnfc2)
nfc2.append(losnfc2)

Nfc2=[]
Afc2=[]

for i in nfc2:
    for k in i:
        Nfc2.append(k)
        
for i in afc2:
    for k in i:
        Afc2.append(k)
        
nfc=[]
afc=[]
champsnfc=[]
losnfc=[]
champsafc=[]
losafc=[]


for i in Standings2:

    if i [0][0]=="NFC":
        for k in i[1]:
            if k==i[1][0]:
                champsnfc.append(k)
            else:
                losnfc.append(k)
    if i[0][0]=="AFC":
        for l in i[1]:
            if l==i[1][0]:    
                champsafc.append(l)
            else:
                losafc.append(l)

littlechampsafc=[]
for i in champsafc:
    littlechampsafc.append(i[1])
            
for i in range(1):
    mae=0
    trocou=0
    listinha=[]
    while mae<4:
        for l in range(0,len(champsafc)-1):
            if len(listinha)<4:
                if (champsafc[l][1]==max(littlechampsafc) and champsafc[l] not in listinha):
                    listinha.append(champsafc[l])
                    littlechampsafc.remove(max(littlechampsafc))
                    break
                mae+=1
    for u in champsafc:
        if u not in listinha:
            listinha.append(u)
    while trocou<300:
        for zx in range(len(listinha)):
            for xz in range(len(listinha)):
                if (int(listinha[zx][1])==int(listinha[xz][1]) and zx!=xz):
                    if (listinha[zx][3]<listinha[xz][3] and xz>zx):
                        aa=listinha[xz]
                        bb=listinha[zx]
                        del listinha[zx]
                        listinha.insert(zx,aa)
                        del listinha[xz]
                        listinha.insert(xz,bb)
                        trocou+=1
                    else:
                        trocou+=4000
                else:
                    trocou+=4000
champsafc=[]
for i in listinha:
    champsafc.append(i)
littlechampsnfc=[]
for i in champsnfc:
    littlechampsnfc.append(i[1])
            
for i in range(1):
    mae=0
    trocou=0
    listinha=[]
    while mae<4:
        for l in range(0,len(champsnfc)-1):
            if len(listinha)<4:
                if (champsnfc[l][1]==max(littlechampsnfc) and champsnfc[l] not in listinha):
                    listinha.append(champsnfc[l])
                    littlechampsnfc.remove(max(littlechampsnfc))
                    break
                mae+=1
    for u in champsnfc:
        if u not in listinha:
            listinha.append(u)
    
    while trocou<300:
        for zx in range(len(listinha)):
            for xz in range(len(listinha)):
                if (int(listinha[zx][1])==int(listinha[xz][1]) and zx!=xz):
                    if (listinha[zx][3]<listinha[xz][3] and xz>zx):
                        aa=listinha[xz]
                        bb=listinha[zx]
                        del listinha[zx]
                        listinha.insert(zx,aa)
                        del listinha[xz]
                        listinha.insert(xz,bb)
                        trocou+=1
                    else:
                        trocou+=4000
                else:
                    trocou+=4000
champsnfc=[]
for i in listinha:
    champsnfc.append(i)
    
littlelosnfc=[]
for i in losnfc:
    littlelosnfc.append(i[1])
            
for i in range(1):
    mae=0
    trocou=0
    listinha=[]
    while mae<1000:
        for l in range(0,len(losnfc)):
            if len(listinha)<12:
                if (losnfc[l][1]==max(littlelosnfc) and losnfc[l] not in listinha):
                    listinha.append(losnfc[l])
                    littlelosnfc.remove(max(littlelosnfc))
                    break
                mae+=1
            if len(listinha)==12:
                mae+=404040404
    for u in losnfc:
        if u not in listinha:
            listinha.append(u)
    while trocou<300:
        for zx in range(len(listinha)):
            for xz in range(len(listinha)):
                if (int(listinha[zx][1])==int(listinha[xz][1]) and zx!=xz):
                    if (listinha[zx][3]<listinha[xz][3] and xz>zx):
                        aa=listinha[xz]
                        bb=listinha[zx]
                        del listinha[zx]
                        listinha.insert(zx,aa)
                        del listinha[xz]
                        listinha.insert(xz,bb)
                        trocou+=1
                    else:
                        trocou+=4000
                else:
                    trocou+=4000
losnfc=[]
for i in listinha:
    losnfc.append(i)
    
littlelosafc=[]
for i in losafc:
    littlelosafc.append(i[1])
            
for i in range(1):
    mae=0
    trocou=0
    listinha=[]
    while mae<1000:
        for l in range(0,len(losafc)):
            if len(listinha)<12:
                if (losafc[l][1]==max(littlelosafc) and losafc[l] not in listinha):
                    listinha.append(losafc[l])
                    littlelosafc.remove(max(littlelosafc))
                    break
                mae+=1
            if len(listinha)==12:
                mae+=404040404
    for u in losafc:
        if u not in listinha:
            listinha.append(u)
    while trocou<300:
        for zx in range(len(listinha)):
            for xz in range(len(listinha)):
                if (int(listinha[zx][1])==int(listinha[xz][1]) and zx!=xz):
                    if (listinha[zx][3]<listinha[xz][3] and xz>zx):
                        aa=listinha[xz]
                        bb=listinha[zx]
                        del listinha[zx]
                        listinha.insert(zx,aa)
                        del listinha[xz]
                        listinha.insert(xz,bb)
                        trocou+=1
                    else:
                        trocou+=4000
                else:
                    trocou+=4000
losafc=[]
for i in listinha:
    losafc.append(i)
    
afc.append(champsafc)
afc.append(losafc)
nfc.append(champsnfc)
nfc.append(losnfc)

Nfc=[]
Afc=[]

for i in nfc:
    for k in i:
        Nfc.append(k)
        
for i in afc:
    for k in i:
        Afc.append(k)
versus=[]
timeusuario=["Green Bay Packers"] # escolha do time
for i in Agendas:
    if i[0]==timeusuario:
        for k in i:
            if k!=i[0] and k!=i[2]: # análise do time
                versus.append(k) # salva os times que irão enfrentar o time escolhido nessa lista
meutime=[]
for i in Times:
    if timeusuario[0]==i[0][0]: #salva as informações importantes do time escolhido
        meutime.append([i[0][2],i[0][3],i[0][6],i[1][0]])
        
for i in Standings2:
    if i[0]==[meutime[0][0],meutime[0][1]]:
        for k in i[1]:
            if k[0]==timeusuario[0]:
                meutime.append([int(k[1]),int(k[2]),int(k[3])])
for i in PredS:
    if i[0]==[meutime[0][0],meutime[0][1]]:
        for k in i[1]:
            if k[0]==timeusuario[0]:
                meutime.append([int(k[1]),int(k[2]),int(k[3])])                
                
passei=0
wildcard=0
if meutime[0][0]=="NFC":
    for i in nfc:
        if i == nfc[0]:
            for k in i:
                if k[0]==timeusuario[0]:
                    passei=1
        if i == nfc[1]:
            for l in i:
                if l==i[0] or l==i[0]:
                    if l[0]==timeusuario[0]:
                        wildcard=1
if meutime[0][0]=="AFC":
    for i in afc:
        if i == afc[0]:
            for k in i:
                if k[0]==timeusuario[0]:
                    passei=1
        if i == afc[1]:
            for l in i:
                if l==i[0] or l==i[0]:
                    if l[0]==timeusuario[0]:
                        wildcard=1
                        
semana=meutime[1][0]+meutime[1][1]+meutime[1][2]
ameaça=['Detroit Lions']
for i in Vitorias:
    for k in range(len(i[1])):
        if k==i[1][0]:
            i.append
#if passei==1:
#    for i in Standings2:
#        
        
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
            if k[0]==timeusuario[0]:
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
            
quantasvit=2 #quantas vitórias são necessárias para ir para os playoffs
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
        
for i in quebonito:
    print(i)


        
        
    