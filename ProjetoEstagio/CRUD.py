from datetime import datetime

import pandas as pd
import streamlit as st


import Pages.Pessoa.Create as PageIncluirPessoa
import Pages.Pessoa.List as PageReadPessoa
import Pages.Veiculo.Create as PageIncluirVeiculo
import Pages.Veiculo.List as PageReadVeiculo
import subprocess
import cv2
import os


st.sidebar.title('Página Principal')
Page_pessoa = st.sidebar.selectbox('Pessoa', ['Incluir', 'Consultar'],0)
Page_veiculo = st.sidebar.selectbox('Veiculo', ['Incluir', 'Consultar'],0)
Page_camera = st.sidebar.selectbox('Camera', ['', 'Tirar Foto'])

from time import sleep










if Page_pessoa == 'Consultar':
    PageReadPessoa.Read()

if Page_veiculo == 'Consultar':
    PageReadVeiculo.Read()

if Page_pessoa == 'Incluir':
    st.experimental_set_query_params()
    PageIncluirPessoa.Incluir()

if Page_veiculo == 'Incluir':
    st.experimental_set_query_params()
    PageIncluirVeiculo.Incluir()

if Page_camera == '':
    cv2.destroyAllWindows()



if Page_camera == 'Tirar Foto':
    key = cv2.waitKey(1)
    webcam = cv2.VideoCapture(0)
    sleep(2)
    val = True
    while val == True:

        try:
            check, frame = webcam.read()
            print(check)  # prints true as long as the webcam is running
            print(frame)  # prints matrix values of each framecd
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'):
                cv2.imwrite(filename='OcrPython/resource/saved_img.jpg', img=frame)
                webcam.release()
                print("Processing image...")
                img_ = cv2.imread('OcrPython/resource/saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                print("Converting RGB image to grayscale...")
                gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                print("Converted RGB image to grayscale...")
                print("Resizing image to 28x28 scale...")
                img_ = cv2.resize(gray, (300, 200))
                print("Resized...")
                img_resized = cv2.imwrite(filename='OcrPython/resource/saved_img-final.jpg', img=img_)
                print("Image saved!")
                val = False
                break

            elif key == ord('q'):
                webcam.release()
                cv2.destroyAllWindows()
                break

        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break










