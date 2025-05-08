---
nav_title: Aprobación de campañas
article_title: Aprobación de campañas
alias: "/campaign_approval/"
page_order: 0
page_type: reference
description: "Esta página ofrece una visión general del proceso de aprobación de campañas."
tool: Campaigns
---

# Aprobación de campañas

> La aprobación de campañas añade un proceso de revisión a su flujo de trabajo antes de lanzar una campaña. Esta función añade estados que están disponibles en el paso de flujo de trabajo de confirmación de campaña. Puede asegurarse de que cada confirmación sea aprobada para lanzar la campaña.

{% alert important %}
La aprobación de campañas no es compatible con el flujo de trabajo de creación de campañas API y campañas de correo electrónico transaccional.
{% endalert %}

## Activar la aprobación de la campaña

Por defecto, la configuración de aprobación de la campaña está desactivada. Para activar esta función, vaya a **Configuración** > **Flujo de aprobación**.

{% alert note %}
Si utiliza la [navegación anterior]({{site.baseurl}}/navigation), puede encontrar esta página en **Gestionar configuración** > **Flujo de trabajo de aprobación**.
{% endalert %}

## Uso de autorizaciones

Una vez activada la aprobación de campañas, deberá disponer del permiso "Aprobar y denegar campañas". Este permiso controla quién puede actualizar el estado de aprobación de una campaña. Este permiso también puede aplicarse a espacios de trabajo o [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) o añadirse a un [conjunto de permisos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets).

En el paso **Revisar resumen** del flujo de trabajo de creación de campañas, utilice la opción de aprobación para aprobar o denegar los componentes clave de su campaña: **Mensajes**, **entrega**, **población destinataria** y **eventos de conversión**. El estado por defecto para la aprobación de campañas es **Pendiente de aprobación**. Nota que es posible autoaprobar componentes de una campaña.

![][1]

Una vez aprobadas todas las secciones, se activará el botón **Lanzar** y podrá poner en marcha su campaña. 

[1]: {% image_buster /assets/img_archive/campaign_approval_example.png %} 
