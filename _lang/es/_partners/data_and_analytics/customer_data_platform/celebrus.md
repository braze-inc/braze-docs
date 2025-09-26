---
nav_title: Celebrus
article_title: Integración de Celebrus
description: "Integración de Braze y Celebrus."
---

# Celebrus

> Celebrus se integra a la perfección con el SDK de Braze en todos los canales web y de aplicaciones móviles, facilitando la población de Braze con datos de actividad del canal. Esto incluye información exhaustiva sobre el tráfico de visitantes a través de activos digitales durante periodos específicos. <br><br>Además, Celebrus captura datos de perfil enriquecidos para cada cliente individual, que pueden sincronizarse con Braze. Esto le permite crear estrategias eficaces de comunicación y análisis de Braze basadas en datos de origen completos, precisos y detallados. Esta capacidad se ve reforzada por las señales basadas en el aprendizaje automático de Celebrus, que permiten una captura de datos sin complicaciones y sin necesidad de un etiquetado exhaustivo. Con un sólido gráfico de identidades de origen, todos los datos son accesibles al instante para su uso inmediato. 

_Esta integración está mantenida por Celebrus._

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta Celebrus | Se necesita una cuenta Celebrus para beneficiarse de esta asociación. |
| Almacén de datos (opcional) | Al utilizar el conector Celebrus para atributos personalizados Braze, debe disponer de un almacén de datos compatible con la integración Braze Cloud Data Ingestion (CDI) y configurar CDI en el panel Braze. |
| Ajustes de configuración del SDK de Braze (opcional) | Cuando utilices el conector Celebrus para el SDK de Braze, debes pasar el punto final SDK y la clave de API de SDK. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Aplicación
Después de instalar su implementación de Celebrus, utilice los conectores de Celebrus para Braze para integrar los datos de Celebrus en Braze. Hay dos elementos en la integración de Celebrus para Braze: el SDK de Braze y los atributos personalizados de Braze. Puede desplegar cualquiera de los dos, o ambos, en función de cómo utilice Braze y de los casos de uso que necesite.

Si aún no tienes implementado el SDK de Braze en tu canal Web, puedes utilizar Celebrus para desplegar el SDK de Braze. Celebrus añadirá el SDK Braze a las páginas web y configurará la identidad Braze para el visitante de la web utilizando el gráfico de identidad de Celebrus. Los atributos de los clientes pueden sincronizarse con Braze mediante una Ingesta de Datos en la Nube (CDI). Esto requiere un almacén de datos compatible con Braze CDI, así como la configuración del CDI en Braze.

### Conector Celebrus para Braze SDK

El conector Celebrus para el SDK de Braze proporciona datos de canal de alto nivel de aplicaciones Web y móviles para Braze. En el SDK de Braze, el `System Identity` de Celebrus del gráfico de identidad de Celebrus se utilizará como identificador para la integración de Braze. Se admiten otros identificadores para sincronizar atributos personalizados a través del conector Braze Custom Attributes Celebrus.

El conector despliega y configura el SDK de Braze en tu canal, por lo que tendrás que configurar algunos ajustes en el flujo de datos del SDK de Braze y proporcionar los valores de estos tres ajustes:

```
    response.addParameter("sdk_endpoint", "sdk.xxxxxx.braze.com");
    response.addParameter("api_key", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
    response.addParameter("app_id", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
```

{% alert important %}
El conector Celebrus para el SDK de Braze insertará e inicializará el SDK de Braze para identificar al usuario y añadir el identificador al Gráfico de Identidad de Celebrus. Este conector no registrará datos en el perfil de usuario ni activará otros métodos del SDK de Braze. <br><br>Puede llamar a los métodos que desee directamente dentro de su base de código para registrar datos a través del [SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) o aprovechar otras funciones compatibles con el SDK de Braze.
{% endalert%}

### Conector Celebrus para atributos personalizados Braze

#### Paso 1: Configurar detalles conectados en Celebrus 

El conector Celebrus para atributos personalizados Braze envía atributos personalizados a una base de datos intermedia, preformateados de la forma en que Braze espera recibirlos. En Celebrus se configuran los detalles de conexión para la base de datos, que dependerán del tipo de base de datos que se esté utilizando (como Snowflake o Redshift). 

#### Paso 2: Configura la ingesta de datos en la nube en tu panel de Braze

Esta integración utiliza Braze Cloud Data Ingestion. Siga las instrucciones en [Integraciones de almacenes de datos]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/) para establecer y configurar [los ajustes de Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/) según el tipo de almacén que esté utilizando. 

#### Paso 3: Sincronizar datos de Celebrus a Braze

Celebrus captura y asigna identificadores únicos a un individuo, como correo electrónico, teléfono, `external_id`o alias de usuario, y los envía a Braze a través de CDI. Esto permite sincronizar con Braze los datos de un mismo individuo.

Celebrus utilizará los identificadores definidos para enviar los atributos del cliente definidos en el generador de perfiles de Celebrus, pero sólo cuando cambien los valores de los atributos. Ten en cuenta que los nombres de atributos definidos en el generador de perfiles Celebrus se utilizarán en Braze por defecto. Así que asegúrate de actualizar estos nombres para que se adhieran a [las convenciones de nomenclatura de Braze]({{site.baseurl}}/api/objects_filters/user_attributes_object/).

{% alert important %}
Por ahora, esta versión no admite eventos ni compras.<br><br> Esta integración envía atributos como valores de cadena, por lo que algunos atributos son listas (como las señales). Por ahora, las listas no pueden convertirse en matrices. No hay atributos anidados.
{% endalert%}

