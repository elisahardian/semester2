# ARRAY
#menggunakan perintah : Nama_array=np.array([])

import numpy as np
print("----array 1 dimensi-----")
a= np.array([50 , 30, 60.43, 'ani']) #ini akan menjadi string
print(a)

import numpy as np
print("----array 1 dimensi-----")
a= np.array([50 , 30, 60.43, 89.0]) #ini akan menjad float
print(a)

#array 2 dimensi
import numpy as np
print("----array 2 dimensi-----")
a = np.array([[50, 30, 60, 45], [150, 230, 600, 450]])
print(a)

#array 3 dimensi
import numpy as np
print("----array 3 dimensi-----")
a = np.array([[[50, 30, 60, 45], [150, 230, 600, 450], [233, 211, 547, 903]]])
print(a)

#array n dimensi
import numpy as np
print("----array n dimensi-----")
a= np.array([50 , 30, 60.43, 89.0], ndmin=4) 
print(a)
print("array ini berdimensi: ", a.ndim)

