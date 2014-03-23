<%inherit file="base.mak"/>
<%block name="title">
%if "author" in meta:
	@${meta['author']} | 
%else:
	${meta['filt']} | 
%endif
Instaghent
</%block>
<div class="photos">
	% for photo in items:
		<div class="photo" id="${photo['id']}">
			<a class="image" href="/by/${photo['author']}/${photo['id']}"  title="@${photo['author']}">
				<img src="${photo['low']}" alt="${photo['author']}">
			</a>
			% if photo["caption"] is not None:
			<p class="caption">
				${photo["caption"]}
			</p>
			% endif
			<div class="meta ui menu">
				<div class="left menu">
					<a class="author item" href="/by/${photo['author']}">@${photo["author"]}</a>
				</div>
				<div class="right menu">
					<span class="item time">${photo["time"].strftime("%d %B %Y")}</span>
				</div>
				<div class="sub menu">
					<div class="left menu">
						<span class="item likes"><i class="icon like"></i> ${photo["likes"]}</span>
						<span class="item comments"><i class="icon chat"></i> ${photo["comments"]}</span>
					</div>
					<div class="right menu">
						<a tabindex="0" class="item thumbs up">
							<i class="icon thumbs up outline"></i>
						</a>
						<div class="item ghents">${photo["ghents"]}</div>
						<a tabindex="0" class="item thumbs down">
							<i class="icon thumbs down outline"></i>
						</a>
					</div>
				</div>
			</div>
		</div>
	% endfor
</div>