# Twitter Sentiment Analysis for Brand

## Project Overview

Twitter is a widely used social media platform, and it generates a large amount of data every day. Sentiment Analysis of this data can be useful for various applications, such as understanding customer opinion on a particular brand. The goal of this project is to address this roblem and provide a solution. This project is a real-time end-to-end Twitter monitoring system which is designed for Moroccan Comapnies / Startups to evaluate Twitter data to inform business decision. To clarify more, this system will be the main motivation to start my own startup **SentilyQ** the purpose of this startuo is to provide some innovation solutions for Moroccan Community. Howeve, the idea behind his project is to allow companies to track and analyze real time tweets, feedbacks about their brand. By tracking these tweets, companies can gain valuable insights and make more informed decisions about their marketing, customer services, and products quality. In other words, this kind of system will help companies to resond quickly to negative comments or feedback, in order to mitigate reputational damage.

## Architecture

![The Architecture of the project](./images/architectureV2.png)


## How to start

To start with the streaming, we must firt run our servers **Zookeeper**, **Kafka**, and **Spark**. We need to open three new terminals and in each, we start different process.

***Terminal 1: Zookeeper***

To run the zookeeper we need to run **zkserver** command on the terminal. Note that by default zookeeper will run port 2181, which is something we can change it on the **zoo.cfg file**

![The zookeeper Server](./images/zkserver.PNG)

***Terminal 2: Kafka server***

To run kafka server, we need to open the folder containing the kafka files and run the following command **.\bin\windows\kafka-server-start.bat .\config\server.properties**, and then the terminal should show a list of text from **Kafka processes**.

![The kafka server](./images/kafka.PNG)

The next step is to create a topic for **Kafka streaming**. We can do this by opening a new terminal and heading to the folder containing Kfaka folders and runnin gthe following command **.\bin\windows\kafka-topics.bat — create — bootstrap-server localhost:9092 — replication-factor 1 — partitions 1 — topic TW_ANALYSIS**, where TW_ANAKYSIS is the name of the topic we are going to use. Note that by default kafka runs in port 9092, which we can change in the **server.properties** files, and also modilfy the Zookeeper default connection port with kafka.


***Terminal 3: Pyspark***

To run spark, we need just to open a new terminal and run run the following command **pyspark**.

![The spark server](./images/pyspark.PNG)
