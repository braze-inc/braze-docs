{% if include.variable_name == "image behavior" %}


| Layout | Behavior |
| --- | --- |
| Image and text | Tall or narrow images will scale down and be horizontally centered. Wide images will be clipped on the left and right edges. |
| Image only | The message will resize to fit images of most aspect ratios. |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "payload size" %}

We recommend the following payload sizes:

| Messaging system | Recommended payload |
| --- | --- |
| iOS (pre-iOS 8) | 0.256 KB |
| iOS (post-iOS 8) | 2 KB |
| Android (FCM) | 4 KB |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "in-app messages" %}

Modal in-app messages are designed to fit the device at the best and most filling ratios possible, while staying true to the size and ratios of your chosen image or copy for your message.

While there are no limits to how many text characters you can include in an in-app message (as well as buttons, headline, main body, and others), we moderate how many text characters you use. Too much text will require users to expand and scroll the message.

All in-app messages have a recommended image size of 500 KB, maximum image size of 5 MB, and support PNG, JPEG, and GIF file types.

{% tabs %}
{% tab Portrait %}

| Type | Aspect ratio | Image quality | Notes |
| --- | --- | --- | --- |
| Portrait full screen with text | 6:5 | High resolution 1200 x 1000 px <br>Minimum resolution 600 x 500 px | Cropping can occur on all sides, but the image will always fill the top 50% of the viewport. |
| Portrait full screen (image only, with or without buttons) | 3:5 | High resolution 1200 x 2000 px <br> Minimum resolution 600 x 1000 px | Cropping can occur on the left and right edges on taller devices. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab Landscape %}

| Type | Aspect ratio | Image quality | Notes |
| --- | --- | --- | --- |
| Landscape full screen with text | 10:3 | High resolution 2000 x 600 px <br>Minimum resolution 1000 x 300 px | Cropping can occur on all sides, but the image will always fill the top 50% of the viewport. |
| Landscape full screen (image only, with or without buttons) | 5:3 | High resolution 2000 x 600 px <br> Minimum resolution 1000 x 600 px | Cropping can occur on the left and right edges on taller devices. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab Slideup %}

| Type | Aspect ratio | Image quality | Notes |
| --- | --- | --- | --- |
| Slideup | 1:1 | High resolution 150 x 150 px <br> Minimum resolution 50 x 50 px | Images of various aspect ratios will fit into a square image container, without cropping. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab Modal %}

| Type | Aspect ratio | Image quality | Notes |
| --- | --- | --- | --- |
| Modal (image only) | 1:1 | Maximum Recommended Resolution: 1200 x 2000 px <br> Minimum resolution: 600 x 600 px | The message will resize to fit images of most aspect ratios. The recommended maximum resolution has a 3:5 aspect ratio, which may not provide optimal results - while larger images are usable, they may lead to longer load times. <br> The ideal aspect ratio for images is 1:1 and not meeting this ratio may trigger a warning during upload. This warning is a suggestion for best results and does not prevent the upload of larger images. |
| Modal with text | 29:10 | High resolution 1450 x 500 px <br> Minimum resolution 600 x 205 px | Tall images will scale down and be horizontally centered. Wide images will be clipped on the left and right edges. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% endtabs %}

{% endif %}

{% if include.variable_name == "push notifications" %}

| Message type | Maximum message length | Maximum title length |
| --- | --- | --- |
| iOS lock screen | 175 characters | 43 characters |
| iOS notification | 175 characters | 43 characters |
| iOS banner alert | 85 characters | 43 characters |
| Android lock screen | 49 characters | 43 characters |
| Android notification drawer | 597 characters | 43 characters |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

The recommended image size for all push images is 500 KB.

<style>
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>Image type</th>
      <th>Aspect ratio</th>
      <th>Maximum pixels</th>
      <th>Maximum image size</th>
      <th>File types</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>iOS</td>
      <td>2:1 (recommended)</td>
      <td>1038 x 1038</td>
      <td>5 MB</td>
      <td>PNG, JPEG, GIF</td>
      <td>As of January 2020, iOS rich push notifications can handle images 1038 x 1038 px as long as they are under 10 MB, but we recommend using as small a file size as possible. In practice, sending large files can cause both unnecessary network stress and make download timeouts more common.<br><br>For more information, see <a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/">iOS rich notifications</a>.</td>
    </tr>
    <tr>
      <td>Android push icon</td>
      <td>1:1</td>
      <td>N/A</td>
      <td>500 KB</td>
      <td>PNG, JPEG</td>
      <td></td>
    </tr>
    <tr>
      <td>Android expanded notification image</td>
      <td>2:1</td>
      <td><b>Small:</b><br>512 x 256<br><br><b>Medium:</b><br>1024 x 512<br><br><b>Large:</b><br>2048 x 1024</td>
      <td>500 KB</td>
      <td>PNG, JPEG</td>
      <td>Used in <a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/">Android rich notifications</a>.</td>
    </tr>
    <tr>
      <td>Android incline image</td>
      <td>3:2</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>PNG, JPEG</td>
      <td>For more details, see <a href="{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/inline_image_push/">Android inline image push</a>.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4  .reset-td-br-5 .reset-td-br-6 role="presentation"}

{% endif %}

{% if include.variable_name == "email" %}

| Email type | Recommended maximum properties |
| --- | --- | 
| Text only | 25 KB |
| Text with images | 60 KB |
| Email width | 600 px |
{: .reset-td-br-1 .reset-td-br-2}

| Image specifications | Recommended maximum properties |
| --- | --- | 
| Size | 5 MB |
| Width | Header: 600 px<br>Body: 480 px |
| File types | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2}

| Text specifications | Recommended maximum properties |
| --- | --- | 
| Subject line length | 35 characters<br>6 to 10 words |
| `"From: Name"` length | 25 characters |
| Pre-header length | 85 characters |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "content cards" %}

| Card type | Aspect ratio     | Image quality       |
| --------- | ---------------- | ------------------- |
| Classic   | 1:1 aspect ratio | 60 x 60&nbsp;px        |
| Captioned | 4:3 aspect ratio | 600&nbsp;px minimum width |
| Banner    | Any aspect ratio | 600&nbsp;px minimum width |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

For more information, refer to [Content Card creative details]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/).

{% endif %}
