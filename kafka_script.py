from kafka import  KafkaConsumer,KafkaProducer
from kafka.admin import KafkaAdminClient,NewTopic
import json
import sys

#import pdb; pdb.set_trace()
def read_json(namefile):
	f = open("json/"+namefile+".json")
	
	data=json.load(f)
	
	for i in data['nodes']:
		print(i)
		  
  	# Closing file
	f.close()
	return data

# Check if any message exists in topic and update with new message
def check_and_update_message(topic_name, consumer,producer,data):

	if consumer.poll(0):
        # Messages exist, delete the first one and update with new message
		for msg in consumer:
			producer.send(topic_name, b'', partition=msg.partition, offset=msg.offset)
			producer.flush()
			producer.send(topic_name, value=data)
		    	# Wait for the message to be sent and delivery report to be received
			producer.flush()
			# Close the KafkaProducer instance
			producer.close()
			break
	else:
		# No messages exist, simply send the new message to the topic
		producer.send(topic_name, value=data)
		# Wait for the message to be sent and delivery report to be received
		producer.flush()
		# Close the KafkaProducer instance
		producer.close()

def main():
	if len(sys.argv) < 4:
		# Prompt the user for input if arguments are not provided
		ip = input("Enter value for ip ")
		port = input("Enter value for port number")
		namefile=input("Enter value for port number")
	else:
		# Retrieve arguments from the command line
		ip = sys.argv[1]
		port = sys.argv[2]
		namefile= sys.argv[3]


	# Define the Kafka broker URL and port
	bootstrap_servers = [ip+":"+port]
	# Define the Kafka topic name
	topic_name = 'testTopic'
	admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)


	topic_metadata = admin_client.list_topics()
	topic_exists = topic_name in topic_metadata


	if not topic_exists:
	    topic_partitions = 1
	    topic_replication_factor = 1
	    new_topic = NewTopic(name=topic_name, num_partitions=topic_partitions, replication_factor=topic_replication_factor)
	    admin_client.create_topics([new_topic])
	    print('Created new topic:', topic_name)
	else:
	    print('Topic already exists:', topic_name)
	consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers, auto_offset_reset='earliest', enable_auto_commit=True, group_id='my-group')

	# Create a KafkaProducer instance
	producer = KafkaProducer(bootstrap_servers=bootstrap_servers,value_serializer=lambda v: json.dumps(v).encode('utf-8'))

	data= read_json(namefile)
	   
	check_and_update_message(topic_name,consumer,producer,data)

	
	
main()

