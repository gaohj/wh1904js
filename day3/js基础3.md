## js基础3   

* function类型 
* 函数的内部属性  
* this  
* 全局调用局部  
* 基本包装类型 
* math对象  
* dom基本操作  



## function 类型  

```js
  /*
        *  求和方法 
        *  @params:num1 number 必须 
        *  return number 
        */
        function sums(num1){
            return num1+10;
        }

        /*
         * @params func function
         * @params num  number类型
         */
        function box(func,num){
            return func(num);
        }
    
        console.log(box(sums,10));
    
        //1sums 传给 box  10 传给 num 
        //sums(10)
        //10+10 
    
```



## 函数内部属性  

> arguments.callee 

```
 //5*4*3*2*1=120
        // function pandas(num){
        //     if(num<=1){
        //         return 1;
        //     }else{
        //         return panda(num-1)*num; //这个名字 随着 方法的更改而更改 
        //         //如果方法名改这里必须改 麻烦  
        //     }
        // }
        function kangbazi1(num){
            if(num<1){
                return 1;
            }else{
                return arguments.callee(num-1)*num;
            }
        }


        console.log(kangbazi1(5));//120 
        //5*panda(4)
        //5*4*panda(3)
        //5*4*3*panda(2)
        //5*4*3*2*1
```



## this 

> window 是最大的对象  写的过程中可以省略 
>
> var color = 'orange';
>
> ​    alert(color);  alert(window.color);效果是一样的

```js
var color = 'orange';
alert(color); //orange
alert(window.color);//orange
alert(this.color);//orange


此时 this 代表最大对象 window

  var color = 'red';
  var ball = {
            'color':'orange',
            'useColor':function(){
                alert(this.color); //此时this 在作用域中this代表 orange
            }
        }

  ball.useColor();//orange
  alert(this.color);//red //this在最外边  所以代表 window


  var ball = {
            'color':'orange',
            'useColor':function(){
                alert(this.color); //此时this 在作用域中this代表 orange
            }
        }

  alert(this.color);//undefined //this在最外边  所以代表 window 全局不能调用局部
```



## 扩展作用域 让全局可以调用局部  

> call 

```js
var color = 'yellow';
        var shehuitianqige = {
            'color':'red',
        }

        function useColor(){
            alert(this.color);
        }
    
        // useColor();//yellow
        useColor.call(shehuitianqige);//red  使用call 扩展了shehuitianqige作用域 虽然作用域在局部 但是 扩展
        useColor.call(window);//作用域在全局 yellow
        useColor.call(this);//这里的this 跟window 是一样的  所以它在全局 yellow
```

### var 不加var 就会变成全局变量

```
function sums(m,n){
            sum = m+n;
            return sum;

        }

        alert(sums(10,20));//30
        alert(sum);//30 因为你没有加var 所有sum成了全局变量 任何地方都可以调用
        //解决方法 加上var 即可
```

## 基本包装类型 

* 字符串
* number
* boolean

```js
var test = {
            'username':'kangbazi',
            'eat':function(){
                alert('吃鸡');
            }
        }
        
        alert(test.username);
        test.eat();
        
  #只有对象才可以自定义属性 和方法  
  
  
  box.name = 'haha';
        box.eat = function(){
            alert('kangbazi');
        }
        alert(box.name);
        box.eat();
   #字符串 这样是报错的  
   
   
   #但是系统封装了一些属性和方法  供 字符串调用  所以将其称之为 基本包装类型 
   
   var box = '甲流虽然是流感但是大可不必慌张';
   alert(box.length); //15
   alert(box.substring(2));//截取前两位      虽然是流感但是大可不必慌张
```

### 方法 

| 方法            | 说明                            |
| --------------- | ------------------------------- |
| concat()        | 串联字符串                      |
| slice(n,m)      | 从下标为n截取到m 包含n 不包含 m |
| substring(n,m） | 同上                            |
| substr(n,m)     | 从n开始 截取m个                 |

| 属性   | 说明         |
| ------ | ------------ |
| length | 字符串的长度 |

```
var box = '迪丽热巴';
		console.log(box.length);
        console.log(box.concat('美女叫什么名字','把你写到我家户口本可好','!'));//迪丽热巴美女叫什么名字把你写到我家户口本可好!

        console.log(box.slice(1,3));//丽热
        console.log(box.substring(1,3));//丽热
        console.log(box.substr(0,3));//迪丽热
        console.log(box.substr(1));//丽热巴 从1截取到最后
        console.log(box.substr(-1));//巴 字符串长度+(-1) 截取到最后
```

