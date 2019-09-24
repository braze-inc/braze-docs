---
nav_title: Hacktober 2019
page_order: 1
permalink: /hacktober/
---

# Hacktober 2019

Braze Docs is now Open Source! To celebrate, we're participating in Hacktober!

{% comment %}
Learn more about [why we went open source](https://www.braze.com/perspectives/article/braze-open-source-documentation-announcement).
{% endcomment %}


## Participation

To participate, just...

1. Check out [our repo](https://github.com/Appboy/braze-docs) or click the <i class="fab fa-github"></i> __Edit this page on Github__ button at the bottom of most pages.
2. Sign [our CLA](http://braze.com/docs/cla).
3. [Make changes](https://github.com/Appboy/braze-docs/wiki/Contributor-Quick-Start-Guide)!

<br>

## To Do

We're still working on setting some things up, but trust us, they're on our mind!

| Migrate Issues to Public Repo | _Expect Friday, September 27, 2019._ |
| Announce Available Prizes | _Expect Early October 2019._ |
| Hacktober Final Report, Stats, and Winners | _Expect November 5, 2019._ |
| Contact Winners & Send Out Prizes | _Expect Mid-November 2019._ |

<br>

## Leaderboards

### PR Leaders

<iframe src="https://script.google.com/macros/s/AKfycbwwJwf3RbgRRx3Ls3QzvyYNrIRWBvO0ID4xtwnQSK_5uUjLb_Q/exec?type=pr" style="margin-top:20px; width:100%;min-height:650px;border:none;" id="gittoppr"></iframe>

### Commit Leaders

<iframe src="https://script.google.com/macros/s/AKfycbwwJwf3RbgRRx3Ls3QzvyYNrIRWBvO0ID4xtwnQSK_5uUjLb_Q/exec" style="width:100%;min-height:650px;border:none;" id="gittopcommit"></iframe>


<script type="text/javascript">
var eventMethod = window.addEventListener ? "addEventListener" : "attachEvent";
var eventer = window[eventMethod];
var messageEvent = eventMethod == "attachEvent" ? "onmessage" : "message";
eventer(messageEvent, function(e) {
    var data = JSON.parse(e.data);
    var scroll_height = data['height'] + 30;
    var targetdiv = '#gittop' + data['type'];
    $(targetdiv).height(scroll_height).css('min-height', scroll_height  + 'px');;
} , false);
</script>
