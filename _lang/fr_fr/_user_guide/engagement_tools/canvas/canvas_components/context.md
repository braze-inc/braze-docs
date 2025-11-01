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
Les étapes du contexte sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.<br><br>Notez que l'abonnement à l'étape du canvas en accès anticipé modifiera la façon dont les horodatages sont gérés dans tous vos canevas. Pour en savoir plus, consultez la rubrique [Normalisation de la cohérence des fuseaux horaires](#time-zone-consistency-standardization).
{% endalert %}

## Comment cela fonctionne-t-il ?

!Une étape du Contexte comme première étape d'un Canvas.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Les étapes du contexte vous permettent de créer et d'utiliser des données temporaires au cours du parcours d'un utilisateur dans un Canvas spécifique. Ces données n'existent que dans le cadre de ce parcours Canvas et ne persistent pas dans les différents Canvas ou en dehors de la session.

Dans ce cadre, chaque étape Contexte peut définir plusieurs variables de contexte - des données temporaires qui vous permettent de personnaliser les délais, de segmenter les utilisateurs de manière dynamique et d'enrichir les envois sans modifier de manière permanente les informations de profil de l'utilisateur.

Par exemple, si vous gérez des réservations de vols, vous pouvez créer une variable contextuelle pour l'heure de vol planifiée de chaque utilisateur. Vous pourriez alors définir des délais par rapport à l'heure de vol de chaque utilisateur et envoyer des rappels personnalisés à partir du même Canvas.

Vous pouvez définir des variables de contexte de deux manières :

- **A l'entrée de la toile :** Lorsque les utilisateurs entrent dans un Canvas, les données de l'événement ou du déclencheur API peuvent automatiquement alimenter les variables de contexte.
- **Dans une étape de Contexte :** Vous pouvez définir ou mettre à jour des variables de contexte manuellement dans le canvas en ajoutant une étape Contexte.

Chaque variable contextuelle comprend

- Un nom (tel que `flight_time` ou `subscription_renewal_date`)
- Un [type de données](#context-variable-types) (comme un nombre, une chaîne de caractères, une heure ou un tableau).
- Une valeur que vous attribuez à l'aide de [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) ou de l'outil **Ajouter une personnalisation**.

Une fois définie, vous pouvez utiliser une variable contextuelle dans l'ensemble du canvas en y faisant référence sous la forme suivante : {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

Par exemple, {% raw %}`{{context.${flight_time}}}`{% endraw %} pourrait renvoyer l'heure du vol planifié de l'utilisateur.

Chaque fois qu'un utilisateur entre dans le canvas - même s'il l'a déjà fait auparavant - les variables contextuelles seront redéfinies en fonction des dernières données d'entrée et de la configuration du canvas. Cette approche par état permet à chaque entrée de Canvas de conserver son propre contexte indépendant, ce qui permet aux utilisateurs d'avoir plusieurs états actifs au sein d'un même parcours tout en conservant le contexte spécifique à chaque état.

Par exemple, si un client a deux vols à venir, il aura deux états de parcours distincts en cours d'exécution simultanément, chacun avec ses propres variables de contexte spécifiques au vol, comme l'heure de départ et la destination. Cela vous permet d'envoyer des rappels personnalisés sur leur vol de 14 heures pour New York tout en envoyant des mises à jour différentes sur leur vol de 8 heures pour Los Angeles demain, de sorte que chaque message reste pertinent pour la réservation spécifique.

## Considérations

- Vous pouvez avoir jusqu'à 10 variables de contexte par étape de contexte.
- Chaque nom de variable contextuelle peut comporter jusqu'à 100 caractères.
- Les noms des variables contextuelles doivent être des identifiants valides (lettres, chiffres, caractères de soulignement uniquement).
- Les définitions des variables contextuelles peuvent comporter jusqu'à 10 240 caractères. 
- Les variables de contexte transmises dans un canevas déclenché par une API partagent les mêmes espaces de noms que les variables de contexte créées dans une étape du canevas. Cela signifie que si vous envoyez une variable `purchased_item` dans l'[objet contextuel de l']({{site.baseurl}}/api/objects_filters/context_object)endpoint `/canvas/trigger/send`, elle peut être référencée en tant que {% raw %}`{context.${purchased_item}}`{% endraw %}, et la redéclaration de cette variable dans une étape du canvas remplacera ce qui a été envoyé précédemment.
- Vous pouvez stocker jusqu'à 50 Ko par pas de contexte, répartis jusqu'à 10 variables par pas. Les variables dont la taille totale dépasse 50 Ko en une seule étape ne seront pas évaluées ni stockées pour l'utilisateur. Ces tailles sont calculées l'une après l'autre. Par exemple, si vous avez 3 variables dans une étape Contexte :
  - Variable 1 : 30 KB
  - Variable 2 : 19 KB
  - Variable 3 : 2 KB
  - Cela signifie que la variable 3 ne sera pas évaluée ou stockée parce que la somme de toutes les autres variables contextuelles dépasse 50 Ko.

## Création d'une étape contextuelle

### Étape 1 : Ajouter une étape

Ajoutez une étape à votre Canvas, puis glissez-déposez le composant depuis la barre latérale, ou cliquez sur le bouton plus de <i class="fas fa-plus-circle"></i> et sélectionnez **Contexte**.

### Étape 2 : Définir les variables

{% alert note %}
Vous pouvez définir jusqu'à 10 variables de contexte pour chaque étape de Contexte.
{% endalert %}

Pour définir une variable de contexte :

1. Donnez un **nom** à votre variable contextuelle.
2. Sélectionnez un [type de données](#context-variable-types).
3. Rédigez manuellement une expression Liquid ou utilisez **Ajouter une personnalisation** pour créer un extrait de code Liquid à partir d'attributs préexistants.
4. Sélectionnez **Aperçu** pour vérifier la valeur de votre variable contextuelle.
5. (Facultatif) Pour ajouter des variables, sélectionnez **Ajouter une variable contextuelle** et répétez les étapes 1 à 4.
6. Lorsque vous avez terminé, sélectionnez **Terminé**.

Vous pouvez désormais utiliser votre variable contextuelle partout où vous utilisez Liquid, comme dans les étapes Message et Mise à jour utilisateur, en sélectionnant **Ajouter une personnalisation**. Pour une présentation complète, voir [Utilisation des variables de contexte](#using-context-variables).

## Types de données des variables contextuelles {#context-variable-types}

Les variables contextuelles créées ou mises à jour au cours de l'étape peuvent se voir attribuer les types de données suivants.

{% alert note %}
Les variables contextuelles ont les mêmes formats attendus pour les types de données que les [événements personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format). <br><br>Pour les objets imbriqués et les tableaux d'objets, utilisez le [filtre`as_json_string` Liquid](#converting-connected-content-strings-to-json). Si vous créez le même objet dans une étape Contexte, vous devrez effectuer le rendu de l'objet à l'aide de `as_json_string`, par exemple {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| Type de données | Exemple de nom de variable | Exemple de valeur |
|---|---|---|
|Booléen| loyalty_program |{% raw %}<code>vrai</code>{% endraw %}| 
|Nombre| credit_score |{% raw %}<code>740{% endraw %}|
|Chaîne de caractères| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|Réseau| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|Heure (en UTC) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|Objet (aplati) | user_profile|{% raw %}<code>{<br> "first_name": "{{user.first_name}}",<br> "last_name": "{{user.last_name}}",<br> "e-mail" : "{{user.email}}",<br> "loyalty_points": {{user.loyalty_points}},<br> "preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Par défaut, le type de données de l'heure est en UTC. Si vous utilisez un type de données chaîne de caractères pour stocker une valeur temporelle, vous pouvez définir l'heure comme un fuseau horaire différent tel que PST. 

Par exemple, si vous envoyez un message à un utilisateur la veille de son anniversaire, vous enregistrerez la variable contextuelle en tant que type de données temporel, car la logique liquide est associée à l'envoi la veille. Toutefois, si vous envoyez un message de vacances le jour de Noël (25 décembre), vous n'aurez pas besoin de référencer l'heure en tant que variable dynamique. Il est donc préférable d'utiliser un type de données de type chaîne de caractères.

## Utilisation de variables contextuelles {#using-context-variables}

Par exemple, supposons que vous souhaitiez informer les passagers de leur accès au salon VIP avant leur prochain vol. Ce message ne doit être envoyé qu'aux passagers ayant acheté un billet de première classe. Une variable de contexte est un moyen souple de suivre ces informations.

Les utilisateurs entreront dans la toile lorsqu'ils achèteront un billet d'avion. Pour déterminer l'admissibilité à l'accès au salon, nous créerons une variable contextuelle appelée `lounge_access_granted` dans une étape Contexte, puis nous ferons référence à cette variable contextuelle dans les étapes suivantes du parcours de l'utilisateur.

Une variable contextuelle a été mise en place pour déterminer si un passager a droit à l'accès au salon VIP.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

Dans cette étape du Contexte, nous utiliserons {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} pour déterminer si le type de vol qu'ils ont acheté est `first_class`.

Ensuite, nous allons créer une étape Message pour cibler les utilisateurs pour lesquels {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} est `true`. Ce message sera une notification push qui comprendra des informations personnalisées sur le salon. En fonction de cette variable contextuelle, les passagers éligibles recevront les messages pertinents avant leur vol.

- Les passagers du billet de première classe recevront "Profitez d'un accès exclusif au salon VIP !
- Les passagers de la classe affaires et de la classe économique recevront "Surclassez votre vol pour bénéficier d'un accès exclusif au salon VIP.

!Une étape de message avec différents messages à envoyer, selon le type de billet d'avion acheté.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
Vous pouvez ajouter des [options de retard personnalisées]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) avec les informations de l'étape Contexte, ce qui signifie que vous pouvez sélectionner la variable qui retarde les utilisateurs.
{% endalert %}

### Pour les parcours d'action et les critères de sortie

Vous pouvez exploiter la comparaison des filtres de propriétés avec des variables de contexte ou des attributs personnalisés dans ces actions de déclenchement : **Réaliser un événement personnalisé** et **effectuer un achat**. Ces déclencheurs d'action prennent également en charge les filtres de propriété pour les propriétés de base et les propriétés imbriquées. 

- Lors de la comparaison avec les propriétés de base, les comparaisons disponibles correspondront au type de propriété défini par l'événement personnalisé. Par exemple, les propriétés de chaînes de caractères auront des correspondances d'expression régulière exactement égales. Les propriétés booléennes seront vraies ou fausses. 
- Lors de la comparaison avec des propriétés imbriquées, les types ne sont pas prédéfinis. Vous pouvez donc sélectionner des comparaisons entre plusieurs types de données pour les booléens, les nombres, les chaînes de caractères, l'heure et le jour de l'année, comme pour les comparaisons avec des attributs personnalisés imbriqués. Si vous sélectionnez un type de données qui ne correspond pas au type de données réel de la propriété imbriquée au moment de la comparaison, l'utilisateur ne correspondra pas au parcours d'action ou aux critères de sortie.

#### Exemples de parcours d'action

{% alert important %}
Pour les comparaisons d'attributs personnalisés, nous utiliserons la valeur de l'attribut personnalisé au moment où l'action est effectuée. Cela signifie qu'un utilisateur ne correspondra pas au groupe de parcours d'action si cet attribut personnalisé n'est pas renseigné au moment de la comparaison ou si la valeur de l'attribut personnalisé ne correspond pas aux comparaisons de propriétés définies. C'est le cas même si l'utilisateur aurait correspondu lorsqu'il est entré dans l'étape du parcours d'action.
{% endalert %}

{% tabs %}
{% tab Perform custom event %}

Le parcours d'action suivant est mis en place pour trier les utilisateurs qui ont effectué l'événement personnalisé `Account_Created` avec la propriété de base `source` vers la variable contextuelle `app_source_variable`.

Un exemple de parcours d'action qui fait référence à une variable de contexte lors de l'exécution d'un événement personnalisé.]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Make purchase %}

Le parcours d'action suivant est mis en place pour faire correspondre la propriété de base `brand` pour le nom de produit spécifique `shoes` à une variable de contexte `promoted_shoe_brand`.

Un exemple de parcours d'action qui fait référence à une variable de contexte lors d'un achat.]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### Exemples de critères de sortie

{% tabs %}
{% tab Perform custom event %}

Les critères de sortie stipulent qu'à tout moment du parcours d'un utilisateur dans le Canvas, il quittera le Canvas si :

- Ils exécutent l'événement personnalisé " **Abandon de panier"** et
- La propriété de base **Item in Cart** correspond à la valeur chaîne de caractères de la variable de contexte `cart_item_threshold`.

Critères de sortie mis en place pour quitter un utilisateur s'il effectue un événement personnalisé basé sur la variable de contexte.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

Les critères de sortie stipulent qu'à tout moment du parcours d'un utilisateur dans le Canvas, il quittera le Canvas si

- Ils effectuent un achat spécifique pour le nom du produit "livre", et
- La propriété d'achat "loyalty_program" est égale à l'attribut personnalisé "VIP" de l'utilisateur.

\![Critères de sortie mis en place pour quitter un utilisateur s'il effectue un achat.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### Filtres de variables contextuelles

Vous pouvez créer des filtres qui utilisent des variables de contexte préalablement déclarées dans les étapes [Parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) et [Arbre]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) [décisionnel]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split).

{% alert important %}
Les filtres d'une variable contextuelle ne sont disponibles que pour les parcours d'audience et les étapes de l'arbre décisionnel.
{% endalert %}

Les variables de contexte sont déclarées et accessibles uniquement dans la portée d'un Canvas, ce qui signifie qu'elles ne peuvent pas être référencées dans des segments. Les filtres d'audience fonctionnent de la même manière dans les parcours d'audience et les étapes décisionnelles. Les parcours d'audience représentent des groupes multiples, tandis que les étapes décisionnelles représentent des décisions binaires.

!Exemple d'étape décisionnelle avec la possibilité de créer un filtre avec une variable contextuelle.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

De la même manière que les variables contextuelles de Canvas ont des types prédéfinis, les comparaisons entre les variables contextuelles et les valeurs statiques doivent avoir des [types de données correspondants]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types). Le filtre de variables contextuelles permet d'effectuer des comparaisons entre plusieurs types de données pour les booléens, les nombres, les chaînes de caractères, l'heure et le jour de l'année, de manière similaire aux comparaisons pour les [attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/).

