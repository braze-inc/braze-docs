{% if include.section == "Plan-specific features" %}

## Características de IA específicas del plan

En la tabla siguiente se describen las diferencias entre la versión gratuita y la pro de los tipos de recomendación AI Personalizada, Popular y Tendencias:

| Área                   | Versión gratuita                          | Versión Pro            |
| :---------------------- | ------------------------------------- | :--------------------------------------- |
| Frecuencia de actualización de <sup>usuarios1</sup>   | Semanalmente                                | Diariamente                                    |
| Frecuencia de reentrenamiento del modelo  | Mensualmente                               | Semanalmente                                   |
| Modelos de recomendación máxima | 1 modelo por <sup>tipo2</sup> | 100 modelos por <sup>tipo2</sup> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

<sup>1\. Es la frecuencia con la que se actualizan las recomendaciones de artículos específicas del usuario (todos los modelos excepto Artículos más populares, que se actualiza cuando el modelo se vuelve a entrenar). Por ejemplo, si un usuario compra un artículo recomendado basándose en las recomendaciones de artículos de la IA, sus artículos recomendados se actualizarán según esta frecuencia</sup><br>
<sup>2\. Los tipos de recomendación disponibles son AI Personalizada, Más reciente, Más popular y Tendencias.</sup>

{% endif %}
