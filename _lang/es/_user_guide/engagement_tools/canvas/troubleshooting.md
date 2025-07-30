---
nav_title: Solución de problemas
article_title: Lienzos de solución de problemas
page_order: 11
page_type: reference
description: "Esta página proporciona pasos para la solución de problemas con los Lienzos."
tool: Canvas
---

# Lienzos de solución de problemas

> Esta página te ayuda a solucionar problemas con tus Lienzos.

## ¿Por qué un usuario no ha recibido un paso en Canvas desencadenado?

Primero, confirma que el evento personalizado se está pasando a Braze. Ve a **Análisis** > **Informe de eventos personalizados** y, a continuación, selecciona el evento personalizado y el intervalo de fechas correspondientes. Si el evento no se muestra, confirma que se ha configurado correctamente y que el usuario ha realizado la acción correcta.

Si aparece el evento personalizado, soluciona el problema haciendo lo siguiente:

- Comprueba la descarga del perfil del usuario para confirmar que desencadenó el evento y cuándo lo hizo. Si se desencadenó el evento, compara la marca de tiempo de cuando se desencadenó el evento con la hora en que el Canvas salió en vivo. El evento puede haberse desencadenado antes de que el Canvas estuviera en vivo.
- Revisa los registros de cambios del Canvas y de cualquier segmento utilizado en la segmentación para determinar si el usuario estaba en el segmento cuando se desencadenó su evento personalizado. Si no estuvieran en el segmento, no habrían recibido el paso en Canvas.
- Comprueba si el usuario fue introducido en un grupo de control mediante segmentación y, en consecuencia, se le impidió recibir el paso en Canvas.
- Si hay un retraso programado, comprueba si el evento personalizado del usuario se desencadenó antes del retraso. Si el evento se hubiera desencadenado antes del retraso, no habrían recibido el paso en Canvas.

{% alert note %}
Los mensajes dentro de la aplicación sólo pueden ser desencadenados por eventos enviados a través del SDK, no de la API REST.
{% endalert %}