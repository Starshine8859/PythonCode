import subprocess
import os
from datetime import datetime, timedelta

def git_commit(date: str, comment: str, branch: str = "main"):
    """
    Creates a backdated empty commit and pushes it to the given branch.
    
    Parameters:
        date (str): Date in ISO format (e.g., '2025-04-16T12:00:00')
        comment (str): Commit message
        branch (str): Branch name to push to (default: 'main')
    """
    # Set up environment with backdated commit info
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date
    env["GIT_COMMITTER_DATE"] = date

    print(f"[*] Creating fake commit dated {date} with message: '{comment}'")
    
    # Create an empty commit
    commit_result = subprocess.run(
        ["git", "commit", "--allow-empty", "-m", comment],
        env=env,
        capture_output=True,
        text=True
    )

    if commit_result.returncode != 0:
        print("[!] Commit failed:\n", commit_result.stderr)
        return False

    print("[+] Commit created successfully.")

    # Push the commit to the remote
    push_result = subprocess.run(
        ["git", "push", "origin", branch],
        capture_output=True,
        text=True
    )

    if push_result.returncode != 0:
        print("[!] Push failed:\n", push_result.stderr)
        return False

    print("[+] Commit pushed to origin/" + branch)
    return True

def get_date_range(start_date: str, end_date: str, format: str = "%Y-%m-%d"):
    """
    Generates a list of dates from start_date to end_date (inclusive).
    
    Parameters:
        start_date (str): e.g., '2025-04-01'
        end_date (str): e.g., '2025-04-05'
        format (str): date string format (default: '%Y-%m-%d')
        
    Returns:
        List of date strings in the given format.
    """
    start = datetime.strptime(start_date, format)
    end = datetime.strptime(end_date, format)

    date_list = []
    while start <= end:
        date_list.append(start.strftime(format))
        start += timedelta(days=1)

    return date_list




for date in get_date_range("2025-06-02","2025-06-06"):
    git_commit(f"{date}T12:00:00" , 'Add new sub project' )
    
for date in get_date_range("2025-06-02","2025-06-06"):
    git_commit(f"{date}T12:00:00" , 'Update new sub project' )
    
for date in get_date_range("2025-06-02","2025-06-06"):
    git_commit(f"{date}T12:00:00" , 'solved porject issue' )
    
for date in get_date_range("2025-06-02","2025-06-06"):
    git_commit(f"{date}T12:00:00" , 'solved porject issue' )