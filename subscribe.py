from google.cloud import pubsub_v1
import time
import os

if __name__ == "__main__":

    # Replace 'my-service-account-path' with your service account path
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/Users/Cris/code/cristianlagranda/gcp/udemypubsub-7ada4e500482.json'

    # Replace 'my-subscription' with your subscription id
    subscription_path = 'projects/udemypubsub/subscriptions/Topic2-sub'

    subscriber = pubsub_v1.SubscriberClient()

    def callback(message):
        print(('Received message: {}'.format(message)))
        message.ack()

    subscriber.subscribe(subscription_path, callback=callback)

    while True:
        time.sleep(60)
