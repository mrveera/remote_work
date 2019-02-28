#!/usr/bin/env bash
abs_path=`dirname $BASH_SOURCE`
say -v Samantha $1

if [[ ! -d ~/.venvs/remote_work ]]; then
		virtualenv ~/.venvs/remote_work
        source ~/.venvs/remote_work/bin/activate
		pip install SpeechRecognition
		brew install portaudio
		pip install pyaudio
		deactive
else
		echo "Virtual env already existed"
fi


source ~/.venvs/remote_work/bin/activate

python ${abs_path}/main.py
if [ "$?" == "83372" ]; then
    echo "updated"
else
    echo "Both Strings are not Equal."
fi
