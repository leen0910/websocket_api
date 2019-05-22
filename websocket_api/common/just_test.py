from multiprocessing import process


# def read_in_chunks(filePath, chunk_size=20*1024):
chunk_size=20*1024
filePath = '../scripts/large1.lua'
fo = open(filePath)
while True:
    chunk_data=fo.read(chunk_size)
    print(chunk_data)
    if not chunk_data:
        break
    # yield chunk_data
fo.close()
# if __name__ == "__main__":
#     filePath = '../scripts/large1.lua'
#     read_in_chunks(filePath)

