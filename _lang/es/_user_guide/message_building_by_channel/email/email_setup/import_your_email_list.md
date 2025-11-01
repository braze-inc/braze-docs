---
nav_title: Importar tu lista de correo electrónico
article_title: Importar tu lista de correo electrónico a Braze
page_order: 4
page_type: reference
description: "Este artículo de referencia cubre las mejores prácticas para importar tu lista de correo electrónico a Braze."
channel: email

---

# Importar tu lista de correo electrónico a Braze {#importing-email-lists}

> Un paso importante para convertirte en un remitente de correo electrónico de éxito es asegurarte de que tienes una lista de correo electrónico de alta calidad. Una gestión adecuada de la lista de correo electrónico puede mejorar tu capacidad de entrega y ofrecerte unos resultados de campaña más precisos y limpios.

## Consideraciones antes de importar

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### Valida tus listas de correo electrónico

Antes de importar tu lista de correo electrónico a Braze, valida que tu lista sólo incluya direcciones de correo electrónico auténticas. Una tasa de rebote elevada puede dañar la reputación del remitente de tu correo electrónico. 

Los servicios de limpieza de listas de correo electrónico pueden hacerlo por ti determinando si la dirección de correo electrónico sigue la sintaxis correcta y tiene las propiedades físicas de una dirección de correo electrónico, verificando el dominio del correo electrónico y conectándose al servidor de correo electrónico para autenticar si la dirección de correo electrónico existe allí.

### Comprueba si una dirección de correo electrónico ya está asociada a un usuario

Antes de crear un usuario a través de la API o el SDK, llama al punto final [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) y especifica la dirección `email_address` del usuario. Si devuelve un perfil de usuario, ese usuario Braze ya está asociado a esa dirección de correo electrónico.

Te recomendamos encarecidamente que busques direcciones de correo electrónico únicas cuando se creen nuevos usuarios, y que evites pasar o importar usuarios con la misma dirección de correo electrónico. De lo contrario, puedes tener consecuencias no deseadas que afecten al envío de mensajes, la segmentación, los informes y otras características.

Por ejemplo, supongamos que tienes perfiles duplicados, pero determinados atributos o eventos personalizados residen sólo en un perfil. Cuando intentas desencadenar campañas o Lienzos con criterios múltiples, Braze no puede identificar al usuario como elegible porque hay dos perfiles de usuario. O, si una campaña se dirige a una dirección de correo electrónico compartida por dos usuarios, la página **Buscar usuarios** mostrará que ambos perfiles de usuario han recibido la campaña.

### Identifica a tus usuarios interactivos

Para identificar a tus usuarios más interactivos, elimina primero a los usuarios que hayan dejado de interactuar. Es una buena práctica no enviar correos electrónicos a usuarios que no hayan interactuado con un correo electrónico en más de seis meses, ya que esto puede dañar la reputación del remitente. Al importar tu lista de correo electrónico, asegúrate de incluir sólo a los usuarios que hayan abierto un correo electrónico tuyo en los últimos seis meses.

A largo plazo, también deberías plantearte aplicar una [política de extinción]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/).

### Evita las listas de supresión

Si estás cambiando de proveedor de correo electrónico, asegúrate de no importar usuarios de una lista de supresión. Las listas de supresión presentan direcciones de correo electrónico que se han dado de baja, han marcado tus correos como spam o han rebotado duramente.

## Métodos de importación

Una vez que tengas preparada tu lista de correo electrónico, hay varias formas de importar usuarios a Braze, como a través de la API REST de Braze o de archivos CSV. Lee más en nuestro artículo dedicado a la [importación de usuarios]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).

