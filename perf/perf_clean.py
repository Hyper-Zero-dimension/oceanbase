import subprocess

clean_data_command = "rm -f perf.*"

subprocess.run(clean_data_command, shell=True)