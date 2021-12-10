---
nav_title: Créer une toile
article_title: Créer une toile
page_order: 0
page_type: Référence
description: "Cet article de référence couvre les étapes nécessaires à la création, à la maintenance et à l’essai d’un Canvas."
tool: Toile
---

# Créer une toile

Suivez ce guide, ou consultez notre [cours LAB](http://lab.braze.com/quick-overview-canvas-setup)!

## Étape 1 : Créer une nouvelle toile

!\[Canvas\]\[1\]{: style="float:right;max-width:20%;margin-left:10px;margin-top:10px;margin-bottom:10px;"}

Allez à la page **Canvas** , située sous la section **Engagement** , puis cliquez sur __Créer une nouvelle toile__.

## Étape 2 : Utilisez l'assistant d'entrée pour configurer votre Canvas

L'assistant d'entrée vous guidera à travers la configuration de votre Canvas—de la nommer aux événements de conversion en passant par la mise en place des bons utilisateurs dans votre voyage client. Cliquez sur chacun des onglets ci-dessous pour voir quels paramètres vous pouvez ajuster dans chacune des étapes de l'Assistant d'entrée.

{% tabs local %}
  {% tab Basics %}
    Ici, vous allez configurer les bases de votre Canvas : - Nommez votre Canvas - Ajoutez des équipes à votre Canvas - Ajoutez des mots clés à votre Canvas - Assignez des événements de conversion et choisissez leurs types d'événements et échéances

    [En savoir plus sur l'étape de base.](#step-2a-set-up-your-canvas-basics)
  {% endtab %}
  {% tab Entry Schedule %}
    Ici, vous déciderez comment vos utilisateurs entreront dans votre Canvas : - Planifié : Ceci est une entrée de Canvas basée sur le temps - Action-Basé : Votre utilisateur entrera dans votre Canvas après avoir effectué une action définie - API-Déclenché : Utilisez une requête API pour entrer des utilisateurs dans votre Canvas

    [En savoir plus sur l'étape du calendrier d'entrée.](#step-2b-set-your-canvas-entry-schedule)
  {% endtab %}
  {% tab Entry Audience %}
    Ici, vous allez sélectionner votre audience d'entrée sur le canevas : - Créer votre audience en ajoutant des segments et des filtres - affiner la reentrée du canevas et les limites d'entrée - Voir un résumé de votre public cible

    [En savoir plus sur l'étape de l'entrée.](#step-2c-set-your-target-entry-audience)
  {% endtab %}
  {% tab Send Settings %}
    Ici, vous allez sélectionner vos paramètres d'envoi de Canvas : - Sélectionnez vos paramètres d'abonnement - Définissez une limite de taux d'envoi pour vos messages de toile - Activez et réglez les heures silencieuses

    [En savoir plus sur l'étape Envoyer les paramètres.](#step-2d-select-your-send-settings)
  {% endtab %}
  {% tab Build Canvas %}
    Ici, vous construirez votre Canevas.

    [Apprenez comment construire votre Canvas en utilisant le constructeur de Canvas.](#step-3-build-your-canvas)
  {% endtab %}
{% endtabs %}

### Étape 2 : Configurez les bases de votre Canvas

Ici, tu nommeras ton Canvas, assigne des équipes []({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams)et créeras ou ajouteras des [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags). Ici, vous assignerez également des événements de conversion pour les Canvas.

{% alert tip %}
Étiquetez vos toiles pour qu'elles soient faciles à trouver et à construire des rapports. Par exemple, lorsque vous utilisez [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/), vous pouvez filtrer par balises particulières.
{% endalert %}

!\[Basics\]\[51\]

#### Choisir les événements de conversion

Choisissez votre type d'événement de conversion, puis sélectionnez les conversions que vous souhaitez enregistrer.

!\[Conversion\]\[52\]

Nous utiliserons [l'événement de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/) que vous avez défini à partir de cet écran pour mesurer l'efficacité de votre Canvas.

Si votre Canvas a plusieurs variantes ou un groupe de contrôle, Braze utilisera cet événement de conversion pour déterminer la meilleure variation pour atteindre cet objectif de conversion. En utilisant la même logique, vous pouvez créer plusieurs événements de conversion.

### Étape 2b : Définissez le calendrier de saisie de votre Canvas

Vous pouvez choisir l'une des trois façons dont les utilisateurs peuvent entrer dans votre Canvas :

- Livraison programmée
- Livraison par action
- Livraison déclenchée par l'API

Après avoir choisi quels paramètres vous utiliserez, ajustez ces paramètres de manière appropriée et passez à la configuration de votre public cible.

!\[Calendrier des entrées\]\[53\]

#### Types d'horaires d'entrée

{% tabs local %}
  {% tab Scheduled Delivery %}
    __Livraison planifiée__<br> Avec livraison planifiée, les utilisateurs entreront sur un calendrier temporel, de même que la façon dont vous planifiez une campagne. Vous pouvez inscrire des utilisateurs sur un Canvas dès son lancement, ou de les entrer dans votre voyage à un moment donné dans le futur, ou sur une base récurrente.

    ![Canvas Planning Delivery]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab Action-Based Delivery %}
    __Livraisons à l'aide d'Action-Based Delivery__<br> Avec une livraison basée sur l'action, vous pouvez choisir d'entrer des utilisateurs dans un Canvas quand ils exécutent certains déclencheurs. Les utilisateurs entreront dans votre Canvas et commenceront à recevoir des messages lorsqu'ils prendront des mesures particulières, comme ouvrir votre application, faire un achat ou déclencher un événement personnalisé. <br><br>Notez que la distribution par action n'est pas disponible pour les étapes de Canvas avec les messages dans l'application.

    ![Canvas Action-Based Delivery]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery. ng %})
    
    Vous pouvez contrôler d'autres aspects du comportement de votre Canvas à partir de la fenêtre **Public d'entrée**, y compris des règles pour la rééligibilité et les paramètres de plafonnement des fréquences.
  {% endtab %}
  {% tab API-Triggered Delivery %}
    __Livraisons déclenchées par l'API__<br> Vous pouvez choisir d'entrer des utilisateurs dans un Canvas via une requête API. Dans le tableau de bord, vous pouvez trouver un exemple de requête cURL qui fait cela ainsi que d'affecter des propriétés facultatives [`canvas_entry_properties`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) en utilisant le [`Canvas Entry Properties Object`]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). <br><br>Les utilisateurs entreront dans votre Canvas et commenceront à recevoir des messages une fois qu'ils auront été ajoutés en utilisant le [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) endpoint via l'API.

    ![Canvas API-Triggered Delivery]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery. ng %})
    
    API Triggered Delivery Endpoints:
    - [POST: Send Canvas Messages via API-Triggered Delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: Schedule API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: Update Scheduled API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

<!--Tag allows alert to be linked to-->
<a id="important-edge-case"></a>

{% alert important %}
Si la fenêtre de rééligibilité est inférieure à la durée maximale du Canvas, un utilisateur sera autorisé à ré-entrer et à recevoir plus d'une étape de message. Dans le cas où la réentrée d'un utilisateur atteint la même étape que son entrée précédente, Braze dédoublera les messages de cette étape. <br><br>Dans le cas où un utilisateur réentre dans le Canvas, atteint la même étape que leur entrée précédente, et est éligible pour un message dans l'application pour chaque entrée, l'utilisateur obtiendra le message deux fois (selon la priorité du message dans l'application) tant qu'il réouvrira une session deux fois.
{% endalert %}

### Étape 2c: Définissez votre audience d'entrée cible

Vous pouvez définir le public cible de votre Canvas à l'étape **Entrée Public**. Seuls les utilisateurs qui correspondent à vos critères définis peuvent entrer le trajet.

!\[Public cible Canvas\]\[54\]

Par exemple, si vous voulez cibler de nouveaux utilisateurs, vous pouvez limiter un voyage particulier aux utilisateurs qui ont utilisé votre application pour la première fois il y a moins de 3 semaines. Vous pouvez également contrôler les paramètres tels que si les messages doivent être envoyés aux utilisateurs qui sont abonnés ou qui ont opté pour vos notifications.

{% alert warning %}
Évitez de configurer une campagne basée sur l'action ou Canvas avec le même déclencheur que le filtre d'audience (c'est-à-dire un attribut modifié ou effectué un événement personnalisé). Une condition de course peut se produire dans laquelle l'utilisateur n'est pas dans le public au moment où il effectue l'événement de déclenchement ce qui signifie qu'ils ne recevront pas la campagne ou n'entreront pas dans le Canvas.
{% endalert %}

### Étape 2: Sélectionnez vos paramètres d'envoi

Cliquez sur **Envoyer les paramètres** pour sélectionner vos paramètres d'abonnement, activer la limitation du taux et pour activer les heures silencieuses.

!\[Paramètres d'envoi\]\[55\]

En activant [la limitation de débit][6b] ou [le plafonnement de fréquence][6c], vous pouvez alléger la pression de marketing exercée sur vos utilisateurs et vous assurer que vous n'avez pas fini de les envoyer.

{% alert note %}
Visitez votre page de [Paramètres globaux de messages](https://dashboard-01.braze.com/engagement/global_message_settings/) dans votre compte Braze pour gérer vos règles de plafonnement des fréquences.
{% endalert %}

Pour les Canvases ciblant les canaux de messagerie et de push, vous pouvez vouloir limiter votre Canvas de sorte que seuls les utilisateurs qui sont explicitement inscrits recevront le message (excluant les utilisateurs abonnés ou désabonnés). Par exemple, dites que vous avez trois utilisateurs de différents statuts d'opt-in :

- **L'utilisateur A** est abonné à l'e-mail et est push activé. Cet utilisateur ne reçoit pas l'email mais recevra le push.
- **L'utilisateur B** est opté pour l'email mais n'est pas poussé activé. Cet utilisateur recevra l'email mais ne recevra pas le push.
- **L'utilisateur C** est opté pour l'email et est push activé. Cet utilisateur recevra à la fois l'email et le push.

Pour ce faire, définissez les **paramètres d'abonnement** pour envoyer ce Canvas à "utilisateurs optés seulement". Cette option vous assurera que seuls les utilisateurs optés recevront votre courriel. et Braze enverra uniquement votre push aux utilisateurs qui sont activés par défaut.

{% alert important %}
Avec cette configuration, n'incluez aucun filtre dans l'étape **Utilisateurs cibles** qui limitent l'audience à un seul canal (e. ., `Push Activé = True` ou `Abonnement par courriel = Opted-In`).
{% endalert %}

Si vous le désirez, indiquez les heures silencieuses (l'heure pendant laquelle vos messages ne seront pas envoyés) pour votre Canvas. Cochez **Activer les heures silencieuses** dans vos __paramètres d'envoi__. Ensuite, sélectionnez vos heures silencieuses dans l'heure locale de votre utilisateur et quelle action suivra si le message se déclenche à l'intérieur de ces heures silencieuses.

!\[Heures silencieures\]\[50\]

## Étape 3: Construisez votre Canevas

### Ajout d'une variante

!\[Canvas Add Variant\]\[11\]{: style="float:right;max-width:40%;margin-left:15px;"}

Cliquez sur **Ajouter une variante** et sélectionnez l'option pour ajouter une nouvelle variante à votre Canvas. Les variantes représentent un voyage que vos utilisateurs prendront, et peuvent contenir plusieurs étapes et branches.

Vous pouvez ajouter des variantes supplémentaires en appuyant sur le bouton <i class="fas fa-plus-circle"></i> plus . Lorsque vous ajoutez de nouvelles variantes, vous serez en mesure d'ajuster la façon dont vos utilisateurs seront répartis entre eux afin que vous puissiez comparer et analyser l'efficacité des différentes stratégies d'engagement.

!\[Variantes multiples de Canvas \]\[12\]

{% alert tip %}
Par défaut, l'affectation des variantes de Canvas est verrouillée lorsque les utilisateurs entrent dans le Canvas, ce qui signifie que si un utilisateur entre pour la première fois dans une variante, ce sera sa variante à chaque fois qu'il entrera à nouveau dans le Canvas. Cependant, il y a des moyens de contourner ce comportement. <br><br>Pour ce faire, vous pouvez créer un générateur de nombres aléatoires en utilisant Liquid, exécutez-le au début de l'entrée Canvas de chaque utilisateur, stocker la valeur comme un attribut personnalisé, puis utiliser cet attribut pour diviser aléatoirement les utilisateurs.

{% details Expand for steps %}

1. Créez un attribut personnalisé pour stocker votre nombre aléatoire. Nommez-le quelque chose de facile à localiser, comme "lottery_number" ou "random_assignment". Vous pouvez créer l'attribut soit [dans votre tableau de bord]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/custom_event_and_attribute_management/), soit via les appels API vers notre point de terminaison [User Track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).<br><br>
2. Créez une campagne de webhook au début de votre Canvas. Cette campagne sera le média dans lequel vous créerez votre nombre aléatoire, et la conserverez comme un attribut personnalisé. Reportez-vous à [Créer un Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook) pour en savoir plus. Définissez l'URL à notre point de terminaison de suivi utilisateur.<br><br>
3. Créer le générateur de nombres aléatoires. Vous pouvez le faire avec le code [décrit ici](https://www.131-studio.com/blogs/shopify-conversion/generate-random-numbers-using-liquid-shopify), qui tire parti de l'heure d'entrée unique de chaque utilisateur pour créer un nombre aléatoire. Définissez le numéro résultant comme une variable Liquid dans votre campagne de webhook.<br><br>
4. Formatez l'appel `utilisateurs/piste` dans votre campagne de webhook afin qu'il définisse l'attribut personnalisé que vous avez créé à l'étape 1 sur le nombre aléatoire que vous avez généré sur le profil de l'utilisateur actuel. Lorsque cette étape s'exécute, vous aurez fait un nombre aléatoire qui change chaque fois qu'un utilisateur entre dans votre campagne.<br><br>
5. Ajustez les branches de votre Canevas pour qu'au lieu d'être divisés par des variantes choisies au hasard, elles soient divisées selon les règles du public. Dans les règles d'audience de chaque branche, définissez le filtre d'audience selon votre attribut personnalisé. <br><br>Par exemple, une branche peut avoir "lottery_number est inférieur à 3" en tant que filtre d'audience, alors qu'une autre branche peut avoir "lottery_number est plus de 3 et moins de 6" comme filtre d'audience.

{% enddetails %}
{% endalert %}

### Modification d'une étape

Cliquez n'importe où sur une étape, et Braze ouvrira l'interface d'édition des étapes. Les étapes peuvent être configurées pour envoyer des messages après un délai fixe (maximum de 31 jours) ou lorsqu'un utilisateur effectue une action particulière. Par exemple, vous pouvez utiliser Canvas pour configurer une campagne d'intégration de Day 1, Day 3, Day 7 avec des délais entre les messages :

!\[Canvas One Day\]\[13\]

Ou vous pouvez définir un groupe de messages à envoyer après que vos utilisateurs aient fait une action particulière, avec une fenêtre configurable, un délai et des [événements d'exception][56]:

!\[Canvas Exception Events\]\[14\]

Vous pouvez également appliquer **Filtres** à chaque étape d'un canevas. Utilisez ceci pour ajouter une logique de flux de contrôle supplémentaire, comme retirer les utilisateurs d'un voyage lorsqu'ils n'ont pas besoin d'encouragement d'engagement supplémentaire :

!\[Canvas Engagement\]\[15\]

{% alert note %}
Par défaut, les filtres et les segments pour les **étapes complètes** dans Canvas sont vérifiés au moment de l'envoi. Cependant, pour [pas de séparation de décision]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/), l'évaluation du public se produit juste après avoir reçu l'étape précédente, ou après un délai (si vous en avez configuré une).
{% endalert %}

#### Messages dans Canvas

Éditez les messages dans une Étape de Canvas pour contrôler les messages qu'une étape particulière enverra. Canvas peut envoyer des messages Email, Mobile & Web Push et Webhooks pour les intégrer à d'autres systèmes.

Similaire aux messages de campagne, vous pouvez utiliser certains modèles de Liquid. Reportez-vous aux onglets ci-dessous pour connaître les limitations.

!\[Canvas Message Edit\]\[16\]

Sélectionnez votre **comportement d'avancement** désiré. En savoir plus sur [l'avancement de vos utilisateurs à travers les étapes de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).

!\[Comportement de l'avancement de Canvas\]\[20\]

Cliquez sur **Terminé** une fois que vous avez terminé la configuration de votre étape.

{% tabs local %}
{% tab Canvas Entry Properties %}
Les propriétés d'entrée de Canvas sont les propriétés que vous avez définies lorsque vous déclenchez ou planifiez un Canvas via l'API.
{% raw %}
- Par exemple, une requête avec `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79. 9}` pourrait ajouter le mot \"chaussures\" à un message en ajoutant le liquide `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

__Les Propriétés de l'entrée du canevas peuvent être référencées dans la première étape d'une toile - or seulement le premier pas__!

Pour plus d'informations sur l'objet Propriétés de l'entrée de Canvas , consultez notre [documentation]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/).
{% endtab %}

{% tab Custom Event Properties %}
Les propriétés d'événements personnalisés sont les propriétés que vous avez définies sur des événements et des achats personnalisés, utilisés principalement dans des campagnes de livraison basées sur des actions. Ces propriétés sont éphémères et ne peuvent être utilisées qu'au moment où elles se produisent. <br><br>Les propriétés événement ne persistent pas, donc si vous planifiez une étape de Canvas plutôt que d'utiliser une distribution basée sur des actions, vous ne seriez pas en mesure d’utiliser une propriété événementielle (comme nous ne stockons pas ces données). Vous ne pouvez pas référencer la propriété événement pour un événement qui s'est déjà produit.

__Les propriétés d'événements personnalisés peuvent être référencées dans la première étape d'une toile - or seulement la première étape__!

Pour plus d'informations sur les propriétés d'événement personnalisées, consultez notre [documentation]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties).

{% endtab %}
{% endtabs %}

{% alert tip %}
Saviez-vous que vous pouvez inclure les noms des étapes de Canvas dans vos messages et modèles de liens ?<br> Utilisez la campagne `.${name}` Balise Liquid dans Canvas pour afficher le nom de l'étape actuelle de Canvas .
{% endalert %}

### Ajout de nouvelles étapes

Ajouter plus d'étapes en appuyant sur le bouton <i class="fas fa-plus-circle"></i> plus :

!\[Canvas More Step\]\[17\]{: style="max-width:75%;"}

### Modification des connexions

Pour déplacer une connexion entre les étapes, cliquez sur la flèche qui relie les deux étapes, et sélectionnez une étape différente. Pour rompre la connexion, cliquez sur la flèche et cliquez sur **Annuler la connexion** dans le pied de page du compositeur de Canvas .

!\[Move or break a connection between two Canvas steps\]\[2\]

## Étape 4 : Utilisez des tests multivariés avec Canvas

Vous pouvez ajouter un groupe de contrôle à votre toile en cliquant sur le bouton <i class="fas fa-plus-circle"></i> plus pour ajouter une nouvelle variante.

Braze suivra les conversions pour les utilisateurs qui sont placés dans le groupe de contrôle, bien qu'ils ne recevront aucun message. Pour préserver un test précis, nous suivrons le nombre de conversions pour vos variantes et le groupe de contrôle pour exactement le même temps comme indiqué sur l'écran de sélection de l'événement de conversion.

Vous pouvez ajuster la distribution entre vos messages en double-cliquant sur les entêtes de **Variant Name**.

!\[Canvas Multivariate\]\[18\]

### Sélection intelligente pour la toile

Des fonctions de sélection intelligente sont maintenant disponibles dans les vasques multivariés. Similaire à la fonctionnalité [de sélection intelligente][18a] pour les campagnes multivariées, La Sélection Intelligente pour Canvas analyse la performance de chaque variante de Canvas et ajuste le pourcentage d'utilisateurs qui sont mis en œuvre par chaque variante. Cette distribution est basée sur les paramètres de performance de chaque variante pour maximiser le nombre total prévu de conversions.

Gardez à l'esprit que les Canvases multivariées vous permettent de tester plus que la copie, mais aussi le timing et les canaux. Grâce à Intelligent Selection, vous pouvez tester vos Canvases plus efficacement et vous assurer que vos utilisateurs seront envoyés dans le meilleur voyage possible sur Canvas .

!\[Intelligent Selection\]\[18b\]

La sélection intelligente de Canvas optimise les résultats de votre Canvas en effectuant des ajustements en temps réel progressifs à la distribution des utilisateurs triés dans chaque variante. Lorsque l'algorithme statistique détermine un gagnant décisif parmi vos variantes, il exclut les variantes sous-performantes et place tous les futurs bénéficiaires admissibles du Canvas dans les variantes gagnantes.

Pour cette raison, Intelligent Selection fonctionne mieux sur les Canevas qui ont de nouveaux utilisateurs qui entrent fréquemment.

## Étape 5 : Sauvegardez et lancez votre Canvas

Une fois que vous avez terminé, appuyez sur **Lancez Canvas** en bas à droite pour enregistrer et lancer votre Canvas. Vous pouvez également enregistrer votre Canevas comme brouillon si vous avez besoin d'y revenir.

Une fois que vous aurez lancé votre Canvas, vous serez en mesure de voir les analyses de votre voyage au fur et à mesure qu'elles arrivent sur la page **Détails sur Canvas**:

!\[Analyses de Canvas\]\[19\]
\[1]:{% image_buster /assets/img_archive/canvas_dropdown.png %} [2]: {% image_buster /assets/img_archive/canvas_connection_edit.gif %} [11]:{% image_buster /assets/img_archive/canvas_add_variant. if %} [12]:{% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %} [13]:{% image_buster /assets/img_archive/Canvas_One_Day. ng %} [14]:{% image_buster /assets/img_archive/Canvas_Exception_Events.png %} [15]:{% image_buster /assets/img_archive/Canvas_Additional_Engagement. ng %} [16]:{% image_buster /assets/img_archive/Canvas_Message_Edit.png %} [17]:{% image_buster /assets/img_archive/Canvas_More_Step. ng %} [18]:{% image_buster /assets/img_archive/Canvas_Multivariate.png %} [18b]: {% image_buster /assets/img_archive/canvas_intelligent_selection. ng %} [19\]\[19\] :{% image_buster /assets/img_archive/Canvas_Analytics.png %} \[20\]\[20\] :{% image_buster /assets/img_archive/Canvas_Advancement_Behavior.png %} [50]: {% image_buster /assets/img/quiet_hours. ng %} [51]: {% image_buster /assets/img/Basics1.gif %} [52]: {% image_buster /assets/img/Conversions-canvas-1.gif %} [53]: {% image_buster /assets/img/entry-schedule-canvas-1. if %} [54]: {% image_buster /assets/img/entry-audience-canvas-1.gif %} [55]: {% image_buster /assets/img/canvas-send-settings-1.gif %}

[6b]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting
[6c]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping
[18a]: {{site.baseurl}}/user_guide/intelligence/intelligent_selection/
[56]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events/
