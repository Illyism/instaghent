<%inherit file="base.mak"/>
<%block name="title">
About Instaghent | Everyday instagram images of Ghent, Belgium
</%block>
<style type="text/css">
  body {
    shape-rendering: crispEdges;
  }

  .day {
    fill: #fff;
    stroke: #ccc;
  }

  .month {
    fill: none;
    stroke: #000;
    stroke-width: 2px;
  }

  .arc path {
    stroke: #fff;
  }
  .arc text {
    font-size: 9px;
  }

  rect.bordered {
    stroke: #E6E6E6;
    stroke-width:2px;   
  }

  text.mono {
    font-size: 9pt;
    fill: #aaa;
  }

  text.axis-workweek {
    fill: #000;
  }

  text.axis-worktime {
    fill: #000;
  }

  #map {
  width: 100%;
  height: 100%;
  min-height: 500px;
  margin: 0;
  padding: 0;
}

.stations, .stations svg {
  position: absolute;
}

.stations svg {
  width: 60px;
  height: 20px;
  padding-right: 100px;
  font: 10px sans-serif;
}

.stations circle {
  fill: brown;
  stroke: black;
  stroke-width: 1.5px;
}

</style>
<div class="contain"><div class="ui stackable grid">
  <div class="ten column wide">
    <div class="ui segment teal">
      <h1>Instaghent</h1>
      <h2>Everyday Instagram photographs of Ghent, Belgium</h2>
    </div>
    <div class="ui segment red">
      <p>Instaghent is a collection of all the cool and amazing images taken in Ghent that can be found on Instagram. You can add your own images by adding the hashtag <b>#instaghent.</b></p><p>We want the citizens of Ghent and the travellers from all over the world to be able to see and enjoy the beauty and style of the city. People can take a picture of their favorite spot, tag it and it will show up here.</p><p>You can rate images as <b>Totally Ghent</b> and <b>Not Ghent</b>.</p>
    </div>
  </div>
  <div class="six column wide">
    <div class="ui segment purple">
      <p>This app is not connected to the City of Ghent in any way. The images are automatically added from several hashtags and location data used by Instagram. We are not responsible for what you see here, please rate any disturbing images you see as "Not Ghent".</p>
    </div>
    <div class="ui segment blue">
      <a href="http://www.illyism.com">Made By <b>Ilias Ismanalijev</b></a>
    </div>
  </div>
  <div class="sixteen column wide">
    <div class="ui segment calendar">
      <h2 class="ui header center aligned">#instaghents per Day</h2>
    </div>
  </div>
  <div class="sixteen column wide">
    <div class="ui segment" id="chart">
      <h2 class="ui header center aligned">#instaghents per Hour x Day of Week</h2>
    </div>
  </div>
  <div class="sixteen column wide">
    <div class="ui segment users">
      <h2 class="ui header center aligned">Top Users</h2>
    </div>
  </div>
  <div class="six column wide">
    <div class="ui segment filters">
      <h2 class="ui header center aligned">Most Used Filters</h2>
    </div>
  </div>
  <div class="ten column wide">
    <div id="map" class="ui segment"></div>
  </div>
</div></div>
<%block name="javascript">
  <script src="http://d3js.org/d3.v3.min.js"></script>
  <script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=true"></script>
  <script src="/js/statistics.js"></script>
  <script src="/js/filters.js"></script>
  <script src="/js/hours.js"></script>
  <script src="/js/users.js"></script>
  <script src="/js/stat_maps.js"></script>
</%block>