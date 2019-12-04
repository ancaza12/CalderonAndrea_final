sigma.png : valores.txt 1.py
	python 1.py

solar.png : monthrg.dat 2.py
	python 2.py
	

3.png : 3.dat 3.py
	python 3.py
clean:
	rm -rf sigma.png solar.png
