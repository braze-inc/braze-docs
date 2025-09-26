---
nav_title: Contexte 
article_title: Contexte 
alias: /context/
page_order: 1.5
page_type: reference
description: "Cet article de référence explique comment créer et utiliser des étapes contextuelles dans votre Canvas."
tool: Canvas

---

# Contexte

> Les étapes du canvas vous permettent de créer et de mettre à jour une ou plusieurs variables pour un utilisateur au fur et à mesure qu'il se déplace dans un canvas. Par exemple, si vous avez un Canvas qui gère les remises saisonnières, vous pouvez utiliser une variable de contexte pour stocker un code de remise différent chaque fois qu'un utilisateur entre dans le Canvas.

{% alert important %}
Les étapes du contexte sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

## Fonctionnement

![Une étape du canvas est la première étape d'un canvas.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Les étapes du contexte vous permettent de créer et d'utiliser des données temporaires au cours du parcours d'un utilisateur dans un canvas spécifique. Ces données n'existent que dans le cadre de ce parcours Canvas et ne persistent pas dans les différents Canvas ou en dehors de la session.

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

Par exemple, 
{% raw %}`{{context.${flight_time}}}{% endraw %}` pourrait renvoyer l'heure de vol planifiée de l'utilisateur.

Chaque fois qu'un utilisateur entre dans le canvas - même s'il l'a déjà fait auparavant - les variables contextuelles seront redéfinies en fonction des dernières données d'entrée et de la configuration du canvas. Cela permet aux trajets de rester personnalisés et précis, même pour les utilisateurs ayant plusieurs entrées.

## Création d'une étape contextuelle

### Étape 1 : Ajouter une étape

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
5. (Facultatif) Pour ajouter des variables, sélectionnez **Ajouter une variable contextuelle** et répétez les étapes 1 à 4.
6. Lorsque vous avez terminé, sélectionnez **Terminé**.

Vous pouvez désormais utiliser votre variable contextuelle partout où vous utilisez Liquid, comme dans les étapes Message et Mise à jour utilisateur, en sélectionnant **Ajouter une personnalisation**. Pour une présentation complète, voir [Utilisation des variables de contexte](#using-context-variables).

### Étape 3 : Test des chemins d'accès utilisateur (facultatif)

Si la variable de contexte est valide, vous pouvez y faire référence dans l'ensemble de votre Canvas. Cependant, si la variable de contexte n'a pas été créée correctement, les étapes ultérieures de votre canvas ne fonctionneront pas non plus correctement. Nous vous recommandons de tester et de [prévisualiser vos parcours utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) pour vous assurer que vos messages sont envoyés à la bonne audience. Soyez attentifs aux scénarios courants qui créent des [variables de contexte non valides](#troubleshooting).

Par exemple, si vous créez une étape Contexte pour attribuer une heure de rendez-vous aux utilisateurs, mais que vous fixez la valeur de l'heure de rendez-vous à une date passée, l'e-mail de rappel que vous créez dans votre étape Message ne sera jamais envoyé. 

## Types de données des variables contextuelles {#context-variable-types}

Les variables contextuelles créées ou mises à jour au cours de l'étape peuvent se voir attribuer les types de données suivants.

{% alert note %}
Les variables de contexte ont les mêmes formats attendus pour les types de données que les [événements personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format), mais les variables de contexte ne prennent pas en charge les objets imbriqués.
{% endalert %}

| Type de données | Exemple de nom de variable | Exemple de valeur |
|---|---|---|
|Valeur booléenne| programme_de_fidélité |{% raw %}<code>true</code>{% endraw %}| 
|Nombre| score_de_crédit |{% raw %}<code>740{% endraw %}|
|Chaîne de caractères| nom_produit |{% raw %}<code>green_tea</code>{% endraw %} |
|Tableau| produits_favoris|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|Date| dernière_date_d'achat|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|Objet (aplati) | profil_utilisateur|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Utilisation de variables contextuelles {#using-context-variables}

Par exemple, supposons que vous souhaitiez informer les passagers de leur accès au salon VIP avant leur prochain vol. Ce message ne doit être envoyé qu'aux passagers ayant acheté un billet de première classe. Une variable de contexte est un moyen souple de suivre ces informations.

Les utilisateurs entreront dans la toile lorsqu'ils achèteront un billet d'avion. Pour déterminer l'admissibilité à l'accès au salon, nous créerons une variable contextuelle appelée `lounge_access_granted` dans une étape Contexte, puis nous ferons référence à cette variable contextuelle dans les étapes suivantes du parcours de l'utilisateur.

![Variable contextuelle mise en place pour déterminer si un passager a droit à l'accès au salon VIP.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

Dans cette étape du Contexte, nous utiliserons {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} pour déterminer si le type de vol qu'ils ont acheté est `first_class`.

Ensuite, nous allons créer une étape Message pour cibler les utilisateurs pour lesquels {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} est `true`. Ce message sera une notification push qui comprendra des informations personnalisées sur le salon. En fonction de cette variable contextuelle, les passagers éligibles recevront les messages pertinents avant leur vol.

- Les passagers du billet de première classe recevront "Profitez d'un accès exclusif au salon VIP !
- Les passagers de la classe affaires et de la classe économique recevront "Surclassez votre vol pour bénéficier d'un accès exclusif au salon VIP.

![Une étape Message avec différents messages à envoyer, en fonction du type de billet d'avion acheté.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
Vous pouvez ajouter des [options de retard personnalisées]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) avec les informations de l'étape Contexte, ce qui signifie que vous pouvez sélectionner la variable qui retarde les utilisateurs.
{% endalert %}

## Conversion des chaînes de contenu connecté en JSON

Lors d'un [appel au contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) dans une étape de Context, le JSON renvoyé par l'appel sera évalué comme un type de données de type chaîne de caractères pour des raisons de cohérence et de prévention des erreurs. Si vous souhaitez convertir cette chaîne de caractères en JSON, convertissez-la en utilisant `as_json_string`. Par exemple :

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Résolution des problèmes{#troubleshooting}

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

## Foire aux questions

### En quoi les variables de contexte diffèrent-elles des propriétés d'entrée dans le canvas ?

Si vous participez à l'étape du canvas en accès anticipé, les propriétés d'entrée de Canvas sont désormais incluses en tant que variables de contexte de Canvas. Cela signifie que vous pouvez envoyer les propriétés de l'entrée Canvas à l'aide de l'API Braze et y faire référence dans d'autres étapes, de manière similaire à l'utilisation d'une variable de contexte avec l'extrait de code Liquid.

### Les variables peuvent-elles faire référence les unes aux autres dans une étape du contexte singulier ?

Oui. Toutes les variables d'une étape contextuelle sont évaluées dans l'ordre, ce qui signifie que vous pourriez avoir les variables contextuelles suivantes configurées :

| Variable de contexte | Valeur | Description |
|---|---|---|
|`favorite_cuisine`| {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | Type de cuisine préféré de l'utilisateur. |
|`promo_code`| {% raw %}`EATFRESH`{% endraw %} | Le code de réduction disponible pour un utilisateur. |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{promo_code}} "on delivery from your favorite" {{favorite_cuisine}} restaurants!"`{% endraw %} | Un message personnalisé qui combine les variables précédentes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Dans une étape Message, vous pourriez utiliser l'extrait de code Liquid {% raw %}`{{context.${personalized_message}}}`{% endraw %} pour faire référence à la variable contextuelle afin d'envoyer un message personnalisé à chaque utilisateur.

Cela s'applique également à plusieurs étapes de Contexte. Imaginez par exemple la séquence suivante :
1. Une étape Contexte initiale crée une variable appelée `JobInfo` avec la valeur `job_title`.
2. Une étape Message fait référence à {% raw %}`{{context.${JobInfo}}}`{% endraw %} et affiche `job_title` à l'intention de l'utilisateur.
3. Plus tard, une étape Contexte met à jour la variable contexte, en changeant la valeur de `JobInfo` en `job_description`.
4. Toutes les étapes suivantes qui font référence à `JobInfo` utiliseront désormais la valeur actualisée `job_description`.

Les variables contextuelles utilisent leur valeur la plus récente tout au long du canvas, chaque mise à jour affectant toutes les étapes suivantes qui font référence à cette variable.


