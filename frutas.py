# %%

import pandas as pd

df = pd.read_excel("dados/dados_frutas.xlsx")

df

# %%
from sklearn import tree

# atributo random_state não permite que o DecisionTreeClassifier tome decisões aleatórias
# isso é uma seed uma semente
arvore = tree.DecisionTreeClassifier(random_state=42)


'''
Variável resposta (y) → aquilo que você quer que o modelo aprenda a prever a partir das características acima. No seu caso: Fruta — o nome/classe da fruta (Morango, Limão, Pera, Banana, Cereja, Tomate, Maçã).

'''

# %%
y = df['Fruta']

caracteristicas = ['Arredondada', 'Suculenta', 'Vermelha', 'Doce']

X = df[caracteristicas]


# %%
# caracteristicas estão na variavel x 
X



# vamos ensinar a maquina

# %%
arvore.fit(X, y)

# %%
arvore.predict([[0,0,0,0]])


# %%
import matplotlib.pyplot as plt

plt.figure(dpi=400)

tree.plot_tree(arvore, 
               feature_names=caracteristicas,
               class_names=arvore.classes_, 
               filled=True)
# %%
proba = arvore.predict_proba([[1,1,1,1]])[0]
pd.Series(proba, index=arvore.classes_)
# %%
