data e;
	infile "/home/u64535084/diabetes analysis/diabetes_class1.csv" dsd;
	input outcome bmi bp age;
	
	/* 
	Must subtract 25 to represent the value to test in the ttest
	
	H0: mean BMI = 25
	Ha: mean BMI > 25
	*/
	
	bmi_ttest = bmi - 25; 
run;

proc means n mean std t probt;
	var bmi_ttest;
run;

proc means clm;
	var bmi;
run;
