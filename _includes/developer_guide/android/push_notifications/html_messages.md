{% multi_lang_include developer_guide/prerequisites/android.md %} Additionally, you'll need to [set up push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## About HTML push notifications

In Braze SDK version 3.1.1, HTML can be sent to a device to render multiplier text in push notifications.

![An Android push message "Multicolor Push test message" where the letters are different colors, italicized and given a background color.]({% image_buster /assets/img/multicolor_android_push.png %}){: style="max-width:40%;"}

This example is rendered with the following HTML:

```html
<p><span style="color: #99cc00;">M</span>u<span style="color: #008080;">lti</span>Colo<span style="color: #ff6600;">r</span> <span style="color: #000080;">P</span><span style="color: #00ccff;">u</span><span style="color: #ff0000;">s</span><span style="color: #808080;">h</span></p>

<p><em>test</em> <span style="text-decoration: underline; background-color: #ff6600;"><strong>message</strong></span></p>
```

Keep in mind that, Android limits which HTML elements and tags are valid in your push notifications. For example, `marquee` is not allowed.

{% alert important %}
Multicolor text rendering is device-specific and may not display based on Android device or version.
{% endalert %}

## Supported HTML tags

Currently, Google doesn't list their supported HTML tags for Android directly in their documentation&#8212;this information can only be found in their [Git repository's `Html.java` file](https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/text/Html.java). Keep this in mind when referencing the following table, as this information was pulled from this file, and their supported HTML tags could be subject to change.

<table>
  <thead>
    <tr>
      <th>Category</th>
      <th>HTML Tag</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">Basic Text Styling</td>
      <td><code>&lt;b&gt;</code>, <code>&lt;strong&gt;</code></td>
      <td>Bold text</td>
    </tr>
    <tr>
      <td><code>&lt;i&gt;</code>, <code>&lt;em&gt;</code></td>
      <td>Italic text</td>
    </tr>
    <tr>
      <td><code>&lt;u&gt;</code></td>
      <td>Underline text</td>
    </tr>
    <tr>
      <td><code>&lt;s&gt;</code>, <code>&lt;strike&gt;</code>, <code>&lt;del&gt;</code></td>
      <td>Strikethrough text</td>
    </tr>
    <tr>
      <td><code>&lt;sup&gt;</code></td>
      <td>Superscript text</td>
    </tr>
    <tr>
      <td><code>&lt;sub&gt;</code></td>
      <td>Subscript text</td>
    </tr>
    <tr>
      <td><code>&lt;tt&gt;</code></td>
      <td>Monospace text</td>
    </tr>
    <tr>
      <td rowspan="3">Size/Font</td>
      <td><code>&lt;big&gt;</code>, <code>&lt;small&gt;</code></td>
      <td>Relative text size changes</td>
    </tr>
    <tr>
      <td><code>&lt;font color="..."&gt;</code></td>
      <td>Sets foreground color</td>
    </tr>
    <tr>
      <td><code>&lt;span&gt;</code> (with inline CSS)</td>
      <td>Inline styles (e.g., color, background)</td>
    </tr>
    <tr>
      <td rowspan="4">Paragraph &amp; Block</td>
      <td><code>&lt;p&gt;</code>, <code>&lt;div&gt;</code></td>
      <td>Block-level sections</td>
    </tr>
    <tr>
      <td><code>&lt;br&gt;</code></td>
      <td>Line break</td>
    </tr>
    <tr>
      <td><code>&lt;blockquote&gt;</code></td>
      <td>Quoted block</td>
    </tr>
    <tr>
      <td><code>&lt;ul&gt;</code> + <code>&lt;li&gt;</code></td>
      <td>Unordered list with bullets</td>
    </tr>
    <tr>
      <td>Headings</td>
      <td><code>&lt;h1&gt;</code> - <code>&lt;h6&gt;</code></td>
      <td>Headings (various sizes)</td>
    </tr>
    <tr>
      <td rowspan="2">Links &amp; Images</td>
      <td><code>&lt;a href="..."&gt;</code></td>
      <td>Clickable link</td>
    </tr>
    <tr>
      <td><code>&lt;img src="..."&gt;</code></td>
      <td>Inline image</td>
    </tr>
    <tr>
      <td>Other Inline</td>
      <td><code>&lt;em&gt;</code>, <code>&lt;strong&gt;</code>, <code>&lt;dfn&gt;</code>, <code>&lt;cite&gt;</code></td>
      <td>Synonyms for italic or bold</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Setting up HTML push notifications

To render multicolor text in a push notification, you can update your `braze.xml` or `BrazeConfig`:

{% tabs local %}
{% tab braze.xml %}
Add the following in your `braze.xml`:

```xml
<bool translatable="false" name="com_braze_push_notification_html_rendering_enabled">true</bool>
```
{% endtab %}

{% tab BrazeConfig %}
Add the following in your [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

{% subtabs local %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setPushHtmlRenderingEnabled(true)
  .build();
Braze.configure(this, brazeConfig);
```
 
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setPushHtmlRenderingEnabled(true)
    .build()
Braze.configure(this, brazeConfig)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
