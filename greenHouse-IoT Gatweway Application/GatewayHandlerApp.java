package neu.crana.connecteddevices.labs.module10;

import java.sql.Timestamp;
import java.util.logging.Level;
import java.util.logging.LogManager;
import java.util.logging.Logger;

import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

import neu.crana.connecteddevices.labs.module10.MqttClientConnector;
import neu.crana.connecteddevices.labs.module10.UbidotsClientConnector;;

public class GatewayHandlerApp{

	static String topic = "test";
	static String content = "Ack";
	static int qos = 2;
	static String clientId = "java";
	static String broker = "tcp://broker.hivemq.com:1883";
	static MemoryPersistence persistence = new MemoryPersistence();
		
		private static UbidotsClientConnector ubidots;
		
		public GatewayHandlerApp() {
			super();
			this.ubidots = new UbidotsClientConnector();
		}
		
		/*
		 * main methos will only call mqttconnector to subscribe the python channel
		 * and to subscribe ubidots channel pubish methods for both will be called via callback function
		 */
		public static void main(String[] args) {
			
			try {
//				TimeUnit.SECONDS.sleep(2);
				GatewayHandlerApp.Mqttconnector();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		
		/*
		 * MqttClient connector will connect to the python channel "test" , subscribes and gets the data using hivemq broker
		 */
		public static void Mqttconnector() throws InterruptedException{
			try {
				//used persistence for reliability in case clean session is set to false 
				MqttClient cli = new MqttClient(broker, clientId, persistence);
				MqttConnectOptions options = new  MqttConnectOptions();
				options.setCleanSession(true);
				cli.connect(options); // connected to broker using MqttConnectOptions
				
				LogManager log_manager = LogManager.getLogManager(); //maintain set of log
				Logger log = log_manager.getLogger(Logger.GLOBAL_LOGGER_NAME); //create logger with global logger name
				log.log(Level.INFO, "connected");
				
				cli.subscribe("test", qos);
				log.log(Level.INFO, "Connected to "+broker+" with client ID "+cli.getClientId());
				cli.setCallback(new MqttClientConnector()); //calling callbacks from MqttClienntConnector
				System.out.println("\n "+"######### Subscribed to test python channel ##############" + "\n");

				String time = new Timestamp(System.currentTimeMillis()).toString();	    	
				MqttMessage message = new MqttMessage();
				System.out.println("Time:\t" +time +
	                    "  Topic:\t" + topic +
	                    "  Message:\t" + new String(message.getPayload()) +
	                    "  QoS:\t" + message.getQos());
				cli.messageArrivedComplete(3, qos); // message with id 3 arrives
				
			} catch (MqttException e) {
				e.printStackTrace();
				System.out.println("reason "+e.getReasonCode());
			}
		}
}
