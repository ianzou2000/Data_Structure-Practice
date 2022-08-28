# 压缩文件
# import zipfile
# with zipfile.ZipFile(zip文件名, "w", zipfile.ZIP_DEFLATED) as zf:
#   zf.write(要压缩的文件名，zip文件中的文件名)

# 解压文件
# with zipfile.ZipFile(zip文件名) as zf:
#     zf.extractall()

import zipfile

# 压缩文件
with zipfile.ZipFile('dream.zip', "w", zipfile.ZIP_DEFLATED) as zf:
    zf.write('dream.txt', 'dream2.txt')

# 解压文件
with zipfile.ZipFile('dream.zip') as zf:
    zf.extractall()