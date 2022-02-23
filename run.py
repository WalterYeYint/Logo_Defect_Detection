import os
import threading
import time

def second_thread(n, name):
	print("Running second thread...")
	time.sleep(5)
	os.system("python main.py")

t = threading.Thread(target=second_thread, name='second_thread', args=(5, 'second_thread'))
t.start()
# t.join()
os.system("python API_project/Database_api/manage.py runserver")

