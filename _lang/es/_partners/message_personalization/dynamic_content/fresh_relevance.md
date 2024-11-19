---
nav_title: Nueva relevancia
article_title: Nueva relevancia
description: "Este artículo de referencia describe la asociación entre Braze y Fresh Relevance, una versátil plataforma de personalización que le permite incluir productos relevantes en sus campañas y lienzos Braze."
alias: /partners/fresh_relevance/
page_type: partner
search_tag: Partner

---

# Nueva relevancia

> [Fresh Relevance][1] es una solución de personalización versátil que permite a las empresas orientadas al comercio crear experiencias personalizadas multicanal con facilidad. La plataforma te ahorra tiempo, se integra con tu pila tecnológica y te permite entregar experiencias del cliente personalizadas que aumentan la conversión en tu sitio web, aplicación, correos electrónicos, SMS y anuncios, sin depender de tu equipo de TI.

La integración de Braze y Fresh Relevance le permite:
* Envíe campañas de correo electrónico activadas avanzadas, como mensajes de bajada de precios, reposición de existencias, navegación en varias etapas o abandono de carritos.
* Incluya contenido personalizado en los mensajes de correo electrónico activados, como recomendaciones de productos basadas en el producto o los artículos de la misma categoría por los que ha navegado el cliente.
* Personalice las campañas de correo electrónico masivo con recomendaciones basadas en IA, tiempos de cuenta atrás, previsiones meteorológicas en tiempo real, feeds de redes sociales y mucho más.
* Haga crecer la base de datos de correo electrónico con nuevos contactos recopilados a través de ventanas emergentes de captura de datos.
* Identifique a los visitantes del sitio web que llegan desde un enlace de correo electrónico Braze.

## Requisitos previos

| Requisito | Descripción |
|-------------| ----------- |
| Cuenta Fresh Relevance  | Se necesita una cuenta de Fresh Relevance para beneficiarse de esta asociación. |
| Clave REST API de Braze | Una clave de API REST de Braze con permisos suficientes para los puntos finales que se indican a continuación. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | [La URL de tu punto final REST][3]. Tu punto final dependerá de la URL Braze de tu instancia. |
| ID de campaña Braze | La campaña Braze predeterminada que desea utilizar para enviar correos electrónicos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

Para configurar la integración en Fresh Relevance, debe crear un canal Braze en **Canales de mensajería** y utilizar el canal en los activadores o contenidos de Fresh Relevance adecuados, según sea necesario. 

Para obtener instrucciones paso a paso, inicie sesión en Fresh Relevance y siga su [documentación][2].

El sistema Fresh Relevance se comunicará con Braze utilizando la clave de API proporcionada. Una integración completa utiliza los siguientes puntos finales de la API de Braze:

* [`/users/alias/new`][4]
* [`/users/track`][5]
* [`/campaigns/triggers/send`][6]
* [`/users/export/ids`][7]
* [`/subscription/status/get`][8]
* [`/v2/subscription/status/set`][9]

[1]: https://www.freshrelevance.com/
[2]: https://admin.freshrelevance.com/help/esp_instructions/?esp_class_name=EspBraze
[3]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[4]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[5]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[6]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[7]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/