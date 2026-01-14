---
nav_title: Exportar datos de segmentos a CSV
article_title: Exportar datos de segmento a CSV
page_order: 2
page_type: reference
description: "Este artículo de referencia explica cómo exportar datos de segmentos a CSV."

---

# Exportar datos de segmentos a CSV

> Esta página explica cómo solicitar una exportación CSV de los datos de usuario de un segmento, y los datos incluidos en la exportación.

Para exportar los datos de un segmento a un CSV, selecciona el menú desplegable **Datos de usuario** mientras editas un segmento y elige exportar los datos de usuario o las direcciones de correo electrónico del segmento.

\![Sección de detalles de segmento con menú desplegable de datos de usuario que muestra las opciones de exportación.]({% image_buster /assets/img_archive/csvexport.png %})

También puedes solicitar una exportación CSV desde la página principal de **Segmentos** seleccionando el desplegable <i class="fas fa-gear"></i> **Configuración** de un segmento:

\![Desplegable de configuración en la página principal de Segmentos.]({% image_buster /assets/img_archive/csvexport2.png %})

{% alert tip %}
Para exportar datos de todos tus perfiles de usuario, crea un segmento sin filtros y, a continuación, solicita una exportación CSV.
{% endalert %}

La salida CSV contiene los datos de cada perfil de usuario capturado en el segmento en el momento de la exportación. Puedes exportar cualquier segmento seleccionando el ícono de engranaje y la exportación CSV. Braze generará el informe en segundo plano y lo enviará por correo electrónico al usuario que esté conectado en ese momento.

{% alert important %}
Debido a las restricciones de tamaño de los archivos, tu exportación puede fallar si el tamaño estimado de tu segmento es superior a 500.000 usuarios. Ten en cuenta que esta restricción utiliza el tamaño estimado de tu segmento, y no el cálculo exacto. Para más detalles, consulta [Exportar segmentos grandes](#exporting-large-segments).
{% endalert %}

Si has vinculado tus [credenciales de Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration) a Braze, el CSV se cargará en tu contenedor de S3 con la clave `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip`. Debes haber iniciado sesión en el panel para acceder al enlace de descarga que se te ha enviado por correo electrónico.

{% multi_lang_include alerts/important_alerts.md alert='S3 file bucket export' %}

## Datos incluidos en la exportación

En función de tu selección, se incluye lo siguiente en tu exportación.

### Exportar datos de usuario CSV

| Nombre del campo                  | Descripción                                              |
| --------------------------- | -------------------------------------------------------- |
| ID de Appboy                   | ID interno (no se puede cambiar)                           |
| país                     | País                                    |
| created_at                  | Fecha y hora de creación del perfil de usuario                   |
| dispositivos                     | Información del dispositivo                           |
| date_of_birth               | Fecha de nacimiento                                            |
| correo electrónico                       | Dirección de correo electrónico                                            |
| unsubscribed_from_emails_at | Fecha de cancelación de suscripción a los envíos electrónicos                            |
| user_id                     | ID externo                                              |
| first_name                  | Nombre                                               |
| first_session               | Fecha y hora de la primera sesión                           |
| género                      | Género                                                   |
| google_ad_ids               | ID de publicidad de Google asociados al usuario                      |
| ciudad                        | Ciudad                                     |
| IDFAs                       | Identificador de valores publicitarios (IDFA)                 |
| IDFVs                       | Identificador de los valores del Vendedor (IDFV)                      |
| idioma                    | Lengua en la norma ISO-639-1                                        |
| last_app_version_used       | Última versión de la aplicación utilizada                             |
| last_name                   | Apellidos                                                |
| last_session                | Fecha y hora de la última sesión                            |
| number_of_google_ad_ids     | Recuento de ID de publicidad de Google asociados               |
| number_of_IDFAs             | Recuento de IDFA asociados                                |
| number_of_IDFVs             | Recuento de IDFV asociadas                                |
| number_of_push_tokens       | Recuento de tokens de notificaciones push asociados             |
| number_of_roku_ad_ids       | Recuento de ID de publicidad Roku asociados                 |
| number_of_windows_ad_ids    | Recuento de ID de publicidad de Windows asociados              |
| phone_number                | Número de teléfono                                             |
| opted_into_push_at          | Fecha de adhesión a las notificaciones push                       |
| unsubscribed_from_push_at   | Fecha de baja de las notificaciones push                |
| random_bucket               | Número de contenedor aleatorio                                 |
| roku_ad_ids                 | ID de publicidad de Roku                          |
| session_count               | Número total de sesiones                                 |
| zona horaria                    | Huso horario del usuario en el mismo formato que la base de datos de husos horarios de IANA                                         |
| in_app_purchase_total       | Importe total gastado en compras dentro de la aplicación                   |
| user_aliases                | Alias de usuario, si los hay                                          |
| windows_ad_ids              | ID de publicidad de Windows                       |
| Eventos personalizados               | Según la selección en la exportación                             |
| Atributos personalizados           | Según la selección en la exportación                             |
{: .reset-td-br-1 .reset-td-br-2 }

### Exportar direcciones de correo electrónico CSV

| Nombre del campo                  | Descripción            |
| --------------------------- | ---------------------- |
| user_id                     | ID externo del usuario     |
| first_name                  | Nombre             |
| last_name                   | Apellidos              |
| correo electrónico                       | Correo electrónico                  |
| unsubscribed_from_emails_at | Fecha de cancelar suscripción por correo electrónico |
| opted_in_to_emails_at       | Fecha de adhesión voluntaria por correo electrónico      |
| user_aliases                | Alias de usuario, si los hay   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita nuestro artículo de [solución de problemas]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %} 

## Exportación de grandes segmentos

Existen varios métodos para exportar un gran segmento de usuarios que contenga más de 500.000 usuarios.

{% tabs %}
{% tab Multiple segments %}

Puedes dividir un segmento grande en segmentos más pequeños y luego exportar cada uno de los segmentos más pequeños desde Braze. 

{% endtab %}
{% tab Random bucket numbers %}

También puedes utilizar [números de contenedor aleatorios]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) para dividir tu base de usuarios en varios segmentos, y combinarlos después de la exportación. Por ejemplo, si necesitas dividir tu segmento en dos segmentos diferentes, puedes hacerlo con los siguientes filtros:
- Segmento 1: El número de contenedor aleatorio es inferior a 5000 (incluye 0-4999)
- Segmento 2: El número de contenedor aleatorio es superior a 4999 (incluye 5000-9999)

{% endtab %}
{% tab Endpoints %}

También puedes aprovechar los siguientes puntos finales para exportar datos de usuario de un segmento específico. Ten en cuenta que estos puntos finales están sujetos a límites de datos.
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)

{% endtab %}
{% endtabs %}
