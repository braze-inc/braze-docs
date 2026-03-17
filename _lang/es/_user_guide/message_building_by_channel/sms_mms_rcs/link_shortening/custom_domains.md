---
nav_title: Dominios personalizados de autoservicio
article_title: Dominios personalizados en autogestión
page_order: 0
description: "Esta página explica cómo utilizar dominios personalizados con acortamiento de enlaces para personalizar el aspecto de tus URL acortadas."
page_type: reference
alias: "/custom_domains/"
tool:
  - Campaigns
channel:
  - SMS
---

# Dominios personalizados de autoservicio

> Esta página explica cómo configurar tus propios dominios personalizados en el panel de Braze. Los dominios personalizados te permiten utilizar un enlace acortado con tu marca que refleje la identidad de esta, en lugar de un enlace acortado genérico o el dominio Braze (`brz.ai`), lo que mejora la confianza de los usuarios y la interacción en las campañas con enlaces SMS.

Los dominios personalizados de autoservicio te permiten configurar y administrar tus propios dominios personalizados para SMS, RCS y WhatsApp, directamente desde tu panel de Braze. Puedes añadir, supervisar y administrar fácilmente hasta 10 dominios personalizados en un solo lugar.

## Ventajas de los dominios personalizados de autoservicio

- **Configuración optimizada:** Configura tus dominios en la página **Configuración de la empresa** y reduce el tiempo de configuración.
- **Mayor transparencia:** Recibe actualizaciones en tiempo real sobre el estado de configuración de tu dominio a través de banners en el panel.
- **Notificaciones proactivas:** Recibe alertas inmediatas cuando tu dominio personalizado esté conectado o si se produce algún error de configuración.

## Requisitos de dominio

- Los dominios deben ser adquiridos, poseídos y gestionados por usted. Esto se puede hacer a través de un registrador de dominios, como GoDaddy, Amazon Route 53 o Google Domains.
- El dominio utilizado para esta característica debe ser:
  - Único (diferente del dominio de tu sitio web)
  - No se puede utilizar para alojar ningún contenido de la Web.
    - También puedes utilizar subdominios únicos. Por ejemplo, el dominio`braze.com`podría tener subdominios de`sms.braze.com`o `whatsapp.braze.com`.

## Delegación del dominio personalizado

Te pedimos que delegues tu dominio personalizado a Braze para que podamos facilitar el enrutamiento adecuado y la compatibilidad de la infraestructura con nuestros servicios de acortamiento de enlaces y seguimiento de clics. Cuando delegas tu dominio en Braze, nos encargamos automáticamente de la renovación del certificado para evitar una interrupción del servicio. 

## Añadir un dominio personalizado

1. En Braze, ve a **Configuración de la empresa** > **SMS/RCS y dominios de aplicaciones de mensajería**.
![Página «SMS/RCS y dominios de aplicaciones de mensajería» con varios dominios enumerados.]({% image_buster /assets/img/main_page.png %})

{: start="2"}
2\. Selecciona **Añadir dominio** para comenzar una nueva configuración de dominio personalizado.
3\. Introduce el dominio personalizado que has comprado en nuestro campo de entrada de la aplicación, que utiliza nuestra lógica de validación existente para garantizar un formato adecuado, y luego selecciona **Siguiente** y **Enviar**.

![Botón «Añadir dominio» en la página «Dominios de SMS/RCS y aplicaciones de mensajería».]({% image_buster /assets/img/custom_domain_button.png %}){: style="max-width:70%;"}

{: start="4"}
4\. Pide a tu equipo técnico (por ejemplo, ingeniería o TI) que actualice tu configuración DNS con los detalles del registro de DNS de Cloudflare que se muestran. Tu equipo técnico debe actualizar tus registros de DNS con estos datos en un plazo de 45 días.
  - Si necesitas más tiempo para actualizar tus registros de DNS, puedes reiniciar el proceso y generar un nuevo conjunto de registros de DNS para tu dominio.

Braze consultará tu configuración DNS aproximadamente cada 30 minutos para comprobar si hay actualizaciones.

