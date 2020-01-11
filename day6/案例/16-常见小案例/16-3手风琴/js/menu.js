$( document ).ready( function(){
	$("#container dd").hover( function(){
		$( this ).toggleClass( "light" );	
	});
	$( "#container dt" ).click( function(){
		$( this ).siblings().show();
		$( this ).parent().siblings().find( "dd" ).hide();
	});
  
});