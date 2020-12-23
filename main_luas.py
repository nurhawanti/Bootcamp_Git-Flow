# main
def main():
    pilih = input('Pilih Luas Bangun Ruang Apa? [Kubus, Prisma Segitiga] ')
    if pilih == 'Kubus':
        print("\nLuas Kubus Adalah:  ", kubus().luas_kubus())
    else:
        print("\nLuas Prisma Segitiga Adalah:  ", prisma_segitiga().luas_prisma_segitiga())

# run program
if __name__ == "__main__":
    main()