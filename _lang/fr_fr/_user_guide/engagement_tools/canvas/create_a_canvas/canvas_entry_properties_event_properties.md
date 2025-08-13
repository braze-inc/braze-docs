---
nav_title: Propriétés d’entrée et propriétés de l’événement Canvas
article_title: Propriétés d’entrée et propriétés de l’événement Canvas
page_order: 4.2
page_type: reference
description: "Cet article de référence décrit les différences entre les propriétés d’entrée et les propriétés de l’événement Canvas ainsi que le moment pour utiliser chacune de ces propriétés."
tool: Canvas
---

# Propriétés d’entrée et propriétés de l’événement Canvas

> Cet article de référence fournit des informations au sujet de `canvas_entry_properties` et `event_properties`, y compris les moments dans lesquels il faut utiliser chaque propriété, y compris les différences entre leurs comportements. <br><br> Pour plus d'informations sur les propriétés d'événements personnalisés en général, consultez la rubrique [Propriétés d'événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties).

{% alert important %}
Si vous participez à l' [accès anticipé au composant Contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context), les propriétés d'entrée de Canvas font partie des variables de contexte de Canvas. Cela signifie que `canvas_entry_properties` est maintenant référencé comme `context`. Chaque variable `context` comprend un nom, un type de données et une valeur qui peut inclure Liquid.
{% endalert %}

Les propriétés d'entrée et les propriétés d'événement de Canvas fonctionnent différemment dans vos flux de travail Canvas. Les propriétés d’événements ou d’appels API qui déclenchent l’entrée d’un utilisateur dans un Canvas sont connues sous le nom de `canvas_entry_properties`. Les propriétés d’un événement qui se produit alors que l’utilisateur se déplace à travers un parcours Canvas sont connues sous le nom de `event_properties`. La différence clé est que `canvas_entry_properties` ne se concentre pas uniquement sur les événements en accédant également aux propriétés des charges utiles d'entrée dans les canevas déclenchés par l'API.

Reportez-vous au tableau suivant pour un résumé des différences entre les propriétés d'entrée de Canvas et les propriétés d'événement.

| | Propriétés d’entrées de canvas | Propriétés d’événement
|----|----|----|
| **Liquid** | `canvas_entry_properties` | `event_properties` |
| **Persistance** | Peut être référencé par toutes les étapes du [message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) pendant la durée d'un canvas créé à l'aide de Canvas Flow. | \- Elle ne peut être référencée qu’une seule fois. <br> \- Elle ne peut pas être référencée par des étapes de messagerie suivantes. |
| **Comportement des toiles** | Vous pouvez référencer `canvas_entry_properties` à toutes les étapes d’un Canvas. Pour le comportement après le lancement, reportez-vous à la section [Modifier les canvas après le lancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties). | \- Peut faire référence à `event_properties` dans la première étape Message **après** une étape [Parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) où l'action entreprise est un événement personnalisé ou un événement d'achat. <br> \- Elles ne peuvent pas se trouver après un parcours « Tous les autres » de l’étape de parcours d’action. <br> \- Il peut y avoir d'autres composants que des messages entre les parcours d'action et les étapes des messages. Si l'un de ces composants autres que Message est une étape Parcours d'action, l'utilisateur peut passer par le parcours « Tous les autres » de ce parcours d'action. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% details Détails de l'éditeur Original Canvas %}

Vous ne pouvez plus créer ou dupliquer des toiles à l'aide de l'éditeur original. Cet article est disponible à titre de référence lors de l'utilisation des propriétés d'entrée de Canvas et des propriétés d'événement pour le flux de travail précédent de Canvas.

**Propriétés de l'entrée de la toile :**
- Les propriétés d'entrées persistantes doivent être activées. 
- Vous ne pouvez référencer les `canvas_entry_properties` que dans la première étape complète d’un Canvas. Le Canvas doit être par événement ou déclenché par API.

**Propriétés d'entrée :**
- Vous pouvez référencer `event_properties` dans toutes les étapes complètes utilisant la livraison par événement dans un Canvas.
- Elles ne peuvent pas être utilisées dans les étapes complètes planifiées n’étant pas la première étape complète d’un Canvas par événement. Toutefois, si un utilisateur utilise un [composant de canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/), le comportement suit les règles de Canvas Flow pour `event_properties`.

**Propriétés d'événement :**
- Impossible d'utiliser `event_properties` dans l'étape du message principal. Au lieu de cela, vous devez utiliser `canvas_entry_properties` ou ajouter une étape de parcours d'action avec l'événement correspondant **avant** l’étape Message qui inclut `event_properties`.

{% enddetails %}

### Choses à savoir

- Les propriétés d'entrée du canvas ne sont disponibles que pour référence dans Liquid. Pour filtrer sur les propriétés du canvas, utilisez plutôt la [segmentation des propriétés d'événement]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).
- Pour les canaux de communication in-app, `canvas_entry_properties` ne peut être référencé que dans un canvas. `event_properties` ne peut pas être utilisé pour les canaux de communication in-app.
- Vous ne pouvez pas utiliser les `event_properties` dans la première étape de message. Au lieu de cela, vous devez utiliser `canvas_entry_properties` ou ajouter une étape de parcours d'action avec l'événement correspondant **avant** l’étape Message qui inclut `event_properties`. 
- Lorsqu'une étape du parcours action contient un déclencheur "Envoi d'un message SMS entrant" ou "Envoi d'un message WhatsApp entrant", les étapes du canvas suivantes peuvent inclure une propriété SMS ou WhatsApp Liquid. Cela reflète le fonctionnement des propriétés d'événement dans Canvases. Vous pouvez ainsi tirer parti de vos messages pour enregistrer et référencer des données first-party sur les profils utilisateurs et les envois de messages conversationnels.

