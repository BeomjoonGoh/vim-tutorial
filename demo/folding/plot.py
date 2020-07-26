#!/usr/bin/python3
import sys, re, subprocess, inspect, getpass

class Plot:
    """ plot - simple command-line interface for gnuplot
        Usage: plot [[OPTION] [FILE]]...
        Options   Description      Reference    Example
            -s    set an option    set          -s'logscale x' -s'terminal png'
            -x    x interval       xrange       -x-1:1
            -y    y interval       yrange       -y-1:1 -y0:
            -X    vertical lines   arrow        -X0,10,20
            -f    plot functions   functions    -f'sin(x)' -f'cos(x), exp(x)'
            -u    x,y columns      using        -uall -u1:2,1:4 -u'($1/5):(log($2))'
            -w    styles           with         -wl -wp -wlp
            -nt   remove title     plot title   -nt
            -o    print output                  -o'out.gpi'
            -h    print this help message
        Beomjoon Goh, 11 Jul 2020
    """
    def __init__(self):
        self.head = 'set terminal qt font "Helvetica,12"\n'
        self.cmds = "plot "
        self.prnt = None

    def process(self, argv):
        def opt(arg, opt):
            return arg[:len(opt)+1] == '-'+opt

        def columns(arg):
            with open(arg, 'r') as f:
                for line in f:
                    if line[0] != '#':
                        return len(line.split())

        using = [False, []]
        style = "lines"
        title = ""
        for arg in argv:
            if   opt(arg, 'h'):
                sys.exit(inspect.cleandoc(self.__doc__))
            elif opt(arg, 'o'):
                self.prnt = arg[2:]
            elif opt(arg, 's'):
                self.head += "set " + arg[2:] + '\n'
            elif opt(arg, 'x'):
                self.head += "set xrange [" + arg[2:] + "]\n"
            elif opt(arg, 'y'):
                self.head += "set yrange [" + arg[2:] + "]\n"
            elif opt(arg, 'X'):
                for a in arg[2:].split(','):
                    self.head += "set arrow from %s, graph 0 to %s, graph 1 nohead\n" % (a,a)
            elif opt(arg, 'f'):
                self.cmds += arg[2:] + ", "
            elif opt(arg, 'u'):
                using = [ arg[2:] == "all", arg[2:].split(',') ]
            elif opt(arg, 'w'):
                style = arg[2:]
            elif opt(arg,'nt'):
                title = "notitle"
            else:
                if using[0]:
                    using[1] = [ "1:"+str(n) for n in range(2,columns(arg)+1) ]
                for u in using[1]:
                    self.cmds += ' '.join(['"'+arg+'"', "using", u, title, "with", style]) + ', '
        self.cmds = re.sub(r",\s*$", '\n', self.cmds) # trim last comma and whitespaces

if __name__ == '__main__':
    plot = Plot()
    plot.process(sys.argv[1:])
    outfile = plot.prnt or "/tmp/gnuplot."+getpass.getuser()+".gpi"
    with open(outfile,'w') as f:
        print(plot.head + plot.cmds + "pause -1", file=f)
    if plot.prnt is None:
        subprocess.run(["gnuplot", outfile])
