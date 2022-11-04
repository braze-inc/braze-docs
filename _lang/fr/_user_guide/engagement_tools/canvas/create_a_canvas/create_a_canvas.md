---
nav_title: Création d’un Canvas
article_title: Création d’un Canvas
page_order: 0
page_type: reference
description: "Cet article de référence aborde les étapes nécessaires à la création, à la gestion et aux essais d’un Canvas."
tool: Canvas

---

# Création d’un Canvas

> Cet article de référence aborde les étapes nécessaires à la création, à la gestion et aux essais d’un Canvas. Suivez ce guide ou consultez notre [Cours d’apprentissage Braze Canvas](https://learning.braze.com/quick-overview-canvas-setup) !

## Étape 1 : Créer un Canvas

![][1]{: style="float:right;max-width:20%;margin-left:10px;margin-top:10px;margin-bottom:10px;"}

Accédez à la page **Canvas**, située sous la section **Engagement**, puis cliquez sur **Créer un Canvas**.

## Étape 2 : Utiliser l’assistant d’entrée pour configurer votre Canvas

L’assistant d’entrée vous guidera tout au long de la configuration de votre Canvas, de la désignation à la définition d’événements de conversion et du transfert des utilisateurs appropriés à votre parcours client. Cliquez sur chacun des onglets suivants pour voir les paramètres que vous pouvez ajuster dans chacune des étapes d’assistant d’entrée.

{% tabs local %}
  {% tab Basics %}
    À ce niveau, vous configurerez les bases de votre Canvas.
    - Donnez un nom à votre Canvas
    - Ajoutez Teams à votre Canvas
    - Ajoutez des balises à votre Canvas
    - Affectez des événements de conversion et sélectionnez les types d’événements et les dates limites

    En savoir plus sur les [Bases](#step-2a-set-up-your-canvas-basics).
  {% endtab %}
  {% tab Entry Schedule %}
    À ce niveau, vous déciderez de la façon dont vos utilisateurs accéderont à votre Canvas.
    - Scheduled: Il s’agit d’une entrée Canvas basée sur le temps
    - Action-Based: Votre utilisateur accédera à votre Canvas après l’exécution d’une action définie
    - API-Triggered: Utilisez une demande API pour que des utilisateurs puissent accéder à votre Canvas

    En savoir plus sur l’[étape Planification d’entrée](#step-2b-set-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Entry Audience %}
    À ce niveau, vous sélectionnerez votre Audience d’entrée Canvas :
    - Créez votre audience en ajoutant des segments et des filtres
    - Affiner Nouvelle entrée et Limites d’entrée Canvas
    - Consulter une synthèse de votre audience cible

    En savoir plus sur l’[étape Audience d’entrée](#step-2c-set-your-target-entry-audience).
  {% endtab %}
  {% tab Send Settings %}
    À ce niveau, vous sélectionnerez vos paramètres d’envoi de Canvas :
    - Sélectionnez vos paramètres d’inscription
    - Définissez une limitation du débit d’envoi pour vos messages Canvas
    - Activer et définir des heures calmes

    En savoir plus sur l’[étape Paramètres d’envoi](#step-2d-select-your-send-settings)
  {% endtab %}
  {% tab Build Canvas %}
    À ce niveau, vous allez créer votre Canvas.

    Découvrez comment [créer votre Canvas](#step-3-build-your-canvas) à l’aide de l’éditeur de Canvas.
  {% endtab %}
{% endtabs %}

### Étape 2a : Configurer les bases de votre Canvas :

À ce niveau, vous allez désigner votre Canvas, affecter [Teams]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams) et créer ou ajouter des [balises]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags). À ce niveau, vous allez également affecter des événements de conversion pour le Canvas.

{% alert tip %}
Balisez vos Canvas pour qu’ils soient faciles à trouver et créez des rapports. Par exemple, lorsque vous utilisez [Créateur de rapports]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/), vous pouvez filtrer les éléments par balises spécifiques
{% endalert %}

![Bases][51]

#### Sélectionner des événements de conversion

Sélectionnez votre type d’événement de conversion puis sélectionnez les conversions que vous souhaiteriez enregistrer.

![][52]

Nous utiliserons l’[événement de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/) que vous définissez dans cet écran pour mesurer l’efficacité de votre Canvas.

Si votre Canvas a plusieurs variantes ou un groupe de contrôle, Braze utilisera cet événement de conversion pour déterminer la meilleure variation pour atteindre cet objectif de conversion. À l’aide de la même logique, vous pouvez créer plusieurs événements de conversion.

### Étape 2b : Définir votre planification d’entrée Canvas

Vous pouvez sélectionner l’un des trois modes d’accès à votre Canvas par les utilisateurs :

- Livraison planifiée
- Livraison par événement
- Livraison déclenchée par API

Une fois que vous avez sélectionné le mode que vous utiliserez, ajustez ces paramètres en conséquence et passez à la configuration de votre audience cible.

![][53]

#### Types de planification d’entrée

{% tabs local %}
  {% tab Scheduled Delivery %}
    Avec une livraison planifiée, les utilisateurs accéderont à un calendrier, de la même façon que vous planifieriez une campagne. Vous pouvez inscrire des utilisateurs à un Canvas dès qu’il est lancé ou les intégrer à votre parcours à un moment donné ou de façon récurrente.

    ![Livraison Canvas planifiée]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab Action-Based Delivery %}
    Avec cette livraison par événement, vous pouvez choisir d’intégrer des utilisateurs à un Canvas lorsqu’ils actionnent certains déclencheurs. Les utilisateurs accéderont à votre Canvas et commenceront à recevoir des messages lors d’activités particulières, comme ouvrir votre application, effectuer un achat ou déclencher un événement personnalisé. <br><br>Notez que cette livraison par événement n’est pas disponible pour des Canvas Steps avec des messages in-app.

    ![Livraison par événement Canvas]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

    Vous pouvez contrôler d’autres aspects de votre comportement de Canvas dans la fenêtre **Audience d’entrée**, incluant des règles de rééligibilité et des paramètres de limite de fréquence.
  {% endtab %}
  {% tab API-Triggered Delivery %}
    Avec la livraison déclenchée par API, vous pouvez décider d’intégrer des utilisateurs à un Canvas via une demande API. Sur le tableau de bord, vous trouverez un exemple de demande cURL à l’origine de cette action qui affecte [`canvas_entry_properties`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) facultatif à l’aide de [`Canvas Entry Properties Object`]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). <br><br>Les utilisateurs accéderont à votre Canvas et commenceront à recevoir des messages une fois qu’ils auront été ajoutés à l’aide de l’endpoint [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) via l’API.

    ![Livraison déclenchée par API Canvas]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    Endpoints de livraison déclenchés par API :
    - [POST: Envoyer des messages Canvas via la livraison déclenchée par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: Planifier des Canvas déclenchés par API]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: Mettre à jour des Canvas planifiés déclenchés par API]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

