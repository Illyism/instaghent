var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-38201998-1']);
_gaq.push(['_setDomainName', 'instaghent.com']);
_gaq.push(['_trackPageview']);

(function() {
var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();

function set_ghents(item) {
	var self = $(item);
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
}
$(".photo a.thumbs").click(function(e) {
	set_ghents(this);
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

var offset=0;
var limit=50;
var order="DESC";
function get_more() {
	offset+=limit;
	$.ajax({type:'POST',
		url: '/more',
		data: JSON.stringify({"offset": offset, "limit": limit, "order": order, "timeframe": timeframe, "filt": filt}),
		contentType: 'application/json; charset=utf-8',
		success: function(items) {
			items = JSON.parse(items).items;
			for (var i = 0; i < items.length; i++) {
				var time = new Date(items[i]["time"]);
				items[i]["time"] = time.toDateString();
				var renderedItem = make_item(items[i]);
				$(".photos").append(renderedItem);
				if (renderedItem.hide) {
					renderedItem.hide().fadeIn();
				}
			};
		} 
	});
}

var FN = {}, // Precompiled templates (JavaScript functions)
  template_escape = {"\\": "\\\\", "\n": "\\n", "\r": "\\r", "'": "\\'"},
  render_escape = {'&': '&amp;', '"': '&quot;', '<': '&lt;', '>': '&gt;'};

function escape(str) {
  return str == undefined ? '' : (str+'').replace(/[&\"<>]/g, function(char) {
    return render_escape[char];
  });
}

$.render = function(tmpl, data, escape_fn) {
  if (typeof escape_fn != 'function' && escape_fn !== false) escape_fn = escape;
  tmpl = tmpl || '';

  return (FN[tmpl] = FN[tmpl] || new Function("_", "e", "return '" +

    tmpl.replace(/[\\\n\r']/g, function(char) {
      return template_escape[char];

    }).replace(/{\s*([\w\.]+)\s*}/g, "'+(function(){try{return e?e(_.$1):_.$1}catch(e){return ''}})()+'") + "'"

  ))(data, escape_fn);

};

function make_item(item) {
	return $.render($(".templates-photo").html(), item);
}

$(window).scroll(function(e) {
    if( $('body').scrollTop() == $(document).height() - $("body").height()) {
       get_more();
       $(window).scrollTop($(window).scrollTop()-1);
    }
})