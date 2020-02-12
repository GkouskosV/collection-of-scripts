
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import cx_Oracle

dsn_tns = cx_Oracle.makedsn('localhost','1521', service_name='xe')
conn = cx_Oracle.connect(user=r'USER', password='MY_PASS', dsn=dsn_tns)
c = conn.cursor()
qry_a = c.execute("SELECT foodid,proteins,carbs,fats FROM foods")
rows_a = c.fetchall()
df = pd.DataFrame(rows_a, columns=['ID','Proteins','Carbs','Fats'])
df = df.drop(['ID'], axis=1)

pca_ = PCA(n_components=3)
x_fit_pca = pca_.fit_transform(df)
kmeans_PCA = KMeans(n_clusters=4, init='k-means++', max_iter= 300, n_init= 10, random_state= 3)
y_kmeans = kmeans_PCA.fit_predict(x_fit_pca)

qry_b = c.execute("SELECT foodid, dietary_value FROM foods WHERE dietary_value is null")
rows_b = c.fetchall()

temp = [item[0] for item in rows_a]
temp = list(zip(temp,y_kmeans))

data = []
for i in range(len(temp)):
    for j in range(len(rows_b)):
        if temp[i][0] == rows_b[j][0]:
            data.append(temp[i])

for i in range(len(data)):    
    c.execute("UPDATE foods SET dietary_value = :dv WHERE foodid = :id", dv=data[i][1].astype(float),id=data[i][0])

conn.commit()
c.close()
conn.close()
