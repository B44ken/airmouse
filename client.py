from time import sleep
from requests import get
import pyautogui as gui

logging = True
def log(s):
    if(logging): print(s)

rate = 1/10 # fetch mouse @ 10hz

dx, dy = 0, 0

endpoint='https://vps.p27.ca:443/read/'

print('user key: ', end='')
endpoint += input() + '/'

def get_data(endpoint):
    d = get(endpoint)
    return d.json()

def do_input(data, mouse_scale = 1):
    x = data['mouse']['x'] * mouse_scale
    y = data['mouse']['y'] * mouse_scale
    x -= dx * rate
    y -= dy * rate
    log(f'moving: {x}, {y}')
    gui.move(x, y)
    for k in data['keyboard']['queue']:
        print('got key: ' + k)

def calibrate(time):
    log('calbirating. do not move the device.')
    old = get_data(endpoint)
    oldx = old['mouse']['x']
    oldy = old['mouse']['y']
    sleep(time) 
    new = get_data(endpoint)
    newx = new['mouse']['x'] 
    newy = new['mouse']['y']

    dx = (oldx - newx) / time
    dy = (oldy - newy) / time
    log(f'done. offset  {dx}, {dy}')
    return [dx, dy]

dx, dy = calibrate(5)

while True:
    d = get_data(endpoint)
    do_input(d)
    # sleep(rate)

