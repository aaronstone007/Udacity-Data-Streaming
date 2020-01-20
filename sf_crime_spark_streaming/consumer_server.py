import asyncio

from confluent_kafka import Consumer

async def consume(topic_name):
    consumer = Consumer({
        'bootstrap.servers': 'PLAINTEXT://localhost:9092',
        'group.id': '0',
    })
    
    consumer.subscribe([topic_name])
    
    while True:
        messages = consumer.consume()
        
        for message in messages:
            if message is None:
                print('Message not found')
            elif message.error() is not None:
                print(f'Error: {message.error()}')
            else:
                print(f'{message.value()}\n')
                
        await asyncio.sleep(1.0)
                
def run_consumer():
    try:
        asyncio.run(consume('police.service.calls'))
        
    except KeyboardInterrupt as e:
        print("Shutting down...")
        
if __name__ == '__main__':
    run_consumer()