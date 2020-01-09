## js基础4 

* bom 
* ajax  
* jquery

## bom  

> browser object model   浏览器对象模型  提供了一些属性和方法 来访问浏览器的一些功能

* window对象
* location对象  
* history对象  



### window对象  

| 方法                               | 说明                 |
| ---------------------------------- | -------------------- |
| alert()                            | 弹框                 |
| blur()                             | 焦点移除             |
| close()                            | 关闭窗口             |
| prompt()  偶尔会用                 | 输入框               |
| confirm()    重要                  | 确认                 |
| print()                            | 调用打印机打印       |
| setInterval() clearInterval() 重要 | 每隔多长时间执行一次 |
| setTimeout() clearTimeout() 重要   | 多长时间以后执行一次 |

```js
<body>
    <script>
        // var xingming = prompt("你叫什么名字",'测试游戏');
        // var his =  prompt("当你进入一个森林,希望看到的第一个动物是什么？",'测试游戏');
        // var her =  prompt("当你进入一个森林,希望看到的下一个动物是什么？",'测试游戏');
        // var house = prompt("当你进入一个森林,希望看到的下一个动物是什么？",'测试游戏');
        // var desk = prompt("当你进入屋子看到一个桌子,你觉得是方的还是圆的",'测试游戏');

        // document.write("你的名字叫:"+xingming+"<br />");
        // document.write("你的前世叫:"+his+"<br />");
        // document.write("你另一半的名字叫:"+her+"<br />");
        // document.write("通常情况下你的做事风格是:"+house+"做人风格是:"+desk);
        // if(window.confirm('请确定或者取消')){
        //     alert('好的服务一会就来');
        // }else{
        //     alert('您取消了服务');
        // }

        // window.print()
        // open('http://www.baidu.com');
        // open('http://www.baidu.com','_parent');//在当前窗口打开

        function back(){
            history.back();
        }

        function forward(){
            history.forward();
        }

        function go(num){
            history.go(num);
        }
        window.onload = function(){
            alert(history.length);
        }

    </script>
    <a href="douban.html" target="_self">千锋教育</a>     
    <a href="javascript:back()">后退</a>        
    <a href="javascript:forward()">前进</a>   #重要程度 一般 
    <a href="javascript:go(2)">前进到2</a>

</body>
```



### 超时调用

```js
 // setTimeout("alert('众生皆苦,唯有你是草莓味')",5000);
        //1000 毫秒为单位  1000毫秒等于1秒

        function box(){
            alert("你知道么,男人怕老婆是爱老婆的表现,我现在好怕你");
        }

        // setTimeout(box,3000); 
        // setTimeout("box()",3000);  

        var test = setTimeout("box()",5000);
        clearTimeout(test);
```



### 间歇调用

```
    function love(){
            alert("告诉你个坏消息,我对你的思想已经不单纯了");
        }

        setInterval(love,2000);
        var test = setInterval(love,2000);
        clearInterval(test);
        
     var str = setInterval(function(){
            console.log('美女祖传医术,免费体检');
        },2000);
        clearInterval(str);
```



## ajax  json  

> 异步 局部刷新技术   

```
生活中的同步: 
	国家GDP增长   人民生活水平提高   多件事情一起做   
	
生活中的异步:
	事情一件一件去处理   


技术上的同步正好跟生活中的 相反  

生活中的 同步       =     技术上的  异步    多件事情一起做   米饭在锅里蒸着 同时炒菜
														微博发送过程中同时可以浏览其它的微博
														比如注册用户的时候 
														写完手机号 自动到服务器去验证是否存在 
														同时你可以写其他的表单而不用等验证结果
											股票网站你继续浏览其他内容 不用刷新网页 自动更新数据
														
生活中的 异步  	  =     技术上的  同步    事情一件一件去做    
```



### 实现ajax 四步骤  

```js
1.先要有个手机 							1.创建ajax对象 
						
2.拨通对方的号码  							2.连接服务器 

3.说话 在么								   3.发送请求 

4.等待对方的回复 							4.等待服务器的返回结果
```

