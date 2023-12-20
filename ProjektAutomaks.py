import tkinter as tk
import datetime

#Järgnev funktsioon eeldab, et co2 mõõtmiseks on kasutatud WLTP-d
def arvuta_aastamaks_tavasõiduauto(EVbool, autoaasta, mootortoomaht, mootorvoimsus, co2, taismass): #(True/False, aasta, cm3, kW, g/km, kg)

    baasosa = 50
    try:
        autovanus = datetime.datetime.today().year - autoaasta
        vanusekordaja = 1
        if autovanus >= 5 and autovanus <= 14:
            vanusekordaja = 1 - 0.09 * (autovanus - 4)
        elif autovanus > 14 and autovanus <= 20:
            vanusekordaja = 0.1
        elif autovanus > 20:
            vanusekordaja = 0

        massiosa = 0
        if not EVbool:
            if taismass > 2000 and ((taismass - 2000) * 0.4) <= 400:
                massiosa = (taismass - 2000) * 0.4
            elif taismass > 2000 and ((taismass - 2000) * 0.4) >= 400:
                massiosa = 400
        elif EVbool:
            if taismass > 2400 and ((taismass - 2400) * 0.4) <= 440:
                massiosa = (taismass - 2400) * 0.4
            elif taismass > 2400 and ((taismass - 2400) * 0.4) >= 440:
                massiosa = 440
            
            
        temparv = 0
        if not EVbool:
            if co2 != 0:
                if co2 >= 118 and co2 <= 150:
                    temparv += (co2 - 117) * 3
                elif co2 >= 151 and co2 <= 200:
                    temparv += (150-117) * 3 + (co2 - 150) * 3.5
                elif co2 >= 201:
                    temparv += (150-117) * 3 + (200 - 150) * 3.5 + (co2 - 200) * 4
                temparv = (temparv + massiosa) * vanusekordaja + baasosa
                return temparv
            elif co2 == 0:
                temparv = (mootortoomaht * 0.05 + mootorvoimsus * 0.8 + massiosa) * vanusekordaja + baasosa
                return temparv
        elif EVbool:
            temparv = massiosa * vanusekordaja + baasosa
            return temparv
    except: return None

def arvuta_aastamaks_kaubik(EVbool, autoaasta, mootortoomaht, mootorvoimsus, co2):
    baasosa = 50
    try:
        autovanus = datetime.datetime.today().year - autoaasta
        vanusekordaja = 1
        if autovanus >= 5 and autovanus <= 14:
            vanusekordaja = 1 - 0.09 * (autovanus - 4)
        elif autovanus > 14 and autovanus <= 20:
            vanusekordaja = 0.1
        elif autovanus > 20:
            vanusekordaja = 0
        
        temparv = 0
        if not EVbool:
            if co2 != 0:
                if co2 >= 205 and co2 <= 250:
                    temparv += (co2 - 204) * 3
                elif co2 >= 251 and co2 <= 300:
                    temparv += (250-204) * 3 + (co2 - 250) * 3.5
                elif co2 >= 301:
                    temparv += (250-204) * 3 + (300 - 250) * 3.5 + (co2 - 300) * 4
                temparv = temparv * vanusekordaja + baasosa
                return temparv
            elif co2 == 0:
                temparv = (mootortoomaht * 0.05 + mootorvoimsus * 0.8) * vanusekordaja + baasosa
                return temparv
        elif EVbool:
            return 30
    except: return None

#print((arvuta_aastamaks_tavasõiduauto(False, 2019, 0, 0, 299, 2860)))
#print((arvuta_aastamaks_tavasõiduauto(False, 2019, 0, 0, 221, 2850)))
#print((arvuta_aastamaks_tavasõiduauto(False, 2019, 0, 0, 196, 2350)))

#print((arvuta_aastamaks_kaubik(False, 2020, 0, 0, 150)))
#print((arvuta_aastamaks_kaubik(False, 2020, 0, 0, 247)))
#print((arvuta_aastamaks_kaubik(False, 2022, 0, 0, 235)))

aken = tk.Tk()

info = tk.Label(
    text='Pythoni projekti jaoks loodud auto aastamaksu kalkulaator.\nHetkel suudab kalkulaator arvutada tavalise sõiduauto ja kaubiku aastamaksu.',
    width = 80,
    height = 4)
info.pack()

AutoTüüp = tk.Label(
    text='Kas soovite arvutada sõiduauto või kaubiku aastamaksu?')
AutoTüüp.pack()

AutoTüüpsisendmuutuja = tk.StringVar()
AutoTüüpsisendradio1 = tk.Radiobutton(text='Sõiduauto', variable=AutoTüüpsisendmuutuja, value='sõiduauto')
AutoTüüpsisendradio2 = tk.Radiobutton(text='Kaubik', variable=AutoTüüpsisendmuutuja, value='kaubik')
AutoTüüpsisendradio1.pack()
AutoTüüpsisendradio2.pack()

