---
nav_title: Inicia tu agente
article_title: Inicia tu agente
page_order: 4
description: "Aprende a iniciar tu agente BrazeAI Decisioning Studio Go y a configurar los informes Business as Usual (BAU) para comparar el rendimiento."
---

# Inicia tu agente

> Una vez que hayas conectado tus orígenes de datos, configurado la orquestación y diseñado tu agente, estarás listo para comenzar. Este artículo trata sobre cómo activar tu agente y configurar los informes BAU opcionales.

## Lanzamiento de tu agente

Después de completar todos los pasos de configuración en el portal Decisioning Studio Go:

1. Revisa la configuración de tu agente para asegurarte de que todos los ajustes sean correctos.
2. Verifica que tu integración CEP esté activa y que la orquestación esté lista.
3. Selecciona **Iniciar** (o la acción equivalente) en el portal Decisioning Studio Go para activar tu agente.

Una vez iniciado, tu agente:
- Comienza a recibir datos de audiencia de tu CEP.
- Empieza a hacer recomendaciones personalizadas para cada cliente.
- Orchestrate envía a través de tu CEP configurado.
- Recopila datos sobre la interacción para aprender y mejorar con el tiempo.

## Configuración de informes BAU

De forma predeterminada, los informes del portal Decisioning Studio Go comparan el grupo Decisioning Studio Go con el grupo de control aleatorio. Si tienes una campaña habitual (BAU) con la que deseas comparar, puedes configurar los informes BAU para ver los tres grupos en un solo lugar.

### Ventajas de los informes BAU

La principal ventaja de configurar los informes BAU es la aplicación del filtrado de clics no válidos de Decisioning Studio Go. Cuando se aplica a los tres grupos del experimento, esto permite realizar una comparación del rendimiento de los clics más precisa y justa («comparando manzanas con manzanas»), ya que elimina el ruido procedente de:
- Sospecha de clics de máquina
- Clics en el enlace para cancelar la suscripción

### Requisitos para la presentación de informes BAU

Antes de configurar los informes BAU, asegúrate de que la comparación entre el grupo de tratamiento BAU, el grupo Decisioning Studio Go y el grupo de control aleatorio sea equitativa:

- **Sin solapamiento**: Ningún destinatario puede pertenecer a más de un grupo durante toda la duración del experimento.
- **Asignación aleatoria**: Los destinatarios son asignados aleatoriamente a grupos sin sesgos.
- **Opciones iguales**: Todas las opciones disponibles para el grupo BAU (creatividad, frecuencia, tiempo, incentivos u ofertas) están disponibles para los grupos Decisioning Studio Go y de control.

{% alert warning %}
Sin un diseño experimental que permita comparar cosas similares, los informes BAU pueden resultar confusos o engañosos.
{% endalert %}

### Información requerida

Después de validar el diseño de tu experimento, recopila los siguientes datos para configurar los informes BAU:

**ID de campaña de tu CEP:**

| CEP | Tipos aceptados |
|-----|---------------|
| **Braze** | Campañas y Canvas |
| **Salesforce Marketing Cloud** | Solo viajes |
| **Klaviyo** | Solo flujos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

**ID de audiencia de tu CEP:**

| CEP | Tipos aceptados |
|-----|---------------|
| **Braze** | Solo segmentos |
| **Salesforce Marketing Cloud** | Solo extensiones de datos |
| **Klaviyo** | Solo segmentos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Si no tienes una audiencia existente que realice el seguimiento de tu audiencia BAU, debes crear una.

### Consideraciones

- **Solo haz clic en los KPI**: Al igual que Decisioning Studio Go en general, los informes BAU solo cubren los KPI de clics, no los KPI de conversión.
- **Limitaciones del Canvas**: Actualmente no admitimos el filtrado por ID de pasos específicos en Canvas. Los eventos de todos los pasos en Canvas se incluirán en los datos BAU. Esto puede invalidar las comparaciones con el BAU si solo se incluyen determinados pasos en Canvas.

### Configuración de informes BAU

Sigue las instrucciones del portal Decisioning Studio Go. Debes tener:
- Uno o más ID de campaña en los que todas las comunicaciones son comunicaciones BAU.
- Un ID de audiencia que realiza un seguimiento diario de los destinatarios de la audiencia BAU.

## Supervisión de tu agente

Después del lanzamiento, supervisa el rendimiento de tu agente en el portal Decisioning Studio Go:

- **Métricas de interacción**: Realiza un seguimiento de las tasas de clics en los grupos del experimento.
- **Progreso en el aprendizaje**: Observa cómo evolucionan las recomendaciones del agente a lo largo del tiempo.
- **Comparaciones entre grupos**: Compara el rendimiento de Decisioning Studio Go con el control aleatorio y BAU (si está configurado).

{% alert tip %}
Espera al menos entre dos y cuatro semanas para la recopilación de datos antes de sacar conclusiones sobre el rendimiento. El agente necesita suficientes interacciones para aprender y optimizarse de manera eficaz.
{% endalert %}

## Solución de problemas

Si tu agente no está rindiendo como esperabas:

1. **Verificar la orquestación**: Confirma que tu integración CEP está activa, que las campañas y los recorridos se están ejecutando y que no hay límites globales ni reglas similares que interfieran en la orquestación.
2. **Comprueba el flujo de datos**: Confirma que los datos sobre la audiencia y la interacción se están recopilando correctamente.
3. **Revisar los grupos experimentales**: Asegúrate de que la asignación aleatoria sea adecuada y de que no haya solapamientos entre los grupos.
4. **Contactar con el servicio de asistencia**: Ponte en contacto con el soporte de Braze para obtener más ayuda.
