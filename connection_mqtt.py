import paho.mqtt.client as mqtt
from notifier import show_notification
import uuid

def on_message(client, userdata, message):
    msg = message.payload.decode()
    topic = message.topic
    print(f"Mensaje recibido en el topic '{topic}': {msg}")

    parts = msg.split(": ")
    title = parts[0]
    notification_title = parts[1]
    show_notification(title, notification_title)

client_id = f"breakify-subscriber-{uuid.uuid4()}"
client = mqtt.Client(client_id=client_id, clean_session=False, protocol=mqtt.MQTTv311, callback_api_version=2)
client.enable_logger()
client.reconnect_delay_set(min_delay=1, max_delay=300)
client.connect("localhost", 1883, keepalive=60)
client.subscribe("breakify/notifications/#")
client.on_message = on_message

print("Esperando mensajes...")
client.loop_forever()