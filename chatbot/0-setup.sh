php 0-setup.php
virtualenv venv
source "venv/bin/activate"
pip install langchain transformers optimum auto-gptq langchain-experimental mysql-connector-python sentence_transformers Flask pyjwt
if [[ $1 == "CPU" ]]
then
  pip install torch torchvision torchaudio --force-reinstall --index-url https://download.pytorch.org/whl/cpu
  pip install --no-cache-dir --upgrade --force-reinstall llama-cpp-python
else
  pip install torch torchvision torchaudio --force-reinstall
  CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install --no-cache-dir --upgrade --force-reinstall llama-cpp-python
fi
echo "Install complete - Please download your own model before running 1-bot.sh"