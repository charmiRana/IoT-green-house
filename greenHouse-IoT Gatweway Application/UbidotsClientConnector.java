package neu.crana.connecteddevices.labs.module10;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.lang.management.ManagementFactory;
import java.lang.management.OperatingSystemMXBean;
import java.security.KeyManagementException;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.LogManager;
import java.util.logging.Logger;

import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClientBuilder;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

import com.labbenchstudios.iot.common.CertManagementUtil;
import com.ubidots.ApiClient;
import com.ubidots.Variable;

import neu.crana.connecteddevices.labs.module10.UpdatedCallback;

public class UbidotsClientConnector{
	
static ApiClient api = new ApiClient("BBFF-29JNJFixHoKIIJPsuAFtbL3R5Bjyce");
	
	static String broker = "ssl://industrial.api.ubidots.com:8883";
	private static String token;
	private String filepath;
	static String payload;
	static int qos =0;
	static MemoryPersistence persistence = new MemoryPersistence();
	private static Map<String, String> tokenHeader;
	private String baseUrl;
	private String name;
	private Thread t;
	
	public UbidotsClientConnector() {
		super();
	}
		
	/*	ConnectUbidots method will connect with ubidots using ssl port and secure connection via certificate. After securing connection it will subscribe to
	 *  channel and get data from the ubidots cloud from tempactuator variable 
	 */	
	public void UbiTempSubscribe(String subtopic) throws MqttException, UnsupportedEncodingException, NoSuchAlgorithmException, KeyManagementException, InterruptedException {
		MqttClient client = new MqttClient(broker,"BBFF-29JNJFixHoKIIJPsuAFtbL3R5Bjyce", new MemoryPersistence()); //URL is api key(username)
		MqttConnectOptions options = new MqttConnectOptions();
		options.setCleanSession(true);
		options.setConnectionTimeout(60);
		options.setKeepAliveInterval(10);
		
		LogManager log_manager = LogManager.getLogManager(); //maintain set of log
		Logger log = log_manager.getLogger(Logger.GLOBAL_LOGGER_NAME);
		
		CertManagementUtil ssl = CertManagementUtil.getInstance();
		options.setSocketFactory(ssl.loadCertificate("C:/Users/Ranac/git/iot-gateway/config/ubidots_cert.pem"));
		options.setUserName("BBFF-29JNJFixHoKIIJPsuAFtbL3R5Bjyce");
		options.setPassword("".toCharArray());
		
		if(!client.isConnected()) {	
			client.connect(options);
		}
//		check for each topic if matched with given than only subscribes and getting vaues from cloud
			if(subtopic == "/v1.6/devices/greenhousehandler/temperatureactuator") {
				client.subscribe(subtopic, 1);
				client.setCallback(new UpdatedCallback());
				Variable temperatureactuator = api.getVariable("5e991ff71d84722e5ce3ef21");
			}
			else if(subtopic == "/v1.6/devices/greenhousehandler/humidityactuator") {
				client.subscribe(subtopic,1);
				client.setCallback(new UpdatedCallback());
				Variable humidityactuator = api.getVariable("5e991fc91d84722e2a095232");
			}
			else if(subtopic == "/v1.6/devices/greenhousehandler/pressureactuator") {
				client.subscribe(subtopic,1);
				client.setCallback(new UpdatedCallback());
				Variable pressureactuator = api.getVariable("5e9921cf1d8472357972b26b");
				}
			else if(subtopic == "/v1.6/devices/greenhousehandler/gasactuator") {
				client.subscribe(subtopic,1);
				client.setCallback(new UpdatedCallback());
				Variable gasactuator = api.getVariable("5e991fba1d84722f8e65486d");
			}
			else if(subtopic == "/v1.6/devices/greenhousehandler/lightactuator") {
				client.subscribe(subtopic,1);
				client.setCallback(new UpdatedCallback());
				Variable lightactuator = api.getVariable("5e9921c31d847233f2546a02");
			}
			else if(subtopic == "/v1.6/devices/greenhousehandler/soilphactuator") {
				client.subscribe(subtopic,1);
				client.setCallback(new UpdatedCallback());
				Variable soilphactuator = api.getVariable("5e9921ed1d847234498eac2a");
			}
			else {
				client.subscribe(subtopic,1);
				client.setCallback(new UpdatedCallback());
				Variable soilmoistureactuator = api.getVariable("5e9922081d847234d3e212ea");
			}
		}
	
	/*
	 * UbiPublish message to publish data on the ubidots cloud with secure connection with ssl. Called in callback function.
	 * 
	 */
	public static void UbiPublish(MqttMessage m, String Ubitopic) throws MqttException {
		System.out.println("welcome to ubidots ****************************");
		MqttClient client = new MqttClient("ssl://industrial.api.ubidots.com:8883","BBFF-29JNJFixHoKIIJPsuAFtbL3R5Bjyce", new MemoryPersistence());
		MqttConnectOptions options = new MqttConnectOptions();
		
		CertManagementUtil ssl = CertManagementUtil.getInstance();
		options.setSocketFactory(ssl.loadCertificate("C:/Users/Ranac/git/iot-gateway/config/ubidots_cert.pem"));
		
		options.setCleanSession(true);
		options.setConnectionTimeout(60);
		options.setUserName("BBFF-29JNJFixHoKIIJPsuAFtbL3R5Bjyce");
		options.setPassword("".toCharArray());
		client.connect(options);
		client.publish(Ubitopic, m);
		
	}
	
	private static Map<String, String> getCustomHeaders() {
		Map<String, String> customHeaders = new HashMap<>();
		customHeaders.put("content-type", "application/json");
		return customHeaders;
	}
	
	private static Map<String, String> prepareHeaders(Map<String, String> arg) {
		Map<String, String> headers = new HashMap<>();
		headers.putAll(getCustomHeaders());
		headers.putAll(arg);
		return headers;
	}
	
	/*
	 * HttpPost to use http api to post on ubidots cloud
	 */
	public static String HttpPost(String path, String message) throws IOException {
		String baseUrl = "http://things.ubidots.com/api/v1.6/";
		String response = null; // return variable
		tokenHeader = new HashMap<>();
		tokenHeader.put("X-AUTH-TOKEN", "BBFF-29JNJFixHoKIIJPsuAFtbL3R5Bjyce");
		Map<String, String> headers = prepareHeaders(tokenHeader);
		try (CloseableHttpClient client = HttpClientBuilder.create().build()) {
			String url = baseUrl +path ;

			HttpPost post = new HttpPost(url);
			for (String name : headers.keySet()) {
				post.setHeader(name, headers.get(name));
			}

			post.setEntity(new StringEntity(message));
			HttpResponse resp = client.execute(post);

			BufferedReader rd = new BufferedReader(new InputStreamReader(resp.getEntity().getContent()));

			StringBuffer result = new StringBuffer();
			String line;

			while ((line = rd.readLine()) != null) {
				result.append(line);
			}

			response = result.toString();
			post.completed();
			client.close();
		} catch (Exception e) {
			e.printStackTrace();
		}

		return response;	
		}

	

}
