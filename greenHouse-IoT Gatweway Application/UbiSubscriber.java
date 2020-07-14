package neu.crana.connecteddevices.labs.module10;

import java.io.UnsupportedEncodingException;
import java.security.KeyManagementException;
import java.security.NoSuchAlgorithmException;

import org.eclipse.paho.client.mqttv3.MqttException;

import neu.crana.connecteddevices.labs.module10.UbidotsClientConnector;

public class UbiSubscriber {
	private static UbidotsClientConnector ubicon;
	String topic;
	public UbiSubscriber() {
		super();
		this.ubicon = new UbidotsClientConnector();
	}
	
	/*
	 * passing every topic to subscribe using subscriber class
	 */
	public static void main(String[] args) throws KeyManagementException, UnsupportedEncodingException, NoSuchAlgorithmException, MqttException, InterruptedException {
		UbidotsClientConnector ubicon = new UbidotsClientConnector();
		ubicon.UbiTempSubscribe("/v1.6/devices/greenhousehandler/temperatureactuator");
		ubicon.UbiTempSubscribe("/v1.6/devices/greenhousehandler/humidityactuator");
		ubicon.UbiTempSubscribe("/v1.6/devices/greenhousehandler/pressureactuator");
		ubicon.UbiTempSubscribe("/v1.6/devices/greenhousehandler/gasactuator");
		ubicon.UbiTempSubscribe("/v1.6/devices/greenhousehandler/lightactuator");
		ubicon.UbiTempSubscribe("/v1.6/devices/greenhousehandler/soilphactuator");
		ubicon.UbiTempSubscribe("/v1.6/devices/greenhousehandler/soilmoistureactuator");
		
	}

}
