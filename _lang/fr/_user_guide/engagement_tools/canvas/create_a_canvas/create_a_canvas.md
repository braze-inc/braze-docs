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

> Cet article de référence aborde les étapes nécessaires à la création, à la gestion et aux essais d’un Canvas. Suivez ce guide ou consultez notre [Cours d’apprentissage Braze Canvas](https://learning.braze.com/quick-overview-canvas-setup) !

{% alert important %}
À compter du 28 février 2023, vous ne pourrez plus créer ou dupliquer de Canvas à l’aide de l’expérience Canvas originale. Braze recommande aux clients qui utilisent l’expérience Canvas originale de passer à Canvas Flow. Il s’agit d’une expérience d’édition améliorée permettant de mieux créer et gérer les Canvas. En savoir plus sur le [clonage de vos Canvas en Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

## Étape 1 : Créer un Canvas 

Accédez à la page **Canvas**, située sous la section **Engagement**, puis cliquez sur **Create Canvas (Créer un Canvas)**. Choisissez ensuite votre expérience Canvas :
- **Canvas Flow :** Tirez parti des composants Canvas allégés pour une expérience d’édition plus simple et plus efficace
- **Flux de travail d’origine :** Créez des parcours utilisateurs avec des composants Canvas habituels

![][3]{: style="max-width:70%;"}

{% alert note %}
Choisir votre expérience Canvas est impossible pour les nouveaux utilisateurs Braze. À la place, vous créerez des Canvas en utilisant uniquement les flux de travail et l’expérience Canvas Flow.
{% endalert %}

## Étape 2 : Utiliser l’assistant d’entrée pour configurer votre Canvas

L’assistant d’entrée vous guidera tout au long de la configuration de votre Canvas, de la désignation à la définition d’événements de conversion et du transfert des utilisateurs appropriés à votre parcours client. Cliquez sur chacun des onglets suivants pour voir les paramètres que vous pouvez ajuster dans chacune des étapes d’assistant d’entrée.

{% tabs local %}
  {% tab Basics %}
    À ce niveau, vous configurerez les bases de votre Canvas.
    - Nommez votre Canvas
    - Ajoutez des équipes
    - Ajoutez des balises
    - Affectez des événements de conversion et sélectionnez leurs types d’événements et les dates limites

    En savoir plus sur les [Bases](#step-2a-set-up-your-canvas-basics).
  {% endtab %}
  {% tab Entry Schedule %}
    À ce niveau, vous déciderez de la façon dont vos utilisateurs accéderont à votre Canvas.
    - Planification : Il s’agit d’une entrée Canvas basée sur le temps
    - En fonction de l’action : Votre utilisateur accédera à votre Canvas après l’exécution d’une action définie
    - Déclenchée par API Utilisez une demande API pour que des utilisateurs puissent accéder à votre Canvas

    En savoir plus sur l’étape [Planification d’entrée](#step-2b-set-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Entry Audience %}
    À ce niveau, vous sélectionnerez votre Audience d’entrée Canvas :
    - Créez votre audience en ajoutant des segments et des filtres
    - Affinez les retours et les limites d’entrée du Canvas
    - Consultez une synthèse de votre audience cible

    En savoir plus sur l’étape [Audience d’entrée](#step-2c-set-your-target-entry-audience).
  {% endtab %}
  {% tab Send Settings %}
    À ce niveau, vous sélectionnerez vos paramètres d’envoi de Canvas :
    - Sélectionnez vos paramètres d’inscription
    - Définissez une limitation du débit d’envoi pour vos messages Canvas
    - Activez et définissez des heures calmes

    En savoir plus sur l’étape [Paramètres d’envoi](#step-2d-select-your-send-settings)
  {% endtab %}
  {% tab Build Canvas %}
    À ce niveau, vous allez créer votre Canvas.

    Découvrez comment [créer votre Canvas](#step-3-build-your-canvas) à l’aide de l’éditeur de Canvas.
  {% endtab %}
{% endtabs %}

### Étape 2a : Configurer les bases de votre Canvas :

À ce niveau, vous allez désigner votre Canvas, affecter [Teams]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams) et créer ou ajouter des [balises]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags). Vous allez également affecter des événements de conversion pour le Canvas.

{% alert tip %}
Balisez vos Canvas pour qu’ils soient faciles à trouver et créez des rapports. Par exemple, lorsque vous utilisez [Créateur de rapports]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/), vous pouvez filtrer les éléments par balises spécifiques
{% endalert %}

![][51]

#### Sélectionner des événements de conversion

Sélectionnez votre type d’événement de conversion puis sélectionnez les conversions que vous souhaiteriez enregistrer. Nous utiliserons l’[événement de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/) que vous définissez dans cet écran pour mesurer l’efficacité de votre Canvas. 

![Un événement de conversion primaire A avec le type d’événement de conversion Effectue un achat pour enregistrer les conversations pour les utilisateurs qui effectuent n’importe quel achat avant une date butoir de conversion de trois jours.][52]{: style="max-width:75%;"}

Si votre Canvas a plusieurs variantes ou un groupe de contrôle, Braze utilisera cet événement de conversion pour déterminer la meilleure variation pour atteindre cet objectif de conversion. À l’aide de la même logique, vous pouvez créer plusieurs événements de conversion.

### Étape 2b : Définir votre planification d’entrée Canvas

Vous pouvez sélectionner l’un des trois modes d’accès à votre Canvas par les utilisateurs.

#### Types de planification d’entrée

{% tabs local %}
  {% tab Scheduled Delivery %}
    Avec une livraison planifiée, les utilisateurs accéderont à un calendrier, de la même façon que vous planifieriez une campagne. Vous pouvez inscrire des utilisateurs à un Canvas dès qu’il est lancé ou les intégrer à votre parcours à un moment donné ou de façon récurrente.

    ![Livraison Canvas planifiée]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab Action-Based Delivery %}
    Avec cette livraison par événement, vous pouvez choisir d’intégrer des utilisateurs à un Canvas lorsqu’ils actionnent certains déclencheurs. Les utilisateurs accéderont à votre Canvas et commenceront à recevoir des messages lors d’activités particulières, comme ouvrir votre application, effectuer un achat ou déclencher un événement personnalisé. <br><br>Notez que cette livraison par événement n’est pas disponible pour des composants Canvas avec des messages in-app.

    ![Livraison par événement Canvas]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

    Vous pouvez contrôler d’autres aspects de votre comportement de Canvas dans la fenêtre **Audience d’entrée**, incluant des règles de rééligibilité et des paramètres de limite de fréquence.
  {% endtab %}
  {% tab API-Triggered Delivery %}
    Avec la livraison déclenchée par API, vous pouvez décider d’intégrer des utilisateurs à un Canvas via une demande API. Sur le tableau de bord, vous trouverez un exemple de demande cURL à l’origine de cette action qui affecte [`canvas_entry_properties`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) facultatif à l’aide de [`l’objet de propriétés de l’entrée Canvas`]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). <br><br>Les utilisateurs accéderont à votre Canvas et commenceront à recevoir des messages une fois qu’ils auront été ajoutés à l’aide de l’endpoint [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) via l’API.

    ![Livraison déclenchée par API Canvas]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    Endpoints de livraison déclenchés par API :
    - [POST : Envoyer des messages Canvas via la livraison déclenchée par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST : Planifier des Canvas déclenchés par API]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST : Mettre à jour des Canvas planifiés déclenchés par API]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

<!--Tag allows alert to be linked to-->
<a id="important-edge-case"></a>

{% alert important %}
Si la fenêtre de rééligibilité est inférieure à la durée maximale du Canvas, un utilisateur sera autorisé à accéder à nouveau au Canvas et à recevoir plusieurs messages de composants. Dans le cas limite où un utilisateur accède à nouveau au même composant que l’accès précédent, Braze dédupliquera ces messages de composant. <br><br>Si un utilisateur accède à nouveau au Canvas, atteint le même composant qu’à l’accès précédent, est éligible à un message In-App pour chaque entrée, il recevra le message deux fois (en fonction de la priorité de message In-App) à condition qu’il rouvre une session deux fois.
{% endalert %}

Une fois que vous avez sélectionné la méthode de livraison, ajustez ces paramètres en conséquence et passez à la configuration de votre audience cible.

### Étape 2c : Définir votre audience d’entrée cible :

Vous pouvez définir l’audience cible pour votre Canvas à l’étape **Audience d’entrée**. Seuls les utilisateurs répondant aux critères définis peuvent accéder au parcours.

Par exemple, si vous souhaitez cibler de nouveaux utilisateurs, vous pouvez limiter un parcours spécifique aux utilisateurs ayant accédé à votre application en premier, il y a moins de 3 semaines. Vous pouvez également contrôler des paramètres, par exemple si des messages doivent être envoyés aux utilisateurs inscrits pour recevoir des notifications.

{% alert warning %}
Éviter de configurer une campagne basée sur une action ou un Canvas avec le même déclencheur que le filtre d’audience (c’est-à-dire un attribut modifié ou un événement personnalisé effectué). Une condition de concurrence peut se produire lorsque l’utilisateur ne figure pas dans l’audience au moment de l’événement déclencheur, ce qui signifie qu’il ne recevra pas la campagne ou ne pourra pas accéder au Canvas.  
{% endalert %}

### Étape 2d : Sélectionner vos paramètres d’envoi

Cliquez sur **Send Settings (Paramètres d’envoi)** pour sélectionner vos paramètres d’inscription, activer la limitation du débit et les heures calmes. 

En activant [Limitation du taux][6b] ou [Limite de fréquence][6c], vous pouvez alléger la pression marketing subie par vos utilisateurs et vérifier qu’ils ne sont pas surchargés de messages. Pour gérer vos règles de limite de fréquence, rendez-vous sur votre page **Global Message Settings (Paramètres généraux des messages)** dans votre compte Braze.

Pour le ciblage d’e-mail et les canaux de notification push de Canvas, vous pouvez limiter votre Canvas de sorte que seuls les utilisateurs explicitement inscrits reçoivent le message (utilisateurs inscrits ou non-inscrits exclus). Par exemple, supposons que vous ayez trois utilisateurs avec un statut d’abonnement différent :

- **L’utilisateur A** est abonné aux e-mails et la notification push est activée. Cet utilisateur ne reçoit pas les e-mails, mais il recevra les notifications push.
- L’**utilisateur B** a consenti explicitement aux e-mails, mais la notification push n’est pas activée. Cet utilisateur recevra les e-mails, mais pas les notifications push.
- L’**utilisateur C** a consenti explicitement aux e-mails et la notification push est activée. Cet utilisateur recevra les e-mails et les notifications push.

Pour ce faire, définissez les **Paramètres d’inscription** pour envoyer ce Canvas « uniquement aux utilisateurs abonnés ». Cette option garantira que seuls les utilisateurs abonnés recevront vos e-mails et Braze enverra uniquement vos notifications push aux utilisateurs pour lesquels la notification push est activée par défaut. 

Ces paramètres d’abonnement sont appliqués par étapes, ce qui signifie qu’ils n’ont pas d’effet sur votre audience d’entrée. Ce paramètre est donc utilisé pour évaluer l’éligibilité d’un utilisateur à recevoir chaque étape Canvas.

{% alert important %}
Avec cette configuration, n’incluez pas de filtres dans l’étape **Utilisateurs cible** qui limitent l’audience à un seul canal (par ex. `Notifications push activées = True` or `Inscription aux e-mails = Abonné`).
{% endalert %}

Si vous le souhaitez, indiquez Heures calmes (période pendant laquelle vos messages ne seront pas envoyés) pour votre Canvas. Cochez **Activer heures calmes** dans vos **Paramètres d’envoi**. Puis sélectionnez vos Heures calmes dans l’heure locale de vos utilisateurs et l’action qui suivra si le message se déclenche pendant ces heures calmes.

![][50]

## Étape 3 : Créer votre Canvas

### Ajouter une variante

![][11]{: style="float:right;max-width:35%;margin-left:15px;"}

Cliquez sur **Add Variant (Ajouter une variante)** et sélectionnez l’option pour ajouter une nouvelle variante à votre Canvas. Les variantes représentent un parcours effectué par vos utilisateurs et peuvent contenir plusieurs étapes et branches.

Vous pouvez ajouter des variantes supplémentaires en cliquant sur le bouton <i class="fas fa-plus-circle"></i> Plus. Lorsque vous ajoutez de nouvelles variantes, vous pourrez ajuster la façon dont elles seront réparties parmi vos utilisateurs de sorte que vous puissiez comparer et analyser l’efficacité des différentes stratégies d’engagement.

![][12]

{% alert tip %}
Par défaut, l’affectation de Canvas Variant est bloquée lorsque des utilisateurs accèdent à Canvas, ce qui signifie que si un utilisateur saisit d’abord une variante, cette dernière reste définie à chaque accès au Canvas. Cependant il existe des façons d’éviter ce comportement. <br><br>Pour ce faire, vous pouvez créer un générateur de nombres aléatoires à l’aide de Liquid, l’exécuter chaque fois qu’un utilisateur accède à Canvas, archiver la valeur comme attribut personnalisé puis utiliser cet attribut pour diviser les utilisateurs de manière aléatoire.

{% details Développer pour les étapes %}

1. Créez un attribut personnalisé pour archiver votre nombre aléatoire. Nommez-la de manière à pouvoir la localiser facilement, comme « lottery_number » ou « random_assignment ». Vous pouvez créer l’attribut [dans votre tableau de bord]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/custom_event_and_attribute_management/) ou via des appels API sur votre Endpoint [Suivi de l’utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)<br><br>
2. Créez une campagne webhook au début de votre Canvas. Cette campagne servira de support pour créer votre nombre aléatoire et l’archiver comme attribut personnalisé. Reportez-vous à [Création d’un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook) pour en savoir plus. Saisissez l’URL pour votre Endpoint Suivi utilisateur.<br><br>
3. Créez le générateur de nombres aléatoires. Vous pouvez le faire à l’aide du code [indiqué ici](https://www.131-studio.com/blogs/shopify-conversion/generate-random-numbers-using-liquid-shopify), qui se sert de l’accès unique de chaque utilisateur pour créer un nombre aléatoire. Définissez le nombre qui en résulte comme variante Liquid dans votre campagne webhook.<br><br>
4. Formatez l’appel `users/track` dans votre campagne webhook de sorte qu’il définisse l’attribut personnalisé que vous avez créé à l’étape 1 pour le nombre aléatoire que vous avez généré sur votre profil utilisateur actuel. L’exécution de cette étape vous permettra de créer correctement un nombre aléatoire qui change chaque fois que votre utilisateur accède à votre campagne.<br><br>
5. Ajustez les branches de votre Canvas de sorte qu’elles soient divisées en fonction des règles d’audience plutôt qu’en variantes sélectionnées de manière aléatoire. Dans les règles d’audience de chaque branche, définissez le filtre d’audience en fonction de votre attribut personnalisé. <br><br>Par exemple, une branche peut avoir « lottery_number est inférieur à 3 » comme filtre d’audience, alors qu’une autre branche peut avoir « lottery_number est supérieur à 3 et inférieur à 6 » comme filtre d’audience.

{% enddetails %}
{% endalert %}

### Ajouter des étapes

{% tabs local %}
{% tab Canvas Flow %}

Vous pouvez ajouter plus d’étapes dans votre flux de travail Canvas en glissant et déposant des composants depuis la barre latérale **Composants**. Sinon, lorsque vous cliquez sur le bouton plus <i class="fas fa-plus-circle"></i>, vous pouvez également ajouter un composant à l’aide du menu qui s’affiche au-dessus.

![]({% image_buster /assets/img_archive/add_components_flow.png %})

{% alert tip %}
Au fur et à mesure que vous ajouterez d’autres étapes, vous pourrez visualiser votre Canvas tout entier un utilisant soir la **Vue détaillée**, soit la **Vue simplifiée**. La **Vue simplifiée** affiche uniquement les icônes de composants pour une visualisation de haut niveau de votre parcours utilisateur alors que la **Vue détaillée** affiche les détails étendus. Selon vos préférences, vous pouvez basculer entre ces affichages !
{% endalert %}

{% alert warning %}
Un Canvas créé en utilisant Canvas Flow peut comprendre jusqu’à 200 étapes. Des erreurs de chargement se produiront si votre Canvas a plus de 200 étapes.
{% endalert %}

{% endtab %}

{% tab Original Canvas Editor %}

Ajoutez un composant en cliquant sur le bouton plus <i class="fas fa-plus-circle"></i> sous votre variante. Lorsque vous ajoutez un nouveau composant au flux de travail Canvas d’origine, il sera ajouté automatiquement en temps qu’**étape complète**.

![]({% image_buster /assets/img_archive/Canvas_More_Step.png %})

{% endtab %}
{% endtabs %}

### Modification d’une étape

Vous désirez éditer une étape dans votre parcours utilisateur ? Regardez comment le faire selon votre flux de travail Canvas !

{% tabs local %}
{% tab Canvas Flow %}

Vous pouvez éditer n’importe quelle étape de votre flux de travail Canvas Flow en cliquant n’importe lequel des composants. 

Par exemple, imaginons que vous désirez modifier votre première étape, un composant de [délai]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), dans votre flux de travail pour qu’il s’applique un jour donné. Cliquez sur l’étape pour afficher son paramétrage et ajustez votre délai pour le 1er juillet. Ceci signifie que le 1er juillet, vos utilisateurs passeront à l’étape suivante de votre Canvas.

