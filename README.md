## STORAGE BOXX EXPERIMENTAL AI
This is the optional experimental AI assistant for Storage Boxx. Take note, this is at a very early stage of "I am figuring things out too".
<br><br>

## :ballot_box_with_check: REQUIREMENTS
1) [Python](https://www.python.org/) - Yes, Python. Not PHP. Version 3.9~3.10 works fine at the time of writing.
2) [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/downloads/?q=build+tools)
<br><br>

## :floppy_disk: INSTALLATION
1) Deploy this module *outside of your HTTP folder*. Yes, keep this outside of the "main Storage Boxx folder".
2) Access the GPT4All website, and scroll down to the "Model Explorer". Pick your poison, save your chosen model into `models` folder.
3) Alternatively, here is the [list of available models in JSON](https://github.com/nomic-ai/gpt4all/blob/main/gpt4all-chat/metadata/models.json).
4) Edit `settings.json`, change the model to your own.
5) Run `1-install.bat` (Windows) `1-install.sh` (Linux/Mac). This will automatically:
   - Create a virtual environment and activate it.
   - Download the necessary modules.
6) Put the documents that you want the AI to "learn" in `docs` – This can be CSV, TXT, PDF, HTML, MD, or DOCX.
7) Run `2-create.bat` (Windows) `2-create.sh` (Linux/Mac).
   - This will read all the documents in `docs` and create a database `db`.
   - Try not to overwhelm by putting in too many documents… There’s a limit to how much things can be processed.
8) Copy the pages in `php` into your Storage Boxx folder.

## :rocket: LAUNCH
1) Just run `3-launch.bat` (Windows) `3-launch.sh` (Linux/Mac).
2) This will deploy the bot at `ws://localhost:5678`.
3) Change `settings.json` and `assets/PAGE-ai.js` if you want to deploy it at a different port.
4) Login and access `http://your-site.com/ai`.

## :electric_plug: FRAMEWORKS + LINKS
- [LangChain](https://www.langchain.com/)
- [GPT4ALL](https://gpt4all.io/)
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