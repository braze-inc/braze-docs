---
nav_title: Sonidos personalizados
article_title: Sonidos de notificación push personalizados para iOS
platform: Swift
page_order: 3
description: "En este artículo se trata la implementación de sonidos personalizados de iOS en el SDK Swift."
channel:
  - push

---

# Sonidos personalizados

## Paso 1: Alojar el sonido en la aplicación

Los sonidos de notificación push personalizados deben alojarse localmente dentro del paquete principal de tu aplicación. Se aceptan los siguientes formatos de datos de audio:

- PCM lineal
- MA4
- µLaw
- aLaw

Puedes empaquetar los datos de audio en un archivo AIFF, WAV o CAF. En Xcode, añade el archivo de sonido a tu proyecto como un recurso no localizado del paquete de la aplicación.

{% alert note %}
Los sonidos personalizados deben durar menos de 30 segundos cuando se reproducen. Si un sonido personalizado supera ese límite, en su lugar, se reproduce el sonido predeterminado del sistema.
{% endalert %}

### Convertir archivos de sonido

Puedes utilizar la herramienta afconvert para convertir sonidos. Por ejemplo, para convertir el sonido del sistema PCM lineal de 16 bits Submarine.aiff a audio IMA4 en un archivo CAF, utiliza el siguiente comando en el terminal:

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

{% alert tip %}
Puedes inspeccionar un sonido para determinar su formato de datos abriéndolo en QuickTime Player y eligiendo **Mostrar inspector de películas** en el menú **Película**.
{% endalert %}

## Paso 2: Proporcionar una URL de protocolo para el sonido

Debes especificar una URL de protocolo que dirija a la ubicación del archivo de sonido en tu aplicación. Hay dos métodos para hacerlo:

* Utiliza el parámetro `sound` del [objeto push de Apple]({{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-object) para pasar la URL a Braze.
* Especifica la URL en el panel. En [el compositor push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#step-3-select-notification-type-ios-and-android), selecciona **Configuración** e introduce la URL del protocolo en el campo **Sonido**. 

![El compositor push en el panel de Braze]({% image_buster /assets/img_archive/sound_push_ios.png %})

Si el archivo de sonido especificado no existe o se introduce la palabra clave "predeterminado", Braze utilizará el sonido de alerta del dispositivo predeterminado. Aparte de nuestro panel, el sonido también se puede configurar a través de nuestra [API de mensajería][12].

Consulta la documentación para desarrolladores de Apple relativa a la [preparación de sonidos de alerta personalizados](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html) para obtener información adicional.

