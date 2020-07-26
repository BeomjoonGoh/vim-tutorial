runtime vimrc

function SlideGoto(page)
  let l:lines = 23
  let l:goto = (line(".")-1)/l:lines*l:lines + 1
  execute l:goto
  if a:page == ""
    execute 'normal' l:lines.'j'
  elseif a:page == "-1"
    execute 'normal' l:lines.'k'
  elseif a:page != "."
    let l:goto = (a:page-1)*l:lines + 1
    execute l:goto
  endif
  normal zt
endfunction

if has("user_commands")
  command! -nargs=? GO call SlideGoto(<q-args>)
  command! BACK call SlideGoto(-1)
  command! ZT call SlideGoto(".")
endif

set scrolloff=0
set path+=**
silent call MouseOnOff()
let g:peekaboo_delay=10000

nnoremap <2-LeftMouse> <C-]>:ZT<CR>
nnoremap <C-]> <C-]>:ZT<CR>

autocmd VimEnter vim_tutorial.txt set rnu
autocmd VimEnter vim_tutorial.txt normal gg
