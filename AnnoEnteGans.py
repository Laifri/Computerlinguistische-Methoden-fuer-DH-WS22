from sklearn.metrics import cohen_kappa_score

anno1 = []
anno2 = []

for i in range(60):
    anno1.append("Ente")
    anno2.append("Ente")

for i in range(15):
    anno1.append("Ente")
    anno2.append("Gans")

for i in range(10):
    anno1.append("Gans")
    anno2.append("Ente")

for i in range(15):
    anno1.append("Gans")
    anno2.append("Gans")

print(cohen_kappa_score(anno1, anno2))