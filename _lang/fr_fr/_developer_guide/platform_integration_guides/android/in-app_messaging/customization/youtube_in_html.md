---
nav_title: YouTube en HTML
article_title: YouTube dans les messages in-app HTML pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 8
description: "Cet article de référence explique comment ajouter des vidéos YouTube dans des messages in-app HTML pour votre application Android ou FireOS."
channel:
  - in-app messages

---

# YouTube en HTML

> YouTube et d’autres contenus HTML5 peuvent être joués dans des messages in-app HTML. Cela nécessite que l’accélération matérielle soit activée dans l’activité où le message in-app est affiché. Consultez le [guide du développeur Android](https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling) pour plus de détails. L’accélération matérielle est uniquement disponible sur les versions 11 et ultérieures des API Android.

Voici un exemple de vidéo YouTube intégrée dans un extrait de code HTML :

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

