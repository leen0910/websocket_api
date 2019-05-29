
# encoding: utf-8
import os

def total_count(fpath,Block_Size):
    with open(fpath,"r",encoding="utf-8") as f:
        # All_Size=os.path.getsize(fpath)
        All_Size=len(f.read())
        if All_Size%Block_Size!=0:
            total=All_Size//Block_Size+1
        else:
            total=All_Size//Block_Size
        return total


def read_file(fpath,Block_Size):
    with open(fpath,"r",encoding="utf-8") as f:
        while True:
            block = f.read(Block_Size)
            if block:
                yield block
            else:
                return

# fpath='../scripts/move.lua'
# Block_Size =1024
# print(total_count(fpath,Block_Size))
# count=0
# for i in read_file(fpath,Block_Size):
#     print(i)
#     count=count+1
#
# print(count)


