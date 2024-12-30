# source this file to start the program as a daemon
sudo setsid python3 -m src.server > logs.txt 2>&1 < /dev/null &
