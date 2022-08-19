conda info --envs.


venv
---
python -m venv venv
venv/Scripts/activate


package manager
---
poetry init
poetry add uvicorn fastapi pydantic


swagger
--------
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc

gitignore using
------------
https://www.toptal.com/developers/gitignore/
keywords : python,macos,windows,linux,visualstudiocode,vim
handles venv ,toml file etc into gitignore-- check on git status should be disabled

https://www.toptal.com/developers/gitignore/api/python,macos,windows,linux,visualstudiocode,vim


git init

git branch -m main

git checkout -b 1-initial-app-set-up

git add .
git commit -m "first commit with initial API setup"
