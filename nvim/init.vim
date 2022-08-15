let g:polyglot_disabled = ['autoindent']

syntax on
set number
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set mouse=a
set clipboard+=unnamedplus
set splitbelow splitright
set noswapfile
set nohlsearch
set hidden 
set nobackup
set nowrap
set signcolumn=yes
set termguicolors
set cmdheight=2
set scrolloff=8
set history=1000
set cmdheight=2
set cursorline
set incsearch
set colorcolumn=80
set undodir=~/.vim/undodir
set undofile
set nocompatible


" Source my Plugins
lua require("user.plugins")

colorscheme gruvbox
highlight Normal guibg=none

let g:airline#extensions#tabline#enabled = 1


" Import The Lua Configs
lua require("user.impatient")
lua require("user.lsp")
lua require("user.cmp")
" lua require("user.treesitter")
lua require("user.telescope")
lua require("user.nvim-tree")
lua require("user.keymaps")
lua require("user.autocommands")
lua require("user.alpha")
lua require("user.colorizer-nvim")

