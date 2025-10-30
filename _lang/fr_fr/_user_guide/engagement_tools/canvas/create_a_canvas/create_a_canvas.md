---
nav_title: "Création d'un canvas"
article_title: "Création d'un canvas"
page_order: 0
page_type: reference
description: "Cet article de référence couvre les étapes nécessaires à la création, à la maintenance et au test d'un canvas."
tool: Canvas
search_rank: 1
---

# Création d'un canvas

> Cet article de référence couvre les étapes nécessaires à la création, à la maintenance et au test d'un canvas. Suivez ce guide ou consultez notre [cours d'apprentissage Canvas Braze](https://learning.braze.com/quick-overview-canvas-setup).

{% details Original Canvas editor %}
Vous ne pouvez plus créer ou dupliquer des toiles en utilisant l'expérience Canvas originale. Braze recommande de [cloner vos Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/) vers l'éditeur le plus récent.
{% enddetails %}

## Création d'un canvas

### Étape 1 : Créer un nouveau Canvas 

Tout d'abord, allez dans **Messagerie** > **Canvas**, puis sélectionnez **Créer un canevas**.

Le générateur de Canvas vous guidera pas à pas dans la configuration de votre Canvas, depuis son nom jusqu'à la définition des événements de conversion et l'intégration des bons utilisateurs dans votre parcours client. Sélectionnez chacun des onglets suivants pour afficher les paramètres que vous pouvez ajuster pour chaque étape du générateur.

{% tabs local %}
  {% tab Basics %}
    Vous y définirez les bases de votre Canvas :
    \- Nommez votre canvas
    \- Ajouter des Teams
    \- Ajouter des tags
    \- Attribuer des événements de conversion et choisir leurs types d'événements et leurs échéances.

    Learn more about the [Basics step](#step-2a-set-up-your-canvas-basics).
  {% endtab %}
  {% tab Entry Schedule %}
    Ici, vous déciderez comment et quand vos utilisateurs entreront dans votre Canvas :
    \- Planifié : Il s'agit d'une entrée dans Canvas basée sur le temps.
    \- Basé sur l'action : Votre utilisateur entrera dans votre canvas après avoir effectué une action définie
    \- Déclenché par l'API : Utilisez une demande d'API pour entrer des utilisateurs dans votre Canvas.

    Learn more about the [Entry Schedule step](#step-2b-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Target Audience %}
    Vous y sélectionnerez votre audience cible :
    \- Créez votre audience en ajoutant des segments et des filtres.
    \- Affiner les limites de réinscription et d'entrée dans les toiles
    \- Voir un résumé de votre audience cible

    Learn more about the [Target Audience step](#step-2c-set-your-target-entry-audience).
  {% endtab %}
  {% tab Send Settings %}
    Vous y sélectionnerez les paramètres d'envoi de Canvas :
    \- Sélectionnez vos paramètres d'abonnement
    \- Fixez une limite de débit pour l'envoi de vos messages Canvas
    \- Activation et réglage des heures calmes

    Learn more about the [Send Settings step](#step-2d-select-your-send-settings).
  {% endtab %}
  {% tab Build Canvas %}
    Vous y créerez votre Canvas.

    Learn how to [build your Canvas](#step-3-build-your-canvas) using the Canvas builder.
  {% endtab %}
  {% tab Summary %}
    Vous y trouverez le résumé des détails de votre Canvas. Si le [flux de travail d'approbation de Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) est activé, vous pouvez approuver les détails de Canvas listés avant le lancement.

  {% endtab %}
{% endtabs %}

#### Étape 1.1 : Commencez par les bases de votre Canvas

C'est ici que vous nommerez votre Canvas, attribuerez des [Teams]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams) et créerez ou ajouterez des [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags). Vous pouvez également attribuer des événements de conversion au Canvas.

{% alert tip %}
Étiquetez vos toiles afin de les retrouver facilement et de créer des rapports à partir de celles-ci. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), vous pouvez filtrer par des étiquettes particulières.
{% endalert %}

La page de détails du canvas, avec des champs pour le nom du canvas, la description, l'emplacement/localisation et les tags.]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

##### Choisissez des événements de conversion

Choisissez votre type d'événement de conversion, puis sélectionnez les conversions à enregistrer. Ces [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) permettront de mesurer l'efficacité de votre canvas. 

\![Événement de conversion principal A avec le type d'événement de conversion Fait un achat pour enregistrer les conversations des utilisateurs qui effectuent un achat quelconque dans un délai de conversion de trois jours.]({% image_buster /assets/img/add_canvas_conversions.png %})

Si votre Canvas comporte plusieurs variantes ou un groupe de contrôle, Braze utilisera cet événement de conversion pour déterminer la meilleure variation permettant d'atteindre cet objectif de conversion. En utilisant la même logique, vous pouvez créer plusieurs événements de conversion.

#### Étape 1.2 : Déterminez votre planification d'entrée dans Canvas

Vous pouvez choisir l'une des trois façons dont les utilisateurs peuvent entrer dans votre Canvas. 

##### Types de planifications d'entrée

{% tabs local %}
  {% tab Scheduled Delivery %}
    Dans le cas de la réception/distribution programmée, les utilisateurs entrent selon une planification, de la même manière que vous programmeriez une campagne. Vous pouvez inscrire des utilisateurs dans un Canvas dès son lancement, les inscrire dans votre parcours à un moment donné dans le futur, ou de manière récurrente (quotidienne, hebdomadaire ou mensuelle). 

    In this example, based on the time-based options, users will enter this Canvas every Tuesday at 12 pm in their local time zone every week, beginning November 14, 2025 until December 31, 2025.

    ![The "Entry Schedule" page with the type set to "Scheduled". Due to the selection, time-based options are shown, including frequency, start time, recurrence, days, and more.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab Action-Based Delivery %}
    Avec la livraison par événement, les utilisateurs entreront dans le Canvas et commenceront à recevoir des messages lorsqu'ils effectueront des actions particulières, comme ouvrir votre appli, effectuer un achat ou déclencher un événement personnalisé.

    You can control other aspects of the Canvas behavior from the **Entry Audience** window, including rules for re-eligibility and frequency capping settings. Note that action-based delivery is unavailable for Canvas components with in-app messages.

    ![An example of action-based delivery. Users will enter the Canvas if they make a purchase with an entry window beginning at 1:30 pm on June 10, 2025.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

  {% endtab %}
  {% tab API-Triggered Delivery %}
    Avec la réception/distribution déclenchée par l'API, les utilisateurs entreront dans votre Canvas et commenceront à recevoir des messages après avoir été ajoutés à l'aide du [point de terminaison`/canvas/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) via l'API. Dans le tableau de bord, vous trouverez un exemple de requête cURL qui effectue cette opération, ainsi que l'attribution d'une propriété optionnelle [`canvas_entry_properties`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) à l'aide de l'[objet de propriétés de l'entrée Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). 

    ![An example of API-triggered delivery with a Canvas ID and an example of a cURL request.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    You can use the following endpoints for API-triggered delivery:
    - [POST: Send Canvas Messages via API-Triggered Delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: Schedule API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: Update Scheduled API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

Après avoir sélectionné votre mode de réception/distribution, ajustez les paramètres en fonction de votre cas d'utilisation, puis continuez en définissant votre audience cible.

{% details Deduplicate behavior for Canvases using the original editor %}
Si la fenêtre de rééligibilité est inférieure à la durée maximale du Canvas, un utilisateur sera autorisé à se réinscrire et à recevoir plus d'un envoi de messages de la composante. Dans le cas où la réentrée d'un utilisateur atteint le même composant que son entrée précédente, Braze dédupliquera les messages de ce composant. 

Si un utilisateur entre à nouveau dans le Canvas, atteint le même composant que son entrée précédente et a droit à un message in-app pour chaque entrée, il recevra le message deux fois (en fonction de la priorité des messages in-app) tant qu'il rouvrira une session deux fois.
{% enddetails %}

#### Étape 1.3 : Définissez votre audience d'entrée cible

Seuls les utilisateurs qui correspondent aux critères que vous avez définis peuvent entrer dans le parcours à l'étape **Audience cible**, ce qui signifie que Braze évalue d'abord l'éligibilité de l'audience cible **avant que** les utilisateurs n **'** entrent dans le parcours Canvas. Par exemple, si vous souhaitez cibler les nouveaux utilisateurs, vous pouvez sélectionner un segment d'utilisateurs qui ont utilisé votre appli pour la première fois il y a moins d'une semaine.

Dans les **contrôles d'entrée**, vous pouvez limiter le nombre d'utilisateurs à chaque fois que le canvas est planifié pour s'exécuter. Pour les canevas basés sur des déclencheurs API et des actions, cette limite se produit à chaque heure UTC. 

{% alert important %}
Évitez de configurer une campagne basée sur une action ou un Canvas avec le même déclencheur que le filtre d'audience (comme un attribut modifié ou l'exécution d'un événement personnalisé). Une [condition de concurrence]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions) peut se produire : l'utilisateur n'est pas dans l'audience au moment où il effectue le déclencheur, ce qui signifie qu'il ne recevra pas la campagne ou n'entrera pas dans le Canvas.
{% endalert %}

##### Tester votre audience

Après avoir ajouté des segments et des filtres à votre audience cible, vous pouvez tester si votre audience est configurée comme prévu en [recherchant un utilisateur]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) pour confirmer s'il correspond aux critères de segmentation.

\![Le champ "Recherche d'utilisateurs", qui vous permet d'effectuer une recherche par ID externe ou par ID Braze.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:100%;"}{: style="max-width:80%;"}

##### Sélection des contrôles d'entrée

Les contrôles d'entrée déterminent si les utilisateurs sont autorisés à entrer à nouveau dans une toile. Vous pouvez également limiter le nombre de personnes susceptibles d'entrer dans ce Canvas en fonction d'une cadence choisie (quotidienne, pendant toute la durée du Canvas ou à chaque fois que le Canvas est planifié). 

Par exemple, si vous sélectionnez **Limiter le volume d'entrée** et que vous réglez le champ **Entrées maximales** sur 5 000 utilisateurs avec **Quotidien** comme cadence limite, alors le Canvas n'enverra qu'à 5 000 utilisateurs par jour.

La page "Contrôles d'entrée" affiche des cases à cocher pour "Autoriser les utilisateurs à entrer à nouveau dans la toile" et "Limiter le volume d'entrée". Cette dernière vous permet de définir le nombre maximum d'entrées et de préciser si vous souhaitez limiter le nombre d'entrées par jour, pendant toute la durée du canvas ou à chaque fois que le canvas est planifié.]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
Braze ne recommande pas d'utiliser la fonctionnalité **Chaque fois que la toile est planifiée** pour le réchauffement d'adresses IP, car cela peut entraîner une augmentation des volumes d'envoi.
{% endalert %}

##### Fixer des critères de sortie

La définition des [critères de sortie]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) permet de déterminer quels utilisateurs doivent quitter un Canvas. Si un utilisateur effectue l'événement d'exception ou correspond aux segments et aux filtres, il ne recevra pas d'autres messages.

##### Calcul de la population cible

Dans la section **Population cible**, vous pouvez consulter un résumé de votre audience, comme les segments sélectionnés et les filtres supplémentaires, ainsi qu'une répartition du nombre d'utilisateurs atteignables par canal de communication. Pour calculer le nombre exact d'utilisateurs joignables dans votre audience cible au lieu de l'estimation par défaut, sélectionnez [Calculer des statistiques exactes]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics).

Notez que :

- Le calcul de statistiques exactes peut prendre quelques minutes. Cette fonction ne calcule les statistiques exactes qu'au niveau du segment, et non au niveau du filtre ou du groupe de filtres.
- Pour les segments de grande taille, il est normal d'observer de légères variations, même en calculant des statistiques exactes. La précision de cette fonctionnalité devrait être supérieure ou égale à 99,999 %.

Pour afficher des statistiques supplémentaires, telles que le chiffre d'affaires moyen sur la durée de vie des utilisateurs ciblés, sélectionnez **Afficher les statistiques supplémentaires.**

!Ventilation de la population cible avec possibilité de calculer des statistiques exactes.]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

##### Pourquoi le nombre d'audiences cibles peut-il différer du nombre d'utilisateurs atteignables ?

{% multi_lang_include segments.md section='Differing audience size' %}

#### Étape 1.4 : Sélectionnez vos paramètres d'envoi

Sélectionnez **Paramètres d'envoi** pour modifier vos paramètres d'abonnement, activer la limite de débit et activer les heures calmes. En activant la [limite de débit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-canvas-components) ou la [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#frequency-capping), vous pouvez alléger la pression marketing exercée sur vos utilisateurs et vous assurer que vous ne leur envoyez pas trop de messages.

Pour les Canvas ciblant les canaux e-mail et push, vous pouvez vouloir limiter votre Canvas de sorte que seuls les utilisateurs qui sont explicitement opt-in recevront le message (à l'exclusion des utilisateurs abonnés ou s'étant désabonnés). Par exemple, supposons que vous ayez trois utilisateurs ayant des statuts d'abonnement différents :

- L'**utilisateur A** est abonné à l'e-mail et dispose de la fonction "push". Cet utilisateur ne reçoit pas l'e-mail mais recevra le push.
- L'**utilisateur B** est abonné à l'e-mail mais n'est pas autorisé à utiliser la fonction "push". Cet utilisateur recevra l'e-mail mais ne recevra pas le push.
- L'**utilisateur C** est abonné à l'e-mail et dispose de la fonction "push". Cet utilisateur recevra à la fois l'e-mail et le push.

Pour ce faire, réglez **les paramètres d'abonnement** de manière à envoyer ce canvas aux "utilisateurs ayant opté pour l'abonnement uniquement". Cette option garantira que seuls les utilisateurs ayant opté pour l'option recevront votre e-mail, et Braze n'enverra votre push qu'aux utilisateurs dont le push est activé par défaut. 

Ces paramètres d'abonnement sont appliqués étape par étape, ce qui signifie qu'il n'y a pas d'effet sur l'audience d'entrée. Ce paramètre est donc utilisé pour évaluer l'éligibilité d'un utilisateur à recevoir chaque étape du canvas.

{% alert important %}
Avec cette configuration, n'incluez aucun filtre dans l'étape **Target Audience** qui limite l'audience à un seul canal (par exemple, `Foreground Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

Si vous le souhaitez, spécifiez des heures calmes (le temps pendant lequel vos messages ne seront pas envoyés) pour votre Canvas. Cochez la case **Activer les heures calmes** dans vos **paramètres d'envoi.** Sélectionnez ensuite vos heures calmes dans l'heure locale de votre utilisateur et l'action qui suivra si le message se déclenche pendant ces heures calmes.

La page "Heures calmes" affiche une case à cocher permettant d'activer les heures calmes. Si elle est activée, l'heure de début, l'heure de fin et le comportement de repli peuvent être définis.]({% image_buster /assets/img/quiet_hours.png %})

### Étape 2 : Créez votre canvas

{% alert tip %}
Enregistrez votre temps et rationalisez votre création de canvas en utilisant les [modèles de Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/#available-braze-templates)! Parcourez notre bibliothèque de modèles préconstruits pour trouver celui qui correspond à votre cas d'utilisation et personnalisez-le pour répondre à vos besoins spécifiques.
{% endalert %}

#### Étape 2.1 : Ajouter une variante

Le bouton "Ajouter une variante" est sélectionné pour afficher un menu contextuel avec l'option "Ajouter une variante".]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

Sélectionnez **Ajouter une variante**, puis ajoutez une nouvelle variante à votre canvas. Les variantes représentent un parcours que vos utilisateurs vont effectuer et peuvent contenir plusieurs étapes et embranchements.

Vous pouvez ajouter des variantes supplémentaires en sélectionnant le bouton <i class="fas fa-plus-circle"></i> plus. Lorsque vous ajouterez de nouvelles variantes, vous pourrez ajuster la répartition de vos utilisateurs entre elles afin de pouvoir effectuer des comparaisons croisées et analyser l'efficacité des différentes stratégies d'engagement.

!Deux exemples de variante du canvas de Braze.]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
Par défaut, l'affectation de la variante du canvas est verrouillée lorsque les utilisateurs entrent dans le canvas, ce qui signifie que si un utilisateur saisit une variante pour la première fois, il s'agira de sa variante chaque fois qu'il entrera à nouveau dans le canvas. Il existe cependant des moyens de contourner ce comportement. <br><br>Pour ce faire, vous pouvez créer un générateur de nombres aléatoires à l'aide de Liquid, l'exécuter au début de l'entrée de chaque utilisateur dans Canvas, stocker la valeur en tant qu'attribut personnalisé, puis utiliser cet attribut pour répartir les utilisateurs de manière aléatoire.

{% details Expand for steps %}

1. Créez un attribut personnalisé pour stocker votre nombre aléatoire. Donnez-lui un nom facile à repérer, comme "lottery_number" ou "random_assignment".. Vous pouvez créer l'attribut soit [dans votre tableau de bord]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/), soit par le biais d'appels API à notre [point de terminaison`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).<br><br>
2. Créez une campagne webhook au début de votre canvas. C'est dans le cadre de cette campagne que vous créerez votre numéro aléatoire et que vous le stockerez en tant qu'attribut personnalisé. Pour en savoir plus, reportez-vous à la section [Création d'un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook). Définissez l'URL de notre endpoint `/users/track`.<br><br>
3. Créez le générateur de nombres aléatoires. Vous pouvez le faire avec le code [présenté ici](https://community.shopify.com/c/technical-q-a/is-there-any-way-to-generate-random-number-with-liquid-shopify/m-p/1595486), qui tire parti de l'heure d'entrée unique de chaque utilisateur pour créer un numéro aléatoire. Définissez le nombre obtenu comme variable Liquid dans votre campagne webhook.<br><br>
4. Formulez l'appel `/users/track` de votre campagne webhook de manière à ce qu'il définisse l'attribut personnalisé que vous avez créé à l'étape 1 avec le nombre aléatoire que vous avez généré dans le profil de votre utilisateur actuel. Lorsque cette étape sera terminée, vous aurez réussi à créer un numéro aléatoire qui changera chaque fois qu'un utilisateur entrera dans votre campagne.<br><br>
5. Ajustez les branches de votre Canvas de sorte qu'au lieu d'être divisées par des variantes choisies au hasard, elles le soient en fonction des règles de l'audience. Dans les règles d'audience de chaque branche, définissez le filtre d'audience en fonction de votre attribut personnalisé. <br><br>Par exemple, une branche peut avoir comme filtre d'audience " "lottery_number est inférieur à 3", tandis qu'une autre branche peut avoir comme filtre d'audience " "lottery_number est supérieur à 3 et inférieur à 6".

{% enddetails %}
{% endalert %}

#### Étape 2.2 : Ajouter des étapes du canvas

Vous pouvez ajouter d'autres étapes à votre flux de travail Canvas en glissant-déposant des composants à partir de la barre latérale **Composants**. Vous pouvez également sélectionner le bouton <i class="fas fa-plus-circle"></i> plus pour ajouter un composant à l'aide du menu déroulant.

{% alert tip %}
Au fur et à mesure que vous ajoutez des étapes, vous pouvez augmenter le niveau de zoom pour vous concentrer sur des détails ou sur l'ensemble du parcours de l'utilisateur. Faites un zoom avant avec <kbd>Shift</kbd> + <kbd>+</kbd> ou un zoom arrière avec <kbd>Shift</kbd> + <kbd>-</kbd>.
{% endalert %}

!La fenêtre de recherche de composants ajoutant une étape du canvas de Braze.]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert important %}
Vous pouvez ajouter jusqu'à 200 étapes dans un canvas. Si votre Canvas dépasse 200 étapes, des problèmes de chargement peuvent survenir.
{% endalert %}

##### Durée maximale

Comme le parcours de votre Canvas augmente par étapes, la durée maximale est le temps le plus long possible qu'un utilisateur peut prendre pour compléter ce Canvas. Elle est calculée en additionnant les retards et les fenêtres de déclenchement de chaque étape de chaque variante pour le chemin le plus long. Par exemple, si votre Canvas comporte une étape Délai avec un délai de 3 jours et une étape Message, la durée maximale de votre Canvas sera de 3 jours.

##### Modifier une étape

Vous souhaitez modifier une étape de votre parcours utilisateur ? Découvrez comment procéder en fonction de votre flux de travail sur Canvas !

Vous pouvez modifier n'importe quelle étape de votre flux de travail Canvas en sélectionnant l'un des composants. Par exemple, disons que vous souhaitez modifier votre première étape, un composant [Délai]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), dans votre flux de travail pour un jour spécifique. Sélectionnez l'étape pour afficher ses paramètres et ajuster votre délai au 1er mars. Cela signifie que le 1er mars, vos utilisateurs passeront à l'étape suivante de votre Canvas.

Un exemple d'étape "Délai" avec le délai réglé sur "Jusqu'à un jour spécifique".]({% image_buster /assets/img_archive/edit_delay_flow.png %})

Vous pouvez également modifier et ajuster rapidement les **paramètres d'action** de votre étape de [parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) afin de retenir les utilisateurs pendant une certaine période. Cela permet de hiérarchiser leur parcours d'action sur la base des actions menées au cours de cette période d'évaluation.

La deuxième étape du canvas, "Paramètres d'action", avec une fenêtre d'évaluation fixée à 1 jour.]({% image_buster /assets/img_archive/action_paths_flow.png %})

Les composants légers de Canvas permettent une expérience de modification simple, ce qui facilite l'ajustement des détails les plus fins de votre Canvas. 

##### Messages dans Canvas

Modifiez les messages d'un composant Canvas pour contrôler les messages qu'une étape particulière enverra. Canvas peut envoyer des messages par e-mail, mobile et web push, ainsi que des webhooks pour s'intégrer à d'autres systèmes. Comme pour les campagnes, vous pouvez utiliser certains modèles de [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) pour personnaliser vos messages.

{% alert tip %}
Saviez-vous que vous pouvez inclure les noms des composants de Canvas dans vos messages et modèles de liens ?<br>
Utilisez l'étiquette Liquid `campaign.${name}` dans Canvas pour afficher le nom du composant Canvas en cours.
{% endalert %}

Le composant Message gère les messages envoyés aux utilisateurs. Vous pouvez sélectionner vos **canaux de communication** et ajuster les **paramètres de réception/distribution** pour optimiser vos messages Canvas. Pour plus de détails sur cette composante, consultez la rubrique [Message.]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)

L'étape "Configurer les messages", en sélectionnant "Canaux de messages", affiche la liste des canaux de communication disponibles, tels que le push android, les cartes de contenu, l'e-mail, etc.]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

Sélectionnez **Terminé** une fois que vous avez fini de configurer votre composant Canvas.

{% tabs local %}
{% tab Canvas Entry Properties %}

Le site `canvas_entry_properties` est configuré à l'étape de la création d'un Canvas intitulée Entry Schedule et indique le déclencheur qui permet à un utilisateur d'entrer dans un Canvas. Ces propriétés peuvent également accéder aux propriétés des charges utiles d'entrée dans les canevas déclenchés par l'API. Notez que l'objet `canvas_entry_properties` peut avoir une taille maximale de 50 Ko. 

Utilisez le Liquid suivant lorsque vous faites référence à ces propriétés d'entrée : {% raw %} ``canvas_entry_properties.${property_name}`` {% endraw %}. Notez que les événements doivent être des événements personnalisés ou des événements d'achat pour être utilisés de cette manière.

{% raw %}
Par exemple, considérez la demande suivante : `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Vous pouvez ajouter le mot "chaussures" à un message avec ce Liquid ``{{canvas_entry_properties.${product_name}}}``.
{% endraw %}

{% endtab %}

{% tab Event Properties %}
Les propriétés d'événement sont les propriétés que vous définissez pour les événements personnalisés et les achats. Ces `event_properties` peuvent être utilisés dans les campagnes avec livraison/distribution par événement ainsi que dans les canevas. 

Dans Canvas, les propriétés d'événement personnalisé et d'achat peuvent être utilisées dans Liquid dans toute étape de message qui suit une étape de parcours d'action. Utilisez ce liquide {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %} lorsque vous faites référence à ces `event_properties`. Ces événements doivent être des événements personnalisés ou des événements d'achat pour être utilisés de cette manière dans le composant Message.

Dans la première étape du message suivant un parcours d'action, vous pouvez utiliser `event_properties` en rapport avec l'événement référencé dans ce parcours d'action. Vous pouvez avoir d'autres étapes (qui ne sont pas d'autres parcours d'action ou d'autres envois de messages) entre cette étape de parcours d'action et l'étape d'envoi de messages. Notez que vous n'aurez accès à `event_properties` que si votre étape Message peut être rattachée à un chemin autre que Tout le monde ailleurs dans une étape Chemin d'action

{% endtab %}
{% endtabs %}

#### Étape 2.3 : Modifier les connexions

Pour déplacer une connexion entre les étapes, sélectionnez la flèche reliant les deux composants et sélectionnez un autre composant. Pour supprimer la connexion, sélectionnez la flèche suivie de **Annuler la connexion** dans le pied de page du compositeur Canvas.

### Étape 3 : Ajouter un groupe de contrôle

Vous pouvez ajouter un groupe de contrôle à votre Canvas en sélectionnant le bouton <i class="fas fa-plus-circle"></i> plus pour ajouter une nouvelle variante. 

Braze suivra les conversions des utilisateurs placés dans le groupe de contrôle, même s'ils ne recevront aucun message. Afin de préserver la précision du test, nous suivrons le nombre de conversions pour vos variantes et le groupe de contrôle pendant exactement la même durée, comme indiqué dans l'écran de sélection de l'événement de conversion. 

Vous pouvez ajuster la répartition entre vos messages en double-cliquant sur les en-têtes **des noms de variante**.

Dans cet exemple, notre canvas est divisé en deux variantes. La variante 1 compte 70 % des utilisateurs. La seconde variante est un groupe de contrôle composé des 30 % d'utilisateurs restants.

!Un exemple de variante dans un Braze Canvas, où 70% vont à la "Variante 1", qui retarde d'un jour dans la première étape, puis envoie un message dans la deuxième étape. Les 30 % restants sont dirigés vers un "contrôle" qui ne prévoit aucune mesure de suivi.]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

#### Sélection intelligente pour les canvas

Les capacités de sélection intelligente sont désormais disponibles dans les canevas multivariés. À l'instar de la fonctionnalité de [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) pour les campagnes multivariées, la sélection intelligente pour Canvas analyse les performances de chaque variante de Canvas et ajuste le pourcentage d'utilisateurs entonnoir par le biais de chaque variante. Cette répartition est basée sur les indicateurs de performance de chaque variante afin de maximiser le nombre total de conversions attendues.

Gardez à l'esprit que les canevas multivariés vous permettent de tester plus que le texte, mais aussi le moment et les canaux. Grâce à la sélection intelligente, vous pouvez tester les canvas plus efficacement et avoir la certitude que vos utilisateurs seront envoyés dans le meilleur parcours possible sur les canvas.

\![L'option "Sélection intelligente" est activée dans la page "Modifier la répartition des variantes". Au fur et à mesure qu'il analyse et optimise le canvas, il affiche une barre horizontale en travers de la page qui est divisée en plusieurs sections, chacune variant en couleur et en taille. Il s'agit uniquement d'une représentation visuelle qui ne correspond à aucune analyse/analytique spécifique.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

La sélection intelligente pour Canvas optimise vos résultats Canvas en procédant à des ajustements progressifs en temps réel de la répartition des utilisateurs triés dans chaque variante. Lorsque l'algorithme statistique détermine un gagnant décisif parmi vos variantes, il élimine les variantes moins performantes et place tous les futurs destinataires éligibles de la toile dans les variantes gagnantes. 

C'est pourquoi la sélection intelligente fonctionne mieux sur les canevas où de nouveaux utilisateurs entrent fréquemment.

### Étape 4 : Enregistrez et lancez

Une fois la création de votre canvas terminée, sélectionnez **Lancer le canvas** pour enregistrer et lancer votre canvas. Après avoir lancé votre Canvas, vous pourrez consulter les analyses/analytiques de votre parcours au fur et à mesure de leur arrivée sur la page **Détails du Canvas**. 

Vous pouvez également enregistrer votre Canvas en tant que brouillon si vous devez y revenir.

!Un exemple de toile en Braze.]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
Vous avez besoin de modifier votre canvas après son lancement ? Eh bien, vous pouvez le faire ! Pour plus d'informations, consultez la page [Modifier les toiles après le lancement]({{site.baseurl}}/post-launch_edits/).
{% endalert %}

