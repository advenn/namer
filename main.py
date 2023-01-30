import os


def filenamer():
    custom_name = 'name.ext'
    count = 1
    if os.path.exists(custom_name):
        while True:
            custom_name2 = 'name ({count}).ext'
            if not os.path.exists(custom_name2.format(count=count)):
                return custom_name2.format(count=count)
            else:
                count += 1
