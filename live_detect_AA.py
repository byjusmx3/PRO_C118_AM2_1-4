# Importa la biblioteca opencv
import cv2

# Carga el archivo Cascade Classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

eye_cascade = cv2.CascadeClassifier('C:/Users/preet/AppData/Local/Programs/Python/Python39/Lib/site-packages/cv2/data/haarcascade_eye.xml') 

# Define un objeto video capture
vid = cv2.VideoCapture(0)

while(True):
   
    # Captura el video cuadro por cuadro
    ret, frame = vid.read()

    # Conviértelo a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta los rostros, ojos y sonrisa
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    eyes = eye_cascade.detectMultiScale(gray, 1.1, 5)

    # Dibuja un rectángulo alrededor del rostro, ojos y boca
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        
    # Muestra el cuadro de resultado
    cv2.imshow('frame', frame)
      
    # Cierra la ventana con la tecla espaciadora
    if cv2.waitKey(25) == 32:
        break
  
# Después del bucle, libera el objeto capturado
vid.release()

# Cierra todas las ventanas
cv2.destroyAllWindows()