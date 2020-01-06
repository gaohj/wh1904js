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

![关键字](C:\Users\neyo\Desktop\day01笔记\关键字.png)

### 保留字  

![保留字](C:\Users\neyo\Desktop\day01笔记\保留字.png)



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



### string  

```
var a='12abc';
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

  

* parseInt()

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
  ```

  

* parseFloat()

 

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

