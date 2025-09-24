import paho.mqtt.client as mqtt

broker_address = "localhost"
port = 1883
topic_comando = "estufa/ventilacao/comando"


def on_message(client, userdata, msg):
    comando = msg.payload.decode()
    if comando == "ligar":
        print("\n[VENTILADOR] LIGAR!")
    elif comando == "desligar":
        print("\n[VENTILADOR] DESLIGAR!")
    else:
        print("\n[VENTILADOR] Comando desconhecido.")


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado e aguardando comandos...")
        client.subscribe(topic_comando)
    else:
        print("Falha na conexão do ventilador.")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "VentiladorSimulado")
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, port)

client.loop_forever()