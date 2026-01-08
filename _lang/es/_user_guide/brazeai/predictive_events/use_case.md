---
nav_title: Casos de uso
article_title: Caso de uso Predecir actualizaciones de suscripción
description: "Este ejemplo muestra cómo una marca ficticia utiliza los Eventos Predictivos de Braze para definir los resultados que importan a su negocio -como pasar a ser miembro profesional- y crear estrategias específicas que mejoren los resultados."
page_type: tutorial
---

# Casos de uso: Predecir las actualizaciones de suscripción con una orientación más inteligente

> Este ejemplo muestra cómo una marca ficticia utiliza los Eventos Predictivos de Braze para definir los resultados que importan a su negocio -como pasar a ser miembro profesional- y crear estrategias específicas que mejoren los resultados. 

Digamos que Jordan es estratega del ciclo de vida de Steppington, una aplicación de salud y fitness con niveles gratuitos y de pago. El equipo de Jordan tiene el objetivo de aumentar las actualizaciones del plan Pro sin bombardear a toda su base de usuarios gratuitos con mensajes de descuento. Actualmente, envían una promoción "Prueba Pro con un 50% de descuento" a todos los usuarios de la capa gratuita al cabo de siete días. Aunque impulsa algunas conversiones (alrededor del 5% en 7 días), también da lugar a un alcance excesivo, incluyendo descuentos a usuarios que probablemente se actualizarían de todos modos.

Para mejorar la segmentación y reducir la fatiga de la mensajería, Jordan utiliza Eventos Predictivos para modelar la probabilidad de que un usuario pase a Pro en los próximos 7 días. Define un evento personalizado: `upgraded_to_pro`, y luego lo utiliza para entrenar un modelo de predicción y segmentar a los usuarios en grupos inteligentes y orientados a la acción. 

Este tutorial explica cómo creó Jordan:

- Un modelo de predicción para `upgraded_to_pro` en 7 días
- Segmentos que ayudan a aumentar las conversiones enviando menos mensajes en total

## Paso 1: Crear un modelo predictivo para las actualizaciones

Jordan empieza definiendo el resultado más importante para su estrategia de actualización: un usuario que pasa del nivel gratuito al Pro. En lugar de basarse en desencadenantes genéricos como "el tiempo transcurrido desde la inscripción", quiere prever qué usuarios tienen realmente probabilidades de convertirse. De este modo, su equipo puede actuar basándose en señales reales, no sólo en suposiciones.

1. En el panel de Braze, Jordan va a **Análisis** > **Eventos de predicción**.
2. [Crea una nueva predicción de evento]({{site.baseurl}}/user_guide/brazeai/predictive_events/creating_an_event_prediction/) y nómbrala "Pasar a Pro en 7 días".
3. Como evento de destino, selecciona su evento personalizado: `upgraded_to_pro`.
4. Jordan establece la ventana de predicción en 7 días, fija un calendario de actualización y crea la predicción.

\![Configuración de la predicción que muestra la definición, la ventana, la audiencia y el calendario de actualización de la predicción.]({% image_buster /assets/img/ai_use_cases/prediction_settings.png %})

## Paso 2: Segmenta a los usuarios en función de la probabilidad de actualización

