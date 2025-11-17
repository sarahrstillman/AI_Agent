import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        # Build absolute path to the target file
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        working_directory_abs = os.path.abspath(working_directory)

        # Security check: stay inside working_directory
        if not full_path.startswith(working_directory_abs):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Check that it's a regular file
        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        file_size = os.path.getsize(full_path)

        # Read file, possibly truncated
        with open(full_path, "r", encoding="utf-8", errors="replace") as f:
            if file_size > MAX_CHARS:
                content = f.read(MAX_CHARS)
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            else:
                content = f.read()

        return content

    except Exception as e:
        return f"Error: {e}"

