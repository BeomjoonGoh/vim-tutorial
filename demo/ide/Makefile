quickfix: quickfix.o
	gcc-7 -lstdc++ -lm -o $@ $^
quickfix.o: quickfix.cpp
	gcc-7 -std=c++11 -Wall -c $< -o $@

.PHONY: clean
clean:
	$(RM) -f quickfix quickfix.o
