# ProjetoDeteccaoPlacas

Softwares and packages required:

  1- Python (3.12.0)
  
  2- OpenCV  --- pip install opencv-python
  
  3- streamlit --- pip install streamlit

How to use:

1- Abrir o terminal e ir até a pasta onde se encontra o arquivo CRUD.py, apos isso, rodar o comando stremalit run CRUD.py

2- No nosso projeto, será possivel fazer um CRUD de pessoas e veiculos, além de tirar uma foto (placa que será identificada)

3-Ao ir até a aba Camera e selecionar Tirar foto. abrirá uma pagina com sua camera, onde será possivel fecha-la apertando 'q' ou tirar uma foto e salvar apertando 's'. Apos tirar a foto, ela será salva na pasta resource, essa pasta foi destinada para receber todas as fotos que serão transformadas em string

4- Voltando a pasta principal (ProjetoDeteccaoPlacas) você deverá abrir a pasta OcrPython e abrir o ExemploEstagio.py

5- na função main o source deverá receber o caminho da imagem que você deseja escanear, após passar o caminho é só executar o script que ele começará fazer o OCR.
