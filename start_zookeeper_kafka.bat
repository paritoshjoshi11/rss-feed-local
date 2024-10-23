@echo off

:: Set the title of the terminal window/tab
title Zookeeper and Kafka

:: Start Zookeeper
docker run --name zookeeper -p 2181:2181 -d zookeeper

:: Start Kafka
docker run --name kafka -p 9092:9092 -e KAFKA_ZOOKEEPER_CONNECT=localhost:2181 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 -d confluentinc/cp-kafka

:: Success message
echo Zookeeper and Kafka have been started.
pause
