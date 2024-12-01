all: day1 day1_2 run
run: day1.exe day1_2.exe
	day1.exe && day1_2.exe
day1: day1.cpp FillVectors.hpp
	g++ day1.cpp -O3 -o day1.exe
day1_2: day1_2.cpp FillVectors.hpp
	g++ day1_2.cpp -O3 -o day1_2.exe
