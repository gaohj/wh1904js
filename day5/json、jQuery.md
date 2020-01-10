# json、jQuery

## json

> json和xml都是结构化的数据表示方式    xml可以自定义标签  也要闭合 但是 占空间过大   
>
> json 并不是js独有的 python js php java .net都提供了 对json的解析 以及序列化操作  
>
> 非常轻量     
>
> 前后端分析  数据表示方式 就是用 json 

```javascript
var box = {
				'user':'test',
				
} //这是对象写法  


{"user":"test"}  //只要是字符  那么键和值都是双引号 


//xml 

<person>
    <username>xiaowen</username>
	<age>18</age>
	<edu>圣斗士</edu>
</person>
```



### 原生js类型 转json 类型  

> JSON.stringify(变量)

```
			var persons = [{'username':'xiaowen','age':18,'height':'181cm'},{'username':'yangyang','age':20,'height':'191cm'}];
			//js数组 
			var test = JSON.stringify(persons);
			document.write(test);
			
结果:			[{"username":"xiaowen","age":18,"height":"181cm"},{"username":"yangyang","age":20,"height":"191cm"}]  //上面的单引号全部变成了双引号
```

### json 转原生   

> JSON.parse(str);

```
window.onload = function(){
				ajax('aa.txt/?new='+new Date().getTime(),function(str){
					var text = JSON.parse(str);
					
					
					var test = '';
					test += '<tr>';
					test += '<td>'+text.city+'</td>'
					test += '<td>'+text.weather[0].weather+'</td>'
					test += '<td>'+text.weather[0].wind+'</td>'
					test += '</tr>';

					document.getElementById('citysearch').innerHTML = test;
					
					
					
				})
			}
			
			
```

aa.txt 

```js
{
	"city": "武汉",
	"pm25": "44",
	"weather": [{
		"date": "周五 01月10日",
		"icon1": "day\/yujiaxue",
		"icon2": "night\/xiaoyu",
		"weather": "雨夹雪转小雨",
		"wind": "无持续风向3-4级",
		"temp": "3 ~ 0℃"
	}],
	"date": "2020-01-10",
	"id": "101200101",
	"t": 1578585600
}
```





## jQuery 

> js不是面向对象语言  但是 可以用面向对象的思想去开发   
>
> jQuery 就是js面向对象思想的产物  也就是 封装的一个框架  为了节约开发时间  
>
> 使用方法跟bootstrap是一样的   先要引入一个封装好的文件   
>
> https://jquery.com/download/ 官网  
>
> http://jquery.cuishifeng.cn/ 中文文档   

* 开发版本   有注释 有换行 没有压缩
* 生产版本   无注释 无换行 压缩   

```
1 实例化一个jQuery对象   jQuery   
2 jQuery = $ 
3.window.onload = function(){} 等同于下面$(function(){});
```



### 基本选择器  

```js
$(function(){
				$("#btn1").click(function(){
					$("#one").css('background','pink');
				});
				$("#btn2").click(function(){
					$('.two').css('background','green');
				});
				$("#btn3").click(function(){
					$('div').css('background','orange');
				});
				$("#btn4").click(function(){
					$('span>.three').css('background','blueviolet');
				});
				$("#btn5").click(function(){
					$('*').css('background','yellow');
				});
				
				$("#btn6").click(function(){
					$('span,.two').css('background','darkgoldenrod');
				});
    
    	<input type="button" value="选中id为one的元素" id="btn1"/>
		<input type="button" value="选中class为two的元素" id="btn2"/>
		<input type="button" value="选中所有标签为DIV元素" id="btn3"/>
		<input type="button" value="选中span元素中class为three元素" id="btn4"/>
		<input type="button" value="选中所有元素" id="btn5"/>
		<input type="button" value="选中span元素及class为two的元素" id="btn6"/>
```

### 层次选择器

```js
$(function(){
				$("#btn1").click(function(){
					//类似于css中的 层级选择器 "body内部所有的div元素
					$("body div").css('background','deeppink')
				});
				
				$("#btn2").click(function(){
					//类似于css中的子类选择器   
					$('body > div').css('background','green')
				});
				
				$("#btn3").click(function(){
					$('.one + div').css('background','greenyellow');
				});
				
				$("#btn4").click(function(){
					$('.two ~ div ').css('background','orange');
				});
			});
			
			
			<input type="button" value="body内部所有的div元素" id="btn1"/>
		<input type="button" value="body内部子元素是div的" id="btn2"/>
		<input type="button" value="class为one的下一个div元素" id="btn3"/>
		<input type="button" value="class为two的所有div的兄弟元素" id="btn4"/>
```



### 基本内容过滤器 

