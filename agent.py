import requests
'''
a = {"id":"18","title":"post1011","body":"body1011","owner":"admin","comments":[],"categories":[]}



res = requests.get('http://127.0.0.1:8000/member')
print(res.content)'''


import requests
import json
from django.shortcuts import render
from django.http import HttpResponse
import os
import platform
from datetime import datetime
import time
import psutil
import threading



url = 'http://127.0.0.1:8000/host/members'
def cpu():
    threading.Timer(60.0,cpu).start()
    sum_cpu = 0
    data = []
    for process in psutil.process_iter():
        # get all process info in one shot
        with process.oneshot():
            # get the process id
            cpu_usage = process.cpu_percent(interval=0.2)
            sum_cpu = sum_cpu + cpu_usage
            cpu_usage = 0
            pid = process.pid
            if pid == 0:
                # System Idle Process for Windows NT, useless to see anyways
                continue
            # get the name of the file executed
            name = process.name()
            # get the time the process was spawned
            try:
                create_time = datetime.fromtimestamp(process.create_time())
            except OSError:
                # system processes, using boot time instead
                create_time = datetime.fromtimestamp(psutil.boot_time())
            try:
                # get the number of CPU cores that can execute this process
                cores = len(process.cpu_affinity())
            except psutil.AccessDenied:
                cores = 0
            status = process.status()
            try:
                # get the process priority (a lower value means a more prioritized process)
                nice = int(process.nice())
            except psutil.AccessDenied:
                nice = 0
            try:
                # get the memory usage in bytes
                memory_usage = process.memory_full_info().uss
            except psutil.AccessDenied:
                memory_usage = 0
            # total process read and written bytes
            io_counters = process.io_counters()
            read_bytes = io_counters.read_bytes
            write_bytes = io_counters.write_bytes
            # get the number of total threads spawned by this process
            n_threads = process.num_threads()
            # get the username of user spawned the process
            try:
                username = process.username()
            except psutil.AccessDenied:
                username = "N/A"
            all_users = []
            users = psutil.users()
            for user in users:
                one_user = {
                    'name': user.name,
                    'host_one': user.host,
                    
                }
            all_users.append(one_user)
            data ={"program_name":str(name),"program_id":pid,"name":str(all_users[0]["name"]), "host":str(all_users[0]["host_one"]), "cpu_usage":int(sum_cpu),"cores":cores,"status":str(status),"memory_usage":memory_usage}
        # Конвертируем данные в формат JSON
            data_json = json.dumps(data)
            print(data)



        # Отправляем POST-запрос на создание новой записи
            response = requests.post(url, data_json, headers={'Content-type': 'application/json'})
        #response = requests.get(url)

            print(response)

        # Проверяем успешность запроса и выводим ответ
           # if response.status_code == 201:
            #    print('Запись создана успешно!')
            #else:
             #   print('Произошла ошибка:',response)

        #sum_of_cpu,user,host_one = cpu()
        #print(sum_of_cpu," :sum")
    return True
cpu()








