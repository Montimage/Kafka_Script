# Script to send json information to Kafka Bus



------------------




This script takes three arguments as input: 

~~~
          1. Ip of KafkaBus
          2. Port of KafkaBus(Default port is 9092)
          3. Name of json file to send(ex. info)
~~~

An example of utilization is the following one:
```
 python kafka_script.py localhost 9092 info
 
```
The json file is composed of 4 elements : topology, attacks, remediation and vulnerabilities.

The **topology** field refers to 5G architecture and it has different field: topology_id,topology_name, topology_description, nodes. Each node has an id, a textual description and the list of the connections with the other nodes.

The **attacks** field refer to the exploit developed in Sancus project. Each attack is identified by a number, then there is a description about how it works, the likelyhood, the impact, the linked vulnerabilities and the linked nodes.

The **remediations** field indicate the strategies to mitigates vulnerabilities/threat discovered in previous stages. Each remediation if made up of an id, a short description, a description, a monetary cost.

The **vulnerabilitied** field indicate all the weaknesses/ flaws in 5G Nokia servers. Each vulnerability has an id, a description, a reference, a likelihood, an integer indicating the impact on the service, and the list of the nodes involved.
