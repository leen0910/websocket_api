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

posit1={["j1"]=0,["j2"]=0,["j3"]=0,["j4"]=0,["j5"]=0,["j6"]=0}
posit2={["j1"]=0,["j2"]=0,["j3"]=-100,["j4"]=0,["j5"]=0,["j6"]=0}
posit3={["j1"]=1,["j2"]=-1,["j3"]=0,["j4"]=0,["j5"]=0,["j6"]=0}
posit4={["j1"]=1,["j2"]=-1,["j3"]=0,["j4"]=0,["j5"]=0,["j6"]=0}
posit5={["j1"]=1,["j2"]=-1,["j3"]=0,["j4"]=0,["j5"]=0,["j6"]=0}

while(1)
do
    robot.move_p2p_posit(posit1,vel,blend)
    robot.move_p2p_posit(posit2,vel,blend)
end