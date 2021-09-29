#!/bin/sh
#!/usr/bin/python3

# kills the script if any of these commands fail
set -e

if ! [ -x "$(command -v pyinstaller)" ];
then
    echo "error: pyinstaller not detected!"
    echo "Ensure you have installed all of the python requirements found in requirements.txt"
    echo "if not run: pip install -r requirements.txt"
    read -p "Shall I run it for your? [y/N]" yn

    case $yn in
        [Yy]* ) pip install -r requirements.txt; break;;
        [Nn]* ) exit 1;;
        * ) exit 1;;
    esac
fi

if [ ! -e .env ]
then
    read -p "We have not detected a .env file, would you like a blank one to be generated? [y/N]" yn
    case $yn in
        [Yy]* ) 
            echo "API_KEY=\nUSER_ID=\nTELLME_ROOT=$PWD\n" > .env
            echo "Generation complete."; 
            echo "-------------"
            echo "In the .env API_KEY needs to be filled out with the key for YOUR bot (you have to make your own one)"
            echo "Thankfully its super easy, search for @BotFather contact on Telegram."
            echo "Send the command /newbot to @BotFather"
            echo "Fill out relevant information, after which you will get a key which you need to include here"
            read -p "Press enter for next instruction." yn

            echo "-------------"
            echo "Next you need to add your Telegram ID to USER_ID in the .env"
            echo "The method for finding this changes all the time."
            echo "You will unfortunately have to google this yourself, it isnt hard, I believe in you :D"
            read -p "Press enter for next instruction." yn

            read -p "Press enter to coninue to installation." yn

            break;;
        [Nn]* ) echo "Remeber to put one in the root directory of this program"; 
            break;;
    esac
else
    echo "found .env"
fi

pyinstaller -F tellme/tellme.py 

if [ ! -e /usr/local/bin/tellme ]
then
    echo "-----------"
    echo "Would you like me to link dist/tellme into /usr/local/bin"
    read -p "(running sudo ln -s $PWD/dist/tellme /usr/local/bin/) [y/N]" yn

    case $yn in
        [Yy]* ) sudo ln -s $PWD/dist/tellme /usr/local/bin/; break;;
        [Nn]* ) exit;;
        * ) exit;;
    esac
else
    echo "Found binary in bin"
fi
