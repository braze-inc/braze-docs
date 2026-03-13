---
nav_title: "Propriétés du contexte et de l'événement"
article_title: "Propriétés du contexte et des propriétés d'événement"
page_order: 4.2
page_type: reference
description: "Cet article de référence décrit les différences entre les propriétés de contexte et les propriétés d'événement, ainsi que les cas dans lesquels chacune d'elles doit être utilisée."
tool: Canvas
---

# Propriétés du contexte et de l'événement

> Cet article de référence fournit des informations au sujet de `context` et `event_properties`, y compris les moments dans lesquels il faut utiliser chaque propriété, y compris les différences entre leurs comportements. <br><br> Pour plus d'informations sur les propriétés d'événements personnalisés en général, consultez la rubrique [Propriétés d'événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties).

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

Les propriétés de contexte et les propriétés d'événement fonctionnent différemment dans vos workflows canvas. Les propriétés d’événements ou d’appels API qui déclenchent l’entrée d’un utilisateur dans un Canvas sont connues sous le nom de `context`. Les propriétés des événements qui se produisent lorsqu'un utilisateur se déplace dans un parcours Canvas sont appelées `event_properties`. La différence clé est que `context` ne se concentre pas uniquement sur les événements en accédant également aux propriétés des charges utiles d'entrée dans les canevas déclenchés par l'API.

Veuillez vous référer au tableau suivant pour obtenir un résumé des différences entre les propriétés de contexte et les propriétés d'événement.

| | Propriétés contextuelles | Propriétés de l’événement |
|----|----|----|
| **Liquid** | `context` | `event_properties` |
| **Persistance** | Peut être référencé par toutes les étapes [Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) pendant toute la durée d'un canvas créé à l'aide de Canvas. | \- Elle ne peut être référencée qu’une seule fois. <br> \- Elle ne peut pas être référencée par des étapes de messagerie suivantes. |
| **Comportement des toiles** | Vous pouvez référencer `context` à toutes les étapes d’un Canvas. Pour le comportement après le lancement, reportez-vous à la section [Modifier les canvas après le lancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties). | \- Peut faire référence à `event_properties` dans la première étape Message **après** une étape [Parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) où l'action entreprise est un événement personnalisé ou un événement d'achat. <br> \- Elles ne peuvent pas se trouver après un parcours « Tous les autres » de l’étape de parcours d’action. <br> \- Il peut y avoir d'autres composants que des messages entre les parcours d'action et les étapes des messages. Si l'un de ces composants autres que Message est une étape Parcours d'action, l'utilisateur peut passer par le parcours « Tous les autres » de ce parcours d'action. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% details Original Canvas editor details %}

Vous ne pouvez plus créer ou dupliquer des toiles à l'aide de l'éditeur original. Veuillez noter que le contexte canvas n'est pas pris en charge dans l'éditeur canvas d'origine. Cette section est donc disponible à titre de référence lorsque vous utilisez les propriétés d'entrée et les propriétés d'événement canvas pour le workflow canvas précédent.

**Propriétés de l'entrée de la toile :**
- Les propriétés d'entrées persistantes doivent être activées. 
- Vous ne pouvez référencer les `canvas_entry_properties` que dans la première étape complète d’un Canvas. Le Canvas doit être par événement ou déclenché par API.

**Propriétés d'entrée :**
- Vous pouvez référencer `event_properties` dans toutes les étapes complètes utilisant la livraison par événement dans un Canvas.
- Elles ne peuvent pas être utilisées dans les étapes complètes planifiées n’étant pas la première étape complète d’un Canvas par événement. Toutefois, si un utilisateur utilise un [composant canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/), le comportement suit les règles actuelles du flux de travail canvas pour `event_properties`.

**Propriétés d'événement :**
- Impossible d'utiliser `event_properties` dans l'étape du message principal. Au lieu de cela, vous devez utiliser `canvas_entry_properties` ou ajouter une étape de parcours d'action avec l'événement correspondant **avant** l’étape Message qui inclut `event_properties`.

{% enddetails %}

### Choses à savoir

