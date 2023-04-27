import datetime
import logging
import os
import requests
import sys

logging.basicConfig(level=logging.INFO, stream=sys.stdout)


def download(src: str, file: str) -> None:
    """Download src file to filename

    Args:
        src (str): source url
        file (str): filename
    """
    if not os.path.exists(file):
        logging.info(f"Retrieving {file}...")
        response = requests.get(src)
        with open(file, "wb") as output_csv:
            output_csv.write(response.content)
    else:
        logging.info(f"Path exists: {file}")


def main():
    url_prefix = "https://health-infobase.canada.ca/src/data/covidLive/"
    files_list = [
        "covid19-download.csv",
        "covid19-data-dictionary.csv",
        "vaccination-coverage-map.csv",
    ]

    # Get the current time
    now = datetime.datetime.utcnow()

    # Then download the datasets
    for file in files_list:
        if not os.path.exists("data/" + file):
            download(url_prefix + file, "data/" + file)
        else:
            # Get the time of modification for the target file
            last_updated = datetime.datetime.utcfromtimestamp(
                os.path.getctime("data/" + file)
            )

            # If the age of the file is >1 week old,
            # delete the old file and download a new one from the source
            age = now - last_updated

            if age.days > 7:
                logging.info(
                    f"{file} is >1 week old at {age.days} days. Redownloading {file} from source..."
                )
                os.remove("data/" + file)
                download(url_prefix + file, "data/" + file)
            else:
                logging.info(f"{file} is <1 week old at {age.days} days.")


if __name__ == "__main__":
    main()
