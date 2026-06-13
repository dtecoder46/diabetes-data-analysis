data e;
	infile "/home/u64535084/data.csv" dsd;
	input id pregnancies glucose bp skin_thickness insulin bmi pedigree_func age outcome;
run;

proc means data = e;
run;
