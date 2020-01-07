## javascript基础2  

* 三元运算符  
* 流程控制 
* 函数
* 对象 和数组  

## 浏览器 分类  

* IE浏览器 
* 非IE浏览器  W3C浏览器 (chrome\firefox\opera)

## 三元运算符    表达式?结果:结果2   

```js
// if(5>4){
    //     alert('对')
    // }else{
    //     alert('错')
    // }
    
   转化成下边的形式就是: 
    var box = 5>4?'对':'错'
    alert(box);
```



## 流程控制语句  

* if
* for 
* while 

* do..while   

### if

> if(表达式){语句;}else if{y语句}else{语句}

```js
var box = 100;
    // if(box>99) alert('box大于99');
    // if(box>99) 
    //     alert('box大于99');
    if(box>=100){
        alert('特别优秀');
    }else if(box>=90){
        alert('优秀');
    }else if(box>=80){
        alert('优');
    }else if(box>=70){
        alert('优良');
    }else if(box>=60){
        alert('及格')
    }else{
        alert('不及格')
    }
```

### switch  

```js
switch(表达式):
	case 值:
		语句 
	default:  如果所有的case 都不符合  那么走 default 
		语句
		
switch(box){
        case 100:
            console.log('优秀');
            break; //表示为了防止穿透到下面造成结果污染
        case 80:
            console.log('还行吧')
            break;
        case 60:
            console.log('及格')
            break;
        default:
}
```

### do .. while语句 

> 先运行一次再判断 

```js
 var box = 6;
    do{
        console.log(box);
        box++;
    }while(box <= 10);  //先运行一次 再判断  
```



### while 

> 先判断 再运行 

```js
var box = 1;
    while(box <= 5){
        console.log(box);
        box++;
    }
```



### for 

```js
 // for(var box=1;box<=5;box++){
    //     console.log(box);

    // }
    // document.write('别追公交车了追我吧')
    document.write('<table>');
    for(var i=9;i>=1;i--){
        document.write('<tr>');
            for(var j=1;j<=i;j++){
                document.write('<th>'+i+"*"+j+'='+(i*j)+'</th>');
            }
        document.write('</tr>');
    }
    document.write('</table>');
```



### for... in  了解  枚举对象的属性  

```
var person = {
        'name':'李白',
        'age':28,
        'height':'178cm',

    }

    for(var p in person){
        console.log(p)
    }
```

### with 

```js
var person = {
        'name':'李白',
        'age':28,
        'height':'178cm',

    }
var n = person.name;
var a = person.age;
var h = person.height;

    console.log(n,a,h);  #每次打印对象的属性 需要加上对象的名字

    with(person){     #这样的话就不需要加上对象的名字了  
        var n =name;
        var a= age;
        var h = height;
    }
    console.log(n,a,h);
```





## 函数   

> function 方法名(){    {作用域}
>
> ​			函数体;
>
> }
>
> if的 {}   和 for的 {} 它们不是作用域

```
function test(x,y){ //形参
            console.log("您输入的第一个参数是:"+x+";"+"第二个参数是:"+y); //实参

        }

 test(5,6);
 
function sums(num1,num2){
            return num1+num2;
}
        
alert(sums(10,20));
```

### arguments对象  

```
  //我不知道你要传多少参数
        function box(){
            // return arguments[0] + arguments[4]; 
            //第一个参数 和第五个参数的和  
            return arguments.length; //参数的个数
        }

        alert(box(11,2,3,4,50,6,7,8,9));
```

## 作用域  

```
function color1(){

            alert(box); //局部可以调用全局  

        } 
        color1(); //pink

        var color = 'pink';
        function color2(){
            var color = 'red'
            alert(color); //局部可以调用自己 

        } 
        color2(); //red

        function color3(){
             var color = 'red'
    
        } 
        alert(color); //提示color 未定义 
        
        局部可以调用全局 可以调用自己内部的  
        全局不可以调用局部变量
        
        
   if(true){
        var color = 'orange';
    }

    alert(color); //返回orange 说明 if 没有作用域

    for(var i=0;i<10;i++){
        var color = 'green';
    }
    alert(color);  //返回green 说明 for 也没有作用域

```



### 类型检测    instanceof  

> 数组、对象、null 、统称为 对象  当我们用typeof 检测的时候  统一返回的是 object  
>
> 但是 我们现在就想判定是否是数组 是否是对象  

```
    var box = ['a','b','c'];     
    alert(box instanceof Array);//true   判断 box 是否是一个数组  返回 Boolean 

    var test = {

    }
    alert(test instanceof Object); //true判断 test 是否是一个对象  返回 Boolean
```



## 对象  

```js
创建对象的第一种方式: 

  var box = new Object();
  box.name = '小文';
  box.age = 18;

  alert(box.name); //小文
  alert(box instanceof Object); //true
创建对象的第二种方式: 

  var person = {
         'name':'kangbazi',
         'age':18,
         'eat':function(num){
             return '恭喜'+num+'大吉大利,今晚吃鸡';
         }
     }

     alert(person.eat('小文')) //调用对象的方法  
```