```js
$(function(){
				$("#btn1").click(function(){
					$("div:first").css('background','#FF6600')
				});
				$("#btn2").click(function(){
					$("div:last").css('background','red');
				});
				$("#btn3").click(function(){
					$('div:not(.one)').css('background','pink')
				});
				$("#btn4").click(function(){
					$('div:even').css('background','blue');
				});
				$("#btn5").click(function(){
					$('div:odd').css('background','chartreuse');
				});
				$("#btn6").click(function(){
					$('div:gt(2)').css('background','rosybrown');
				});
				$("#btn7").click(function(){
					$('div:eq(2)').css('background','coral');
				});
				$("#btn8").click(function(){
					$('div:lt(2)').css('background','darkred');
				});
			});
		
		<input type="button" value="选择第一个div元素" id="btn1"/>
		<input type="button" value="选择最后一个div元素" id="btn2"/>
		<input type="button" value="class不为one的所有的div元素" id="btn3"/>
		<input type="button" value="索引值为偶数的" id="btn4"/>
		<input type="button" value="索引值为奇数的" id="btn5"/>
		<input type="button" value="索引值大于2的" id="btn6"/>
		<input type="button" value="索引值等于2的" id="btn7"/>
		<input type="button" value="索引值小于2的" id="btn8"/>
```



### 可见性选择器 

```js
		$(function(){
				$('#btn1').click(function(){
					$('div:visible').hide(3000).css('background','#FF6600')
				})
				
				
				$('#btn2').click(function(){
					$('div:hidden').show(3000).css('background','goldenrod')
				})
			});
		<input type="button" value="所有可见的div" id="btn1" />
		<input type="button" value="所有不可见的div" id="btn2" />
```



### 属性选择器 

```js
$(function(){
				$("#btn1").click(function(){
					$('div[title]').css('background','green');
				})
				$("#btn2").click(function(){
					$('div[title="test"]').css('background','red');
				})
				$("#btn3").click(function(){
					$('div[title!="test"]').css('background','yellow');
				})
				$("#btn4").click(function(){
					$('div[title^="te"]').css('background','pink');
				})
				$("#btn5").click(function(){
					$('div[title$="est"]').css('background','darkorchid');
				})
				$("#btn6").click(function(){
					$('div[title*="es"]').css('background','fuchsia');
				})
				$("#btn7").click(function(){
					$('div[id][title*="es"]').css('background','deepskyblue')
				})
			});
		<input type="button" value="选取含有 属性title 的div元素." id="btn1"/>
  <input type="button" value="选取 属性title值等于“test”的div元素." id="btn2"/>
  <input type="button" value="选取 属性title值不等于“test”的div元素(没有属性title的也将被选中)." id="btn3"/>
  <input type="button" value="选取 属性title值 以“te”开始 的div元素." id="btn4"/>
  <input type="button" value="选取 属性title值 以“est”结束 的div元素." id="btn5"/>
  <input type="button" value="选取 属性title值 含有“es”的div元素." id="btn6"/>
  <input type="button" value="组合属性选择器,首先选取有属性id的div元素，然后在结果中 选取属性title值 含有“es”的元素." id="btn7"/>

```

### 子元素 过滤选择器 

```js
$(function(){
				$("#btn1").click(function(){
					$('div.one :nth-child(2)').css('background','green')
				})
				$("#btn2").click(function(){
					$('div.one :first-child').css('background','red');
				})
				$("#btn3").click(function(){
					$('div.one :last-child').css('background','yellow');
				})
				$("#btn4").click(function(){
					$('div.one :only-child').css('background','pink');
				})
				
			});
	<input type="button" value="选取每个class为one的div父元素下的第2个子元素." id="btn1"/>
  <input type="button" value="选取每个class为one的div父元素下的第一个子元素." id="btn2"/>
  <input type="button" value="选取每个class为one的div父元素下的最后一个子元素." id="btn3"/>
  <input type="button" value="如果class为one的div父元素下的仅仅只有一个子元素，那么选中这个子元素." id="btn4"/>
```



### 遍历节点树 

```js
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>遍历节点树</title>
		<script src="js/jquery-3.4.1.min.js"></script>
		<script>
			$(function(){
				var body = $('body').children()
				//alert(body.length);//2
				var ulls = $('ul').children();
				//alert(ulls.length);//4
				var p = $('p').children();
				//alert(p.length);//0 文本节点不看作是一个子节点     
				//alert(ulls[1].innerText);//只有文本不含标签   
				alert($('p').next().html());//标签内部html 标签及内容 
				alert($('ul').prev().html());//等同于innerHTML
				
			})
		</script>
	</head>
	<body>
		<p title="男人最喜欢的水果"><a href="">男人最喜欢的水果</a></p>
		<ul>
			<li title="草莓">straw</li>
			<li title="香蕉"><a href="#">banana</a></li>
			<li title="苹果">apple</li>
			<li title="橘">orange</li>
		</ul>
	</body>
</html>

```



### 模糊查询 

```js
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>模糊查询</title>
		<script src="js/jquery-3.4.1.min.js"></script>
		<script>
			$(function(){
				$("#test").keyup(function(){
					var key = $(this).val();
					$('ul > li').hide();
					if(key == ''){
						$('ul > li').show();
					}else{
						$('ul>li:contains('+key+')').show();
					}
				})
			});
		</script>
	</head>
	<body>
		<input type="text" id="test" placeholder="请输入要查找的关键词" width="100" height="20"/>
		<div>
			<ul>
				<li>乒乓球</li>
				<li>排球</li>
				<li>羽毛球</li>
				<li>篮球</li>
			</ul>
		</div>
	</body>
</html>

```



### 手风琴

```

```

