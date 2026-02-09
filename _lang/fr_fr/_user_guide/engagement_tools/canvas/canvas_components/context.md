---
nav_title: Contexte 
article_title: Contexte 
alias: /context/
page_order: 1.5
page_type: reference
toc_headers: "h2"
description: "Cet article de référence explique comment créer et utiliser des étapes contextuelles dans votre Canvas."
tool: Canvas

---

# Contexte

> Les étapes du canvas vous permettent de créer et de mettre à jour une ou plusieurs variables pour un utilisateur au fur et à mesure qu'il se déplace dans un canvas. Par exemple, si vous avez un Canvas qui gère les remises saisonnières, vous pouvez utiliser une variable de contexte pour stocker un code de remise différent chaque fois qu'un utilisateur entre dans le Canvas.

{% alert important %}
Les étapes du contexte sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.<br><br>Notez que l'abonnement à l'étape du canvas en accès anticipé met à jour la façon dont les horodatages sont traités dans tous vos canevas. Pour en savoir plus, consultez la rubrique [Normalisation de la cohérence des fuseaux horaires](#time-zone-consistency-standardization).
{% endalert %}

## Fonctionnement

![Une étape du Contexte est la première étape d'un Canvas.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Les étapes du contexte vous permettent de créer et d'utiliser des données temporaires au cours du parcours d'un utilisateur dans un Canvas spécifique. Ces données n'existent que dans le cadre de ce parcours Canvas et ne persistent pas dans les différents Canvas ou en dehors de la session.

Pour une référence complète sur les variables de contexte, y compris les types de données, l'utilisation et les meilleures pratiques, consultez la [référence sur les variables de contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

Dans une étape Contexte, vous pouvez définir ou mettre à jour jusqu'à 10 variables contextuelles. Ces variables peuvent être utilisées pour personnaliser les délais, segmenter les utilisateurs de manière dynamique et enrichir les envois de messages dans l'ensemble du Canvas. Par exemple, vous pouvez créer une variable contextuelle pour l'heure de vol planifiée d'un utilisateur, puis l'utiliser pour définir des retards personnalisés et envoyer des rappels.

Vous pouvez définir des variables de contexte de deux manières :

- **A l'entrée de la toile :** Les données de l'événement ou du déclencheur API peuvent alimenter automatiquement les variables de contexte.
- **Dans une étape de Contexte :** Définissez ou mettez à jour manuellement les variables de contexte en ajoutant une étape Contexte.

Chaque variable contextuelle requiert un nom, un type de données et une valeur (définie à l'aide de Liquid ou de l'outil Ajouter une personnalisation). Une fois définies, vous pouvez faire référence à des variables de contexte dans tout le canvas à l'aide de Liquid, comme {% raw %}`{{context.${flight_time}}}`{% endraw %}.

Chaque entrée dans Canvas redéfinit les variables de contexte en fonction des dernières données d'entrée et de la configuration de Canvas, ce qui permet aux utilisateurs d'avoir plusieurs parcours actifs avec leur propre contexte. Par exemple, si un client a deux vols à venir, il aura deux états de parcours distincts en cours d'exécution simultanément, chacun avec ses propres variables de contexte spécifiques au vol, comme l'heure de départ et la destination. Cela vous permet d'envoyer des rappels personnalisés sur leur vol de 14 heures pour New York tout en envoyant des mises à jour différentes sur leur vol de 8 heures pour Los Angeles demain, de sorte que chaque message reste pertinent pour la réservation spécifique.

### Traitement des utilisateurs et mise en lots

Les étapes contextuelles traitent les utilisateurs par lots afin d'optimiser les performances. Lorsque des utilisateurs entrent dans une étape Contexte, Braze les traite par lots de 1 000 utilisateurs par défaut. Ces lots sont traités en parallèle, mais au sein de chaque lot, les utilisateurs sont traités de manière séquentielle.

Cela signifie que :
- **Traitement par lots en parallèle**: Plusieurs lots de 1 000 utilisateurs sont traités simultanément, ce qui permet de gérer efficacement de grandes audiences.
- **Traitement séquentiel au sein des lots**: Dans chaque lot, les utilisateurs sont traités les uns après les autres. Si votre étape Contexte comprend des appels de [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call), la demande de contenu connecté de chaque utilisateur doit être terminée avant que l'utilisateur suivant de ce lot ne soit traité.
- **Progression indépendante des lots :** Chaque lot progresse de manière indépendante. Lorsqu'un lot a terminé son traitement, les utilisateurs passent immédiatement à l'étape suivante, même si d'autres lots sont encore en cours de traitement. Cela signifie que les utilisateurs de différents lots peuvent atteindre les étapes suivantes à des moments différents.

**Exemple**: Si 3 500 utilisateurs entrent dans une étape contextuelle avec du contenu connecté, cela prend 650 ms par utilisateur :
- Braze crée environ 4 lots d'utilisateurs (612, 802, 1 000, 880 et 120 utilisateurs dans cet exemple).
- Chaque lot traite les utilisateurs de manière séquentielle, de sorte qu'un lot de 1 000 utilisateurs prend environ 11 minutes (1 000 × 650 ms).
- Les lots se terminent à des moments différents, de sorte que les utilisateurs passent à l'étape suivante au fur et à mesure que leur lot se termine.
- Les premiers utilisateurs peuvent atteindre l'étape suivante plusieurs minutes avant les derniers utilisateurs, en fonction de la taille du lot et des temps de réponse du contenu connecté.

Sans contenu connecté, les étapes du contexte se déroulent beaucoup plus rapidement car il n'y a pas d'appels d'API externes à attendre.

## Considérations

- Vous pouvez définir jusqu'à 10 variables de contexte par étape de contexte.
- Chaque variable doit porter un nom unique (lettres, chiffres, caractères de soulignement uniquement, jusqu'à 100 caractères).
- La taille totale de toutes les variables d'une étape ne peut dépasser 50 Ko.
- Les variables transmises à l'aide de déclencheurs API partagent le même espace de noms que celles créées dans les étapes contextuelles ; la redéfinition d'une variable dans une étape contextuelle remplace la valeur API.

Pour plus de détails et une utilisation avancée, voir la [référence des variables contextuelles]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

## Création d'une étape contextuelle

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### Étape 1 : Ajouter une étape

Ajoutez une étape à votre Canvas, puis glissez-déposez le composant à partir de la barre latérale, ou sélectionnez le bouton plus de <i class="fas fa-plus-circle"></i> et sélectionnez **Contexte**.

### Étape 2 : Définir les variables

{% alert note %}
Vous pouvez définir jusqu'à 10 variables de contexte pour chaque étape de Contexte.
{% endalert %}

Pour définir une variable de contexte :

1. Donnez un **nom** à votre variable contextuelle.
2. Sélectionnez un [type de données](#context-variable-types).
3. Rédigez manuellement une expression Liquid ou utilisez **Ajouter une personnalisation** pour créer un extrait de code Liquid à partir d'attributs préexistants.
4. Sélectionnez **Aperçu** pour vérifier la valeur de votre variable contextuelle.
5. (Facultatif) Pour ajouter des variables supplémentaires, sélectionnez **Ajouter une variable contextuelle** et répétez les étapes 1 à 4.
6. Lorsque vous avez terminé, sélectionnez **Terminé**.

Vous pouvez désormais utiliser votre variable contextuelle partout où vous utilisez Liquid, comme dans les étapes Message et Mise à jour utilisateur, en sélectionnant **Ajouter une personnalisation**. Pour une présentation complète, voir la [référence aux variables contextuelles]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

### Filtres de variables contextuelles

Vous pouvez créer des filtres à l'aide de variables contextuelles dans les [parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) et les étapes de l'arbre [décisionnel]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split). Pour la configuration du filtre, la logique de comparaison et les exemples avancés, voir la [référence des variables de contexte.]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters)

## Prévisualisation des parcours utilisateurs

Nous vous recommandons de tester et de [prévisualiser vos parcours utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) pour vous assurer que vos messages sont envoyés à la bonne audience et que les variables de contexte sont évaluées en fonction des résultats attendus.

{% alert note %}
Si vous prévoyez votre Canvas dans la section **Prévisualisation & Test d'envoi de l'** éditeur, l'horodatage dans la prévisualisation du message de test **n'est pas** normalisé en UTC car ce panneau génère des prévisualisations sous forme de chaînes de caractères. Cela signifie que si un canvas est configuré pour accepter un objet `time`, l'aperçu du message ne donne pas une idée précise de ce qui se passe lorsque le canvas est en ligne/en production/instantanée. Pour tester votre Canvas de la manière la plus précise, nous vous recommandons plutôt de prévisualiser les parcours des utilisateurs.
{% endalert %}

Veillez à observer les scénarios courants qui créent des variables de contexte non valides. Lors de la prévisualisation de votre parcours d'utilisateur, vous pouvez visualiser les résultats des étapes de délai personnalisées à l'aide de variables de contexte, ainsi que toutes les comparaisons d'étapes d'audience, de décision ou de parcours d'action qui font correspondre les utilisateurs à n'importe quelle variable de contexte.

Si la variable de contexte est valide, vous pouvez y faire référence dans l'ensemble de votre Canvas. Cependant, si la variable de contexte n'a pas été créée correctement, les étapes ultérieures de votre canvas ne fonctionneront pas non plus correctement. Par exemple, si vous créez une étape Contexte pour attribuer une heure de rendez-vous aux utilisateurs et que vous définissez la valeur de l'heure de rendez-vous à une date passée, l'e-mail de rappel de votre étape Message n'est pas envoyé.

## Conversion des chaînes de contenu connecté en JSON

Lors d'un [appel au contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) dans une étape de Context, le JSON renvoyé par l'appel est évalué comme un type de données de type chaîne de caractères pour des raisons de cohérence et de prévention des erreurs. Si vous souhaitez convertir cette chaîne de caractères en JSON, convertissez-la en utilisant `as_json_string`. Par exemple :

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Normalisation de la cohérence des fuseaux horaires

Bien que la plupart des propriétés d'événement utilisant le type d'horodatage soient déjà en UTC dans Canvas, il y a quelques exceptions. Avec l'ajout de Canvas Context, toutes les propriétés d'événement d'horodatage par défaut dans les canevas basés sur l'action sont en UTC. Cette modification s'inscrit dans le cadre d'un effort plus large visant à garantir une expérience plus prévisible et plus cohérente lors de la modification des étapes du canvas et des messages. Notez que ce changement a un impact sur toutes les toiles basées sur des actions, que la toile en question utilise ou non une étape contextuelle.

{% alert important %}
En toutes circonstances, nous vous recommandons vivement d'utiliser les [filtres Liquid time_zone ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) pour que les horodatages soient conseillés dans le fuseau horaire souhaité. Vous pouvez vous référer à cette [question fréquemment posée](#faq-example) pour un exemple.
{% endalert %}

## Résolution des problèmes

### Variables de contexte non valides

Une variable de contexte est considérée comme invalide lorsque

- L'appel à un contenu connecté intégré échoue.
- Au moment de l'exécution, l'expression Liquid renvoie une valeur qui ne correspond pas au type de données ou qui est vide (null).

Par exemple, si le type de données de la variable contextuelle est **Number** mais que l'expression Liquid renvoie une chaîne de caractères, elle n'est pas valide.

Dans ces conditions :
- L'utilisateur passe à l'étape suivante.
- L'étape du canvas analytique considère que cette information _n'a pas été mise à jour_.

Lors de la résolution des problèmes, surveillez les indicateurs de _non-actualisation_ pour vérifier que votre variable contextuelle est correctement mise à jour. Si la variable de contexte n'est pas valide, vos utilisateurs peuvent continuer dans votre Canvas après l'étape du contexte, mais ne pourront pas se qualifier pour les étapes suivantes.

Reportez-vous à la section [Types de données]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#data-types) pour connaître les exemples de configuration pour chaque type de données.

### Retards dans l'envoi de contenu connecté

Lorsque le contenu connecté échoue à une étape du contexte, les utilisateurs qui réussissent passent immédiatement à l'étape suivante, tandis que les utilisateurs qui échouent sont relancés séparément. Cela signifie qu'un lot n'attend pas que tous les utilisateurs aient réussi avant de progresser : les utilisateurs qui ont réussi avancent dès que leur appel au contenu connecté est terminé.

**Comportement de réessai**: Les étapes du canvas (et toutes les étapes du canvas) utilisent des mécanismes de rappel spécifiques au canvas, et non le comportement de rappel standard du contenu connecté. En cas d'échec d'un appel de contenu connecté, Braze retente l'étape environ 13 fois avec des délais exponentiels. Si toutes les tentatives échouent, l'utilisateur quitte le Canvas.

**Remarque** : L'étiquette `:retry` utilisée dans le contenu connecté standard ne s'applique pas aux appels de contenu connecté effectués dans les étapes de Canvas. Les étapes du canvas ont leur propre logique de réessai optimisée pour les flux de travail du canvas.

**Délai de traitement**: Le temps nécessaire pour traiter tous les utilisateurs à travers une étape du Contexte dépend des éléments suivants :
- Le nombre d'utilisateurs entrant dans l'étape
- L'utilisation ou non de contenu connecté (et son temps de réponse)
- La taille du lot (par défaut, 1 000 utilisateurs par lot)

Si votre endpoint de contenu connecté a des limites de débit, considérez que les étapes de Contexte traitent les utilisateurs de manière séquentielle dans chaque lot, ce qui permet de respecter naturellement les limites de débit. Cependant, comme plusieurs lots sont traités en parallèle, assurez-vous que votre endpoint peut traiter des demandes simultanées provenant de plusieurs lots.

## Foire aux questions

### Qu'est-ce qui change lorsque le contexte Canvas devient généralement disponible ?

Lorsque le contexte Canvas devient généralement disponible, les détails suivants s'appliquent :

- Tous les horodatages de [type datetime]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) provenant des [propriétés des événements déclencheurs]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) dans les canevas basés sur l'action sont en [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). 
- Cette modification concerne toutes les toiles basées sur des actions, que la toile en question utilise ou non une étape contextuelle.

