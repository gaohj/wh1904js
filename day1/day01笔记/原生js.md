# 原生js  

> javascript 跟java一点关系都没有 
>
> 就是脚本语言 跟我们学习的shell 、python 、php 一样 不需要编译  
>
> 弱类型的语言  

* 基本语法  
* 数据类型 
* 运算符 
* 流程控制  
* 函数  
* 对象和数组  
* 内置对象 
* DOM操作 
* BOM操作    
* Ajax 异步     
* jquery  
* vue.js    



## 基本语法   

1.严格区分大小写   变量  方法名  操作符都是区分大小写的   比如 text Text 就是不同的变量  

2.标识符命名规则   变量的名字、方法的名字  方法的属性 函数的参数都称之为标识符  

*  第一个字符必须是字母  及 下划线  或者 $       **不能是数字 ** 
*    其它字符可以是 字母数字 及下划线  或者$ 
*  不能把关键字、保留字 true false null等作为标识符  也就是说 给变量起名字的时候  避开if else true等关键词    

   ###　关键字　　

![关键字](C:\Users\neyo\Desktop\wh1904\day1\day01笔记\关键字.png)

### 保留字  

![保留字](C:\Users\neyo\Desktop\wh1904\day1\day01笔记\保留字.png)



3. 注释 

   ```javascript
   //   单行注释  
   
   /*多行注释  
   */
   ```

   

4. 如何在页面上进行使用    

   `css`:  

     * 行内  

       ```
       <p style='color:red'>python1904 2020年鼠你奥利给</p>
       ```

   * 内联 

     ```css
     <style>
           #container{
               width: 50px;
               height: 50px;
               background: pink;
           }
       
       </style>
     
       <div id="container">
     
       </div>
     ```

     

   * 外链  

     ```html
     <link rel="stylesheet" href="style.css">
     ```

   `js`:

   * 行内  

     ```
      <a href="javascript:方法名()">点我试试</a>
     ```

   * 内联  

     ```js
     <script type="text/javascipt">
             function test(){
                 alert('2020奥利给!')
             }   
     </script>
     ```

   * 外链   

        ```html
        
        ```
   <script src="index.js"></script>  如果是外链 标签中间不要写内容  
        ```



## 打印平台 

> 浏览器 -> 右键 ->检查->console  (控制台) 直接可以在这里写 js代码  经常用来做测试用     
>
> console.log(‘在控制台打印 只有程序员才知道 普通用户察觉不到打印’)

## 变量

> 声明新变量 需要加上var    不加var 不会报错 但是 是有区别的  
>
> 不加var 就会变成全局变量 一直待在内存里边   

```js
var a;  //声明一个空变量 没有赋值  并且以分号结尾  遇到;就知道这一行结束了 
ps: 不加;不报错 但是 我们建议大家加上  
alert(a);  //undefined  表示未定义  

var name='zhangsan'
var password='123456'
console.log(name+':'+password); //建议加上;要不然 意想不到的错误  


var a=1,b=2,c=3,d=4;  //同时声明多个变量 
alert(a+b+c+d);

```



## 数据类型  

* string  
* number
* boolean 
* undefined 
* null
* function   
* object 

### typeof  

```
typeof 变量名   //查看变量的数据类型 
```



### number 

* 二进制   不能超过2   0~1    ob开头二进制  
* 八进制   不能超过8   0~7    0开头 
* 十进制   不能超过10     0~9   普通的数字就是 十进制
* 十六进制    不能超过16 0~9 A~F  A 代表10 B 11 C 12 D 13 E 14 F 15    以0x开头的数字 

```
var b=100
var c=100.123

所属用户的权限所属组的权限其它用户的权限 
100  4
010  2
001  1

var box = 070; //0乘以8的0次方 + 7乘以8的1次方 = 56 
alert(box);
var test = 078;// 大于等于8 认为你这不是8进制是10进制 索引去掉0 显示78
alert(test)

var $a = 0x1F;//15*16的0次方 + 1乘以16的1次方  = 31 
alert($a);
 
var _b = .8; //0.8 不报错 但是不建议这么写
alert(_b);

js的范围 (-Infinity,Infinity) #负无穷到正无穷  

