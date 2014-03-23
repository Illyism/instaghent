var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-38201998-1']);
_gaq.push(['_setDomainName', 'instaghent.com']);
_gaq.push(['_trackPageview']);

(function() {
var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();


$(".photo a.thumbs").click(function(e) {
	var self = $(this);
	var parent = $(self.parents(".photo"));
	var icon = $(self.find(".icon"));
	var item = parent.attr("id");

	var thumbs = 0;
	if (self.hasClass("up")) thumbs = 1;

	icon.removeClass("thumbs " + (thumbs==1 ? "up" : "down")).addClass("loading");
	$.ajax({type:'POST',
		url: '/thumbs',
		data: JSON.stringify({"item": item, "thumbs": thumbs}),
		contentType: 'application/json; charset=utf-8',
		success: function(ghents) {
			console.log(item, ghents);
			self.addClass("active disabled " + (thumbs==1 ? "green" : "red"));
			icon.removeClass("loading outline").addClass("thumbs " + (thumbs==1 ? "up" : "down"));
			self.parent().find(".ghents").text(ghents);
		} 
	});
}).keydown(function(event){ // Keyboard accessibility
    if(event.keyCode==13){
       $(this).trigger('click');
    }
});

$(".sidebar-open").click(function() {
	$("#sidebar").sidebar("toggle");
});

// Tab Accessibility support
$(".photos .photo a").focus(function() {
	$(this).parents(".photo").addClass("active");
}).blur(function() {
	$(this).parents(".photo").removeClass("active");
})

$("#sidebar").sidebar();