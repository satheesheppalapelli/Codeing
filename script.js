/*
console.log('Hello World! ' +
            'This is Satheesh');*/

// Lecture Variable
/*var name='Satheesh';
console.log(name);

var lastName='Eppalapelli';
console.log(lastName);

var age=23;
console.log(age);

var job='Student';
console.log(job);

var isMarried=false;
console.log(isMarried);

console.log(name+age);

console.log(age + age);

console.log(name + ' ' + lastName + ' ' + age + ' ' + job + ' ' + isMarried);

console.log(name + ' ' + lastName + ' is ' + age + ' years old. Is Profession is ' + job + '. Is he Married = ' + isMarried +'.');

var lastaname=prompt('What is your last name');

console.log(lastaname);
alert(name + ' ' + lastName + ' is ' + age + ' years old. Is Profession is ' + job + '. Is he Married = ' + isMarried +'.');*/

// Lecture Operators

/*var  ageJohn=30;
var  ageMark=30;
console.log(ageJohn);
console.log(ageMark);

ageJohn=ageMark=(3+5)*4-6;
ageJohn ++;  // increment
ageMark *=2; // multiply

console.log(ageJohn);
console.log(ageMark);*/

// Lecture : if/else statement

/*var name='Satheesh';
var age=26;
var isMarried='No';

if(isMarried == 'Yes'){
    console.log(name + 'is Married!');
   } else{
       console.log(name + ' will hopefully marry soon:');
   } 


isMarried=true;

if(isMarried){
   console.log('Yes!');
   }else {
    console.log('No!');
   }if(age===age){
    console.log('Something to Print:');
   }*/


// Lecture : Boolean/Switch Case

// &&= both are true result is true
// ||= any one is true result is true

/*var age=35;

if( age<20 ){
    console.log('Satheesh is a Teenager.');
   } else if ( age > 20 && age<30 ) {
       console.log('Satheesh is a Young man.');
   } else {
       console.log('Satheesh is Man.');
   }


//var job='Student';
var job=prompt('What is the Satheesh Profession.');

switch(job) {
    case 'Student':
            console.log('Satheesh is a Student.');
    break;
    case 'Teacher':
            console.log('Satheesh is a Teacher.');
    break;
    case 'Software':
            console.log('Satheesh is a Software Engineer.');
    break;
    default :
            console.log('Satheesh is a ' + job +'.');
    }*/


// Coding Challenge 1
/*

var heightSatheesh=171.2;
var ageSatheesh=23;
var heightPspk=174;
var agepspk=35;

var scoreSatheesh=heightSatheesh + 5 * ageSatheesh;
var scorePspk= heightPspk + 5 * agepspk;
*/

/*
if(scoreSatheesh > scorePspk){
   console.log('Satheesh Wins the game with '+ scorePspk +' Points!');
   }else if(scorePspk > scoreSatheesh){
       console.log('Pspk wins the game with '+ scoreSatheesh +' Points!');
   }else{
       console.log('Both Score are Equal and it is a draw match.');
   }
*/
/*

var heightMahesh=180;
var ageMahesh=28;

var scoreMahesh= heightMahesh + 5 * ageMahesh;

if( scoreSatheesh > scorePspk && scoreSatheesh > scoreMahesh){
    console.log('Satheesh Wins the game with '+ scorePspk + scoreMahesh +' Points!');
    }else if(scorePspk > scoreSatheesh && scorePspk > scoreMahesh){
    console.log('Pspk Wins the game with '+ scoreSatheesh + scoreMahesh +' Points!');
    }else if( scoreMahesh > scoreSatheesh && scoreMahesh > scorePspk){
    console.log('Mahesh Wins the game with '+scoreSatheesh + scorePspk +' Points!');
    }else{
        console.log('The game is drawn.');
    }
*/


// Lecture: Functions
/*

function calculateAge(yearOfBirth){
    var age = 2018 - yearOfBirth;
    return age;
}
var ageJohn = calculateAge(1990);
var ageSathi = calculateAge(1994):
var ageMike = calculateAge(1996);
var ageMary = calculateAge(1948);
console.log(ageJohn);
console.log(ageSathi);
console.log(ageMike);
console.log(ageMary);

function yearsUntilRetirement(name,year){
    var age=calculateAge(year);
    var retirement = 65 - age;
    if (retirement >= 0){
        console.log(name + ' retires in '+ retirement +' years.');
    }else{
        console.log(name + 'is already retired.');
    }
}
    yearsUntilRetirement('John',1990);
    yearsUntilRetirement('Mike',1966);
    yearsUntilRetirement('Mary',1948);
*/

// Lecture: Arrays
/*

var names = ['John','Mark','Peter'];
var years = new Array(1990,1966,1948);
console.log(names);
console.log(years);
 
names[2] = 'Stark'; // mutateing names and variables. In Peter place we are inserting Stark
years[0] = 1994;
console.log(names);
console.log(years);
console.log(names[0]); // displays index values
console.log(years[1]);

var domnic = ['Torrento', 'Smith',1990, 'Student', false];
domnic.push('blue'); // push is method,add element at ending of the array
domnic.unshift('Mr.Satheesh'); // unshift is method,add element at begining of the array
domnic.pop(); // pop is method, remove last element of the array
domnic.shift(); // shift is method, remove begin element of the array
console.log(domnic);
alert(domnic.indexOf('Smith'));
 if (domnic.indexOf('Student') === -1){
     console.log('Domnic is not a Teacher ');
 } else{
     console.log('Domnic is a Student' );
 }

*/

// Lecture: Object and P roperties

/*var John ={
    name:'John',
    lastName:'Smith',
    yearOfBirth:1990,
    job:'Teacher',
    isMarried:false
}
 
console.log(John);
console.log(John.lastName);
console.log(John['name']);

var xyz='Job';
console.log(John[xyz]);

John.lastName = 'Miller';   // data mutation
John['job'] = 'Programmer';
console.log(John);

var john = new Object();
john.name = 'Peter';
john['lastName' ]= 'Mark';
john['yearOfBirth' ]= 1990 ;
john['job']= 'Student';
john['isMarried'] = false ;

console.log(john);*/


// Lecture : Object and Methods

// v2.0
/*
var John ={
    name:'John',
    lastName:'Smith',
    yearOfBirth:1990,
    job:'Teacher',  
    isMarried:false,
    family: ['Ben','Rosy','Mary'], // adding arrays to the object method
    calculateAge : function (){
        return 2016 - this.yearOfBirth;
    }
}
console.log(John.calculateAge());
var age= John.calculateAge();
John.age= age;
console.log(John);
console.log(age);
*/





//v2.0
var John = {
    name:'John',
    lastName:'Smith',
    yearOfBirth:1948,
    job:'Teacher',  
    isMarried:false,
    family: ['Ben','Rosy','Mary'], // adding arrays to the object method
    calculateAge : function(){
        this.age= 2016 - this.yearOfBirth;
    }
    
};

John.calculateAge();
console.log(John);


var Mike = {
    yearOfBirth : 1993,
    calculateAge : function (){
    this.age = 2016 - this.yearOfBirth;
}
};
 
Mike.calculateAge();
console.log(Mike);