## 数组  类似于python的列表

```js
 var box = []; //生命一个空数组 
        // alert(box.length); //数组的长度  0  
        var test = [1,2,3,];//不建议这么命名 ie8以上 输入3
        //以下输出4
        var test = [1,2,3,99]; 

        //
        // alert(test.length);
        alert(test[test.length-1]);//数组的最后一个元素
        //最后一个元素的下标位 数组的长度-1 
        //数组的下标从0开始的   
var box = [11,23,45,64];
box[box.length] = 88; //在数组的最后位置插入一个元素
//下标正好是 数组的长度

var python = [200,'hello',false,null,{'name':'xiaowen'}]
alert(python.length);//5

第二种创建数组的方式:
 var box = new Array();
        alert(box.length); //0
        var test = new Array(
            100,
            'abc',
            null,
            {
                'name':'kangbazi'
            },
            true,

        );
        alert(test.length);//4
        
    
```



## 系统函数  操作数组  

* 栈方法  

  * push()
  * pop()

  ```js
  var box = ['苍老师','小泽老师','龙老师','波老师']
          console.log(box.length);
          console.log(box.push('吉泽老师','东京热系列','xx系列')); //返回的是插入元素之后数组的长度  
          console.log(box);
          console.log(box.pop()); //返回的是数组的最后一个元素 吉泽老师  
          console.log(box);
  
  ```

  

* 队列方法   

  * shift()
  * unshift()

  ```
   var language = ['html','c','c++'];
          console.log(language.length);
          console.log(language.unshift('python','go','R','javascript')); //返回的是插入元素之后数组的长度  
          console.log(language);//["python", "go", "R", "javascript", "html", "c", "c++"]
          console.log(language.shift());//弹出数组的第一个元素  
  ```

  

### 排序算法  

* reverse()
* sort() 

```
	    var box = [11,12,3,24,45,36,7];
        //var box = ['a','f','c','g','e'];
        //alert(box.reverse());//7,6,5,4,3,2,1  
        //alert(box.reverse());//e,d,c,b,a
        //因为这个方法 对数字和字母同时生效 
        //但是 只能连续的数字 或者连续的字母结果准确如果不连续 造成结果不准确 
        
         var box = [117,26,235,44,53,62,11]; //sort 和 reverse 对字母也生效  所以结果可能不准确  
         但是我们像排序  可以自己写方法 干预结果  
         
         
         console.log(box.sort());// [11, 117, 235, 26, 44, 53, 62]
        console.log(box.sort(compare));//[11, 26, 44, 53, 62, 117, 235]
        console.log(box.reverse(compare));//[235, 117, 62, 53, 44, 26, 11] 
        
         function compare(num1,num2){
            if(num1<num2){
                return -1; //正序排列   如果想倒序这里就是 1 
            }else{
                return 1;   
            }
        }

```



ps: 以上的操作 原数组结果发生了改变   



### 数组操作方法   将结果放到新的数组里 原数组保持不变  

* concat()

```js
var ximen = ['俯卧撑','单手俯卧撑','两只手指'];
        var test = ximen.concat('不允许用手');
        console.log(ximen);//['俯卧撑','单手俯卧撑','两只手指']
        console.log(test);//['俯卧撑','单手俯卧撑','两只手指','不允许用手']; 对原来的数组没有产生任何影响
```



* slice()

```
var liushui = ['居家生活','潮流电子','时尚衣品','转账红包'];
        var zhifubao = liushui.slice(1,3);
        console.log(liushui);//["居家生活", "潮流电子", "时尚衣品", "转账红包"]
        console.log(zhifubao); //["潮流电子", "时尚衣品"]包含1 不包含3   
        console.log(liushui.slice(1));//包含1 从1截取到最后  
        console.log(liushui.slice(0));//包含0 从0截取到最后  

        //slice(0) 相当于复制了一个数组 
```





### 复制数组  

* slice(0)

* ```
   var person = ['zhangsan','lisi','wangwu','zhaoliu'];
  
          var new_person = [];
  
          for(i=0;i<person.length;i++){
              new_person.push(person[i]);
          }
  
          console.log(new_person);
          console.log(person);
  ```



### 数组的中间插入 及替换删除等功能  splice 

````js
#插入功能
   var office = ['qq','weixin','dingding'];
        var box2 = office.splice(2,0,'yinxiangbiji','youdaoyunbiji');
        console.log(office); //["qq", "weixin", "yinxiangbiji", "youdaoyunbiji", "dingding"]
        //从下标为2的位置截取0个 然后在下标2的位置从插入两个元素 
        console.log(box2);//空 因为上面第二个参数是0 所以这里为空
        
#删除功能  

  var office = ['qq','weixin','dingding'];
        var box2 = office.splice(0,2);//从第0个位置开始 截取2个
        console.log(box2);// ["qq", "weixin"]
        console.log(office);//["dingding"]


#替换功能   

		var office = ['qq','weixin','dingding'];
        var box2 = office.splice(1,2,'momo','tantan');
        console.log(office);//["qq", "momo", "tantan"]
        console.log(box2);//["weixin", "dingding"]
````

