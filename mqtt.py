import paho.mqtt.client as mqtt
class mqtt:
    def __init__(self):
        self.temperatura=0
        self.temperatura = 0
        self.listaTemp = []
        self.tempOra = 0
        self.tempMin = 0
        self.tempDieci = 0
        self.cont1 = 0
        self.cont10 = 0
        self.contOra = 0
        self.client = mqtt.Client(client_name="calvino00", protocol=mqtt.MQTTv311)
    def connect_and_take(self):

        self.client.username_pw_set(username="calvino00", password="0123456789")
        self.client.on_connect = on_connect
        self.client.on_subscribe = on_subscribe
        self.client.on_message = on_message

        self.client.connect(host='broker.shiftr.io', port=1883, keepalive=60)
        try:
            self.client.loop_forever()
        except KeyboardInterrupt:
            print()


    def on_connect(self, client, userdata, flags, rc):
        print('result from connect: {}'.format(mqtt.connack_string(rc)))
        self.client.subscribe('calvino-08/temperatura', qos=0)

    def on_subscribe(client, userdata, mid, granted_qos):
        print('subscribed topic with QoS: {}'.format(granted_qos[0]))

    def on_message(self,client, userdata, msg):
        self.temperatura = str(msg.payload.decode("utf-8"))
        self.listaTemp.append(self.temperatura)
        self.cont1 += 1
        self.cont10 += 1
        self.contOra += 1
        if (self.cont1 == 11):
            tmp = 0
            for i in range(1, 13):
                tmp = tmp + self.listaTemp[-i]
            self.tempMin = tmp / 12
        if (self.cont10 == 119):
            tmp = 0
            for i in range(1, 121):
                tmp = tmp + self.listaTemp[-i]
            self.tempDieci = tmp / 120
        if (self.contOra == 719):
            tmp = 0
            for i in range(1, 721):
                tmp = tmp + self.listaTemp[-1]
            self.tempOra = tmp / 720






