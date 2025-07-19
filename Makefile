julia:
	/usr/bin/time python src/julia_set.py

perf_julia:
	python -m cProfile -o "julia.prof" src/julia_set.py
	python -m snakeviz julia.prof


