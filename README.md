# Leitor de Sorriso

Detector de sorrisos em tempo real que aciona um LED no Arduino quando detecta uma pessoa sorrindo. Projeto de integração entre visão computacional (OpenCV) e hardware.

## O que faz

O programa captura frames da webcam, detecta rostos e sorrisos usando classificadores Haar Cascade do OpenCV, e envia comandos via serial para o Arduino acender/apagar um LED quando detecta sorriso.

## Stack

- **Python 3**: OpenCV para detecção facial, pyserial para comunicação serial
- **Arduino**: sketch simples que lê comandos da serial e controla o LED no pino 13
- **Hardware**: Arduino Uno (ou compatível), LED, webcam

## Como rodar

### 1. Setup Python

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

### 2. Configurar Arduino

1. Conecte o Arduino via USB
2. Identifique a porta serial:
   - **Windows**: geralmente `COM3`, `COM4`, etc (veja no Gerenciador de Dispositivos)
   - **Linux/Mac**: geralmente `/dev/ttyUSB0` ou `/dev/ttyACM0` (use `ls /dev/tty*`)
3. Abra `leitorSorriso.py` e ajuste a linha 9:
   ```python
   serialCom = serial.Serial('COM3', 9600)  # Trocar COM3 pela sua porta
   ```
4. Carregue o sketch `arduino.ino` no Arduino pela IDE oficial

### 3. Rodar

```bash
python leitorSorriso.py
```

Pressione `q` para sair.

## Estrutura

```
.
├── leitorSorriso.py    # Script principal (captura, detecção, comunicação serial)
├── arduino.ino         # Sketch Arduino (recebe "on"/"off" e controla LED)
├── requirements.txt    # Dependências Python
├── video.mp4           # Vídeo de demonstração
└── README.md
```

## Como funciona

1. Captura frame da webcam
2. Converte para escala de cinza
3. Detecta rostos com `haarcascade_frontalface_default.xml`
4. Para cada rosto detectado, busca sorrisos com `haarcascade_smile.xml`
5. Se detectar sorriso, envia `"on"` pela serial; caso contrário, envia `"off"`
6. Arduino lê o comando e liga/desliga o LED no pino 13

## Melhorias futuras

- [ ] Adicionar logs para debug da comunicação serial
- [ ] Permitir configurar porta serial via argumento CLI ou arquivo de config
- [ ] Calibrar parâmetros de detecção (scaleFactor, minNeighbors) para reduzir falsos positivos
- [ ] Adicionar testes para validar detecção em diferentes condições de iluminação
- [ ] Gravar vídeos de exemplo com detecções bem-sucedidas

## Licença

MIT - veja [LICENSE](LICENSE)
