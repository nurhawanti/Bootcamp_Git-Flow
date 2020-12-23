# main
def main():
    pilih = input('Pilih Volume Bangun Ruang Apa? [Kubus, Prisma Segitiga] ')
    if pilih == 'Kubus':
        print("\nVolume Kubus Adalah:  ", kubus().volume_kubus())
    else:
        print("\nVolume Prisma Segitiga Adalah:  ", prisma_segitiga().Volume_prisma_segitiga())

# run program
if __name__ == "__main__":
    main()