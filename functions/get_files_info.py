def get_files_info(working_directory, directory="."):
    abs_working_path = os.path.abspath(working_directory) # 绝对路径-long
    target_dir = os.path.normalpath(os.path.join(abs_working_path, directory)) # 合理的target_path
    is_valid = os.path.commonpath([abs_working_path, target_dir]) == abs_working_path # input a list
    if is_valid == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if os.path.isdir(directory) == False:
        return f'Error: "{directory}" is not a directory'
    try:
        files = os.path.listdir(target_dir) # 获取目标文件夹的内容,ls返回
        for file in files:
            file_path = join(target_dir, file)
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            print(f"- {file}: file_size={file_size} bytes, is_dir={is_dir}")
    except Exception as e:
        print(f"Error: {str(e)}")
