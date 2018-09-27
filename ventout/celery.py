from celery import Celery

downloader = Celery('ventout',
             broker='amqp://',
             backend='amqp://',
             include=['ventout.download'])

if __name__ == "__main__":
    downloader.start()