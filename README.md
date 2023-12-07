# ProjetoDeteccaoPlacas

Softwares e pacotes necessários:

  1- Python (3.12.0)
  
  2- OpenCV  --- pip install opencv-python
  
  3- streamlit --- pip install streamlitr

  4- tesseract --- https://github.com/tesseract-ocr/tesseract

  5- pytesseract --- pip install pytesseract

Como Usar:

1- Abrir o terminal e ir até a pasta onde se encontra o arquivo CRUD.py, apos isso, rodar o comando stremalit run CRUD.py

2- No nosso projeto, será possivel fazer um CRUD de pessoas e veiculos, além de tirar uma foto (placa que será identificada)

3-Ao ir até a aba Camera e selecionar Tirar foto. abrirá uma pagina com sua camera, onde será possivel fecha-la apertando 'q' ou tirar uma foto e salvar apertando 's'. Apos tirar a foto, ela será salva na pasta resource, essa pasta foi destinada para receber todas as fotos que serão transformadas em string

4- Voltando a pasta principal (ProjetoDeteccaoPlacas) você deverá abrir a pasta OcrPython e abrir o ExemploEstagio.py

5- na função main o source deverá receber o caminho da imagem que você deseja escanear, após passar o caminho é só executar o script que ele começará fazer o OCR.

Situação do projeto:

No presente momento, conseguimos desenvolver o CRUD e também o script q faz o OCR, detectando a placa e imprimindo no final uma string com o conteudo encontrado na placa, e também o Front-end.
O problema que encontramos foi a junção de ambas partes, por exemplo fazer com que o CRUD consiga chamar o script do OCR no momento em que o usuario clicar para tirar a foto, tentamos de varias maneiras e não conseguimos atingir o objetivo esperado.
Quanto ao front-end, ele está desenvolvido, mas, tivemos problemas também na hora de conectar ao back-end


OBS: tivemos um problema com o tesseract, para resolver foi necessario passar o caminho de onde ele foi instalado

import pytesseract as pt

pt.pytesseract.tesseract_cmd = r'C:\Users\55149\AppData\Local\Tesseract.exe'
