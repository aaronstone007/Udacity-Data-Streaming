import producer_server


def run_kafka_server():
    
    # TODO get the json file path
    input_file = "police-department-calls-for-service.json"

    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic="police.service.calls",
        bootstrap_servers="localhost:9092",
        client_id="consumer-1",
        api_version=(0, 10, 1)
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()
