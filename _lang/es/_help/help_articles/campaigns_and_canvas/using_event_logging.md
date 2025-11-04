---
nav_title: Uso del registro de eventos
article_title: Uso del registro de eventos
page_order: 6
page_type: solution
description: "Este artículo de ayuda describe cómo utilizar el registro de eventos para solucionar problemas con tu integración Braze."
---

# Utilizar el registro de eventos

Para ayudar a solucionar problemas con tu integración Braze, puedes configurar un perfil de usuario anónimo y un [registro de usuarios del evento]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab). Para saber cómo configurar un perfil anónimo, consulta [Añadir usuarios de prueba]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users).

## Sobre los registros

Utiliza el registro de eventos para probar cómo es el comportamiento de un usuario anónimo. Esto puede ser especialmente útil para identificar el ID de usuario si la aplicación que se está probando no recopila correo electrónico. Puedes utilizar Braze y la dirección IP de tu dispositivo para añadir ese dispositivo como usuario de prueba.

Es una buena forma de encontrar usuarios anónimos. También puedes utilizar esta información para comprobar qué datos se envían a Braze y comprobar si hay discrepancias. Desde esta vista, puedes identificar si los deltas de tus datos se están enviando a Braze. Si se envía una dirección de correo electrónico o un token de notificaciones push con cada evento registrado, entonces todos los datos se envían a Braze.

¿Aún necesitas ayuda? Abre un [ticket de soporte]({{site.baseurl}}/braze_support/).

_Última actualización: 16 de noviembre de 2022_

