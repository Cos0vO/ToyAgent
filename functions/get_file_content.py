import os
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(

)


def get_file_content(working_directory, file_path):
    abs_working_path = os.path.abspath(working_directory) # 绝对路径-long
    target_path  = os.path.normpath(os.path.join(abs_working_path, file_path)) # 合理的target_path
    is_valid = os.path.commonpath([abs_working_path, target_path]) == abs_working_path # input a list
    if is_valid == False:
        return f'    Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if os.path.isfile(target_path) == False:
        return f'    Error: "File not found or is not a regular file: "{file_path}"'
    try:
        MAX_CHARS = 10000
        with open(target_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string
    except Exception as e:
        return f"    Error: {str(e)}"
