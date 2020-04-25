# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# jika saya rank ke 0 maka saya akan mengirimkan pesan ke proses yang mempunyai rank 1 s.d size
if rank == 0:
    x = ("rank = ",rank,"size = ",size)
    comm.send(x, dest=1, tag=11)
    comm.send(x, dest=2, tag=11)
    comm.send(x, dest=3, tag=11)
    
# jika saya bukan rank 0 maka saya menerima pesan yang berasal dari proses dengan rank 0
else:
    print("receiving rank ",rank)
    y = comm.recv(source=0, tag=11)
    print("x = ",y)
    print("rank = ",rank)
    print("total size = ",size)
    print("received by rank ",rank)