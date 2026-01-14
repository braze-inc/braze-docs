---
nav_title: MetaRouter
article_title: MetaRouter
description: "Eleva tu administración de datos de clientes en Braze con MetaRouter. Esta solución de gestión de etiquetas del lado del servidor de alto rendimiento ofrece el máximo cumplimiento y control con opciones de despliegue sin fisuras, ya sea en una nube privada alojada en MetaRouter o en su propia infraestructura."
alias: /partners/metarouter/
page_type: partner
search_tag: Partner
---

# MetaRouter

> [MetaRouter](https://www.metarouter.io/) eleva tu experiencia Braze integrándose fácilmente como una potente plataforma de gestión de etiquetas del lado del servidor. Le permite orquestar un recorrido completo de los datos del cliente dentro de Braze, desde la recopilación de datos de origen totalmente fiable y enriquecida hasta en un 30%, hasta la activación de flujos de eventos en tiempo real para recorridos personalizados. Además, MetaRouter agiliza la implementación al eliminar la necesidad de etiquetas Braze u otras etiquetas de terceros, otorgándole un control granular, parámetro por parámetro, sobre los datos que fluyen hacia Braze.

_Esta integración está mantenida por Metarouter._

## Características compatibles

- Se pueden incorporar reintentos.
- Las solicitudes se procesan por lotes.
- Los problemas de limitación de velocidad se gestionan con un reintento.
- Se admiten ID y PII externos. MetaRouter pasa su ID anónimo y cualquier PII (correo electrónico, número de teléfono, nombre) que los clientes deseen.
- Puede enviar datos de compras y eventos personalizados de Braze.
  - Se admiten propiedades de eventos.
  - No se admiten propiedades de eventos anidadas.

## Requisitos previos

Antes de empezar, necesitarás lo siguiente:

| Requisito           | Descripción                                                                                                                                          |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Una cuenta MetaRouter  | Una [cuenta MetaRouter Enterprise](https://enterprise.metarouter.io/).                                                                                |
| Clave REST API de Braze    | Una clave de API REST de Braze con permisos `users.track`. Para crear una, vaya a **Configuración** > **Claves API**.                                                |
| Un punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Configuración de MetaRouter

Para configurar MetaRouter para su integración Braze:

1. Ve a MetaRouter y crea un nuevo cluster.
2. Elija los eventos que desea seguir.
3. Instala un SDK de MetaRouter e integra eventos en tu sitio web.
4. Conecte su clúster a la interfaz de usuario de su sitio web.
5. Crea una nueva canalización.
6. Verifique que su sitio web está enviando eventos a MetaRouter.

## Integración de Braze

### Paso 1: Añadir la integración Braze

En Enterprise MetaRouter, selecciona **Integraciones** > **Nueva integración** > **Braze**, y luego asigna un nombre a tu integración. A continuación, introduzca la URL de su instancia y la clave API y seleccione **Aplicar cambios**.

![Añadir Braze como integración en MetaRouter.]({% image_buster /assets/img/metarouter/img1.png %}){: style="max-width:50%;"}

### Paso 2: Añadir asignación de eventos

Añada la asignación de eventos para cada salida de identidad y, a continuación, configure los eventos que desea enviar a Braze. Cuando haya terminado, seleccione **Guardar como nueva revisión**.

![Añadir mapeo de eventos para cada una de las salidas de identidad.]({% image_buster /assets/img/metarouter/img2.png %})

