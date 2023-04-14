import difflib
import io
import json

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
    return render(request, 'index.html', {'info': info})



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
    return render(request, 'disk.html', {'disks': disks})

import requests
def users(request):
    all_users = []
    ''' [suser(name='Fan', terminal=None, host=None, started=1595661568.4721968, pid=None)]
     users = psutil.users()
    for user in users:
        one_user = {
            'name': user.name,
            'host': user.host,
            'started': datetime.fromtimestamp(user.started)
        }
        all_users.append(one_user)'''
    res = requests.get('http://127.0.0.1:8000/member')
    print(res.content)
    all_users  = json.loads(res.content)
    return render(request, 'users.html', {'users': all_users})

   


def diff(request):
    print("Запроса: ", request.method)
    if request.method == 'POST':
        files = request.FILES
        content1 = files.get('filename1').read()
        content2 = files.get('filename2').read()

        if get_md5(content1) == get_md5(content2):
            return HttpResponse("оК")
        else:
            hdiff = difflib.HtmlDiff()
            content1 = content1.decode('utf-8').splitlines()
            content2 = content2.decode('utf-8').splitlines()
            result = hdiff.make_file(content1, content2)  
            return HttpResponse(result)
    return render(request, 'diff.html')

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
    return render(request, 'monitor.html', {'processes': processes})


def apidatas(request):
    return render(request, 'apidatas.html')

def about(request):
    return render(request, 'about.html')

def auth(request):
    return render(request, 'auth.html')

from django.shortcuts import render
from .models import Members


#from .serializers import UserSerializer
#from .models import Members
#def get_date_from_bd(request):
 #   mem = Members.objects.all().order_by('name')
 #   context = {'mem': mem}
  #  serializer_class = UserSerializer
  #  return render(request, 'host/members.html', {'mem':mem})

from rest_framework import generics
from . import serializers
from .models import Members


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Members,all_users_data
from .serializers import MemberSerializer,all_memberSerializer
from collections import namedtuple


nt = namedtuple("object", ["model", "serializers"])
pattern = {
#"member" : nt(Members, MemberSerializer),
"members": nt(all_users_data, all_memberSerializer)
}
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


@api_view(["GET", "POST"])
def ListView(request, api_name): 

    object = pattern.get(api_name, None)
    if object == None:
        return Response(
    data = "Invalid URL",
    status = status.HTTP_404_NOT_FOUND,
    )
    if request.method == "GET":
        object_list = object.model.objects.all()
        serializers = object.serializers(object_list, many=True)
        return Response(serializers.data)

    if request.method == "POST":
        #data = request.data
        #stream = io.BytesIO(json)
        #data = JSONParser().parse(stream)
       # json = JSONRenderer().render(serializers.data)
        #serializers = object.serializers(data=data)            
        serializer =all_memberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors) 

    if not serializers.is_valid():
     return Response(
        data = serializers.error,
        status = status.HTTP_404_NOT_FOUND
    )
    serializers.save()
    return Response(
        data = serializers.error,
        status = status.HTTP_201_CREATED
)