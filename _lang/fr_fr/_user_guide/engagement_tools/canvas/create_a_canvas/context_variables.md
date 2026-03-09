---
nav_title: Variables de contexte
article_title: Variables de contexte
page_type: reference
description: "Cet article de référence explique les variables de contexte dans Braze Canvases, notamment leurs types, leur utilisation et les meilleures pratiques."
---

# Variables de contexte

> Les variables de contexte sont des données temporaires que vous pouvez créer et utiliser au cours du parcours d'un utilisateur dans un canvas spécifique. Ils vous permettent de personnaliser les délais, de segmenter les utilisateurs de manière dynamique et d'enrichir l'envoi de messages sans modifier de manière permanente les informations du profil utilisateur. Les variables de contexte n'existent que dans la session Canvas et ne persistent pas entre différentes sessions Canvas ou en dehors de la session.

## Fonctionnement des variables de contexte

Les variables de contexte peuvent être définies de deux manières :

- **A l'entrée de la toile :** Lorsque les utilisateurs entrent dans un Canvas, les données de l'événement ou du déclencheur API peuvent automatiquement alimenter les variables de contexte.
- **Dans une étape de Contexte :** Vous pouvez définir ou mettre à jour manuellement les variables de contexte dans le canvas en ajoutant une [étape Contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context).

Chaque variable contextuelle comprend

- Un nom (tel que `flight_time` ou `subscription_renewal_date`)
- Un type de données (tel que nombre, chaîne de caractères, heure ou tableau)
- Une valeur que vous attribuez à l'aide de [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) ou de l'outil **Ajouter une personnalisation**.

Une fois définie, vous pouvez utiliser une variable contextuelle dans l'ensemble du canvas en y faisant référence sous la forme suivante : {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

Par exemple,{% raw %}`{{context.${flight_time}}}`{% endraw %}cela pourrait renvoyer l'heure de vol prévue pour la planification de l'utilisateur.

Chaque fois qu'un utilisateur entre dans le canvas - même s'il l'a déjà fait auparavant - les variables contextuelles seront redéfinies en fonction des dernières données d'entrée et de la configuration du canvas. Cette approche avec état permet à chaque entrée canvas de conserver son propre contexte indépendant, ce qui permet aux utilisateurs d'avoir plusieurs états actifs au cours d'un même parcours tout en conservant le contexte spécifique à chaque état.

Par exemple, si un client a deux vols à venir, il aura deux statuts de voyage distincts fonctionnant simultanément, chacun avec ses propres variables contextuelles spécifiques au vol, telles que l'heure de départ et la destination. Cela vous permet d'envoyer des rappels personnalisés concernant leur vol de 14 h à destination de New York, tout en envoyant des informations différentes concernant leur vol de 8 h à destination de Los Angeles demain, de sorte que chaque message reste pertinent par rapport à la réservation spécifique.

## Considérations

Vous pouvez définir jusqu'à 10 variables de contexte par [étape de contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/). Chaque nom de variable peut comporter jusqu'à 100 caractères et doit être composé uniquement de lettres, de chiffres ou de traits de soulignement.

