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


# TO RUN THE OCCUPANCY GRID GENERATOR 

```
roslaunch occupancy occupancy_live_rviz.launch
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





