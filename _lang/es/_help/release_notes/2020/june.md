---
nav_title: Junio
page_order: 7
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de junio de 2020."
---
# Junio de 2020

## Informes de retención

Los Informes de Retención ofrecen ahora Retención por rangos para [campañas][2] y [Lienzos][1]. El Rango de Retención mide cuántos usuarios vuelven y realizan un evento de retención seleccionado durante intervalos de tiempo específicos. 

## Actualizaciones de la API del seguimiento de usuarios

El [punto final `users/track` ][3] tiene ahora una tasa predeterminada de 50 000 solicitudes de API por minuto para las empresas del panel creadas después del 2 de junio de 2020. Las empresas existentes creadas antes de esta fecha y sus espacios de trabajo seguirán pudiendo realizar solicitudes ilimitadas de API al punto final `users/track`.

Braze está imponiendo este predeterminado en nuestro punto final más utilizado de cara al cliente como un paso hacia nuestros objetivos de estabilidad y fiabilidad para nuestra API e infraestructura. El límite impuesto es muy liberal, y afectará a muy pocas empresas del panel y a sus operaciones habituales. En caso de que necesites aumentar este límite, ponte en contacto con tu administrador del éxito del cliente o con nuestro equipo de soporte para solicitar un aumento.

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/
[3]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
