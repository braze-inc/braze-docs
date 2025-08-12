---
nav_title: actionable.me
article_title: actionable.me
description: "Este artículo de referencia describe la asociación entre Braze y actionable.me, un software y unos procesos patentados, que te permiten sacar el máximo partido a tu inversión en Braze de inmediato."
alias: /partners/actionableme/
page_type: partner
search_tag: Partner

---

# actionable.me

> [actionable.me](https://actionable.me), desarrollado por el equipo de Massive Rocket, una agencia de datos y CRM, es un enfoque estandarizado y automatizado para ejecutar programas de CRM, que proporciona herramientas y procesos diseñados para que los clientes de Braze obtengan valor de forma rápida, consistente y predecible. 

_Esta integración está mantenida por actionable.me._

## Sobre la integración

La integración de Braze y actionable.me te permite desplegar un servicio para supervisar tu progreso en la utilización de Braze. Mediante una combinación de herramientas y procesos, evaluarán rápidamente el rendimiento de tu CRM, identificarán nuevas oportunidades y proporcionarán recomendaciones sobre cómo obtener mejores resultados.

## Requisitos previos

| Requisito | Descripción |
| --- | --- |
| Cuenta actionable.me | Se necesita una cuenta en actionable.me para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con los permisos enumerados en la siguiente sección.<br><br> Puede crearse en el dashboard de Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

Para integrar Braze y actionable.me, hay que configurar la plataforma actionable.me, y crear una clave de API Braze en Braze y configurarla en el panel actionable.me.

### Paso 1: Crea tu clave de API Braze

En Braze, ve a **Configuración** > **Claves de API**. Selecciona **Crear nueva clave de API** y asegúrate de que se añaden los siguientes permisos:

- `campaigns.list`
- `campaigns.data_series`
- `campaigns.details`
- `sends.data_series`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `events.list`
- `canvas.list`
- `canvas.data_series`
- `canvas.details`
- `canvas.data_summary`
- `kpi.mau.data_series`
- `kpi.dau.data_series`
- `kpi.new_users.data_series`
- `kpi.uninstalls.data_series`

### Paso 2: Proporciona información al equipo de actionable.me 

Para completar la integración, debes proporcionar tu clave de API REST y [la URL del punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) a tu equipo de operaciones de actionable.me. A continuación, actionable.me establecerá la conexión y se pondrá en contacto contigo una vez finalizada la configuración para empezar a compartir información.

![La página actionable.me "añadir plataforma" que configurará el equipo de operaciones actionable.me.]({% image_buster /assets/img/actionableme/image2.png %})

## Solución de problemas

Ponte en contacto con el equipo de actionable.me o Massive Rocket para obtener ayuda adicional: [info@massiverocket.com](mailto:info@massiverocket.com)


