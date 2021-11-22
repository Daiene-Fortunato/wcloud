![Licensa MIT](https://img.shields.io/github/license/Daiene-Fortunato/wcloud)![GitHub repo size](https://img.shields.io/github/repo-size/Daiene-Fortunato/wcloud)

# :cloud: WCloud :cloud: - Seja bem-vindo!

​		Projeto de **Data Science** para iniciantes que desejam aprender a executar o tratamento e análise de dados simples através da programação com **Python**, **Markdown**, **Jupyter** e **StreamLit**. Tem o objetivo de gerar um arquivo de imagem contendo uma nuvem de palavras extraída de documentos de texto.

​		Criar uma **nuvem de palavras** pode ajudar o analista a identificar padrões de linguagem e reconhecer as palavras_chaves mais utilizadas em textos, relatórios e currículos. Há ainda algumas pessoas que utilizam o recurso para decorações de sites ou até mesmo estabelecimentos e residências.

Quer aprender um jeito fácil de programar e obter esse recurso? Eu te ajudo.

### Preparação

------

Há duas maneiras de utilizar o código:

1. Através do [Google Colab](https://colab.research.google.com/), você não vai precisar instalar nada e poderá fazer o download das imagens que gerar.
2. Através do seu ambiente local, para essa escolha tenha atenção especial aos requisitos informados, pois será necessário baixar uma IDE, módulos e etc.

​	Obs: eu não vou te ensinar a fazer o deploy deste projeto, mas se for fazer use o [Streamlit Share](https://share.streamlit.io/) ou o [Heroku](https://heroku.com/), são gratuitos e fáceis de usar.

### Usando o Google Colab (recomendado)

------

​		O Google Colab é uma ferramenta de programação em nuvem que permite a utilização de algumas linguagens como Python, R, Julia e Swift em conjunto com textos e imagens. Além disso, o ambiente é colaborativo, você pode fragmentar e rodar todo o código, fazer testes, desenvolver versões e compartilhar resultados com seus amigos e colegas de trabalho. 

Para executar o WCloud no google colab você vai precisar:

1. Possuir uma conta google e acessar o colab [aqui](https://colab.research.google.com/)
2. Inserir o código exatamente como nesse [arquivo](https://github.com/Daiene-Fortunato/wcloud/blob/main/colab.ipynb)
3. Adicionar na pasta do ambiente o seu "arquivo.pdf", copiar seu caminho e inserir no código
4. Rodar cada seção do código
5. Fazer o download do arquivo "mywordcloud.png" gerado na pasta do ambiente

​	Todas as ações são interativas e fáceis de serem implementadas, tenha calma e observe o ambiente ou assista vídeos de instrução no youtube.

- Exemplo de extração a partir de um currículo:

![wordcloud](https://github.com/Daiene-Fortunato/wcloud/blob/main/example.png?raw=true)



### Usando o Local Host (avançado)

------

​	Para fazer a aplicação rodar no seu ambiente local você terá que fazer algumas instalações e possuir conhecimentos básicos de programação, siga os passos descritos abaixo.

**Requisitos:**

- Anaconda (4.10.3)
- Python (3.9.7)
- Vs Code ou PyCharm
- streamlit (0.83.0)
- pdfplumber (0.5.2)
- nltk (3.5.0)
- numpy (1.19.2)
- pandas (1.1.3)
- wordcloud (1.8.1)
- matplotlib (3.3.2)

**Conhecimento prévio:**

- Saber usar o terminal do Anaconda para instalar as bibliotecas
- Saber configurar uma IDE para a linguagem Python
- Saber implementar uma aplicação no local host através do StreamLit
- Saber fazer um fork do github e puxar ele para sua máquina local

**Acessando a aplicação**

Uma vez que esse repositório esteja ativo na sua máquina:

1. Pelo prompt do Anaconda use o streamlit para rodar o wcloud.py
2. Uma aba do seu browser deve abrir contendo um painel interativo
3. Insira o arquivo.pdf que deseja analisar (apenas a primeira página será utilizada)
4. Clique em "Gerar Imagem"
5.  A imagem gerada com sua nuvem de palavras aparecerá na tela
6. Um novo arquivo chamado "mywordcloud.png" deve surgir no seu diretório local, é ele que você está visualizando na aplicação

7. Para fazer o deploy basta acrescentar os arquivos necessários em seu repositório e enviar

## Origem do Projeto e Agradecimentos

​				A ideia de inserir esse pequeno projeto de forma organizada para auxiliar devs iniciantes surgiu durante uma aula do Curso de Imersão em Data Science da [Flai](https://www.flai.com.br/) uma empresa de consultoria e ensino que eu descobri por acaso, mas que deu uma luz nos meus estudos. Fica registrado meu agradecimento.

​				O modelo utilizado para o Google Colab é uma cópia do que foi escrito em aula para exemplificar uma das tantas possibilidades da análise de dados em arquivos de texto, já a codificação para o ambiente local foi alterada e incrementada por mim para se tornar viável como uma aplicação Web independente.

## Contribuindo

​		Teve uma ideia que pode melhorar ou acrescentar algo bacana ao projeto? Leia [CONTRIBUTING.md](https://github.com/Daiene-Fortunato/wcloud/blob/main/CONTRIBUTING.md) para obter detalhes sobre o processo de envio de solicitações pull.

**Desafios Propostos:**

(iniciante)

- [ ] Criar uma função para deixar o código mais organizado
- [ ] Excluir o save automático e criar um botão para baixar a imagem gerada
- [ ] Criar a opção de selecionar vários arquivos de texto e gerar imagens para cada um deles importando automaticamente o nome dos arquivos

(avançado)

- [ ] Criar a opção de selecionar layout para a imagem (alterando formas, cores e tamanhos)

Divirta-se!



## Autoras

Contribuiu com:

1.  **wcloud.py**
2.  **colab.ipynb**
3. README.md
4. LICENSE.md
5. CONTRIBUTING.md
6. example.png



:woman_student: [**Daiene Fortunato**](https://www.linkedin.com/in/daienefortunato/) - Gestora de TI e Dev Backend

:email:  daiene.fortunato@gmail.com

![Daiene Fortunato](https://media-exp1.licdn.com/dms/image/D4E03AQGBXxy-MaASgA/profile-displayphoto-shrink_200_200/0/1634165214468?e=1643241600&v=beta&t=3nP5RbaTr6Sw_K4_6v255iU3MTWK6u94AF2Cxzf60nk)



------

Contribuiu com:

1. Origem do **colab.ipynb**



:woman_student: [**Juliana Scudilho**](https://www.linkedin.com/in/julianascudilio/) da [Flai](flai.com.br) - Data Science e Inteligência Artificial

:email: juliana-scudilio@uol.com.br

![JULIANA SCUDILIO](https://media-exp1.licdn.com/dms/image/C4E03AQEepqyGWj1iww/profile-displayphoto-shrink_200_200/0/1619750599237?e=1643241600&v=beta&t=qxhlW1i4hg-C-Nndyw4z8usKS_KXcQVHBYz_GV0E_lU)



## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE.md](https://github.com/Daiene-Fortunato/wcloud/blob/main/LICENSE.md) para detalhes

