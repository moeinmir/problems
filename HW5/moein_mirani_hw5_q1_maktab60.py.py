import pandas as pd
d=pd.read_csv("data.csv")
d2=d[["a","c","b"]]
d2.to_csv("data.csv")
d["d"]=d["a"]+d["b"]+d["c"]

