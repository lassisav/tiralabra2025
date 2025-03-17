import tkinter as tk
from gift_wrapping import gift_wrapping as gw

def main():
    ikkuna = tk.Tk()
    ikkuna.title('Konveksin verhon algoritmit')
    teksti_syote = tk.Label(ikkuna, text="Syötä pisteiden määrä")
    syote = tk.Entry(ikkuna)
    teksti_valinta = tk.Label(ikkuna, text="Valitse algoritmi")
    nappi_wrapping = tk.Button(ikkuna, text = "Gift Wrapping", width=25, command= lambda: dialogi(syote.get(), "Gift Wrapping ", 1))
    nappi_graham = tk.Button(ikkuna, text = "Graham Scan", width=25, command= lambda: dialogi(syote.get(), "Graham Scan ", 2))
    nappi_quickhull = tk.Button(ikkuna, text = "Quickhull", width=25, command= lambda: dialogi(syote.get(), "Quickhull", 3))
    teksti_tyhja = tk.Label(ikkuna, text="")
    nappi_lopeta = tk.Button(ikkuna, text = "Lopeta", width=25, command=ikkuna.destroy)

    teksti_syote.pack()
    syote.pack()
    teksti_valinta.pack()
    nappi_wrapping.pack()
    nappi_graham.pack()
    nappi_quickhull.pack()
    teksti_tyhja.pack()
    nappi_lopeta.pack()

    ikkuna.mainloop()

def dialogi(maara, nimi, numero):
    print("Suoritetaan " + nimi + "-algoritmi " + maara + ":n pisteen joukolle")
    print("Haetaan pisteet.")
    pisteet = pisteiden_haku(maara)
    print("Pisteet haettu!")
    print(pisteet)
    print("Kello käyntiin, laskenta alkaa!")
    print("TODO: Kellotuksen aloitus")
    algoritmin_valinta(pisteet, numero)
    print("TODO: Kellotuksen lopetus")
    print(maara + " pisteellä " + nimi + "-algortimilla meni x millisekuntia. (WIP)")

def pisteiden_haku(maara):
    return [(1, 1), (2, 9), (7, 4), (4, 8), (5, 6), (9, 2), (5, 9), (4, 2), (7, 6)]

def algoritmin_valinta(pisteet, numero):
    match numero:
        case 1:
            gift_wrapping(pisteet)
        case 2:
            graham_scan(pisteet)
        case 3:
            quickhull(pisteet)
    return
        
def gift_wrapping(pisteet):
    print("Ajetaan Gift Wrapping:")
    print(gw(pisteet))

def graham_scan(pisteet):
    print("TODO: Graham scan -algoritmi")

def quickhull(pisteet):
    print("TODO: Quickhull-algoritmi")

if __name__ == "__main__":
    main()