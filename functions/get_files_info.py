import os
from google.genai import types


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

def get_files_info(working_directory, directory):
    abs_working_path = os.path.abspath(working_directory) # 绝对路径-long
    target_dir = os.path.normpath(os.path.join(abs_working_path, directory)) # 合理的target_path
    is_valid = os.path.commonpath([abs_working_path, target_dir]) == abs_working_path # input a list
    if is_valid == False:
        return f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if os.path.isdir(target_dir) == False:
        return f'    Error: "{directory}" is not a directory'
    try:
        ls = []
        files = os.listdir(target_dir) # 获取目标文件夹的内容,ls返回
        for file in files:
            file_path = os.path.join(target_dir, file)
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            ls.append(f"  - {file}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(ls)
    except Exception as e:
        return f"    Error: {str(e)}"
