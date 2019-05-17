-- {"move_p2p_posit", move_p2p_posit},
-- {"move_line_pose", move_line_pose},
-- {"move_arc_pose", move_arc_pose},
-- {"wait_move_done", wait_move_done},
-- {"set_default_script", set_default_script},
-- {"set_delay_sec", set_delay_sec},

-- 关节坐标
pose_x=300
length=17.67766953
vel=100;
blend=0;

pose1={["x"] = 250, ["y"] =0, ["z"] = -50,["a"] = 0,["b"] = 0,["c"] = 0}
posem1={["x"] = 300, ["y"] =50, ["z"] = -50,["a"] = 0,["b"] = 0,["c"] = 0}
pose2={["x"] = 350, ["y"] =0, ["z"] = -50,["a"] = 0,["b"] = 0,["c"] = 0}
posem2={["x"] = 300, ["y"] =-50, ["z"] = -50,["a"] = 0,["b"] = 0,["c"] = 0}

posit1={["j1"]=1,["j2"]=-1,["j3"]=0,["j4"]=0,["j5"]=0,["j6"]=0}
robot.move_p2p_posit(posit1,vel,blend)
robot.move_line_pose(pose1,vel,blend)
while(1)
do
	robot.move_arc_pose(posem1,pose2,vel,blend)
	robot.move_arc_pose(posem2,pose1,vel,blend)

end