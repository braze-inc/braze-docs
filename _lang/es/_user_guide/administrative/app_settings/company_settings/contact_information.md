---
nav_title: Información de contacto
article_title: Información de contacto
page_order: 0
page_type: reference
description: "Este artículo de referencia contiene información importante para los administradores sobre la gestión de la información de contacto y la zona horaria de su empresa en Braze."

---

# Información de contacto

> Como administrador, puedes utilizar la página **Información de contacto** para administrar la información de contacto y la zona horaria de tu empresa en Braze.

Para acceder a esta página, vaya a **Configuración** > **Configuración de administración** > **Información de contacto**. Asegúrate de seleccionar **Guardar** para aplicar cualquier cambio antes de salir de la página.

## Consecuencias del cambio de huso horario

{% alert warning %}
El cambio de zona horaria puede provocar discrepancias en los datos en torno al periodo en que se produjo el cambio. Si cambias tu zona horaria, Braze hará todo lo posible por realizar la conversión con precisión, pero no garantiza una conversión perfecta. Es posible que note una discontinuidad en los datos, que pueden cambiar de una zona horaria a otra.
{% endalert %}

Si decide cambiar de zona horaria, puede sufrir diversas consecuencias, entre ellas:

- Aunque las campañas programadas para horas concretas en ubicaciones específicas (como las 21:00, hora del este) se ejecutarán correctamente según lo previsto hasta que se editen, tanto los análisis de campaña como la programación de futuras campañas se verán afectados por el cambio.
- Cualquier programación de tarjetas que no esté asignada a la hora local puede verse afectada, pudiendo aparecer las tarjetas activas como finalizadas o al revés.
- Los filtros de segmentación del tipo «Ha hecho X antes/después `Date`de» se ajustarán en cuanto al tiempo, ya que la fecha inicial ahora se localizará en la zona horaria predeterminada de tu espacio de trabajo (por ejemplo, hora del Pacífico).
