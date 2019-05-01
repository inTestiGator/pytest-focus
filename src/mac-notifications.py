import os
# import pync as pync


# Will need to install pync
# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

if __name__== "__main__":
    notify("Error Notification", "python error", "Check your terminal. You have 3 errors!")