![]({% image_buster /assets/img_archive/edit_delay_flow.png %})

Vous pouvez également éditer et ajuster rapidement les **paramètres d’action** de votre étape de [parcours d’action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) pour retenir les utilisateurs pour une durée donnée. Leur parcours suivant est donc priorisé selon les actions intervenant durant cette période d’évaluation.

![]({% image_buster /assets/img_archive/action_paths_flow.png %})

Les composants légers de Canvas Flow permettent une expérience d’édition facilitée. Ajuster les détails les plus précis de votre Canvas en est d’autant plus simple. 

{% endtab %}

{% tab Original Canvas Editor %}

Cliquez n’importe où dans une étape complète pour que Braze ouvre l’interface de modification de cette étape complète. Les composants peuvent être configurés pour envoyer des messages après un délai défini (31 jours au maximum) ou lorsqu’un utilisateur exécute une action spécifique. Par exemple, vous pouvez utiliser Canvas pour configurer une campagne d’intégration Jour 1, Jour 3, Jour 7 avec des laps de temps entre les messages :

![]({% image_buster /assets/img_archive/Canvas_One_Day.png %})

Ou vous pouvez définir un groupe de messages à envoyer une fois que vos utilisateurs ont pris une mesure spécifique, avec une fenêtre, un délai et des [événements d’exception]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events/) pouvant être configurés :

