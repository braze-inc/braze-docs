---
nav_title: Migración de fuentes de datos a códigos de promoción
article_title: Migración de fuentes de datos a códigos de promoción
page_order: 0
description: "Este artículo de referencia ofrece orientación sobre la migración de fuentes de datos a códigos promocionales."
---

# Migración de fuentes de datos a códigos de promoción

{% alert note %}
Las Fuentes de datos están obsoletas. Braze recomienda a los clientes que utilizan Data Feeds que se pasen a las listas de códigos promocionales.
{% endalert %}

> Esta página te guía en la migración de fuentes de datos a códigos promocionales. Se trata de un proceso sencillo que implica crear manualmente listas de códigos promocionales con la información de tus fuentes de datos y actualizar las referencias de tus mensajes en consecuencia.

## Características y funciones

Existen algunas diferencias entre las listas de códigos promocionales y los feeds de datos.

| Característica          | Códigos de promoción | Fuentes de datos   |
|------------------|-----------------|--------------|
| Descripciones     | Sí             | No           |
| Fechas de caducidad | Sí             | No           |
| Método de creación  | Cargar un CSV | Pegar texto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Cómo migrar

Para sustituir una fuente de datos por una lista de códigos de promoción, haga lo siguiente: 

1. Vaya a **Configuración de datos** y seleccione **Crear lista de códigos promocionales**.
2. [Configure su lista de códigos promocionales]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes).
3. Vaya a los mensajes que anteriormente hacían referencia a la fuente de datos y actualícelos para utilizar la lista de códigos promocionales.