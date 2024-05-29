from threading import Thread
import os

def run_serveo():
  os.system("bash serveo.sh")

def run_jupyter():
  os.system("echo -e 'e\ne' | jupyter notebook password && jupyter notebook --ip=0.0.0.0 --port=3000 --allow-root --no-browser")

if True:
  Thread(target=run_jupyter).start();
  Thread(target=run_serveo).start();
