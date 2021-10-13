# tellme
### (build is working!)

Simple little script (for now) that will send you a Telegram message when you add it as a pipe in a command.

## Dependencies:
- Check requirements.txt
- pyTelegramBot
- grep

## Setup:
- install python packages from requirements.txt
- run ``` ./install.sh ```

## Running example
You can add it as a pipe in any command and it will notify you when finished
for example:
```
$ sleep 5 | tellme
```

## Issues:
- may need to include a __init__.py in tellme/ but it doesnt play nicely with pyinstaller
- ZSH not implemented yet
- Bash not implemented yet


