# membuat fungsi TSP dengan menggunakan Dynamic Programming
def tsp_dp(graph):
    n = len(graph)
    # membuat tabel memoisasi (caching), dengan batas infinity (takterbatas)
    memo = [[float('inf')] * (1 << n) for _ in range(n)]

    # membuat fungsi dynamic programming, dan penandaan node 
    # yang sudah dikunjungi dengan bitmask(mask)
    def dp(node, mask):

        # pada best case.
        # jika mask (penandaan kota yang sudah dikunjungi) bernilai sama dengan 1, 
        # maka akan kembali ke starting node,dan menandakan semua node sudah terkunjungi
        if mask == (1 << n) - 1: # operasi menggeser bit 1 sebanyak n kali
            return graph[node][0]  # kembali ke starting node

        # jika hasil perhitungan untuk node dan mask tertentu sudah ada, 
        # (tidak sama dengan nilai infinity yang belum diketahui)
        # maka akan kembali ke perhitungan tersebut. menghindari perhitungan berulang.
        if memo[node][mask] != float('inf'):
            return memo[node][mask] 

        # loop perhitungan node selanjutnya ke semua node yang belum dikunjungi
        for next_node in range(n):
            # Ini adalah kondisi yang memeriksa apakah next_node belum dikunjungi 
            # (belum ada dalam mask).
            # jika 'penanda (mask) yang digeser ke kanan sebanyak next_node kali 
            #-dan sama dengan 1' hasilnya sama dengan 0 (belum dikunjungi), maka
            if (mask >> next_node) & 1 == 0:  
                # menambahkan data baru untuk tabel memoisasi. 
                # dengan melakukan perhitungan rekursif, menggunakan bitmask
                memo[node][mask] = min(
                    memo[node][mask],
                    graph[node][next_node] + dp(next_node, mask | (1 << next_node))
                )
        # mengembalikan nilai yang sudah diperhitungkan tadi
        return memo[node][mask]
    # mengembalikan hasil fungsi dp dengan node awal keberangkatan (0), 
    # dan catatan mask 1 (kota awal yang sudah dikunjungi)
    return dp(0, 1)

# n merupakan banyak node
n= int(input(""))
# untuk membuat matrix nya, dengan setiap elemen dipisahkan dengan spasi
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# menampilkan perhitungan Traveling Salesman Problem
shortest_tour_cost = tsp_dp(matrix)
print(shortest_tour_cost)
