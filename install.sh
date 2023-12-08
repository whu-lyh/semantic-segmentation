apt-get update
apt-get install -y libgl1 libglib2.0-0 libx11-6 git

# apex
#git clone https://github.com/NVIDIA/apex.git
cd apex/
#git switch 22.04-dev
pip install -v --disable-pip-version-check --no-cache-dir --no-build-isolation --config-settings "--build-option=--cpp_ext" --config-settings "--build-option=--cuda_ext" ./
cd ..

pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