![Sección «Registro de DNS» con tres pasos que debes completar para finalizar la configuración de tu dominio.]({% image_buster /assets/img/dns_record.png %})

{% alert note %}
El progreso de tu dominio se guarda automáticamente. Si necesitas salir a mitad del proceso, puedes reanudarlo más tarde seleccionando la entrada de dominio pendiente en la página **Dominios de SMS/RCS y aplicaciones de mensajería**.
{% endalert %}

### Gestión y uso continuos

Una vez verificado tu dominio, tus dominios personalizados aparecerán en la tabla de la página **Dominios de SMS/RCS y aplicaciones de mensajería** con indicadores de estado. Puedes utilizar inmediatamente los dominios conectados en varios grupos de suscripción, espacios de trabajo y canales SMS, RCS y WhatsApp.

![Lista de dominios personalizados y estados.]({% image_buster /assets/img/custom_domain_statuses.png %}){: style="max-width:60%;"}

La supervisión en tiempo real te avisará en el panel de Braze si alguno de tus dominios activos tiene algún problema, para que tus enlaces personalizados sigan siendo utilizables. Si tienes algún problema, consulta los detalles del error en la aplicación o ponte en contacto con [el soporte]({{site.baseurl}}/braze_support/) de Braze para obtener ayuda.

## Asignación de dominios personalizados a grupos de suscripción

Una vez configurados, los dominios personalizados se pueden asignar a uno o varios grupos de suscripción de SMS, RCS y WhatsApp.

1. Ve a **Audiencia** > **Gestión de grupos de suscripción**.
2. Busca y selecciona tu grupo de suscripción en la lista.
3. En **Detalles del grupo de suscripción**, selecciona tu dominio personalizado como **Dominio** de **acortamiento de enlaces**.

![La configuración de los grupos de suscripción permite seleccionar un dominio de acortamiento de enlaces.]({% image_buster /assets/img/custom_domain.png %})

Las campañas enviadas con la función de acortamiento de enlaces activada utilizarán el dominio asignado asociado a tu grupo de suscripción de SMS, RCS o WhatsApp.

![Vista previa del creador de mensajes SMS con un dominio de enlace acortado que es diferente del dominio del cuadro "Mensaje".]({% image_buster /assets/img/custom_domain2.png %})

## Preguntas más frecuentes

### ¿Pueden compartirse los dominios delegados entre varios grupos de suscripción?

Sí. Un único dominio puede utilizarse con varios grupos de suscripción. Para ello, seleccione el dominio de cada grupo de suscripción al que debe asociarse.

### ¿Pueden compartirse los dominios delegados en varios espacios de trabajo?

Sí. Los dominios pueden asociarse a grupos de suscripción en varios espacios de trabajo, suponiendo que los espacios de trabajo estén dentro de la misma empresa.

### ¿Cuántos dominios personalizados puedes agregar?

Puedes añadir hasta 10 dominios personalizados por panel.

### ¿Qué sucede si no actualizas tus registros de DNS en un plazo de 45 días?

Aunque los datos de tu registro de DNS de Cloudflare caducarán al cabo de 45 días, puedes reiniciar el proceso de configuración con el mismo dominio y Braze generará un conjunto de nuevos registros de DNS para ampliar tu ventana de configuración.

### ¿Se me notificará si se produce un error durante el proceso de actualización del DNS?

Sí. Si se produce un error, recibirás un banner en el panel de Braze con detalles sobre el problema y los pasos para resolverlo. 

### ¿Puedo utilizar un dominio personalizado en varios canales?

Sí. Una vez verificado un dominio personalizado, se puede utilizar en todos los grupos de suscripción de SMS, RCS y WhatsApp en todos los espacios de trabajo dentro de un panel. 

### ¿Qué pasa si tienes preguntas o necesitas más ayuda?

Para obtener información más detallada sobre cómo configurar y administrar dominios personalizados, incluidos los pasos para la solución de problemas y los requisitos técnicos, [ponte en contacto con el servicio de asistencia técnica]({{site.baseurl}}/braze_support/).
