## virtual-assistant
Virtual Assistan Bot

## install separate libs
First of all you need to install the Pytorch library.
For every OS there is a different type of installation:

Windows:
pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
Instalation with conda:
conda install pytorch torchvision cpuonly -c pytorch

MacOS:
pip install torch torchvision
Instalation with conda:
conda install pytorch torchvision -c pytorch

Linux:
pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
Instalation with conda:
conda install pytorch torchvision cpuonly -c pytorch

If you are on linux, install libasound for PyAudio compatibility   
(source: http://portaudio.com/docs/v19-doxydocs/compile_linux.html)
sudo apt-get install libasound-dev

## install libs
pip3 install -r requirements.txt

## to open the bot just type in main folder:
python3 main.py


the commands for bot responses are in ./src/data/data.json
