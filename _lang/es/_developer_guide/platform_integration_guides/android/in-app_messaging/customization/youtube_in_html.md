---
nav_title: YouTube en HTML
article_title: Mensajes dentro de la aplicación de YouTube en HTML para Android y FireOS
platform: 
  - Android
  - FireOS
page_order: 8
description: "Este artículo de referencia explica cómo añadir videos de YouTube en mensajes HTML dentro de la aplicación para tu aplicación Android o FireOS."
channel:
  - in-app messages

---

# YouTube en HTML

> YouTube y otros contenidos HTML5 pueden reproducirse en mensajes HTML dentro de la aplicación. Esto requiere habilitar la aceleración por hardware en la actividad en la que se está mostrando el mensaje dentro de la aplicación; consulta la [guía del desarrollador de Android](https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling) para más detalles. La aceleración por hardware solo está disponible en las versiones 11 y posteriores de la API de Android.

A continuación se muestra un ejemplo de un video de YouTube incrustado en un fragmento de código HTML:

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

