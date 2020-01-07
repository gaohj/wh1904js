var a=10;
var b=++a + a++;
//  a=11  + 11
var c=b-- - --b;
//    22  -  20
console.log(a); //12
console.log(b); //20
console.log(c); //2


// var d=30;
// var e=--d - d--;
// var f = ++e+e++;

// console.log(d,e,f);

// var box='89'
// alert(box++);//89 
// alert(box);//90 

// var test=20;
// alert(+test); //20
// alert(-test); //-20
// var age = '您的年龄是:'+20+30;
// alert(age);//您的年龄是2030
// var ag1= 20+30+'是你的年龄';
// alert(ag1);//50是你的年龄

// var age2 = '您的年龄是:'+(20+30);
// alert(age2);//您的年龄是50

// alert(Infinity-Infinity); //NaN 
// alert(-Infinity-Infinity);//-Infinity
// alert(Infinity+Infinity);//Infinity

// alert(100*'kangbazi'); //NaN
// alert('123'*100); //12300 先把'123'转成123 

// alert(100/null); //Infinity 先把null转成 0 

// alert(100%'kangbazi') //NaN

// alert(null == undefined );
// alert(null ==0 );

// var test = null;
// var person = new Object();

// var a = test && (5>4); //如果有一个是null 那么返回null
// alert(a)

// var b = person && (10>9);
// alert(b); //第一个是对象  那么返回第二个 结果  
// var c = (10>9) && person; //第二个是对象 那么返回 object 
// alert(c); 

// var d; 

// var e = d && (10>1);  //有一个是undefined 那么立马返回undefined
// alert(e);

// var d = '';
// alert('abc' && d ); //有一个是空字符串 那么返回 空 
var test = !(5>4);console.log(test);//false
var test = !{};  console.log(test);//false
var test = !'';console.log(test);//true
var test = !0 ;console.log(test); //true
var test = !null ;console.log(test); //true
var test = !NaN ;console.log(test); //true
var test = !undefined ;console.log(test); //true
var test = !'adfadsf' ;console.log(test); //false