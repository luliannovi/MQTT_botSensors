import subprocess
import paho.mqtt.client as mqtt
import os
class mqtt:
    temperatura=0
    listaTemp=[]
    tempOra=0
    tempMin=0
    tempDieci=0
    cont1=0
    cont10=0
    contOra=0
    client = mqtt.Client(client_name="calvino00",protocol=mqtt.MQTTv311)
    def __init__(self):
        self.temperatura=0
    def connect_and_take(self):
        client.username_pw_set(username="calvino00", password="0123456789")
        client.on_connect = on_connect
        client.on_subscribe = on_subscribe
        client.on_message = on_message

        client.connect(host='broker.shiftr.io', port=1883, keepalive=60)
        try:
            client.loop_forever()
        except KeyboardInterrupt:
            print()
        #self.temperatura=os.system("mosquitto_sub -h \"broker.shiftr.io\" -u \"calvino00\" -P \"0123456789\" -t calvino-08/temperatura")
        #Aggiunta a liste
        self.listaTemp.append(self.temperatura)
        self.cont1+=1
        self.cont10+=1
        self.contOra+=1
        if(self.cont1==11):
            tmp=0
            for i in range(1,13):
                tmp=tmp+self.listaTemp[-i]
            self.tempMin=tmp/12
        if(self.cont10==119):
            tmp=0
            for i in range(1,121):
                tmp=tmp+self.listaTemp[-i]
            self.tempDieci=tmp/120
        if(self.contOra==719):
            tmp=0
            for i in range(1,721):
                tmp=tmp+self.listaTemp[-1]
            self.tempOra=tmp/720

    def on_connect(client, userdata, flags, rc):
        print('result from connect: {}'.format(mqtt.connack_string(rc)))
        self.client.subscribe('calvino-08/temperatura', qos=0)

    def on_subscribe(client, userdata, mid, granted_qos):
        print('subscribed topic with QoS: {}'.format(granted_qos[0]))

    def on_message(client, userdata, msg):
        self.temperatura = str(msg.payload.decode("utf-8"))






