#!/usr/bin/env python3

import os, sys

repo_path = sys.argv[1]

if not os.path.exists(repo_path):
    print(f'Ошибка в пути!')
    sys.exit(1)

if not os.path.isdir(repo_path):
    print(f'Это не директория!')
    sys.exit(1)

bash_command = f"git -C {repo_path} status"

result_req = os.popen(bash_command).read()


for result in result_req.split('\n'):
    if result.startswith('\tmodified:'):
        output = os.path.join(repo_path, result.replace('\tmodified:', 
'').strip())
        print(output)
