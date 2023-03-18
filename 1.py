import os

repo_path = '/Users/stanislavmayboroda/Desktop/IT/DevOps/python_hw/'

bash_command = ["cd " + repo_path, "git status"]

result_req = os.popen(' && '.join(bash_command)).read()

for result in result_req.split('\n'):
    if result.startswith('\tmodified:'):
        output = os.path.join(repo_path, result.replace('\tmodified:', 
'').strip())
        print(output)
