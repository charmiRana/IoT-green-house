package neu.crana.connecteddevices.labs.module10;

import java.lang.management.ManagementFactory;
import java.lang.management.OperatingSystemMXBean;
import java.util.concurrent.TimeUnit;
import java.util.logging.Level;
import java.util.logging.LogManager;
import java.util.logging.Logger;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.json.JSONObject;

import com.google.gson.JsonElement;

import neu.crana.connecteddevices.common.DataUtil;

public class MqttClientConnector implements MqttCallback {
	
	private DataUtil datautil = new DataUtil();

	@Override
	public void connectionLost(Throwable cause) {
		System.out.println("******** Connection lost!!!! problem occured subscribing Python  ********");		
	}
	
	/**
	 * call back message arrived is used for publishing data to ubidots
	 * with json we can get value from the incoming string from java
	 * json object is passed with put to post the data to ubidots variable
	 * it is checking topic name if it matches than only sends data to ubidots
	 * 
	 */

	@Override
	public void messageArrived(String topic, MqttMessage message) throws Exception {
		System.out.println("Message arrived from python. Topic:  " + topic + " Message:  " + message.toString());
		TimeUnit.SECONDS.sleep(5); 
		
		LogManager log_manager = LogManager.getLogManager(); //maintain set of log
		Logger log = log_manager.getLogger(Logger.GLOBAL_LOGGER_NAME);
				
		String payload = message.toString();
		
		log.log(Level.INFO, "Publishing temperature value to ubidots usinh HTTP API");
		JsonElement jsonelement = datautil.ToSesnsorData(payload, "temperature");
		JSONObject jobj = new JSONObject();
		jobj.put("temperature",jsonelement); 
		String json = jobj.toString();
		UbidotsClientConnector.HttpPost("devices/greenhousehandler", json);
		
		log.log(Level.INFO, "Publishing Humidity value to ubidots usinh HTTP API");
		JsonElement jsonelement1 = datautil.ToSesnsorData(payload, "humidity");
		JSONObject jobj1 = new JSONObject();
		jobj1.put("humidity",jsonelement1);
		String json1 = jobj1.toString();
		UbidotsClientConnector.HttpPost("devices/greenhousehandler", json1);
		
		log.log(Level.INFO, "Publishing Pressure value to ubidots usinh HTTP API");
		JsonElement jsonelement2 = datautil.ToSesnsorData(payload, "pressure");
		JSONObject jobj2 = new JSONObject();
		jobj2.put("pressure",jsonelement2);
		String json2 = jobj2.toString();
		UbidotsClientConnector.HttpPost("devices/greenhousehandler", json2);
		
		log.log(Level.INFO, "Publishing gas value value to ubidots usinh HTTP API");
		JsonElement jsonelement3 = datautil.ToSesnsorData(payload, "gasvalue");
		JSONObject jobj3 = new JSONObject();
		jobj3.put("co2gas",jsonelement3);
		String json3 = jobj3.toString();
		UbidotsClientConnector.HttpPost("devices/greenhousehandler", json3);
		
		log.log(Level.INFO, "Publishing PH value to ubidots usinh HTTP API");
		JsonElement jsonelement4 = datautil.ToSesnsorData(payload, "phvalue");
		JSONObject jobj4 = new JSONObject();
		jobj4.put("soilphvalue",jsonelement4);
		String json4 = jobj4.toString();
		UbidotsClientConnector.HttpPost("devices/greenhousehandler", json4);
		
		log.log(Level.INFO, "Publishing Soil moisture value to ubidots usinh HTTP API");
		JsonElement jsonelement5 = datautil.ToSesnsorData(payload, "soilmoisture");
		JSONObject jobj5 = new JSONObject();
		jobj5.put("soilmoisture",jsonelement5);
		String json5 = jobj5.toString();
		UbidotsClientConnector.HttpPost("devices/greenhousehandler", json5);
		
		log.log(Level.INFO, "Publishing Luminance value to ubidots usinh HTTP API");
		JsonElement jsonelement6 = datautil.ToSesnsorData(payload, "luminance");
		JSONObject jobj6 = new JSONObject();
		jobj6.put("luminance",jsonelement6);
		String json6 = jobj6.toString();
		UbidotsClientConnector.HttpPost("devices/greenhousehandler", json6);
		
		log.log(Level.INFO, "Publishing cpu util value to ubidots usinh HTTP API");
		JsonElement jsonelement7 = datautil.ToSesnsorData(payload, "cpu");
		JSONObject jobj7 = new JSONObject();
		jobj7.put("cpuutil",jsonelement7);
		String json7 = jobj7.toString();
		UbidotsClientConnector.HttpPost("devices/greenhousehandler", json7);
		
		log.log(Level.INFO, "Publishing gateway application system performance average value to ubidots usinh HTTP API");
		JSONObject jobj8 = new JSONObject();
		jobj8.put("gatewaycpu",this.SystemPerformance());
		String json8 = jobj8.toString();
		UbidotsClientConnector.HttpPost("devices/greenhousehandler", json8);
	}	

	@Override
	public void deliveryComplete(IMqttDeliveryToken token) {
		try {
			System.out.println("delivery complete" + new String(token.getMessage().getPayload()));
		} catch (MqttException e) {
			e.printStackTrace();
		} 
	}
	
	/*
	 * checking for systemperformance
	 */
	public double SystemPerformance() {
		OperatingSystemMXBean bean = ManagementFactory.getPlatformMXBean(OperatingSystemMXBean.class);
		double cpuload = bean.getSystemLoadAverage();
		return cpuload;
	}
}
