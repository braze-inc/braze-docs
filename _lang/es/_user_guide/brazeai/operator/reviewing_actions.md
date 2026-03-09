---
nav_title: Revisar acciones
article_title: Revisión de las acciones de BrazeAI Operator<sup>TM</sup>
page_order: 2
description: "Aprende a revisar y aprobar acciones cuando BrazeAI Operator proponga cambios en el panel."
---

# Revisión de las acciones de BrazeAI Operator

> Aprende a revisar y aprobar acciones cuando BrazeAI Operator<sup>TM</sup> proponga cambios en el panel.

![Operador presentando tarjetas de acciones sugeridas para su revisión.]({% image_buster /assets/img/operator/suggested_actions.png %}){: style="max-width:40%; border:none; float:right; margin-left:15px;"}

## Cómo funcionan las tarjetas de acción

Cuando el operador propone cambios en el panel (como rellenar campos de formularios, actualizar configuraciones o generar imágenes), presenta cada cambio como una tarjeta de acción para su revisión.

1. **El operador resume el plan:** El operador explica lo que planea hacer antes de mostrar las tarjetas de acción.
2. **Aparecen las tarjetas de acción individuales:** Cada cambio propuesto se presenta en una tarjeta independiente que muestra lo que el operador quiere cambiar o hacer en el panel. En el caso de los cambios en los valores existentes, se muestran uno al lado del otro el valor anterior y el valor propuesto para que puedas compararlos.
3. **Revisar y aprobar:** Revisa cada tarjeta y apruébala o recházala.
4. **La acción se ejecuta:** Las acciones aprobadas se ejecutan en Braze. Las acciones rechazadas no se aplican.

Si una acción falla después de su aprobación, el operador notificará los detalles del fallo.

### Disponibilidad

Las tarjetas de acción son compatibles con los siguientes editores:

- Mensajes dentro de la aplicación (solo editor tradicional)
- Tarjetas de contenido
- Correo electrónico (solo editor HTML)
- Notificaciones push
- SMS/MMS/RCS
- Webhooks

En otras páginas, el operador proporciona una lista de pasos a seguir en la interfaz de usuario en lugar de realizar la acción por sí mismo. La funcionalidad del operador se mejora periódicamente y se espera ampliar la cobertura de las herramientas de creación.

## Modificar un plan

Para modificar el plan del operador, primero aprueba o rechaza las acciones pendientes. A continuación, describe el cambio deseado en un nuevo mensaje de chat.

Las acciones aprobadas no se pueden deshacer a través del operador. Describe el nuevo cambio al operador o realiza los cambios manualmente en el panel.

## Aprobación automática de acciones

La ubicación de la opción **«Aprobación automática de acciones»** es en el panel de chat del operador.

- **En:** Las acciones sugeridas por el operador se ejecutan inmediatamente sin necesidad de aprobación manual. Algunas acciones aún requieren una aprobación explícita por motivos de seguridad, como la generación de imágenes o la realización de modificaciones en la configuración del espacio de trabajo.
- **Desactivado (predeterminado):** Todas las acciones propuestas siguen el proceso de revisión manual descrito.

![El botón para alternar la aprobación automática y el modal de confirmación en el panel de chat del operador.]({% image_buster /assets/img/operator/auto-approval_toggle.png %}){: style="max-width:50%;"}

La aprobación automática se restablece cuando actualizas la página, abres una nueva pestaña o cierras sesión y vuelves a iniciarla. Pasar de una página a otra en el panel no lo reinicia. La función de aprobación automática se puede desactivar en cualquier momento.
