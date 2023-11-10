import subprocess
import time
import re

observer_process = subprocess.Popen(["python3", "../deploy.py", "--cluster-home-path", "/root/obcluster"])

time.sleep(1)

ps_command = "ps -ef | grep observer"
ps_output = subprocess.check_output(ps_command, shell=True).decode()
observer_pid = re.search(r"root\s+(\d+)", ps_output).group(1)
print(f"Observer process's pid = {observer_pid}")

perf_command = f"perf record -p {observer_pid} -g -- sleep 61"
subprocess.run(perf_command, shell=True)
print("DONE: record 61s data")

observer_process.wait()

observer_clean = subprocess.Popen(["python3", "../deploy.py", "--cluster-home-path", "/root/obcluster", "--clean"])

observer_clean.wait()

perf_command = f"perf script -i perf.data &> perf.unfold"

subprocess.run(perf_command, shell=True)

flame_graph_command = f"./FlameGraph/stackcollapse-perf.pl perf.unfold &> perf.folded"

subprocess.run(flame_graph_command, shell=True)