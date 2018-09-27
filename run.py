from ventout import app, downloader


if __name__ == '__main__':
    app.run(debug=True)
    downloader.start()
