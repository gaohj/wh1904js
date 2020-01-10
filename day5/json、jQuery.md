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

```

```

