import requests
import tkinter as tk


def get_joke():
    response = requests.get(f'https://api.chucknorris.io/jokes/random')
    print(response.status_code)
    data = response.json()
    joke = data['value']
    print(joke)


def main():

    root = tk.Tk()
    root.geometry('200x200')
    root.title('API hub')
    chuck_norris_btn = tk.Button(root, text='Chuck Norris', command=get_joke)
    chuck_norris_btn.grid(column=1, row=1)
    root.mainloop()


if __name__ == '__main__':
    main()
