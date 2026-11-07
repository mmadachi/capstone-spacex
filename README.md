# Vencendo a corrida espacial com Ciência de Dados

Projeto final do curso de Ciência de Dados: prever se o primeiro estágio do foguete **Falcon 9** da SpaceX vai pousar com sucesso. Como o custo de um lançamento depende da reutilização desse estágio, a previsão ajuda a estimar o preço de um lançamento.

## Perguntas do projeto
- Quais fatores determinam o sucesso do pouso?
- Como carga útil, órbita, local de lançamento e número do voo se relacionam com o resultado?
- Qual modelo de classificação prevê melhor o pouso?

## Estrutura do repositório
| Caminho | Conteúdo |
|---|---|
| `notebooks/01_coleta_api_spacex.ipynb` | Coleta via API REST da SpaceX |
| `notebooks/02_coleta_web_scraping.ipynb` | Web scraping da Wikipedia |
| `notebooks/03_data_wrangling.ipynb` | Tratamento e criação da variável-alvo `Class` |
| `notebooks/04_eda_sql.ipynb` | Análise exploratória com SQL |
| `notebooks/05_eda_visualizacao.ipynb` | Análise exploratória com gráficos |
| `notebooks/06_mapa_folium.ipynb` | Mapa interativo com Folium |
| `dashboard/spacex_dash_app.py` | Dashboard Plotly Dash |
| `notebooks/07_classificacao.ipynb` | Modelos de classificação |
| `apresentacao/` | Apresentação final em PDF |

## Como executar
```bash
git clone https://github.com/mmadachi/capstone-spacex.git
cd capstone-spacex
pip install -r requirements.txt
jupyter notebook notebooks/
python dashboard/spacex_dash_app.py
```

## Resultados principais

| Item | Resultado |
|---|---|
| Taxa de sucesso do pouso no dataset | **66.67%** (60 pousos com sucesso em 90 lançamentos) |
| Local com maior taxa de sucesso | **KSC LC-39A** (76.92% de taxa de sucesso) |
| Acurácia dos modelos no teste | **83.33%** |
| Melhor modelo | **Regressão Logística / SVM / Árvore de Decisão** (83.33% no conjunto de teste) |

## Apresentação
O relatório completo está em `apresentacao/Relatório do Projeto Final de Ciência de Dados.pdf`.
