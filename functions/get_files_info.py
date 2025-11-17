import os

def get_files_info(working_directory, directory="."):
    try:
        # Step 1: Build the full path
        full_path = os.path.abspath(os.path.join(working_directory, directory))

        # Step 2: Security check — full_path must stay inside working_directory
        working_directory_abs = os.path.abspath(working_directory)

        if not full_path.startswith(working_directory_abs):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Step 3: Check if directory exists and is a real directory
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        # Step 4: List directory contents
        entries = []
        for name in os.listdir(full_path):
            entry_path = os.path.join(full_path, name)

            is_dir = os.path.isdir(entry_path)
            size = os.path.getsize(entry_path)

            entries.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")

        # Step 5: Join into a single string to return
        return "\n".join(entries)

    except Exception as e:
        return f"Error: {e}"
