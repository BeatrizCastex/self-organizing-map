# self-organizing-map

Projeto 4 - Análise e Reconhecimento de Padrões

Beatriz de Camargo Castex Ferreira

Docente: Prof. Luciano da Fontoura Costa

USP São Carlos - IFSC

07/2020

OS ARQUIVOS DESSA PASTA FORAM FEITOS COM OBJETIVOS EDUCATIVOS COMO PARTE DE UM
PROJETO DA MATÉRIA DE ANÁLISE E RECONHECIMENTO DE PADRÕES DO CURSO DE GRADUAÇÃO
EM FÍSICA COMPUTACIONAL DO IFSC-USP.

Note que nesse projeto foi utilizada a base de dígitos manuscritos da UC Irvine, disponível no link: https://archive.ics.uci.edu/ml/datasets/Optical+Recognition+of+Handwritten+Digits
Pode ser necessário baixar a base de dados antes de rodar o programa no seu próprio computador.

Também foi utilizada a biblioteca SciKit Learn disponível em https://scikit-learn.org
Pode ser necessário instalar essa biblioteca antes de rodar o programa em seu próprio computador. 

Mais informações e referências completas podem ser encontradas no relatório do projeto e nos comentários do código.

====== Descrição do projeto ========

Preparação para Projeto:

Parte A: Implementar a estrutura de dados para a camada córtex (NXN) e entrada
retina (MXM) da rede neuronal auto-organizada, SOM. Inicializar os pesos dos
neurônios lineares com valores aleatórios uniformemente distribuídos entre 0 e 1.

Parte B: Obter base de dados de caracteres manuscritos da internet. Escolher
ao menos 5 caracteres e considerar ao menos 12 instâncias de cada caracter.
Recomenda-se que as imagens dos caracteres não seja grande, algo em torno de 15X15.

Parte C: Entrar alguns dos caracteres na rede obtida em A e identificar o(s)
neurônio(s) que produzem máxima saída para cada caracter testado.

PROJETO 4: SOM
Parte A: Implementar a arquitetura SOM, com camada de entrada (retina) e córtex.
Inicializar com valores aleatórios uniformemente distribuídos, e testar com a
alguns padrões para verificar a resposta dos neurônios.

Parte B: Obter base de dados de caracteres manuscritos, ao menos 4 categorias,
com ao menos 20 exemplos por categoria. Treinar a rede com esta base e
identificar as regiões particionadas do córtex em termos das respostas aos 4
tipos de caracteres

=======================================

=============== ÍNDICE ================

1-figuras:
  Pasta contendo todas as imagens e gráficos geradas na produção do projeto.


som.py:
  Programa que implementa a arquitetura som.
