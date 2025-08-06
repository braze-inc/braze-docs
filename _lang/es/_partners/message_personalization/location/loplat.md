---
nav_title: loplat
article_title: loplat
description: "Este artículo de referencia describe la asociación entre Braze y loplat, una plataforma de marketing offline basada en la localización, para permitirle ejecutar campañas de marketing de proximidad añadiendo contexto de localización."
alias: /partners/loplat/
page_type: partner
search_tag: Partner

---

# loplat

> [Loplat](https://www.loplat.com/) es la principal plataforma offline basada en la localización. Utiliza el SDK de loplat para aumentar la afluencia a tu tienda de forma inteligente y ejecutar campañas de marketing que fomenten las compras en tienda. Puede medir el rendimiento de la tienda mediante el análisis de afluencia una vez finalizada la campaña.

_Esta integración está mantenida por Loplat._

## Sobre la integración

La integración de Braze y loplat permite utilizar los servicios de localización de loplat (POI de la tienda y geovalla personalizada) para activar campañas de marketing geocontextuales y crear eventos personalizados mediante segmentación offline. Cuando los usuarios visitan la ubicación seleccionada en loplat X, la información sobre la campaña y la ubicación se envía inmediatamente a Braze.

## Requisitos previos

| Requisito | Descripción |
| --- | --- |
| cuenta loplat X | Para beneficiarse de esta integración es necesario disponer de una cuenta loplat X.<br><br>Envía un correo electrónico a [support@loplat.com](mailto:support@loplat.com) para solicitar una cuenta loplat X. |
| SDK de loplat | loplat SDK reconoce las visitas de los usuarios a las tiendas, procesa los eventos de localización y distingue si los usuarios permanecen en un lugar o se desplazan. Puedes utilizar el SDK de loplat para analizar la afluencia a tu tienda, enviar mensajes push cuando los usuarios entren en ella, etc.<br><br>Ten en cuenta que el SDK sólo está disponible para Android e iOS. |
| Clave REST API de Braze | Una clave Braze REST API con los siguientes permisos:<br>- `users.track`<br>- `campaigns.trigger.send`<br>- `campaigns.list`<br>- `canvas.trigger.send`<br>- `canvas.list`<br><br>Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

La información de localización de eventos personalizada que proporciona loplat puede utilizarse en sus campañas para lograr casos de uso como:

- [Alerta de promoción en las tiendas libres de impuestos](https://www.loplat.com/loplat-x#usecase)
    - Envíe cupones de descuento de tiendas libres de impuestos a los usuarios que se encuentren cerca de las puertas de embarque en el aeropuerto.
- Impulso a la ubicación de estaciones de recarga de vehículos eléctricos
    - Establezca geocercas alrededor de las estaciones de recarga de vehículos eléctricos y notifique a los usuarios cuando estén cerca de la estación, animándoles a cargar.

## Integración

### Paso 1: Integrar los SDK

Integra el SDK de loplat y el SDK de Braze en tu aplicación siguiendo los pasos indicados en la documentación de [integración de loplat-Braze](https://developers.loplat.com/braze/).

### Paso 2: Sincroniza los cuadros de mandos de Braze y loplat X y crea una campaña

Cree una nueva clave API en el panel Braze. Copie la clave API y péguela en **Ajustes > Ajustes API** en el panel de control de loplat X. Consulta la [guía del usuario de loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e?pvs=25) para más detalles.

#### Entrega activada por API

1. Cree una campaña Braze o Canvas que envíe con **Entrega activada por API** y copie el ID de campaña.
2. Inicie la campaña en Braze una vez completados todos los pasos.
3. Vaya a loplat X y cree una campaña siguiendo las instrucciones de la [guía del usuario de loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#2ed232c885014f19b1870b9fca4230fb).
4. Pegue el ID de la campaña Braze en **Configuración del mensaje de la campaña** y lance la campaña.

![]({% image_buster /assets/img/loplat/loplat_api_triggered_delivery.png %})

#### Entrega basada en la acción

Con la integración, puede aplicar condiciones de ubicación mediante el envío de información de geovalla, región, marca o nombre de la tienda. Además, puede añadir segmentos o asignar conversiones con el evento personalizado que ha creado.
1. Cree una campaña loplat X siguiendo las instrucciones de la [guía del usuario de loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#f898aa55ef74440aba76dd9a0e3e7598).
2. Añada un evento personalizado en la **configuración de mensajes de campaña** e inicie la campaña.
3. Vaya al panel Braze y cree una campaña o Canvas que envíe con **Entrega basada en acciones**.
4. Seleccione el evento personalizado que creó en loplat X para establecer una acción de activación de ubicación.

![]({% image_buster /assets/img/loplat/loplat_action_based_delivery.png %})


