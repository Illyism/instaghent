<!DOCTYPE html>
<html lang="{{i18n.lang}}">
	<head>
		<link rel="dns-prefetch" href="//fonts.googleapis.com">
		<link rel="dns-prefetch" href="//code.jquery.com">
		<link rel="dns-prefetch" href="//1-ps.googleusercontent.com">
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>{% block title %}Instaghent{% endblock %}</title>
		<meta name="description" content="{% block description %}{{i18n.metashort}}{% endblock %}" />
		<meta name="keywords" content="instagram, gent, ghent, instaghent" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0" />
		<link type="text/css" rel="stylesheet" href="/css/style.css" />
		<link rel="shortcut icon" href="/favicon.ico" />
		<%block name="head"/>
	</head>

	<body>
		<div class="ui fixed top menu">
      <div class="left menu">
        <a class="sidebar-open item">
          <i class="list layout icon"></i> Settings
        </a>
        <a href="/" class="item">Instaghent</a>
        <%def name="addAuthor(author)">
        % if "author" in meta:
          <a href="/by/${meta['author']}" class="active item">By @${meta['author']}</a>
        % endif
        </%def>
        ${addAuthor(author)}
      </div>
      <div class="right menu">
        <a href="/about" class="item">About</a>
      </div>
    </div>
    <div class="ui thin sidebar navigation segment" id="sidebar">
      <div class="ui text vertical menu">
        <a class="sidebar-open black item">
          <i class="close icon"></i> Close
        </a>
        <div class="item">
          <i class="filter icon"></i> Filter By
          <div class="menu">
            <%def name="isFilter(x)">
                % if meta["filt"] == x:
                active
                % endif
            </%def>
            <a href="/time" class="${isFilter('time')}item">Time</a>
            <a href="/ghents" class="${isFilter('ghents')}item">Ghents</a>
            <a href="/likes" class="${isFilter('likes')}item">Likes</a>
            <a href="/comments" class="${isFilter('comments')}item">Comments</a>
            ${addAuthor(author)}
          </div>
        </div>
        <div class="item">
          <i class="calendar icon"></i> From
          <div class="menu">
            <a class="item">Today</a>
            <a class="item">This Week</a>
            <a class="item">This Month</a>
            <a class="item">This Year</a>
            <a class="active item">All Time</a>
          </div>
        </div>
      </div>
    </div>
		<div class="content">
			${self.body()}
		</div>
		<script src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
		<script src="/js/semantic.min.js"></script>
		<%block name="javascript"/>
		<script src="/js/instaghent.js"></script>
	</body>
</html>