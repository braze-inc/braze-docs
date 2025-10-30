---
nav_title: Modelos de datos
article_title: Crear un modelo de datos B2B
page_order: 0
page_type: reference
description: "Aprende a utilizar las herramientas de datos Braze para crear modelos B2B."
---

# Crear un modelo de datos B2B

> Este caso de uso demuestra cómo puedes utilizar las herramientas de datos Braze para crear un modelo de datos B2B eficaz y eficiente que te ayude a orientar, desencadenar, personalizar y enviar mensajes a los usuarios de tu empresa. 

{% alert note %}
Estas recomendaciones pueden cambiar con el tiempo a medida que Braze desarrolle sus capacidades B2B.
{% endalert %}

Antes de entrar en cómo puedes configurar tu modelo de datos B2B, vamos a repasar varios conceptos y términos que debes conocer.

Hay cuatro objetos B2B principales que necesitas para ejecutar campañas B2B.

| Objeto | Descripción |
| --- | --- |
| Dirige | Un registro de clientes potenciales que han mostrado interés por un producto o servicio, pero que aún no han sido calificados como una oportunidad. |
| Contactos | Normalmente, personas que han sido cualificadas y convertidas de cliente potencial a contacto para buscar una oportunidad de venta. |
| Oportunidades | Un registro que sigue los detalles de una venta potencial o de un acuerdo en curso
| Cuentas | Un registro de una organización que es un cliente potencial cualificado, un cliente existente, un socio o un competidor que mantiene una relación de importancia similar. |
{: .reset-td-br-1 .reset-td-br-2 }

En Braze, estos cuatro objetos se combinan y se reducen a dos: perfiles de usuario y objetos empresariales.

| Objeto Braze B2B | Descripción | Objetos B2B originales  |
| --- | --- | --- |
| Perfiles de usuario | Éstos se mapean directamente con clientes potenciales y contactos en tu sistema CRM de ventas. Como Braze capta los clientes potenciales, se crean automáticamente como clientes potenciales en tu sistema CRM de ventas. A medida que se convierten en contactos, los ID y detalles de los contactos se sincronizan de nuevo con Braze. |Dirige<br> Contactos |
| Objetos empresariales | Se mapean con cualquier objeto no usuario de tu sistema CRM de ventas. Esto incluye tus objetos específicos de ventas, como objetos de cuenta y objetos de oportunidad. | Cuentas<br> Oportunidades |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Paso 1: Crea tus objetos de negocio en Braze

Los objetos de negocio son cualquier conjunto de datos no centrado en el usuario. En un contexto B2B, éstos incluyen tus datos de cuentas y oportunidades, y cualquier otro conjunto de datos pertinente no centrado en el usuario que tu empresa siga.

Existen dos métodos para crear y gestionar tus objetos de negocio en Braze, los catálogos y las fuentes conectadas. 

| Método | Descripción |
| --- | --- |
| [Catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs) | Son objetos de datos independientes (objetos de datos complementarios) del perfil de usuario principal en Braze. En un contexto B2B, probablemente tendrías catálogos para tus cuentas y oportunidades. |
| [Fuentes conectadas]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/) | Permiten a Braze consultar directamente tu almacén de datos. Es probable que ya estés sincronizando regularmente tus objetos de clientes potenciales, contactos, oportunidades y cuentas con tu almacén de datos, así que puedes dirigir la segmentación Braze directamente a ese almacén y activarla en un entorno de copia cero. |
{: .reset-td-br-1 .reset-td-br-2 }

{% tabs %}
{% tab Catalogs %}

### Opción 1: Utiliza catálogos para cuentas y oportunidades

Los catálogos son tablas de datos que se alojan y gestionan en Braze. Aunque los datos de cuentas y oportunidades proceden del sistema CRM de ventas que hayas elegido, los duplicarías en Braze para utilizarlos con fines de marketing: segmentación basada en cuentas, marketing basado en cuentas, gestión de clientes potenciales, etc.