Les définitions des variables de contexte peuvent comporter jusqu'à 10 240 caractères. Si vous transmettez des variables de contexte à un canvas déclenché par une API, elles partagent le même espace de noms que les variables créées dans une étape Contexte. Par exemple, si vous transmettez une variable`purchased_item`dans l'objet de contexte[`/canvas/trigger/send` de l'endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/), vous pouvez la référencer comme {% raw %}`{{context.${purchased_item}}}`{% endraw %}. Si vous redéfinissez cette variable dans une étape Contexte, la nouvelle valeur remplacera la valeur API pour le parcours de cet utilisateur.

Vous pouvez stocker jusqu'à 50 Ko par étape de contexte, répartis sur un maximum de 10 variables. Si la taille totale de toutes les variables d'une étape dépasse 50 Ko, les variables qui dépassent cette limite ne seront ni évaluées ni stockées. Par exemple, si vous avez trois variables dans une étape Context :

- Variable 1 : 30 KO
- Variable 2 : 19 KO
- Variable 3 : 2 Ko

La variable 3 ne sera ni évaluée ni stockée, car la somme des variables précédentes dépasse 50 Ko.

## Types de données

Les variables contextuelles créées ou mises à jour au cours de l'étape peuvent se voir attribuer les types de données suivants.

{% alert note %}
Les variables de contexte ont les mêmes formats attendus pour les types de données que [les événements personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format). <br><br>Lorsque vous utilisez le type tableau, Braze tente d'analyser la valeur au format JSON, ce qui permet de créer correctement des tableaux d'objets. Si les objets contenus dans vos tableaux ne sont pas valides au format JSON, le résultat sera un simple tableau de chaînes de caractères. <br><br>Pour les objets imbriqués et les tableaux d'objets, veuillez utiliser le [filtre`as_json_string` Liquid](#converting-connected-content-strings-to-json). Si vous créez le même objet dans une étape Context, vous devrez rendre l'objet à l'aide de `as_json_string`, tel que {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| Type de données | Exemple de nom de variable | Exemple de valeur |
|---|---|---|
|Valeur booléenne| loyalty_program |{% raw %}<code>true</code>{% endraw %}| 
|Nombre| credit_score |{% raw %}<code>740</code>{% endraw %}|
|Chaîne de caractères| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|Tableau| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|Tableau (d'objets)| pet_details |{% raw %}<code>[_mem_lt_br>_mem_amp_emsp;{ "id": 1, "type": "dog", "breed": "beagle", "name": "Gus" }_mem_lt_br>_mem_amp_emsp;,_mem_lt_br>_mem_amp_emsp;{ "id": 2, "type": "cat", "breed": "calico", "name": "Gerald" }_mem_lt_br>]</code>{% endraw %}|
|Heure (en UTC) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|Objet (aplati) | user_profile|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Par défaut, le type de données temporelles est en UTC. Si vous utilisez un type de données de chaîne de caractères pour stocker une valeur temporelle, vous pouvez définir l'heure comme un fuseau horaire différent, tel que PST. 

Par exemple, si vous envoyez un message à un utilisateur la veille de son anniversaire, vous enregistrerez la variable de contexte sous forme de type de données temporelles, car il existe une logique Liquid associée à l'envoi la veille. Toutefois, si vous envoyez un message de vœux le jour de Noël (25 décembre), il n'est pas nécessaire de faire référence à l'heure en tant que variable dynamique. Il est donc préférable d'utiliser un type de données de chaîne de caractères.

## Utilisation des variables de contexte

Vous pouvez utiliser les variables de contexte partout où vous utilisez Liquid dans un canvas, par exemple dans les étapes [Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) et [Mise à jour utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update), en sélectionnant **Ajouter une personnalisation**.

Par exemple, supposons que vous souhaitiez informer les passagers de leur accès au salon VIP avant leur prochain vol. Ce message ne doit être envoyé qu'aux passagers ayant acheté un billet de première classe. Une variable de contexte est un moyen souple de suivre ces informations.

Les utilisateurs entreront dans la toile lorsqu'ils achèteront un billet d'avion. Pour déterminer l'admissibilité à l'accès au salon, nous créerons une variable contextuelle appelée `lounge_access_granted` dans une étape Contexte, puis nous ferons référence à cette variable contextuelle dans les étapes suivantes du parcours de l'utilisateur.

![Variable contextuelle configurée pour déterminer si un passager est admissible à l'accès au salon VIP.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

Dans cette étape du Contexte, nous utiliserons {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} pour déterminer si le type de vol qu'ils ont acheté est `first_class`.

Ensuite, nous allons créer une étape Message pour cibler les utilisateurs pour lesquels {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} est `true`. Ce message sera une notification push contenant des informations de personnalisation sur le salon. En fonction de cette variable contextuelle, les passagers éligibles recevront les messages pertinents avant leur vol.

- Les passagers du billet de première classe recevront "Profitez d'un accès exclusif au salon VIP !
- Les passagers de la classe affaires et de la classe économique recevront "Surclassez votre vol pour bénéficier d'un accès exclusif au salon VIP.

![Une étape Message avec différents messages à envoyer, en fonction du type de billet d'avion acheté.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
Vous pouvez ajouter des [options de retard personnalisées]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) avec les informations de l'étape Contexte, ce qui signifie que vous pouvez sélectionner la variable qui retarde les utilisateurs.
{% endalert %}

### Pour les parcours d’action et les critères de sortie

Vous pouvez comparer les filtres de propriété à l'aide de variables de contexte ou d'attributs personnalisés dans les actions de déclenchement suivantes : **Réaliser un événement personnalisé** et **effectuer un achat**. Ces déclencheurs d'action prennent également en charge les filtres de propriétés pour les propriétés de base et les propriétés imbriquées. 

- Lors de la comparaison avec les propriétés de base, les comparaisons disponibles correspondront au type de propriété défini par l'événement personnalisé. Par exemple, les propriétés de chaîne de caractères auront des correspondances d’expressions régulières exactement identiques. Les propriétés booléennes peuvent être vraies ou fausses. 
- Lors de la comparaison avec des propriétés imbriquées, les types ne sont pas prédéfinis. Vous pouvez donc sélectionner des comparaisons entre plusieurs types de données pour les booléens, les nombres, les chaînes de caractères, l'heure et le jour de l'année, comme pour les comparaisons d'attributs personnalisés imbriqués. Si vous sélectionnez un type de données qui ne correspond pas au type de données réel de la propriété imbriquée au moment de la comparaison, l'utilisateur ne correspondra pas au parcours d’action ou aux critères de sortie.

#### Exemples de parcours d’action

{% alert important %}
Pour les comparaisons d'attributs personnalisés, nous utiliserons la valeur de l'attribut personnalisé au moment où l'action est effectuée. Cela signifie qu'un utilisateur ne correspondra pas au groupe de parcours d’action si cet attribut personnalisé n'est pas renseigné au moment de la comparaison, ou si la valeur de l'attribut personnalisé ne correspond pas aux comparaisons de propriétés définies. Cela s'applique même si l'utilisateur aurait été identifié lorsqu'il a saisi l'étape du parcours d’action.
{% endalert %}

{% tabs %}
{% tab Perform custom event %}

Le parcours d’action suivant est configuré pour trier les utilisateurs qui ont effectué l’événement personnalisé`Account_Created` avec la propriété de base`source` vers la variable de contexte`app_source_variable`.

![Exemple de parcours d’action qui fait référence à une variable de contexte lors de l’exécution d’un événement personnalisé.]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Make purchase %}

Le parcours d’action suivant est configuré pour faire correspondre la propriété`brand`de base du nom du produit `shoes`spécifique à une variable de contexte`promoted_shoe_brand`.

![Exemple de parcours d’action faisant référence à une variable de contexte lors d’un achat.]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### Exemples de critères de sortie

{% tabs %}
{% tab Perform custom event %}

Les critères de sortie stipulent qu'à tout moment du parcours d'un utilisateur dans Canvas, celui-ci quittera Canvas si :

- Ils exécutent l'événement personnalisé « **Abandon du panier** » et
- La propriété de base **Article dans le panier** correspond à la valeur de chaîne de caractères de la variable de contexte`cart_item_threshold`.

![Critères de sortie définis pour exclure un utilisateur s'il effectue un événement personnalisé basé sur la variable de contexte.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

Les critères de sortie stipulent qu'à tout moment du parcours d'un utilisateur dans Canvas, celui-ci quittera Canvas si :

- Ils effectuent un achat spécifique pour le nom de produit « livre », et
- La propriété imbriquée de"loyalty_program" cet achat est identique à l'attribut personnalisé « VIP » de l'utilisateur.

![Critères de sortie définis pour exclure un utilisateur s'il effectue un achat.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### Filtres de variables contextuelles

Vous pouvez créer des filtres qui utilisent des variables de contexte précédemment déclarées dans les étapes [du parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) et [de l'arbre décisionnel]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split).

{% alert note %}
Les filtres de variables contextuelles sont uniquement disponibles pour les étapes du parcours d'audience et de l'arbre décisionnel.
{% endalert %}

Les variables de contexte sont déclarées et accessibles uniquement dans le cadre d'un canvas, ce qui signifie qu'elles ne peuvent pas être référencées dans les segments. Les filtres de variables contextuelles fonctionnent de manière similaire dans les étapes « Parcours d'audience » et « Étape de l'arbre décisionnel » : les étapes « Parcours d'audience » représentent plusieurs groupes, tandis que les étapes « Étape de l'arbre décisionnel » représentent des décisions binaires.

![Exemple de l'étape de l'arbre décisionnel avec la possibilité de créer un filtre à l'aide d'une variable de contexte.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

Tout comme les variables de contexte canvas ont des types prédéfinis, les comparaisons entre les variables de contexte et les valeurs statiques doivent avoir [des types de données correspondants]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types). Le filtre de variable de contexte permet d'effectuer des comparaisons entre plusieurs types de données pour les booléens, les nombres, les chaînes de caractères, l'heure et le jour de l'année, de manière similaire aux comparaisons pour [les attributs personnalisés imbriqués.]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/)

{% alert note %}
Veuillez utiliser le même type de données pour votre variable de contexte et votre comparaison. Par exemple, si votre variable de contexte est de type données temporelles, veuillez utiliser des comparaisons temporelles (telles que « avant » ou « après »). L'utilisation de types de données incompatibles (tels que les comparaisons de chaînes de caractères avec une variable contextuelle temporelle) peut entraîner un comportement inattendu.
{% endalert %}

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

Voici un exemple de filtre de variable de contexte comparant la variable de contexte`product_name` à l'expression régulière`/braze/`.

![Configuration d'un filtre pour que la variable de contexte"product_name" corresponde à l'expression régulière « /Braze/ ».]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Comparaison avec des variables de contexte ou des attributs personnalisés

En basculant sur le bouton **Comparer à une variable de contexte ou à un attribut personnalisé**, vous pouvez créer des filtres de variables de contexte qui comparent les variables de contexte ou les attributs personnalisés de l'utilisateur préalablement définis. Cela peut être utile pour effectuer des comparaisons dynamiques par utilisateur, comme celles déclenchées par une API`context`, ou pour condenser une logique de comparaison complexe définie à travers des variables de contexte.

{% tabs %}
{% tab Example 1 %}

Supposons que vous souhaitiez envoyer un rappel personnalisé aux utilisateurs après une période d'inactivité dynamique, ce qui inclut toute personne qui ne s'est pas connectée à votre application au cours des trois derniers jours et qui devrait recevoir un message.

Vous disposez d'une variable de contexte `re_engagement_date`définie comme {% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %}suit. Veuillez noter que`3 days`cela peut être un montant variable qui est également stocké en tant qu'attribut personnalisé de l'utilisateur. Ainsi, si le`re_engagement_date`  est postérieur au`last_login_date`  (enregistré en tant qu'attribut personnalisé dans le profil utilisateur), un message leur sera envoyé.

![Une configuration de filtre avec des attributs personnalisés comme type de personnalisation pour la variable de contexte"re_engagement_date" après l'attribut "last_login_date".]({%image_buster/assets/img/context_variable_filter2.pngpersonnalisé    %})

{% endtab %}
{% tab Example 2 %}

Le filtre suivant compare la variable de contexte`reminder_date`  à la variable de contexte`appointment_deadline` . Cela peut aider les utilisateurs du groupe dans une étape du parcours d'audience à déterminer s'ils doivent recevoir des rappels supplémentaires avant la date limite de leur rendez-vous.

![Une configuration de filtre avec des variables de contexte comme type de personnalisation pour la variable de contexte"reminder_date"  sur la variable de contexte"appointment_deadline".]({%image_buster/assets/img/context_variable_filter3.png    %})

{% endtab %}
{% endtabs %}

## Normalisation de la cohérence des fuseaux horaires

Bien que la plupart des propriétés d'événement utilisant le type d'horodatage soient déjà en UTC dans Canvas, il existe quelques exceptions. Avec l'ajout de Canvas Context, toutes les propriétés d'événement d'horodatage par défaut dans les canevas basés sur les actions seront systématiquement en UTC. Ce changement s'inscrit dans le cadre d'une initiative plus large visant à garantir une expérience plus prévisible et cohérente lors de la modification des étapes du canvas et des messages. Veuillez noter que cette modification affectera toutes les toiles basées sur des actions, que la toile spécifique utilise ou non une étape de contexte.

{% alert important %}
Dans tous les cas, nous recommandons fortement d'utiliser [des filtrestime_zone Liquid]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) pour que les horodatages soient représentés dans le fuseau horaire souhaité. Vous pouvez vous référer à cette [question fréquemment posée dans l'article Étape Contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#faq-example) pour obtenir un exemple.
{% endalert %}

## Articles connexes

- [Étape contextuelle]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/)
- [Personnalisation et contenu dynamique avec Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)