- Le contexte est uniquement disponible à titre de référence dans Liquid. Pour filtrer sur les propriétés du canvas, utilisez plutôt la [segmentation des propriétés d'événement]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).
- Pour les canaux de message in-app, vous pouvez faire référence à`context`et`event_properties`dans un Canvas.`event_properties`est accessible lorsqu'il est inclus dans la première étape du canvas, car il est basé sur un déclencheur.
- Vous ne pouvez pas utiliser les `event_properties` dans la première étape de message. Vous pouvez également utiliser`context`ou ajouter une étape Parcours d’action avec l’événement correspondant **avant** l’étape Message qui inclut `event_properties`.
- Lorsqu'une étape du parcours action contient un déclencheur "Envoi d'un message SMS entrant" ou "Envoi d'un message WhatsApp entrant", les étapes du canvas suivantes peuvent inclure une propriété SMS ou WhatsApp Liquid. Cela reflète le fonctionnement des propriétés d'événement dans Canvases. Vous pouvez ainsi tirer parti de vos messages pour enregistrer et référencer des données first-party sur les profils utilisateurs et les envois de messages conversationnels.

{% alert note %}
L'admissibilité de l'audience est évaluée une fois à l'entrée dans canvas. Si un utilisateur est fusionné lors de son entrée, l'utilisateur identifié poursuit son parcours dans le canvas et n'est pas réévalué par rapport aux critères du segment de Canvas.
{% endalert %}

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### Horodatage des déclencheurs

Si vous utilisez des horodatages avec un [type datetime]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) provenant d'événements qui sont des déclencheurs d'actions de déclenchement pour des canevas basés sur des actions, qui sont référencés à l'aide [du contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties), les horodatages sont normalisés en UTC.

Compte tenu de ce comportement, Braze vous recommande vivement d'utiliser un filtre de fuseau horaire liquide tel que l'exemple suivant pour garantir l'envoi de vos messages avec votre [fuseau horaire préféré]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#time-zone-filter).

{% raw %}
```liquid
{{context.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }}
```
{% endraw %}

#### Exceptions

- Les horodatages ne sont pas normalisés à UTC dans la première étape d'un canvas si cette étape est une étape de message.
- Les horodatages ne sont pas normalisés à UTC dans toute étape du Message utilisant le canal message in-app, quel que soit son ordre dans le Canvas.

## Cas d’utilisation

![Un parcours d’action suivi d’une étape Délai et d’une étape Message pour les utilisateurs ayant ajouté un article à leur liste de souhaits, et un chemin pour tous les autres.]({% image_buster /assets/img_archive/canvas_entry_properties1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Pour mieux comprendre les différences entre`context`et `event_properties`, examinons ce scénario dans lequel les utilisateurs accèdent à un canvas basé sur une action s'ils effectuent l'événement personnalisé « ajouter un article à la liste de souhaits ». 

Le contexte est configuré à l'étape de [planification de l'entrée]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule) lors de la création d'un canevas et correspond au moment où un utilisateur accède à un canevas. Le contexte peut également être référencé dans n'importe quelle étape de message.

Dans ce canvas, nous avons un parcours utilisateur qui commence par une étape Parcours d'action pour déterminer si un utilisateur a ajouté un article à sa liste de souhaits. À partir de là, si l'utilisateur a ajouté un article, il constate un délai avant de recevoir le message « Nouvel article dans votre liste de souhaits ! » à l'étape Message. 

La première étape Message d'un parcours client a accès à la personnalisation`event_properties`de votre étape du parcours d’action. Dans ce cas, nous sommes en mesure d'inclure ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` dans cette étape Message en tant que partie du contenu de notre message. Si un utilisateur n'ajoute pas d'élément à sa liste de souhaits, il suit le chemin « Tout le monde », ce qui signifie que l'élément`event_properties`ne peut pas être référencé et renvoie une erreur de paramètres non valides.

Prenez en compte le fait que vous n’aurez accès aux `event_properties` que si votre étape de message peut être remontée jusqu’à un parcours n’étant pas « Tous les autres » dans l’étape du parcours d’action. Si l'étape Message est connectée à un chemin Tout le monde, mais qu'elle peut être retracée jusqu'à une étape Parcours d’action dans le parcours utilisateur, vous avez également toujours accès à `event_properties`. Pour plus d'informations sur ces comportements, veuillez consulter [l'étape Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

