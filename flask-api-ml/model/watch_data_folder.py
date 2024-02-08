from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time


class NewDataHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"New file added : {event.src_path}")
            subprocess.run(["python", "run_model_training.py", event.src_path])


if __name__ == "__main__":
    path = "flask-api-ml/model/data"
    event_handler = NewDataHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
