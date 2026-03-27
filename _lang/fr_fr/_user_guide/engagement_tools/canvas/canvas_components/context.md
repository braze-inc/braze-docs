---
nav_title: Contexte 
article_title: Contexte 
alias: /context/
page_order: 6
page_type: reference
toc_headers: "h2"
description: "Cet article de référence explique comment créer et utiliser des étapes Contexte dans votre Canvas."
tool: Canvas

---

# Contexte

> Les étapes Contexte vous permettent de créer et de mettre à jour une ou plusieurs variables pour un utilisateur au fil de sa progression dans un Canvas. Par exemple, si vous avez un Canvas qui gère des remises saisonnières, vous pouvez utiliser une variable de contexte pour stocker un code de remise différent chaque fois qu'un utilisateur entre dans le Canvas.

## Fonctionnement

![Une étape Contexte comme première étape d'un Canvas.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Les étapes Contexte vous permettent de créer et d'utiliser des données temporaires pendant le parcours d'un utilisateur dans un Canvas spécifique. Ces données n'existent que dans le cadre de ce parcours Canvas et ne persistent ni dans d'autres Canvas, ni en dehors de la session.

Les variables de contexte n'existent que pour ce parcours Canvas spécifique. Elles ne modifient pas de manière permanente le profil de l'utilisateur et n'apparaissent pas dans d'autres Canvas. Elles sont donc idéales pour les informations temporaires qui ne concernent qu'une campagne ou un flux de travail spécifique.

{% alert tip %}
Pour obtenir des informations complètes sur les variables de contexte, y compris les types de données, leur utilisation et les bonnes pratiques, consultez l'[article de référence sur les variables de contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).
{% endalert %}

Dans une étape Contexte, vous pouvez définir ou mettre à jour jusqu'à 10 variables de contexte. Ces variables peuvent servir à personnaliser les délais, segmenter dynamiquement les utilisateurs et enrichir l'envoi de messages dans l'ensemble du Canvas. Par exemple, vous pourriez créer une variable de contexte pour l'heure de vol prévue d'un utilisateur, puis l'utiliser pour définir des délais personnalisés et envoyer des rappels.

Vous pouvez définir des variables de contexte de deux manières :

- **À l'entrée du Canvas :** Les données provenant de l'événement ou du déclencheur API peuvent automatiquement remplir les variables de contexte.
- **Dans une étape Contexte :** Définissez ou mettez à jour manuellement les variables de contexte en ajoutant une étape Contexte.

Chaque variable de contexte nécessite un nom, un type de données et une valeur (définie à l'aide de Liquid ou de l'outil Ajouter une personnalisation). Une fois définies, vous pouvez référencer les variables de contexte dans tout le Canvas à l'aide de Liquid, par exemple {% raw %}`{{context.${flight_time}}}`{% endraw %}. Dans le champ **Nom de la variable de contexte**, vous pouvez également saisir le nom de la variable de contexte ou le sélectionner dans le menu déroulant de l'éditeur d'étape. Pour plus de détails, consultez l'[article de référence sur les variables de contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

Chaque entrée dans le Canvas redéfinit les variables de contexte en fonction des dernières données d'entrée et de la configuration du Canvas, ce qui permet aux utilisateurs d'avoir plusieurs parcours actifs avec leur propre contexte. Par exemple, si un client a deux vols à venir, il aura deux états de parcours distincts fonctionnant simultanément, chacun avec ses propres variables de contexte spécifiques au vol, comme l'heure de départ et la destination. Cela vous permet d'envoyer des rappels personnalisés concernant son vol de 14 h à destination de New York, tout en envoyant des informations différentes concernant son vol de 8 h à destination de Los Angeles le lendemain, de sorte que chaque message reste pertinent par rapport à la réservation concernée.

### Traitement et regroupement des utilisateurs

Les étapes Contexte traitent les utilisateurs par lots afin d'optimiser les performances. Lorsque les utilisateurs arrivent à une étape Contexte, Braze les traite par lots de 1 000 utilisateurs par défaut. Ces lots sont traités en parallèle, mais au sein de chaque lot, les utilisateurs sont traités de manière séquentielle.

Concrètement :

**Exemple** : Si 3 500 utilisateurs arrivent à une étape Contexte avec du contenu connecté qui prend 650 ms par utilisateur :
- Braze crée quatre lots d'utilisateurs (1 000, 1 000, 1 000 et 500 utilisateurs dans cet exemple).
- Chaque lot traite les utilisateurs de manière séquentielle, de sorte qu'un lot de 1 000 utilisateurs prend environ 10,8 minutes (650 secondes ; 1 000 × 650 ms).
- Les lots se terminent à des moments différents, de sorte que les utilisateurs passent à l'étape suivante au fur et à mesure que leur lot est terminé.
- Les premiers utilisateurs peuvent atteindre l'étape suivante plusieurs minutes avant les derniers, en fonction de la taille du lot et des temps de réponse du contenu connecté.

Sans contenu connecté, les étapes Contexte s'exécutent beaucoup plus rapidement, car il n'y a pas d'appels API externes à attendre.

## Considérations

- Vous pouvez définir jusqu'à 10 variables de contexte par étape Contexte.
- Chaque variable doit avoir un nom unique (lettres, chiffres et underscores uniquement, jusqu'à 100 caractères).
- La taille totale de toutes les variables d'une étape ne doit pas dépasser 50 Ko.
- Les variables transmises via des déclencheurs API partagent le même espace de noms que celles créées dans les étapes Contexte ; redéfinir une variable dans une étape Contexte remplace la valeur provenant de l'API.

Pour plus de détails et une utilisation avancée, consultez l'[article de référence sur les variables de contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

## Créer une étape Contexte

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### Étape 1 : Ajouter une étape

Ajoutez une étape à votre Canvas, puis glissez-déposez le composant depuis la barre latérale, ou sélectionnez le bouton plus <i class="fas fa-plus-circle"></i> et choisissez **Contexte**.

### Étape 2 : Définir les variables

{% alert note %}
Vous pouvez définir jusqu'à 10 variables de contexte pour chaque étape Contexte.
{% endalert %}

Pour définir une variable de contexte :

1. Donnez un **nom** à votre variable de contexte.
2. Sélectionnez un [type de données]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#data-types).
3. Rédigez manuellement une expression Liquid ou utilisez **Ajouter une personnalisation** pour créer un extrait de code Liquid à partir d'attributs préexistants.
4. Sélectionnez **Prévisualiser** pour vérifier la valeur de votre variable de contexte.
5. (Facultatif) Pour ajouter des variables supplémentaires, sélectionnez **Ajouter une variable de contexte** et répétez les étapes 1 à 4.
6. Lorsque vous avez terminé, sélectionnez **Terminé**.

Vous pouvez désormais utiliser votre variable de contexte partout où vous utilisez Liquid, par exemple dans les étapes Message et Mise à jour utilisateur, en sélectionnant **Ajouter une personnalisation**. Dans le champ **Nom de la variable de contexte**, vous pouvez également saisir le nom de la variable de contexte ou le sélectionner dans le menu déroulant de l'éditeur d'étape. Pour des instructions détaillées, consultez l'[article de référence sur les variables de contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

{% alert important %}
Lorsque vous faites référence à des variables de contexte, utilisez toujours le format {% raw %}`{{context.${variable_name}}}`{% endraw %}.
{% endalert %}

### Filtres de variables de contexte

Vous pouvez créer des filtres à l'aide de variables de contexte dans les étapes [Parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) et [Arbre décisionnel]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split). Pour la configuration des filtres, la logique de comparaison et des exemples avancés, consultez l'[article de référence sur les variables de contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters).

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

## Prévisualiser les parcours utilisateur

Nous vous recommandons de tester et de [prévisualiser vos parcours utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) afin de vous assurer que vos messages sont envoyés à la bonne audience et que les variables de contexte produisent les résultats attendus.

{% alert note %}
Si vous prévisualisez votre Canvas dans la section **Prévisualisation et envoi test** de l'éditeur, l'horodatage dans l'aperçu du message test **n'est pas** normalisé en UTC, car ce panneau génère les aperçus sous forme de chaînes de caractères. Cela signifie que si un Canvas est configuré pour accepter un objet `time`, l'aperçu du message ne reflète pas fidèlement ce qui se produit lorsque le Canvas est en production. Pour tester votre Canvas de manière plus précise, nous vous recommandons de prévisualiser les parcours utilisateur.
{% endalert %}

Veillez à prendre en compte tous les scénarios courants susceptibles de générer des variables de contexte non valides. Lorsque vous prévisualisez votre parcours utilisateur, vous pouvez visualiser les résultats des étapes de délai personnalisées utilisant des variables de contexte, ainsi que toutes les comparaisons d'audience ou d'arbre décisionnel qui associent les utilisateurs à des variables de contexte.

Si la variable de contexte est valide, vous pouvez y faire référence dans l'ensemble de votre Canvas. En revanche, si la variable de contexte n'a pas été créée correctement, les étapes suivantes de votre Canvas ne fonctionneront pas correctement non plus. Par exemple, si vous créez une étape Contexte pour attribuer un rendez-vous aux utilisateurs et que vous définissez la valeur du rendez-vous sur une date passée, l'e-mail de rappel de votre étape Message ne sera pas envoyé.

## Convertir les chaînes de contenu connecté en JSON

Lorsqu'un [appel de contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) est effectué dans une étape Contexte, le JSON renvoyé par l'appel est évalué comme un type de données chaîne de caractères, par souci de cohérence et de prévention des erreurs. Si vous souhaitez convertir cette chaîne en JSON, utilisez `as_json_string`. Par exemple :

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Résolution des problèmes

### Variables de contexte non valides

Une variable de contexte est considérée comme non valide lorsque :

- L'appel à un contenu connecté intégré échoue.
- Au moment de l'exécution, l'expression Liquid renvoie une valeur qui ne correspond pas au type de données attendu ou qui est vide (null).

Par exemple, si le type de données de la variable de contexte est **Nombre** mais que l'expression Liquid renvoie une chaîne de caractères, la variable est non valide.

Dans ce cas :
- L'utilisateur passe à l'étape suivante.
- L'analytique de l'étape du Canvas comptabilise cela comme _Non mis à jour_.

Lors de la résolution des problèmes, surveillez l'indicateur _Non mis à jour_ pour vérifier que votre variable de contexte est correctement mise à jour. Si la variable de contexte est non valide, vos utilisateurs peuvent continuer dans votre Canvas après l'étape Contexte, mais risquent de ne pas se qualifier pour les étapes suivantes.

Consultez la section [Types de données]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#data-types) pour des exemples de configuration pour chaque type de données.

### Retards d'envoi avec le contenu connecté

Tous les utilisateurs d'un lot sont traités avant que quiconque ne puisse avancer. Une fois le traitement du lot terminé, les utilisateurs traités avec succès passent à l'étape suivante, tandis que ceux ayant échoué font l'objet d'une nouvelle tentative séparée. Les utilisateurs traités avec succès n'attendent pas que les nouvelles tentatives aboutissent avant d'avancer.

**Comportement de réessai** : Les étapes Contexte (et toutes les étapes du Canvas) utilisent des mécanismes de nouvelle tentative spécifiques au Canvas, et non le comportement de nouvelle tentative standard du contenu connecté. Si un appel de contenu connecté échoue, Braze réessaie l'étape environ 13 fois avec des délais exponentiels. Si toutes les tentatives échouent, l'utilisateur quitte le Canvas.

{% alert note %}
L'étiquette `:retry` utilisée dans le contenu connecté standard ne s'applique pas aux appels de contenu connecté effectués dans les étapes du Canvas. Les étapes du Canvas disposent de leur propre logique de réessai, optimisée pour les workflows Canvas.
{% endalert %}

**Temps de traitement** : Le temps nécessaire pour traiter tous les utilisateurs via une étape Contexte dépend de :
- Le nombre d'utilisateurs entrant dans l'étape
- L'utilisation ou non du contenu connecté (et son temps de réponse)
- La taille du lot (par défaut, 1 000 utilisateurs par lot)

Si votre endpoint de contenu connecté est soumis à des limites de débit, notez que les étapes Contexte traitent les utilisateurs de manière séquentielle au sein de chaque lot, ce qui contribue naturellement au respect de ces limites. Cependant, plusieurs lots sont traités en parallèle : assurez-vous donc que votre endpoint peut gérer les requêtes simultanées provenant de plusieurs lots.

## Normalisation des fuseaux horaires

Avec la disponibilité générale de Canvas Context, toutes les propriétés d'événement d'horodatage par défaut dans les Canvas basés sur les actions sont désormais en UTC. Ce changement s'inscrit dans une initiative plus large visant à garantir une expérience plus prévisible et cohérente lors de la modification des étapes du Canvas et des messages. Notez que cette modification affecte tous les Canvas basés sur des actions, que le Canvas en question utilise ou non une étape Contexte.

{% alert important %}
Dans tous les cas, nous recommandons fortement d'utiliser les [filtres Liquid time_zone]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) pour que les horodatages soient représentés dans le fuseau horaire souhaité. Consultez cette [question fréquente](#faq-example) pour un exemple.
{% endalert %}

## Foire aux questions

### Quels changements ont été apportés depuis que Canvas Context est devenu accessible à tous ?

Maintenant que Canvas Context est disponible pour tous, voici ce qui s'applique :

- Tous les horodatages de [type datetime]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) provenant des [propriétés d'événement déclencheur]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) dans les Canvas basés sur des actions sont exprimés en [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time).
- Cette modification affecte tous les Canvas basés sur des actions, que le Canvas en question utilise ou non une étape Contexte.

#### Quelle est la raison de ce changement ?

Ce changement s'inscrit dans une initiative plus large visant à offrir une expérience plus prévisible et cohérente lors de la modification des étapes du Canvas et des messages.

#### Les Canvas déclenchés par API ou planifiés sont-ils affectés par ce changement ?

Non.

#### Ce changement affecte-t-il les propriétés d'entrée du Canvas ?

Oui, cela a une incidence sur `canvas_entry_properties` si la `canvas_entry_property` est utilisée dans un Canvas basé sur les actions et que le type de propriété est `time`. Dans tous les cas, nous recommandons d'utiliser les filtres Liquid `time_zone` pour que les horodatages soient représentés dans le fuseau horaire souhaité.

Voici un exemple illustrant comment procéder :

| Liquid dans l'étape Message | Sortie | Est-ce la bonne manière de représenter les fuseaux horaires dans Liquid ? |
|---|---|---|
| {% raw %}```{{canvas_entry_properties.${timestamp_property}}}```{% endraw %} | `2025-08-05T08:15:30:250-0800` | Non |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 4:15pm` | Non
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 8:15am` | Oui |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Quel est un exemple concret de la façon dont le nouveau comportement de l'horodatage pourrait affecter mes messages ? {#faq-example}

Supposons que nous ayons un Canvas basé sur les actions contenant le texte suivant dans une étape Message :

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Cela génère le message suivant : 

```
Your appointment is scheduled for 2025-08-05 4:15pm, we’ll see you then!
```

Étant donné qu'aucun fuseau horaire n'est spécifié avec Liquid, l'horodatage est ici en UTC. 

Pour spécifier clairement un fuseau horaire, nous pouvons utiliser les filtres Liquid `time_zone` comme suit : 

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Cela génère le message suivant : 

```
Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!
```

Étant donné que le fuseau horaire America/Los_Angeles est spécifié à l'aide de Liquid, l'horodatage est ici en heure PST.

Le fuseau horaire préféré peut également être envoyé dans le payload des propriétés d'événement et utilisé dans la logique Liquid :

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

### En quoi les variables de contexte diffèrent-elles des propriétés d'entrée du Canvas ?

Les propriétés d'entrée du Canvas sont incluses en tant que variables de contexte Canvas. Cela signifie que vous pouvez envoyer les propriétés d'entrée du Canvas via l'API Braze et y faire référence dans d'autres étapes, de la même manière qu'une variable de contexte avec un extrait de code Liquid.

### Les variables peuvent-elles faire référence les unes aux autres dans une même étape Contexte ?

Oui. Toutes les variables d'une étape Contexte sont évaluées de manière séquentielle, ce qui signifie que vous pourriez configurer les variables de contexte suivantes :

| Variable de contexte | Valeur | Description |
|---|---|---|
|`favorite_cuisine`| {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | Le type de cuisine préféré de l'utilisateur. |
|`promo_code`| {% raw %}`EATFRESH`{% endraw %} | Le code de réduction disponible pour l'utilisateur. |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{context.${promo_code}}} "on delivery from your favorite" {{context.${favorite_cuisine}}} restaurants!"`{% endraw %} | Un message personnalisé qui combine les variables précédentes. Dans une étape Message, vous pourriez utiliser l'extrait de code Liquid {% raw %}`{{context.${personalized_message}}}`{% endraw %} pour faire référence à la variable de contexte et envoyer un message personnalisé à chaque utilisateur. Vous pouvez également utiliser une étape Contexte pour enregistrer la valeur du [code promotionnel]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) et l'intégrer dans d'autres étapes du Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Cela s'applique également à plusieurs étapes Contexte. Imaginez par exemple la séquence suivante :

1. Une étape Contexte initiale crée une variable appelée `JobInfo` avec la valeur `job_title`.
2. Une étape Message fait référence à {% raw %}`{{context.${JobInfo}}}`{% endraw %} et affiche `job_title` à l'utilisateur.
3. Plus tard, une étape Contexte met à jour la variable de contexte en changeant la valeur de `JobInfo` en `job_description`.
4. Toutes les étapes suivantes qui font référence à `JobInfo` utilisent désormais la valeur mise à jour `job_description`.

Les variables de contexte utilisent leur valeur la plus récente tout au long du Canvas, chaque mise à jour affectant toutes les étapes suivantes qui font référence à cette variable.