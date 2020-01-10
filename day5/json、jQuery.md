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



