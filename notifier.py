from winotify import Notification, audio

def show_notification(title, message):
    toast = Notification(
        app_id="Breakify Notifier",
        title=title,
        msg=message,
        duration="short"
    )
    toast.set_audio(audio.Default, loop=False)
    toast.show()