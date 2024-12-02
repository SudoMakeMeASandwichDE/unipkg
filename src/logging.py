import src.vars as vars
from datetime import datetime, timedelta
import os

def log(entry, command=False, output=False, error=False):
    log_file = os.path.join(vars.config_folder, "unipkg.log")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if error:
        log_entry = f"[{timestamp}] ERROR {entry}\n"
    elif output:
        log_entry = f"[{timestamp}] OUTPUT {entry}\n"
    elif command:
        log_entry = f"[{timestamp}] COMMAND {entry}\n"
    else:
        log_entry = f"[{timestamp}] INFO {entry}\n"

    if not os.path.exists(log_file):
        try:
            with open(log_file, 'w'):
                pass
        except Exception as e:
            print(f"Failed to make log file: {str(e)}")
    
    try:
        with open(log_file, "a") as file:
            file.write(log_entry)
    except IOError as e:
        print(f"Failed to write to log file: {str(e)}")

def clean_log():
    file_path = os.path.join(vars.config_folder, "unipkg.log")
    three_days_ago = datetime.now() - timedelta(days=7)
    lines_to_keep = []

    if not os.path.exists(file_path):
        print(f"Log file does not exist: {file_path}")
        return
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    timestamp_str = line.split(']', 1)[0].strip('[')
                    line_date = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                    if line_date >= three_days_ago:
                        lines_to_keep.append(line)
                except (ValueError, IndexError):
                    lines_to_keep.append(line)
    except IOError as e:
        print(f"Failed to read log file: {str(e)}")
        return

    try:
        with open(file_path, 'w') as file:
            file.writelines(lines_to_keep)
    except IOError as e:
        print(f"Failed to clean log file: {str(e)}")
