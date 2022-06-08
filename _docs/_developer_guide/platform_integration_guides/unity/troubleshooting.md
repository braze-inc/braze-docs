---
nav_title: Troubleshooting
article_title: Troubleshooting for Unity
platform: 
  - Unity
  - iOS
  - Android
page_order: 29
description: "This reference article covers troubleshooting topics for the Unity platform."

---

# Troubleshooting

## File could not be read errors

Errors resembling the following may be safely ignored. Apple software uses a proprietary PNG extension called CgBI, which Unity does not recognize. These errors will affect neither your iOS build nor proper display of the associated images in the Braze bundle.

```
Could not create texture from Assets/Plugins/iOS/AppboyKit/Appboy.bundle/...png: File could not be read
```
