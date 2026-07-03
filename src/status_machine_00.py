import csv
import random

def motion_patrol(x,y):
    action = random.choice(["up","up","up",
                            "down",
                            "left","left",
                            "right","right",
                            "stop"])
    if action == "up":
        y += 1
    elif action == "down":
        y -= 1
    elif action == "left":
        x -= 1
    elif action == "right":
        x += 1
    elif action == "stop":
        pass
    return  x, y, action

def motion_return(x,y):
    if x > 0:
        x -= 1
        action = "left"
    elif x < 0:
        x += 1
        action = "right"
    elif y > 0:
        y -= 1
        action = "down"
    elif y < 0:
        y += 1
        action = "up"
    else:
        action = "stop"

    return  x, y, action,

def low_battery_return(x,y):
    x, y, action = motion_return( x, y)
    return  x, y, action

def battery_protection(mode,battery):
    mode="rest"
    return mode

def motion_status(step,battery):
    step+=1
    battery-=1
    return step,battery

step=0
x=0
y=0
action="start"
battery=0
motion_log=[]
battery=100
mode="patrol"
motion_log=[[0,x,y,action,battery,mode]]
i=random.randint(30,100)
print(f"爬虫想探索{i}步")

while True:
    if mode == "patrol":
        x, y, action = motion_patrol(x, y)
        step,battery = motion_status(step,battery)
        if battery <= 20:
            mode = "low_battery_return"
        elif step >= i:
            mode = "return"

    elif mode == "return":
        x, y, action = motion_return(x, y)
        step, battery = motion_status(step, battery)
        if x==0 and y==0:
            mode = "rest"
        if battery <= 0:
            mode = battery_protection(mode,battery)

    elif mode == "low_battery_return":
        x, y, action = low_battery_return(x, y)
        step,battery = motion_status(step,battery)
        if x==0 and y==0:
            mode="rest"
        if battery <= 0:
            mode = battery_protection(mode,battery)

    print(f"-------------\n"
          f"定位:（{x},{y}）\n"
          f"动作：{action}\n"
          f"状态：{mode}\n"
          f"电量：{battery}%")

    motion_log.append([step, x, y, action, battery, mode])

    if mode == "rest":
        break

with open("data/motion_log_06.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["step","x","y","action","battery","mode"])
    writer.writerows(motion_log)
