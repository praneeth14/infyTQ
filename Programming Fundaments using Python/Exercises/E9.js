//PF-Exer-9

noOfFlightsTakeOff = 100;
noOfFlightsLanded = 110;
seatingCapacityTakeOff = 150;
seatingCapacityLanded = 185;
totalCookies = 0;

//Write your code here
//Populate the variable: totalCookies
totalCookies = (noOfFlightsTakeOff * seatingCapacityTakeOff + noOfFlightsLanded * (seatingCapacityLanded / 2)) * 2;

//Do not modify the below print statement for verification to work

console.log(totalCookies);


