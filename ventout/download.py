from .celery import downloader
import secrets


@downloader.task
def download_it(content):
    print("I'm running in download first")
    # file = open(secrets.token_hex(8) + '.txt', 'w')
    file = open('result.txt', 'w')
    file.write(content)
    print("I'm running in download second")
    return 'result.txt'
