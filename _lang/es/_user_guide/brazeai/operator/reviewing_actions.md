---
nav_title: Revisar acciones
article_title: Revisión de las acciones de BrazeAI Operator<sup>TM</sup>
page_order: 2
description: "Aprende a revisar y aprobar acciones cuando BrazeAI Operator proponga cambios en el dashboard."
---

# Revisión de las acciones de BrazeAI Operator

> Aprende a revisar y aprobar acciones cuando BrazeAI Operator<sup>TM</sup> proponga cambios en el dashboard.

![Operator presentando tarjetas de acciones sugeridas para su revisión.]({% image_buster /assets/img/operator/suggested_actions.png %}){: style="max-width:40%; border:none; float:right; margin-left:15px;"}

## Cómo funcionan las tarjetas de acción

Cuando Operator propone cambios en el dashboard (como rellenar campos de formularios, actualizar la configuración o generar imágenes), presenta cada cambio como una tarjeta de acción para su revisión.

1. **Operator resume el plan:** Operator explica lo que planea hacer antes de mostrar las tarjetas de acción.
2. **Aparecen las tarjetas de acción individuales:** Cada cambio propuesto se presenta en una tarjeta independiente que muestra lo que Operator quiere cambiar o hacer en el dashboard. En el caso de cambios en valores existentes, se muestran uno al lado del otro el valor anterior y el valor propuesto para que puedas compararlos.
3. **Revisar y aprobar:** Revisa cada tarjeta y apruébala o recházala.
4. **La acción se ejecuta:** Las acciones aprobadas se ejecutan en Braze. Las acciones rechazadas no se aplican.

Si una acción falla después de su aprobación, Operator te notificará con detalles sobre el fallo.

### Disponibilidad

Las tarjetas de acción son compatibles con los siguientes editores y páginas. 

- **Editores de mensajes:**
    - Mensajes dentro de la aplicación (solo editor tradicional)
    - Tarjetas de contenido
    - Correo electrónico (solo editor HTML)
    - Notificaciones push
    - SMS/MMS/RCS
    - Webhooks
- Página [Crear agente personalizado]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
 
En otras páginas, Operator proporciona una lista de pasos a seguir en la interfaz de usuario en lugar de realizar la acción por sí mismo. La funcionalidad de Operator se mejora periódicamente y se espera ampliar la cobertura de las herramientas de creación.

## Modificar un plan

Para modificar el plan de Operator, primero aprueba o rechaza las acciones pendientes. A continuación, describe el cambio deseado en un nuevo mensaje de chat.

Las acciones aprobadas no se pueden deshacer a través de Operator. Describe el nuevo cambio a Operator o realiza los cambios manualmente en el dashboard.

## Aprobación automática de acciones

El conmutador **Aprobación automática de acciones** se encuentra en el panel de chat de Operator.

- **Activado:** Las acciones sugeridas por Operator se ejecutan inmediatamente sin necesidad de aprobación manual. Algunas acciones aún requieren una aprobación explícita por motivos de seguridad, como la generación de imágenes o la realización de modificaciones en la configuración a nivel de espacio de trabajo.
- **Desactivado (predeterminado):** Todas las acciones propuestas siguen el proceso de revisión manual descrito.

![El conmutador de aprobación automática y el modal de confirmación en el panel de chat de Operator.]({% image_buster /assets/img/operator/auto-approval_toggle.png %}){: style="max-width:50%;"}

La aprobación automática se restablece cuando actualizas la página, abres una nueva pestaña o cierras sesión y vuelves a iniciarla. Navegar entre páginas en el dashboard no la restablece. La aprobación automática se puede desactivar en cualquier momento.