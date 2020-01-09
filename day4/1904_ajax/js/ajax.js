function ajax(url,funcsuccess,funcfail){
	//1 创建 ajax 对象  
	if(window.XMLHttpRequest){
		//如果为true 说明是w3c浏览器 
		var aJax = new XMLHttpRequest();
	}else{
		var aJax = new ActiveXObject("Microsoft.XMLHTTP");
	}



	//2连接服务器  
	//http://www.baidu.com/?username=jiadong&password=123456 get
	//第一个参数 method get post 请求方式
	//第二个参数  url 服务器的地址  
	//第三个参数  true 表示异步  false  同步 
	aJax.open('GET',url,true);




	//3 发送请求  
	aJax.send()


	//4等待服务器的返回结果
	//接收服务器返回的数据 需要监听 XMLHttpRequest的状态  
	//当状态发生改变  那么会触发一个事件onreadystatechange事件 
	//onreadystatechange有5个状态 分别是 0 1234 
	//0 请求没有初始化  
	//1 连接已经建立 
	//2 服务器接收了你的请求了
	//3.请求处理中 
	//4.请求完成开始响应   
	aJax.onreadystatechange = function(){
		if(aJax.readyState==4){  //请求开始响应 
			if(aJax.status == 200){ //返回成功 
//				alert("成功:"+aJax.responseText);
				//成功以后你要把结果返回给前台
				funcsuccess(aJax.responseText)
			}else{
//				alert("失败");
				if(funcfail){
					funcfail();
				}
			}
		}
	}
}
	