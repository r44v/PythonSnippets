import threading
import time


def callback(wait, say):
    time.sleep(wait)
    print(say)


thread = threading.Thread(target=callback, args=(3, 'I come from another thread'))
thread.daemon = False  # Daemonize thread ## Nice explantion about daemon threads : https://stackoverflow.com/a/190017
thread.start()         # Start the execution

print("I am from the main thread")
time.sleep(6)
print("Main thread again saying goodbye")
