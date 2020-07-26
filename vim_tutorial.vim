runtime vimrc

set scrolloff=0
set path+=**

if has('mouse')
  if exists("*MouseOnOff")
    silent call MouseOnOff()
  else
    set mouse="a"
  endif
  nnoremap <2-LeftMouse> <C-]>:ZT<CR>
endif

let g:peekaboo_delay=10000

let s:slide_lines = 23

function SlideGetpage()
  " Get cursor's page number.
  return (line(".")-1)/s:slide_lines
endfunction

function SlideReposition(p)
  " Move cursor to the first line of page 'p' and set screen to the top.
  let l:goto = ( a:p >= 0 ) ? a:p*s:slide_lines + 1 : 0
  execute l:goto
  normal zt
endfunction

function SlideGoto(N)
  if a:N == ""          " SlideGoto():    Next page
    let l:page = SlideGetpage() + 1
  elseif a:N == "-1"    " SlideGoto(-1):  Previous page
    let l:page = SlideGetpage() - 1
  else                  " SlideGoto(N):   N'th page
    let l:page = a:N - 1
  endif

  call SlideReposition(l:page)
endfunction

if has("user_commands")
  command! -nargs=? GO call SlideGoto(<q-args>)
  command! BACK call SlideGoto(-1)
  command! ZT call SlideReposition(SlideGetpage())
endif

nnoremap <C-]> <C-]>:ZT<CR>

autocmd VimEnter vim_tutorial.txt set rnu
autocmd VimEnter vim_tutorial.txt normal gg
