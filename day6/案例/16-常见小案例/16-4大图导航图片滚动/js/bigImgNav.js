$( document ).ready(function(e) {
	alert($(window).width())
	
	var imgSize = 6;
	for( var i = 0; i < imgSize; i++ ){
		$( "ol" ).append( "<li><img src='img/li" + (i+1) + ".jpg' /></li>" );
	}
	$( "ol" ).width( imgSize * 61 );
	
	$( "b,s" ).hover(function(){
		$( this ).toggleClass( "hover" );	
	});
	
	$( "li" ).mouseover( function(){
		$( this ).addClass( "hover" ).siblings().removeClass( "hover" );
		$( "dt img" ).attr( "src", "img/" + ( $(this).index()+1 ) + "md.jpg" );
	});
	
	if( imgSize > 5 ){
		$( "b" ).click( function(){
			if( $( "ol" ).css( "margin-left" ) != "0px" ){
				$( "ol" ).not( ":animated" ).animate({"margin-left": "+=61" });
			}
		});
		$( "s" ).click( function(){
			if( $( "ol" ).css( "margin-left" ) != ($( "li" ).length-5) * -61 + "px" ){
				$( "ol" ).not( ":animated" ).animate({"margin-left": "-=61" });
			}
		});
	}
	
});