---
nav_title: Merkury
article_title: Merkury
description: "Este artículo de referencia describe la asociación entre Braze y Merkury, una plataforma de identidad empresarial para tus aplicaciones, que te permite aprovechar el `MerkuryID` para aumentar las tasas de reconocimiento de los visitantes del sitio de los clientes de Braze."
page_type: partner
search_tag: Partner

---

# Merkury

> [Merkury](https://merkury.merkleinc.com/) es la plataforma de identidad empresarial de Merkle que ayuda a las marcas a maximizar la interacción, la experiencia y los ingresos de los consumidores a través de funciones de identidad de primera mano sin necesidad de intermediarios. `MerkuryID` unifica los registros de clientes y clientes potenciales conocidos y desconocidos de una marca, las visitas a sitios o aplicaciones y los datos de los consumidores en un único y persistente identificador de persona.

_Esta integración está mantenida por Merkury._

## Sobre la integración

La integración de Braze y Merkury permite aprovechar `MerkuryID` para aumentar las tasas de reconocimiento de los visitantes del sitio para los clientes de Braze. Al reconocer a los visitantes que son suscriptores de correo electrónico de la marca, Merkury actualizará el perfil de Braze para incluir la dirección de correo electrónico del suscriptor. La mayor capacidad de reconocimiento de `MerkuryID` mejora el compromiso y las oportunidades de personalización y aumenta inmediatamente las cantidades de envíos de correo electrónico por abandono del sitio y los ingresos asociados. 

## Requisitos previos

| Requisito | Descripción |
| --- | --- |
| Cuenta Merkle | Se necesita una cuenta de Merkle para beneficiarse de esta asociación. |
| ID de cliente de Merkle | Obtén tu ID de cliente de tu representante de Merkle. |
| Etiqueta Merkury | Coloca la etiqueta Merkury de Merkle en tu sitio web. |
| Punto final REST y SDK de Braze | La URL de tu punto final REST o SDK. Tu punto final dependerá de la [URL Braze de tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track, users.export.ids, users.export.segment, and segments.list`. <br><br>Se puede crear en **el panel de Braze > Consola para desarrolladores > Clave de API REST > Crear nueva clave de API**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Las solicitudes del conector de identidad Merkury a Braze operan dentro de las especificaciones de límite de velocidad de Braze API. Ponte en contacto con Braze o con tu director de cuentas de Merkle si tienes alguna pregunta.<br><br>Merkury enviará al menos una solicitud al final de una sesión cualificada.
{% endalert %}

## Integración en paralelo de SDK

Utiliza la etiqueta Merkury del lado del cliente de Merkle para capturar dispositivos Braze y los reenvía al punto final del conector de identidad Merkury para su identificación.

### Paso 1: Configurar la etiqueta web SDK de Braze

Debes tener el [SDK de Braze Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#install-gtm) desplegado en tu sitio web para utilizar esta integración.

### Paso 2: Despliega la etiqueta Merkle de Merkury

Despliega la etiqueta Merkury en tu sitio web. Esto hará que el conector de identidad Merkury esté disponible en tu sitio web. El director de cuentas de Merkle te proporcionará una guía detallada con instrucciones.

### Paso 3: Crear atributos personalizados

Los siguientes campos serán rellenados por el conector de identidad Merkury y necesitan ser creados en Braze como [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#custom-attributes).

| Nombre del atributo | Tipo de datos | Descripción |
| --- | --- | --- |
| `hmid` | Cadena | ID de Merkury de Merkle |
| `confidence_score` | Número | Nivel de confianza con el que Merkury pudo identificar (1-8, cuanto más bajo mejor) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Paso 4: Proporcionar a Merkle el universo de correos electrónicos de los usuarios

Merkle recomienda una exportación de segmentación de su universo de correo electrónico permitido. Esto puede seguirse con exportaciones diarias de usuarios activos permitidos.

Los siguientes campos son obligatorios:

- `braze_id`
- `external_id`
- dirección de correo electrónico

Consulta a tu representante de Braze para más información.

