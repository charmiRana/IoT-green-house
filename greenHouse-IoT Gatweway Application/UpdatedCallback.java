package neu.crana.connecteddevices.labs.module10;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;
import org.json.JSONObject;

 class UpdatedCallback implements MqttCallback{
	
	private UpdatedCallback call;
	
	@Override
	public void connectionLost(Throwable cause) {
		System.out.println("******** Connection lost!!!! problem occured subscribing ubidots  ********");
	}

	/*
	 * this call back is called after subscribing to cloud 
	 * publishes data to python channel
	 */
	@Override
	public void messageArrived(String topic, MqttMessage message) throws Exception {
		System.out.println("Message arrived from cloud:. Topic:  " + topic + " Message:  " + message.toString());
		
		MqttClient cli = new MqttClient("tcp://mqtt.eclipse.org:1883", "java", new MemoryPersistence());		
		MqttConnectOptions options = new  MqttConnectOptions();		
		options.setCleanSession(true);
		 // connected to broker using MqttConnectOptions
		options.setConnectionTimeout(60);
		options.setKeepAliveInterval(65);
		cli.connect(options);	
		
		String jsonString = message.toString();
		JSONObject obj = new JSONObject(jsonString);
		float value = obj.getFloat("value");
		String data = "{\""+"value \" : " + value +   " , \"Topic\" : "+ "\"" + topic +"\"}";
		MqttMessage m = new MqttMessage(data.getBytes());
		System.out.println("publishing value -->" + m);
		m.setQos(2);
		
		cli.publish("temp", m);		
		}

	@Override
	public void deliveryComplete(IMqttDeliveryToken token) {
		try {
			System.out.println("delivery complete" + new String(token.getMessage().getPayload()));
		} catch (MqttException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 
	}
}
