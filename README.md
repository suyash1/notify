### Notify: event-based pub-sub microservice

This python demo aims to demonstrate event-driven pub-sub architecture using rabbitmq.

#### Architecture
There are two proposed architecture which aims to leverage the existing push notification functionality.
Both the architectures assumes that there is a database which contains information about pilot and his scheduled delivery to customers.
This table will be referred by the consumer process to trigger push notifications for the current pilot and scheduled users' devices.

##### Assumption
* Delivery job table
* customer_id, device_id and application_provider lookup 


##### Schema and Approach 
As soon as pilot sends the message, the file uploader service uploads the audio file to S3 bucket.
The file path to S3 bucket is stored in a relational database (e.g., RDS) with pilot_id, delivery_job_id (FK) and media path.
The notification service is triggered next which:

* ###### Approach 1
    fetches SNS arn and token for a customer_id who is scheduled for the delivery and
    send out push notification to SNS topic with message metadata with embedded audio file download path
    
    Advantage: SNS does all the application provider routing, retries, application provider interactions etc.
    AWS managed ad monitored services which reduces operational overhead on developers.  

* ###### Approach 2
    fetches all the information as mentioned in approach 1, except,
    it send then message to a kafka topic which is then consumed by a consumer / consumer group
    and is send out to the application providers based upon customer id and device lookup
    
    Advantage: Main advantage is you don't need to store arn mapping, which would be significantly larger when the customer base grows and have substantial number of customizations in push notifications
    
##### Demo Usage:
* This demo assumes RabbitMQ is installed on local system and running on 5672.
If not, please refer to [installation on ubuntu](https://tecadmin.net/install-rabbitmq-server-on-ubuntu/) or 
[installation on mac](https://www.rabbitmq.com/install-homebrew.html)
* Login to RabbitMQ management console `http://localhost:15672` and create an `Exchange` with subscription queue and routing key.
Please refer to [this tutorial](https://www.youtube.com/watch?v=eic-CUNdLLA)
* Create a python virtual environment using `python 3` and activate it
* Clone the project
* Install the requirements `pip install -r requirements.txt`
* Run the flask server as `python runserver.py`
* Now, open two separate terminals / tabs and activate virtual env in both.
In one tab, go to `../notify/voice_note/consumer/` and run the consumer process by `python consumer.py`
In the other tab, go to `../notify/voice_note/` and run the file `python sound_rec.py`.

   `sound_rec.py` simulates the voice recording from device and once the recording is done, it stores file locally in same directory.
   In this demo, only the message passing to consumer is demonstrated.
* After recording sound, `sound_rec.py` triggers notify API to publish the message to topic in rabbitmq. The message consists of random pilot_id and file_path (file name in this instance)