alert(Number.MAX_VALUE); //最大值  
alert(Number.MIN_VALUE);//最小值
```

#### 非数值转成数值类型  

* Number()

  ```
  alert(typeof Number('123')) //number
  alert(Number(true)) //1 
  alert(typeof Number(true)) //number
  
  alert(Number(null))// 0
  alert(typeof Number(null)) //number
  
  alert(Number(undefined)) //NaN 
  
  alert(Number('070')) //70 
  alert(Number('18.1')) //18.1
  ```

  

* parseInt()   重点  

  ```
  // alert(parseInt('56.78')); //56
          // alert(parseInt('123abc'));//123 
          // alert(parseInt('123abc456'));//123
          // alert(parseInt('dec123abc')); //NaN
          // alert(parseInt(''));//NaN
          // alert(parseInt('0xA')); //10
          // alert(parseInt('070')); //70
          // alert(parseInt('0xFLee')); //15
          // alert(parseInt('AF'));//NaN
          // alert(parseInt('AF',16));//告诉系统 AF是个16进制数字  
          // alert(parseInt('10101010',2)); //10101010是个二进制数字
          alert(parseInt('10101010'));
  // alert(parseInt('10101010',8)) //先将字符串10101010转成 数值 如果有第二个参数 不是十进制  先转成10进制 再输出  
  alert(parseInt('70',8));  //56
  ```

  

* parseFloat()  次重点  

```
 console.log(typeof parseFloat('12.34')) //12.34  number 
        console.log(parseFloat('123lee')) //123
        console.log(parseFloat('0xB')) //0 不认16进制   
        console.log(parseFloat('12.34.56'))//12.34 只认一个小数点  
        console.log(parseFloat('01234.56'))//1234.56
        console.log(parseFloat('12.34e10'))//123400000000
```



 

### undefined 

```
var test;
console.log(test)  //undefined 
```

### null 

> 特殊的对象 一般拿它判断来用   
>
> 或者声明一个空对象       

```
var box=null;
console.log(typeof box);//object

if(box != null){
	console.log('对象已经存在')
}else{
	console.log('对象不存在')
}
```

## 等号  

* =  赋值  
* == 值相等  
* === 值和数据类型都相等   python没有  === 



### undefined 和 null 的关系  

> undefined 是从null 派生出来的      

```js
console.log(undefined == null); //true  undefined 是从null 派生出来的 
console.log(undefined === null); //false  
```



### boolean 

> 经常用在判断用 

```js
python True 
js boolean 都是纯小写   

var test=true;
console.log(typeof test) //boolean  

 var box=''; //空字符串 代表假 
 if(box){        
 	alert('真')
 }else{
 	alert('假')    
 }
```

> 重点  ★ ★ ★ ★ ★

| 数据类型  | 为true的情况                                         | 为false的情况          |
| --------- | ---------------------------------------------------- | ---------------------- |
| string    | 非空字符串  也就是说 只要不是''                      | ''  空字符串           |
| boolean   | true                                                 | false                  |
| number    | 非0数字 整型浮点型 均可    包括无穷大 正无穷和负无穷 | 0 NaN （not a number） |
| object    | 任何对象都是真的                                     | null                   |
| undefined | 没有真的                                             | 全为假                 |
| function  | 都是真                                               |                        |



### NaN  

> NaN == NaN   返回 false 
>
> NaN 跟自己 及所有的 都不相等

```js
 alert(isNaN(6)); //6不是 NaN 所以返回false 
alert(isNaN(12/0*0)); //12/0*0不是个数字 所以返回 true
```



### string  

```
var a='12abc';


toString()  非数值类型转成数值类型  

var b = 100;
console.log(typeof b);//number
console.log(typeof b.toString()); //string

var c = true;
console.log(typeof c);
console.log(c.toString());
console.log(typeof c.toString());

var d = 10;

console.log(d.toString()); //将数值转成字符串  10进制 
console.log(d.toString(2));//1010 将10转成2进制形式的字符串
console.log(d.toString(8));//12 8进制形式的字符串
console.log(d.toString(16)); //a 16进制形式的字符串
        
```

### 

## object  

```
var a = new Object();
alert(typeof a);
```



## 数据类型 分类  

* 基本类型  
  * string 
  * number 
  * bull 
  * undefined  
* 引用类型    
  * null 
  * object 
  * function  





## 运算符

* 一元运算符 
* 算术运算符 
* 关系运算符 
* 逻辑 运算符  
* 位运算符   了解 
* 赋值
* 其它运算符   

### 表达式  

> 解释器 通过计算将它变成一个值  
>
> 最简单的表达式就是   字面量 或者 变量名  

```
6.9 数值字面量  
'tianba' 字符串字面量 
true 布尔字面量 
null 空值字面量 
/python/ 正则表达式字面量 

