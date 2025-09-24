import paho.mqtt.client as mqtt

broker_address = "localhost"
port = 1883
topic_temperatura = "estufa/temperatura"
topic_comando = "estufa/ventilacao/comando"
topic_status = "estufa/ventilacao/status"

temp_minima = 18.0
temp_maxima = 25.0
ventilador_ligado = False

def mandar_mensagem(client, userdata, msg):
    global ventilador_ligado
    print(f"\n[CLIENTE DE CONTROLE] Mensagem recebida: {msg.payload.decode()}°C")

    try:
        temperatura = float(msg.payload.decode())
        
        if temperatura > temp_maxima and not ventilador_ligado:
            print("Temperatura muito alta. Ligando o ventilador...")
            client.publish(topic_comando, "ligar")
            client.publish(topic_status, "ligado")
            ventilador_ligado = True
        elif temperatura < temp_minima and ventilador_ligado:
            print("Temperatura ideal. Desligando o ventilador...")
            client.publish(topic_comando, "desligar")
            client.publish(topic_status, "desligado")
            ventilador_ligado = False
        else:
            print("Temperatura ideal.")

    except ValueError:
        print("Dados inválidos.")

def conectar(client, userdata, flags, rc):
    if rc == 0:
        print("Cliente de controle conectado. Aguardando dados...")
        client.subscribe(topic_temperatura)
    else:
        print("Falha na conexão do cliente.")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "ClienteControle")
client.on_connect = conectar
client.on_message = mandar_mensagem
client.connect(broker_address, port)

client.loop_forever()