---
nav_title: YouTube in HTML
article_title: YouTube in HTML-In-App-Nachrichten für Android und FireOS
platform: 
  - Android
  - FireOS
page_order: 8
description: "Dieser Referenzartikel beschreibt, wie Sie YouTube-Videos in HTML-In-App-Nachrichten für Ihre Android- oder FireOS-Anwendung einfügen."
channel:
  - in-app messages

---

# YouTube in HTML

> YouTube und andere HTML5-Inhalte können in HTML-In-App-Nachrichten abgespielt werden. Dazu muss die Hardware-Beschleunigung in der Aktivität, in der die In-App-Nachricht angezeigt wird, aktiviert sein. Weitere Informationen finden Sie im [Android-Entwicklerhandbuch](https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling). Die Hardware-Beschleunigung ist nur für Android-APIs ab Version 11 verfügbar.

Im Folgenden sehen Sie ein Beispiel für ein eingebettetes YouTube-Video in einem HTML-Snippet:

```html
<body>
    <div class="box">
        <div class="relativeTopRight">
            <a href="appboy://close">X</a>
        </div>
        <iframe width="60%" height="50%" src="https://www.youtube.com/embed/_x45EB3BWqI">
        </iframe>
    </div>
</body>
```

