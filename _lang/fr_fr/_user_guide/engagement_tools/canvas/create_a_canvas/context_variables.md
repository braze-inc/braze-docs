---
nav_title: Variables de contexte
article_title: Variables de contexte
page_type: reference
description: "Cet article de référence explique les variables de contexte dans les Canvas Braze, notamment leurs types, leur utilisation et les bonnes pratiques."
---

# Variables de contexte

> Les variables de contexte sont des données temporaires que vous pouvez créer et utiliser au cours du parcours d'un utilisateur dans un canvas spécifique. Elles vous permettent de personnaliser les délais, de segmenter les utilisateurs de manière dynamique et d'enrichir l'envoi de messages sans modifier de manière permanente les informations du profil utilisateur. Les variables de contexte n'existent que dans la session du Canvas et ne persistent pas entre différents Canvas ou en dehors de la session.

## Fonctionnement des variables de contexte

Les variables de contexte peuvent être définies de deux manières :

- **À l'entrée du Canvas :** Lorsque les utilisateurs entrent dans un Canvas, les données de l'événement ou du déclencheur API peuvent automatiquement alimenter les variables de contexte.
- **Dans une étape Contexte :** Vous pouvez définir ou mettre à jour manuellement les variables de contexte dans le Canvas en ajoutant une [étape Contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context).

Chaque variable de contexte comprend :

- Un nom (tel que `flight_time` ou `subscription_renewal_date`)
- Un type de données (tel que nombre, chaîne de caractères, heure ou tableau)
- Une valeur que vous attribuez à l'aide de [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) ou de l'outil **Ajouter une personnalisation**.

Une fois définie, vous pouvez utiliser une variable de contexte dans l'ensemble du Canvas en y faisant référence sous la forme suivante : {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

Par exemple, {% raw %}`{{context.${flight_time}}}`{% endraw %} pourrait renvoyer l'heure de vol prévue de l'utilisateur.

Chaque fois qu'un utilisateur entre dans le Canvas — même s'il l'a déjà fait auparavant — les variables de contexte sont redéfinies en fonction des dernières données d'entrée et de la configuration du Canvas. Cette approche avec état permet à chaque entrée dans le Canvas de conserver son propre contexte indépendant, ce qui permet aux utilisateurs d'avoir plusieurs états actifs au cours d'un même parcours tout en conservant le contexte spécifique à chaque état.

Par exemple, si un client a deux vols à venir, il aura deux états de parcours distincts fonctionnant simultanément, chacun avec ses propres variables de contexte spécifiques au vol, telles que l'heure de départ et la destination. Cela vous permet d'envoyer des rappels personnalisés concernant leur vol de 14 h à destination de New York, tout en envoyant des informations différentes concernant leur vol de 8 h à destination de Los Angeles le lendemain, de sorte que chaque message reste pertinent par rapport à la réservation spécifique.

## Considérations

Vous pouvez définir jusqu'à 10 variables de contexte par [étape Contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/). Chaque nom de variable peut comporter jusqu'à 100 caractères et doit être composé uniquement de lettres, de chiffres ou de traits de soulignement.

Les définitions des variables de contexte peuvent comporter jusqu'à 10 240 caractères. Si vous transmettez des variables de contexte à un Canvas déclenché par une API, elles partagent le même espace de noms que les variables créées dans une étape Contexte. Par exemple, si vous transmettez une variable `purchased_item` dans l'objet de contexte de l'[endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/), vous pouvez la référencer comme {% raw %}`{{context.${purchased_item}}}`{% endraw %}. Si vous redéfinissez cette variable dans une étape Contexte, la nouvelle valeur remplacera la valeur API pour le parcours de cet utilisateur.

Vous pouvez stocker jusqu'à 50 Ko par étape Contexte, répartis sur un maximum de 10 variables. Si la taille totale de toutes les variables d'une étape dépasse 50 Ko, les variables qui dépassent cette limite ne seront ni évaluées ni stockées. Par exemple, si vous avez trois variables dans une étape Contexte :

- Variable 1 : 30 Ko
- Variable 2 : 19 Ko
- Variable 3 : 2 Ko

La variable 3 ne sera ni évaluée ni stockée, car la somme des variables précédentes dépasse 50 Ko.

## Types de données

Les variables de contexte créées ou mises à jour dans l'étape peuvent se voir attribuer les types de données suivants.

