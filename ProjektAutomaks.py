import tkinter as tk

#Järgnev funktsioon eeldab, et co2 mõõtmiseks on kasutatud WLTP-d
def arvuta_aastamaks_tavasõiduauto(EVbool, autoaasta, mootortoomaht, mootorvoimsus, co2, taismass): #(True/False, aasta, cm3, kW, g/km, kg)
    import datetime
    baasosa = 50
    
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
        if co2 != '':
            if co2 >= 118 and co2 <= 150:
                temparv += (co2 - 117) * 3
            elif co2 >= 151 and co2 <= 200:
                temparv += (150-117) * 3 + (co2 - 150) * 3.5
            elif co2 >= 201:
                temparv += (150-117) * 3 + (200 - 150) * 3.5 + (co2 - 200) * 4
            temparv = (temparv + massiosa) * vanusekordaja + baasosa
            return temparv
        elif co2 == '':
            temparv = (mootortoomaht * 0.05 + mootorvoimsus * 0.8 + massiosa) * vanusekordaja + baasosa
            return temparv
    elif EVbool:
        temparv = massiosa * vanusekordaja + baasosa
        return temparv
    
aken = tk.Tk()

info = tk.Label(
    text='Pythoni projekti jaoks loodud auto aastamaksu kalkulaator.\nHetkel suudab kalkulaator arvutada tavalise sõiduauto aastamaksu.',
    width = 80,
    height = 4)
info.pack()

EVboolsisend = tk.Label(
    text='Kas auto on elektriauto? (Jah/Ei)')
EVboolsisend.pack()

EVboolsisendvali = tk.Entry(
    width = 10)
EVboolsisendvali.pack()

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

TaisMass = tk.Label(text='Mis on auto täismass(kg)?')
TaisMass.pack()

TaisMasssisendvali = tk.Entry(width = 10)
TaisMasssisendvali.pack()

tyhik = tk.Label(
    text='-',
    height=2,
    width = 70)
tyhik.pack()

def arvutusnupp():
    EVboolsisendvalitoodeldud = bool()
    if EVboolsisendvali.get() == 'Jah':
        EVboolsisendvalitoodeldud = True
    else: EVboolsisendvalitoodeldud = False
    if MootorToomahtsisendvali.get() == '': MootorToomahtsisendvali.insert(0, '0')
    if MootorVoimsussisendvali.get() == '': MootorVoimsussisendvali.insert(0, '0')
    if CO2sisendvali.get() == '': CO2sisendvali.insert(0, '0')
    tulemus = arvuta_aastamaks_tavasõiduauto(EVboolsisendvalitoodeldud, int(AutoAastasisendvali.get()), int(MootorToomahtsisendvali.get()), int(MootorVoimsussisendvali.get()), int(CO2sisendvali.get()), int(TaisMasssisendvali.get()))
    Tulemus = tk.Label(text='Automaks on ' + str(tulemus) + ' eurot aastas', height=2)
    Tulemus.pack()
    
    
arvutanupp = tk.Button(
    text='Arvuta aastamaks',
    width=15,
    height=2,
    bg='gray',
    command=arvutusnupp)
arvutanupp.pack()


aken.mainloop()