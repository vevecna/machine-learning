# Machine Learning

Projeto de estudos de Machine Learning com Python, focado em classificação usando Árvores de Decisão (Decision Trees).

## Estrutura do Projeto

```
├── dados/               # Datasets utilizados (.xlsx, .parquet)
├── cerveja.py           # Classificação de cervejas
├── frutas.py            # Classificação de frutas
└── .gitignore
```

## Projetos

### Classificação de Frutas (`frutas.py`)

Modelo de árvore de decisão que classifica frutas (Morango, Limão, Pera, Banana, Cereja, Tomate, Maçã) com base em características como:

- Arredondada
- Suculenta
- Vermelha
- Doce

Utiliza `predict` para prever a classe e `predict_proba` para exibir a probabilidade de cada fruta.

### Classificação de Cervejas (`cerveja.py`)

Modelo de árvore de decisão que classifica tipos de cerveja com base em:

- Temperatura
- Tipo de copo (mud/pint)
- Espuma (sim/não)
- Cor (clara/escura)

Inclui visualização da árvore gerada com `matplotlib`.

## Tecnologias

- Python
- Pandas
- Scikit-learn (Decision Tree)
- Matplotlib
