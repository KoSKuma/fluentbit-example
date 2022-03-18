import arrow
import json
import logging
import random
import time

CHANNELS = ['facebook', 'twitter', 'instagram', 'youtube', 'pantip', 'website']

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s][%(levelname)s] %(message)s', datefmt='%Y-%m-%dT%H:%M:%S%z')

while True:
    logging.debug('Debug message 1')
    logging.debug('Debug message 2')

    for channel in CHANNELS:
        inserted_count = random.randint(10, 50)
        log_data = {
            'destination': 'InfluxDB',
            'time': arrow.utcnow().isoformat(),
            'count': inserted_count,
            'channel': channel,
            'country': 'TH',
        }
        print(json.dumps(log_data))

    if random.randint(0, 10) > 5:
        error_log_data = {
            'destination': 'Elasticsearch',
            'time': arrow.utcnow().isoformat(),
            'error': 'Something went wrong',
        }
        print(json.dumps(error_log_data))

    sleep_secs = random.randint(1, 3)
    time.sleep(sleep_secs)
