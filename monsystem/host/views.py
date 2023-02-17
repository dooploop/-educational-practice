import difflib

from django.shortcuts import render
from django.http import HttpResponse
import os
import platform
from datetime import datetime
import time
import psutil

# Create your views here.

from host.tools import get_md5


def index(request):
    try:
        system_info = os.uname()
        node = system_info.nodename
        system = system_info.sysname
    except Exception as e:
        system_info = platform.uname()
        node = system_info.node
        system = system_info.system

    boot_time = psutil.boot_time()
    boot_time = datetime.fromtimestamp(boot_time)
    now_time = datetime.fromtimestamp(time.time())
    info = {
        'node': node,
        'system': system,
        "kernel_name": system,
        'release': system_info.release,
        'version': system_info.version,
        'machine': system_info.machine,
        'now_time': now_time,
        'boot_time': boot_time,
        'boot_delta': now_time - boot_time
    }
    return render(request, 'host/index.html', {'info': info})



def disk(request):
    parts = psutil.disk_partitions()
    disks = []
    for part in parts:
        usage = psutil.disk_usage(part.device)
        disk = {
            'device': part.device,
            'mountpoint': part.mountpoint,
            'fstype': part.fstype,
            'opts': part.opts,
            'total': usage.total,
            'percent': usage.percent
        }
        disks.append(disk)
    return render(request, 'host/disk.html', {'disks': disks})


def users(requests):
    all_users = []
    # [suser(name='Fan', terminal=None, host=None, started=1595661568.4721968, pid=None)]
    users = psutil.users()
    for user in users:
        one_user = {
            'name': user.name,
            'host': user.host,
            'started': datetime.fromtimestamp(user.started)
        }
        all_users.append(one_user)
    return render(requests, 'host/users.html', {'users': all_users})



def diff(request):
 
    print("Запроса: ", request.method)
    if request.method == 'POST':
        files = request.FILES
        content1 = files.get('filename1').read()
        content2 = files.get('filename2').read()

        if get_md5(content1) == get_md5(content2):
            return HttpResponse("文件内容一致")
        else:
            hdiff = difflib.HtmlDiff()
            content1 = content1.decode('utf-8').splitlines()
            content2 = content2.decode('utf-8').splitlines()
            result = hdiff.make_file(content1, content2)  
            return HttpResponse(result)
    return render(request, 'host/diff.html')

def dicttolist(dict):
    listmain = []
    for lists in dict:
        l1 = list(lists.values())
       # print(l1)
        listmain.append(l1)
    return listmain

def monitor(request):
    # the list the contain all process dictionaries
    processes = []
    for process in psutil.process_iter():
        # get all process info in one shot
        with process.oneshot():
            # get the process id
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
            # get the CPU usage percentage
            cpu_usage = process.cpu_percent(interval=0.1)
            # get the status of the process (running, idle, etc.)
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
            
        processes.append({
            'program_id': pid, 
            'name': name, 
            'create_time': create_time,
            'cores': cores,
             'cpu_usage': cpu_usage, 
             'status': status, 
             'Приоритет': nice,
            'memory_usage': memory_usage, 
            'n_threads': n_threads
        })
             
       # print(cpu_usage)
   # return processes
   # processes = dicttolist(processes)
    return render(request, 'host/monitor.html', {'processes': processes})


def about(request):
    return render(request, 'host/about.html')

def auth(request):
    return render(request, 'host/auth.html')