{% alert note %}
Utilisez le même type de données pour votre variable de contexte et votre comparaison. Par exemple, si votre variable de contexte est un type de données temporelles, utilisez des comparaisons temporelles (telles que "avant" ou "après"). L'utilisation de types de données non concordants (comme les comparaisons de chaînes de caractères avec une variable de contexte temporel) peut entraîner un comportement inattendu.
{% endalert %}

Voici un exemple de filtre de variable contextuelle comparant la variable contextuelle `product_name` à l'expression régulière `/braze/`.

\![Configuration d'un filtre pour la variable contextuelle "product_name" correspondant à l'expression régulière "/braze/".]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Comparaison avec des variables de contexte ou des attributs personnalisés

En basculant l'option **Comparer à une variable de contexte ou à un attribut personnalisé**, vous pouvez construire des filtres de variables de contexte qui se comparent à des variables de contexte préalablement définies ou à des attributs personnalisés de l'utilisateur. Cela peut être utile pour effectuer des comparaisons dynamiques par utilisateur, comme celles déclenchées par l'API `context`, ou pour condenser une logique de comparaison complexe définie à travers des variables de contexte.

{% tabs %}
{% tab Example 1 %}

Imaginons que vous souhaitiez envoyer un rappel personnalisé aux utilisateurs après une période d'inactivité dynamique, ce qui inclut que toute personne ne s'étant pas connectée à votre appli au cours des trois derniers jours, devrait recevoir un message.