Una vez completada la formación, Braze asigna una [Puntuación de Probabilidad de Suceso]({{site.baseurl}}/user_guide/brazeai/predictive_events/analytics/#purchase_score) (0-100) a cada usuario elegible. Jordan utiliza esta puntuación para crear segmentos procesables: uno para los usuarios de alta intención que quizá no necesiten un descuento, y otro para los usuarios que probablemente no se conviertan sin ayuda.

1. Jordan navega hasta Segmentos en Braze.
2. Crea dos [segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) utilizando el [filtro Puntuación de Probabilidad de Suceso]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#event-likelihood-score) y selecciona la predicción que ha creado. Los dos segmentos son:
  - **Probable mejora:** Puntuación superior al 70
  - **Necesita un empujón para actualizarse:** Puntuación superior a 40 e inferior a 70

{% alert tip %}
Los filtros de predicción pueden combinarse con cualquier otro atributo o comportamiento del usuario. Jordan planea refinar aún más estos segmentos basándose en los intereses de los usuarios, como dar prioridad a los usuarios que utilizan con frecuencia las características de seguimiento del estado físico. Esto le proporciona cuatro subgrupos a los que dirigirse con mayor precisión, permitiendo que el contenido y la mensajería se ajusten a las necesidades de cada usuario.
{% endalert %}

\![Creador de segmentos con dos filtros para la Puntuación de Probabilidad de Suceso.]({% image_buster /assets/img/ai_use_cases/event_likelihood_score.png %})

## Paso 3: Personalización de la mensajería por nivel de intención

Ahora que Jordan tiene claras las señales de intención de actualización -y subgrupos refinados basados en el comportamiento de los usuarios- construye una estrategia de mensajería que se adapta a lo que necesita cada usuario. Se acabaron las explosiones únicas para todos.

Elige el correo electrónico como canal principal para esta campaña. ¿Por qué? Porque Jordan quiere explicar el valor de Pro a los usuarios de alta intención y presentar un argumento convincente a los usuarios más indecisos: ambas cosas requieren espacio, elementos visuales y una fuerte CTA. El correo electrónico le da flexibilidad para hacerlo bien sin presionar a los usuarios, y le permite hacer un seguimiento del rendimiento a través del comportamiento de los clics.

Jordan [crea un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) que divide la experiencia en función de los segmentos que acaba de construir. Añade un paso de Rutas de audiencia a la audiencia objetivo:

- Usuarios de alta intención, centrados en el fitness
- Gran intención, otros usuarios
- Usuarios de baja intención, centrados en el fitness
- Baja intención, otros usuarios

\![Ruta de audiencia de Canvas con cuatro rutas para cada tipo de intención.]({% image_buster /assets/img/ai_use_cases/canvas_paths_by_intent.png %})

También establece el evento de conversión Canvas en el evento personalizado `upgraded_to_pro`, para que Braze realice un seguimiento automático de las conversiones de actualización a medida que los usuarios avanzan por el flujo.

### Ejemplo de mensajes por ruta

{% tabs %}
{% tab High intent, fitness %}

Estos usuarios ya son activos y tienen una gran interacción con las características del seguimiento del estado físico. Es probable que se actualicen sin incentivos adicionales, por lo que el mensaje se centra en desbloquear información más profunda y herramientas avanzadas que se basen en sus hábitos actuales.

- **Línea del asunto:** Llega más lejos con tus objetivos de fitness
- **Cabecera:** Tu progreso merece Pro
- **Cuerpo:** Ya has construido una rutina sólida. Con Pro, puedes ir más allá: realizar un seguimiento del progreso en todos los grupos musculares, establecer objetivos de rendimiento semanales y desbloquear análisis avanzados adaptados a cómo te mueves.
- **CTA:** Inicia tu prueba Pro gratuita

{% endtab %}
{% tab High intent, other %}
Estos usuarios muestran fuertes señales de interacción, como navegar por las características Pro o una actividad frecuente en la aplicación, pero no se centran específicamente en el seguimiento del estado físico. El mensaje destaca las ventajas más amplias de Pro, como la formación y la personalización, para animarles a superar la línea.

- **Línea del asunto:** Ya casi has llegado-Pro está listo cuando tú lo estés
- **Cabecera:** Desbloquea más formas de moverte
- **Cuerpo:** Has explorado lo que Pro puede ofrecerte. Ahora tienes la oportunidad de acceder a planes personalizados, contenidos de entrenamiento 1:1 y programas guiados creados para alcanzar tus objetivos únicos, ya sea fuerza, equilibrio o constancia.
- **CTA:** Inicia tu prueba Pro gratuita

{% endtab %}
{% tab Low intent, fitness %}
Estos usuarios se interesan por las características de fitness, pero no han tomado medidas para actualizarse. El mensaje se centra en sus intereses de fitness, al tiempo que reduce la fricción con una oferta por tiempo limitado, ayudándoles a ver Pro como una forma poco arriesgada de mejorar su rutina.

- **Línea del asunto:** ¿Preparado para entrenar de forma más inteligente? Prueba Pro con un 50% de descuento
- **Cabecera:** Tu mejora de entrenamiento te está esperando
- **Cuerpo:** Pro te ofrece todo lo que necesitas para empezar con fuerza: planes de entrenamiento fáciles de seguir, consejos de expertos y un seguimiento real del progreso. Pruébalo ahora con un 50% de descuento, y cancélalo cuando quieras.
- **CTA:** Consigue un 50% de descuento en Pro

{% endtab %}
{% tab Low intent, other %}

Estos usuarios muestran una interacción mínima en general. Es poco probable que se actualicen sin un incentivo convincente, así que el mensaje adopta un enfoque sencillo, centrado en las ventajas, con un descuento y un lenguaje suave para invitar a la exploración sin presiones.

- **Línea del asunto:** 50% de descuento en Pro sólo este fin de semana
- **Cabecera:** Listo cuando tú lo estés
- **Cuerpo:** Crea tu primer plan de fitness personalizado, sigue tus progresos y accede a entrenamientos exclusivos, todo por la mitad de precio. Prueba Pro por menos y cancélalo cuando quieras.
- **CTA:** Consigue un 50% de descuento en Pro

{% endtab %}
{% endtabs %}

## Paso 4: Mide los resultados y optimiza tu estrategia

Después de que se ejecute la campaña, Jordan revisa el rendimiento en [los análisis de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) para comprender qué tal funcionaron las rutas personalizadas y si la combinación de la intención predictiva con las señales de comportamiento mejoró las tasas de actualización.

Rendimiento del correo electrónico por ruta:

- **Alta intención, aptitud**
   - *Tarifa abierta:* 34%
   - *Tasa de clics:* 20%
   - *Tasa de conversión:* 13%
   - Sin descuento
- **Gran intención, otros**
   - *Tarifa abierta:* 30%
   - *Tasa de clics:* 17%
   - *Tasa de conversión:* 11%
   - Sin descuento
- **Baja intención, aptitud**
   - *Tarifa abierta:* 27%
   - *Tasa de clics:* 12%
   - *Tasa de conversión:* 8%
   - Oferta del 50% de descuento incluida
- **Baja intención, otros**
   - *Tarifa abierta:* 23%
   - *Tasa de clics:* 9%
   - *Tasa de conversión:* 6%
   - Oferta del 50% de descuento incluida

En comparación con la campaña anterior del equipo, de talla única (en la que un descuento general después de 7 días sólo producía un 5% de conversiones y un exceso de mensajería), el enfoque específico muestra un aumento significativo en todos los grupos, con mayor eficacia y menos descuentos innecesarios.

El [informe de embudo]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) también muestra una clara reducción del abandono en los pasos clave, sobre todo para los usuarios de baja intención que recibieron mensajería personalizada. Más usuarios abren, hacen clic y actualizan, lo que demuestra el valor de la orientación basada en la intención.

Jordania utiliza estas informaciones para:

- Explora las pruebas A/B sobre líneas del asunto y frases de CTA
- Reevaluar el umbral de descuento para los usuarios de intención media
- Sigue refinando los segmentos basándote en comportamientos adicionales, como la visualización de contenidos o el uso de características de la aplicación.

Gracias a los Eventos Predictivos y a la segmentación por capas, su equipo dispone ahora de una estrategia escalable que adapta la mensajería en función de la intención y el comportamiento del usuario, consiguiendo más actualizaciones y preservando la confianza en la marca.
