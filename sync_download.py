import requests
import tqdm

CHUNK_SIZE = 8192  # recommended default value


def download_files(url: str, filename: str):
    with open(filename, 'wb') as f:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            total = int(r.headers.get('content-length', 0))

            tqdm_params = {
                'desc': url,
                'unit': 'it',
                'miniters': 1,
                'total': total,
                'colour': 'white',
                'unit_scale': True,
                'unit_divisor': 1024,
            }

            with tqdm.tqdm(**tqdm_params) as pb:
                for chunk in r.iter_content(chunk_size=CHUNK_SIZE):
                    pb.update(len(chunk))
                    f.write(chunk)


def main():
    download_files('http://ipv4.download.thinkbroadband.com/50MB.zip', '50MB.zip')


if __name__ == '__main__':
    main()
