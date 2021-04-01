---
nav_title: Styling Test Page
page_order: 2
hidden: true
---

# Header Test

# H1 Banner
H1 Text

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor.
Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

Donec pellentesque facilisis odio, sed imperdiet ante. Maecenas blandit justo sed turpis auctor varius. Morbi sollicitudin erat in ex egestas condimentum a et mi.

## H2 Banner
H2 Text

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor.
Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Donec pellentesque facilisis odio, sed imperdiet ante. Maecenas blandit justo sed turpis auctor varius. Morbi sollicitudin erat in ex egestas condimentum a et mi.

### H3 Banner
H3 Text

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor.
Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Donec pellentesque facilisis odio, sed imperdiet ante. Maecenas blandit justo sed turpis auctor varius. Morbi sollicitudin erat in ex egestas condimentum a et mi.

#### H4 Banner
H4 Text

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor.
Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Donec pellentesque facilisis odio, sed imperdiet ante. Maecenas blandit justo sed turpis auctor varius. Morbi sollicitudin erat in ex egestas condimentum a et mi.

##### H5 Banner
H5 Text

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor.
Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Donec pellentesque facilisis odio, sed imperdiet ante. Maecenas blandit justo sed turpis auctor varius. Morbi sollicitudin erat in ex egestas condimentum a et mi.

###### H6 Banner
H6 Text

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor.
Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Donec pellentesque facilisis odio, sed imperdiet ante. Maecenas blandit justo sed turpis auctor varius. Morbi sollicitudin erat in ex egestas condimentum a et mi.

# Font Test
Normal

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor.
Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Donec pellentesque facilisis odio, sed imperdiet ante. Maecenas blandit justo sed turpis auctor varius. Morbi sollicitudin erat in ex egestas condimentum a et mi.

*Emphasize Text*

**Bold**

_**Bold Emphasize**_

~~Strikethrough~~


# Quote
> Quoted Text

# Inline quotes
Lorem ipsum dolor ``sit amet, consectetur adipiscing elit``. Sed nec tortor at lectus tempus tempor.
Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. ``Donec pellentesque facilisis odio``, sed ``imperdiet ante``. Maecenas blandit justo sed turpis auctor varius. Morbi sollicitudin erat in ex egestas condimentum a et mi.

# Pre
```
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor.
Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Donec pellentesque facilisis odio, sed imperdiet ante. Maecenas blandit justo sed turpis auctor varius. Morbi sollicitudin erat in ex egestas condimentum a et mi.
```

# Table

Instance    | Dashboard URL   | REST Endpoint
----------- |---------------- | --------------------
US-01 | `https://dashboard.braze.com` or<br> `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com`
US-02 | `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com`
US-03 | `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com`
US-04 | `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com`
US-06 | `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com`
EU-01 | `https://dashboard.braze.eu` or<br> `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu`
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Resetting Table word-break by column
For tables columns which word-break should be reset to the default style, use markdown options to add a class to the table using `.reset-td-br-1`, `.reset-td-br-2`, `.reset-td-br-3` , `.reset-td-br-4`, with the `#` corresponding to the column up to 4.

### Usage
```
| Event Name                           | Feed Type              | Description                                                                               | Custom Attributes
| ------------------------------------ | ---------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG | Unbound Feed           | An email was successfully delivered to a User’s mail server.                              | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`                      |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG`                       | Unbound Feed           | User opened an email.                                                                     | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`                      |
| In-App Message Impression            | Platform-specific Feed | User viewed an In-App Message.                                                            | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`             |
| In-App Message Clicked               | Platform-specific Feed | User tapped or clicked a button in an In-App Message.                                     | `button_id`, `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
| Content Card Dismissed               | Platform-specific Feed | User dismissed a Content Card                                                             | `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| News Feed Viewed                     | Platform-specific Feed | User viewed the native Braze News Feed.                                                   | `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| News Feed Card Viewed                | Platform-specific Feed | User viewed a Card within the native Braze News Feed.                                     | `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

```

