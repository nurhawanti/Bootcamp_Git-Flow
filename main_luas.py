# main
def main():
    pilih = input('Pilih Luas Bangun Ruang Apa? [Kubus, Balok] ')
    if pilih == 'Kubus':
        print("\nLuas Kubus Adalah:  ", kubus().luas_kubus())
    else:
        print("\nLuas Balok Adalah:  ", balok().luas_balok())

# run program
if __name__ == "__main__":
    main()