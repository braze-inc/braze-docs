{% if include.section == "Plan-specific features" %}

## Plan-specific AI features

The following table describes the differences between the free and pro version of the AI Personalized, Popular, and Trending recommendation types:

| Area                   | Free version                          | Pro version            |
| :---------------------- | ------------------------------------- | :--------------------------------------- |
| User update frequency<sup>1</sup>   | Weekly                                | Daily                                    |
| Model retraining frequency  | Monthly                               | Weekly                                   |
| Maximum recommendation models | 1 model per type<sup>2</sup> | 100 models per type<sup>2</sup> |

<sup>1. This is the frequency at which user-specific item recommendations are updated (all models except Most Popular items, which updates when the model retrains). For example, if a user purchases an item recommended based on AI item recommendations, their recommended items will be updated according to this frequency</sup><br>
<sup>2. Available recommendation types are AI Personalized, Most recent, Most popular, and Trending.</sup>

{% endif %}
