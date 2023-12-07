import cv2
import pytesseract as pt


pt.pytesseract.tesseract_cmd = r'C:\Users\55149\AppData\Local\Tesseract.exe'

def EncontrarPlaca(source):
    img = cv2.imread(source)
    #cv2.imshow('img', img)

    #TRANSFORMANDO A IMAGEM EM CINZA
    cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('cinza', cinza)

    #BINARIZAR A IMAGEM
    _, bin = cv2.threshold(cinza, 90, 255, cv2.THRESH_BINARY)
    #cv2.imshow('bin', bin)

    #DESFOCAR E TIRAR RUIDOS DA IMAGEM
    desfoque = cv2.GaussianBlur(bin, (5, 5), 0)
    #cv2.imshow('des', desfoque)

    #ENCONTRAR CONTORNOS
    contornos, hierarquia = cv2.findContours(desfoque, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #cv2.drawContours(img, contornos, -1, (0, 255, 0), 1)


    #cv2.imshow('cont', img)

    for c in contornos:

        perimetro = cv2.arcLength(c, True)
        if perimetro > 450 :
            aprox = cv2.approxPolyDP(c, 0.03 * perimetro, True)
            if len(aprox) == 4:
                (x, y, alt, lar) = cv2.boundingRect(c)
                cv2.rectangle(img, (x, y), (x + alt, y + lar), (0, 255, 0), 2)
                roi = img[y:y + lar, x:x + alt]
                cv2.imwrite('output/roi.png', roi)



    cv2.imshow('draw',img)


    cv2.waitKey(0)
    cv2.destroyAllWindows()

def PreProcessamento():

    img_roi = cv2.imread("output/roi.png")

    if img_roi is None:
        return

    img_resize = cv2.resize(img_roi, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

    img_cinza = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)

    _, img_binary = cv2.threshold(img_cinza, 86, 255, cv2.THRESH_BINARY)

    cv2.imwrite("output/roi-OCR.png", img_binary)

    cv2.imshow("roi", img_binary)


    cv2.waitKey(0)
    cv2.destroyAllWindows()

def ocrImagemPlaca():
    image = cv2.imread("output/roi-OCR.png")

    custom_config = r'-c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyz/ --psm 6'
    saida = (pt.image_to_string(image, config=custom_config))
    print(saida)
    return saida


if __name__ == "__main__":
    source ='resource/save1.jpg'

    EncontrarPlaca(source)

    PreProcessamento()

    ocrImagemPlaca()