Para esta opción, recomendamos crear un catálogo para tus cuentas y otro para tus oportunidades, y actualizarlos con frecuencia enviando actualizaciones de Braze a través de nuestra [API de catálogos]({{site.baseurl}}/api/endpoints/catalogs/) o de [la Ingesta de datos en la nube (CDI) de catálogos]({{site.baseurl}}/user_guide/data/cloud_ingestion/sync_catalogs_data/). Al crear estos catálogos, asegúrate de que la `id` (primera columna) de tu catálogo coincide con la `id` de tu sistema CRM de ventas.

#### Mapeado sobre tus campos CRM

Las tablas siguientes incluyen algunos ejemplos de campos que puedes mapear desde los objetos de cuenta y oportunidad de tu CRM.

{% subtabs %}
{% subtab Account catalog %}

En este caso de uso, Salesforce es el sistema CRM de ejemplo. Puedes mapear sobre cualquier campo incluido en los objetos de tu CRM.

<table border="1">
  <tr>
    <th><b>Objeto Braze</b></th>
    <th><b>Campo de Braze</b></th>
    <th><b>Objeto CRM (Salesforce)</b></th>
    <th><b>Campo CRM (Salesforce)</b></th>
  </tr>
  <tr>
    <td rowspan="4">Catálogo > Catálogo de cuentas</td>
    <td><code>ID</code></td>
    <td><code>cuenta</code></td>
    <td><code>ID</code></td>
  </tr>
  <tr>
    <td><code>NombreCuenta</code></td>
    <td><code>cuenta</code></td>
    <td><code>Nombre de la cuenta</code></td>
  </tr>
  <tr>
    <td><code>Tipo</code></td>
    <td><code>cuenta</code></td>
    <td><code>Tipo</code></td>
  </tr>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>cuenta</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
</table>

##### Ejemplo de tabla de campos de cuenta mapeados

\![Tabla de cuentas de Salesforce con la información correspondiente, como la dirección de facturación y el propietario de la cuenta.]({% image_buster /assets/img/b2b/sf_accounts.png %})

{% endsubtab %}
{% subtab Opportunity catalog %}

En este caso de uso, Salesforce es el sistema CRM de ejemplo. Puedes mapear sobre cualquier campo incluido en los objetos de tu CRM.

<table border="1">
  <tr>
    <th><b>Objeto Braze</b></th>
    <th><b>Campo de Braze</b></th>
    <th><b>Objeto CRM (Salesforce)</b></th>
    <th><b>Campo CRM (Salesforce)</b></th>
  </tr>
  <tr>
    <td rowspan="4">Catálogo > Catálogo de oportunidades</td>
    <td><code>ID</code></td>
    <td><code>oportunidad</code></td>
    <td><code>ID</code></td>
  </tr>
  <tr>
    <td><code>NombreDeLaOportunidad</code></td>
    <td><code>oportunidad</code></td>
    <td><code>Nombre de la oportunidad</code></td>
  </tr>
  <tr>
    <td><code>Territorio</code></td>
    <td><code>oportunidad</code></td>
    <td><code>Territorio</code></td>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>oportunidad</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
  </tr>
</table>

##### Ejemplo de tabla de campos de oportunidad mapeados

\![Tabla de oportunidades de Salesforce con la información correspondiente, como la dirección de facturación y el propietario de la cuenta.]({% image_buster /assets/img/b2b/sf_opportunities.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Connected sources %}

### Opción 2: Utiliza fuentes conectadas para cuentas y oportunidades

Los orígenes conectados son tablas de datos alojadas por ti en tu propio almacén de datos y consultadas por [las extensiones de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/) Braze [CDI]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/). A diferencia de los catálogos, en lugar de duplicar tus objetos de negocio (cuentas y oportunidades) en Braze, los mantendrías en tu almacén de datos y utilizarías tu almacén como fuente de verdad.

Para configurar las [fuentes conectadas]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources#integrating-connected-sources), consulta [Integrar fuentes conectadas]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources#integrating-connected-sources).

{% endtab %}
{% endtabs %}

## Paso 2: Relaciona los objetos de tu empresa con los perfiles de usuario