Vous disposez d'une variable de contexte `re_engagement_date` définie comme {% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %}. Notez que `3 days` peut être un montant variable qui est également stocké en tant qu'attribut personnalisé de l'utilisateur. Ainsi, si le `re_engagement_date` se trouve après le `last_login_date` (stocké en tant qu'attribut personnalisé sur le profil utilisateur), un message lui sera envoyé.

\![Une configuration de filtre avec des attributs personnalisés comme type de personnalisation pour la variable de contexte "re_engagement_date" après l'attribut personnalisé "last_login_date".]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab Example 2 %}

Le filtre suivant compare la variable contextuelle `reminder_date` à la variable contextuelle `appointment_deadline`. Cela peut aider à regrouper les utilisateurs dans une étape de parcours d'audience afin de déterminer s'ils doivent recevoir des rappels supplémentaires avant la date limite de leur rendez-vous.

\![Une configuration de filtre avec des variables de contexte comme type de personnalisation pour la variable de contexte "reminder_date" sur la variable de contexte "appointment_deadline".]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## Prévisualisation des parcours utilisateurs

Nous vous recommandons de tester et de [prévisualiser vos parcours utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) pour vous assurer que vos messages sont envoyés à la bonne audience et que les variables de contexte sont évaluées en fonction des résultats attendus.

{% alert note %}
Si vous prévoyez votre Canvas dans la section **Prévisualisation & Test d'envoi de l'** éditeur, l'horodatage dans la prévisualisation du message de test **ne sera pas** normalisé en UTC car ce panneau génère des prévisualisations sous forme de chaînes de caractères. Cela signifie que si un canvas est configuré pour accepter un objet `time`, l'aperçu du message ne donnera pas un aperçu précis de ce qui se passe lorsque le canvas est en ligne/en production/instantanée. Pour tester votre Canvas de la manière la plus précise, nous vous recommandons plutôt de prévisualiser les parcours des utilisateurs.
{% endalert %}

Veillez à observer les scénarios courants qui créent des variables de contexte non valides. Lors de la prévisualisation de votre parcours d'utilisateur, vous pouvez visualiser les résultats des étapes de délai personnalisées à l'aide de variables de contexte, ainsi que toutes les comparaisons d'étapes d'audience, de décision ou de parcours d'action qui font correspondre les utilisateurs à n'importe quelle variable de contexte.

Si la variable de contexte est valide, vous pouvez y faire référence dans l'ensemble de votre Canvas. Cependant, si la variable de contexte n'a pas été créée correctement, les étapes ultérieures de votre canvas ne fonctionneront pas non plus correctement. Par exemple, si vous créez une étape Contexte pour attribuer une heure de rendez-vous aux utilisateurs, mais que vous fixez la valeur de l'heure de rendez-vous à une date passée, l'e-mail de rappel de votre étape Message ne sera jamais envoyé.

## Conversion des chaînes de contenu connecté en JSON

Lors d'un [appel au contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) dans une étape de Context, le JSON renvoyé par l'appel sera évalué comme un type de données de type chaîne de caractères pour des raisons de cohérence et de prévention des erreurs. Si vous souhaitez convertir cette chaîne de caractères en JSON, convertissez-la en utilisant `as_json_string`. Par exemple :

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Normalisation de la cohérence des fuseaux horaires

Avec l'ajout de Canvas Context, tous les horodatages de [type datetime]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) provenant des [propriétés d'événements déclencheurs]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) dans les Canvas basés sur l'action seront toujours normalisés en [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). Auparavant, les horodatages des propriétés d'événement étaient normalisés en UTC, à [quelques exceptions]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) près. Désormais, l'expérience de modification des étapes du canvas et des messages sera plus cohérente.

