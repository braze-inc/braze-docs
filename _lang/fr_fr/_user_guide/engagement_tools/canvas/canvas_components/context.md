---
nav_title: Contexte 
article_title: Contexte 
alias: /context/
page_order: 6
page_type: reference
toc_headers: "h2"
description: "Cet article de référence explique comment créer et utiliser des étapes contextuelles dans votre Canvas."
tool: Canvas

---

# Contexte

> Les étapes contextuelles vous permettent de créer et de mettre à jour une ou plusieurs variables pour un utilisateur lorsqu'il navigue dans un canvas. Par exemple, si vous avez un Canvas qui gère les remises saisonnières, vous pouvez utiliser une variable de contexte pour stocker un code de remise différent chaque fois qu'un utilisateur entre dans le Canvas.

## Fonctionnement

![Une étape du Contexte est la première étape d'un Canvas.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Les étapes contextuelles vous permettent de créer et d'utiliser des données temporaires pendant le parcours d'un utilisateur dans un canevas spécifique. Ces données n'existent que dans le cadre de ce parcours Canvas et ne persistent pas dans les différents Canvas ou en dehors de la session.

Les variables de contexte n'existent que pour ce parcours canvas spécifique. Ils ne modifient pas de manière permanente le profil utilisateur et n'apparaissent pas dans d'autres canevas. Cela les rend particulièrement adaptés aux informations temporaires qui ne concernent qu'une campagne ou un flux de travail spécifique.

{% alert tip %}
Pour obtenir des informations complètes sur les variables de contexte, y compris les types de données, leur utilisation et les meilleures pratiques, veuillez consulter la [référence sur les variables de contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).
{% endalert %}

Dans une étape Contexte, vous pouvez définir ou mettre à jour jusqu'à 10 variables de contexte. Ces variables peuvent être utilisées pour personnaliser les délais, réaliser une segmentation dynamique des utilisateurs et enrichir l'envoi de messages dans l'ensemble du canvas. Par exemple, vous pourriez créer une variable de contexte pour l'heure de vol planifiée pour un utilisateur, puis l'utiliser pour définir des retards de personnalisation et envoyer des rappels.

Vous pouvez définir des variables de contexte de deux manières :

- **A l'entrée de la toile :** Les données provenant de l'événement ou du déclencheur API peuvent automatiquement remplir les variables de contexte.
- **Dans une étape de Contexte :** Définissez ou mettez à jour manuellement les variables de contexte en ajoutant une étape Contexte.

Chaque variable de contexte nécessite un nom, un type de données et une valeur (définie à l'aide de Liquid ou de l'outil Ajouter une personnalisation). Une fois définies, vous pouvez référencer les variables de contexte dans tout le canvas à l'aide de liquid, par exemple {% raw %}`{{context.${flight_time}}}`{% endraw %}.

Chaque entrée Canvas redéfinit les variables de contexte en fonction des dernières données saisies et de la configuration de Canvas, permettant ainsi aux utilisateurs d'avoir plusieurs parcours actifs avec leur propre contexte. Par exemple, si un client a deux vols à venir, il aura deux statuts de voyage distincts fonctionnant simultanément, chacun avec ses propres variables contextuelles spécifiques au vol, telles que l'heure de départ et la destination. Cela vous permet d'envoyer des rappels personnalisés concernant leur vol de 14 h à destination de New York, tout en envoyant des informations différentes concernant leur vol de 8 h à destination de Los Angeles demain, de sorte que chaque message reste pertinent par rapport à la réservation spécifique.

### Traitement et regroupement des utilisateurs

Le contexte traite les utilisateurs par lots afin d'optimiser les performances. Lorsque les utilisateurs accèdent à une étape Context, Braze les traite par lots de 1 000 utilisateurs par défaut. Ces lots sont traités en parallèle, mais au sein de chaque lot, les utilisateurs sont traités de manière séquentielle.

Cela signifie :

**Exemple** : Si 3 500 utilisateurs accèdent à une étape Context avec du contenu connecté qui prend 650 ms par utilisateur :
- Braze crée quatre lots d'utilisateurs (1 000, 1 000, 1 000 et 500 utilisateurs dans cet exemple).
- Chaque lot traite les utilisateurs de manière séquentielle, de sorte qu'un lot de 1 000 utilisateurs prend environ 10,8 minutes (650 secondes ; 1 000 × 650 ms).
- Les lots sont traités à des moments différents, de sorte que les utilisateurs passent à l'étape suivante dès que leur lot est terminé.
- Les premiers utilisateurs peuvent atteindre l'étape suivante plusieurs minutes avant les derniers utilisateurs, en fonction de la taille du lot et des temps de réponse du contenu connecté.

Sans contenu connecté, les étapes de contexte s'exécutent beaucoup plus rapidement, car il n'y a pas d'appels API externes à attendre.

## Considérations

- Vous pouvez définir jusqu'à 10 variables de contexte par étape de contexte.
- Chaque variable doit avoir un nom unique (lettres, chiffres et traits de soulignement uniquement, jusqu'à 100 caractères).
- La taille totale de toutes les variables d'une étape ne doit pas dépasser 50 Ko.
- Les variables transmises à l'aide des déclencheurs API partagent le même espace de noms que celles créées dans les étapes Context ; la redéfinition d'une variable dans une étape Context remplace la valeur API.

Pour plus de détails et une utilisation avancée, veuillez consulter [la référence des variables de contexte.]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/)

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
2. Sélectionnez un [type de données]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#data-types).
3. Rédigez manuellement une expression Liquid ou utilisez **Ajouter une personnalisation** pour créer un extrait de code Liquid à partir d'attributs préexistants.
4. Sélectionnez **Aperçu** pour vérifier la valeur de votre variable contextuelle.
5. (Facultatif) Pour ajouter des variables supplémentaires, veuillez sélectionner **Ajouter une variable de contexte** et répéter les étapes 1 à 4.
6. Lorsque vous avez terminé, sélectionnez **Terminé**.

Vous pouvez désormais utiliser votre variable contextuelle partout où vous utilisez Liquid, comme dans les étapes Message et Mise à jour utilisateur, en sélectionnant **Ajouter une personnalisation**. Pour obtenir des instructions détaillées, veuillez consulter [la référence des variables de contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

{% alert important %}
Lorsque vous faites référence à des variables de contexte, veuillez toujours utiliser le format {% raw %}`{{context.${variable_name}}}`{% endraw %}.
{% endalert %}

### Filtres de variables contextuelles

Vous pouvez créer des filtres à l'aide de variables de contexte dans les étapes [du parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) et [de l'arbre décisionnel]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split). Pour la configuration des filtres, la logique de comparaison et des exemples avancés, veuillez consulter [la référence des variables de contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters).

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