#### Before

| Event Name                           | Feed Type              | Description                                                                               | Custom Attributes
| ------------------------------------ | ---------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG | Unbound Feed           | An email was successfully delivered to a User’s mail server.                              | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`                      |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG`                         | Unbound Feed           | User opened an email.                                                                     | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`                      |
| In-App-Message-Impression            | Platform-specific Feed | User viewed an In-App Message.                                                            | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`             |
| In-App Message Clicked               | Platform-specific Feed | User tapped or clicked a button in an In-App Message.                                     | `button_id`, `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
| Content Card Dismissed               | Platform-specific Feed | User dismissed a Content Card                                                             | `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| News Feed Viewed                     | Platform-specific Feed | User viewed the native Braze News Feed.                                                   | `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| News Feed Card Viewed                | Platform-specific Feed | User viewed a Card within the native Braze News Feed.                                     | `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

#### After

| Event Name                           | Feed Type              | Description                                                                               | Custom Attributes
| ------------------------------------ | ---------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG | Unbound Feed           | An email was successfully delivered to a User’s mail server.                              | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`                      |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG`                       | Unbound Feed           | User opened an email.                                                                     | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`                      |
| In-App-Message-Impression            | Platform-specific Feed | User viewed an In-App Message.                                                            | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`             |
| In-App Message Clicked               | Platform-specific Feed | User tapped or clicked a button in an In-App Message.                                     | `button_id`, `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
| Content Card Dismissed               | Platform-specific Feed | User dismissed a Content Card                                                             | `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| News Feed Viewed                     | Platform-specific Feed | User viewed the native Braze News Feed.                                                   | `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| News Feed Card Viewed                | Platform-specific Feed | User viewed a Card within the native Braze News Feed.                                     | `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

