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