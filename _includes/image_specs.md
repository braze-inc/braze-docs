{% if include.variable_name == "payload size" %}

Smaller, high quality images will load faster, so we recommend using the smallest asset possible to achieve your desired output. We recommend the following payload sizes:

| Messaging system | Recommended payload |
| --- | --- |
| iOS (pre-iOS 8) | 0.256 KB |
| iOS (post-iOS 8) | 2 KB |
| Android (GCM) | 2 KB |
| Android (FCM) | 4 KB |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "in-app messages" %}

In general, we recommend using images that fit into a 16:10 screen.

While there are no limits to how many text characters you can include in an in-app message (as well as buttons, headline, main body, and others), we moderating how many text characters you use. Too much text will require users to expand and scroll the message.

| Type | Aspect ratio | Recommended image size | Max image size | File types |
| --- | --- | --- | --- | --- |
| Portrait full screen with text | 5:4 | 500 KB | 5 MB | PNG, JPG, GIF |
| Portrait full screen (image only) | 10:16 | 500 KB | 5 MB | PNG, JPG, GIF |
| Landscape full screen with text | 16:5 | 500 KB | 5 MB | PNG, JPG, GIF |
| Landscape full screen (image only) | 16:10 | 500 KB | 5 MB | PNG, JPG, GIF |
| Slideup | 1:1 | 500 KB | 5 MB | PNG, JPG, GIF |
| Modal (image only) | 1:1 | 500 KB | 5 MB | PNG, JPG, GIF |
| Modal with text | 29:10 | 500 KB | 5 MB | PNG, JPG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5}

{% endif %}

{% if include.variable_name == "push notifications" %}

| Message type | Max message length | Max title length |
| --- | --- | --- |
| iOS lock screen | 175 characters | 43 characters |
| iOS notification | 175 characters | 43 characters |
| iOS banner alert | 85 characters | 43 characters |
| Android lock screen | 49 characters | 43 characters |
| Android notification drawer | 597 characters | 43 characters |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

| Image type | Recommended image size | Max image size | File types |
| --- | --- | --- | --- |
| iOS 2:1 (recommended) | 500 KB | 5 MB | PNG, JPG, GIF |
| Android push icon | 500 KB | 500 KB | PNG, JPG |
| Android expanded notification | 500 KB | 500 KB | PNG, JPG |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

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
| File types | PNG, JPG, GIF |
{: .reset-td-br-1 .reset-td-br-2}

| Text specifications | Recommended maximum properties |
| --- | --- | 
| Subject line length | 35 characters<br>6 to 10 words |
| `"From: Name"` length | 25 characters |
| Pre-header length | 85 characters |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}