test + '接收69么'; 表达式 
testt > 10 ;表达式 
```





### 一元 运算符  

* a++ 相当于  a = a+1 或者 a+=1 
* ++a 相当于  a = a+1 或者 a+=1 
* a--  相当于  a = a-1 或者 a-=1 
* --a 相当于  a = a-1 或者 a-=1 

### 前置和后置的区别  

* 如果没有赋值操作  那么前置后置结果是一样的   var a = 10  ++a； a++;  的结果对于a来讲 都是一样的  
* 如果有赋值 那么就是  前置   ++a； 先运算 后赋值  
* 后置 a++ 就是先赋值  后运算  

```js
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


```



### 算术运算符  

```js
var age = '您的年龄是:'+20+30;
alert(age);//您的年龄是2030
var ag1= 20+30+'是你的年龄';
alert(ag1);//50是你的年龄

var age2 = '您的年龄是:'+(20+30);
alert(age2);//您的年龄是50

alert(Infinity-Infinity); //NaN 
alert(-Infinity-Infinity);//-Infinity
alert(Infinity+Infinity);//Infinity


alert(100*'kangbazi'); //NaN
alert('123'*100); //12300

alert(100/null); //Infinity 先把null转成 0 

alert(100%'kangbazi') //NaN
```



## 关系运算符 

> 大于> 小于 < 等于 =  >= <=  != ==   

### 特殊值的对比 

| 值                | 结果  |
| ----------------- | ----- |
| null == undefined | true  |
| 'NaN' == NaN      | false |
| NaN == NaN        | false |
| false == 0        | true  |
| true == 1         | true  |
| undefined == 0    | false |
| null == 0         | false |
| '100' == 100      | true  |
| '100' === 100     | false |



## 逻辑运算符  

* AND  逻辑与  &&
* OR   逻辑或   ||
* NOT  逻辑非  ! 

### 逻辑与   两个都为真才是真  

| 第一个表达式 | 第二个表达式 | 结果  |
| ------------ | ------------ | ----- |
| true         | false        | false |
| true         | true         | true  |
| flase        | true         | false |
| false        | false        | false |

```js
3>4  && 5<8
false && true  = false

var test = null;
var person = new Object();

var a = test && (5>4); //如果有一个是null 那么返回null
alert(a)

var b = person && (10>9);
alert(b); //第一个是对象  那么返回第二个 结果  
var c = (10>9) && person; //第二个是对象 那么返回 object 
alert(c); 

var d; 

var e = d && (10>1);  //有一个是undefined 那么立马返回undefined
alert(e);

var d = '';
alert('abc' && d ); //有一个是空字符串 那么返回 空 
```



### 逻辑或  有一个为真 就为真  两个都是false 结果才是false

| 第一个表达式 | 第二个表达式 | 结果  |
| ------------ | ------------ | ----- |
| true         | false        | true  |
| true         | true         | true  |
| flase        | true         | true  |
| false        | false        | false |

```
第一个表达式 是一个对象  那么返回  对象  
第一个表达式的求值结果是false  那么 返回第二个操作数  
两个表达式都是对象 那么返回第一个 
两个都是null  返回null
两个都是NaN 返回NaN 
两个都是undefined  那么返回undefined 

```

### 逻辑非   ！ 

```js
var test = !(5>4);console.log(test);//false
var test = !{};  console.log(test);//false
var test = !'';console.log(test);//true
var test = !0 ;console.log(test); //true
var test = !null ;console.log(test); //true
var test = !NaN ;console.log(test); //true
var test = !undefined ;console.log(test); //true
var test = !'adfadsf' ;console.log(test); //false
```





### 位运算  

```
101010
110011
-------  位于两个都为1 得1     位与 
101010

101101
111011   位或
------
111111   

var test = 25 << 3;  //200 
‭00011001‬ 25
11001000 200 
```



## 运算符优先级 

![运算符优先级](C:\Users\neyo\Desktop\wh1904\day1\day01笔记\运算符优先级.png)