<!--Tag allows alert to be linked to-->
<a id="important-edge-case"></a>

{% alert important %}
Si la fenêtre de rééligibilité est inférieure à la durée maximale du Canvas, un utilisateur sera autorisé à accéder à nouveau au Canvas et à recevoir plusieurs messages d’étapes. Lors d’un nouvel accès, lorsqu’un utilisateur accède à nouveau à la même étape que l’accès précédent, Braze dédupliquera ces messages d’étape. <br><br>Si un utilisateur accède à nouveau au Canvas, atteint la même étape qu’à l’accès précédent, est éligible à un message In-App pour chaque entrée, il recevra le message deux fois (en fonction de la priorité de message In-App) à condition qu’il rouvre une session deux fois.
{% endalert %}

### Étape 2c : Définir votre audience d’entrée cible :

Vous pouvez définir l’audience cible pour votre Canvas à l’étape **Audience d’entrée**. Seuls les utilisateurs répondant aux critères définis peuvent accéder au parcours.

![][54]

Par exemple, si vous souhaitez cibler de nouveaux utilisateurs, vous pouvez limiter un parcours spécifique aux utilisateurs ayant accédé à votre application en premier, il y a moins de 3 semaines. Vous pouvez également contrôler des paramètres, par exemple si des messages doivent être envoyés aux utilisateurs inscrits pour recevoir des notifications.

