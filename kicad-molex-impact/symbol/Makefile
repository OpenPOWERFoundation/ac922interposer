all: molex.lib

molex.csv: molex.py
	./molex.py > molex.csv

molex.lib: molex.csv
	kipart --overwrite molex.csv

clean:
	rm -f molex.csv molex.lib
