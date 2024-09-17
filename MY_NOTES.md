# 2024 Setup

## WSL Ubuntu-24.04 Environment Setup

- get correct python version
  - Python 3.11.10, documentation released on 6 September 2024.
  - <https://docs.python.org/release/3.11.10/>

```bash
pyenv versions # check if python 3.11 exits
# pyenv install 3.11.10 # install if not available yet
pyenv global 3.11.10
# alternatively
#uv python install 3.11.10
```

- create virtual environment using `uv` because its fast

```bash
# install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
# create environment
uv venv venv --python 3.11.10
# > Using Python 3.11.10 interpreter at: /home/alex/.pyenv/versions/3.11.10/bin/python3.11
# activate it
source venv/bin/activate
# deactivate
```

- install requirements

```bash
uv pip install -r requirements.txt
```
