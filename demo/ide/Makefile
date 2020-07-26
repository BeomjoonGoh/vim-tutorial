
all:	quickfix

quickfix.o: quickfix.cpp
	gcc-7 -std=c++11 -Wall -c $< -o $@
quickfix: quickfix.o
	gcc-7 -lstdc++ -lm -o $@ $^

clean:
	$(RM) -f quickfix quickfix.o
