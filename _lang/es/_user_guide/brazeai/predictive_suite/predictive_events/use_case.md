---
nav_title: Casos de uso
article_title: "Caso de uso: predicción de las actualizaciones de suscripciones"
description: "Este ejemplo muestra cómo una marca ficticia utiliza Braze Predictive Events para definir los resultados que son importantes para su negocio, como la actualización a una suscripción profesional, y crear estrategias específicas que mejoren los resultados."
page_type: tutorial
---

# Casos de uso: Predice las mejoras de suscripción con una segmentación más inteligente.

> Este ejemplo muestra cómo una marca ficticia utiliza Braze Predictive Events para definir los resultados que son importantes para su negocio, como la actualización a una suscripción profesional, y crear estrategias específicas que mejoren los resultados. 

Supongamos que Jordan es estratega de ciclo de vida en Steppington, una aplicación de salud y fitness con niveles gratuitos y de pago. El equipo de Jordan tiene el objetivo de aumentar las actualizaciones al plan Pro sin bombardear a toda tu base de usuarios gratuitos con mensajes de descuento. Actualmente, envían una promoción de «Prueba Pro con un 50 % de descuento» a todos los usuarios del nivel gratuito después de siete días. Aunque genera algunas conversiones (alrededor del 5 % en 7 días), también da lugar a un alcance excesivo, incluyendo descuentos para usuarios que probablemente hubieran actualizado de todos modos.

Para mejorar la segmentación y reducir la fatiga de la mensajería, Jordan utiliza Predictive Events para modelar la probabilidad de que un usuario se actualice a Pro en los próximos 7 días. Define un evento personalizado: `upgraded_to_pro`, y luego lo utiliza para entrenar un modelo de predicción y realizar la segmentación de los usuarios en grupos inteligentes y orientados a la acción. 

Este tutorial explica cómo Jordan creó:

- Un modelo de predicción para`upgraded_to_pro`  en un plazo de 7 días.
- Segmentos que ayudan a aumentar las conversiones y a enviar menos mensajes en total.

## Paso 1: Crear un modelo de predicción para las actualizaciones.

Jordan comienza definiendo el resultado más importante para su estrategia de actualización: que un usuario pase del nivel gratuito al Pro. En lugar de basarse en factores desencadenantes genéricos como «tiempo desde el registro», quiere pronosticar qué usuarios son realmente propensos a convertirse. De esta manera, tu equipo puede actuar basándose en señales reales, no solo en suposiciones.

1. En el panel de Braze, Jordan va a **Análisis** > **Eventos predictivos**.
2. [Crea una nueva predicción de evento]({{site.baseurl}}/user_guide/brazeai/predictive_events/creating_an_event_prediction/) y la llama «Actualización a Pro en 7 días».
3. Como evento de destino, selecciona su evento personalizado: `upgraded_to_pro`.
4. Jordan establece el periodo de predicción en 7 días, configura un calendario de actualizaciones y crea la predicción.

![Configuración de predicciones que muestra la definición, la ventana, la audiencia y el calendario de actualización de la predicción.]({% image_buster /assets/img/ai_use_cases/prediction_settings.png %})

## Paso 2: Segmentar a los usuarios en función de la probabilidad de actualización.

