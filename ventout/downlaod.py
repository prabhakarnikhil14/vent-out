from ventout import celery_down

@celery_down.task
def download_it(content):
    with open('./ventout/static/blog.txt', 'w') as f:
        f.write(content)
    return 'blog.txt'