# T265 Robot Navigation


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





