print("启动")
x=0
y=0
direction="start"
motion_log=[[0,x,y,"start"]]
step=1
for step in range(1,11):
  if step<=5:
       x=x+1
       direction="right"
  else :
      y=y-1
      direction="down"
  motion_log.append([step,x,y,direction])
import csv
with open("data/motion_log.csv",'w',encoding="utf-8",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["step","x","y","direction"])
    writer.writerows(motion_log)
print("完成动作\n数据已记录至data/motion_log.csv")