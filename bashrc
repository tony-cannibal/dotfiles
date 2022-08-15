# .bashrc

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

EDITOR="nvim"

export PATH="$PATH:/home/luis/.bin:~/.local/bin/:~/.cargo/bin/"

alias ls='exa -l'
alias ll='exa -la' 
alias loadx='xrdb ~/.Xresources'
alias at='alacritty-themes'
alias gset='sudo lightdm-gtk-greeter-settings'
alias sdir='cd ~/.config/suckless'
alias at='alacritty-themes'
alias lf='lfwrapper.sh'

PS1='[\u@\h \W]\$ '

eval "$(oh-my-posh init bash)"

ufetch