Los perfiles de usuario son el objeto principal de Braze, que impulsa la mayor parte de tu segmentación demográfica, desencadenamiento y personalización. Los perfiles de usuario incluyen [datos de usuario predeterminados]({{site.baseurl}}/user_guide/data/user_data_collection/) recopilados por nuestro SDK y otras fuentes, incluidos [datos personalizados]({{site.baseurl}}/user_guide/data/custom_data/), que adoptan la forma de atributos (datos demográficos), eventos (datos de comportamiento) o compras (datos de transacciones).

### Paso 2.1: Mapea ID de CRM de ventas a Braze

En primer lugar, asegúrate de que Braze y el CRM que elijas tengan un identificador común con el que compartir datos. Te sugerimos que utilices la siguiente tabla para mapear tus campos de ID de CRM de ventas al objeto de usuario Braze. En la tabla siguiente, Salesforce es el sistema CRM, pero se puede hacer con cualquier CRM.

#### Objeto Braze: Usuario

| Campo de Braze | Objeto CRM (Salesforce) | Campo CRM (Salesforce) | Información adicional |
| --- | --- | --- | --- |
| `Aliases.salesforce_lead_id` | Dirige | `id` |  \- Etiqueta de alias de usuario: `salesforce_lead_id` <br>\- Nombre del alias de usuario: `lead_id`|
| `Aliases.salesforce_contact_id` | Ponte en contacto con | `id` | \- Etiqueta de alias de usuario: `salesforce_contact_id` <br>\- Nombre del alias de usuario: `contact_id` |
| `AccountId` | Ponte en contacto con | `AccountId` | 
| `OpportunityId` (opcional, escalar) <br>o<br> `Opportunities` (opcional, matriz) | Oportunidad | `id` | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% alert note %}
Recomendamos utilizar [alias]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) en lugar de `external_id` para mapear los identificadores de contactos y clientes potenciales de Salesforce a Braze. Esto se debe a que reduce la cantidad de búsquedas necesarias a la hora de identificar y ejecutar tus iniciativas de estilo de crecimiento basadas en productos.
{% endalert %}

Una vez sincronizados tus ID, tienes que relacionar tus perfiles de usuario Braze con tus objetos empresariales. 

### Paso 2.2: Crea una relación entre los perfiles de usuario y tus objetos empresariales

{% tabs %}
{% tab Catalogs %}

#### Opción 1: Cuando utilices catálogos

Ahora que tus detalles de oportunidad y de cuenta se contabilizan como catálogos Braze, tienes que crear una relación entre esos catálogos y los perfiles de usuario a los que quieres enviar mensajes. Actualmente, esto requiere dos pasos:

1. Incluye la cuenta (como `account_id (string)`), el ID de oportunidad (como `opportunity_ids (array)`), o ambos en el perfil de usuario como atributos.
2. Registra un evento (como `account_linked`) que incluya el ID de la cuenta como propiedad del evento.

```json
{
  "attributes" : [
    {
      "external_id" : "user1",
      "accountId" : "001J7000004K7AF",
      "opportunityIds" : [
"0064J000004EU59",
"0064J000004EU5G"
]
    }
  ],
  "events" : [
    {
      "external_id" : "user1",
      "name" : "account_linked",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "account_id": "001J7000004K7AF"
      }
    }
  ]
}
```

{% endtab %}
{% tab Connected sources %}

#### Opción 2: Cuando utilices fuentes conectadas

Una de las tablas de tu fuente conectada debe incluir un `user_id` que coincida con el `external_user_id` configurado en Braze para tus usuarios. La configuración del perfil de usuario anterior utiliza tu lead y `contact_ids` como tu `external_id`, por lo que debes asegurarte de que tus tablas de lead/contacto incluyen estos ID.

Además de asegurarnos de que los ID coinciden, recomendamos escribir en los perfiles de usuario datos básicos a nivel de cuenta, como `account_id`, `opportunity_id`, e incluso atributos firmográficos comunes, como `industry`, para una segmentación y personalización eficaces.

{% endtab %}
{% endtabs %}