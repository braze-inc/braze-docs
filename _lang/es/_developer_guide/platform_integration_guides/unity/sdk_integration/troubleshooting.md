---
nav_title: Solución de problemas
article_title: Solución de problemas para Unity
platform: 
  - Unity
  - iOS
  - Android
page_order: 3
description: "En este artículo de referencia se cubren temas de solución de problemas para la plataforma Unity."

---

# Solución de problemas

> Este artículo proporciona varios escenarios de solución de problemas de Unity.

## Errores de "No se pudo leer el archivo"

Los errores parecidos a los siguientes pueden ignorarse con seguridad. El software de Apple utiliza una extensión PNG propietaria llamada CgBI, que Unity no reconoce. Estos errores no afectarán a tu compilación de iOS ni a la correcta visualización de las imágenes asociadas en el paquete Braze.

```
Could not create texture from Assets/Plugins/iOS/AppboyKit/Appboy.bundle/...png: File could not be read
```