Una vez completada la formación, Braze asigna una [puntuación de probabilidad de evento]({{site.baseurl}}/user_guide/brazeai/predictive_events/analytics/#purchase_score) (0-100) a cada usuario elegible. Jordan utiliza esta puntuación para crear segmentos procesables: uno para usuarios con alta intención de compra que quizá no necesiten un descuento, y otro para usuarios que probablemente no se conviertan sin ayuda.

1. Jordan navega hasta Segments (Segmentos) en Braze.
2. Crea dos [segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) utilizando el [filtro «Puntuación de probabilidad de evento»]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#event-likelihood-score) y selecciona la predicción que ha creado. Los dos segmentos son:
  - **Probabilidad de actualización:** Obtén una puntuación superior a 70.
  - **Necesita un empujón para actualizarse:** Obtén una puntuación superior a 40 e inferior a 70.

{% alert tip %}
Los filtros predictivos se pueden combinar con cualquier otro atributo o comportamiento de los usuarios. Jordan tiene previsto perfeccionar aún más estos segmentos en función de los intereses de los usuarios, por ejemplo, dando prioridad a los usuarios que utilizan con frecuencia las características de seguimiento de la actividad física. Esto te permite segmentar con mayor precisión cuatro subgrupos, lo que te permite adaptar el contenido y la mensajería a las necesidades de cada usuario.
{% endalert %}

![Generador de segmentos con dos filtros para la puntuación de probabilidad de eventos.]({% image_buster /assets/img/ai_use_cases/event_likelihood_score.png %})

## Paso 3: Personaliza la mensajería según el nivel de intención.

Ahora que Jordan tiene señales claras de intención de actualización, y subgrupos refinados basados en el comportamiento de los usuarios, crea una estrategia de mensajería que se adapta a las necesidades de cada usuario. Se acabaron los mensajes genéricos para todos.

Elige el correo electrónico como canal principal para esta campaña. ¿Por qué? Porque Jordan quiere explicar el valor de Pro a los usuarios con alta intención de compra y presentar argumentos convincentes a los usuarios más indecisos, lo que requiere espacio, elementos visuales y una llamada a la acción contundente. El correo electrónico te ofrece la flexibilidad necesaria para hacerlo bien sin presionar a los usuarios y te permite realizar el seguimiento del rendimiento a través del comportamiento de los clics.

Jordan [crea un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) que divide la experiencia en función de los segmentos que acaba de crear. Añade un paso de ruta de audiencia para orientar:

- Usuarios con mucha intención y centrados en el fitness
- Alta intención, otros usuarios
- Usuarios con poca intención y centrados en el fitness
- Baja intención, otros usuarios

![Canvas Ruta de audiencia con cuatro rutas para cada tipo de intención.]({% image_buster /assets/img/ai_use_cases/canvas_paths_by_intent.png %})

También configura el evento de conversión de Canvas como evento personalizado`upgraded_to_pro`, de modo que Braze realiza el seguimiento automático de las conversiones de actualización a medida que los usuarios avanzan en el flujo.

### Ejemplos de mensajes por ruta

{% tabs %}
{% tab High intent, fitness %}

Estos usuarios ya son activos y tienen una gran interacción con las características de seguimiento de la actividad física. Es probable que actualicen sin incentivos adicionales, por lo que el mensaje se centra en ofrecer información más detallada y herramientas avanzadas que se basan en sus hábitos actuales.

- **Línea del asunto:** Ve más allá con tus objetivos de fitness
- **Cabecera:** Tu progreso se merece Pro
- **Cuerpo:** Ya has creado una rutina sólida. Con Pro, puedes ir más allá: realiza el seguimiento del progreso de todos los grupos musculares, establece objetivos de rendimiento semanales y desbloquea análisis avanzados adaptados a tu forma de moverte.
- **CTA:** Comienza tu prueba gratuita de Pro

{% endtab %}
{% tab High intent, other %}
Estos usuarios muestran fuertes indicios de interacción, como navegar por las características Pro o utilizar la aplicación con frecuencia, pero no se centran específicamente en el seguimiento de la actividad física. El mensaje destaca las ventajas generales de Pro, como el coaching y la personalización, para animaros a dar el paso.

- **Línea del asunto:** Ya casi lo tienes: Pro estará listo cuando tú lo estés.
- **Cabecera:** Descubre más formas de moverte
- **Cuerpo:** Has estado explorando lo que Pro tiene para ofrecer. Ahora tienes la oportunidad de acceder a planes personalizados, contenido de entrenamiento individualizado y programas guiados diseñados para adaptarse a tus objetivos únicos, ya sea ganar fuerza, mejorar el equilibrio o mantener la constancia.
- **CTA:** Comienza tu prueba gratuita de Pro

{% endtab %}
{% tab Low intent, fitness %}
Estos usuarios prueban las características de fitness, pero no han dado pasos para mejorar. El mensaje se centra en sus intereses en materia de fitness y reduce la fricción con una oferta por tiempo limitado, lo que les ayuda a ver Pro como una forma de bajo riesgo de mejorar su rutina.

- **Línea del asunto:** ¿Listo para entrenar de forma más inteligente? Prueba Pro con un 50 % de descuento
- **Cabecera:** Tu mejora en el entrenamiento te está esperando.
- **Cuerpo:** Pro te ofrece todo lo que necesitas para empezar con fuerza: planes de entrenamiento fáciles de seguir, consejos de expertos y seguimiento del progreso real. Pruébalas ahora con un 50 % de descuento y cancélalas en cualquier momento.
- **CTA:** Consigue un 50 % de descuento en Pro

{% endtab %}
{% tab Low intent, other %}

Estos usuarios muestran una interacción mínima en general. Es poco probable que se actualicen sin un incentivo convincente, por lo que el mensaje adopta un enfoque sencillo que prioriza las ventajas, con un descuento y un lenguaje suave para invitar a explorar sin presiones.

- **Línea del asunto:** 50 % de descuento en Pro, solo durante este fin de semana.
- **Cabecera:** Listo cuando tú lo estés
- **Cuerpo:** Crea tu primer plan de entrenamiento personalizado, realiza el seguimiento de tu progreso y accede a entrenamientos exclusivos, todo por la mitad de precio. Prueba Pro por menos dinero y cancela en cualquier momento.
- **CTA:** Consigue un 50 % de descuento en Pro

{% endtab %}
{% endtabs %}

## Paso 4: Mide los resultados y optimiza tu estrategia.

Una vez finalizada la campaña, Jordan revisa el rendimiento en [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) para comprender qué tan bien funcionaron las rutas personalizadas y si la combinación de la intención predictiva con las señales de comportamiento mejoró las tasas de actualización.

Rendimiento del correo electrónico por ruta:

- **Alta intención, estado físico**
   - *Tasa de apertura:* 34 %
   - *Tasa de clics:* 20%
   - *Tasa de conversión:* 13 %
   - No se ha aplicado ningún descuento.
- **Alta intención, otros**
   - *Tasa de apertura:* 30 %
   - *Tasa de clics:* 17 %
   - *Tasa de conversión:* 11 %
   - No se ha aplicado ningún descuento.
- **Baja intención, estado físico**
   - *Tasa de apertura:* 27 %
   - *Tasa de clics:* 12 %
   - *Tasa de conversión:* 8 %
   - Oferta del 50 % de descuento incluida.
- **Baja intención, otros**
   - *Tasa de apertura:* 23 %
   - *Tasa de clics:* 9 %
   - *Tasa de conversión:* 6 %
   - Oferta del 50 % de descuento incluida.

En comparación con la campaña anterior del equipo, que era igual para todos (en la que un descuento general después de 7 días solo generó un 5 % de conversiones y un exceso de mensajes), el enfoque específico muestra un aumento significativo en todos los grupos, con una mayor eficiencia y menos descuentos innecesarios.

El [informe de]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) [embudo]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) también muestra una clara reducción en el abandono en los pasos clave, especialmente en el caso de los usuarios con poca intención de compra que recibieron mensajes personalizados. Cada vez más usuarios abren, hacen clic y actualizan, lo que demuestra el valor de la segmentación basada en la intención.

Jordan utiliza esta información para:

- Explora las pruebas A/B en las líneas del asunto y la redacción de las llamadas a la acción (CTA).
- Reevaluar el umbral de descuento para los usuarios con intención media.
- Continúa perfeccionando los segmentos basándote en comportamientos adicionales, como las visualizaciones de contenido o el uso de las características de la aplicación.

Gracias a Predictive Events y a la segmentación por capas, su equipo cuenta ahora con una estrategia escalable que adapta la mensajería en función de la intención y el comportamiento de los usuarios, lo que impulsa más actualizaciones y preserva la confianza en la marca.
