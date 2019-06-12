import time

import os


def main():
    interval = float(os.environ.get('APP_SLEEP_INTERVAL', 5))
    while True:
        print('Hello IoT from Isaax {0}'.format(interval))
        time.sleep(interval)


if __name__ == '__main__':
    main()
