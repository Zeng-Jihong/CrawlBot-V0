import csv
import random
i=random.randint(10,30)
print(f"爬虫想探索{i}步")
x=0
y=0
action="start"
battery=100
mode="patrol"
motion_log=[[0,x,y,action,battery,mode]]

def motion_patrol(i,x,y,action,battery,mode,motion_log):
    mode="patrol"
    for step in range(1,1+i):
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
        battery=battery-1
        if battery<=0:
            action = "stop"
            mode = "low_battery"
            motion_log.append([step, x, y, action, battery, mode])
            break
        motion_log.append([step,x,y,action,battery,mode])
    return step,x,y,battery,motion_log
step,x,y,battery,motion_log=motion_patrol(i,x,y,action,battery,mode,motion_log)

def motion_return(step,x,y,action,battery,mode,motion_log):
    mode="return"
    while x!=0 or y!=0:
        if x > 0:
            x -= 1
            action = "left"
        elif x < 0:
            x += 1
            action= "right"
        elif y > 0:
            y -= 1
            action= "down"
        elif y < 0:
            y += 1
            action= "up"
        else:
            action= "stop"
        step += 1
        battery -= 1
        if battery<=0:
            action = "stop"
            mode = "low_battery"
            motion_log.append([step,x,y,action,battery,mode])
            break
        motion_log.append([step, x, y, action, battery, mode])
    return step,x,y,battery,motion_log

motion_return(step,x,y,action,battery,mode,motion_log)

with open("data/motion_log_02.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["step","x","y","action","battery","mode"])
    writer.writerows(motion_log)
