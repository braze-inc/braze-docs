---
nav_title: Sheetlabs
article_title: Sheetlabs
description: "Este artículo de referencia describe la asociación entre Braze y Sheetlabs, un servicio que le permite personalizar sus campañas de marketing con datos procedentes de hojas de cálculo."
alias: /partners/sheetlabs/
page_type: partner
search_tag: Partner
---

# Sheetlabs

> [Sheetlabs](https://sheetlabs.com/) es una plataforma que permite convertir hojas de cálculo en API potentes y bien documentadas. Puedes importar datos de Google Sheets o Excel, convertirlos en una API y luego utilizar esa API en otras aplicaciones, como Braze.
_Esta integración está mantenida por Sheetlabs._

## Sobre la integración

La integración de Sheetlabs y Braze le permite aprovechar [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/) para incluir las API de Sheetlabs en sus campañas de marketing Braze. Se suele utilizar para establecer un puente entre una hoja de cálculo de Google (que el equipo de marketing actualiza directamente) y las plantillas de Braze. Esto le permite conseguir más con las plantillas Braze, como traducciones o conjuntos más amplios de atributos personalizados.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Sheetlabs | Para beneficiarse de esta colaboración es necesario disponer de una [cuenta en Sheetlabs](https://sheetlabs.com/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

La integración de Braze y Sheetlabs le permite lograr los siguientes casos de uso:

1. **Separar el acceso del especialista en marketing del acceso a la campaña Braze**: Algunos equipos desean evitar dar a todo el personal acceso para configurar directamente las plantillas y el contenido de Braze. En su lugar, quieren que el personal actualice el contenido de marketing en una hoja de cálculo. Sheetlabs sirve de puente entre las hojas de cálculo y Braze y puede actualizarse en tiempo real.
2. **Traducciones**: Las plantillas Braze no admiten traducciones de forma nativa. Si deseas admitir varias lenguas, debes crear varias plantillas. Al utilizar Sheetlabs junto con Braze, puede tener una única plantilla Braze traducida a varios idiomas.
3. **Ampliación de los atributos personalizados**: Braze proporciona un cierto número de atributos personalizados que pueden configurarse. Al utilizar Sheetlabs junto con Braze, puede añadir atributos personalizados adicionales más allá de esta asignación inicial.

Consulte [Sheetlabs](https://app.sheetlabs.com/docs/producers/braze/) para obtener más información sobre estos casos de uso.

## Integración

### Paso 1: Importe su hoja de cálculo a Sheetlabs

En Sheetlabs, cargue una hoja de cálculo de Excel o vincule su cuenta de Google e importe una hoja de Google. 

- Para importar una hoja de cálculo de Excel, haga clic en **Tablas de datos** en la barra de menús y, a continuación, en **Importar desde CSV/Excel**.
- Para importar desde Google Sheets, haz clic en **Tablas de datos** en la barra de menús y, a continuación, en **Importar desde Google**. A continuación, tendrás que proporcionar tus credenciales de acceso a Google e importar la hoja.

También puede optar por mantener su Hoja de Google sincronizada, lo que significa que Sheetlabs obtendrá automáticamente los datos más recientes de su Hoja de Google cuando cambien.

Asegúrate de incluir el ID de usuario Braze en tu hoja de cálculo o cualquier otra cosa que puedas utilizar como búsqueda más adelante.

### Paso 2: Crear una API en Sheetlabs

A continuación, en Sheetlabs, vaya a **APIs > Crear API**, y dé un nombre a su API. Es probable que desee permitir consultas a través de un campo de búsqueda de su hoja de cálculo, como el ID de usuario Braze.

En este punto, deberías poder acceder a tu API con un enlace como:<br> [`https://sheetlabs.com/ACME/email1_translations?country=en`](https://sheetlabs.com/ACME/email1_translations?country=en).

### Paso 3: Utilizar la API en el contenido conectado Braze

Ahora que tu API es accesible, puedes utilizarla en tus llamadas a Contenido conectado. He aquí un ejemplo de lo que podría ser una plantilla de traducción:

{% raw %}
```js
{% connected_content https://sheetlabs.com/ACME/email1_translations?country={{${country}}} :save translations %}

{{translations[0].greeting}} {{${first_name}}},

{{translations[0].message_body}}
```
{% endraw %}
{% alert tip %}
Para más ejemplos y consejos sobre la integración con Sheetlabs, consulte [la documentación de Sheetlabs](https://app.sheetlabs.com/docs/producers/braze/).
{% endalert %}
