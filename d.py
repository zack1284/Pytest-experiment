import subprocess

# Replace these with your actual credentials and repository details
username = 'zack1284'
password = 'ASDFasdf0203'
repository_url = 'git@github.com:zack1284/Pytest-experiment.git'
branch_name = 'test'  # Replace with the appropriate branch name

# Add and commit changes using Git CLI
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'upload'])

# Push changes to the remote repository using HTTPS URL with credentials
push_command = ['git', 'push', repository_url, branch_name]
push_input = f'{username}\n{password}\n'
subprocess.run(push_command, input=push_input, text=True)
