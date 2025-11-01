---
nav_title: Dominios personalizados de autoservicio
article_title: Dominios personalizados de autoservicio
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

> Esta página explica cómo configurar tus propios dominios personalizados en el panel de Braze. Los dominios personalizados te permiten utilizar un enlace acortado de marca que refleje la identidad de tu marca en lugar de un enlace acortado genérico o el dominio Braze (`brz.ai`)-mejorando la confianza de los usuarios y la interacción con los usuarios en las campañas con enlaces SMS.

Los dominios personalizados de autoservicio te permiten configurar y gestionar tus propios dominios personalizados para SMS, RCS y WhatsApp, directamente desde tu panel Braze. Puedes añadir, supervisar y gestionar fácilmente hasta 10 dominios personalizados en un solo lugar.

## Ventajas del autoservicio de dominios personalizados

- **Configuración simplificada:** Configura tus dominios en la página **Configuración de la empresa**, reduciendo el tiempo de configuración.
- **Mayor transparencia:** Recibe actualizaciones en tiempo real sobre el estado de configuración de tu dominio mediante banners en el panel.
- **Notificaciones proactivas:** Recibe alertas inmediatas cuando se conecte tu dominio personalizado o si se produce algún error de configuración.

## Requisitos del dominio

- Los dominios deben ser adquiridos, de tu propiedad y gestionados por ti. Esto puede hacerse a través de un registrador de dominios, como GoDaddy, Amazon Route 53 o Google Domains.
- El dominio utilizado para esta característica debe ser:
  - Único (diferente del dominio de tu sitio web)
  - No puede utilizarse para alojar ningún contenido Web
    - También puedes utilizar subdominios únicos. Por ejemplo, el dominio `braze.com` podría tener subdominios de `sms.braze.com` o `whatsapp.braze.com`.

## Delegar tu dominio personalizado

Te pedimos que delegues tu dominio personalizado en Braze para que podamos facilitar el enrutamiento adecuado y la compatibilidad de la infraestructura con nuestros servicios de acortamiento de enlaces y seguimiento de clics. Cuando delegas tu dominio en Braze, nos encargamos automáticamente de la renovación del certificado para evitar una interrupción del servicio. 

## Añadir un dominio personalizado

1. En Braze, ve a **Configuración de la empresa** > **SMS/RCS y Dominios de aplicaciones de mensajería**.
Página "Dominios de aplicaciones de mensajería y SMS/RCS" con varios dominios listados.]({% image_buster /assets/img/main_page.png %})

{: start="2"}
2\. Selecciona **Añadir dominio** para iniciar la configuración de un nuevo dominio personalizado.
3\. Introduce el dominio personalizado que has comprado en nuestra entrada de la aplicación, que utiliza nuestra lógica de validación existente para que el formato sea correcto, luego selecciona **Siguiente** y **Enviar**.

Botón "Añadir dominio" en la página "Dominios de aplicaciones de mensajería y SMS/RCS".]({% image_buster /assets/img/custom_domain_button.png %}){: style="max-width:70%;"}

{: start="4"}
4\. Haz que tu equipo técnico (como ingeniería o TI) actualice la configuración de DNS con los detalles del registro de DNS de Cloudflare que se muestran. Tu equipo técnico debe actualizar tus registros de DNS con estos datos en un plazo de 45 días.
  - Si necesitas más tiempo para actualizar tus registros de DNS, puedes reiniciar el proceso y generar un nuevo conjunto de registros de DNS para tu dominio.

Braze sondeará tu configuración de DNS aproximadamente cada 30 minutos para comprobar si hay actualizaciones.

\!["Registro de DNS" sección con 3 pasos a completar para terminar de configurar tu dominio.]({% image_buster /assets/img/dns_record.png %})

{% alert note %}
El progreso de tu dominio se guarda automáticamente. Si necesitas salir a mitad del flujo, puedes reanudarlo más tarde seleccionando la entrada del dominio pendiente en la página **Dominios de aplicaciones de mensajería y SMS/RCS**.
{% endalert %}

### Gestión y uso continuados

Una vez verificado tu dominio, tus dominios personalizados aparecerán en la tabla de la página **Dominios de las aplicaciones de mensajería y SMS/RCS** con indicadores de estado. Puedes utilizar inmediatamente dominios conectados en varios grupos de suscripción, espacios de trabajo y canales de SMS, RCS y WhatsApp.

\![Lista de dominios y estados personalizados.]({% image_buster /assets/img/custom_domain_statuses.png %}){: style="max-width:60%;"}

La supervisión en vivo te avisará en el panel de Braze si alguno de tus dominios activos tiene algún problema, para que tus enlaces personalizados sigan siendo utilizables. Si tienes algún problema, consulta los detalles de error de la aplicación o ponte en contacto con [el soporte]({{site.baseurl}}/braze_support/) de Braze para obtener ayuda.

## Utilizar dominios personalizados

Una vez configurados, los dominios personalizados pueden asignarse a uno o varios grupos de suscripción a SMS, RCS y WhatsApp.

\![Configuración de los grupos de suscripción que te permite seleccionar un dominio de acortamiento de enlaces.]({% image_buster /assets/img/custom_domain.png %})

Las campañas enviadas con el acortamiento de enlaces activado utilizarán el dominio asignado asociado a tu grupo de suscripción de SMS, RCS o WhatsApp.

\![Vista previa del creador de mensajes SMS con un dominio de enlace acortado que es diferente del dominio del cuadro "Mensaje".]({% image_buster /assets/img/custom_domain2.png %})

## Preguntas más frecuentes

### ¿Se pueden compartir dominios delegados entre varios grupos de suscripción?

Sí. Un único dominio puede utilizarse con varios grupos de suscripción. Para ello, selecciona el dominio de cada grupo de suscripción al que deba asociarse.

### ¿Se pueden compartir dominios delegados en varios espacios de trabajo?

Sí. Los dominios pueden asociarse a grupos de suscripción en varios espacios de trabajo, suponiendo que los espacios de trabajo estén dentro de la misma empresa.

### ¿Cuántos dominios personalizados puedo añadir?

Puedes añadir hasta 10 dominios personalizados por panel.

### ¿Qué ocurre si no actualizo mis registros de DNS en un plazo de 45 días?

Aunque los detalles de tu registro de DNS de Cloudflare caducarán a los 45 días, puedes reiniciar el proceso de configuración con el mismo dominio y Braze generará un conjunto de nuevos registros de DNS para ampliar tu ventana de configuración.

### ¿Se me notificará si se produce un error durante el proceso de actualización de DNS?

Sí. Si hay un error, recibirás un aviso en el panel de Braze detallando el problema junto con los pasos para resolverlo. 

### ¿Puedo utilizar un dominio personalizado en varios canales?

Sí. Una vez verificado un dominio personalizado, puede utilizarse en todos los grupos de suscripción de SMS, RCS y WhatsApp en todos los espacios de trabajo dentro de un panel. 

### ¿Qué hago si tengo preguntas o necesito más ayuda?

Para obtener información más detallada sobre la configuración y gestión de dominios personalizados, incluidos los pasos para la solución de problemas y los requisitos técnicos, [ponte en contacto con el servicio de asistencia]({{site.baseurl}}/braze_support/).