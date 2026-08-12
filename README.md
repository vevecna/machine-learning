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

### Análise de Clones (`dados/dados_clones.parquet`)

**O Problema:** O Conselho Jedi busca entender por que soldados clones estão falhando em combate (sendo classificados como "defeituosos"). O dataset contém mais de 1 milhão de linhas, com dados biométricos (massa, estatura, idade, etc.) e o general Jedi responsável por cada pelotão.

**Análise Inicial vs. Árvore de Decisão:**

- **Análise Bivariada (Descritiva):** Ao analisar apenas a relação entre o general Jedi e o status do clone, a conclusão errônea seria que os generais Yoda e Shakti seriam ineficientes.
- **Árvore de Decisão:** Ao aplicar a árvore de decisão (removendo a variável do general), descobre-se que o problema não é a liderança, mas sim um lote de fabricação com defeito. A árvore identifica cortes precisos em massa e estatura (ex: clones com menos de 83.4kg possuem maior incidência de falhas), mostrando que o perfil do clone é o fator determinante.

**Conclusão:** O caso ilustra como o aprendizado de máquina pode desmentir correlações superficiais em BI, revelando causas raízes que não são visíveis a olho nu ou em análises simples.

## Tecnologias

- Python
- Pandas
- Scikit-learn (Decision Tree)
- Matplotlib
