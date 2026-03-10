---
nav_title: "Tutorial: Restaurante de comida rápida"
article_title: Tutorial de Intelligence Suite
page_order: 10
search_rank: 12
description: "¿Nuevo en la Braze Intelligence Suite? Empieza con este tutorial."
tool:
  - Dashboard
---

# Tutorial de Intelligence Suite

> ¿Nuevo en la Braze Intelligence Suite? ¡Empieza con este tutorial! Para información más general, consulta [Intelligence Suite]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/).

## Tutorial: Restaurante de comida rápida

Imagina que trabajamos en SandwichEmperor, un restaurante de comida rápida con un nuevo artículo de menú por tiempo limitado: el Royal Roast. Usaremos dos funciones de la Intelligence Suite para enviar promociones personalizadas en un Canvas.

### Paso 1: Usar Intelligent Timing para cuándo enviar notificaciones

Usaremos Intelligent Timing para analizar las interacciones pasadas de nuestros usuarios con nuestra app y cada canal de mensajería, y luego seleccionar automáticamente el mejor momento para promocionar el Royal Roast a cada usuario. Algunos usuarios pueden recibir la promoción por la tarde y otros por la noche.

Proporcionaremos una hora de alternativa para usuarios sin suficientes interacciones pasadas para analizar: la hora más popular de uso de la app entre todos los usuarios.

![Configuración de envío de Intelligent Timing para un paso de mensaje.]({% image_buster /assets/img/intelligence_suite1.png %})

### Paso 2: Usar Intelligent Selection para elegir la promoción

Para los mensajes promocionales en sí, usaremos Intelligent Selection para probar tres mensajes distintos (notificación push, correo electrónico y SMS) para el Royal Roast. Intelligent Selection analizará el rendimiento de todos nuestros mensajes promocionales dos veces al día y enviará gradualmente más de los mejores mensajes y menos de los demás.

Cuando Intelligent Selection reúna suficientes datos para determinar el mejor mensaje, usará ese mensaje en el 100 % de los envíos futuros.

![Sección de pruebas A/B de un Canvas con Intelligent Selection activado.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

### Paso 3: Lanzar el Canvas

Con Intelligent Timing e Intelligent Selection, hemos configurado nuestras promociones Royal Roast para que estén optimizadas en momento y mensaje. Podemos lanzar nuestro Canvas y ver cómo los envíos se ajustan a las preferencias de los usuarios.
