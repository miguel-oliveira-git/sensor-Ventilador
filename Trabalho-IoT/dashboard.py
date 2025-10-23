import dash
from dash import html, dcc
from dash.dependencies import Output, Input
import paho.mqtt.client as mqtt
from threading import Thread

broker = "localhost"
port = 1883
topic_temp = "estufa/temperatura"
topic_status = "estufa/ventilacao/status"

temperatura = "--"
status_vent = "Desligado"
temp_min = 18
temp_max = 25

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao broker")
        client.subscribe(topic_temp)
        client.subscribe(topic_status)

def on_message(client, userdata, msg):
    global temperatura, status_vent
    if msg.topic == topic_temp:
        temperatura = msg.payload.decode()
    elif msg.topic == topic_status:
        status_vent = msg.payload.decode().capitalize()

def mqtt_loop():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    client.loop_forever()

t = Thread(target=mqtt_loop)
t.daemon = True
t.start()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard de Miguel Oliveira Jardim"),
    html.H3("Monitoramento da Estufa"),
    html.P(id="temp"),
    html.P("Temperatura mínima: " + str(temp_min) + "°C"),
    html.P("Temperatura máxima: " + str(temp_max) + "°C"),
    html.P(id="vent"),
    dcc.Interval(id="atualiza", interval=2000, n_intervals=0)
])

@app.callback(
    [Output("temp", "children"), Output("vent", "children")],
    Input("atualiza", "n_intervals")
)
def atualizar(n):
    return f"Temperatura atual: {temperatura} °C", f"Ventilador: {status_vent}"

if __name__ == "__main__":
    app.run(debug=False)
