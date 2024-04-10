import os
import datetime


class Log_writer:
    def __init__(self):
        self.log_file = "C:/users/nicke/IdeaProjects/QuizSelfExercise/log.txt"
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as log:
                log.write("Log file created\n")

    def write_log(self, message):
        with open(self.log_file, 'a') as log:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"{timestamp}: {message}\n")
            print(f"{timestamp}: {message}")

    def clear_log(self):
        with open(self.log_file, 'w') as log:
            log.truncate(0)
