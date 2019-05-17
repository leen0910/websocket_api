pose_ref= {["x"] = 250, ["y"] =250, ["z"] = 0,["a"] = 0,["b"] = 0,["c"] = 0}
pose_world={["x"] = 0, ["y"] =0, ["z"] = 0,["a"] = 0,["b"] = 0,["c"] = 0}

vel=50
blend=50
pose1={["x"] = 0, ["y"] =0, ["z"] = 0,["a"] = 0,["b"] = 0,["c"] = 0}

pose2 = {["x"] = 300, ["y"] =0, ["z"] = 0,["a"] = 0,["b"] = 0,["c"] = 0}

posit1={["j1"]=0,["j2"]=0,["j3"]=0,["j4"]=0,["j5"]=0,["j6"]=0}
posit2={["j1"]=1,["j2"]=-1,["j3"]=0,["j4"]=0,["j5"]=0,["j6"]=0}

while(1)
do
    robot.set_ref_frame(pose_ref)
    robot.move_p2p_pose(pose1,vel,blend)
    --robot.set_ref_frame(pose_world)
    robot.move_p2p_pose(pose2,vel,blend)
end