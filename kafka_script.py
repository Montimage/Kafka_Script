from kafka import KafkaProducer
import json
import sys
#import pdb; pdb.set_trace()
def read_json():
	f = open('json/topology.json')
	
	data=json.load(f)
	
	for i in data['nodes']:
		print(i)
		  
  	# Closing file
	f.close()
	return data
def main():
	if len(sys.argv) < 3:
		# Prompt the user for input if arguments are not provided
		ip = input("Enter value for ip ")
		port = input("Enter value for port number")
	else:
		# Retrieve arguments from the command line
		ip = sys.argv[1]
		port = sys.argv[2]

	# Define the Kafka topic name
	topic_name = 'testTopic'
	print("27")
	# Define the Kafka broker URL and port
	bootstrap_servers = [ip+":"+port]

	# Create a KafkaProducer instance
	producer = KafkaProducer(bootstrap_servers=bootstrap_servers,value_serializer=lambda v: json.dumps(v).encode('utf-8'))

	data= read_json()
	   

	  # Publish the JSON message to the Kafka topic
	producer.send(topic_name, value=data)
	# Wait for the message to be sent and delivery report to be received
	producer.flush()
	# Close the KafkaProducer instance
	producer.close()
	
	
main()

