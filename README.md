## STORAGE BOXX AI ASSISTANT
This is an optional AI assistant for [Storage Boxx](https://github.com/code-boxx/Storage-Boxx-PHP-Inventory-System) - It can **directly query the database to answer the user's questions**.

Take note, this module is experimental and doesn't always produce expected results.
<br><br>

## :ballot_box_with_check: REQUIREMENTS
1) [Python](https://www.python.org/) - Yes, Python. Not PHP. Version 3.9~3.10 works fine at the time of writing.
2) [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/downloads/?q=build+tools)
3) [CMake](https://cmake.org/)
4) [Nvidia CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit) - If you have an Nvidia graphics card.
5) An Nvidia graphics card with at least 8GB VRAM is highly recommended. You can TRY to run on CPU, but it is painfully slow and practically useless.
<br><br>

## :floppy_disk: INSTALLATION
1) Copy/unzip this module into your existing Storage Boxx folder.
2) I have tried multiple AI models, [codellama-7b-instruct.Q5_K_M.gguf](https://huggingface.co/TheBloke/CodeLlama-7B-Instruct-GGUF/tree/main) is the only one that produced decent(ish) results - Download that into `chatbot/models` or choose a better/larger/smarter model on your own.
3) Edit `chatbot/a_settings.py`, change the `model_name` to your own.
4) *BE WARNED, GIGABYTES WORTH OF DOWNLOAD!* - `0-setup.bat` (Windows) `0-setup.sh` (Linux).

## :rocket: LAUNCH
1) Run `1-bot.bat / 1-bot.sh`, this will deploy the bot at `http://your-site.com:8008`.
2) The Chatbot is accessible at `http://your-site.com/ai` (must be signed in).

## :electric_plug: FRAMEWORKS + LINKS
- [LangChain](https://www.langchain.com/)
- [Transformers](https://huggingface.co/docs/transformers/index)
- [Llama.cpp](https://github.com/ggerganov/llama.cpp)
<br><br>

## :star: SUPPORT
Like this project? Just give it a star. That will indirectly help grow my blog a little bit. :wink:
<br><br>

## :newspaper: LICENSE
Copyright by Code Boxx

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
