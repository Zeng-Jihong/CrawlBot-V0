import csv
import random
i=random.randint(30,100)
print(f"爬虫想探索{i}步")
#定义初始状态
x=0
y=0
action="start"
battery=100
battery_status=True
mode="rest"
motion_log=[[0,x,y,action,battery,mode]]

def motion_patrol(i, x, y, action, battery, mode, motion_log):
    mode="patrol"
    has_return=False
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
        battery=battery_check(battery)
        motion_log.append([step, x, y, action, battery, mode])
        # 低电量自动巡回
        if battery <= 20:
            battery_status ="low"
            step,x,y,battery,motion_log=motion_return(step, x, y, action, battery, mode,motion_log,battery_status)
            has_return=True
            break

    return step,x,y,battery,motion_log,has_return

def motion_return(step,x,y,action,battery,mode,motion_log,battery_status):
    if battery_status=="low" :
        mode = "low_battery_return"
    else:
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
        battery=battery_check(battery)
        battery_status,action,battery,mode=battery_protection(action,battery,mode)
        if battery_status==False:
            break
        motion_log.append([step, x, y, action, battery, mode])
    return step,x,y,battery,motion_log

def battery_check(battery):
    battery-=1
    return battery

def battery_protection(action,battery,mode):
    battery_status = True
    if battery<=0:
        action = "stop"
        mode = "battery_protection"
        battery_status=False
    return battery_status ,action,battery,mode

# 主程序
step,x,y,battery,motion_log,has_return=motion_patrol(i,x,y,action,battery,mode,motion_log)
if has_return==False:
     step,x,y,battery,motion_log=motion_return(step,x,y,action,battery,mode,motion_log,battery_status)

with open("data/motion_log_04.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["step","x","y","action","battery","mode"])
    writer.writerows(motion_log)

