---
nav_title: Migración de fuentes de datos a códigos promocionales
article_title: Migración de fuentes de datos a códigos promocionales
page_order: 0
description: "Este artículo de referencia proporciona orientación sobre la migración de fuentes de datos a códigos promocionales."
---

# Migración de fuentes de datos a códigos promocionales

{% alert note %}
Las fuentes de datos están en desuso. Braze recomienda a los clientes que utilicen fuentes de datos que se pasen a las listas de códigos promocionales.
{% endalert %}

> Esta página te guía en la migración de fuentes de datos a códigos promocionales. Se trata de un proceso sencillo que implica crear manualmente listas de códigos promocionales con la información de tus fuentes de datos y actualizar las referencias de tus mensajes en consecuencia.

## Características y funcionalidad

Hay algunas diferencias entre las listas de códigos promocionales y las fuentes de datos.

| Característica          | Códigos promocionales | Fuentes de datos   |
|------------------|-----------------|--------------|
| Descripciones     | Sí             | No           |
| Fechas de caducidad | Sí             | No           |
| Método de creación  | Cargar un CSV | Pegar texto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Cómo migrar

Para sustituir una Fuente de datos por una lista de códigos promocionales, haz lo siguiente: 

1. Ve a **Configuración de datos** y selecciona **Crear lista de códigos promocionales**.
2. [Configura tu lista de códigos promocionales]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes).
3. Navega hasta tus mensajes que anteriormente hacían referencia a la Fuente de datos y actualízalos para utilizar la lista de códigos promocionales.