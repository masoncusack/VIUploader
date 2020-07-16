# Video Indexer Uploader

Trouble with the UI? I built this to allow video uploads to [Video Indexer](https://videoindexer.ai) using simple Python scripts (i.e. your command line).

## Setup

Recommend you use a [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/), e.g.:
```shell
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
```

Install requirements:
```shell
pip3 install -r requirements.txt
```

Rename `.env-dev` to `.env` and fill in the required variables according to your Video Indexer instance. I'll add some guidance on where to find all this information shortly.

## Use

Run `main.py`:
```shell
python3 ./main.py
```

This will require use of the optional `.env` variable `VIDEO_FILEPATH`, but for convenience, there is an optional command line argument to pass in paths videos while variables relating to your video indexer instance remain static:

```shell
python ./main.py -p "path-to-local-video-file"
```