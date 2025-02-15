---
nav_title: Prueba tu integración básica
article_title: Prueba tu integración básica para Android y FireOS
page_order: 1
platform: 
  - Android
  - FireOS
description: "Este artículo de referencia cubre cómo probar la integración básica para tu aplicación Android o FireOS."

---

# Prueba tu integración básica

> Este artículo de referencia cubre cómo probar la integración básica para tu aplicación Android o FireOS.

## Confirmar que el seguimiento de la sesión funciona

En este punto, deberías tener el seguimiento de sesiones funcionando en tu integración Braze. Para probarlo, ve a **Resumen**, selecciona tu aplicación en el menú desplegable del nombre de la aplicación seleccionada (predeterminado a "Todas las aplicaciones") y establece **Mostrar datos para** en "Hoy". A continuación, abre tu aplicación y actualiza la página: todas tus métricas principales deberían haber aumentado en 1.

![]({% image_buster /assets/img_archive/android_sessions.png %})

Debes seguir probando tu integración navegando por tu aplicación y asegurándote de que sólo se ha registrado una sesión. A continuación, deja la aplicación en segundo plano durante al menos 10 segundos y vuelve a ponerla en primer plano. Por defecto, se crea una nueva sesión si la aplicación pasa a primer plano después de haber estado en segundo plano o cerrada durante más de 10 segundos. Una vez hecho esto, confirma que se ha registrado otra sesión.

## Depuración del seguimiento de la sesión
Si el seguimiento de la sesión se comporta de forma inesperada, activa el [registro detallado]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/additional_customization_and_configuration/#enabling-logs) y observa tu aplicación mientras reproduces los pasos que desencadenan la sesión. Observa las declaraciones de Braze en el logcat para detectar dónde puedes haber pasado por alto el registro de las llamadas a `openSession` y `closeSession` en tus actividades.