Examinez cet exemple de la manière dont cette modification pourrait affecter un horodatage dans Canvas. Supposons que nous ayons un canevas basé sur des actions qui utilise une propriété d'événement dans la première étape du canevas avec l'étape de message suivante : 

{% raw %}
`Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!`
{% endraw %}

!Voyage en contexte avec un envoi de messages comme première étape.]({% image_buster /assets/img/context_timezone_example.png %}){: style="max-width:50%"}

L'étape aura également une charge utile d'événement comme : 

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
}
```

Historiquement, le message serait le suivant : `Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!`

Avec l'accès anticipé à Canvas Context, le message sera désormais le suivant : `Your appointment is scheduled for 2025-08-05 4:15pm, we’ll see you then!` Cela est dû au fait que l'horodatage est en UTC, c'est-à-dire 8 heures avant l'heure du Pacifique (le fuseau horaire spécifié dans la charge utile d'origine avec `-08:00`).

{% alert important %}
Pour tenir compte de ce changement d'horodatage, en toutes circonstances, nous vous recommandons vivement d'[utiliser les filtres Liquid]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) pour que les horodatages soient conseillés dans le fuseau horaire souhaité.
{% endalert %}

### Utilisation de Liquid pour indiquer un horodatage dans votre fuseau horaire préféré

Considérez l'extrait de code liquide suivant :

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Cette logique aboutit à la sortie suivante : `Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!`

Le fuseau horaire préféré peut également être envoyé dans la charge utile des propriétés d'événement et utilisé dans la logique Liquid : 

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

Voici un exemple d'extrait de code liquide :

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: canvas_entry_properties.${user_timezone} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

## Résolution des problèmes {#troubleshooting}

### Variables de contexte non valides

Une variable de contexte est considérée comme invalide lorsque
- L'appel à un contenu connecté intégré échoue.
- Au moment de l'exécution, l'expression Liquid renvoie une valeur qui ne correspond pas au type de données ou qui est vide (null).

Par exemple, si le type de données de la variable contextuelle est **Number** mais que l'expression Liquid renvoie une chaîne de caractères, elle n'est pas valide.

Dans ces conditions : 
- L'utilisateur passe à l'étape suivante. 
- L'analyse/analytique de l'étape du canvas considérera que cette information _n'a pas été mise à jour_.

Lors de la résolution des problèmes, surveillez les indicateurs de _non-actualisation_ pour vérifier que votre variable contextuelle est correctement mise à jour. Si la variable de contexte n'est pas valide, vos utilisateurs peuvent continuer dans votre Canvas après l'étape du contexte, mais ne pourront pas se qualifier pour les étapes suivantes.

Reportez-vous à la section [Types de données variables contextuelles](#context-variable-types) pour obtenir des exemples de configuration pour chaque type de données.

## Questions fréquemment posées

### En quoi les variables de contexte diffèrent-elles des propriétés d'entrée dans le canvas ?

Si vous participez à l'étape du canvas en accès anticipé, les propriétés d'entrée de Canvas sont désormais incluses en tant que variables de contexte de Canvas. Cela signifie que vous pouvez envoyer les propriétés de l'entrée Canvas à l'aide de l'API Braze et y faire référence dans d'autres étapes, de manière similaire à l'utilisation d'une variable de contexte avec l'extrait de code Liquid.

### Les variables peuvent-elles faire référence les unes aux autres dans une étape du contexte singulier ?

Oui. Toutes les variables d'une étape contextuelle sont évaluées dans l'ordre, ce qui signifie que vous pourriez avoir les variables contextuelles suivantes configurées :

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
4. Toutes les étapes suivantes qui font référence à `JobInfo` utiliseront désormais la valeur actualisée `job_description`.

Les variables contextuelles utilisent leur valeur la plus récente tout au long du canvas, chaque mise à jour affectant toutes les étapes suivantes qui font référence à cette variable.

### La normalisation de la cohérence des fuseaux horaires du contexte Canvas a-t-elle un impact sur les Canvas déclenchés par l'API ?

Non, cette modification n'a d'incidence que sur les toiles déclenchées par une action. Les horodatages envoyés dans les canevas déclenchés par l'API seront de type chaîne de caractères, et non de type heure, de sorte que le fuseau horaire d'origine est toujours préservé.

### Quel est le lien avec les exceptions relevées dans les propriétés d'entrée et les propriétés d'événement de Canvas ?

La participation à l'accès anticipé à Canvas Context supprime [ces exceptions]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know), que vous utilisiez ou non une étape de Canvas Context.