tyhik = tk.Label(
    text='-',
    height=2,
    width = 70)
tyhik.pack()

EVboolsisend = tk.Label(
    text='Kas auto on elektriauto?')
EVboolsisend.pack()

EVboolsisendmuutuja = tk.IntVar()
EVboolsisendradio1 = tk.Radiobutton(text="Jah", variable=EVboolsisendmuutuja, value=1)
EVboolsisendradio2 = tk.Radiobutton(text='Ei', variable=EVboolsisendmuutuja, value=0)
#EVboolsisendvali = tk.Entry(
#    width = 10)
EVboolsisendradio1.pack()
EVboolsisendradio2.pack()

tyhik = tk.Label(
    text='-',
    height=2,
    width = 70)
tyhik.pack()

AutoAasta = tk.Label(text='Mis aastal on auto toodetud?')
AutoAasta.pack()

AutoAastasisendvali = tk.Entry(width = 10)
AutoAastasisendvali.pack()

tyhik = tk.Label(
    text='-',
    height=2,
    width = 70)
tyhik.pack()


MootorToomaht = tk.Label(text='Mis on auto mootori töömaht(cm3)? NB! Seda välja ei pea täitma, kui on teada CO2 heitmeid.')
MootorToomaht.pack()

MootorToomahtsisendvali = tk.Entry(width = 10)
MootorToomahtsisendvali.pack()

tyhik = tk.Label(
    text='-',
    height=2,
    width = 70)
tyhik.pack()

MootorVoimsus = tk.Label(text='Mis on mootori võimsus(kW)? NB! Seda välja ei pea täitma, kui on teada CO2 heitmeid.')
MootorVoimsus.pack()

MootorVoimsussisendvali = tk.Entry(width = 10)
MootorVoimsussisendvali.pack()

tyhik = tk.Label(
    text='-',
    height=2,
    width = 70)
tyhik.pack()

CO2 = tk.Label(text='Mis on CO2 heitmete arv(g/km)? Kalkulaator eeldab, et kasutate WLTP standardit.')
CO2.pack()

CO2sisendvali = tk.Entry(width = 10)
CO2sisendvali.pack()

tyhik = tk.Label(
    text='-',
    height=2,
    width = 70)
tyhik.pack()

TaisMass = tk.Label(text='Mis on auto täismass(kg)? NB! Kaubiku puhul seda pole vaja.')
TaisMass.pack()

TaisMasssisendvali = tk.Entry(width = 10)
TaisMasssisendvali.pack()

tyhik = tk.Label(
    text='-',
    height=2,
    width = 70)
tyhik.pack()

def arvutusnupp():
#    EVboolsisendvalitoodeldud = bool()
#    if EVboolsisendvali.get() == 'Jah':
#        EVboolsisendvalitoodeldud = True
#    else: EVboolsisendvalitoodeldud = False
    if AutoAastasisendvali.get() == '': AutoAastasisendvali.insert(0, '0')
    if TaisMasssisendvali.get() == '': TaisMasssisendvali.insert(0, '0')
    if MootorToomahtsisendvali.get() == '': MootorToomahtsisendvali.insert(0, '0')
    if MootorVoimsussisendvali.get() == '': MootorVoimsussisendvali.insert(0, '0')
    if CO2sisendvali.get() == '': CO2sisendvali.insert(0, '0')
    print(AutoTüüpsisendmuutuja.get())
    if AutoTüüpsisendmuutuja.get() == 'sõiduauto' and AutoAastasisendvali.get() != 0:
        tulemus = arvuta_aastamaks_tavasõiduauto(EVboolsisendmuutuja.get(), int(AutoAastasisendvali.get()), int(MootorToomahtsisendvali.get()), int(MootorVoimsussisendvali.get()), int(CO2sisendvali.get()), int(TaisMasssisendvali.get()))
        if tulemus != None: Tulemus = tk.Label(text='Automaks on ' + str(tulemus) + ' eurot aastas', height=2)
        else: Tulemus = tk.Label(text='Sisestatud andmed on puudulikud', height=2)
    elif AutoTüüpsisendmuutuja.get() == 'kaubik' and AutoAastasisendvali.get() != 0:
        tulemus = arvuta_aastamaks_kaubik(EVboolsisendmuutuja.get(), int(AutoAastasisendvali.get()), int(MootorToomahtsisendvali.get()), int(MootorVoimsussisendvali.get()), int(CO2sisendvali.get()))
        if tulemus != None: Tulemus = tk.Label(text='Automaks on ' + str(tulemus) + ' eurot aastas', height=2)
        else: Tulemus = tk.Label(text='Sisestatud andmed on puudulikud', height=2)
    else: Tulemus = tk.Label(text='Sisestatud andmed on puudulikud', height=2)
    Tulemus.pack()
    
    
arvutanupp = tk.Button(
    text='Arvuta aastamaks',
    width=15,
    height=2,
    bg='gray',
    command=arvutusnupp)
arvutanupp.pack()


aken.mainloop()