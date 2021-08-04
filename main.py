import pymssql
import numpy as np
from matplotlib import pyplot as plt
# sin numpy
numeros=range(1,10)   # 1..10
resultado=[]
for numero in numeros:
    resultado.append(numero*2)

# con numpy
x: np.ndarray = np.arange(1,11) # 1..10
y = x*2 # ???




conn = pymssql.connect("104.36.110.17", "alumno", "Bestapple5520", "MilkCo")

cursor: pymssql.Cursor = conn.cursor(as_dict=True)

cursor.execute("select top(10) sku,name,unitprice from skus")


todos=cursor.fetchall()

ejesx=[]
ejesy=[]
for prod in todos:
    print("id:{0},nombre={1},precio={2}"
          .format(prod.get('sku'),prod.get('name'),prod.get('unitprice')))
    ejesx.append(prod.get('sku'))
    ejesy.append(prod.get('unitprice'))


fig=plt.figure()
# ax = fig.add_axes([0,0,1,1])
plt.bar(ejesx,ejesy)
plt.xticks(ejesx, ejesy)
plt.show()



cursor.close()
conn.close()




