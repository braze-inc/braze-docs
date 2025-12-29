---
nav_title: Mensajes de derecha a izquierda
article_title: Creación de mensajes de derecha a izquierda
page_order: 1
alias: /right_to_left_messages/
page_type: reference
description: "En esta página se describen las mejores prácticas para elaborar mensajes en Braze que se lean de derecha a izquierda."
---

# Crear mensajes de derecha a izquierda

> El aspecto final de los mensajes de derecha a izquierda depende en gran medida de cómo los rendericen los proveedores de servicios (como Apple, Android y Google). En esta página se describen las mejores prácticas para elaborar mensajes de derecha a izquierda, de modo que tus mensajes se muestren con la mayor precisión posible.

## Apariencia del mensaje

Cuando crees un mensaje de derecha a izquierda, ten en cuenta lo siguiente:

- **Apariencia en el panel de Braze:** Cuando aparece un mensaje en el dispositivo de un usuario, su apariencia viene determinada en gran medida por el sistema operativo y la configuración de idioma de su dispositivo, lo que significa que lo que ves en el panel no siempre es exacto al 100%.
- **Apariencia en el dispositivo:** Apple y Android tienen un control significativo sobre cómo se envían los mensajes, mientras que los proveedores de servicios de correo electrónico (ESP) tienen cierto control. La personalización del correo electrónico HTML en Braze puede ser más flexible; sin embargo, el mismo mensaje puede seguir mostrándose de forma diferente en distintos dispositivos en función de la configuración del usuario.

Además, comprueba la puntuación y los emojis para determinar si tu mensaje se está reproduciendo de forma estándar o de derecha a izquierda.

| Interpretación occidental estándar | Renderizado de derecha a izquierda |
|------------------|------------------------|
| Muestra el signo de exclamación y el emoji al **final** de las frases. | Muestra el signo de exclamación y el emoji al **principio** de la frase. |
| \![Un ejemplo de mensaje estándar de derecha a izquierda.]({% image_buster /assets/img/right-to-left/standard.png %}) | \![Un ejemplo de mensajes de izquierda a derecha.]({% image_buster /assets/img/right-to-left/right-to-left.png %}) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Crear un mensaje de derecha a izquierda

Para crear tu mensaje de derecha a izquierda en Braze:

1. Redacta tu mensaje estándar en el editor Braze.
2. Copia el texto del mensaje de Braze y, a continuación, utiliza una herramienta de localización para convertirlo en un mensaje de derecha a izquierda.
3. Vuelve a pegar tu mensaje convertido en Braze.
4. Comprueba el formato y la alineación del texto. Si estás creando un mensaje de correo electrónico de arrastrar y soltar o HTML, puedes hacerlo dentro del compositor. Si no, tendrás que utilizar otro procesador de textos.<br><br>Menú del editor de arrastrar y soltar con botón para alternar la alineación del texto entre derecha-izquierda e izquierda-derecha.]({% image_buster /assets/img/rtl_button.png %}){: style="max-width:50%;"}

## Consideraciones
 
### Notificaciones push largas

El método de copiar y pegar para mensajes push puede ser difícil de usar con notificaciones push más largas, porque el contenido más largo puede aparecer en varias líneas en un dispositivo móvil. Si copias el texto de tu mensaje desde fuera de Braze (como un documento de Word) y lo pegas directamente en Braze, la alineación de las frases y la colocación de las palabras pueden cambiar. Para evitarlo, copia y pega por partes y añade un salto de línea. Por ejemplo, copia y pega las cinco primeras palabras, añade un salto de línea, copia las cinco palabras siguientes, añade un salto de línea, etc.

Las funciones de vista previa y de prueba están diseñadas para mensajes de izquierda a derecha, por lo que los mensajes de derecha a izquierda no se mostrarán correctamente en la sección de **prueba de la vista previa & **, pero se mostrarán correctamente en los dispositivos de usuario si sus ajustes están configurados para ello. Te sugerimos que te envíes mensajes a ti mismo en un entorno en vivo para confirmar que se muestran correctamente en función de la configuración del dispositivo.

### Texto bidireccional

Muchos usuarios que escriben en lenguas de derecha a izquierda están utilizando en realidad texto bidireccional: una combinación de lenguas de izquierda a derecha y de derecha a izquierda. Por ejemplo, un especialista en marketing puede enviar un mensaje en hebreo con el nombre de una empresa en inglés. Braze no puede manejar el formato del texto bidireccional. Dos formas de evitar problemas de formato son evitar por completo el texto bidireccional o separar el texto de izquierda a derecha del de derecha a izquierda mediante saltos de línea. 

{% alert tip %}
Un formato adecuado para el texto bidireccional es especialmente importante cuando se elaboran mensajes que incluyen códigos promocionales; los códigos promocionales suelen tener un formato de izquierda a derecha porque los mismos códigos pueden utilizarse en todos los mercados. Dos formas de acomodar los códigos promocionales son utilizar una imagen para el código promocional o añadir el código promocional al final del mensaje tras un salto de línea.
{% endalert %}

### Caracteres especiales, números y emojis

Los caracteres especiales (como puntuación, símbolos matemáticos y divisas), números, viñetas y emojis pueden "saltar" al elaborar mensajes de derecha a izquierda en Braze. Para evitarlo, escribe tu copia con el formato adecuado en un procesador de textos externo, y luego pega la copia en Braze. También puede ser útil evitar colocar los emojis al principio del texto y, en su lugar, separarlos (y los caracteres especiales y los números) del texto con saltos de línea para evitar problemas de alineación.

### Mensajes en árabe

Cuando redactes mensajes en árabe, utiliza tamaños de letra considerablemente más grandes para conseguir la misma legibilidad que lograrías con otros idiomas. Te sugerimos que utilices un tamaño de letra un 20% mayor que el habitual para las lenguas que utilizan el alfabeto latino o romano. Esto se debe a que las fuentes árabes se hacen pequeñas para acomodar el espacio vertical que ocupan los diacríticos (tildes).
