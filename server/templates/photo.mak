<%inherit file="base.mak"/>
<%block name="title">
% if photo["caption"] is not None:
	${photo["caption"]} | 
%endif
%if "author" in meta:
	@${meta['author']} | 
%else:
	${meta['filt']} | 
%endif
Instaghent
</%block>
<%block name="head">
<meta property="og:image" content="${photo['standard']}">
</%block>
<div class="contain"><div class="ui stackable grid photo" id="${photo['id']}">
  <div class="twelve column wide">
    <div class="ui segment teal">
  		<div class="ui image photo-img fluid" style="background-image: url(/photo?q=${photo['standard']});" data-adaptive-background='1' data-ab-css-background='1' alt="${photo['author']}" width="100%"></div>
    </div>
    %if "location" in photo:
    	%if photo["location"] is not None:
    		<div class="ui segment map">
    			<div class="title"><i class="icon map marker"></i>Map</div>
    			<div id="map" style="height:500px;"></div>
    		</div>
    	%endif
    %endif
    <div class="ui disqus segment purple">
    	<div id="disqus_thread"></div>
    </div>
	</div>
	<div class="four column wide">
		<div class="ui segment blue">
			<div class="ui menu fluid three item">
				<a tabindex="0" class="item thumbs up">
					<i class="icon thumbs up outline"></i>
				</a>
				<div class="item ghents">${photo["ghents"]}</div>
				<a tabindex="0" class="item thumbs down">
					<i class="icon thumbs down outline"></i>
				</a>
			</div>
		</div>
	% if photo["caption"] is not None:
		<div class="ui segment teal">
			<div class="title"><i class="icon comment"></i>Caption</div>
			<p class="caption">
				${photo["caption"]}
			</p>
		</div>
	% endif
		<div class="ui segment red">
			<div class="title"><i class="icon user"></i><a class="author item" href="/by/${photo['author']}">@${photo["author"]}</a></div>
			<img class="ui image rounded" width="100%" src="${photo['profile_picture']}">
			<div class="ui vertical fluid menu small">
				<a class="item" href="/by/${photo['author']}">More by @${photo["author"]}</a>
				<a class="item" target="_blank" href="http://www.instagram.com/${photo['author']}">Instagram Profile</a>
			</div>
		</div>
		<div class="ui segment details">
			<div class="title"><i class="icon instagram"></i>Details</div>
			<div class="ui menu vertical fluid">
				<span class="item"><i class="icon basic photo"></i> ${photo["filters"]}</span>
				<span class="item time"><i class="icon calendar"></i> ${photo["time"].strftime("%d %B %Y")}</span>
				<span class="item likes"><i class="icon like"></i> ${photo["likes"]} likes</span>
				<span class="item comments"><i class="icon chat"></i> ${photo["comments"]} comments</span>
				<a class="item" href="${photo['link']}">View on Instagram</a>
			</div>
		</div>
		<div class="ui segment tags">
			<div class="title"><i class="icon tags"></i>Tags</div>
			<div class="ui menu vertical fluid">
				%for tag in photo["tags"]:
					<span class="item">#${tag}</span>
				%endfor
			</div>
		</div>

	</div>

</div></div>
<%block name="javascript">
<script src="/js/bgcol.js"></script>
%if "location" in photo:
%if photo["location"] is not None:
	<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=true"></script>
	<script>
			function initialize() {
			  var myLatlng = new google.maps.LatLng${photo['location']};
			  var mapOptions = {
			    zoom: 15,
			    center: myLatlng
			  }
			  var map = new google.maps.Map(document.getElementById('map'), mapOptions);

			  var marker = new google.maps.Marker({
			      position: myLatlng,
			      map: map,
			      title: 'Hello World!'
			  });
			}

			google.maps.event.addDomListener(window, 'load', initialize);
	</script>
%endif
%endif
</%block>