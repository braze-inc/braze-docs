---
nav_title: Importar su lista de correo electrónico
article_title: Importar su lista de correo electrónico a Braze
page_order: 4
page_type: reference
description: "Este artículo de referencia cubre las mejores prácticas para importar tu lista de correo electrónico a Braze."
channel: email

---

# Importar su lista de correo electrónico a Braze {#importing-email-lists}

> Un paso importante para convertirse en un remitente de correo electrónico de éxito es asegurarse de que dispone de una lista de correo electrónico de alta calidad. Una gestión adecuada de las listas de correo electrónico puede mejorar su capacidad de entrega y ofrecerle unos resultados de campaña más precisos y limpios.

## Consideraciones antes de importar

{% multi_lang_include email-via-sms-warning.md %}

### Valida tus listas de correo electrónico

Antes de importar su lista de correo electrónico a Braze, valide que su lista incluya sólo direcciones de correo electrónico auténticas. Una tasa de rebote elevada puede dañar su reputación como remitente de correo electrónico. 

Los servicios de limpieza de listas de correo electrónico pueden hacer esto por usted determinando si la dirección de correo electrónico sigue la sintaxis correcta y tiene las propiedades físicas de una dirección de correo electrónico, verificando el dominio de correo electrónico y conectándose al servidor de correo electrónico para autenticar si la dirección de correo electrónico existe allí.

### Identifique a sus usuarios comprometidos

Para identificar a tus usuarios más interactivos, elimina primero a los usuarios que hayan dejado de interactuar. Es una buena práctica no enviar correos electrónicos a usuarios que no hayan interactuado con un mensaje en más de seis meses, ya que esto puede dañar la reputación del remitente. Cuando importe su lista de correo electrónico, asegúrese de incluir sólo a usuarios que hayan abierto un correo suyo en los últimos seis meses.

A largo plazo, también deberías plantearte aplicar una [política de extinción]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/).

### Evitar las listas de supresión

Si está realizando la transición desde un proveedor de correo electrónico existente, asegúrese de no importar usuarios de una lista de supresión. Las listas de supresión presentan direcciones de correo electrónico que cancelaron la suscripción, marcaron tus correos como correo no deseado o arrojaron un rebote duro.

## Métodos de importación

Una vez que tenga su lista de correo electrónico preparada, hay varias formas de importar usuarios a Braze, como a través de la API REST de Braze o archivos CSV. Más información en nuestro artículo dedicado a [la importación de usuarios]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).

