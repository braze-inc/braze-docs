---
nav_title: Transifex
article_title: Transifex
alias: /partners/transifex/
description: "Este artículo de referencia describe la asociación entre Braze y Transifex, una plataforma de localización que le permite automatizar la traducción liberando a sus equipos para que se centren en ofrecer experiencias brillantes a los clientes."
page_type: partner
search_tag: Partner

---

# Transifex

> Transifex permite una localización robusta en toda su base de usuarios, sin importar el idioma.

_Esta integración está mantenida por Transifex._

## Sobre la integración

La integración de Braze y Transifex aprovecha Connected Content para permitirte extraer una colección de cadenas de recursos e incluir las traducciones pertinentes en tus mensajes en lugar de líneas de formato condicional basadas en el idioma. Esto automatiza la traducción y libera a sus equipos para que se centren en ofrecer experiencias brillantes a los clientes.

{% alert important %}
A partir del 7 de abril de 2022, Transifex ha dejado obsoletas sus versiones 2 y 2.5 de la API para dar paso a la versión 3\. Las v2 y v2.5 ya no son operativas, y las solicitudes correspondientes fallarán. <br><br>Las siguientes instrucciones de integración reflejan la actualización de la versión 3. Actualice en consecuencia sus llamadas a Contenidos Conectados.
{% endalert %}

## Requisitos previos

| Requisito| Descripción|
| ---| ---|
|Cuenta Transifex | Se necesita una [cuenta Transifex](https://www.transifex.com/signin/) para beneficiarse de esta asociación. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

La integración de Transifex utiliza la [API de traducción de recursos](https://developers.transifex.com/reference/get_resource-translations) de Transifex. El siguiente cURL te permitirá ver si tu cuenta tiene valores de contenido asociados a traducciones. 

En primer lugar, introduce los datos `<ORGANIZATION_NAME>`, `<PROJECT_NAME>`, y `<RESOURCE_NAME>` que se encuentran en tu cuenta de Transifex. A continuación, sustituya `<LANGUAGE>` por el código de idioma por el que desea filtrar las traducciones y `<TRANSIFEX_BEARER_TOKEN>` por su [token de portador](https://developers.transifex.com/reference/api-authentication) Transifex.

```
curl --request GET \
     --url 'https://rest.api.transifex.com/resource_translations?filter\[resource\]=o:<ORGANIZATION_NAME>:p:<PROJECT_NAME>:r:<RESOURCE_NAME>&filter\[language\]=l:<LANGUAGE>' \
     --header 'Accept: application/vnd.api+json' \
     --header 'Authorization: Bearer 1/<TRANSFIX_BEARER_TOKEN>'
```

Por ejemplo, si su proyecto Transifex se encuentra en `https://www.transifex.com/appboy-3/french2/french_translationspo/`, el `project_name` será "french2" y el `resource_name` será "french_translationspo".

## Ejemplo de mensaje de contenido conectado

Este fragmento de código de ejemplo utiliza la API de traducción de recursos de Transifex y el atributo `language` del usuario. En función de sus necesidades, puede realizar un bucle a través de los objetos de cadena y extraer el contenido pertinente utilizando el siguiente Liquid: `{{strings.data[X].attributes.strings.other}}`.

{% raw %}
```
{% assign organization = "<ORGANIZATION_NAME>" %}
{% assign project = "<PROJECT_NAME>" %}
{% assign resource = "<RESOURCE_NAME>" %}

{% if {{${language}}} == "en" or {{${language}}} == "it" or {{${language}}} == "de" or {{${language}}} == "another_language_you_support"  %}
{% connected_content
     https://rest.api.transifex.com/resource_translations?filter[resource]=o:{{organization}}:p:{{project}}:r:{{resource}}&filter[language]=l:{{${language}}}
     :method GET
     :headers {
       "Authorization": "Bearer <TRANSIFEX_BEARER_TOKEN>"
  }
     :accept application/vnd.api+json
     :save strings
%}
{% endif %}

{% if {{strings}} != null and {{strings.data[0].attributes.strings.other}} != "" and {{${language}}} != null %}
  {{strings.data[0].attributes.strings.other}}
{% else %}
  {% abort_message('null or blank') %}
{% endif %}
```
{% endraw %}


[16]: [success@braze.com](mailto:success@braze.com)
