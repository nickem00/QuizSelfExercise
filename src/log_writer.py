import os


class log_writer:
    def __init__(self):
        self.log_file = "../log.txt"
        if not os.path.exists(self.log_file):
            open(self.log_file, 'w').close()

    def write_log(log_file, message):
        with open(log_file, 'a') as log:
            log.write(message + '\n')

    def clear_log(log_file):
        with open(log_file, 'w') as log:
            log.truncate(0)