![]({% image_buster /assets/img_archive/Canvas_Exception_Events.png %})

Vous pouvez également appliquer des **Filtres** à chaque étape d’un Canvas. Utilisez cette action pour ajouter une logique de flux de contrôle supplémentaire, par exemple, exclure des utilisateurs d’un parcours lorsqu’il est probable qu’ils n’aient plus besoin d’encouragement supplémentaire :

![]({% image_buster /assets/img_archive/Canvas_Additional_Engagement.png %})

{% alert note %} 
Par défaut, les filtres et segments pour des étapes complètes dans Canvas sont cochés à l’heure de l’envoi. Cependant, pour les étapes de [fractionnement des décisions]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/), une évaluation d’audience est effectuée dès réception de l’étape précédente ou après un délai (si vous en avez configuré un). 
{% endalert %}


{% endtab %}
{% endtabs %}

#### Messages dans Canvas

Modifiez des messages dans un composant Canvas pour contrôler les messages envoyés dans une étape spécifique. Canvas peut envoyer des messages par e-mail, téléphone mobile et notification Web et webhooks pour s’intégrer à d’autres systèmes. De la même façon que pour les messages de campagne, vous pouvez utiliser la création d’un modèle Liquid spécifique pour personnaliser vos messages.

{% alert tip %}
Savez-vous que vous pouvez inclure des noms de composants Canvas dans vos messages et vos modèles de lien ?<br>
Utilisez la balise Liquid `campaign.${name}` dans Canvas pour afficher le nom du composant Canvas actuel.
{% endalert %}

