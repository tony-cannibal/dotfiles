#!/bin/bash 


clear


while :
do

    printf "\n\n\n\n\n" 
    echo 'Wich Window Manager'
    echo 'Do you want to use'
    read wm

    case $wm in 
        dwm)
            break
            ;;
        openbox)
            break
            ;;
        qtile)
            break
            ;;
        bspwm)
            break
            ;;
        *)
            echo 'That is not a valid option.'
            ;;
    esac
done

  
startx ~/.xinitrc $wm 
