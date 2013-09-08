function isValidURL(url)
{
      var urlregex = new RegExp(
			            "^(http|https|ftp)\://([a-zA-Z0-9\.\-]+(\:[a-zA-Z0-9\.&amp;%\$\-]+)*@)*((25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])|([a-zA-Z0-9\-]+\.)*[a-zA-Z0-9\-]+\.(com|edu|gov|int|mil|net|org|biz|arpa|info|name|pro|aero|coop|museum|[a-zA-Z]{2}))(\:[0-9]+)*(/($|[a-zA-Z0-9\.\,\?\'\\\+&amp;%\$#\=~_\-]+))*$");
									      return urlregex.test(url);
}

$(document).ready(function(){

	$("#loader").hide(); 
	$("#warning").hide();

	$("#url_input").click(function(){
		$("#url_input").attr("value", "");
		$("#url_input").css("color", "black");
		$("#url_input").css("font-size", "20");

	});

	$("#url_submit").click(function(){ 

		
		$("#loader").show();
		$("#warning").hide();

		$.ajax({
			type: "POST",
			url: "process_url.php",
			data: {url: $("#url_input").val()},
			success: function(ret){
				if(ret=="no_rss")
				{
					alert("no_rss");
					$("#warning").show();
					return false;
				}
				alert("success!");
				$("#result").html("Thank you for using Wulu. The link to your podcast is: <br> <a id=\"link\" href=\""+ret+"\">"+ret+"</a>");

				$("#loader").hide();
				return false;
			},
			error: function(a,b,c)
			{
				alert(c);

			}
		});

		return false;


	});

	$("#url_submit_button").click(function(){
		$("#url_submit").click(); 
		return false;
	});

});
