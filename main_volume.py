# main
def main():
    pilih = input('Pilih Volume Bangun Ruang Apa? [Kubus, Balok] ')
    if pilih == 'Kubus':
        print("\nVolume Kubus Adalah:  ", kubus().volume_kubus())
    else:
        print("\nVolume Balok Adalah:  ", balok().Volume_balok())

# run program
if __name__ == "__main__":
    main()