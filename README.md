1. 建立环境
virtualenv -p $(which python3) py3env
2. 开启py3env 环境
. py3env/bin/active
3. 安装Django
pip install Django
4. 冻结环境
pip freeze > requirement.txt
