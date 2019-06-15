//PF-Exer-16

num1 = 5;
num2 = 10;

//Write your code here
function gcd(a, b) {
    while (a % b != 0) {
        r = a % b;
        a = b;
        b = r;
    }
    return b
}
if(a >b){
    console.log((a * b) / gcd(a, b));
}
else{
        console.log((a * b) / gcd(b, a));
}
