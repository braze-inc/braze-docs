---
nav_title: Revisar acciones
article_title: Revisar acciones de BrazeAI Operator<sup>TM</sup>
page_order: 2
description: "Aprende a revisar y aprobar acciones cuando BrazeAI Operator propone cambios en el dashboard."
---

# Revisar acciones de BrazeAI Operator

> Aprende a revisar y aprobar acciones cuando BrazeAI Operator<sup>TM</sup> propone cambios en el dashboard.

![Operator mostrando tarjetas de acción sugeridas para revisión.]({% image_buster /assets/img/operator/suggested_actions.png %}){: style="max-width:40%; border:none; float:right; margin-left:15px;"}

## Cómo funcionan las tarjetas de acción

Cuando Operator propone cambios en el dashboard (por ejemplo, rellenar campos de formulario, actualizar configuraciones o generar imágenes), cada cambio se presenta como una tarjeta de acción para revisión.

1. **Operator resume el plan:** Operator explica lo que planea hacer antes de mostrar las tarjetas de acción.
2. **Aparecen tarjetas de acción individuales:** Cada cambio propuesto se presenta en una tarjeta separada que muestra qué quiere cambiar o hacer Operator en el dashboard. Para cambios en valores existentes, se muestran el valor anterior y el propuesto uno al lado del otro.
3. **Revisar y aprobar:** Revisa cada tarjeta y aprébala o recházala.
4. **La acción se ejecuta:** Las acciones aprobadas se ejecutan en Braze. Las acciones rechazadas no se aplican.

Si una acción falla después de la aprobación, Operator te lo notificará con detalles del fallo.

### Disponibilidad

Las tarjetas de acción son compatibles con los siguientes editores:

- Mensajes in-app (solo editor tradicional)
- Content Cards
- Email (solo editor HTML)
- Notificaciones push
- SMS/MMS/RCS
- Webhooks

En otras páginas, Operator proporciona una lista de pasos a seguir en la interfaz en lugar de ejecutar las acciones por sí mismo. La funcionalidad de Operator se mejora con regularidad y se espera una cobertura ampliada de las herramientas de creación.

## Modificar un plan

Para modificar el plan de Operator, primero aprueba o rechaza las acciones pendientes. Luego describe el cambio deseado en un nuevo mensaje de chat.

Las acciones aprobadas no se pueden deshacer mediante Operator. Describe el nuevo cambio a Operator o haz los cambios manualmente en el dashboard.

## Aprobación automática de acciones

El botón **Aprobación automática de acciones** está en el panel de chat de Operator.

- **Activado:** Las acciones sugeridas por Operator se ejecutan de inmediato sin aprobación manual. Algunas acciones siguen requiriendo aprobación explícita por seguridad, como generar imágenes o modificar configuraciones a nivel de espacio de trabajo.
- **Desactivado (por defecto):** Todas las acciones propuestas siguen el proceso de revisión manual descrito.

![El botón de aprobación automática y el modal de confirmación en el panel de chat de Operator.]({% image_buster /assets/img/operator/auto-approval_toggle.png %}){: style="max-width:50%;"}

La aprobación automática se restablece al actualizar la página, abrir una nueva pestaña o cerrar sesión y volver a iniciarla. Cambiar de página en el dashboard no la restablece. Puedes desactivar la aprobación automática en cualquier momento.