# Link Test
Link here: [Braze.com](https://www.braze.com){: height="36px" width="36px"}

# Image Test
Image: ![Logo]({{site.baseurl}}/assets/img/braze-logo-mark.png){: height="36px" width="36px"}

## Linked Image Test
Linked Image: [![Braze]({{site.baseurl}}/assets/img/braze-logo-mark.png){: height="36px" width="36px"}](https://www.braze.com)

## Gallery Test

{% gallery %}
{{site.baseurl}}/assets/img_archive/EBTH_Email.png?bf892368baf287cba5ab9a6e3b09431d  <br> This is a [link](https://www.braze.com).
{{site.baseurl}}/assets/img_archive/iHeartRadio_Email.png?ecd2c8fe148939b7de957fe85cd6317e  <br> This is another `comment`.
{{site.baseurl}}/assets/img_archive/Saucey_Email.png?b9768937a1cc12d4c08e55a52e700d68  <br> This is yet another __comment__.
{% endgallery %}

Other content

{% gallery %}
{{site.baseurl}}/assets/img/schellman_iso27001_seal_grey_CMYK_300dpi_jpg.png?1b1fb9dbb80b0332c62512dcf9c83258 <br> **IMAGE TITLE** <br> This is a test to see if it will line break.
{{site.baseurl}}/assets/img/SOC2.png?6338040be8e98c4c9abe1f35b3e43e3a  <br> This is a regular comment.
{% endgallery %}

## Interactive Image Test

<div class="iactiveImg" data-ii="6967"></div><script src="https://interactive-img.com/js/include.js"></script>

<div style="position: relative; padding-bottom: 83%; padding-top: 0; height: 0;"><iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-width:0px; max-width:100%; overflow-y:auto;" width="100%" height="100%" src="https://interactive-img.com/view?id=6967&iframe=true"></iframe></div>

# Code Test Objective C
```objc
- (void)submitFeedback:(ABKFeedback * )feedback
 withCompletionHandler:(nullable void (^)(ABKFeedbackSentResult feedbackSentResult))completionHandler;


# Code Test Swift
```swift
Appboy.sharedInstance()?.submitFeedback(feedback) { (feedbackSentResult) in
      print("Feedback sent: (feedbackSentResult)")
    }
```

# Code Test Java
```java
@Override
public void onResume() {
  super.onResume();
  // Registers the AppboyInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  AppboyInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

# Code Test json
```json
{
   "attributes" : "Attributes" ,
   "events" : ["Array", "Of", "Object"],
   "purchases" : ["Array" ,"Of" ,"Purchase" ,"Object"]
}
```





# Code Test JavaScript
```javascript
appboy.subscribeToFeedUpdates(function(feed) {
  var cards = feed.cards;
  appboy.display.showFeed(undefined, cards);
});
appboy.requestFeedRefresh();
```

# Pygments Test
```python
#!/usr/bin/python3

from engine import RunForrestRun

"""Test code for syntax highlighting!"""

class Foo:
	def __init__(self, var):
		self.var = var
		self.run()

	def run(self):
		RunForrestRun()  # run along!

```
# Short Alert Test

{{site.data.alerts.tip}} This is a Tip {{site.data.alerts.end}}

{{site.data.alerts.note}} This is a note {{site.data.alerts.end}}

{% alert important %}
This is a important `adsadasd`
 {%endalert%}

{{site.data.alerts.warning}}This is a warning {{site.data.alerts.end}}

{{site.data.alerts.update}}This is an update {{site.data.alerts.end}}



## Long Alert test

 {% alert note %}
  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor.
 Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Donec pellentesque facilisis odio, sed imperdiet ante. Maecenas blandit
 justo sed turpis auctor varius. Morbi sollicitudin erat in ex egestas condimentum a et mi.
 Sed bibendum condimentum lectus, quis venenatis neque volutpat eget.
 Sed sodales felis ut nisi ullamcorper pharetra. Sed ut justo mollis, aliquet ipsum ac, pharetra nunc.
 Etiam pretium mauris eu leo vestibulum, in laoreet urna rhoncus. Proin ut varius diam, et fringilla nibh.
 {% endalert %}

 {% alert important %}
 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor.
 Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Donec pellentesque facilisis odio, sed imperdiet ante. Maecenas blandit
 justo sed turpis auctor varius. Morbi sollicitudin erat in ex egestas condimentum a et mi.
 Sed bibendum condimentum lectus, quis venenatis neque volutpat eget.
 Sed sodales felis ut nisi ullamcorper pharetra. Sed ut justo mollis, aliquet ipsum ac, pharetra nunc.
 Etiam pretium mauris eu leo vestibulum, in laoreet urna rhoncus. Proin ut varius diam, et fringilla nibh.
 {% endalert %}

 {% alert update %}
 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor.
 Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Donec pellentesque facilisis odio, sed imperdiet ante. Maecenas blandit
 justo sed turpis auctor varius. Morbi sollicitudin erat in ex egestas condimentum a et mi.
 Sed bibendum condimentum lectus, quis venenatis neque volutpat eget.
 Sed sodales felis ut nisi ullamcorper pharetra. Sed ut justo mollis, aliquet ipsum ac, pharetra nunc.
 Etiam pretium mauris eu leo vestibulum, in laoreet urna rhoncus. Proin ut varius diam, et fringilla nibh.
 {% endalert %}

 {% alert tip %}
 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor.
 Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Donec pellentesque facilisis odio, sed imperdiet ante. Maecenas blandit
 justo sed turpis auctor varius. Morbi sollicitudin erat in ex egestas condimentum a et mi.
 Sed bibendum condimentum lectus, quis venenatis neque volutpat eget.
 Sed sodales felis ut nisi ullamcorper pharetra. Sed ut justo mollis, aliquet ipsum ac, pharetra nunc.
 Etiam pretium mauris eu leo vestibulum, in laoreet urna rhoncus. Proin ut varius diam, et fringilla nibh.
{% endalert %}

 {% alert warning %}

Alert Liquid (Warning) Tag test

Should support the same list of tags above.

usage:
{% raw  %}

```liquid
{% alert [alertname] %}
Content

{% endalert %}

```
{% endraw  %}

example:

{% raw  %}

```liquid
{% alert important %}
this is a very important alert

{% endalert %}

```
{% endraw  %}

Link here: [Braze.com](https://www.braze.com)


 {% endalert %}

# Embedded video/youtube test
Defaults to youtube embedded.
{% include video.html id="XY5uXoKIvFY" %}


# Embedded video right align test
{% include video.html id="XY5uXoKIvFY" align="right" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis congue tortor sed tincidunt cursus. Sed iaculis molestie ligula, vel aliquam ante ultrices vel. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum nec risus velit. Curabitur urna tellus, dictum non convallis ac, porta vel neque. Ut egestas magna et turpis ullamcorper ultricies. Cras dolor lacus, fringilla sed enim ut, porttitor convallis arcu. Nam placerat neque vitae vestibulum dictum. Nam in pulvinar neque. Quisque eget sodales est. Mauris mattis porta felis scelerisque convallis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nunc sodales nibh vitae felis ultrices consectetur. Etiam efficitur elementum ante.

Vivamus ac commodo massa. Donec maximus, arcu nec aliquet malesuada, augue nibh venenatis elit, nec egestas libero turpis nec est. Aliquam condimentum molestie massa in finibus. Nulla sit amet pretium lectus, ut pulvinar mi. Fusce eget sapien ac diam mollis aliquam. Sed tellus est, tristique sed turpis vel, aliquet mattis nunc. Vestibulum maximus, dolor et luctus malesuada, leo sapien facilisis turpis, tincidunt suscipit turpis massa condimentum tortor. Nulla molestie at ex placerat vulputate. Integer sed tortor vel mauris rutrum consectetur a nec sapien.

Proin sed commodo mi, non bibendum metus. Praesent non justo lacus. Curabitur non feugiat nisl. Nam commodo tortor quis urna auctor consectetur. Duis at nisl eu tellus consectetur laoreet. Integer id orci congue, elementum ex non, lacinia neque. Aenean dictum tempus nibh ac fringilla. Vestibulum condimentum vel lectus ac lobortis. Nulla vehicula semper nisi, sed sodales metus ornare nec. Cras leo urna, finibus vitae nisi sit amet, mattis aliquam mi.


# Embedded video left align test
{% include video.html id="XY5uXoKIvFY" align="left" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed pretium elit non pulvinar tristique. Sed tellus dolor, commodo id laoreet non, pretium id velit. Donec tristique egestas felis, quis sagittis nibh sodales quis. Ut ut urna faucibus, sagittis justo dictum, efficitur arcu. Phasellus consequat nunc mollis, convallis eros at, euismod ex. Morbi id finibus velit, eu sollicitudin sem. Cras feugiat quis nibh non convallis.

Donec urna odio, gravida eu arcu sit amet, placerat aliquam erat. In sit amet nulla fermentum, tempor nulla nec, eleifend urna. Proin condimentum ipsum arcu, et venenatis elit luctus nec. Vestibulum risus lacus, cursus eget lacus eu, aliquam malesuada justo. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nunc porttitor rutrum molestie. Aenean in ligula at odio dignissim sodales. Nunc consequat enim id odio varius aliquam. Maecenas tempus ipsum id ligula bibendum congue. Praesent sed urna vitae velit dapibus scelerisque vel a magna. Phasellus molestie lobortis sem eu malesuada.


## Usage:
{% raw  %}
```html
{% include video.html id="[youtubeid]" %}
```
{% endraw  %}

To align right or left, and limit max width to 50% use the `align` parameter = `left` or `right`:
{% raw  %}
```html
{% include video.html id="[youtubeid]" align="left" %}

{% include video.html id="[youtubeid]" align="right" %}

```
{% endraw  %}

# Featured video layout with static placement for higher resolution
To use the featured video layout which places a static video on the left side
for higher resolution display, add a video_id and a video_type ie `youtube` to
the yaml header for the page.
video_source defaults to `youtube`

{% raw  %}
```yaml
layout: featured_video
video_id: [video_id]
video_source: youtube
```
{% endraw  %}

# List Test

## Bullet
* List 1
  * Sub List 1
* List 2
  * Sub List 2a
    * Sub Sub List 2
* List 3

## Numbered
1. List 1
  * Sub List 1
2. List 2
3. List 3
  * Sub List 3a
  * Sub List 3b
    * Sub Sub List 3
4. List 4
    1. Sub list 4a
        1. Sub Sub List 4
    2. Sub list 4b
        1. sub sub list 4

# Horizontal Rule

---
___
***

# Collapsible Content

{% details CLICK ME TO EXPAND %}
#### Look a Hidden Code Block!

```python
print("hello world!")
```

{% enddetails %}


# Custom Tabs

{% tabs %}
{% tab OBJECTIVE-C %}

Add the following line of code to your `AppDelegate.m` file:

```objc
{% if include.platform == 'iOS' %}#import "Appboy-iOS-SDK/AppboyKit.h"{% else %}#import <AppboyTVOSKit/AppboyKit.h>{% endif %}
```

Within your `AppDelegate.m` file, add the following snippet within your `application:didFinishLaunchingWithOptions` method:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

{% endtab %}
{% tab swift %}

If you are integrating the Braze SDK with CocoaPods or Carthage, add the following line of code to your `AppDelegate.swift` file:

```swift
{% if include.platform == 'iOS' %}#import Appboy_iOS_SDK{% else %}#import AppboyTVOSKit{% endif %}
```

For more information about using Objective-C code in Swift projects, please see the [Apple Developer Docs][apple_initial_setup_19].

In `AppDelegate.swift`, add following snippet to your `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

{% endtab %}
{% endtabs %}


## Usage
{%raw %}
Enclose __tabs__ in a `{% tabs %}` and `{% endtabs %}`
Enclose individual __tab__ with the Liquid code and name of the tab `{% tab [Tab name] %}` and `{% endtab %}`
{% endraw %}

{% alert important %}
 Note number of tabs on the page should be consistent, otherwise tabs content might be hidden.
 For example if one set of tabs has `C++`,`C-Sharp` and `JS`, and another set of tabs has `C-Sharp` and `JS`,
 then when somebody clicks on `C++`, the other section will show nothing. See local tabs option below for workaround.
{% endalert %}

{%raw %}
```liquid
{% tabs %}
  {% tab objective-c %}
    Content of objective-c
  {% endtab %}
  {% tab swift %}
    Content of swift
  {% endtab %}
{% endtabs %}
```

{% endraw %}

### Local Tabs
For self contain tabs, ie tabs that only change the tab content for the specific section, then use the local parameter in the parent tabs block.

{%raw %}
```liquid
{% tabs local %}
...
{% endtabs %}
```
{% endraw %}

## Sub Tabs
For tabs within tabs, `subtabs` and `subtab` can be used. Default setting is `local`.
For global `subtabs`, use the `global` option: {%raw %}`{% subtabs global %}`{% endraw %}

{% tabs local %}
{% tab Tab 1 %}
tab content 1
{% subtabs %}
{% subtab Sub Tab 1a %}
Sub Tab 1a Content
{% endsubtab %}
{% subtab Sub Tab 2a %}
Sub Tab 2a Content
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Tab 2 %}
tab content 2
{% subtabs %}
{% subtab Sub Tab 1b %}
Sub Tab 1a Content
{% endsubtab %}
{% subtab Sub Tab 2b %}
Sub Tab 2a Content
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Example
{% raw %}
```
{% tabs %}
{% tab Tab 1 %}
{% subtabs %}
{% subtab Sub Tab 1 %}
Sub Tab 1 Content
{% endsubtab %}
{% subtab Sub Tab 2 %}
Sub Tab 2 Content
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
```
{% endraw %}
# Images

## Image Styling

![Text]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="max-width:600px; color: green" }