#### Quelle est la raison de ce changement ?

Cette modification s'inscrit dans le cadre d'un effort plus large visant à créer une expérience plus prévisible et plus cohérente lors de la modification des étapes du canvas et des messages.

#### Quand ce changement prend-il effet ?

- Si vous participez à l'accès anticipé à Canvas Context, ce changement a déjà été appliqué. 
- Si vous ne participez pas à l'accès anticipé à Canvas Context, ce changement s'appliquera lorsque vous rejoindrez l'accès anticipé ou lorsque Canvas Context sera disponible de manière générale.

#### Les toiles déclenchées par l'API ou planifiées sont-elles concernées par cette modification ?

Non.

#### Ce changement aura-t-il un impact sur les propriétés de Canvas entry ?

Oui, cela a un impact sur `canvas_entry_properties` si le `canvas_entry_property` est utilisé dans un canevas basé sur l'action et que le type de propriété est `time`. En toutes circonstances, nous vous recommandons d'utiliser les filtres Liquid `time_zone` pour que les horodatages soient conseillés dans le fuseau horaire souhaité.

Voici un exemple de la manière de procéder :

| Liquide dans l'envoi de messages | Sortie | Est-ce la façon de conseiller correctement les fuseaux horaires dans Liquid ? |
|---|---|---|
| {% raw %}```{{canvas_entry_properties.${timestamp_property}}}```{% endraw %} | `2025-08-05T08:15:30:250-0800` | Non |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 4:15pm` | Non
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 8:15am` | Oui |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Quel est l'exemple pratique de la façon dont le nouveau comportement de l'horodatage peut affecter mes messages ? {#faq-example}

Supposons que nous ayons un canvas basé sur des actions qui présente le contenu suivant dans une étape du message :

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Il en résulte le message suivant : 

```
Your appointment is scheduled for 2025-08-05 4:15pm, we’ll see you then!
```

Comme aucun fuseau horaire n'est spécifié à l'aide de Liquid, l'horodatage est ici en UTC. 

Pour spécifier clairement un fuseau horaire, nous pouvons utiliser les filtres Liquid `time_zone` comme suit : 

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Il en résulte le message suivant : 

```
Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!
```

Le fuseau horaire Amérique/Los Angeles étant spécifié à l'aide de Liquid, l'horodatage est ici en PST.

Le fuseau horaire préféré peut également être envoyé dans les propriétés d'événement et utilisé dans la logique Liquid :

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

### En quoi les variables de contexte diffèrent-elles des propriétés d'entrée dans le canvas ?

Si vous participez à l'étape du canvas en accès anticipé, les propriétés d'entrée de Canvas sont désormais incluses en tant que variables de contexte de Canvas. Cela signifie que vous pouvez envoyer les propriétés de l'entrée Canvas à l'aide de l'API Braze et y faire référence dans d'autres étapes, de manière similaire à l'utilisation d'une variable de contexte avec l'extrait de code Liquid.

### Les variables peuvent-elles faire référence les unes aux autres dans une étape du contexte singulier ?

Oui. Toutes les variables d'une étape contextuelle sont évaluées dans l'ordre, ce qui signifie que vous pouvez avoir les variables contextuelles suivantes :

| Variable de contexte | Valeur | Description |
|---|---|---|
|`favorite_cuisine`| {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | Type de cuisine préféré de l'utilisateur. |
|`promo_code`| {% raw %}`EATFRESH`{% endraw %} | Le code de réduction disponible pour un utilisateur. |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{context.promo_code}} "on delivery from your favorite" {{context.favorite_cuisine}} restaurants!"`{% endraw %} | Un message personnalisé qui combine les variables précédentes. Dans une étape Message, vous pourriez utiliser l'extrait de code Liquid {% raw %}`{{context.${personalized_message}}}`{% endraw %} pour faire référence à la variable contextuelle afin d'envoyer un message personnalisé à chaque utilisateur. Vous pouvez également utiliser une étape contextuelle pour enregistrer la valeur du [code promo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) et la modéliser dans d'autres étapes d'un canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Cela s'applique également à plusieurs étapes de Contexte. Imaginez par exemple la séquence suivante :
1. Une étape Contexte initiale crée une variable appelée `JobInfo` avec la valeur `job_title`.
2. Une étape Message fait référence à {% raw %}`{{context.${JobInfo}}}`{% endraw %} et affiche `job_title` à l'intention de l'utilisateur.
3. Plus tard, une étape Contexte met à jour la variable contexte, en changeant la valeur de `JobInfo` en `job_description`.
4. Toutes les étapes suivantes qui font référence à `JobInfo` utilisent désormais la valeur actualisée `job_description`.

Les variables contextuelles utilisent leur valeur la plus récente tout au long du canvas, chaque mise à jour affectant toutes les étapes suivantes qui font référence à cette variable.
