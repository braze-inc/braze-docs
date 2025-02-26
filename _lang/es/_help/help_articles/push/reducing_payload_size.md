---
nav_title: Reducir el tamaño de la carga útil de las notificaciones push
article_title: Reducir el tamaño de la carga útil de las notificaciones push
page_type: solution
description: "Este artículo de ayuda proporciona algunos consejos para reducir el tamaño de la carga útil de tus notificaciones push si no puedes lanzar una campaña o un paso en Canvas debido a los límites de tamaño de la carga útil push."
channel: push
---

# Reducir el tamaño de la carga útil de las notificaciones push

Si no puedes lanzar una campaña push o un paso en Canvas porque tu carga útil push es demasiado grande, consulta estos consejos para reducir el tamaño de tu carga útil de notificación push.

{% alert note %}
El tamaño máximo de nuestra carga útil es de **3.807 bytes**. Si tu push supera este tamaño, es posible que el mensaje no se envíe. Como práctica recomendada, mantén tu carga útil en unos pocos cientos de bytes.
{% endalert %}

## ¿Qué es una carga útil push?

Los proveedores de servicios push calculan si tu notificación push puede mostrarse a un usuario teniendo en cuenta el tamaño en bytes de toda la carga útil push. La carga útil está limitada a **4 KB (4096 bytes)** para la mayoría de los servicios push, incluidos los siguientes:

- servicio de notificaciones push de Apple (APN)
- Mensajería en la nube Firebase de Android (FCM)
- Notificación push web
- Huawei push

Estos servicios push rechazarán cualquier notificación que supere este límite.

Braze reserva una parte de la carga útil push para fines de integración y análisis. Por tanto, el tamaño máximo de nuestra carga útil es de **3807 bytes**. Si tu push supera este tamaño, es posible que el mensaje no se envíe. Como práctica recomendada, mantén tu carga útil en unos pocos cientos de bytes.

Los siguientes elementos de tu push constituyen la carga útil de tu push:

- Copia, como el título y el cuerpo del mensaje
- Render final de cualquier personalización Liquid
- URL de las imágenes (pero no el tamaño de la propia imagen)
- URL para objetivos de clic
- Nombres de los botones
- Pares clave-valor

## Consejos para reducir el tamaño de la carga útil

Para reducir el tamaño de la carga útil:

- Haz que tu mensaje sea breve. Una buena pauta general es hacerlo procesable y beneficioso en menos de 40 caracteres.
- Omite los espacios en blanco y los saltos de línea en tu copia.
- Ten en cuenta cómo se representará Liquid en el envío. Dado que la representación final de cualquier personalización de Liquid variará de un usuario a otro, Braze no puede determinar si una carga útil push superará el límite de tamaño cuando se incluya Liquid. Si tu Liquid muestra un mensaje más corto, puede que te vaya bien. Sin embargo, si tu Liquid da lugar a un mensaje más largo, tu push puede superar el límite de tamaño de la carga útil. Prueba siempre tu mensaje push en un dispositivo real antes de enviarlo a los usuarios.
- Considera la posibilidad de acortar las URL utilizando un acortador de URL.
