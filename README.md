⚽ Projeto Previsão ML - Brasileirão

Aplicação de Machine Learning para prever o resultado de partidas do Campeonato Brasileiro, utilizando dados históricos reais, pipeline de treinamento com Scikit-learn e interface interativa em Streamlit.

🔗 Aplicação online

👉 Teste o projeto ao vivo: https://brasileirao-match-predictor-ckjgt2tfuqstkbbak4ky5w.streamlit.app/

📌 Sobre o projeto

O objetivo do projeto é prever a probabilidade de três possíveis resultados de uma partida:

🏠 Vitória do mandante

🤝 Empate

🛫 Vitória do visitante


O modelo foi treinado com partidas históricas do Brasileirão e utiliza os times mandante e visitante como variáveis de entrada para estimar as probabilidades do confronto.

🚀 Tecnologias utilizadas

Python

Pandas

Scikit-learn

Streamlit

Joblib

Git & GitHub


🧠 Pipeline do projeto

O fluxo do projeto foi dividido em etapas para simular um pipeline real de Machine Learning:

Limpeza e tratamento dos dados;

leitura da base histórica;

criação da variável alvo (resultado);

exportação dos dados tratados;

Treinamento do modelo;

codificação dos times com OneHotEncoder;

treinamento com LogisticRegression;

serialização com joblib;

Predição;

carregamento do modelo salvo;

inferência baseada nos times selecionados;

Aplicação web;

interface interativa em Streamlit;

seleção de mandante e visitante;

exibição das probabilidades;


📊 Funcionalidades

✅ Tratamento dos dados históricos;

✅ Treinamento automatizado do modelo;

✅ Predição de resultados em tempo real;

✅ Interface web interativa;

✅ Deploy em nuvem com Streamlit Cloud;


📁 Estrutura do projeto

projeto-previsao-ml/
│
├── data/
│   ├── campeonato-brasileiro-full.csv
│   └── jogos_tratados.csv
├── models/
│   └── modelo.pkl
├── src/
│   ├── limpeza.py
│   ├── treino.py
│   └── previsao.py
├── app.py
├── requirements.txt
└── README.md

▶️ Como executar localmente


No terminal do VS Code:


pip install -r requirements.txt

python src/limpeza.py

python src/treino.py

streamlit run app.py


Este projeto foi desenvolvido como parte do meu portfólio em Machine Learning aplicado, unindo:

análise de dados;

modelagem preditiva;

desenvolvimento de produto;

deploy em nuvem;

storytelling com dados esportivos;

Ideal para demonstrar habilidades em projetos reais de IA e Data Science.

👨‍💻 Autor

Vitor Gabriel Penhorato

LinkedIn: https://www.linkedin.com/in/vitor-penhorato

GitHub: https://github.com/vitorgabriel100

Portfólio: https://vitorgabriel100.github.io/portfolio/

