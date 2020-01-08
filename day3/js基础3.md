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

```js
var box = '迪丽热巴';
		console.log(box.length);
        console.log(box.concat('美女叫什么名字','把你写到我家户口本可好','!'));//迪丽热巴美女叫什么名字把你写到我家户口本可好!

        console.log(box.slice(1,3));//丽热
        console.log(box.substring(1,3));//丽热
        console.log(box.substr(0,3));//迪丽热
        console.log(box.substr(1));//丽热巴 从1截取到最后
        console.log(box.substr(-1));//巴 字符串长度+(-1) 截取到最后
```

### 位置方法  

| 方法               | 说明                                                         |
| ------------------ | ------------------------------------------------------------ |
| indexOf（str,r）   | 从下标为r的位置开始搜到第一个str 如果搜到 返回所在的索引位置否则返回-1 |
| lastIndexOf(str,r) | 从下标为r的位置开始搜到最后一个str 如果搜到 返回所在的索引位置否则返回-1 |

```
 var box = 'good good study,day day up';
        // var test = box.indexOf('ziwen');//-1
        //var test = box.lastIndexOf('good');//10
        var test = box.lastIndexOf('good');//5
        console.log(test);
        
```



## 内置对象之数学对象 

```
console.log(Math.PI);//3.141592653589793
        console.log(Math.ceil(12.46788));//13 向上取整
        console.log(Math.round(4.457));//4 四舍五入 取整
        console.log(Math.floor(5.123));//5 向下取整
        console.log(Math.random());//0到1之间的小数 包含0 不包含1 
```

> 万能公式 

```js
值=Math.floor(Math.random()*总数+第一个数)

  //5到90之间的随机数   总数是86 第一个数是5
        console.log(Math.floor(Math.random()*86+5))
    
```



## 双色球   

> 红球  1-33    6个   蓝球  1-16    1个   

```js
var box = document.getElementById('box');
var span = box.getElementsByTagName('span');
var redBall = []; //空数组 用来存放  红球 
for(var i=0;i<6;i++){   //随机产生6个随机数
    var rand = Math.floor(Math.random()*33+1); //每次都是1到33之间的随机数 
    if(redBall.indexOf(rand) == -1){
        redBall.push(rand);
    }else{
        i--;
    }
}
for(var i=0;i<redBall.length;i++){
    //跟下一个球进行比较
    for(var j=i+1;j<redBall.length;j++){
        if(redBall[i]>redBall[j]){
            var temp = redBall[i];
            redBall[i] = redBall[j];
            redBall[j] = temp;
        }
    }

}
var blueball = Math.floor(Math.random()*16+1); //随机生成一个 
//1-16的蓝球
redBall.push(blueball);
for(var i=0;i<span.length;i++){
    span[i].innerHTML = redBall[i];
}
```



## Dom  

```js
var divs = document.getElementsByClassName('names');
        // alert(divs.length);
        // console.log(divs[0].getAttribute('style')); //background: blue;
        // divs[0].setAttribute("style","width:50px;height:100px;background:pink");
        // divs[1].removeAttribute('style');
        // console.log(divs[1].tagName);
        // console.log(divs[0].innerHTML);

        console.log(divs[0].nodeType); //元素节点 1 
        console.log(divs[0].nodeName); //元素节点名称 DIV
        console.log(divs[0].nodeValue);
        console.log(divs[0].getAttribute('class').nodeType);//names undefined 
        console.log(divs[0].attributes[0].nodeType); 
        //attributes 表示所有的属性 第1个属性的nodetype  因为是属性节点
        //所以是2 
        console.log(divs[0].attributes[0].nodeName);//属性名称 从；class
        console.log(divs[0].attributes[0].nodeValue);
        console.log(divs[0].childNodes[0].nodeType);//把标签中间的内容看作 div的子节点 子节点的nodetype 因为是个文本 所以是 3
        console.log(divs[0].childNodes[0].nodeName);//#test
        console.log(divs[0].childNodes[0].nodeValue);

            //         1
            //  DIV
            // null
            // undefined
            //2
            //class
            //names
            // 3
            //#text
            //我是文本


 var divs = document.getElementsByClassName('names');
        console.log(divs[0].firstChild.nodeType);
        console.log(divs[0].firstChild.nodeName);
        console.log(divs[0].childNodes.length);
        console.log(divs[0].parentNode.nodeName);
        console.log(divs[0].ownerDocument.nodeName);
        console.log(divs[0].previousSibling.nodeName);
        console.log(divs[0].nextSibling.nodeName);
```



## 事件   

* 鼠标事件 
* 键盘事件 
* HTML事件  

> 语法  on+事件名称  

```js
html事件
<script>
       window.onload = function(){
            var box = document.getElementById('test')
            alert(box.innerHTML); 
       }
    </script>

    <div id="test">
        test
    </div>



  onselect 选择文本框或者textarea的时候 触发  
  onblur 失去焦点的时候触发 
  onsubmit 提交的时候触发 
  onreset 重置按钮点击的时候触发 
  onscroll 滚动条滚动的时候触发 
  
  
  window.onscroll = function(){
        alert('来啊 快活啊');
    }


键盘事件: 
 onkeydown 按下任意键 触发 按住不放 重复触发  
 onkeypress 按下键盘字符键 触发  按住不放 重复触发 
 onkeyup 松开以后才触发  
 
鼠标事件: 
onclick 点击  
ondblclick 双击 
onmousedown 按下鼠标 还没弹起来的时候触发 

onmouseup 弹起来的时候触发  
onmouseover  鼠标移入的时候触发  
onmouseout  鼠标移出的时候触发  
onmousemove 鼠标在区域上移动  触发 
```



