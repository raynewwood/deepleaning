# deeplearning
video, picture andtime



1、建立rc-local.service文件
sudo gedit /etc/systemd/system/rc-local.service

2、将下列内容复制进rc-local.service文件
[Unit]
Description=/etc/rc.local Compatibility
ConditionPathExists=/etc/rc.local
 
[Service]
Type=forking
ExecStart=/etc/rc.local start
TimeoutSec=0
StandardOutput=tty
RemainAfterExit=yes
SysVStartPriority=99
 
[Install]
WantedBy=multi-user.target

3、创建文件rc.local
sudo gedit /etc/rc.local

4、将下列内容复制进rc.local文件

#!/bin/sh -e

_IP=$(hostname -I)||true
if ["$_IP"]; then
  printf"My IP address is %s\n""$_IP"
fi

sudo /usr/bin/python3 /home/deep/autoIP.py

exit 0

5、给rc.local加上权限

sudo chmod +x /etc/rc.local

6、启用服务
sudo systemctl enable rc-local

7、启动服务并检查状态

sudo systemctl start rc-local.service
sudo systemctl status rc-local.service


设置每2小时运行一次

crontab -e
在键盘上键入“O”开始输入状态
按“ERC”键进入命令状态
输入“:wq”表示写入 退出，完成编辑
0 */2 * * * /usr/bin/python3 /home/nll/autoIP.py
检查状态
crontab -l
此时的显示应该是

0 */2 * * * /usr/bin/python3 /home/nll/autoIP.py

