import requests
import tkinter as tk


root = tk.Tk()
root.geometry('500x500')
root.title('API hub')
chuck_norris_url = 'https://api.chucknorris.io/jokes/random'
trump_api = 'https://www.tronalddump.io/'


def main():
    for widgets in root.winfo_children():
        widgets.destroy()
    chuck_norris_btn = tk.Button(root, text='Chuck Norris', command=lambda: get_joke(chuck_norris_url, chuck_norris_btn))
    chuck_norris_btn.grid(column=1, row=1)
    trump_btn = tk.Button(root, text='Trump', command=lambda: get_joke(trump_api, trump_btn))
    trump_btn.grid(column=2, row=1)
    root.mainloop()


def get_joke(api, btn):
    response = requests.get(api)
    print(response.status_code)
    data = response.json()
    print(data)
    joke = data['value']
    btn.destroy()
    lbl = tk.Label(root, text=joke)
    lbl.pack(anchor='center', expand=True)
    return_btn = tk.Button(root, text='Return', command=main)
    return_btn.pack(anchor='center', expand=True)
    print(joke)


if __name__ == '__main__':
    main()
