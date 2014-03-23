<%inherit file="base.mak"/>
<div class="photo" id="${photo['id']}">
	<a class="image" href="/by/${photo['author']}/${photo['id']}"  title="@${photo['author']}">
		<img src="${photo['standard']}" alt="${photo['author']}">
	</a>
	% if photo["caption"] is not None:
	<p class="caption">
		${photo["caption"]}
	</p>
	% endif
	<div class="meta ui vertical fixed icon right menu">
		<a class="author item" href="/by/${photo['author']}">@${photo["author"]}</a>
		<span class="item time">${photo["time"].strftime("%d %B %Y")}</span>
		<span class="item likes"><i class="icon like"></i> ${photo["likes"]}</span>
		<span class="item comments"><i class="icon chat"></i> ${photo["comments"]}</span>
		<a tabindex="0" class="item thumbs up">
			<i class="icon thumbs up outline"></i>
		</a>
		<div class="item ghents">${photo["ghents"]}</div>
		<a tabindex="0" class="item thumbs down">
			<i class="icon thumbs down outline"></i>
		</a>
	</div>
</div>
