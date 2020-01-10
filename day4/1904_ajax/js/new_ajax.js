
function ajax(url,funcsuccess,funcfail){
//1 先要有一个电话             1 先要有一个ajax 对象 

//alert(window.XMLHttpRequest); //如果w3c IE8以上 返回真  否则返回假

if(window.XMLHttpRequest){
	var aJax = new XMLHttpRequest();//这是w3c浏览器支持的    
}else{
	var aJax = new ActiveXObject("Microsoft.XMLHTTP");
	//这是IE浏览器支持的
}

//2拨通美女号码                   2.连接服务器   
//method 请求方法  get post   GET POST  
//url 服务器的地址 
//true 异步  false 表示同步 
	aJax.open('GET',url,true);



//3说出你的心声    		3.发送请求  
	aJax.send();


//4等待美女答复                   4.等待服务器的返回  
	//接收服务器返回的数据 需要监听XMLHttpR	equest的状态   
	//当状态发生改变  会触发 readystatechange 事件  
	//onreadystatechange 有以下状态   
	//0  请求还没有初始化
	//1 已经建立连接了 
	//2 客户端的请求 服务器已经接收了
	//3 请求处理 
	//4 请求完成 开始响应  
	
	//2开头的表示成功 
	//4开头的表示  客户端这边出问题   
	//5开头表示  服务器这边出问题    
	aJax.onreadystatechange = function(){
		if(aJax.readyState == 4){
			if(aJax.status == 200){
//				alert(aJax.responseText);
				funcsuccess(aJax.responseText);
			}else{
//				alert(aJax.responseText);
				if(funcfail){
					funcfail()
				}
			}
		}
	}


}