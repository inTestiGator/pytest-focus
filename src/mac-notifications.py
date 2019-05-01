import os
# import pync as pync


# Will need to install pync
# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

pync.remove_notifications(os.getpid())

pync.list_notifications(os.getpid())

Notifier.notify('Hello World')
Notifier.notify('Hello World', title='Python')
Notifier.notify('Hello World', group=os.getpid())
Notifier.notify('Hello World', activate='com.apple.Safari')
Notifier.notify('Hello World', open='http://github.com/')
Notifier.notify('Hello World', execute='say "OMG"')

Notifier.remove(os.getpid())

Notifier.list(os.getpid())
