import requests


def main():

    response = requests.get(f'https://api.chucknorris.io/jokes/random')
    print(response.status_code)
    data = response.json()
    joke = data['value']
    print(joke)


if __name__ == '__main__':
    main()
