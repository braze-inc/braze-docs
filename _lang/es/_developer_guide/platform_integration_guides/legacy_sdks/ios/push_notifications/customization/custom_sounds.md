---
nav_title: Sonidos personalizados
article_title: Sonidos de notificación push personalizados para iOS
platform: iOS
page_order: 3
description: "Este artículo de referencia cubre la implementación de sonidos personalizados en tus notificaciones push de iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Sonidos personalizados

## Paso 1: Alojar el sonido en la aplicación

Los sonidos de notificación push personalizados deben alojarse localmente dentro del paquete principal de la aplicación cliente. Se aceptan los siguientes formatos de datos de audio:

- PCM lineal
- MA4
- µLaw
- aLaw

Puedes empaquetar los datos de audio en un archivo AIFF, WAV o CAF. En Xcode, añade el archivo de sonido a tu proyecto como un recurso no localizado del paquete de la aplicación.

Puedes utilizar la herramienta afconvert para convertir sonidos. Por ejemplo, para convertir el sonido del sistema PCM lineal de 16 bits Submarine.aiff a audio IMA4 en un archivo CAF, utiliza el siguiente comando en el terminal:

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

Puedes inspeccionar un sonido para determinar su formato de datos abriéndolo en QuickTime Player y eligiendo **Mostrar inspector de películas** en el menú **Película**.

Los sonidos personalizados deben durar menos de 30 segundos cuando se reproducen. Si un sonido personalizado supera ese límite, en su lugar, se reproduce el sonido predeterminado del sistema.

## Paso 2: Proporcionar al panel una URL de protocolo para el sonido

Tu sonido debe alojarse localmente dentro de la aplicación. Debes especificar una URL de protocolo que dirija a la ubicación del archivo de sonido en la aplicación dentro del campo **Sonido** en el compositor push. Si especificas "predeterminado" en este campo, se reproducirá el sonido de notificación predeterminado en el dispositivo. Esto se puede especificar a través de nuestra [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/) o de nuestro panel en **Configuración** en el compositor push, como se muestra en la siguiente captura de pantalla:

![]({% image_buster /assets/img_archive/sound_push_ios.png %})

Si el archivo de sonido especificado no existe o se introduce la palabra clave "predeterminado", Braze utilizará el sonido de alerta del dispositivo predeterminado. Aparte de nuestro panel, el sonido también se puede configurar a través de nuestra [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/). Consulta la documentación para desarrolladores de Apple relativa a la [preparación de sonidos de alerta personalizados](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html) para obtener información adicional.

