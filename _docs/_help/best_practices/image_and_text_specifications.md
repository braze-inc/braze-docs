---
nav_title: Image and Text Specifications
page_order: 7
---
# Image and Text Specifications

## Tips and Tricks for Rendering

For every and any channel you use to communicate with your users, here are some of Braze’s recommendations to help you ensure your images and text are rendered just right.

### General Tips

1. PNG files are recommended.

2. Smaller, high quality images will load faster, so it’s recommended to use the smallest asset possible to achieve your desired output.

3. A custom image library is required in order to display Gifs on Android. We recommend Glide.

### In-App Messages

#### Images

In general, Braze recommends using images that fit into a 16:10 screen.

| **Type** | **Aspect Ratio** | **Recommended Image Size** | **Max Image Size** | **File Types** |
| --- | --- | --- | --- | --- |
| Portrait Full Screen with Text | 6:5 | Hi-Res 1200 x 1000px<br>Min. 600 x 500px | 5MB | PNG, JPG, GIF |
| Portrait Full Screen (Image Only) | 3:5 | Hi-Res 1200 x 2000px <br>Min. 600 x 1000px | 5MB | PNG, JPG, GIF |
| Slideup | 1:1 | Hi-Res 150 x 150px<br>Min. 600 x 500px | 5MB | PNG, JPG, GIF |
| Modal (Image Only) | 1:1 | Hi-Res __Max__ 1200 x 2000px<br>Min. 600 x 600px | 5MB | PNG, JPG, GIF |
| Modal with Text | 29:10 | Hi-Res 1200 x 1000px<br>Min. 600 x 500px | 5MB | PNG, JPG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

#### Text

While there are no limits to how many characters of text you can include in an in-app message (as well as buttons, headline, main body, etc.) we recommend that you avoid too much text in in-app messages because they make can require users expand and scroll the message.

### Native Mobile Push Notifications

#### Images

**Image Type** | **Recommended Image Size** | **Max Image Size** | **File Types**
--- | --- | --- | ---
(iOS) 2:1 *Recommended* | 500KB | 5MB | PNG, JPG, GIF
(Android) Push Icon | 500KB | 5MB | PNG, JPG
(Android) Expanded Notification | 500KB | 5MB | PNG, JPG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

#### Text

**Message Type** | **Max Message Length**
--- | ---
(iOS) Lock Screen | 110 Characters
(iOS) Notification Center | 110 Characters
(iOS) Banner Alert | 63 Characters
(Android) Lock Screen | 49 Characters
(Android) Notification Drawer | 597 Characters
{: .reset-td-br-1 .reset-td-br-2}

#### Payload Size

**Platform** | **Size**
--- | ---
pre iOS 8 | 0.256 KB
post iOS 8 | 2 KB
Android (FCM) | 4 KB
{: .reset-td-br-1 .reset-td-br-2}

### Web Push Notifications

#### Images

| **Browser** | **Recommended Icon Size**
| --- | ---
Chrome | 192 x 192 ≥
Firefox | 192 x 192 ≥
Safari | Icons not configurable on a per-campaign basis
Opera | 192x192 ≥
{: .reset-td-br-1 .reset-td-br-2}

| **Browser** | **Platform** | **Large Image Size**
| --- | --- | ---
Chrome | macOS | N/A
Chrome | Android | 2 : 1 aspect ratio
Chrome | Windows | 360 ≥ x 240
Firefox | macOS| N/A
Safari | macOS | N/A
Opera | macOS | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Text

| **Browser** | **Platform** | **Maximum Title Length**  | **Maximum Message Body Length**
| --- | --- | --- | ---
Chrome | macOS | 28 | 27
Safari | macOS | 38 | 84
Firefox | macOS | 38 | 42
Opera | macOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### News Feed Specifications

#### Images

**Type** | **Aspect Ratio** | **Recommended Image Size** | **Max Image Size** | **File Types**
--- | --- | --- | --- | ---
Classic Card | 1:1 (110 pixels wide minimum) | 500KB | 1MB | PNG, JPG, GIF
Captioned Image Card | 4:3 (600 pixels wide minimum) | 500KB | 1MB | PNG, JPG, GIF
Banner Card | 6:1 (600 pixels wide mimimum) | 500KB | 1MB | PNG, JPG, GIF
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Email

#### Images

**Image Specifications** | **Recommended Properties**
--- | ---
Size | 5MB maximum
Width | (Header: 600 pixels maximum) (Body: 480 pixels maximum)
File Types | PNG, JPG, GIF
{: .reset-td-br-1 .reset-td-br-2}

#### Text

**Text Specifications** | **Recommended Properties**
--- | ---
Subject Line Length | 35 characters maximum (for optimal mobile display) (6 to 10 words)
Sender Name Length | 25 characters maximum (for optimal mobile display)
Pre-Header Length | 85 characters maximum
{: .reset-td-br-1 .reset-td-br-2}

#### Size

**Email Type** | **Recommendations**
--- | ---
Text Only | 25KB maximum
Text With Images | 60KB maximum
Email Width | 600 pixels maximum
{: .reset-td-br-1 .reset-td-br-2}
