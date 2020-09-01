import clipboard
from pynput import keyboard

data = ["gsutil mb gs://omgind290420/\nwget --output-document ada.jpg https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Ada_Lovelace_portrait.jpg/800px-Ada_Lovelace_portrait.jpg\ngsutil cp ada.jpg gs://omgind290420\ngsutil cp gs://omgind290420/ada.jpg gs://omgind290420/image-folder/\ngsutil acl ch -u AllUsers:R gs://omgind290420/ada.jpg\n",
        "gsutil acl ch -d AllUsers gs://omgind290420/ada.jpg\n"]

maxIndex = len(data)
currentIndex = 0

def on_press(key):
    if str(key) == "Key.scroll_lock":
        global currentIndex, maxIndex
        clipboard.copy(data[currentIndex])
        currentIndex += 1
        if currentIndex == maxIndex:
            print("100% completed")
            exit(0) 

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
listener.join()