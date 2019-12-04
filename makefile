sigma.png : valores.txt 1.py
	python 1.py

solar.png : monthrg.dat 1.py
	python 1.py
clean:
	rm -rf sigma.png solar.png
