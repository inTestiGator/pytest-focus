""" Module designed to push notifications to mac screen """
import os
import sys


# The notifier function
def notify(title, subtitle, message):
    """ Send a notification to the user's screen """
    t = "-title {!r}".format(title)
    s = "-subtitle {!r}".format(subtitle)
    m = "-message {!r}".format(message)
    os.system(
        'terminal-notifier {} -activate "com.apple.Terminal"'.format(
            " ".join([m, t, s])
        )
    )


if __name__ == "__main__":
    notify(
        "Failed Test Cases",
        "uh oh!",
        "Check your terminal. You have 3 failed test cases!",
    )
    sys.stdout.write("It appears you have failing test cases...\n")
