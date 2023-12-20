import requests


def main():
    trump_api = 'https://www.tronalddump.io/'
    response = requests.get(trump_api)
    print(response.status_code)
    data = response.json()
    print(data)


if __name__ == '__main__':
    main()