{% tabs local %}
{% tab Canvas Flow %}

Le composant de message gère les messages envoyés aux utilisateurs. Vous pouvez sélectionner vos **canaux de communication** et ajuster les **paramètres de livraison** pour optimiser vos envois de messages Canvas. Pour plus de détail concernant ce composant, consultez la section [Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

![]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

{% endtab %}

{% tab Original Canvas Editor %}

Pour l’éditeur Canvas d’origine, les étapes complètes fonctionnent de la même manière que le composant de [message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) utilisé dans votre Canvas Flow. Vous pouvez sélectionner votre canal de communication. Dans cet exemple, nous avons sélectionné une notification push iOS avec un bref message disposant d’une modélisation Liquid pour inciter les utilisateurs à acheter les objets de leur panier.

![]({% image_buster /assets/img_archive/Canvas_Message_Edit.png %})

Sélectionnez ensuite le **comportement d’avancement** de votre choix. En savoir plus sur l’[avance des utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) dans les Canvas Steps.

![Options de comportement d’avancement pour un composant Canvas avec l’option permettant d’avancer les utilisateurs lorsque le message est envoyé ou pour avancer l’audience après un délai d’un jour.]({% image_buster /assets/img_archive/Canvas_Advancement_Behavior.png %})

{% endtab %}
{% endtabs %}

Cliquez sur **Done (Effectué)** une fois que vous avez terminé la configuration de votre composant Canvas.

{% tabs local %}
{% tab Canvas Entry Properties %}

Les `canvas_entry_properties` sont configurées dans l’étape de planification d’entrée de la création du Canvas et indiqueront le déclencheur qui fait entrer l’utilisateur dans le Canvas. Ces propriétés peuvent également accéder aux propriétés des charges utiles d’entrée dans les Canvas déclenchés par API. Notez que l’objet `canvas_entry_properties` a une taille maximale limite de 50 KB. 

Pour les Canvas construits à partir de l’éditeur d’origine, `canvas_entry_properties` ne peut être référencé que dans la première étape complète d’un Canvas.

Pour les envois de messages Canvas Flow, les propriétés d’entrée peuvent être utilisées en Liquid dans n’importe laquelle des étapes de message. Utilisez le Liquid suivant lorsque vous référencez ces propriétés d’entrée : {% raw %} ``canvas_entry_properties${property_name}`` {% endraw %}. Les événements doivent être des événements personnalisés ou d’achat pour être utilisés ainsi.

{% alert note %}
Expressément pour les Canaux de communication in-app, `canvas_entry_properties` ne peut être référencé dans Canvas Flow et dans l’éditeur Canvas d’origine que si vous avez activé les propriétés d’entrées persistantes dans l’éditeur d’origine durant l’accès anticipé précédent.
{% endalert %}

Utilisez le Liquid suivant lorsque vous référencez ces propriétés d’entrée : {% raw %} ``canvas_entry_properties${property_name}`` {% endraw %}. Prenez note du fait que les événements doivent être des événements personnalisés ou d’achat pour être utilisés ainsi.

{% raw %}
Vous pouvez, par exemple, considérer la demande suivante : `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Vous pouvez ajouter le mot « chaussures » à un message avec ce Liquid ``{{canvas_entry_properties.${product_name}}}``.
{% endraw %}

{% endtab %}

{% tab Event Properties %}
Les propriétés de l’événement sont les propriétés que vous avez définies sur des événements personnalisés et des achats. Ces `event_properties` peuvent être utilisées dans les campagnes ayant une livraison par événement ainsi que dans les Canvas. 

Dans Canvas Flow, les événements personnalisés et les propriétés de l’événement d’achat peuvent être utilisés en Liquid dans n’importe quelle étape de message suivant une étape de parcours d’action. Pour le flux de toile, utilisez ce Liquid {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %}  lorsque vous référencez ces `event_properties`. Ces événements doivent être des événements personnalisés ou d’achat pour être utilisés ainsi dans le composant de message.

Pour l’éditeur Canvas d’origine, `event_properties` ne peut pas être utilisé dans les étapes complètes planifiées. Cependant, vous pouvez utiliser `event_properties` dans la première étape complète d’un Canvas par événement, même si l’étape complète est planifiée.

Dans la première étape de message suivant un parcours d’action, vous pouvez utiliser les `event_properties` liées à l’événement référencé dans le parcours d’action. Vous pouvez disposer d’autres étapes (n’étant pas un autre parcours d’action ou une étape de message) entre cette étape de parcours d’action et celle de message. Prenez en compte le fait que vous n’aurez accès aux `event_properties` que si votre étape de message peut être remontée jusqu’à un parcours n’étant pas « Tous les autres » dans l’étape du parcours d’action

{% endtab %}
{% endtabs %}

{% alert important %}

Pour l’éditeur Canvas d’origine et Canvas Flow, vous ne pouvez pas utiliser `event_properties` au cours de l’étape du premier message. Au lieu de cela, vous devez utiliser `canvas_entry_properties` ou ajouter une étape de parcours d’action avec l’événement correspondant **avant** l’étape de message qui comprend `event_properties`. Pour obtenir plus d’informations ainsi que des exemples, consultez notre section [Propriété d’entrées et d’événement Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/).

{% endalert %}


### Modifications de connexions

Pour déplacer une connexion entre des étapes, cliquez sur la flèche reliant les deux composants et sélectionnez un composant différent. Pour rompre la connexion, cliquez sur la flèche et sur **Annuler la connexion** en pied de page de l’éditeur Canvas.

## Étape 4 : Utiliser le test multivarié via Canvas.

Vous pouvez ajouter un groupe de contrôle à votre Canvas en cliquant sur le bouton <i class="fas fa-plus-circle"></i> plus pour ajouter une nouvelle variante. 

Braze effectuera un suivi des conversions pour les utilisateurs figurant dans le groupe de contrôle, même s’ils ne recevront pas de messages. Pour conserver un test précis, nous effectuerons un suivi du numéro de conversions pour vos variantes et le groupe de contrôle pendant exactement le même laps de temps, comme décrit à l’écran de sélection d’événements de conversion. 

Vous pouvez ajuster la répartition entre vos messages en double-cliquant dans les en-têtes **Nom de variante**.

{% tabs local %}
{% tab Canvas Flow %}

Dans cet exemple, notre Canvas est divisé entre deux variantes. La variante 1 est composée de 70 % des utilisateurs. La deuxième variante est dans le groupe de contrôle avec les 30 % d’utilisateurs restants.

![]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

{% endtab %}

{% tab Original Canvas Editor %}

Le flux de travail Canvas dispose de trois variantes avec comme utilisateurs respectifs :
***Variante 1 :** 45 % des utilisateurs
* **Variante 2 :** 45 % des utilisateurs
* **Groupe de contrôle :** Les 10 % d’utilisateurs restants

![]({% image_buster /assets/img_archive/Canvas_Multivariate.png %})

{% endtab %}
{% endtabs %}

### Sélection intelligente pour Canvas

Les fonctionnalités de sélection intelligente sont désormais disponibles dans les Canvas multivariés Comme pour la fonctionnalité [Sélection intelligente][18a] pour des campagnes multivariées, la sélection intelligente pour Canvas analyse la performance de chaque Canvas Variant et ajuste le pourcentage d’utilisateurs à diriger via chaque variante. Cette répartition est basée sur chaque métrique de performance de variante pour augmenter le nombre total de conversions escompté.

N’oubliez pas que les Canvas multivariés vous permettent plutôt de tester que de copier, mais le calendrier et les canaux également. La sélection intelligente vous permet de tester des Canvas de manière plus efficace et de garantir que vos utilisateurs seront dirigés vers le meilleur parcours Canvas.

![][18b]

La sélection intelligente pour Canvas optimise vos résultats Canvas en effectuant des ajustements progressifs en temps réel sur la répartition des utilisateurs triés dans chaque variante. Lorsque l’algorithme statistique détermine un élément pertinent parmi vos variantes, il éliminera les variantes peu performantes et reliera tous les futurs destinataires éligibles du Canvas aux variantes pertinentes. 

En ce sens, la sélection intelligente fonctionne mieux sur des Canvas auxquels de nouveaux utilisateurs accèdent fréquemment.

## Étape 5 : Sauvegarder et lancer vos Canvas

Une fois que vous avez fini de créer votre Canvas, cliquez sur **Launch Canvas (Lancer un Canvas)** pour enregistrer et lancer votre Canvas. Vous pouvez également enregistrer votre Canvas comme ébauche si vous devez y revenir.

Une fois que vous avez lancé votre Canvas, vous pourrez voir les éléments analytiques de votre parcours en accédant à la page **Détails de Canvas**.

![][19]

{% alert tip %}
Vous avez besoin de modifier votre Canvas après son lancement ? Vous le pouvez ! Consultez notre section [Modifier vos Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/) après le lancement pour plus d’informations.
{% endalert %}


[1]:{% image_buster /assets/img_archive/canvas_dropdown.png %}
[3]: {% image_buster /assets/img_archive/choose_canvas_experience.png %}
[6b]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting
[6c]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping
[11]:{% image_buster /assets/img_archive/canvas_add_variant.gif %}
[12]:{% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %}
[13]:{% image_buster /assets/img_archive/Canvas_One_Day.png %}
[14]:{% image_buster /assets/img_archive/Canvas_Exception_Events.png %}
[15]:{% image_buster /assets/img_archive/Canvas_Additional_Engagement.png %}
[17]:{% image_buster /assets/img_archive/Canvas_More_Step.png %}
[18a]: {{site.baseurl}}/user_guide/intelligence/intelligent_selection/
[18b]: {% image_buster /assets/img_archive/canvas_intelligent_selection.png %}
[19]:{% image_buster /assets/img_archive/Canvas_Analytics.png %}
[50]: {% image_buster /assets/img/quiet_hours.png %}
[51]: {% image_buster /assets/img/Basics1.gif %}
[52]: {% image_buster /assets/img/add_canvas_conversions.png %}
[53]: {% image_buster /assets/img/entry-schedule-canvas-1.gif %}
[54]: {% image_buster /assets/img/entry-audience-canvas-1.gif %}
[55]: {% image_buster /assets/img/canvas-send-settings-1.gif %}