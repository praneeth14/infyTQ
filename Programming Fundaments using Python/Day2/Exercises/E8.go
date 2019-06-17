//PF-Exer-8
//This verification is based on string match.

package main
import ("fmt")
func main(){
    var finalFee int
    //Write your program logic here
    //Populate the variable: finalFee
    var course_fee int=25000
    var marks int=70
    var extra_fee int=1500
    var course_fee_after int = course_fee - ((marks/2)*course_fee)/100
    finalFee = course_fee_after + extra_fee 

     //Do not modify the below print statement for verification to work
     fmt.Println(finalFee) 
}