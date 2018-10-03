# Thirdday

1. tf (功能包） 调整机器人各个部位和机身之前的关系
2. rqt_graph 用来分析节点和话题之间的关系
3. rqt 图形化的调试工具


## 机器人建图过程

1. roslaunch turtlebot_gazebo turtlebot_world.launch 启动gazebo的一个虚拟的环境
2. roslaunch turtlebot_gazebo gmapping_demo.launch   启动生成地图的算法
3. roslaunch turtlebot_rviz_launchers view_navigation.launch 启动地图的规划 rviz
4. roslaunch turtlebot_teleop keyboard_teleop.launch 用键盘操控机器人运动

## 自动导航的绘制过程
1. roslaunch mx_bringup rbc_lidar_start.launch 打开激光雷达和地盘
2. roslaunch mx_nav amcl_demo.launch 打开蒙特卡洛定位算法
3. roslaunch mx_rviz amcl_view.launch 打开地图编辑器
4. 在地图上先确定机器人本身的位置，红线就是激光雷达告诉了我们当前机器人附近的障碍物，只有当地图上墙壁的黑线和激光雷达的红线重合的时候才说明我们已经正确确定了乐机器人的初始位置。（用 2d estimate）
5. 使用2D goal nav 确定目标地点及机器人方向。
6. 可以用rqt中 插件中的plungins中的configuration中的dynamic去调试自主导航的各种参数
`
### 实现路径规划的功能包 movebase
机器人在当前环境陷入困境中就无法行走 
1. recover_behaviors 在机器人陷入困境中之后的备选解决方案）
2. global costmap 作为golbl planner 作出抉择的依据
3. local costmap  作为local planner 作出临时抉择的依据
4. base controllr 地盘控制
5. global planner 提前布局
6. local planner  根据现场情况临时抉择


### 保存地图的方法
rosrun map_server 


### 自主导航的参数

TrajectoryPlannerROS:
   max_vel_x: 0.5  # 机器人最大速度
   min_vel_x: 0.05 # 机器人最小速度
   max_vel_y: 0.0  # zero for a differential drive robot
   min_vel_y: 0.0
   max_vel_theta: 0.5  #最大角速度
   min_vel_theta: -0.5 #最小角速度
   min_in_place_vel_theta: 0.4
   escape_vel: -0.1 # 逃逸速度
   acc_lim_x: 2.5
   acc_lim_y: 0.0  # zero for a differential drive robot
   acc_lim_theta: 3.2

   holonomic_robot: false
   yaw_goal_tolerance: 1.2 # about -- degrees 目标地点偏角容错
   xy_goal_tolerance: 0.15  # 10 cm 目标地点位置容错
   latch_xy_goal_tolerance: false
   pdist_scale: 0.65 # 局部规划置信度
   gdist_scale: 0.35 # 全局规划置信度
   sim_time: 2.5 # 仿真时间
   
