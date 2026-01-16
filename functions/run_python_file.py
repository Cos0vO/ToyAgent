import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    abs_working_path = os.path.abspath(working_directory) # 绝对路径-long
    target_path  = os.path.normpath(os.path.join(abs_working_path, file_path)) # 合理的target_path
    is_valid = os.path.commonpath([abs_working_path, target_path]) == abs_working_path # input a list
    if is_valid == False:
        return f'    Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if os.path.isfile(target_path) == False:
        return f'    Error: "{file_path}" does not exist or is not a regular file'
    if file_path[-3:] != '.py':
        return f'    Error: "{file_path}" is not a Python file'
    try:
        command = ["python", target_path]
        if args != None:
            command.extend(args)
        comple_process = subprocess.run(command, capture_output=True, text=True, timeout=30)
        str_out = []
        if comple_process.returncode != 0:
            str_out.append(f"    Process exited with code {str(returncode)}")
        if comple_process.stdout == None and comple_process.stderr == None:
            str_out.append("    No output produced")
        if comple_process.stdout != None:
            str_out.append(f'    STDOUT: {comple_process.stdout}')
        if comple_process.stderr != None:
            str_out.append(f'    STDERR: {comple_process.stderr}')
        return "\n".join(str_out)
    except Exception as e:
        return f'    Error: executing Python file: {e}'
