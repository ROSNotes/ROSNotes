# Second day 

## Git 操作基础命令

git clone 克隆远程仓储
git status 仓储状态
git pull 拉远程仓储. 
3. 编译 工作空间的根目录 catkin_make
4. 创建ROS工作包 catkin_create_pkg turtlesim_bringup rpspy
5. launch 文件格式 
<launch>
  <node name="talker" pkg="rospy_tutorials" type="talker" />
</launch>

## ROS 结构
publisher --- topic --- subscriber
rqt_graph 节点关系图

ROS master 节点管理器
ROS node   节点
ROS topic  话题
ROS msg    消息
list       列出话题
find       通过type找到话题
info       列出关于节点或者话题的基本信息
pub        给话题发布消息



## launch 文件的关键词
1. pkg  表示该节点所在的功能包
2. type 表示该节点的实际名字（就是开发时候所起的名字）
3. name 也是该节点的名字，在launch文件中更换名字会覆盖原来launch文件的名字

## git推送
1. git add . 添加当前目录所有更改
2. git commit -m “ 备注 ” 
3. git push  推送
4. 输入你的用户名和密码。

## 
