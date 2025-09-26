---
nav_title: Création d’un Canvas
article_title: Création d’un Canvas
page_order: 0
page_type: reference
description: "Cet article de référence aborde les étapes nécessaires à la création, à la gestion et aux essais d’un Canvas."
tool: Canvas
search_rank: 1
---

# Création d’un Canvas

> Cet article de référence aborde les étapes nécessaires à la création, à la gestion et aux essais d’un Canvas. Suivez ce guide, ou consultez notre [cours d'apprentissage Canvas Braze](https://learning.braze.com/quick-overview-canvas-setup).

{% details Editeur de canevas original %}
Vous ne pouvez plus créer ou dupliquer des toiles en utilisant l'expérience Canvas originale. Braze recommande de [cloner vos toiles dans Canvas Flow.]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/)
{% enddetails %}

## Création d’un Canvas

### Étape 1 : Créer un nouveau Canvas 

Tout d'abord, allez dans **Messagerie** > **Canvas**, puis sélectionnez **Créer un canevas**.

Le constructeur de Canvas vous guidera étape par étape pour configurer votre Canvas—de la nomination à la définition des événements de conversion et à l'intégration des bons utilisateurs dans votre parcours client. Sélectionnez chacun des onglets suivants pour voir quels paramètres vous pouvez ajuster pour chaque étape du constructeur.

{% tabs local %}
  {% tab Bases %}
    À ce niveau, vous configurerez les bases de votre Canvas.
    \- Donnez un nom à votre canvas
    \- Ajoutez des équipes
    \- Ajoutez des balises
    \- Affectez des événements de conversion et sélectionnez leurs types d’événements et les dates limites

    Learn more about the [Basics step](#step-2a-set-up-your-canvas-basics).
  {% endtab %}
  {% tab Planification d’entrée %}
    À ce niveau, vous déciderez de la façon dont vos utilisateurs accéderont à votre Canvas.
    \- Planification : Il s’agit d’une entrée Canvas basée sur le temps
    Basé sur l'action: Votre utilisateur accédera à votre Canvas après l’exécution d’une action définie
    Déclenché par l'API: Utilisez une demande API pour que des utilisateurs puissent accéder à votre Canvas

    Learn more about the [Entry Schedule step](#step-2b-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Audience cible %}
    À ce niveau, vous sélectionnerez votre audience cible :
    \- Créez votre audience en ajoutant des segments et des filtres
    \- Ajustez les limites d’entrées et nouvelles entrées du canvas
    \- Consultez une synthèse de votre audience cible

    Learn more about the [Target Audience step](#step-2c-set-your-target-entry-audience).
  {% endtab %}
  {% tab Paramètres d’envoi %}
    À ce niveau, vous sélectionnerez vos paramètres d’envoi de Canvas :
    \- Sélectionnez vos paramètres d'abonnement
    \- Définissez une limitation du débit d’envoi pour vos messages Canvas
    \- Activez et définissez les heures calmes

    Learn more about the [Send Settings step](#step-2d-select-your-send-settings).
  {% endtab %}
  {% tab Créer un canvas %}
    À ce niveau, vous allez créer votre Canvas.

    Learn how to [build your Canvas](#step-3-build-your-canvas) using the Canvas builder.
  {% endtab %}
  {% tab Résumé %}
    Ici, vous trouverez la synthèse des détails de votre canvas. Si vous avez activé le [flux de travail d'approbation Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/), vous pouvez approuver les détails du canvas répertoriés avant le lancement.

  {% endtab %}
{% endtabs %}

#### Étape 1.1 : Commencez par les bases de votre Canvas

Ici, vous nommerez votre Canvas, assignerez [des équipes]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams) et créerez ou ajouterez [des étiquettes]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags). Vous allez également affecter des événements de conversion pour le Canvas.

{% alert tip %}
Balisez vos Canvas pour qu’ils soient faciles à trouver et créez des rapports. Par exemple, lors de l'utilisation de [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), vous pouvez filtrer par des balises particulières.
{% endalert %}

![La page de détails du canvas, avec des champs pour le nom du canvas, la description, l'emplacement/localisation et les tags.]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

##### Sélectionner des événements de conversion

Choisissez votre type d'événement de conversion, puis sélectionnez les conversions à enregistrer. Ces [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) mesureront l'efficacité de votre canvas. 

![Événement de conversion principal A avec le type d'événement de conversion Effectue un achat pour enregistrer les conversations des utilisateurs qui effectuent un achat dans un délai de conversion de trois jours.]({% image_buster /assets/img/add_canvas_conversions.png %})

Si votre Canvas a plusieurs variantes ou un groupe de contrôle, Braze utilisera cet événement de conversion pour déterminer la meilleure variation pour atteindre cet objectif de conversion. À l’aide de la même logique, vous pouvez créer plusieurs événements de conversion.

#### Étape 1.2 : Déterminez votre planification d'entrée Canvas

Vous pouvez sélectionner l’un des trois modes d’accès à votre Canvas par les utilisateurs. 

##### Types de planification d’entrée

{% tabs local %}
  {% tab Livraison prévue %}
    Avec une livraison planifiée, les utilisateurs accéderont selon un calendrier, de la même façon que vous planifieriez une campagne. Vous pouvez inscrire des utilisateurs dans un Canvas dès qu'il est lancé, les intégrer dans votre parcours à un moment donné dans le futur, ou de manière récurrente (quotidienne, hebdomadaire ou mensuelle). 

    In this example, based on the time-based options, users will enter this Canvas every Tuesday at 12 pm in their local time zone every week, beginning November 14, 2025 until December 31, 2025.

    ![The "Entry Schedule" page with the type set to "Scheduled". Due to the selection, time-based options are shown, including frequency, start time, recurrence, days, and more.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab Livraison basée sur l'action %}
    Avec une livraison basée sur l'action, les utilisateurs entreront dans le Canvas et commenceront à recevoir des messages lorsqu'ils effectueront des actions particulières, telles que l'ouverture de votre application, l'achat ou le déclenchement d'un événement personnalisé.

    You can control other aspects of the Canvas behavior from the **Entry Audience** window, including rules for re-eligibility and frequency capping settings. Note that action-based delivery is unavailable for Canvas components with in-app messages.

    ![An example of action-based delivery. Users will enter the Canvas if they make a purchase with an entry window beginning at 1:30 pm on June 10, 2025.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

  {% endtab %}
  {% tab Livraison déclenchée par l'API %}
    Avec la livraison déclenchée par l'API, les utilisateurs entreront dans votre Canvas et commenceront à recevoir des messages après avoir été ajoutés en utilisant le [`/canvas/trigger/send` point de terminaison]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) via l'API. Dans le tableau de bord, vous trouverez un exemple de requête cURL à l’origine de cette action, et pourrez attribuer des [`canvas_entry_properties`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) facultatives à l’aide de [l’objet Propriétés d’entrées de Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). 

    ![An example of API-triggered delivery with a Canvas ID and an example of a cURL request.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    You can use the following endpoints for API-triggered delivery:
    - [POST: Send Canvas Messages via API-Triggered Delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: Schedule API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: Update Scheduled API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

Après avoir sélectionné votre méthode de livraison, ajustez les paramètres pour qu'ils correspondent à votre cas d'utilisation, puis continuez à définir votre public cible.

{% details Dédupliquer le comportement des Canvases en utilisant l'éditeur original %}
Si la fenêtre de rééligibilité est inférieure à la durée maximale du Canvas, un utilisateur sera autorisé à accéder à nouveau au Canvas et à recevoir plusieurs messages de composants. Dans le cas limite où un utilisateur accède à nouveau au même composant que l’accès précédent, Braze dédupliquera ces messages de composant. 

Si un utilisateur revient sur le Canvas, atteint le même composant que lors de son entrée précédente et est éligible pour un message intégré à l'application pour chaque entrée, l'utilisateur recevra le message deux fois (en fonction de la priorité du message intégré) tant qu'il rouvre une session deux fois.
{% enddetails %}

#### Étape 1.3 : Définir votre audience d’entrée cible

Vous pouvez définir le public cible de votre Canvas à l'étape **Public cible**. Seuls les utilisateurs qui correspondent à vos critères définis peuvent entrer dans le parcours, ce qui signifie que Braze évalue d'abord l'éligibilité du public cible avant que les utilisateurs n'entrent dans le parcours Canvas. Par exemple, si vous souhaitez cibler de nouveaux utilisateurs, vous pouvez sélectionner un segment d'utilisateurs qui ont utilisé votre application pour la première fois il y a moins d'une semaine.

Sous **Contrôles d'entrée**, vous pouvez limiter le nombre d'utilisateurs chaque fois que le Canvas est programmé pour s'exécuter. Pour les canvas déclenchés par API et livrés par événement, cette limite se produit à chaque heure UTC. 

{% alert warning %}
Évitez de configurer une campagne ou un Canvas basé sur une action avec le même déclencheur que le filtre d'audience (comme un attribut modifié ou un événement personnalisé effectué). Une condition de concurrence peut se produire lorsque l’utilisateur ne figure pas dans l’audience au moment de l’événement déclencheur, ce qui signifie qu’il ne recevra pas la campagne ou ne pourra pas accéder au Canvas.  
{% endalert %}

##### Tester votre audience

Après avoir ajouté des segments et des filtres à votre audience cible, vous pouvez tester si votre audience est configurée comme prévu en [recherchant un utilisateur]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) pour confirmer s'ils correspondent aux critères de l'audience.

![Le champ "Recherche d'utilisateurs", qui vous permet d'effectuer une recherche par ID externe ou ID Braze.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:100%;"}{: style="max-width:80%;"}

##### Sélection des contrôles d'entrée

Les contrôles d'entrée déterminent si les utilisateurs sont autorisés à entrer de nouveau dans un canvas. Vous pouvez également limiter le nombre de personnes susceptibles d'entrer dans ce Canvas en fonction d'une cadence choisie (quotidienne, pendant toute la durée du Canvas ou à chaque fois que le Canvas est planifié). 

Par exemple, si vous sélectionnez **Limiter le volume d'entrée** et que vous réglez le champ **Entrées maximales** sur 5 000 utilisateurs avec **Quotidien** comme cadence limite, alors le Canvas n'enverra qu'à 5 000 utilisateurs par jour.

![La page "Contrôles d'entrée" affiche des cases à cocher pour "Autoriser les utilisateurs à entrer à nouveau dans Canvas" et "Limiter le volume d'entrée". Ce dernier vous permet de définir le nombre maximum d'entrées et de préciser si vous souhaitez limiter les entrées par jour, pendant toute la durée de vie du canvas ou à chaque fois que le canvas est planifié.]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
Braze ne recommande pas d'utiliser la fonctionnalité **Chaque fois que la toile est planifiée** pour le réchauffement d'adresses IP, car cela peut entraîner une augmentation des volumes d'envoi.
{% endalert %}

##### Définir les critères de sortie

Définir les [critères de sortie]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) détermine quels utilisateurs vous souhaitez faire sortir d'un Canvas. Si un utilisateur effectue l'événement d'exception ou correspond aux segments et aux filtres, il ne recevra plus aucun message.

##### Calcul de la population cible

Dans la section **Population cible**, vous pouvez consulter un résumé de votre audience, comme les segments sélectionnés et les filtres supplémentaires, ainsi qu'une répartition du nombre d'utilisateurs atteignables par canal de communication. Pour calculer le nombre exact d'utilisateurs joignables dans votre audience cible au lieu de l'estimation par défaut, sélectionnez [Calculer des statistiques exactes]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics).

Remarques :

- Le calcul de statistiques exactes peut prendre quelques minutes. Cette fonction ne calcule les statistiques exactes qu'au niveau du segment, et non au niveau du filtre ou du groupe de filtres.
- Pour les segments de grande taille, il est normal de constater de légères variations, même en calculant des statistiques exactes. La précision de cette fonctionnalité devrait être égale ou supérieure à 99,999 %.

Pour afficher des statistiques supplémentaires, telles que le chiffre d'affaires moyen sur la durée de vie des utilisateurs ciblés, sélectionnez **Afficher les statistiques supplémentaires.**

![Ventilation de la population cible avec possibilité de calculer des statistiques exactes.]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

##### Pourquoi le nombre d'audiences cibles peut-il différer du nombre d'utilisateurs atteignables ?

{% multi_lang_include segments.md section='Differing audience size' %}

#### Étape 1.4 : Sélectionner vos paramètres d’envoi

Sélectionnez **Envoyer les paramètres** pour modifier vos paramètres d'abonnement, activer la limitation du débit et activer les heures de silence. En activant la [limite de débit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-canvas-components) ou la [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#frequency-capping), vous pouvez alléger la pression marketing exercée sur vos utilisateurs et vous assurer que vous ne leur envoyez pas trop de messages.

Pour le ciblage d’e-mail et les canaux de notification push de Canvas, vous pouvez limiter votre Canvas de sorte que seuls les utilisateurs explicitement inscrits reçoivent le message (utilisateurs inscrits ou non-inscrits exclus). Par exemple, supposons que vous ayez trois utilisateurs avec un statut d’abonnement différent :

- **Utilisateur A** est abonné à l'email et les notifications push sont activées. Cet utilisateur ne reçoit pas les e-mails, mais il recevra les notifications push.
- L'**utilisateur B** est abonné à l'e-mail mais n'est pas autorisé à utiliser la fonction "push". Cet utilisateur recevra les e-mails, mais pas les notifications push.
- **Utilisateur C** est abonné aux e-mails et les notifications push sont activées. Cet utilisateur recevra les e-mails et les notifications push.

Pour ce faire, définissez les **Paramètres d'abonnement** pour envoyer ce Canvas uniquement aux "utilisateurs ayant choisi de participer". Cette option garantira que seuls les utilisateurs abonnés recevront vos e-mails et Braze enverra uniquement vos notifications push aux utilisateurs pour lesquels la notification push est activée par défaut. 

Ces paramètres d’abonnement sont appliqués par étapes, ce qui signifie qu’ils n’ont pas d’effet sur votre audience d’entrée. Ainsi, ce paramètre est utilisé pour évaluer l'éligibilité d'un utilisateur à recevoir chaque étape Canvas.

{% alert important %}
Avec cette configuration, n'incluez aucun filtre dans l'étape **Target Audience** qui limite l'audience à un seul canal (par exemple, `Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

Si vous le souhaitez, spécifiez les heures de silence (la période pendant laquelle vos messages ne seront pas envoyés) pour votre Canvas. Cochez **Activer les heures calmes** dans vos **paramètres d'envoi**. Puis sélectionnez vos Heures calmes dans l’heure locale de vos utilisateurs et l’action qui suivra si le message se déclenche pendant ces heures calmes.

![La page "Heures calmes" affiche une case à cocher permettant d'activer les heures calmes. Si elle est activée, l'heure de début, l'heure de fin et le comportement de repli peuvent être définis.]({% image_buster /assets/img/quiet_hours.png %})

### Étape 2 : Créer votre Canvas

{% alert tip %}
Enregistrez votre temps et rationalisez votre création de canvas en utilisant les [modèles de Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/#available-braze-templates)! Parcourez notre bibliothèque de modèles préconstruits pour trouver celui qui correspond à votre cas d'utilisation et personnalisez-le pour répondre à vos besoins spécifiques.
{% endalert %}

#### Étape 2.1 : Ajouter une variante

![Le bouton "Ajouter une variante" est sélectionné pour afficher un menu contextuel avec l'option "Ajouter une variante".]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

Sélectionnez **Ajouter une variante**, puis ajoutez une nouvelle variante à votre Canvas. Les variantes représentent un parcours que vos utilisateurs emprunteront et peuvent contenir plusieurs étapes et branches.

Vous pouvez ajouter des variantes supplémentaires en sélectionnant le bouton <i class="fas fa-plus-circle"></i> plus. Lorsque vous ajoutez de nouvelles variantes, vous pourrez ajuster la façon dont elles seront réparties parmi vos utilisateurs de sorte que vous puissiez comparer et analyser l’efficacité des différentes stratégies d’engagement.

![Deux exemples de variante du canvas Braze.]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
Par défaut, l'assignation de variante de Canvas est verrouillée lorsque les utilisateurs entrent dans le Canvas, ce qui signifie que si un utilisateur entre d'abord dans une variante, ce sera sa variante à chaque fois qu'il rentrera dans le Canvas. Cependant il existe des façons d’éviter ce comportement. <br><br>Pour ce faire, vous pouvez créer un générateur de nombres aléatoires à l’aide de Liquid, l’exécuter chaque fois qu’un utilisateur accède à Canvas, archiver la valeur comme attribut personnalisé puis utiliser cet attribut pour diviser les utilisateurs de manière aléatoire.

{% details Développer pour les étapes %}

1. Créez un attribut personnalisé pour archiver votre nombre aléatoire. Nommez-le quelque chose de facile à localiser, comme "numéro_de_loterie" ou "attribution_aléatoire". Vous pouvez créer l'attribut soit [dans votre tableau de bord]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/), soit par des appels API à notre [`/users/track` point de terminaison]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).<br><br>
2. Créez une campagne webhook au début de votre Canvas. Cette campagne sera le moyen par lequel vous créerez votre nombre aléatoire et le stockerez en tant qu'attribut personnalisé. Consultez [Créer un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook) pour plus d'informations. Définissez l'URL sur notre `/users/track` point de terminaison.<br><br>
3. Créez le générateur de nombres aléatoires. Vous pouvez le faire avec le code [présenté ici](https://community.shopify.com/c/technical-q-a/is-there-any-way-to-generate-random-number-with-liquid-shopify/m-p/1595486), qui tire parti de l'heure d'entrée unique de chaque utilisateur pour créer un numéro aléatoire. Définissez le nombre qui en résulte comme variante Liquid dans votre campagne webhook.<br><br>
4. Formatez l’appel `/users/track` dans votre campagne webhook de sorte qu’il définisse l’attribut personnalisé que vous avez créé à l’étape 1 pour le nombre aléatoire que vous avez généré sur votre profil utilisateur actuel. L’exécution de cette étape vous permettra de créer correctement un nombre aléatoire qui change chaque fois que votre utilisateur accède à votre campagne.<br><br>
5. Ajustez les branches de votre Canvas de sorte qu’elles soient divisées en fonction des règles d’audience plutôt qu’en variantes sélectionnées de manière aléatoire. Dans les règles d’audience de chaque branche, définissez le filtre d’audience en fonction de votre attribut personnalisé. <br><br>Par exemple, une branche peut avoir « numéro de loterie est inférieur à 3 » comme filtre d’audience, alors qu’une autre branche peut avoir « numéro de loterie est supérieur à 3 et inférieur à 6 » comme filtre d’audience.

{% enddetails %}
{% endalert %}

#### Étape 2.2 : Ajouter des étapes du canvas

Vous pouvez ajouter plus d'étapes à votre flux de travail Canvas en faisant glisser et déposer des composants depuis la barre latérale des **Composants**. Vous pouvez également sélectionner le bouton plus <i class="fas fa-plus-circle"></i> pour ajouter un composant avec le menu contextuel.

{% alert tip %}
Au fur et à mesure que vous commencez à ajouter plus d'étapes, vous pouvez changer le niveau de zoom pour vous concentrer sur les détails ou pour avoir une vue d'ensemble du parcours utilisateur. Zoomer avec <kbd>Shift</kbd> + <kbd>+</kbd> ou dézoomer avec <kbd>Shift</kbd> + <kbd>-</kbd>.
{% endalert %}

![La fenêtre de recherche de composants ajoutant une étape du canvas de Braze.]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert warning %}
Un Canvas créé en utilisant Canvas Flow peut comprendre jusqu’à 200 étapes. Des erreurs de chargement se produiront si votre Canvas a plus de 200 étapes.
{% endalert %}

##### Durée maximale

Au fur et à mesure que votre parcours Canvas augmente en étapes, la durée maximale est le temps le plus long possible qu'un utilisateur peut prendre pour compléter ce Canvas. Ceci est calculé en ajoutant les délais et les fenêtres de déclenchement de chaque étape pour chaque variante pour le chemin le plus long. Par exemple, si votre canvas a une étape de délai avec un délai de 3 jours et une étape Message, la durée maximale de votre canvas sera de 3 jours.

##### Modification d’une étape

Vous désirez modifier une étape dans votre parcours utilisateur ? Regardez comment le faire selon votre flux de travail Canvas !

Vous pouvez modifier n'importe quelle étape de votre flux de travail Canvas Flow en sélectionnant n'importe lequel des composants. Par exemple, disons que vous souhaitez modifier votre première étape, un composant de [Retard]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), dans votre flux de travail à un jour spécifique. Sélectionnez l'étape pour afficher ses paramètres et ajustez votre délai sur le 1er mars. Ceci signifie que le 1er mars, vos utilisateurs passeront à l’étape suivante de votre Canvas.

![Exemple d'étape "Délai" avec le délai réglé sur "Jusqu'à un jour précis".]({% image_buster /assets/img_archive/edit_delay_flow.png %})

Ou vous pouvez rapidement modifier et ajuster les **Paramètres d'Action** de votre [Chemins d'Action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) étape pour retenir les utilisateurs pendant une période de temps. Leur parcours suivant est donc priorisé selon les actions intervenant durant cette période d’évaluation.

![La deuxième étape du canvas, "Paramètres des actions", avec une fenêtre d'évaluation fixée à 1 jour.]({% image_buster /assets/img_archive/action_paths_flow.png %})

Les composants légers de Canvas permettent une expérience d’édition facilitée. Ajuster les détails les plus précis de votre Canvas en est d’autant plus simple. 

##### Messages dans Canvas

Modifiez des messages dans un composant Canvas pour contrôler les messages envoyés dans une étape spécifique. Canvas peut envoyer des messages par e-mail, téléphone mobile, notification push Web et webhooks pour s’intégrer à d’autres systèmes. Similaire aux campagnes, vous pouvez utiliser certains [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) modèles pour personnaliser vos messages.

{% alert tip %}
Savez-vous que vous pouvez inclure des noms de composants Canvas dans vos messages et vos modèles de lien ?<br>
Utilisez la balise Liquid `campaign.${name}` dans Canvas pour afficher le nom du composant Canvas actuel.
{% endalert %}

Le composant de message gère les messages envoyés aux utilisateurs. Vous pouvez sélectionner vos **canaux de messagerie** et ajuster les **paramètres de livraison** pour optimiser votre messagerie Canvas. Pour plus de détails sur ce composant, consultez la section [Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

![L'étape "Configurer les messages", avec "Canaux d'envoi" sélectionné, affiche la liste des canaux de communication disponibles, tels les notifications push Android, les cartes de contenu, l'e-mail, et plus encore.]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

Sélectionnez **Terminé** après avoir terminé la configuration de votre composant Canvas.

{% tabs local %}
{% tab Propriétés d'entrée de la toile %}

Les `canvas_entry_properties` sont configurés dans l'étape de planification d'entrée de la création d'un Canvas et indiquent le déclencheur qui fait entrer un utilisateur dans un Canvas. Ces propriétés peuvent également accéder aux propriétés des charges utiles d’entrée dans les Canvas déclenchés par API. Notez que l'objet `canvas_entry_properties` peut avoir une taille maximale de 50 Ko. 

Utilisez le code Liquid suivant lorsque vous faites référence à ces propriétés d'entrée : {% raw %} ``canvas_entry_properties.${property_name}`` {% endraw %}. Notez que les événements doivent être des événements personnalisés ou des événements d'achat pour être utilisés de cette manière.

{% raw %}
Imaginons, par exemple, la requête suivante : `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Vous pourriez ajouter le mot « chaussures » à un message avec ce code Liquid ``{{canvas_entry_properties.${product_name}}}``.
{% endraw %}

{% endtab %}

{% tab Propriétés de l'événement %}
Les propriétés de l’événement sont les propriétés que vous avez définies sur des événements personnalisés et des achats. Ces `event_properties` peuvent être utilisées dans les campagnes ayant une livraison par événement ainsi que dans les Canvas. 

Dans Canvas Flow, les événements personnalisés et les propriétés de l’événement d’achat peuvent être utilisées en Liquid dans n’importe quelle étape de message suivant une étape de parcours d’action. Utilisez ce code Liquid {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %} lorsque vous faites référence à ces `event_properties`. Ces événements doivent être des événements personnalisés ou d’achat pour être utilisés ainsi dans le composant de message.

Dans la première étape de message suivant un parcours d’action, vous pouvez utiliser les `event_properties` liées à l’événement référencé dans le parcours d’action. Vous pouvez disposer d’autres étapes (n’étant pas un autre parcours d’action ou une étape de message) entre cette étape de parcours d’action et celle de message. Prenez en compte le fait que vous n’aurez accès aux `event_properties` que si votre étape de message peut être remontée jusqu’à un parcours n’étant pas « Tous les autres » dans l’étape du parcours d’action

{% endtab %}
{% endtabs %}

#### Étape 2.3 : Modifier les connexions

Pour déplacer une connexion entre des étapes, sélectionnez la flèche reliant les deux composants et sélectionnez un autre composant. Pour supprimer la connexion, sélectionnez la flèche suivie de **Annuler la connexion** dans le pied de page du compositeur Canvas.

### Étape 3 : Ajouter un groupe de contrôle

Vous pouvez ajouter un groupe de contrôle à votre canvas en sélectionnant le bouton plus <i class="fas fa-plus-circle"></i> pour ajouter une nouvelle variante. 

Braze assurera un suivi des conversions des consommateurs figurant dans ce groupe de contrôle. Ils ne recevront toutefois aucun message. Pour garantir la précision du test, nous suivrons le nombre de conversions pour vos variantes et votre groupe de contrôle pour la même durée, comme il est indiqué dans l'écran de sélection de l'événement de conversion. 

Pour modifier la diffusion de vos messages, double-cliquez sur les en-têtes **Nom de variante (Variant Name).**

Dans cet exemple, notre Canvas est réparti en deux variantes. La variante 1 concerne 70 % des consommateurs. La seconde variante est un groupe de contrôle qui rassemble les 30 % de consommateurs restants.

![Un exemple de variante dans un canvas Braze, où 70 % vont à la "variante 1", qui retarde d'un jour dans la première étape, puis envoie un message dans la deuxième étape. Les 30 % restants sont dirigés vers un "contrôle" qui ne prévoit aucune mesure de suivi.]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

#### Sélection intelligente pour Canvas

Les fonctionnalités de sélection intelligente sont désormais disponibles dans les Canvas multivariés. À l'instar de la fonctionnalité de [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) pour les campagnes multivariées, la sélection intelligente pour Canvas analyse les performances de chaque variante de Canvas et ajuste le pourcentage d'utilisateurs entonnoir par le biais de chaque variante. Cette répartition est basée sur les indicateurs de performance de chaque variante afin de maximiser le nombre total de conversions attendues.

N’oubliez pas que les Canvas multivariés vous permettent plutôt de tester que de copier, mais le calendrier et les canaux également. La sélection intelligente vous permet de tester des Canvas de manière plus efficace et de garantir que vos utilisateurs seront dirigés vers le meilleur parcours Canvas.

![L'option "Sélection intelligente" est activée dans la page "Modifier la répartition des variantes". Au fur et à mesure qu'il analyse et optimise le canvas, il affiche une barre horizontale en travers de la page qui est divisée en plusieurs sections, chacune variant en couleur et en taille. Il s'agit uniquement d'une représentation visuelle qui ne correspond à aucune analyse/analytique spécifique.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

La sélection intelligente pour Canvas optimise vos résultats Canvas en effectuant des ajustements progressifs en temps réel à la distribution des utilisateurs triés dans chaque variante. Lorsque l'algorithme statistique détermine un gagnant décisif parmi vos variantes, il élimine les variantes moins performantes et place tous les futurs destinataires éligibles de la toile dans les variantes gagnantes. 

En ce sens, la sélection intelligente fonctionne mieux sur des Canvas auxquels de nouveaux utilisateurs accèdent fréquemment.

### Étape 4 : Enregistrer et lancer

Une fois la création de votre canvas terminée, sélectionnez **Lancer le canvas** pour enregistrer et lancer votre canvas. Après avoir lancé votre Canvas, vous pourrez consulter les analyses de votre parcours au fur et à mesure qu'elles arrivent sur la page **Canvas Details**. 

Vous pouvez également enregistrer votre Canvas en tant que brouillon si vous souhaitez le retravailler un peu plus tard.

![Exemple de toile en Braze.]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
Vous avez besoin de modifier votre Canvas après son lancement ? C’est tout à fait possible. Consultez [Modification des toiles après le lancement]({{site.baseurl}}/post-launch_edits/) pour plus d'informations.
{% endalert %}

