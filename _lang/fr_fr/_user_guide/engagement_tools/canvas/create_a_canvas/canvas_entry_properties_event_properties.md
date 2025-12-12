---
nav_title: "Propriétés d'entrée dans le canvas et propriétés d'événement"
article_title: "Propriétés d'entrée dans le canvas et propriétés d'événement"
page_order: 4.2
page_type: reference
description: "Cet article de référence décrit les différences entre les propriétés d'entrée de Canvas et les propriétés d'événement, ainsi que le moment où il convient d'utiliser chaque propriété."
tool: Canvas
---

# Propriétés d'entrée dans le canvas et propriétés d'événement

> Cet article de référence contient des informations sur `canvas_entry_properties` et `event_properties`, y compris quand utiliser chaque propriété et les différences de comportement. <br><br> Pour plus d'informations sur les propriétés d'événements personnalisés en général, consultez la rubrique [Propriétés d'événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties).

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

Les propriétés d'entrée et les propriétés d'événement de Canvas fonctionnent différemment dans vos flux de travail Canvas. Les propriétés des événements ou des appels API qui déclenchent l'entrée d'un utilisateur dans un canvas sont appelées `canvas_entry_properties`. Les propriétés d'événements qui se produisent lorsqu'un utilisateur se déplace dans un parcours Canvas sont connues sous le nom de `event_properties`. La différence clé est que `canvas_entry_properties` ne se concentre pas uniquement sur les événements en accédant également aux propriétés des charges utiles d'entrée dans les canevas déclenchés par l'API.

Reportez-vous au tableau suivant pour un résumé des différences entre les propriétés d'entrée de Canvas et les propriétés d'événement.

| | Propriétés de l'entrée dans le canevas | Propriétés d'événement
|----|----|----|
| **Liquide** | `canvas_entry_properties` | `event_properties` |
| **Persistance** | Peut être référencé par toutes les étapes du [message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) pendant la durée d'un canvas créé à l'aide de Canvas. | \- Ne peut être référencé qu'une seule fois. <br> \- Ne peut être référencé par aucune étape de message ultérieure. |
| **Comportement des toiles** | Peut faire référence à `canvas_entry_properties` à n'importe quelle étape d'un canvas. Pour les comportements postérieurs au lancement, reportez-vous à la section [Modifier les toiles après le lancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties). | \- Peut faire référence à `event_properties` dans la première étape Message **après** une étape [Parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) où l'action entreprise est un événement personnalisé ou un événement d'achat. <br> \- Ne peut se situer après le parcours d'autres personnes de l'étape "Chemins d'action". <br> \- Il peut y avoir d'autres composants que des messages entre les parcours d'action et les étapes des messages. Si l'un de ces composants sans message est une étape du parcours d'action, l'utilisateur peut passer par le chemin "Everyone Else" de ce parcours d'action. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% details Original Canvas editor details %}

Vous ne pouvez plus créer ou dupliquer des toiles à l'aide de l'éditeur original. Cet article est disponible à titre de référence lors de l'utilisation des propriétés d'entrée de Canvas et des propriétés d'événement pour le flux de travail précédent de Canvas.

**Propriétés de l'entrée de la toile :**
- Les propriétés d'entrées persistantes doivent être activées. 
- Ne peut faire référence à `canvas_entry_properties` que dans la première étape complète d'un canvas. Le canvas doit être basé sur une action ou déclenché par l'API.

**Propriétés d'entrée :**
- Peut faire référence à `event_properties` dans toute étape complète qui utilise la livraison par événement dans un Canvas.
- Ne peut être utilisé dans des étapes complètes planifiées autres que la première étape complète d'un Canvas basé sur l'action. Toutefois, si un utilisateur utilise un [composant Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/), le comportement suit les règles actuelles du flux de travail Canvas pour `event_properties`.

**Propriétés d'événement :**
- Impossible d'utiliser `event_properties` dans l'étape du message principal. Au lieu de cela, vous devez utiliser `canvas_entry_properties` ou ajouter une étape de parcours d'action avec l'événement correspondant **avant l'** étape de message qui inclut `event_properties`.

{% enddetails %}

