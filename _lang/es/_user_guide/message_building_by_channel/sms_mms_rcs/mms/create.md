---
nav_title: Creación de una campaña MMS
article_title: Creación de una campaña MMS
page_order: 2
description: "Este artículo de referencia cubre los pasos necesarios para crear, enviar y obtener una vista previa de un mensaje MMS."
page_type: reference
alias: /create_mms_message/
tool:
  - Campaigns
channel:
  - MMS
search_rank: 1  
---

# Crear una campaña MMS

> Este artículo contiene información específica sobre la composición MMS, que forma parte del compositor de SMS. Para obtener información más detallada sobre el compositor de SMS/MMS, consulta [Compositor de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/create/).

## Conceptos básicos del envío de MMS

### Seleccione su grupo de suscripción

Debe designar un grupo de suscripción con números de teléfono habilitados para MMS a los que dirigirse (pueden ser códigos cortos o largos).

### Cuerpo del mensaje de entrada

Introduce tipos de imagen PNG, JPEG, GIF y VCF desde la biblioteca multimedia o especifica una URL. Sólo se admite una imagen.

### Comprender el envío de MMS

Los MMS se facturan a una tasa diferente que los SMS de sólo texto, y no todos los operadores aceptan MMS. En estos casos, Twilio convertirá automáticamente el MMS en un enlace de imagen en el que el usuario podrá hacer clic.

### Utiliza tarjetas de contacto

Las tarjetas de contacto (a veces conocidas como vCard o Archivos Virtuales de Contacto (vcf)) son un formato de archivo estandarizado para enviar información empresarial y de contacto que puede importarse fácilmente a libretas de direcciones o de contactos. Estas tarjetas pueden crearse [mediante programación](https://www.twilio.com/blog/send-vcard-twilio-sms) y cargarse en la biblioteca multimedia de Braze o crearse a través de nuestro [generador de tarjetas de contacto]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/) integrado.

## Crear un mensaje MMS

La creación de un mensaje MMS requiere que su grupo de suscripción esté configurado para el envío de MMS. Esto se indica viendo la etiqueta MMS al seleccionar un grupo de suscripción. Al seleccionar un grupo de suscripción habilitado para MMS, tendrás la posibilidad de subir una imagen, hacer referencia a una URL de imagen o incluir una tarjeta de contacto.

![La pestaña "Redactar" para escribir tu mensaje.]({% image_buster /assets/img/sms/mms_composer.png %}){: style="max-width:80%;"}

### Especificaciones de imagen

| **Especificaciones de imagen** | **Propiedades recomendadas** |
|--------------------------|----------------------------|
| Tamaño                     | Hasta 600 KB        |
| Tipos de archivo               | PNG, JPEG, GIF             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Vista previa de un mensaje MMS

Braze proporciona una vista previa de la imagen que has cargado en el panel **Vista previa** del compositor de mensajes. 

{% alert note %}
El orden de los activos SMS o MMS no se puede personalizar. El pedido depende del teléfono que recibe este mensaje.
{% endalert %}

![Un ejemplo de mensaje "¿Listo para llegar a casa gym...at?". La vista previa muestra el mensaje y la imagen enviados como textos.]({% image_buster /assets/img/sms/mms_preview.png %})
