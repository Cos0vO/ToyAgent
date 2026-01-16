import os

def write_file(working_directory, file_path, content):
    abs_working_path = os.path.abspath(working_directory) # 绝对路径-long
    target_path  = os.path.normpath(os.path.join(abs_working_path, file_path)) # 合理的target_path
    is_valid = os.path.commonpath([abs_working_path, target_path]) == abs_working_path # input a list
    if is_valid == False:
        return f'    Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(target_path) == True:
        return f'    Error: Cannot write to "{file_path}" as it is a directory'
    try:
        os.makedirs(os.path.dirname(target_path), exist_ok=True) # auto补全需要的目录
        with open(target_path, "w") as f:
            f.write(content)
            return f'    Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'    Error: {str(e)}'
