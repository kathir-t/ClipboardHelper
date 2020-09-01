import clipboard
from pynput import keyboard

data = ["mkdir gcf_hello_world\ncd gcf_hello_world\nnano index.js\n",
        "/**\n * Cloud Function.\n *\n * @param {object} event The Cloud Functions event.\n * @param {function} callback The callback function.\n */\nexports.helloWorld = function helloWorld (event, callback) {\n  console.log(`My Cloud Function: ${JSON.stringify(event.data.message)}`);\n  callback();\n};\n",
        "gsutil mb gs://vanakkamchennai290420\ngcloud functions deploy helloWorld --stage-bucket vanakkamchennai290420 --trigger-topic hello_world --runtime nodejs6",
        "gcloud functions deploy helloWorld --stage-bucket vanakkamchennai290420 --trigger-topic hello_world --runtime nodejs6\n"]

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