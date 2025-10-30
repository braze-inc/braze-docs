---
nav_title: Casos de uso
article_title: Caso de uso REDUCIR TASA DE ABANDONOS CON CONTENIDO A TIEMPO
description: "Este ejemplo muestra cómo una marca ficticia utiliza Predictive Churn para reducir proactivamente el abandono de usuarios."
page_type: tutorial
---

# Casos de uso: REDUCIR TASA DE ABANDONOS con la reactivación oportuna del contenido

> Este ejemplo muestra cómo una marca ficticia utiliza Predictive Churn para reducir proactivamente el abandono de usuarios. En lugar de esperar a que se produzca el abandono, predice qué usuarios están en riesgo y entrégales mensajes personalizados mientras siguen activos.

Digamos que Camila es administradora de CRM en MovieCanon, una plataforma de streaming de películas independientes, documentales y series internacionales.

El equipo de Camila ha detectado una tendencia preocupante: los usuarios se registran, ven una o dos películas y luego desaparecen. Históricamente, han intentado enviar un correo electrónico genérico "Te echamos de menos" una semana después, pero con una tasa de conversión de sólo el 3%, es demasiado poco y demasiado tarde. La mayoría de los usuarios no vuelven a interactuar, y el abandono es inevitable.

Camila quiere cambiar eso. En lugar de reaccionar al abandono después de que se produzca, utiliza Predictive Churn para identificar a los usuarios que probablemente quedarán inactivos en los próximos 14 días, lo que da a su equipo la oportunidad de reactivar la interacción de las personas mientras siguen activas.

Este tutorial explica cómo funciona Camila:

- Crea un modelo de predicción del abandono basado en el comportamiento de los usuarios
- Segmenta a los usuarios por nivel de riesgo
- Crea una campaña de reactivación de la interacción adaptada a las personas de mayor riesgo.
- Evalúa el impacto mediante análisis de campaña

## Paso 1: Crear un modelo de predicción del abandono de clientes

Camila empieza modelando el resultado que quiere evitar: que los usuarios se vuelvan inactivos. Para MovieCanon, el abandono significa no iniciar un flujo en 14 días, así que ése es el comportamiento que quiere predecir.

1. En el panel de Braze, Camila va a **Análisis** > Predictive Churn.
2. Crea una nueva predicción de abandono y nómbrala "Riesgo de abandono en 2 semanas".
3. Para definir el abandono, selecciona `do not` y el evento personalizado `stream_started`, que indica una interacción activa.
4. Establece la ventana de predicción en 14 días, lo que significa que el modelo identificará a los usuarios que probablemente pasen 14 días sin iniciar un nuevo flujo.

\![Definición de abandono que muestra el abandono definido como un usuario que no realiza un evento personalizado "stream_started" en los últimos 14 días.]({% image_buster /assets/img/ai_use_cases/churn_definition.png %})

{:start="5"}
5\. Selecciona una audiencia de predicción que incluya a todos los usuarios que hayan desencadenado eventos relevantes en los últimos 30 días, lo que proporciona al modelo suficiente comportamiento reciente del que aprender.
6\. Establece el programa de actualización de predicciones en semanal para que los resultados se mantengan actualizados.
7\. Selecciona **Crear predicción**.

A continuación, el modelo empieza a entrenarse, analizando comportamientos como las sesiones recientes, la frecuencia de visionado y las interacciones con el contenido para sacar a la luz patrones que predigan el abandono. Camila recibe un correo electrónico una hora después de que su predicción ha terminado el entrenamiento, así que lo abre en Braze y comprueba la puntuación de [calidad de la predicción]({{site.baseurl}}/user_guide/brazeai/predictive_events/analytics/#prediction_quality). Está etiquetado como "Bueno", lo que significa que es probable que las predicciones del modelo sean precisas y fiables. Confiada en el rendimiento del modelo, sigue adelante.

## Paso 2: Segmenta a los usuarios por riesgo de abandono

Cuando el modelo termina de entrenarse, Braze asigna a cada usuario elegible una [Puntuación de Riesgo de Abandono de]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/#churn_score) entre 0 y 100. 

Para determinar un umbral de partida para la segmentación, Camila utiliza el control deslizante de audiencia de predicción para previsualizar cuántos usuarios entran en cada rango de puntuación y lo precisa que es la predicción en ese nivel. Equilibra la cobertura y la precisión en función de los verdaderos positivos esperados. Basándose en esto, decide apuntar a puntuaciones de riesgo superiores a 70. 

1. Camila navega hasta Segmentos en Braze.
2. Crea un [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) utilizando el [filtro Puntuación de riesgo de abandono]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#churn-risk-score) y selecciona la predicción de abandono que ha creado:
   - **Es probable que abandonen:** Puntuación superior al 70

Filtrar por segmentos a los usuarios con una puntuación de riesgo de abandono superior a 70.]({% image_buster /assets/img/ai_use_cases/churn_risk_score.png %})

