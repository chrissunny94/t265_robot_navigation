# T265 Robot Navigation



## Pre requisites 

```
sudo apt install python-catkin-tools
```


Build from source


```
mkdir ~/realsense_ws/src -p
cd ~/realsense_ws/src
git clone https://github.com/chrissunny94/t265_robot_navigation
cd ..
catkin build
source devel/setup.bash

```


To run the **Occupancy Grid Generator**

```
roslaunch occupancy occupancy_live_rviz.launch
```

To run **Depthimage_to_laserscan** 

```
roslaunch doozy_localization depth_to_laserscan.launch
```

To run **move_base**
(please save map in maps folder and change map file name in move_base_demo.launch file.....If we are using real robot, then change parameter of robot_base_frame from t265_link to base link)

```
roslaunch doozy_navigation move_base_demo.launch
```



#
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Launch the following command to spawn robot's urdf in **gazebo** test world with Realsense D435 & Realsense T265 attached to it in front along with a RPLidar in the middle of the robot
```
roslaunch doozy_description gazebo.launch
```


To visualize in **rviz**
```
roslaunch doozy_description display.launch
```

For **keyboard teleop**
```
rosrun teleop_twist_keyboard teleop_twist_keyboard.py 
```

For **Gmapping**
```
roslaunch doozy_localization gmapping.launch
```

For **Hector slam**
```
roslaunch doozy_localization hector_slam.launch
```