{% alert warning %}
Éviter de configurer une campagne basée sur une action ou un Canvas avec le même déclencheur que le filtre d’audience (c’est-à-dire un attribut modifié ou un événement personnalisé effectué). Une condition de concurrence peut se produire lorsque l’utilisateur ne figure pas dans l’audience au moment de l’événement déclencheur, ce qui signifie qu’il ne recevra pas la campagne ou ne pourra pas accéder au Canvas.  
{% endalert %}

### Étape 2d : Sélectionner vos paramètres d’envoi

Cliquez sur **Paramètres d’envoi** pour sélectionner vos paramètres d’inscription, activer la limitation du débit et les heures calmes.

![][55]

En activant [Limitation du taux][6b] ou [Limite de fréquence][6c], vous pouvez alléger la pression marketing subie par vos utilisateurs et vérifier qu’ils ne sont pas surchargés de messages.

{% alert note %}
Consultez notre page [Global Message Settings](https://dashboard-01.braze.com/engagement/global_message_settings/) dans votre compte Braze pour gérer vos règles de Limite de fréquence.
{% endalert %}

Pour le ciblage d’e-mail et les canaux de notification push de Canvas, vous pouvez limiter votre Canvas de sorte que seuls les utilisateurs explicitement inscrits reçoivent le message (utilisateurs inscrits ou non-inscrits exclus). Par exemple, supposons que vous ayez trois utilisateurs avec un statut d’abonnement différent :

- **L’utilisateur A** est inscrit aux e-mails et la notification push est activée. Cet utilisateur ne reçoit pas les e-mails, mais il recevra les notifications push.
- L’**utilisateur B** est abonné aux e-mails, mais la notification push n’est pas activée. Cet utilisateur recevra les e-mails, mais ne reçoit pas les notifications push.
- L’**utilisateur C** est inscrit aux e-mails et la notification push est activée. Cet utilisateur recevra les e-mails et les notifications push.

Pour ce faire, définissez les **Paramètres d’inscription** pour envoyer ce Canvas « uniquement aux utilisateurs abonnés ». Cette option garantira que seuls les utilisateurs abonnés recevront vos e-mails et Braze enverra uniquement vos notifications push aux utilisateurs pour lesquels la notification push est activée par défaut.

{% alert important %}
Avec cette configuration, n’incluez pas de filtres dans l’étape **Utilisateurs cible** qui limitent l’audience à un seul canal (par ex. `Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

Si vous le souhaitez, indiquez Heures calmes (période pendant laquelle vos messages ne seront pas envoyés) pour votre Canvas. Cochez **Activer heures calmes** dans vos **Paramètres d’envoi**. Puis sélectionnez vos Heures calmes dans l’heure locale de vos utilisateurs et l’action qui suivra si le message se déclenche pendant ces heures calmes.

![][50]

## Étape 3 : Créer votre Canvas

### Ajouter une variante

![][11]{: style="float:right;max-width:40%;margin-left:15px;"}

Cliquez sur **Ajouter une variante** et sélectionnez l’option pour ajouter une nouvelle variante à votre Canvas. Les variantes représentent un parcours effectué par vos utilisateurs et peuvent contenir plusieurs étapes et branches.

Vous pouvez ajouter des variantes supplémentaires en cliquant sur le bouton <i class="fas fa-plus-circle"></i> Plus. Lorsque vous ajoutez de nouvelles variantes, vous pourrez ajuster la façon dont elles seront réparties parmi vos utilisateurs de sorte que vous puissiez comparer et analyser l’efficacité des différentes stratégies d’engagement.

![][12]

{% alert tip %}
Par défaut, l’affectation de Canvas Variant est bloquée lorsque des utilisateurs accèdent à Canvas, ce qui signifie que si un utilisateur saisit d’abord une variante, cette dernière reste définie à chaque accès au Canvas. Cependant il existe des façons d’éviter ce comportement. <br><br>Pour ce faire, vous pouvez créer un générateur de nombres aléatoires à l’aide de Liquid, l’exécuter chaque fois qu’un utilisateur accède à Canvas, archiver la valeur comme attribut personnalisé puis utiliser cet attribut pour diviser les utilisateurs de manière aléatoire.

{% details Expand for steps %}

1. Créez un attribut personnalisé pour archiver votre nombre aléatoire. Attribuez-lui un nom simple pour le retrouver, par exemple « numéro_de loterie » ou « affectation_aléatoire ». Vous pouvez créer l’attribut [dans votre tableau de bord]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/custom_event_and_attribute_management/) ou via des appels API sur votre Endpoint [Suivi de l’utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)<br><br>
2. Créez une campagne webhook au début de votre Canvas. Cette campagne servira de support pour créer votre nombre aléatoire et l’archiver comme attribut personnalisé. Reportez-vous à [Création d’un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook) pour en savoir plus. Saisissez l’URL pour votre Endpoint Suivi utilisateur.<br><br>
3. Créez le générateur de nombres aléatoires. Vous pouvez le faire à l’aide du code [indiqué ici](https://www.131-studio.com/blogs/shopify-conversion/generate-random-numbers-using-liquid-shopify), qui se sert de l’accès unique de chaque utilisateur pour créer un nombre aléatoire. Définissez le nombre qui en résulte comme variante Liquid dans votre campagne webhook.<br><br>
4. Formatez l’appel `users/track` dans votre campagne webhook de sorte qu’il définisse l’attribut personnalisé que vous avez créé à l’étape 1 pour le nombre aléatoire que vous avez généré sur votre profil utilisateur actuel. L’exécution de cette étape vous permettra de créer correctement un nombre aléatoire qui change chaque fois que votre utilisateur accède à votre campagne.<br><br>
5. Ajustez les branches de votre Canvas de sorte qu’elles soient divisées en fonction des règles d’audience plutôt qu’en variantes sélectionnées de manière aléatoire. Dans les règles d’audience de chaque branche, définissez le filtre d’audience en fonction de votre attribut personnalisé. <br><br>Par exemple, une branche peut avoir « numéro de_loterie est inférieur à 3 » comme filtre d’audience, alors qu’une autre branche peut avoir « numéro_de loterie est supérieur à 3 et inférieur à 6 » comme filtre d’audience.

{% enddetails %}
{% endalert %}

### Modification d’une étape

Cliquez n’importe où dans une étape pour que Braze ouvre l’interface de modification d’étape. Les étapes peuvent être configurées pour envoyer des messages après un délai défini (31 jours au maximum) ou lorsqu’un utilisateur exécute une action spécifique. Par exemple, vous pouvez utiliser Canvas pour configurer une campagne d’intégration Jour 1, Jour 3, Jour 7 avec des laps de temps entre les messages :

![Canvas Jour un][13]

Ou vous pouvez définir un groupe de messages à envoyer une fois que vos utilisateurs ont pris une mesure spécifique, avec une fenêtre, un délai et des [événements d’exception][56] pouvant être configurés :

![Événements d’exception Canvas][14]

Vous pouvez également appliquer des **Filtres** à chaque étape d’un Canvas. Utilisez cette action pour ajouter une logique de flux de contrôle supplémentaire, par exemple, exclure des utilisateurs d’un parcours lorsqu’il est probable qu’ils n’aient plus besoin d’encouragement supplémentaire :

![Engagement supplémentaire Canvas][15]

{% alert note %}
Par défaut, les filtres et segments pour des **Étapes complètes** dans Canvas sont cochés à l’heure de l’envoi. Cependant, pour les [Étapes de fractionnement des décisions]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/), une évaluation d’audience est effectuée dès réception de l’étape précédente ou après un délai (si vous en avez configuré un).
{% endalert %}

#### Messages dans Canvas

Modifiez des messages dans une Canvas Step pour contrôler les messages envoyés dans une étape spécifique. Canvas peut envoyer des messages par e-mail, téléphone mobile et notification Web et webhooks pour s’intégrer à d’autres systèmes. De la même façon que pour les messages de campagne, vous pouvez utiliser la création d’un modèle Liquid spécifique pour personnaliser vos messages.

![][16]

Sélectionnez le **Comportement d’avancement** de votre choix. En savoir plus sur l’[avance des utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) dans les Canvas Steps.

![Options de comportement d’avance pour une Canvas Step avec l’option permettant d’avancer les utilisateurs lorsque le message est envoyé ou pour avancer l’audience après un délai d’un jour.][20]

Cliquez sur **Effectué** une fois que vous avez terminé la configuration de votre Canvas Step.

{% tabs local %}
{% tab Canvas Entry Properties %}
Les [Propriétés d’entrée Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) désignent les propriétés que vous mappez, lorsque vous déclenchez ou planifiez un Canvas via l’API. Notez que l’objet des propriétés d’entrée Canvas a une taille maximale limite de 50 KB.

{% raw %}
Par exemple, une requête avec `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}` pourrait inclure le terme \"chaussures\"à un message en ajoutant Liquid `{{canvas_entry_properties.${product_name}}}`
{% endraw %}

{% alert note %}
Les propriétés d’entrée Canvas peuvent uniquement être référencées dans la première étape d’un Canvas.
{% endalert %}

{% endtab %}

{% tab Custom Event Properties %}
Les [propriétés d’événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) désignent les propriétés que vous avez définies sur des événements personnalisés et des achats, utilisées surtout dans les campagnes Livraison par événement. Ces propriétés sont éphémères et peuvent être utilisées uniquement lorsqu’elles apparaissent. <br><br>Les propriétés de l’événement ne sont pas définitives, donc si vous planifiez une Canvas Step plutôt que d’utiliser une livraison par événement, vous ne pourrez pas utiliser une propriété de l’événement (car nous n’archivons pas ces données). Vous ne pouvez pas référencer la propriété d’événement pour un événement qui s’est déjà produit.

{% alert note %}
Les propriétés d’événement personnalisées peuvent être référencées uniquement dans la première étape d’un Canvas.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert tip %}
Savez-vous que vous pouvez inclure des noms de Canvas Step dans vos messages et des modèles de lien ?<br>
Utilisez la balise Liquid `campaign.${name}` dans Canvas pour afficher le nom de Canvas Step actuel.
{% endalert %}

### Ajout d’étapes supplémentaires

Ajoutez plus d’étapes en cliquant sur le bouton <i class="fas fa-plus-circle"></i> Plus :

![][17]{: style="max-width:75%;"}

### Modifications de connexions

Pour déplacer une connexion entre des étapes, cliquez sur la flèche reliant les deux étapes et sélectionnez une étape différente. Pour rompre la connexion, cliquez sur la flèche et sur **Annuler la connexion** en pied de page de l’éditeur Canvas.

![][2]

## Étape 4 Utiliser le test multivarié via Canvas.

Vous pouvez ajouter un groupe de contrôle à votre Canvas en cliquant sur le bouton <i class="fas fa-plus-circle"></i> plus pour ajouter une nouvelle variante.

Braze effectuera un suivi des conversions pour les utilisateurs figurant dans le groupe de contrôle, même s’ils ne recevront pas de messages. Pour conserver un test précis, nous effectuerons un suivi du numéro de conversions pour vos variantes et le groupe de contrôle pendant exactement le même laps de temps, comme décrit à l’écran de sélection Événement de conversion.

Vous pouvez ajuster la répartition entre vos messages en double-cliquant dans les en-têtes **Nom de variante**.

![][18]

### Sélection intelligente pour Canvas

Les fonctionnalités de sélection intelligente sont désormais disponibles dans les Canvas multivariés Comme pour la fonctionnalité [Sélection intelligente][18a] pour des campagnes multivariées, la sélection intelligente pour Canvas analyse la performance de chaque Canvas Variant et ajuste le pourcentage d’utilisateurs à diriger via chaque variante. Cette répartition est basée sur chaque métrique de performance de variante pour augmenter le nombre total de conversions escompté.

N’oubliez pas que les Canvas multivariés vous permettent plutôt de tester que de copier, mais le calendrier et les canaux également. La sélection intelligente vous permet de tester des Canvas de manière plus efficace et de garantir que vos utilisateurs seront dirigés vers le meilleur parcours Canvas.

![][18b]

La sélection intelligente pour Canvas optimise vos résultats Canvas en effectuant des ajustements progressifs en temps réel sur la répartition des utilisateurs triés dans chaque variante. Lorsque l’algorithme statistique détermine un élément pertinent parmi vos variantes, il éliminera les variantes peu performantes et reliera tous les futurs destinataires éligibles du Canvas aux variantes pertinentes.

En ce sens, la sélection intelligente fonctionne mieux sur des Canvas auxquels de nouveaux utilisateurs accèdent fréquemment.

## Étape 5 : Sauvegarder et lancer vos Canvas

Une fois que vous avez fini de créer votre Canvas, cliquez sur **Lancer un Canvas** pour enregistrer et lancer votre Canvas. Vous pouvez également enregistrer votre Canvas comme ébauche si vous devez y revenir.

Une fois que vous avez lancé votre Canvas, vous pourrez voir les éléments analytiques de votre parcours en accédant à la page **Détails de Canvas**.

![][19]


[1]:{% image_buster /assets/img_archive/canvas_dropdown.png %}
[2]: {% image_buster /assets/img_archive/canvas_connection_edit.gif %}
[6b]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting
[6c]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping
[11]:{% image_buster /assets/img_archive/canvas_add_variant.gif %}
[12]:{% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %}
[13]:{% image_buster /assets/img_archive/Canvas_One_Day.png %}
[14]:{% image_buster /assets/img_archive/Canvas_Exception_Events.png %}
[15]:{% image_buster /assets/img_archive/Canvas_Additional_Engagement.png %}
[16]:{% image_buster /assets/img_archive/Canvas_Message_Edit.png %}
[17]:{% image_buster /assets/img_archive/Canvas_More_Step.png %}
[18]:{% image_buster /assets/img_archive/Canvas_Multivariate.png %}
[18a]: {{site.baseurl}}/user_guide/intelligence/intelligent_selection/
[18b]: {% image_buster /assets/img_archive/canvas_intelligent_selection.png %}
[19]:{% image_buster /assets/img_archive/Canvas_Analytics.png %}
[20]:{% image_buster /assets/img_archive/Canvas_Advancement_Behavior.png %}
[50]: {% image_buster /assets/img/quiet_hours.png %}
[51]: {% image_buster /assets/img/Basics1.gif %}
[52]: {% image_buster /assets/img/add_canvas_conversions.png %}
[53]: {% image_buster /assets/img/entry-schedule-canvas-1.gif %}
[54]: {% image_buster /assets/img/entry-audience-canvas-1.gif %}
[55]: {% image_buster /assets/img/canvas-send-settings-1.gif %}
[56]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events/
