---
nav_title: Propriétés d’entrée et propriétés de l’événement Canvas
article_title: Propriétés d’entrée et propriétés de l’événement Canvas
page_type: reference
description: "Cet article de référence décrit les différences entre les propriétés d’entrée et les propriétés de l’événement Canvas ainsi que le moment pour utiliser chacune de ces propriétés."
tool: Canvas
page_order: 4.1
---

# Propriétés d’entrée et propriétés de l’événement Canvas

> Cet article de référence fournit des informations au sujet de `canvas_entry_properties` et `event_properties`, y compris les moments dans lesquels il faut utiliser chaque propriété, y compris les différences entre leurs comportements.

Bien que leur nom soit similaire, les propriétés d’entrée et les propriétés de l’événement Canvas fonctionnent différemment dans vos flux de travail Canvas. Les propriétés d’événements ou d’appels API qui déclenchent l’entrée d’un utilisateur dans un Canvas sont connues sous le nom de `canvas_entry_properties`. Les propriétés d’un événement qui se produit alors que l’utilisateur se déplace à travers un parcours Canvas sont connues sous le nom de `event_properties`. La différence centrale est que les `canvas_entry_properties` se concentrent sur plus que les événements, mais aussi sur l’accès aux propriétés des charges utiles d’entrée dans les Canvas déclenchés par API.

{% alert important %}
Pour l’éditeur Canvas d’origine et Canvas Flow, vous ne pouvez pas utiliser `event_properties` au cours de l’étape du premier message. Au lieu de cela, vous devez utiliser `canvas_entry_properties` ou ajouter une étape de parcours d’action avec l’événement correspondant **avant** l’étape de message qui comprend `event_properties`.
{% endalert %}

Le comportement peut changer entre deux flux de travail construits avec l’éditeur de Canvas d’origine ou Canvas Flow. Par exemple, dans l’éditeur Canvas d’origine, vous pouvez utiliser `event_properties` dans la première étape complète s’il s’agit d’une étape par événement. Ceci n’est pas valable dans Canvas Flow étant donné que les étapes complètes n’y sont pas prises en charge. 

Consultez ce tableau pour obtenir un résumé des différences entre `canvas_entry_properties` et `event_properties`.

| | Propriétés d’entrées de Canvas | Propriétés de l’événement
|----|----|----|
| **Liquid** | `canvas_entry_properties` | `event_properties` |
| **Persistance** | Elle peut être référencée par toutes les étapes de [Message][1] pour toute la durée d’un Canvas, uniquement pour Canvas Flow. | - Elle ne peut être référencée qu’une seule fois. <br> - Elle ne peut pas être référencée par des étapes de messagerie suivantes. |
| **Comportement du Canvas d’origine** | - Les propriétés d’entrée persistantes doivent être activées. <br> - Vous ne pouvez référencer les `canvas_entry_properties` que dans la première étape complète d’un Canvas. Le Canvas doit être par événement ou déclenché par API. | - Vous pouvez référencer `event_properties` dans toutes les étapes complètes utilisant la livraison par événement dans un Canvas. <br> - Elles ne peuvent pas être utilisées dans les étapes complètes planifiées n’étant pas la première étape complète d’un Canvas basé sur des actions. Cependant, si un utilisateur utilise un [composant de Canvas][2] dans l’éditeur Canvas d’origine, le comportement suit les règles Canvas Flow pour les `event_properties`. |
| **Comportement Canvas Flow** | Vous pouvez référencer `canvas_entry_properties` à toutes les étapes d’un Canvas. | - Vous pouvez référencer `event_properties` dans la première étape de Message **après** une étape de [parcours d’actions][3] pour laquelle l’action effectuée est un événement personnalisé ou un événement d’achat. <br> - Elles ne peuvent pas se trouver après un parcours « Tous les autres » de l’étape de parcours d’action. <br> - Elles peuvent avoir d’autres composants Canvas n’étant pas des messages entre les parcours d’action et les étapes de message. Si aucun des composants du Canvas n’étant pas des messages ne se trouve dans l’étape de parcours d’action, l’utilisateur ne peut pas suivre le parcours « Tous les autres » de ce parcours d’action. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
Pour les Canaux de communication in-app, `canvas_entry_properties` ne peut être référencé dans Canvas Flow et dans l’éditeur Canvas d’origine que si vous avez activé les [propriétés d'entrées persistantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/) dans l’éditeur d’origine durant l’accès anticipé précédent. Cependant, `event_properties` ne peut pas être utilisé pour les canaux de communication in-app.
{% endalert %}

## Exemple

![][7]{: style="float:right;max-width:30%;margin-left:15px;"}

Voici un exemple expliquant le comportement de `canvas_entry_properties` et `event_properties` dans Canvas Flow. Imaginons un Canvas par événement. Dans ce scénario, les utilisateurs entreront dans ce Canvas s’ils effectuent l’événement personnalisé « ajouter un objet à la liste de souhait ». 

Les `canvas_entry_properties` sont configurées dans l’étape de [planification d’entrée]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule) de la création du Canvas et correspondront au moment où un utilisateur entre dans le Canvas. Ces `canvas_entry_properties` peuvent également être référencées dans n’importe lequel des étapes de message dans Canvas Flow étant donné que Canvas Flow prend en charge les propriétés d'entrées persistantes. 

Dans ce Canvas, nous avons un parcours utilisateur qui débute par une étape de parcours d’action pour déterminer si un utilisateur a ajouté un objet à sa liste de souhaits. À partir de là, si un utilisateur a ajouté un objet, il expérimentera alors un délai avant de recevoir un message « Nouvel objet dans votre liste de souhaits ! » de la part de l’étape de message. La première étape de message dans un parcours utilisateur aura accès aux `event_properties` personnalisées de votre étape de parcours d’action. Dans le cas présent, nous pourrons inclure ``  {% raw %} {{event_properties.${property_name}}} {% endraw %}`` ici dans cette étape de message au sein de notre contenu de message. 

Si un utilisateur n’ajoute pas un objet dans sa liste de souhait, il emprunte le parcours « Tous les autres », donc les `event_properties` ne peuvent pas être référencées et renverront une erreur de paramètres invalides.

Prenez en compte le fait que vous n’aurez accès aux `event_properties` que si votre étape de message peut être remontée jusqu’à un parcours n’étant pas « Tous les autres » dans l’étape du parcours d’action. Si l’étape de message est connectée à un parcours « Tous les autres » mais peut être remontée jusqu’à une étape de parcours d’action dans le parcours utilisateur, vous aurez également accès aux `event_properties`. Pour plus de renseignements sur ces comportements, consultez la section [Message][8].

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/
[3]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/
[7]: {% image_buster /assets/img_archive/canvas_entry_properties1.png %}
[8]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/
