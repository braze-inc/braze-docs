---
nav_title: Seguimiento de sesiones
article_title: Sesiones de seguimiento para Windows Universal
platform: Windows Universal
page_order: 0
description: "Este artículo de referencia explica cómo hacer un seguimiento de las sesiones en la plataforma Windows Universal."
hidden: true
---

# Análisis
{% multi_lang_include archive/windows_deprecation.md %}

## Seguimiento de la sesión

El SDK de Braze genera datos de sesión que utiliza el panel de Braze para calcular la interacción del usuario y otros análisis esenciales para comprender a tus usuarios. Basándose en la siguiente semántica de sesión, nuestro SDK genera puntos de datos de "inicio de sesión" y "cierre de sesión" que tienen en cuenta la duración de la sesión y los recuentos de sesiones visibles en el panel de Braze.

### Ciclo de vida de la sesión

Nuestra integración de Windows registra la sesión que se abre cuando se inicia la aplicación y registra la sesión que se cierra cuando se cierra la aplicación. El valor mínimo de `sessionTimeoutInSeconds` es 1 segundo. Si necesitas forzar una nueva sesión, puedes hacerlo cambiando de usuario.

### Probar el seguimiento de la sesión

Para detectar sesiones a través de tu usuario, búscalo en el panel y ve a "Uso de la aplicación" en el perfil de usuario. Puedes confirmar que el seguimiento de sesiones funciona comprobando que la métrica "Sesiones" aumenta cuando cabría esperar.

![Un perfil de usuario que muestra el uso de la aplicación en 25 sesiones, utilizada por última vez hace dos horas y utilizada por primera vez hace veinte días.]({% image_buster /assets/img_archive/test_session.png %})


