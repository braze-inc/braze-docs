---
nav_title: Reorientación de usuarios
article_title: Reorientación de usuarios
page_order: 3
description: "Este artículo de referencia cubre cómo los usuarios pueden reorientar sus mensajes por las interacciones de WhatsApp de los usuarios."
page_type: reference
channel:
  - WhatsApp
---

# Reorientación de usuarios 

> Además de cambiar el estado de suscripción del usuario, Braze también registrará las interacciones con el perfil del usuario para filtrar y activar mensajes.<br><br>Estos filtros y activadores permiten filtrar los usuarios que han recibido mensajes de WhatsApp o que han recibido mensajes de WhatsApp de una campaña de WhatsApp o un paso de Canvas específicos.

## Opciones de reorientación

{% alert note %}
Al crear audiencias con retargeting de usuarios, es posible que desee incluir o excluir a determinados usuarios en función de sus preferencias, y con el fin de cumplir con las leyes de privacidad, como el derecho de "No vender ni compartir" en virtud de la CCPA. Los vendedores deben implementar los filtros pertinentes para la elegibilidad de los usuarios dentro de sus criterios de entrada de Canvas y/o Campaña.
{% endalert %}

### Filtrar usuarios por WhatsApp

Los usuarios pueden ser filtrados por cuándo recibieron un WhatsApp por última vez o si han recibido un WhatsApp de una campaña de WhatsApp específica. Los filtros pueden establecerse en el paso Usuarios objetivo del generador de campañas.

**Filtrar por último WhatsApp recibido**<br>
![Filtrar la última vez que se recibió un mensaje de WhatsApp el 22 de abril de 2025.]({% image_buster /assets/img/whatsapp/whatsapp23.png %}){: style="max-width:75%"}

**Filtrar por mensajes recibidos de la campaña de WhatsApp**<br>
Filtra los usuarios que han recibido un mensaje de una campaña específica de WhatsApp. Con este filtro, también tienes la opción de filtrar a aquellos que no han recibido mensajes de una campaña de WhatsApp.<br>
![Filtrar para recibir una campaña de WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp22.png %}){: style="max-width:75%"}

### Filtrar por compromiso
Vuelva a dirigirse a los usuarios que hayan leído o no una campaña de WhatsApp o un paso de Canvas. 

**Vuelve a dirigirte a los usuarios que hayan abierto/leído una campaña de WhatsApp específica**
1. Cree un segmento utilizando el filtro **Campaña clicada/abierta**.
2. Selecciona **leer mensaje de WhatsApp**.
3. Elija la campaña deseada.<br>

![Filtrar por haber leído un mensaje de WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp21.png %}){: style="max-width:75%"}

**Reorientar a los usuarios que han abierto/leído un Paso en Canvas específico**
1. Cree un segmento utilizando el filtro **Paso pulsado/abierto**.
2. Selecciona **leer mensaje de WhatsApp**.
3. Elija el lienzo y los pasos de lienzo deseados.<br>

![Filtrar para leer un paso de WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp20.png %}){: style="max-width:75%"}

**Filtrar por campaña o atribución Canvas**<br>
Filtro para usuarios que han abierto/leído una campaña de WhatsApp o un componente o etiqueta de Canvas específicos.

![Filtrar para abrir un mensaje concreto de WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp19.png %}){: style="max-width:75%"}