## Prévisualisation des chemins d'accès des utilisateurs

Nous vous recommandons de tester et [de prévisualiser vos chemins d'accès utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) afin de vous assurer que vos messages sont envoyés au bon public et que les variables contextuelles sont évaluées conformément aux résultats attendus.

{% alert note %}
Si vous prévisualisez votre Canvas dans la section **Prévisualisation  Envoi& test** de l'éditeur, l'horodatage dans l'aperçu du message test **n'est pas** normalisé en UTC, car ce panneau génère des aperçus sous forme de chaînes de caractères. Cela signifie que si un Canvas est configuré pour accepter un`time`objet, l'aperçu du message ne reflète pas fidèlement ce qui se produit lorsque le Canvas est en ligne/en production/instantané. Afin de tester votre canvas de manière plus précise, nous vous recommandons de prévisualiser les chemins d'accès des utilisateurs.
{% endalert %}

Veuillez vous assurer de respecter tous les scénarios courants qui génèrent des variables de contexte non valides. Lorsque vous prévisualisez votre chemin utilisateur, vous pouvez visualiser les résultats des étapes de délai de personnalisation à l'aide de variables de contexte, ainsi que toutes les comparaisons d'audience ou d'étapes de décision qui associent les utilisateurs à des variables de contexte.

Si la variable de contexte est valide, vous pouvez y faire référence dans l'ensemble de votre Canvas. Cependant, si la variable de contexte n'a pas été créée correctement, les étapes suivantes de votre canvas ne s'exécuteront pas correctement non plus. Par exemple, si vous créez une étape Contexte pour attribuer un rendez-vous aux utilisateurs et que vous définissez la valeur du rendez-vous sur une date passée, l'e-mail de rappel de votre étape Message ne sera pas envoyé.

## Conversion des chaînes de contenu connecté en JSON

Lorsqu'un [appel de contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) est effectué dans une étape Context, le JSON renvoyé par l'appel est évalué comme un type de données de chaîne de caractères afin d'assurer la cohérence et de prévenir les erreurs. Si vous souhaitez convertir cette chaîne de caractères en JSON, convertissez-la en utilisant `as_json_string`. Par exemple :

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Résolution des problèmes

### Variables de contexte non valides

Une variable de contexte est considérée comme invalide lorsque

- L'appel à un contenu connecté intégré échoue.
- Au moment de l'exécution, l'expression Liquid renvoie une valeur qui ne correspond pas au type de données ou qui est vide (null).

Par exemple, si le type de données de la variable contextuelle est **Number** mais que l'expression Liquid renvoie une chaîne de caractères, elle n'est pas valide.

Dans ces conditions :
- L'utilisateur passe à l'étape suivante.
- L'analyse des étapes du canvas considère cela comme _non mis à jour_.

Lors de la résolution des problèmes, surveillez les indicateurs de _non-actualisation_ pour vérifier que votre variable contextuelle est correctement mise à jour. Si la variable de contexte n'est pas valide, vos utilisateurs peuvent continuer dans votre Canvas après l'étape du contexte, mais ne pourront pas se qualifier pour les étapes suivantes.

Veuillez vous référer à [la section Types de données]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#data-types) pour consulter les exemples de configuration pour chaque type de données.

### Retards dans l'envoi avec le contenu connecté

Tous les utilisateurs d'un lot sont traités avant que les utilisateurs suivants ne puissent procéder à leur avancement. Une fois le traitement par lots terminé, les utilisateurs ayant réussi effectuent l'avancement vers l'étape suivante, tandis que ceux ayant échoué font l'objet d'une nouvelle tentative séparée. Les utilisateurs ayant réussi n'attendent pas que les nouvelles tentatives aboutissent avant d'effectuer l'avancement vers l'étape suivante.

**Comportement de réessai** : Les étapes de contexte (et toutes les étapes du canvas) utilisent des mécanismes de nouvelle tentative spécifiques à Canvas, et non le comportement de nouvelle tentative standard du contenu connecté. Si un appel de contenu connecté échoue, Braze réessaie l'étape environ 13 fois avec des délais exponentiels. Si toutes les tentatives échouent, l'utilisateur quitte le canvas.

{% alert note %}
L'étiquette`:retry` utilisée dans le contenu connecté standard ne s'applique pas aux appels de contenu connecté effectués dans les étapes du canvas. Les étapes du canvas disposent de leur propre logique de réessai optimisée pour les workflows du canvas.
{% endalert %}

**Délai de traitement** : Le temps nécessaire pour traiter tous les utilisateurs via une étape Context dépend des éléments suivants :
- Le nombre d'utilisateurs entrant dans l'étape
- Utilisation du contenu connecté (et son temps de réponse)
- La taille du lot (par défaut, 1 000 utilisateurs par lot)

Si votre endpoint de contenu connecté est soumis à des limites de débit, veuillez noter que les étapes Context traitent les utilisateurs de manière séquentielle au sein de chaque lot, ce qui contribue naturellement au respect des limites de débit. Cependant, plusieurs lots sont traités en parallèle. Veuillez donc vous assurer que votre endpoint peut gérer les demandes simultanées provenant de plusieurs lots.

## Normalisation de la cohérence des fuseaux horaires

Bien que la plupart des propriétés d'événement utilisant le type d'horodatage soient déjà en UTC dans Canvas, il existe quelques exceptions. Avec l'ajout de Canvas Context, toutes les propriétés d'événement d'horodatage par défaut dans les canevas basés sur les actions sont en UTC. Ce changement s'inscrit dans le cadre d'une initiative plus large visant à garantir une expérience plus prévisible et cohérente lors de la modification des étapes du canvas et des messages. Veuillez noter que cette modification affecte toutes les canevas basées sur des actions, que la canevas spécifique utilise ou non une étape de contexte.

{% alert important %}
Dans tous les cas, nous recommandons fortement d'utiliser [des filtrestime_zone Liquid]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) pour que les horodatages soient représentés dans le fuseau horaire souhaité. Veuillez vous référer à cette [question fréquemment posée](#faq-example) pour obtenir un exemple.
{% endalert %}

## Foire aux questions

### Quels changements ont été observés depuis que Canvas Context est devenu accessible à tous ?

Maintenant que Canvas Context est disponible pour tous, les détails suivants s'appliquent :

- Tous les horodatages de [type]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) [date/heure]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) provenant [des propriétés d'événement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) dans les canevas basés sur des actions sont exprimés en [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time).
- Cette modification affecte toutes les canevas basées sur des actions, que la canevas spécifique utilise ou non une étape Contexte.

#### Quelle est la raison de ce changement ?

Ce changement s'inscrit dans le cadre d'une initiative plus large visant à offrir une expérience plus prévisible et cohérente lors de la modification des étapes du canvas et des messages.

#### Les canevas déclenchés par API ou soumis à la planification sont-ils affectés par ce changement ?

Non.

#### Ce changement affecte-t-il les propriétés d'entrée de canvas ?

Oui, cela a une incidence`canvas_entry_properties`si le`canvas_entry_property`  est utilisé dans un canvas basé sur les actions et que le type de propriété est `time`. Dans tous les cas, nous recommandons d'utiliser des filtres`time_zone` Liquid pour que les horodatages soient représentés dans le fuseau horaire souhaité.

Voici un exemple illustrant comment procéder :

| Liquid dans l'étape Message | Sortie | Est-ce la manière appropriée de représenter correctement les fuseaux horaires dans Liquid ? |
|---|---|---|
| {% raw %}```{{canvas_entry_properties.${timestamp_property}}}```{% endraw %} | `2025-08-05T08:15:30:250-0800` | Non |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 4:15pm` | Non
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 8:15am` | Oui |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Pourriez-vous fournir un exemple concret illustrant comment le nouveau comportement de l'horodatage pourrait affecter mes messages ? {#faq-example}

Supposons que nous disposions d'un canevas basé sur les actions qui contient les éléments suivants dans une étape Message :

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

Pour spécifier clairement un fuseau horaire, nous pouvons utiliser des filtres`time_zone` Liquid comme suit : 

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Cela génère le message suivant : 

```
Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!
```

Étant donné que le fuseau horaire Amérique/Los Angeles est spécifié à l'aide de Liquid, l'horodatage est ici en heure PST.

Le fuseau horaire préféré peut également être envoyé dans la charge utile des propriétés d'événement et utilisé dans la logique Liquid :

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

### En quoi les variables de contexte diffèrent-elles des propriétés d'entrée dans le canvas ?

Les propriétés d'entrée canvas sont incluses en tant que variables de contexte canvas. Cela signifie que vous pouvez envoyer les propriétés de l'entrée Canvas à l'aide de l'API Braze et y faire référence dans d'autres étapes, de manière similaire à l'utilisation d'une variable de contexte avec l'extrait de code Liquid.

### Les variables peuvent-elles faire référence les unes aux autres dans une étape du contexte singulier ?

Oui. Toutes les variables d'une étape Context sont évaluées dans un ordre précis, ce qui signifie que vous pourriez configurer les variables de contexte suivantes :

| Variable de contexte | Valeur | Description |
|---|---|---|
|`favorite_cuisine`| {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | Type de cuisine préféré de l'utilisateur. |
|`promo_code`| {% raw %}`EATFRESH`{% endraw %} | Le code de réduction disponible pour un utilisateur. |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{context.${promo_code}}} "on delivery from your favorite" {{context.${favorite_cuisine}}} restaurants!"`{% endraw %} | Un message personnalisé qui combine les variables précédentes. Dans une étape Message, vous pourriez utiliser l'extrait de code Liquid {% raw %}`{{context.${personalized_message}}}`{% endraw %} pour faire référence à la variable contextuelle afin d'envoyer un message personnalisé à chaque utilisateur. Vous pouvez également utiliser une étape Contexte pour enregistrer la valeur [du code promotionnel]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) et l'utiliser comme modèle dans d'autres étapes du canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Cela s'applique également à plusieurs étapes de Contexte. Imaginez par exemple la séquence suivante :

1. Une étape Contexte initiale crée une variable appelée `JobInfo` avec la valeur `job_title`.
2. Une étape Message fait référence à {% raw %}`{{context.${JobInfo}}}`{% endraw %} et affiche `job_title` à l'intention de l'utilisateur.
3. Plus tard, une étape Contexte met à jour la variable contexte, en changeant la valeur de `JobInfo` en `job_description`.
4. Toutes les étapes suivantes qui font référence à  `JobInfo`utilisent désormais la valeur mise à`job_description` jour.

Les variables contextuelles utilisent leur valeur la plus récente tout au long du canvas, chaque mise à jour affectant toutes les étapes suivantes qui font référence à cette variable.
