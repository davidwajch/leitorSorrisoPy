Este projeto tem como objetivo detectar sorrisos em tempo real usando a biblioteca OpenCV, que é uma biblioteca de visão computacional de código aberto, e um Arduino para controlar um LED. Quando um sorriso é detectado, o programa envia um sinal serial ao Arduino para acender o LED.

Requisitos:

Python 3
Bibliotecas OpenCV e Serial
Arduino
Arduino IDE
Webcam

Instalação:

Instale a biblioteca OpenCV e Serial utilizando o pip.
Conecte o Arduino.
Execute o código Python no terminal.
Compile e envie o código do Arduino para o microcontrolador.

Funcionamento:

O programa inicia capturando os frames da webcam e transformando-os em imagens em escala de cinza. Em seguida, a biblioteca OpenCV é usada para detectar rostos e sorrisos na imagem. Quando um sorriso é detectado, o status é atualizado para "on" e enviado ao Arduino através da porta serial. O LED é ligado quando o Arduino recebe o status "on" e desligado quando recebe o status "off".

Código Python:

A biblioteca cv2 é importada para usar as funções de detecção de rostos e sorrisos.
A biblioteca serial é importada para enviar o status para o Arduino.
A câmera é inicializada e aberta para capturar os frames.
O loop principal começa.
Os frames são capturados e transformados em escala de cinza.
A função detectMultiScale é usada para detectar rostos na imagem.
Dentro do loop de detecção de rostos, a função detectMultiScale é usada novamente para detectar sorrisos em cada rosto.
Quando um sorriso é detectado, o status é atualizado para "on".
O status é enviado para o Arduino através da porta serial e o LED é ligado ou desligado de acordo com o status.
A imagem com as caixas delimitadoras dos rostos e sorrisos é exibida.
O loop continua até que a tecla 'q' seja pressionada.

Código Arduino:

A biblioteca Serial é importada para receber o status do Python.
O LED é configurado como uma saída.
O loop principal começa.
O Arduino aguarda a recepção de dados pela porta serial.
Quando os dados são recebidos, eles são armazenados em uma variável de string.
Se a variável for igual a "on", o LED é ligado.
Se a variável for igual a "off", o LED é desligado.
O loop continua indefinidamente.

Conclusão:

Este projeto demonstra como é possível usar a biblioteca OpenCV para detectar sorrisos em tempo real e controlar um dispositivo externo usando um microcontrolador Arduino.
