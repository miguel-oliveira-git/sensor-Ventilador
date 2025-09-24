# 🌱 Estufa IoT com MQTT

Simulação de uma **estufa inteligente** usando **Python + MQTT**.  
O sistema tem três partes principais:

- 🌡️ **Sensor (`sensor.py`)** → publica temperaturas aleatórias (15°C ~ 30°C) no tópico `estufa/temperatura`.  
- 🧠 **Cliente de Controle (`cliente.py`)** → decide ligar/desligar o ventilador conforme a temperatura.  
- 💨 **Ventilador (`ventilador.py`)** → recebe comandos e imprime ações no terminal.  

---

## ⚡ Tecnologias
🐍 Python 3 • 📡 MQTT (paho-mqtt) • 🌀 Mosquitto Broker  

---
