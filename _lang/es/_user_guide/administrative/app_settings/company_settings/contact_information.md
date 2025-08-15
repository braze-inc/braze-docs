---
nav_title: Información de contacto
article_title: Información de contacto
page_order: 0
page_type: reference
description: "Este artículo de referencia contiene información importante para los administradores sobre la gestión de la información de contacto y la zona horaria de su empresa en Braze."

---

# Información de contacto

<style>
.fa-crown {
  color: gold;
}
</style>

> Esta página contiene información importante para los administradores sobre la gestión de la información de contacto y la zona horaria de su empresa en Braze.

Para acceder a esta página, vaya a **Configuración** > **Configuración de administración** > **Información de contacto**.

En esta página puede gestionar la información de contacto y la zona horaria de su empresa. Asegúrate de pulsar **Guardar** antes de salir de la página.

## Consecuencias del cambio de huso horario

{% alert warning %}

El cambio de zona horaria puede causar algunas discrepancias en los datos en torno al momento en que se cambió la zona horaria. Si alguien cambia de huso horario, hacemos un esfuerzo de buena fe para convertir las cosas con precisión, pero no siempre es una conversión perfecta. Es posible que note una discontinuidad en los datos, que pueden cambiar de una zona horaria a otra.

{% endalert %}

Si decide cambiar de zona horaria, puede sufrir diversas consecuencias, entre ellas:

- Aunque las campañas programadas para horas concretas en ubicaciones específicas (como las 21:00, hora del este) se ejecutarán correctamente según lo previsto hasta que se editen, tanto los análisis de campaña como la programación de futuras campañas se verán afectados por el cambio.
- Cualquier programación de tarjetas que no esté asignada a la hora local puede verse afectada, pudiendo aparecer las tarjetas activas como finalizadas o al revés.
- Los filtros de segmentación de la forma "Ha hecho X antes/después de `Date`" tendrán la hora ajustada porque la fecha inicial estará ahora localizada en la hora del Pacífico.