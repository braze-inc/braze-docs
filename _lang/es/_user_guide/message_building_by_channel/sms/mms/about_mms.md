---
nav_title: "Acerca de MMS"
article_title: Acerca de MMS
page_order: 0
description: "Este artículo de referencia explica qué son los mensajes MMS y los casos generales de uso del canal MMS."
page_type: reference
channel:
  - MMS
search_rank: 2  
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}Sobre mensajes MMS

> El MMS, también conocido como servicio de mensajes multimedia, se utiliza para enviar mensajes que contienen activos multimedia (JPEG, GIF, PNG) a teléfonos móviles.<br><br>Al igual que el SMS, el MMS es un canal de mensajería de alta urgencia que le permite comunicarse con los clientes de forma inmediata de una manera que no puede con ningún otro canal. Sin embargo, los MMS amplían las posibilidades de los SMS, ya que permiten añadir contenido multimedia a mensajes que, de otro modo, serían sólo de texto.

## Posibles casos de uso

| Caso de uso | Explicación |
| --- | --- |
| Promociones | Llega a los usuarios con campañas de SMS de gran visibilidad, pero aprovecha también el aspecto mediático de los MMS para atraer a los compradores con lo que ofreces. | 
| Campañas de reactivación de la interacción | Vuelva a captar a los clientes que optaron por recibir SMS cuando todos los demás canales no consigan atraerlos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Conoce el MMS

### Disponibilidad de MMS

La mayoría de las operadoras estadounidenses y canadienses admiten la recepción y visualización de contenidos multimedia en los teléfonos de sus clientes. En el caso de las operadoras internacionales, Braze convertirá automáticamente los mensajes MMS enviados desde un número de teléfono compatible con EE.UU. o Canadá, y sólo a destinos que no admitan MMS. Para estos mensajes, Braze sustituirá los medios adjuntos por una URL corta añadida al cuerpo del mensaje que enlaza con el archivo.

### Grupos de suscripción

Un [grupo de suscripción][1] es una colección de números de teléfono de envío (códigos cortos, códigos largos e ID alfanuméricos de remitente) que se utilizan para un tipo específico de mensajería. Tu grupo de suscripción requiere un número de teléfono habilitado para MMS. Habla con tu director de cuentas Braze para habilitar esta característica.

### Límites y rendimiento de los mensajes MMS

Para MMS, el límite de mensajes es de 1 MB (esto incluye el activo multimedia y el tamaño del cuerpo del mensaje). Para estar más seguro, Braze recomienda no superar los 600 KB para tu activo multimedia, incluyendo también el cuerpo del mensaje.

El caudal de MMS es de un segmento por segundo a través de un código largo.

### MMS entrantes

Cuando un usuario envíe un mensaje entrante que contenga un elemento multimedia, Braze expondrá la URL del elemento multimedia en Currents y en Liquid a través de la etiqueta Liquid {%raw%}`{{sms.${inbound_media_url}}}`{%endraw%}

### Tipos de archivo aceptados

Braze acepta archivos JPEG, GIF, PNG y VCF y te permite adjuntar un único activo multimedia a tu mensaje MMS.


[picture]: {% image_buster /assets/img/sms/MMS.png %}
[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement
