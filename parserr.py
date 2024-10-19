import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")
parser.add_argument('-t', '--tanggallahir',required=True, type=int, help='Maukkan tanggal lahir Anda')
args = parser.parse_args()
 

if args.tanggallahir < 30:
    print("Terima kasih telah menggunakan panggildicoding.py, kakak "+args.nama)
else:
    print("Terima kasih telah menggunakan panggildicoding.py, "+args.nama)
