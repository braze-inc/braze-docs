---
nav_title: Lanza tu agente
article_title: Lanza tu agente
page_order: 4
description: "Aprende a iniciar tu agente BrazeAI Decisioning Studio Go y a configurar los informes Business as Usual (BAU) para comparar el rendimiento."
---

# Lanza tu agente

> Una vez que hayas conectado tus orígenes de datos, configurado la orquestación y diseñado tu agente, estarás listo para lanzarlo. Este artículo cubre la activación de tu agente y la configuración de los informes BAU opcionales.

## Poner en marcha tu agente

Tras completar todos los pasos de configuración en el portal Decisioning Studio Go:

1. Revisa la configuración de tu agente para asegurarte de que todos los ajustes son correctos.
2. Comprueba que tu integración CEP está activa y que la orquestación está lista.
3. Selecciona **Lanzar** (o una acción equivalente) en el portal Decisioning Studio Go para activar tu agente.

Una vez lanzado, tu agente
- Empieza a recibir datos de audiencia de tu CEP
- Empieza a hacer recomendaciones personalizadas para cada cliente
- Orquesta los envíos a través de tu CEP configurado
- Recoger datos de interacción para aprender y mejorar con el tiempo

## Configuración de los informes BAU

Por defecto, los informes del portal Decisioning Studio Go comparan el grupo Decisioning Studio Go con el grupo de control aleatorio. Si tienes una campaña Business as Usual (BAU) con la que te gustaría comparar, puedes configurar los informes BAU para ver los tres grupos en un solo lugar.

### Ventajas de los informes BAU

La principal ventaja de configurar los informes BAU es la aplicación del filtrado de clics no válidos de Decisioning Studio Go. Cuando se aplica a los tres grupos del experimento, permite la comparación más precisa y justa ("manzanas con manzanas") del rendimiento de los clics, al eliminar el ruido de:
- Clics sospechosos de la máquina
- Haz clic en el enlace cancelar suscripción

### Requisitos para los informes BAU

Antes de configurar los informes BAU, asegúrate de que se realiza una comparación entre el grupo de tratamiento BAU, el grupo de Decisioning Studio Go y el grupo de control aleatorio:

- **No hay solapamiento**: Ningún destinatario puede pertenecer a más de un grupo durante toda la duración del experimento
- **Asignación aleatoria**: Los destinatarios se asignan aleatoriamente a grupos sin ningún sesgo
- **Opciones iguales**: Cualquier opción disponible para el grupo BAU (creativa, frecuencia, tiempo, incentivo u oferta) está disponible para los grupos Decisioning Studio Go y Random Control

{% alert warning %}
Sin un diseño experimental "manzanas con manzanas", los informes BAU pueden ser confusos o engañosos.
{% endalert %}

### Información necesaria

Tras validar el diseño de tu experimento, reúne los siguientes datos para configurar los informes BAU:

**ID de campaña de tu CEP:**

| CEP | Tipos aceptados |
|-----|---------------|
| **Braze** | Campañas y Canvas |
| **Salesforce Marketing Cloud** | Sólo viajes |
| **Klaviyo** | Sólo flujos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

**ID de audiencia de tu CEP:**

| CEP | Tipos aceptados |
|-----|---------------|
| **Braze** | Sólo segmentos |
| **Salesforce Marketing Cloud** | Sólo extensiones de datos |
| **Klaviyo** | Sólo segmentos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Si no tienes una audiencia existente que haga un seguimiento de tu audiencia BAU, debes crear una.

### Consideraciones

- **Haz clic sólo en los KPI**: Al igual que Decisioning Studio Go en general, los informes BAU sólo cubren los KPI de clics, no los de conversión.
- **Limitaciones del Canvas**: Actualmente no podemos filtrar por ID de pasos en Canvas específicos. Los eventos de todos los pasos en Canvas se incluirán en los datos BAU. Esto puede invalidar las comparaciones con BAU si sólo deben incluirse determinados pasos en Canvas.

### Configuración de los informes BAU

Sigue las instrucciones de tu portal Decisioning Studio Go. Debes tener:
- Uno o más ID de campaña donde todas las comunicaciones son comunicaciones BAU
- Un ID de audiencia que hace un seguimiento diario de los destinatarios de la audiencia BAU

## Supervisar a tu agente

Tras la puesta en marcha, supervisa el rendimiento de tu agente en el portal Decisioning Studio Go:

- **Métricas de interacción**: Seguimiento de las tasas de clics en los grupos de experimentación
- **Progreso en el aprendizaje**: Observa cómo evolucionan las recomendaciones del agente a lo largo del tiempo
- **Comparaciones de grupos**: Compara el rendimiento de Decisioning Studio Go con Control Aleatorio y BAU (si está configurado)

{% alert tip %}
Deja pasar al menos 2-4 semanas de recopilación de datos antes de sacar conclusiones sobre el rendimiento. El agente necesita suficientes interacciones para aprender y optimizar eficazmente.
{% endalert %}

## Solución de problemas

Si tu agente no rinde como esperabas:

1. **Verifica la orquestación**: Confirma que tu integración CEP está activa, que las campañas y los viajes se están ejecutando y que no hay límites globales o reglas similares que interfieran con la orquestación.
2. **Comprueba el flujo de datos**: Confirma que los datos de audiencia y de interacción se recogen correctamente.
3. **Revisa los grupos de experimentación**: Asegúrate de que la asignación aleatoria sea correcta y de que no haya solapamiento entre los grupos.
4. **Contacta con el servicio de asistencia**: Ponte en contacto con el soporte de Braze para obtener más ayuda.
