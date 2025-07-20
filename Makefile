julia:
	/usr/bin/time python src/calculate_julia_set.py

perf_julia:
	python -m cProfile -o "julia.prof" src/calculate_julia_set.py
	python -m snakeviz julia.prof

build:
	python setup.py build_ext -b src

