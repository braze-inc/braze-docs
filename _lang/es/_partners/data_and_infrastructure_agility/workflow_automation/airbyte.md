---
nav_title: Airbyte
article_title: Airbyte
description: "Este artículo de referencia cubre la integración de Braze y Airbyte. Airbyte es un motor de integración de datos de código abierto que le ayuda a consolidar sus datos en sus almacenes de datos, lagos y bases de datos, reenviando eventos en tiempo real desde Airbyte a Braze."
alias: /partners/airbyte/
page_type: partner
search_tag: Airbyte

---

# Airbyte

> [Airbyte](https://airbyte.com/) es un motor de integración de datos de código abierto que te ayuda a consolidar tus datos en tus almacenes de datos, lagos y bases de datos.

_Esta integración está mantenida por Airbyte._

## Sobre la integración

La integración de Braze y Airbyte permite a los usuarios crear una canalización de datos para recopilar y analizar datos de Braze conectando todas sus aplicaciones y bases de datos a un almacén central. Una vez recopilados los datos en el almacén central, los equipos de datos pueden explorar los datos de Braze con eficacia utilizando sus herramientas de inteligencia empresarial preferidas.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Airbyte Cloud | Se requiere una cuenta [Airbyte Cloud](https://cloud.airbyte.io/workspaces) para aprovechar esta integración. |
| Clave REST API de Braze | Una clave Braze REST API con todos los permisos. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | Tu punto final dependerá de la URL Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

1. En su cuenta de Airbyte Cloud, vaya a **Fuentes > + Nueva fuente > Configurar la fuente**.
2. Introduce "Braze" como nombre de la fuente y selecciona **Braze** en el desplegable de fuentes.
3. Proporciona la URL de tu punto final, la clave de API REST de Braze y la fecha de inicio. Haz clic en **Configurar fuente**.

### Modos de sincronización admitidos

El conector de fuente Braze de Airbyte admite los siguientes [modos de sincronización](https://docs.airbyte.com/cloud/core-concepts#connection-sync-modes):
- **Actualización completa | Sobrescribir**: sincroniza todos los registros del origen y sustituye los datos en el destino sobrescribiéndolos.
- **Sincronización incremental | Añadir**: Sincroniza nuevos registros desde el origen y añádelos al destino sin borrar ningún dato.

### Flujos admitidos

- [`campaigns`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18)
- [`campaigns_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c07b5ebd-0246-471e-b154-416d63ae28a1)
- [`canvases`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e6c150d7-fceb-4b10-91e2-a9ca4d5806d1)
- [`canvases_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0fd61e93-7edf-4d87-a8dc-052420aefb73)
- [`events`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1)
- [`events_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bd1ab63-d1a5-4301-8d17-246cf24a178c)
- [`kpi_daily_new_users`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#07756c39-cfa0-40a0-8101-03f8791cec01)
- [`kpi_daily_active_users`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#90a64560-65aa-4f71-a8ef-1edf49321986)
- [`kpi_daily_app_uninstalls`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#59c4d592-3e77-42f8-8ff1-d5d250acbeae)
- [`cards`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9fa7a3bc-4a02-4de2-bc4c-8f111750665e)
- [`cards_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9cdc3b1e-641e-4d62-b9e8-42d04ee9d4d8)
- [`segments`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f)
- [`segments_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#62d9d142-cdec-4aea-a287-c13efea7415e)

{% alert note %}
Los límites de velocidad varían en función del flujo. Visite la [tabla de límites de tarifas]({{site.baseurl}}/api/api_limits/#rate-limits-by-request-type) para obtener más información.
{% endalert %}