### Ce qu'il faut savoir

- Les propriétés d'entrée du canvas ne sont disponibles que pour référence dans Liquid. Pour filtrer sur les propriétés du canvas, utilisez plutôt la [segmentation des propriétés d'événement]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).
- Pour les canaux de communication in-app, `canvas_entry_properties` ne peut être référencé que dans un canvas. `event_properties` ne peut pas être utilisé pour les canaux de communication in-app.
- Vous ne pouvez pas utiliser `event_properties` à l'étape du message principal. Au lieu de cela, vous devez utiliser `canvas_entry_properties` ou ajouter une étape de parcours d'action avec l'événement correspondant **avant l'** étape de message qui inclut `event_properties`. 
- Lorsqu'une étape du parcours action contient un déclencheur "Envoi d'un message SMS entrant" ou "Envoi d'un message WhatsApp entrant", les étapes du canvas suivantes peuvent inclure une propriété SMS ou WhatsApp Liquid. Cela reflète le fonctionnement des propriétés d'événement dans Canvases. Vous pouvez ainsi tirer parti de vos messages pour enregistrer et référencer des données first-party sur les profils utilisateurs et les envois de messages conversationnels.

### Horodatage des propriétés d'événement

Si vous utilisez des horodatages avec un [type de date à]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) partir de [propriétés d'événements déclencheurs]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) dans des toiles basées sur des actions, les horodatages sont normalisés en UTC. Certaines exceptions sont détaillées ci-dessous.

Compte tenu de ce comportement, Braze vous recommande vivement d'utiliser un filtre de fuseau horaire liquide tel que l'exemple suivant pour garantir l'envoi de vos messages avec votre [fuseau horaire préféré]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#time-zone-filter).

{% raw %}
```liquid
{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }
```
{% endraw %}

#### Exceptions

- Les horodatages ne sont pas normalisés à UTC dans la première étape d'un canvas si cette étape est une étape de message.
- Les horodatages ne sont pas normalisés à UTC dans toute étape du Message utilisant le canal message in-app, quel que soit son ordre dans le Canvas.

## Cas d'utilisation

Une étape de parcours d'action suivie d'une étape de délai et d'une étape de message pour les utilisateurs qui ont ajouté un article à leur liste de souhaits, et un parcours pour tous les autres.]({% image_buster /assets/img_archive/canvas_entry_properties1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Pour mieux comprendre les différences entre `canvas_entry_properties` et `event_properties`, examinons le scénario suivant : les utilisateurs entrent dans un canvas basé sur des actions s'ils réalisent l'événement personnalisé "ajouter un article à la liste de souhaits". 

Le site `canvas_entry_properties` est configuré à l'étape de la création d'un canevas intitulée [Entry Schedule]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule) et correspondra au moment où l'utilisateur entrera dans le canevas. Ces `canvas_entry_properties` peuvent également être référencés dans n'importe quelle étape du message.

Dans ce Canvas, nous avons un parcours utilisateur qui commence par une étape de parcours d'action pour déterminer si un utilisateur a ajouté un article à sa liste de souhaits. À partir de là, si l'utilisateur a ajouté un article, il subira un délai avant de recevoir un message "Nouvel article dans votre liste de souhaits !" à l'étape Message. 

La première étape Message d'un parcours client aura accès à l'adresse `event_properties` personnalisée à partir de votre étape Chemins d'action. Dans ce cas, nous sommes en mesure d'inclure ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` dans cette étape du message en tant que partie du contenu de notre message. Si un utilisateur n'ajoute pas d'article à sa liste de souhaits, il passe par le chemin "Everyone Else", ce qui signifie que le site `event_properties` ne peut pas être référencé et qu'il renvoie une erreur de paramètres non valides.

Notez que vous n'aurez accès à `event_properties` que si votre étape Message peut être retracée jusqu'à un chemin autre que Tout le monde ailleurs dans une étape Chemins d'action. Si l'étape du message est liée à un parcours Everyone Else mais peut être retracée jusqu'à une étape Action Paths dans le parcours de l'utilisateur, vous aurez également accès à `event_properties`. Pour plus d'informations sur ces comportements, consultez l'[étape du message.]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)

