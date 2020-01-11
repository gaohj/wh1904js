$(function(){
	adreshow();
	//点击che复选框 也就是单行的复选框时
	$(".che").on("click",function(){
		if($(this).is(":checked")){//当前点击的复选框的值为true
			$(this).parent().parent().addClass("djbj");
		}else{//当前点击的复选框的值为false
			$(this).parent().parent().removeClass("djbj");

		}
	})
	//当点击allcheck时 也就是 几个全选的文本框时 将所有的复选框的值设置为true
	$(".allcheck").click(function(){
		if($(this).is(":checked")){
			$("input[type='checkbox']").prop("checked",true);
			$(".tbodys1").addClass("djbj");
			$(".tbodys2").addClass("djbj");
		}else{
			$("input[type='checkbox']").prop("checked",false);
			$(".tbodys1").removeClass("djbj");
			$(".tbodys2").removeClass("djbj");
		}
		
	})
	//点击减号按钮
	var num=1,//初始化txt中的值
		price1=20.90,//初始化mess1中的单价
		price2=13.90;//初始化mess2中的单价
	$(".mess1>li>.jia").click(function(){//点击mess1中的加号按钮时
		num++;//文本框中的值自增
		sum=price1*num;//计算总价=num*price1
		zj=sum.toFixed(2);//将总价保留两位小数
		$(".mess1>li>.txt").val(num);//否则将文本框的值设为num最后的结果
		$(".mess1>li>b").text(zj);//将b标签中的值设为保留两位小数后的值
		
	})
	$(".mess1>li>.jian").click(function(){//点击mess1中的减号按钮时
		num--;//文本框中的值自减
		sum=price1*num;//计算总价=num*price1
		zj=sum.toFixed(2);//将总价保留两位小数
		if(num<1){//判断最小值为1
			num=1;
		}else{
			$(".mess1>li>.txt").val(num);//否则将文本框的值设为num最后的结果
			$(".mess1>li>b").text(zj);//将b标签中的值设为保留两位小数后的值
		}
	})
	$(".mess2>li>.jia").click(function(){//点击mess2中的加号按钮时
		num++;//文本框中的值自增
		sum=price1*num;//计算总价=num*price2
		zj=sum.toFixed(2);//将总价保留两位小数
		$(".mess2>li>.txt").val(num);//否则将文本框的值设为num最后的结果
		$(".mess2>li>b").text(zj);//将b标签中的值设为保留两位小数后的值
		
	})
	$(".mess2>li>.jian").click(function(){//点击mess1中的减号按钮时
		num--;//文本框中的值自减
		sum=price2*num;//计算总价=num*price1
		zj=sum.toFixed(2);//将总价保留两位小数
		if(num<1){//判断最小值为1
			num=1;
		}else{
			$(".mess2>li>.txt").val(num);//否则将文本框的值设为num最后的结果
			$(".mess2>li>b").text(zj);//将b标签中的值设为保留两位小数后的值
		}
	})
	//点击移除所执行的效果
	$("#dele1").click(function(){
		$(this).parents(".tbodys1").remove();
	})
	$("#dele2").click(function(){
		$(this).parents(".tbodys2").remove();
	})
	//main3相关效果
	$(".main3>ol").on("mouseover","li",function(){
		var idx=$(this).index();//获取当前划过的标题的li的索引
		$(this).addClass("on").siblings().removeClass("on");
		$(".main3>ul>li").eq(idx).show().siblings().hide();
	})
})
function adreshow(){
	$(".addr").on("mouseover",function(){//找到.addr添加mouseover事件
		$("#city").show();//将城市显示
		$("#city>ul>li").each(function(){//找到北京 朝阳区 三环到四环之间 添加mouseover事件 遍历
			$(this).mouseover(function(){
				var idx=$(this).index();
				//console.log(idx)
				//给当前划过的li添加overbj样式
				$(this).addClass("overbj").siblings().removeClass("overbj");
				//划过ul中的li时 相对应的 ol的li 也随之变化 找到所有的ol 通过eq找到和ul中的li idx相对的ol显示 其他的隐藏
				$("#city>ol").eq(idx).show().siblings("ol").hide();
			})
			$("#city").mouseleave(function(){//鼠标离开隐藏
				$("#city").hide();
			})
		})
	})	
}