# import mpi4py
from mpi4py import MPI

# import library random untuk generate angka integer secara random
import random

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# generate angka integer secara random untuk setiap proses
random_int = random.randint(1,8)

# jika saya adalah proses dengan rank 0 maka:
# saya menerima nilai dari proses 1 s.d proses dengan rank terbesar
# menjumlah semua nilai yang didapat (termasuk nilai proses saya)
if rank == 0:
    sum = 0
    for i in range(1,size):
        print("penerimaan data ke ",i)
        data_recv = comm.recv(source=i, tag=11)
        print(data_recv)
        sum = sum + data_recv['send_data']
    print("Jumlah = ",sum)  
# jika bukan proses dengan rank 0, saya akan mengirimkan nilai proses saya ke proses dengan rank=0
else:
    data2 = {'rank': rank,'destination':0,'send_data':random_int}
    comm.send(data2, dest=0, tag=11)