### Horodatage des propriétés d'événement

Si vous utilisez `event_properties` dans un canvas, les horodatages sont normalisés en UTC, à quelques exceptions près, détaillées ci-dessous. Compte tenu de ce comportement, Braze vous recommande vivement d'utiliser un filtre de fuseau horaire liquide tel que l'exemple suivant pour garantir l'envoi de vos messages avec votre [fuseau horaire préféré]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#time-zone-filter).

{% raw %}
```liquid
{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }
```
{% endraw %}

#### Exceptions

- Les horodatages ne sont pas normalisés à UTC dans la première étape d'un canvas si cette étape est une étape de message.
- Les horodatages ne sont pas normalisés à UTC dans toute étape du Message utilisant le canal message in-app, quel que soit son ordre dans le Canvas.

## Cas d’utilisation

![Une étape du parcours d'action suivie d'une étape de délai et d'une étape de message pour les utilisateurs qui ont ajouté un article à leur liste de souhaits, et un parcours pour tous les autres.]({% image_buster /assets/img_archive/canvas_entry_properties1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Pour mieux comprendre les différences entre `canvas_entry_properties` et `event_properties`, examinons le scénario suivant : les utilisateurs entrent dans un canvas basé sur des actions s'ils réalisent l'événement personnalisé "ajouter un article à la liste de souhaits". 

Le site `canvas_entry_properties` est configuré à l'étape de la création d'un canevas intitulée [Entry Schedule]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule) et correspondra au moment où l'utilisateur entrera dans le canevas. Ces `canvas_entry_properties` peuvent également être référencées dans n’importe lequel des étapes de message dans Canvas Flow étant donné que Canvas Flow prend en charge les propriétés d'entrées persistantes. 

Dans ce canvas, nous avons un parcours utilisateur qui commence par une étape Parcours d'action pour déterminer si un utilisateur a ajouté un article à sa liste de souhaits. À partir de là, si l'utilisateur a ajouté un article, il subira un délai avant de recevoir un message « Nouvel article dans votre liste de souhaits ! » à l'étape Message. 

La première étape Message d'un parcours client aura accès aux `event_properties` personnalisées à partir de votre étape Parcours d'action. Dans ce cas, nous sommes en mesure d'inclure ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` dans cette étape Message en tant que partie du contenu de notre message. Si un utilisateur n'ajoute pas d'article à sa liste de souhaits, il passe par le parcours « Tous les autres », ce qui signifie qu’il ne peut pas être fait référence aux `event_properties` et qu’une erreur de paramètres non valides sera renvoyée.

Prenez en compte le fait que vous n’aurez accès aux `event_properties` que si votre étape de message peut être remontée jusqu’à un parcours n’étant pas « Tous les autres » dans l’étape du parcours d’action. Si l’étape de message est connectée à un parcours « Tous les autres » mais peut être remontée jusqu’à une étape de parcours d’action dans le parcours utilisateur, vous aurez également accès aux `event_properties`. Pour plus d'informations sur ces comportements, consultez l'[étape du message.]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)

