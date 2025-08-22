---
nav_title: Tellius
article_title: Tellius
alias: /partners/tellius/
description: "Este artículo de referencia describe la asociación entre Braze y Tellius, una plataforma de inteligencia de decisiones y analítica aumentada, que permite aprovechar los datos, sin depender de ingenieros de BI, para crear cuadros de mando y generar perspectivas para tomar mejores decisiones de marketing."
page_type: partner
search_tag: Partner

---

# Tellius

> [Tellius](https://www.tellius.com/), una plataforma de inteligencia para la toma de decisiones y analítica aumentada, le permite responder a preguntas de sus datos mediante búsquedas en lenguaje natural y profundizar para entender el "por qué" con perspectivas guiadas basadas en IA.

La integración de Braze y Tellius permite a los usuarios aprovechar los datos, sin depender de ingenieros de BI, para crear cuadros de mando y generar perspectivas que les permitan tomar mejores decisiones de marketing. Esta integración requiere que los datos de Braze se almacenen en Snowflake, donde Tellius puede conectarse directamente y realizar consultas con integración en modo directo.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Tellius | Se necesita una cuenta Tellius para beneficiarse de esta asociación. Puedes empezar tu recorrido Tellius con una [prueba gratuita](https://www.tellius.com/free-trial/)|
| Programa de intercambio de datos Snowflake | Para los clientes actuales de Snowflake, ponte en contacto con tu representante de Braze sobre el programa de Intercambio de Datos de Snowflake para transferir tus datos de Braze a tu instancia de Snowflake.|
| Cuenta Snowflake Reader | Si no es cliente de Snowflake, póngase en contacto con su representante de Braze para que le proporcione una cuenta de Snowflake Reader que le permita acceder a sus datos de Braze.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Obtener acceso a Braze a través de Snowflake

Braze almacena datos granulares de los clientes en Snowflake. Puedes aprovechar tus datos Braze para generar información a través del programa de intercambio de datos Braze Snowflake u obteniendo una cuenta de lector Snowflake. 

Sigue la [integración de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) para configurarlo. 

### Paso 2: Conectar los datos de Tellius a Braze en Snowflake

Conecte Tellius a los datos de Braze en Snowflake mediante uno de los siguientes métodos:

- Acceso directo: Para cargar datos en Tellius, sigue los pasos para [Cargar conjuntos de datos](https://help.tellius.com/article/jn6o59d5gk-load-datasets).
- Acceso OAuth: Para el acceso OAuth a Snowflake, sigue los pasos para la [autenticación OAuth](https://help.tellius.com/article/11517w63b6-oauth-authentication-for-snowflake).

### Paso 3: Crear Business View en Tellius a partir de los datos cargados

Para empezar a utilizar la búsqueda en lenguaje natural y la información automatizada, cree una [Business View](https://help.tellius.com/article/hy9yvh5tom-create-business-view) y seleccione conjuntos de datos de su conexión Snowflake.

### Paso 4: Saca el máximo partido a tus datos con Tellius

En Tellius, hay una interfaz guiada para que veas las características de la plataforma. Para más preguntas y guías, consulta su [base de conocimientos](https://help.tellius.com/).