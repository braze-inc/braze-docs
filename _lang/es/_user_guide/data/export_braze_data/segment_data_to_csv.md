---
nav_title: Exportar datos de segmentos a CSV
article_title: Exportar datos de segmentos a CSV
page_order: 2
page_type: reference
description: "Este artículo de referencia explica cómo exportar datos de segmentos a CSV."

---

# Exportación de datos de segmentos a CSV

> Esta página explica cómo solicitar una exportación CSV de los datos de usuario de un segmento, y los datos incluidos en la exportación.

Para exportar los datos de un segmento a un CSV, selecciona el menú desplegable **Datos de usuario** mientras editas un segmento y elige exportar los datos de usuario o las direcciones de correo electrónico del segmento.

![Sección de detalles de segmento con menú desplegable de datos de usuario que muestra las opciones de exportación.]({% image_buster /assets/img_archive/csvexport.png %})

También puede solicitar una exportación CSV desde la página principal de **Segmentos** seleccionando el desplegable <i class="fas fa-gear"></i> **Settings** para un segmento:

![Desplegable de configuración en la página principal de Segmentos.]({% image_buster /assets/img_archive/csvexport2.png %})

{% alert tip %}
Para exportar los datos de todos sus perfiles de usuario, cree un segmento sin filtros y, a continuación, solicite una exportación CSV.
{% endalert %}

La salida CSV contiene los datos de cada perfil de usuario capturado en el segmento en el momento de la exportación. Puede exportar cualquier segmento seleccionando el icono del engranaje y Exportar CSV. Braze generará el informe en segundo plano y lo enviará por correo electrónico al usuario que esté conectado en ese momento.

{% alert important %}
Debido a las restricciones de tamaño de los archivos, la exportación puede fallar si el tamaño estimado de tu segmento es superior a 500 000 usuarios. Tenga en cuenta que esta restricción utiliza el tamaño estimado de su segmento, y no el cálculo exacto. Para más detalles, consulta [Exportar segmentos grandes]({{site.baseurl}}/help/help_articles/segments/exporting_large_segments/).
{% endalert %}

Si has vinculado tus [credenciales de Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration) a Braze, el CSV se cargará en tu contenedor de S3 con la clave `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip`. El enlace que se te envía por correo electrónico caducará al cabo de un día de la exportación, y requiere que hayas iniciado sesión en el panel para acceder a él.

## Datos incluidos en la exportación

Dependiendo de su selección, su exportación incluirá lo siguiente.

### Exportación de datos de usuario a CSV

| Nombre del campo                  | Descripción                                              |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | ID interno (no se puede cambiar)                           |
| country                     | País                                    |
| fecha_de_creación                  | Fecha y hora de creación del perfil de usuario                   |
| devices                     | Información sobre el dispositivo                           |
| fecha_de_nacimiento               | Fecha de nacimiento                                            |
| correo electrónico                       | Dirección de correo electrónico                                            |
| unsubscribed_from_emails_at | Fecha de cancelación de suscripción por correo electrónico                            |
| user_id                     | ID externo                                              |
| first_name                  | Nombre                                               |
| first_session               | Fecha y hora de la primera sesión                           |
| gender                      | Género                                                   |
| google_ad_ids               | ID de publicidad de Google asociados al usuario                      |
| ciudad                        | Localidad                                     |
| IDFAs                       | Valores del Identificador para Publicidad (IDFA)                 |
| IDFVs                       | Valores del identificador de proveedor (IDFV)                      |
| language                    | Idioma en la norma ISO-639-1                                        |
| última_versión_app_utilizada       | Última versión de la aplicación utilizada                             |
| last_name                   | Apellido                                                |
| last_session                | Fecha y hora de la última sesión                            |
| número_de_anuncios_de_google     | Recuento de ID de publicidad de Google asociados               |
| number_of_IDFAs             | Recuento de IDFA asociados                                |
| number_of_IDFVs             | Recuento de IDFV asociados                                |
| number_of_push_tokens       | Recuento de tokens de notificación push asociados             |
| número_de_roku_ad_ids       | Recuento de ID de publicidad de Roku asociados                 |
| number_of_windows_ad_ids    | Recuento de identificadores de publicidad de Windows asociados              |
| phone_number                | Número de teléfono                                             |
| opted_into_push_at          | Fecha de aceptación de las notificaciones push                       |
| unsubscribed_from_push_at   | Fecha de baja de las notificaciones push                |
| random_bucket               | Número de contenedor aleatorio                                 |
| roku_ad_ids                 | ID de publicidad de Roku                          |
| session_count               | Número total de sesiones                                 |
| zona horaria                    | Zona horaria del usuario en el mismo formato que la base de datos de zonas horarias de IANA                                         |
| in_app_purchase_total       | Importe total gastado en compras dentro de la aplicación                   |
| user_aliases                | Alias de usuario, en su caso                                          |
| windows_ad_ids              | ID de publicidad de Windows                       |
| Eventos personalizados               | Basado en la selección en la exportación                             |
| Atributos personalizados           | Basado en la selección en la exportación                             |
{: .reset-td-br-1 .reset-td-br-2 }

### Exportación de direcciones de correo electrónico a CSV

| Nombre del campo                  | Descripción            |
| --------------------------- | ---------------------- |
| user_id                     | ID externo del usuario     |
| first_name                  | Nombre             |
| last_name                   | Apellido              |
| correo electrónico                       | Correo electrónico                  |
| unsubscribed_from_emails_at | Fecha de cancelación de suscripción por correo electrónico |
| opted_in_to_emails_at       | Fecha de suscripción      |
| user_aliases                | Alias de usuario, en su caso   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visite nuestro artículo de [solución de problemas]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %} 