{% alert note %}
Les variables de contexte ont les mêmes formats attendus pour les types de données que les [événements personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format). <br><br>Lorsque vous utilisez le type tableau, Braze tente d'analyser la valeur au format JSON, ce qui permet de créer correctement des tableaux d'objets. Si les objets contenus dans vos tableaux ne sont pas valides au format JSON, le résultat sera un simple tableau de chaînes de caractères. <br><br>Pour les objets imbriqués et les tableaux d'objets, utilisez le [filtre Liquid `as_json_string`](#converting-connected-content-strings-to-json). Si vous créez le même objet dans une étape Contexte, vous devrez effectuer le rendu de l'objet à l'aide de `as_json_string`, par exemple {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| Type de données | Exemple de nom de variable | Exemple de valeur |
|---|---|---|
|Valeur booléenne| loyalty_program |{% raw %}<code>true</code>{% endraw %}| 
|Nombre| credit_score |{% raw %}<code>740</code>{% endraw %}|
|Chaîne de caractères| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|Tableau| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|Tableau (d'objets)| pet_details |{% raw %}<code>[<br>&emsp;{ "id": 1, "type": "dog", "breed": "beagle", "name": "Gus" }<br>&emsp;,<br>&emsp;{ "id": 2, "type": "cat", "breed": "calico", "name": "Gerald" }<br>]</code>{% endraw %}|
|Heure (en UTC) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|Objet (aplati) | user_profile|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Par défaut, le type de données temporelles est en UTC. Si vous utilisez un type de données chaîne de caractères pour stocker une valeur temporelle, vous pouvez définir l'heure dans un fuseau horaire différent, tel que PST. 

Par exemple, si vous envoyez un message à un utilisateur la veille de son anniversaire, vous enregistrerez la variable de contexte sous forme de type de données temporelles, car il existe une logique Liquid associée à l'envoi la veille. En revanche, si vous envoyez un message de vœux le jour de Noël (25 décembre), il n'est pas nécessaire de faire référence à l'heure en tant que variable dynamique. Il est donc préférable d'utiliser un type de données chaîne de caractères.

Pour les types de données objet, vous pouvez utiliser la notation par points pour spécifier un chemin dans les données. Par exemple, si votre étape Contexte définit une variable de contexte `order_summary` avec cette structure :

```json
{
  "shipping": {
    "carrier": "overnight"
  }
}
```

Dans un filtre de [parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) ou d'[arbre décisionnel]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/), saisissez le chemin comme nom de variable de contexte en utilisant la notation par points (par exemple, `order_summary.shipping.carrier`). Lorsque le filtre est évalué, Braze résout ce chemin vers la valeur `overnight`.

En Liquid (par exemple dans une étape [Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)), utilisez plutôt {% raw %}`{{context.${order_summary}.shipping.carrier}}`{% endraw %}.

## Utilisation des variables de contexte

Vous pouvez utiliser les variables de contexte partout où vous utilisez Liquid dans un Canvas, par exemple dans les étapes [Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) et [Mise à jour utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update), en sélectionnant **Ajouter une personnalisation**. Pour les messages in-app et les bannières dans les étapes Message, vous pouvez sélectionner des variables de contexte pour déterminer quand le message doit expirer.

Par exemple, supposons que vous souhaitiez informer les passagers de leur accès au salon VIP avant leur prochain vol. Ce message ne doit être envoyé qu'aux passagers ayant acheté un billet de première classe. Une variable de contexte est un moyen flexible de suivre cette information.

Les utilisateurs entreront dans le Canvas lorsqu'ils achèteront un billet d'avion. Pour déterminer l'éligibilité à l'accès au salon, nous créerons une variable de contexte appelée `lounge_access_granted` dans une étape Contexte, puis nous ferons référence à cette variable de contexte dans les étapes suivantes du parcours de l'utilisateur.

![Variable de contexte configurée pour déterminer si un passager est éligible à l'accès au salon VIP.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

Dans cette étape Contexte, nous utiliserons {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} pour déterminer si le type de vol acheté est `first_class`.

Ensuite, nous créerons une étape Message pour cibler les utilisateurs pour lesquels {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} est `true`. Ce message sera une notification push contenant des informations personnalisées sur le salon. En fonction de cette variable de contexte, les passagers éligibles recevront les messages pertinents avant leur vol.

- Les passagers en première classe recevront : « Profitez d'un accès exclusif au salon VIP ! »
- Les passagers en classe affaires et en classe économique recevront : « Surclassez votre vol pour bénéficier d'un accès exclusif au salon VIP. »

![Une étape Message avec différents messages à envoyer, en fonction du type de billet d'avion acheté.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
Vous pouvez ajouter des [options de délai personnalisées]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) avec les informations de l'étape Contexte, ce qui signifie que vous pouvez sélectionner la variable qui retarde les utilisateurs.
{% endalert %}

### Pour les parcours d'action et les critères de sortie

Vous pouvez comparer les filtres de propriété avec des variables de contexte ou des attributs personnalisés dans les actions de déclenchement suivantes : **Réaliser un événement personnalisé** et **Effectuer un achat**. Ces déclencheurs d'action prennent également en charge les filtres de propriétés pour les propriétés de base et les propriétés imbriquées. 

- Lors de la comparaison avec les propriétés de base, les comparaisons disponibles correspondront au type de propriété défini par l'événement personnalisé. Par exemple, les propriétés de type chaîne de caractères auront des correspondances exactes ou par expression régulière. Les propriétés booléennes seront vraies ou fausses. 
- Lors de la comparaison avec des propriétés imbriquées, les types ne sont pas prédéfinis. Vous pouvez donc sélectionner des comparaisons entre plusieurs types de données pour les booléens, les nombres, les chaînes de caractères, l'heure et le jour de l'année, de manière similaire aux comparaisons pour les attributs personnalisés imbriqués. Si vous sélectionnez un type de données qui ne correspond pas au type de données réel de la propriété imbriquée au moment de la comparaison, l'utilisateur ne correspondra pas au parcours d'action ou aux critères de sortie.

#### Exemples de parcours d'action

{% alert important %}
Pour les comparaisons d'attributs personnalisés, la valeur utilisée sera celle de l'attribut personnalisé au moment où l'action est effectuée. Cela signifie qu'un utilisateur ne correspondra pas au groupe du parcours d'action si cet attribut personnalisé n'est pas renseigné au moment de la comparaison, ou si sa valeur ne correspond pas aux comparaisons de propriétés définies. Cela s'applique même si l'utilisateur aurait correspondu au moment de son entrée dans l'étape du parcours d'action.
{% endalert %}

{% tabs %}
{% tab Perform custom event %}

Le parcours d'action suivant est configuré pour trier les utilisateurs qui ont effectué l'événement personnalisé `Account_Created` avec la propriété de base `source` vers la variable de contexte `app_source_variable`.

![Exemple de parcours d'action qui fait référence à une variable de contexte lors de l'exécution d'un événement personnalisé.]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Make purchase %}

Le parcours d'action suivant est configuré pour faire correspondre la propriété de base `brand` pour le nom de produit spécifique `shoes` à une variable de contexte `promoted_shoe_brand`.

![Exemple de parcours d'action faisant référence à une variable de contexte lors d'un achat.]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### Exemples de critères de sortie

{% tabs %}
{% tab Perform custom event %}

Les critères de sortie stipulent qu'à tout moment du parcours d'un utilisateur dans le Canvas, celui-ci quittera le Canvas si :

- Il effectue l'événement personnalisé **Abandon du panier**, et
- La propriété de base **Article dans le panier** correspond à la valeur de chaîne de caractères de la variable de contexte `cart_item_threshold`.

![Critères de sortie configurés pour faire sortir un utilisateur s'il effectue un événement personnalisé basé sur la variable de contexte.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

Les critères de sortie stipulent qu'à tout moment du parcours d'un utilisateur dans le Canvas, celui-ci quittera le Canvas si :

- Il effectue un achat spécifique pour le nom de produit « book », et
- La propriété imbriquée « loyalty_program » de cet achat est identique à l'attribut personnalisé « VIP » de l'utilisateur.

![Critères de sortie configurés pour faire sortir un utilisateur s'il effectue un achat.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### Définir une expiration

Pour les [bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners/) et les [messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) dans une étape [Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) d'un Canvas, sélectionnez **Une durée après la disponibilité de l'étape** pour l'expiration, puis activez **Personnaliser la durée** pour piloter la fenêtre de disponibilité à partir d'une variable de contexte — par exemple, pour correspondre à la durée d'une promotion ou d'une réservation définie dans une étape Contexte.

**Personnaliser la durée** s'applique à cette option d'expiration basée sur la durée. Si vous choisissez plutôt **À une date et une heure spécifiques**, définissez l'expiration à l'aide des contrôles de date et d'heure.

### Délais des parcours d'action

Dans une étape [Parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/), sous **Fenêtre d'évaluation**, activez **Personnaliser le délai** pour définir la durée pendant laquelle les utilisateurs sont retenus dans l'étape à partir d'une variable de contexte. Utilisez cette option lorsque la période d'attente doit varier selon l'utilisateur en fonction de détails tels que le niveau ou la région.

### Filtres de variables de contexte

Vous pouvez créer des filtres qui utilisent des variables de contexte précédemment déclarées dans les étapes [Parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) et [Arbre décisionnel]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split).

{% alert note %}
Les filtres de variables de contexte sont uniquement disponibles pour les étapes Parcours d'audience et Arbre décisionnel.
{% endalert %}

Les variables de contexte sont déclarées et accessibles uniquement dans le cadre d'un Canvas, ce qui signifie qu'elles ne peuvent pas être référencées dans les segments. Les filtres de variables de contexte fonctionnent de manière similaire dans les étapes Parcours d'audience et Arbre décisionnel : les étapes Parcours d'audience représentent plusieurs groupes, tandis que les étapes Arbre décisionnel représentent des décisions binaires.

![Exemple d'étape Arbre décisionnel avec la possibilité de créer un filtre à l'aide d'une variable de contexte.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

Tout comme les variables de contexte du Canvas ont des types prédéfinis, les comparaisons entre les variables de contexte et les valeurs statiques doivent avoir des [types de données correspondants]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types). Le filtre de variable de contexte permet d'effectuer des comparaisons entre plusieurs types de données pour les booléens, les nombres, les chaînes de caractères, l'heure et le jour de l'année, de manière similaire aux comparaisons pour les [attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/).

{% alert note %}
Utilisez le même type de données pour votre variable de contexte et votre comparaison. Par exemple, si votre variable de contexte est de type temporel, utilisez des comparaisons temporelles (telles que « avant » ou « après »). L'utilisation de types de données incompatibles (tels que des comparaisons de chaînes de caractères avec une variable de contexte temporelle) peut entraîner un comportement inattendu.
{% endalert %}

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

Voici un exemple de filtre de variable de contexte comparant la variable de contexte `product_name` à l'expression régulière `/braze/`.

![Configuration d'un filtre pour que la variable de contexte « product_name » corresponde à l'expression régulière « /braze/ ».]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Comparaison avec des variables de contexte ou des attributs personnalisés

En activant le bouton **Comparer à une variable de contexte ou à un attribut personnalisé**, vous pouvez créer des filtres de variables de contexte qui comparent avec des variables de contexte ou des attributs personnalisés de l'utilisateur préalablement définis. Cela peut être utile pour effectuer des comparaisons dynamiques par utilisateur, comme celles déclenchées par une API `context`, ou pour condenser une logique de comparaison complexe définie à travers des variables de contexte.

{% tabs %}
{% tab Example 1 %}

Supposons que vous souhaitiez envoyer un rappel personnalisé aux utilisateurs après une période d'inactivité dynamique : toute personne qui ne s'est pas connectée à votre application au cours des trois derniers jours devrait recevoir un message.

Vous disposez d'une variable de contexte `re_engagement_date` définie comme {% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %}. Notez que `3 days` peut être un montant variable également stocké en tant qu'attribut personnalisé de l'utilisateur. Ainsi, si `re_engagement_date` est postérieur à `last_login_date` (enregistré en tant qu'attribut personnalisé dans le profil utilisateur), un message leur sera envoyé.

![Configuration d'un filtre avec des attributs personnalisés comme type de personnalisation pour la variable de contexte « re_engagement_date » après l'attribut personnalisé « last_login_date ».]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab Example 2 %}

Le filtre suivant compare la variable de contexte `reminder_date` pour qu'elle soit antérieure à la variable de contexte `appointment_deadline`. Cela peut aider à regrouper les utilisateurs dans une étape Parcours d'audience pour déterminer s'ils doivent recevoir des rappels supplémentaires avant la date limite de leur rendez-vous.

![Configuration d'un filtre avec des variables de contexte comme type de personnalisation pour la variable de contexte « reminder_date » sur la variable de contexte « appointment_deadline ».]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## Standardisation de la cohérence des fuseaux horaires

Bien que la plupart des propriétés d'événement utilisant le type d'horodatage soient déjà en UTC dans Canvas, il existe quelques exceptions. Avec l'ajout de Canvas Context, toutes les propriétés d'événement d'horodatage par défaut dans les Canvas basés sur les actions seront systématiquement en UTC. Ce changement s'inscrit dans le cadre d'une initiative plus large visant à garantir une expérience plus prévisible et cohérente lors de la modification des étapes du Canvas et des messages. Notez que cette modification affectera tous les Canvas basés sur des actions, que le Canvas en question utilise ou non une étape Contexte.

{% alert important %}
Dans tous les cas, nous recommandons fortement d'utiliser les [filtres Liquid time_zone]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) pour que les horodatages soient représentés dans le fuseau horaire souhaité. Vous pouvez consulter cette [question fréquemment posée dans l'article sur l'étape Contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#faq-example) pour obtenir un exemple.
{% endalert %}

## Articles connexes

- [Étape Contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/)
- [Personnalisation et contenu dynamique avec Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)