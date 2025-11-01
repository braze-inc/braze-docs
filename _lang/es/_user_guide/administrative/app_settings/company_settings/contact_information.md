---
nav_title: Información de contacto
article_title: Información de contacto
page_order: 0
page_type: reference
description: "Este artículo de referencia contiene información importante para administradores sobre cómo gestionar la información de contacto y la zona horaria de tu empresa en Braze."

---

# Información de contacto

<style>
.fa-crown {
  color: gold;
}
</style>

> Esta página contiene información importante para los administradores sobre cómo gestionar la información de contacto y la zona horaria de tu empresa en Braze.

Para acceder a esta página, ve a **Configuración** > **Configuración de administración** > **Información de contacto**.

En esta página puedes gestionar la información de contacto y la zona horaria de tu empresa. Asegúrate de seleccionar **Guardar** antes de salir de la página.

## Consecuencias de cambiar de huso horario

{% alert warning %}

El cambio de zona horaria puede causar algunas discrepancias de datos alrededor del punto en que se cambió la zona horaria. Si alguien cambia de huso horario, hacemos un esfuerzo de buena fe para convertir las cosas con precisión, pero no siempre es una conversión perfecta. Puede que notes una discontinuidad en tus datos, en los que puede cambiar entre zonas horarias.

{% endalert %}

Si decides cambiar de zona horaria, puedes sufrir diversas consecuencias, entre ellas

- Aunque las campañas programadas para horas concretas en ubicaciones específicas (como las 21:00, hora del este) se ejecutarán correctamente según lo previsto hasta que se editen, tanto los análisis de campaña como la programación de futuras campañas se verán afectados por el cambio.
- Cualquier programación de tarjetas que no esté asignada a la hora local puede verse afectada, pudiendo aparecer tarjetas activas como finalizadas o al revés.
- Los filtros de segmentación de la forma "Ha hecho X antes/después de `Date`" tendrán la hora ajustada porque la fecha inicial estará ahora localizada en la hora del Pacífico.