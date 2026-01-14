---
nav_title: Reorientar al usuario
article_title: Reorientación de usuarios
page_order: 4
description: "Este artículo de referencia explica cómo los usuarios pueden reorientar sus mensajes mediante las interacciones de WhatsApp."
page_type: reference
channel:
  - WhatsApp
---

# Reorientar al usuario 

> Además de cambiar el estado de suscripción del usuario, Braze también registrará las interacciones con el perfil de usuario para filtrar y desencadenar mensajes.<br><br>Estos filtros y desencadenantes te permiten filtrar los usuarios que han recibido mensajes de WhatsApp o que han recibido mensajes de WhatsApp de una campaña de WhatsApp o paso en Canvas concretos.

## Opciones de reorientación

{% alert note %}
Al crear audiencias con reorientación de usuarios, puede que desees incluir o excluir a determinados usuarios en función de sus preferencias, y para cumplir las leyes de privacidad, como el derecho de "No vender ni compartir" según la CCPA. Los especialistas en marketing deben aplicar los filtros pertinentes para la elegibilidad de los usuarios dentro de los criterios de entrada de su Canvas y/o campaña.
{% endalert %}

### Filtrar usuarios por WhatsApp

Los usuarios pueden ser filtrados por cuándo recibieron un WhatsApp por última vez o si han recibido un WhatsApp de una campaña de WhatsApp específica. Los filtros se pueden establecer en el paso Usuarios objetivo del constructor de campañas.

**Filtrar por último WhatsApp recibido**<br>
Filtrar la última vez que se recibió un mensaje de WhatsApp el 22 de abril de 2025.]({% image_buster /assets/img/whatsapp/whatsapp23.png %}){: style="max-width:75%"}

**Filtrar por mensajes recibidos de la campaña de WhatsApp**<br>
Filtra los usuarios que han recibido un mensaje de una campaña específica de WhatsApp. Con este filtro, también tienes la opción de filtrar a los que no han recibido mensajes de una campaña de WhatsApp.<br>
Filtrar para recibir una campaña de WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp22.png %}){: style="max-width:75%"}

### Filtrar por interacción
Reorienta a los usuarios que hayan leído o no una campaña de WhatsApp o un paso en Canvas. 

**Reorientar a los usuarios que han abierto/leído una campaña específica de WhatsApp**
1. Crea un segmento utilizando el filtro **Campaña clicada/abierta**.
2. Selecciona **leer mensaje de WhatsApp**.
3. Elige la campaña deseada.<br>

Filtrar por haber leído un mensaje de WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp21.png %}){: style="max-width:75%"}

**Reorientar a los usuarios que han abierto/leído un Paso en Canvas específico**
1. Crea un segmento utilizando el filtro **Paso hecho clic/Abierto**.
2. Selecciona **leer mensaje de WhatsApp**.
3. Elige el Canvas y los pasos en Canvas deseados.<br>

Filtrar para leer un paso de WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp20.png %}){: style="max-width:75%"}

**Filtrar por atributo de campaña o Canvas**<br>
Filtrar a los usuarios que han abierto/leído una campaña de WhatsApp o un componente o etiqueta de Canvas específicos.

Filtrar para abrir un mensaje de WhatsApp concreto.]({% image_buster /assets/img/whatsapp/whatsapp19.png %}){: style="max-width:75%"}