## Paso 3: Dirígete a usuarios de riesgo con contenidos recurrentes de reactivación de la interacción

Con su predicción y segmento listos, Camila configura una campaña recurrente que llega automáticamente a los usuarios que se ponen en riesgo cada semana.

1. Camila crea una campaña recurrente y habilita [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/), para que cada mensaje se entregue cuando cada usuario individual tenga más probabilidades de interactuar, en lugar de depender de un día y una hora fijos.
2. Se dirige al segmento "Probable abandono" que acaba de crear.
3. Configura el evento de conversión de la campaña en el evento personalizado `stream_started`, para hacer un seguimiento de cuántos usuarios vuelven realmente a ver el contenido.
4. Camila elige el correo electrónico como canal principal: le da espacio para destacar múltiples selecciones de contenido personalizado en un formato visualmente rico sin demasiada presión. El correo electrónico incluye:
   - Una lista de visionado personalizada basada en [recomendaciones de artículos de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/), seleccionada dinámicamente del catálogo de MovieCanon.
   - Una llamada a la acción que les lleve directamente a la aplicación.

Esto garantiza que, cada semana, MovieCanon llegue sólo a los usuarios que necesitan un empujoncito: sin exceso de mensajería ni conjeturas.

### Ejemplo de correo electrónico

- **Línea del asunto:** No dejes colgados estos títulos
- **Cabecera:** Tu próximo gran reloj te está esperando
- **Cuerpo:** ¿Hace tiempo que no le das al play? No te preocupes: hemos preparado unas cuantas opciones para ti. Desde thrillers de acción lenta a documentales premiados, aquí hay algo que lleva tu nombre.
- **CTA:** Ver más selecciones

## Paso 4: Medir el rendimiento

Al cabo de unas semanas, Camila comprueba [los análisis de]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/) su [campaña]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/) para evaluar el rendimiento de la estrategia. 

Ella ve:

- *Tarifa abierta:* 31%
- *Tasa de clics:* 15%
- *Tasa de conversión* (flujo iniciado en 48 horas): 11%

En comparación con la antigua campaña "Te echamos de menos" (en la que las tasas de conversión rondaban el 3%), este nuevo flujo reduce el abandono en el grupo objetivo en un 28%. Indaga en el [informe de embudo]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) para detectar dónde abandonan los usuarios. Aunque las tasas de clics y de apertura son altas, nota una ligera fricción entre los clics y la conversión, lo que le lleva a plantearse probar el texto de la CTA o experimentar con el diseño.

Para comprender el impacto a largo plazo, Camila también hace un seguimiento del volumen de usuarios que entran en el segmento de "Probables abandonos" semana tras semana. Esto le ayuda a evaluar la salud general del ciclo de vida e informar la estrategia de retención a un nivel más amplio. Por último, vuelve a visitar la página [Análisis de predicciones]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) de su predicción de abandono para comparar las predicciones con los usuarios que abandonan, una comprobación útil para asegurarse de que el modelo está rindiendo como se esperaba.

Basándose en esta información, Camila planea hacer pruebas A/B de las líneas del asunto, probar diferentes ventanas de tiempo y experimentar con formatos de contenido como recomendaciones de estilo carrusel en un mensaje dentro de la aplicación.

Con Predictive Churn, Intelligent Timing y la personalización basada en IA, el equipo de Camila no se limita a reaccionar ante el abandono, sino que se adelanta a él. Y su campaña se desarrolla silenciosamente en segundo plano, llegando a las personas adecuadas, en el momento adecuado, con contenidos que realmente les interesan.
