-- {"move_p2p_posit", move_p2p_posit},
-- {"move_line_pose", move_line_pose},
-- {"move_arc_pose", move_arc_pose},
-- {"wait_move_done", wait_move_done},
-- {"set_default_script", set_default_script},
-- {"set_delay_sec", set_delay_sec},

-- 关节坐标
pose_x=250
length=17.67766953
vel=100;
blend=30;

pose1={["x"] = pose_x, ["y"] =-150, ["z"] = -100,["a"] = 0,["b"] = 0,["c"] = 0}
posem1={["x"] = pose_x, ["y"] =-125-length, ["z"] = -100+length,["a"] = 0,["b"] = 0,["c"] = 0}
pose2={["x"] = pose_x, ["y"] =-150+25, ["z"] = -75,["a"] = 0,["b"] = 0,["c"] = 0}
pose3={["x"] = pose_x, ["y"] =150-25, ["z"] = -75,["a"] = 0,["b"] = 0,["c"] = 0}
posem2={["x"] = pose_x, ["y"] =125+length, ["z"] = -100+length,["a"] = 0,["b"] = 0,["c"] = 0}
pose4={["x"] = pose_x, ["y"] =150, ["z"] = -100,["a"] = 0,["b"] = 0,["c"] = 0}
poset1={["x"] = pose_x, ["y"] =-50, ["z"] = -100,["a"] = 0,["b"] = 0,["c"] = 0}
poset2={["x"] = pose_x, ["y"] =-50+length, ["z"] = -100+length,["a"] = 0,["b"] = 0,["c"] = 0}
poset3={["x"] = pose_x+0.001, ["y"] =0, ["z"] = -75,["a"] = 0,["b"] = 0,["c"] = 0}

posit1={["j1"]=1,["j2"]=-1,["j3"]=0,["j4"]=0,["j5"]=0,["j6"]=0}
robot.move_p2p_posit(posit1,vel,blend)
robot.move_line_pose(pose1,vel,blend)
while(1)
do
	robot.move_arc_pose(posem1,pose2,vel,blend)
	robot.move_line_pose(pose3,vel,blend)
	robot.move_arc_pose(posem2,pose4,vel,blend)
	print("hello")
	robot.move_arc_pose(posem2,pose3,vel,blend)
	robot.move_line_pose(pose2,vel,blend)
	robot.move_arc_pose(posem1,pose1,vel,blend)
end