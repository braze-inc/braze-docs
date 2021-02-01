---
nav_title: Message Format
page_order: 5
---
# Message Format

## iOS

- Message Length:
  - iOS Lock Screen: 110 Characters
  - iOS Notification Center: 110 Characters
  - iOS Banner Alert: 62 Characters
  - iOS Pop Up Alert: 235 Characters
- Payload Size:
  - iOS: 2KB
- Number of Lines:
  - iOS Lock Screen: 4 Lines
  - iOS Notification Center: 4 Lines
  - iOS Banner Alert: 2 Lines
  - iOS Pop Up Alert: 8 Lines
- Customizable UI: No
- Deep Link Capable: Yes

### iOS Image Sizes

|    Aspect Ratio   | Recommended Image Size | Maximum Image Size |   File Types  |
|:-----------------:|:----------------------:|:------------------:|:-------------:|
| 2:1 (recommended) |          500KB         |         5MB        | PNG, JPG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### iOS Example

![iOS_Push][42]

### iOS Large Image Format Example

![iOS Rich Push][54]

![iOS Rich Push On Hard Push][55]

## Android
- Message Length:
  - Lock Screen: 1 line (estimated 49 characters max)
  - Notification Drawer: 1 line, up to 8 lines when expanded (estimated 597 characters max)
- Payload Size:
  - FCM: 4KB
- Customizable UI: Yes
- Deep Link Capable: Yes

### Android Image Sizes

|             Type            |         Aspect Ratio         | Recommended Image Size |                         Maximum Image Size                         | File Types |
|:---------------------------:|:----------------------------:|:----------------------:|:------------------------------------------------------------------:|:----------:|
|          Push Icon          | 1:1 (400x400 pixels minimum) |          500KB         | N/A - however a balance should be  struck between quality and size |  PNG, JPG  |
| Expanded Notification Image | 2:1 (600x300 pixels minimum) |          500KB         | N/A - however a balance should be  struck between quality and size |  PNG, JPG  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

- Smaller, high quality images will load faster, so it’s recommended to use the smallest asset possible to achieve your desired output.

### Android Example

![Android_Push][43]

### Large Image Format Example

![Large Android Image][27]

- Large image notifications display best when using an image of at least 600x300 pixels

## Windows Universal
- Message Length: Depends on Device
- Payload Size: 3 kilobytes
- Number of lines: 1-3 Lines
- Customizable UI: No
- Deep Link Capable: No

### Windows Universal Example

![Push_Window_Universal][46]

## Windows Phone 8
- Message Length: Varies. If only title is set, about 40 characters can be displayed. If only content is set, about 47 characters can be displayed. If title and content is set, then about 41 characters can be displayed.
- Payload Size: 5 kilobytes
- Number of lines: 1
- Customizable UI: No
- Deep Link Capable: No

### Windows Phone 8 Example

![Push_Window8][47]

[27]: {% image_buster /assets/img_archive/android_push_img2.png %}
[42]: {% image_buster /assets/img_archive/iOS_push_notification_small.png %}
[43]: {% image_buster /assets/img_archive/Push_Android_2.png %}
[46]:{% image_buster /assets/img_archive/Push_Window8_Toast.png %}
[47]:{% image_buster /assets/img_archive/Push_Windows_Universal_Toast.png %}
[54]: {% image_buster /assets/img_archive/braze_richpush1.png %}
[55]: {% image_buster /assets/img_archive/braze_richpush2.png %}
