#   SMTP "MAIL FROM" message checker
#   Author: Christian Nell
#   Onyen: cnell
#   PID: 7302-29326
#   Date: 8/11/20
#   Purpose: To check a Simple Mail Transfer Protocol "MAIL FROM" message
#               and make sure it is following the correct syntax. This
#               message tells the mail server which person is trying to
#               email a message.
#
#   UNC Honor Pledge: I certify that no unauthorized assistance has been received or
#       given in the completion of this work
#       Signature: _Christian Nell__
import sys
import shutil


def fromParse(string):
    return False


def call_command(string):
    print(string.rstrip())
    return False


def main():
    with open(sys.argv[1], 'r') as my_file:
        for line in my_file:
            call_command(line)
    return False


main()
