---
nav_title: Créer un Canvas
article_title: Créer un Canvas
page_order: 0
page_type: reference
description: "Cet article de référence aborde les étapes nécessaires à la création, à la gestion et aux essais d'un Canvas."
tool: Canvas
search_rank: 1
---

# Créer un Canvas

> Cet article de référence aborde les étapes nécessaires à la création, à la gestion et aux essais d'un Canvas. Suivez ce guide, ou consultez notre [cours d'apprentissage Canvas Braze](https://learning.braze.com/quick-overview-canvas-setup).

{% details Développer pour les détails de l'éditeur Canvas original %}
Vous ne pouvez plus créer ou dupliquer des Canvas en utilisant l'expérience Canvas originale. Braze recommande de [cloner vos Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/) vers l'éditeur le plus récent.
{% enddetails %}

## Création d'un Canvas

### Étape 1 : Créer un nouveau Canvas 

Tout d'abord, allez dans **Messagerie** > **Canvas**, puis sélectionnez **Créer un Canvas**.

Le générateur de Canvas vous guidera étape par étape pour configurer votre Canvas, de la nomination à la définition des événements de conversion et à l'intégration des bons utilisateurs dans votre parcours client. Sélectionnez chacun des onglets suivants pour voir quels paramètres vous pouvez ajuster pour chaque étape du générateur.

{% tabs local %}
  {% tab Basics %}
    À ce niveau, vous configurerez les bases de votre Canvas :
    - Donnez un nom à votre Canvas
    - Ajoutez des équipes
    - Ajoutez des tags
    - Affectez des événements de conversion et sélectionnez leurs types d'événements et les dates limites

    Learn more about the [Basics step](#step-2a-set-up-your-canvas-basics).
  {% endtab %}
  {% tab Entry Schedule %}
    Ici, vous déciderez comment et quand vos utilisateurs entreront dans votre Canvas :
    - Planification : Il s'agit d'une entrée Canvas basée sur le temps
    - Basé sur l'action : Votre utilisateur accédera à votre Canvas après l'exécution d'une action définie
    - Déclenché par l'API : Utilisez une requête API pour que des utilisateurs puissent accéder à votre Canvas

    Learn more about the [Entry Schedule step](#step-2b-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Target Audience %}
    À ce niveau, vous sélectionnerez votre audience cible :
    - Créez votre audience en ajoutant des segments et des filtres
    - Ajustez les limites d'entrées et de nouvelles entrées du Canvas
    - Consultez une synthèse de votre audience cible

    Learn more about the [Target Audience step](#step-2c-set-your-target-entry-audience).
  {% endtab %}
  {% tab Send Settings %}
    À ce niveau, vous sélectionnerez vos paramètres d'envoi de Canvas :
    - Sélectionnez vos paramètres d'abonnement
    - Définissez une limite de débit d'envoi pour vos messages Canvas
    - Activez et définissez les heures calmes

    Learn more about the [Send Settings step](#step-2d-select-your-send-settings).
  {% endtab %}
  {% tab Build Canvas %}
    À ce niveau, vous allez créer votre Canvas.

    Learn how to [build your Canvas](#step-3-build-your-canvas) using the Canvas builder.
  {% endtab %}
  {% tab Summary %}
    Ici, vous trouverez la synthèse des détails de votre Canvas. Si vous avez activé le [flux de travail d'approbation Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/), vous pouvez approuver les détails du Canvas répertoriés avant le lancement.

  {% endtab %}
{% endtabs %}

#### Étape 1.1 : Commencez par les bases de votre Canvas

Ici, vous nommerez votre Canvas, assignerez des [Teams]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams) et créerez ou ajouterez des [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags). Vous allez également affecter des événements de conversion pour le Canvas.

{% alert tip %}
Balisez vos Canvas pour qu'ils soient faciles à trouver et pour créer des rapports. Par exemple, lors de l'utilisation du [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), vous pouvez filtrer par des tags particuliers.
{% endalert %}

![La page de détails du Canvas, avec des champs pour le nom du Canvas, la description, l'emplacement et les tags.]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

##### Sélectionner des événements de conversion

Choisissez votre type d'événement de conversion, puis sélectionnez les conversions à enregistrer. Ces [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) mesureront l'efficacité de votre Canvas. 

![Un événement de conversion principal A avec le type d'événement de conversion Effectue un achat pour enregistrer les conversions pour les utilisateurs qui effectuent n'importe quel achat avant une date butoir de conversion de trois jours.]({% image_buster /assets/img/add_canvas_conversions.png %})

Si votre Canvas a plusieurs variantes ou un groupe de contrôle, Braze utilisera cet événement de conversion pour déterminer la meilleure variation pour atteindre cet objectif de conversion. À l'aide de la même logique, vous pouvez créer plusieurs événements de conversion.

#### Étape 1.2 : Déterminez votre planification d'entrée Canvas

Vous pouvez sélectionner l'un des trois modes d'accès à votre Canvas par les utilisateurs. 

##### Types de planification d'entrée

{% tabs local %}
  {% tab Scheduled Delivery %}
    Avec une livraison planifiée, les utilisateurs accéderont selon un calendrier, de la même façon que vous planifieriez une campagne. Vous pouvez inscrire des utilisateurs dans un Canvas dès qu'il est lancé, les intégrer dans votre parcours à un moment donné dans le futur, ou de manière récurrente (quotidienne, hebdomadaire ou mensuelle). 

    Dans cet exemple, en fonction des options basées sur le temps, les utilisateurs entreront dans ce Canvas chaque mardi à 12 h dans leur fuseau horaire local chaque semaine, à partir du 14 novembre 2025 jusqu'au 31 décembre 2025.

    ![La page "Planification d'entrée" avec le type défini sur "Planifié". En raison de la sélection, les options basées sur le temps sont affichées, y compris la fréquence, l'heure de début, la récurrence, les jours, et plus encore.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab Action-Based Delivery %}
    Avec une livraison par événement, les utilisateurs entreront dans le Canvas et commenceront à recevoir des messages lorsqu'ils effectueront des actions particulières, telles que l'ouverture de votre application, l'achat ou le déclenchement d'un événement personnalisé.

    Vous pouvez contrôler d'autres aspects du comportement du Canvas depuis la fenêtre **Audience d'entrée**, y compris les règles de rééligibilité et les paramètres de limite de fréquence. Notez que la livraison par événement n'est pas disponible pour les composants Canvas avec des messages in-app.

    ![Un exemple de livraison par événement. Les utilisateurs entreront dans le Canvas s'ils effectuent un achat avec une fenêtre d'entrée commençant à 13 h 30 le 10 juin 2025.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

  {% endtab %}
  {% tab API-Triggered Delivery %}
    Avec la livraison déclenchée par l'API, les utilisateurs entreront dans votre Canvas et commenceront à recevoir des messages après avoir été ajoutés en utilisant l'[endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) via l'API. Dans le tableau de bord, vous trouverez un exemple de requête cURL à l'origine de cette action, et pourrez attribuer des [`context`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) facultatifs à l'aide de l'[objet context]({{site.baseurl}}/api/objects_filters/context_object/). 

    ![Un exemple de livraison déclenchée par l'API avec un ID Canvas et un exemple de requête cURL.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    Vous pouvez utiliser les endpoints suivants pour la livraison déclenchée par l'API :
    - [POST: Send Canvas Messages via API-Triggered Delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: Schedule API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: Update Scheduled API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

Après avoir sélectionné votre méthode de livraison, ajustez les paramètres pour qu'ils correspondent à votre cas d'utilisation, puis continuez à définir votre audience cible.

{% details Comportement de déduplication pour les Canvas utilisant l'éditeur original %}
Si la fenêtre de rééligibilité est inférieure à la durée maximale du Canvas, un utilisateur sera autorisé à accéder à nouveau au Canvas et à recevoir plusieurs messages de composants. Dans le cas limite où un utilisateur accède à nouveau au même composant que l'accès précédent, Braze dédupliquera ces messages de composant. 

Si un utilisateur revient sur le Canvas, atteint le même composant que lors de son entrée précédente et est éligible pour un message in-app pour chaque entrée, l'utilisateur recevra le message deux fois (en fonction de la priorité du message in-app) tant qu'il rouvre une session deux fois.
{% enddetails %}

#### Étape 1.3 : Définir votre audience d'entrée cible

Seuls les utilisateurs qui correspondent aux critères que vous avez définis peuvent entrer dans le parcours à l'étape **Audience cible**, ce qui signifie que Braze évalue d'abord l'éligibilité de l'audience cible **avant que** les utilisateurs n'entrent dans le parcours Canvas. Par exemple, si vous souhaitez cibler de nouveaux utilisateurs, vous pouvez sélectionner un segment d'utilisateurs qui ont utilisé votre application pour la première fois il y a moins d'une semaine.

Dans les **Contrôles d'entrée**, vous pouvez limiter le nombre d'utilisateurs à chaque fois que le Canvas est planifié pour s'exécuter. Pour les Canvas déclenchés par API et livrés par événement, cette limite se produit à chaque heure UTC. 

{% include alerts/warning_alerts.md alert='Canvas race condition audience trigger' %}

##### Tester votre audience

Après avoir ajouté des segments et des filtres à votre audience cible, vous pouvez tester si votre audience est configurée comme prévu en [recherchant un utilisateur]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) pour confirmer s'il correspond aux critères de l'audience.

![Le champ "Recherche d'utilisateurs", qui vous permet d'effectuer une recherche par ID externe ou par ID Braze.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

##### Sélection des contrôles d'entrée

Les contrôles d'entrée déterminent si les utilisateurs sont autorisés à entrer de nouveau dans un Canvas. Vous pouvez également limiter le nombre de personnes susceptibles d'entrer dans ce Canvas en fonction d'une cadence choisie selon votre type de planification d'entrée :

- **Planifié :** Durée de vie du Canvas ou à chaque fois que le Canvas est planifié
- **Basé sur l'action :** Horaire, quotidien ou durée de vie du Canvas
- **Déclenché par l'API :** Horaire, quotidien ou durée de vie du Canvas

Par exemple, si vous avez un Canvas basé sur l'action et que vous sélectionnez **Limiter le volume d'entrée** et réglez le champ **Entrées maximales** sur 5 000 utilisateurs avec **Quotidien** comme cadence limite, alors le Canvas n'enverra qu'à 5 000 utilisateurs par jour.

![La page "Contrôles d'entrée" affiche des cases à cocher pour "Autoriser les utilisateurs à entrer à nouveau dans le Canvas" et "Limiter le volume d'entrée". Cette dernière vous permet de définir le nombre maximum d'entrées et de choisir une cadence qui dépend du type de planification d'entrée (par exemple, durée de vie du Canvas ou à chaque fois que le Canvas est planifié pour une entrée planifiée, et horaire, quotidien ou durée de vie du Canvas pour une entrée basée sur l'action ou déclenchée par l'API).]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
Braze ne recommande pas de sélectionner **Chaque fois que le Canvas est planifié** pour le réchauffement d'adresses IP, car cela peut entraîner une augmentation des volumes d'envoi.
{% endalert %}

##### Définir les critères de sortie

Définir les [critères de sortie]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) détermine quels utilisateurs vous souhaitez faire sortir d'un Canvas. Si un utilisateur effectue l'événement d'exception ou correspond aux segments et aux filtres, il ne recevra plus aucun message.

##### Calcul de la population cible

Dans la section **Population cible**, vous pouvez consulter un résumé de votre audience, comme les segments sélectionnés et les filtres supplémentaires, ainsi qu'une répartition du nombre d'utilisateurs atteignables par canal de communication. Pour calculer le nombre exact d'utilisateurs joignables dans votre audience cible au lieu de l'estimation par défaut, sélectionnez [Calculer des statistiques exactes]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics).

Remarques :

- Le calcul de statistiques exactes peut prendre quelques minutes. Cette fonction ne calcule les statistiques exactes qu'au niveau du segment, et non au niveau du filtre ou du groupe de filtres.
- Pour les segments de grande taille, il est normal de constater de légères variations, même en calculant des statistiques exactes. La précision de cette fonctionnalité devrait être égale ou supérieure à 99,999 %.

Pour afficher des statistiques supplémentaires, telles que le chiffre d'affaires moyen sur la durée de vie des utilisateurs ciblés, sélectionnez **Afficher les statistiques supplémentaires**.

![Ventilation de la population cible avec possibilité de calculer des statistiques exactes.]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

##### Pourquoi le nombre d'audiences cibles peut-il différer du nombre d'utilisateurs atteignables ?

{% multi_lang_include segments.md section='Differing audience size' %}

#### Étape 1.4 : Sélectionner vos paramètres d'envoi

Sélectionnez **Paramètres d'envoi** pour modifier vos paramètres d'abonnement, activer la limite de débit et activer les heures calmes. En activant la [limite de débit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-canvas-components) ou la [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#frequency-capping), vous pouvez alléger la pression marketing exercée sur vos utilisateurs et vous assurer que vous ne leur envoyez pas trop de messages.

Pour les Canvas ciblant les canaux e-mail et push, vous pouvez limiter votre Canvas de sorte que seuls les utilisateurs explicitement abonnés reçoivent le message (utilisateurs inscrits ou non-inscrits exclus). Par exemple, supposons que vous ayez trois utilisateurs avec un statut d'abonnement différent :

- L'**utilisateur A** est abonné à l'e-mail et les notifications push sont activées. Cet utilisateur ne reçoit pas les e-mails, mais il recevra les notifications push.
- L'**utilisateur B** est abonné à l'e-mail mais n'a pas activé les notifications push. Cet utilisateur recevra les e-mails, mais pas les notifications push.
- L'**utilisateur C** est abonné aux e-mails et les notifications push sont activées. Cet utilisateur recevra les e-mails et les notifications push.

Pour ce faire, définissez les **Paramètres d'abonnement** pour envoyer ce Canvas uniquement aux « utilisateurs ayant choisi de participer ». Cette option garantira que seuls les utilisateurs abonnés recevront vos e-mails et Braze enverra uniquement vos notifications push aux utilisateurs pour lesquels la notification push est activée par défaut. 

Ces paramètres d'abonnement sont appliqués étape par étape, ce qui signifie qu'ils n'ont pas d'effet sur votre audience d'entrée. Ainsi, ce paramètre est utilisé pour évaluer l'éligibilité d'un utilisateur à recevoir chaque étape du Canvas.

{% alert important %}
Avec cette configuration, n'incluez aucun filtre dans l'étape **Audience cible** qui limite l'audience à un seul canal (par exemple, `Foreground Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

Si vous le souhaitez, spécifiez les heures calmes (la période pendant laquelle vos messages ne seront pas envoyés) pour votre Canvas. Cochez **Activer les heures calmes** dans vos **Paramètres d'envoi**. Puis sélectionnez vos heures calmes dans le fuseau horaire local de vos utilisateurs et l'action qui suivra si le message se déclenche pendant ces heures calmes.

![La page "Heures calmes" affiche une case à cocher permettant d'activer les heures calmes. Si elle est activée, l'heure de début, l'heure de fin et le comportement de repli peuvent être définis.]({% image_buster /assets/img/quiet_hours.png %})

### Étape 2 : Créer votre Canvas

{% alert tip %}
Gagnez du temps et rationalisez votre création de Canvas en utilisant les [modèles de Canvas Braze]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/#available-braze-templates) ! Parcourez notre bibliothèque de modèles préconstruits pour trouver celui qui correspond à votre cas d'utilisation et personnalisez-le pour répondre à vos besoins spécifiques.
{% endalert %}

#### Étape 2.1 : Ajouter une variante

![Le bouton "Ajouter une variante" est sélectionné pour afficher un menu contextuel avec l'option "Ajouter une variante".]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

Sélectionnez **Ajouter une variante**, puis ajoutez une nouvelle variante à votre Canvas. Les variantes représentent un parcours que vos utilisateurs emprunteront et peuvent contenir plusieurs étapes et branches.

Vous pouvez ajouter des variantes supplémentaires en sélectionnant le bouton <i class="fas fa-plus-circle"></i> plus. Lorsque vous ajoutez de nouvelles variantes, vous pourrez ajuster la façon dont elles seront réparties parmi vos utilisateurs de sorte que vous puissiez comparer et analyser l'efficacité des différentes stratégies d'engagement.

![Deux exemples de variantes dans un Canvas Braze.]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
Par défaut, l'assignation de variante du Canvas est verrouillée lorsque les utilisateurs entrent dans le Canvas, ce qui signifie que si un utilisateur entre d'abord dans une variante, ce sera sa variante à chaque fois qu'il rentrera dans le Canvas. Cependant, il existe des façons de contourner ce comportement. <br><br>Pour ce faire, vous pouvez créer un générateur de nombres aléatoires à l'aide de Liquid, l'exécuter chaque fois qu'un utilisateur accède au Canvas, stocker la valeur comme attribut personnalisé puis utiliser cet attribut pour diviser les utilisateurs de manière aléatoire.

{% details Développer pour les étapes %}

1. Créez un attribut personnalisé pour stocker votre nombre aléatoire. Donnez-lui un nom facile à repérer, comme « lottery_number » ou « random_assignment ». Vous pouvez créer l'attribut soit [dans votre tableau de bord]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/), soit par le biais d'appels API à notre [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).<br><br>
2. Créez une campagne webhook au début de votre Canvas. Cette campagne sera le moyen par lequel vous créerez votre nombre aléatoire et le stockerez en tant qu'attribut personnalisé. Pour en savoir plus, reportez-vous à la section [Créer un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook). Définissez l'URL sur notre endpoint `/users/track`.<br><br>
3. Créez le générateur de nombres aléatoires. Vous pouvez le faire avec le code [présenté ici](https://community.shopify.com/c/technical-q-a/is-there-any-way-to-generate-random-number-with-liquid-shopify/m-p/1595486), qui tire parti de l'heure d'entrée unique de chaque utilisateur pour créer un nombre aléatoire. Définissez le nombre qui en résulte comme variable Liquid dans votre campagne webhook.<br><br>
4. Formatez l'appel `/users/track` dans votre campagne webhook de sorte qu'il définisse l'attribut personnalisé que vous avez créé à l'étape 1 sur le nombre aléatoire que vous avez généré sur le profil de votre utilisateur actuel. L'exécution de cette étape vous permettra de créer correctement un nombre aléatoire qui change chaque fois que votre utilisateur accède à votre campagne.<br><br>
5. Ajustez les branches de votre Canvas de sorte qu'elles soient divisées en fonction des règles d'audience plutôt qu'en variantes sélectionnées de manière aléatoire. Dans les règles d'audience de chaque branche, définissez le filtre d'audience en fonction de votre attribut personnalisé. <br><br>Par exemple, une branche peut avoir comme filtre d'audience « lottery_number est inférieur à 3 », tandis qu'une autre branche peut avoir comme filtre d'audience « lottery_number est supérieur à 3 et inférieur à 6 ».

{% enddetails %}
{% endalert %}

#### Étape 2.2 : Ajouter des étapes du Canvas

Vous pouvez ajouter plus d'étapes à votre flux de travail Canvas en faisant glisser et déposer des composants depuis la barre latérale des **Composants**. Vous pouvez également sélectionner le bouton <i class="fas fa-plus-circle"></i> plus pour ajouter un composant avec le menu contextuel.

{% alert tip %}
Au fur et à mesure que vous ajoutez des étapes, vous pouvez changer le niveau de zoom pour vous concentrer sur les détails ou pour avoir une vue d'ensemble du parcours utilisateur. Zoomez avec <kbd>Shift</kbd> + <kbd>+</kbd> ou dézoomez avec <kbd>Shift</kbd> + <kbd>-</kbd>.
{% endalert %}

![La fenêtre de recherche de composants ajoutant une étape de délai au Canvas Braze.]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert important %}
Vous pouvez ajouter jusqu'à 200 étapes dans un Canvas. Si votre Canvas dépasse 200 étapes, des problèmes de chargement peuvent survenir.
{% endalert %}

##### Durée maximale

Au fur et à mesure que votre parcours Canvas augmente en étapes, la durée maximale est le temps le plus long possible qu'un utilisateur peut prendre pour compléter ce Canvas. Elle est calculée en ajoutant les délais et les fenêtres de déclenchement de chaque étape pour chaque variante sur le chemin le plus long. Par exemple, si votre Canvas a une étape de délai avec un délai de 3 jours et une étape Message, la durée maximale de votre Canvas sera de 3 jours.

##### Modification d'une étape

Vous souhaitez modifier une étape dans votre parcours utilisateur ? Découvrez comment procéder selon votre flux de travail Canvas !

Vous pouvez modifier n'importe quelle étape de votre flux de travail Canvas en sélectionnant l'un des composants. Par exemple, disons que vous souhaitez modifier votre première étape, un composant de [Délai]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), dans votre flux de travail à un jour spécifique. Sélectionnez l'étape pour afficher ses paramètres et ajustez votre délai sur le 1er mars. Ceci signifie que le 1er mars, vos utilisateurs passeront à l'étape suivante de votre Canvas.

![Exemple d'étape "Délai" avec le délai réglé sur "Jusqu'à un jour précis".]({% image_buster /assets/img_archive/edit_delay_flow.png %})

Vous pouvez également modifier et ajuster rapidement les **Paramètres d'action** de votre étape [Parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) pour retenir les utilisateurs pendant une période donnée. Leur parcours suivant est donc priorisé selon les actions intervenant durant cette période d'évaluation.

![La deuxième étape du Canvas, "Paramètres d'action", avec une fenêtre d'évaluation fixée à 1 jour.]({% image_buster /assets/img_archive/action_paths_flow.png %})

Les composants légers de Canvas permettent une expérience d'édition facilitée. Ajuster les détails les plus précis de votre Canvas en est d'autant plus simple. 

##### Messages dans Canvas

Modifiez les messages dans un composant Canvas pour contrôler les messages envoyés dans une étape spécifique. Canvas peut envoyer des e-mails, des notifications push mobiles et Web, ainsi que des webhooks pour s'intégrer à d'autres systèmes. Comme pour les campagnes, vous pouvez utiliser certains modèles [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) pour personnaliser vos messages.

{% alert tip %}
Saviez-vous que vous pouvez inclure des noms de composants Canvas dans vos messages et vos modèles de lien ?<br>
Utilisez l'étiquette Liquid `campaign.${name}` dans Canvas pour afficher le nom du composant Canvas actuel.
{% endalert %}

Le composant Message gère les messages envoyés aux utilisateurs. Vous pouvez sélectionner vos **Canaux de messagerie** et ajuster les **Paramètres de réception** pour optimiser l'envoi de messages de votre Canvas. Pour plus de détails sur ce composant, consultez la section [Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

![L'étape "Configurer les messages", avec "Canaux de messagerie" sélectionné qui affiche la liste des canaux de communication disponibles, tels que le push Android, les cartes de contenu, l'e-mail, et plus encore.]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

Sélectionnez **Terminé** après avoir terminé la configuration de votre composant Canvas.

{% tabs local %}
{% tab Canvas Entry Properties %}

L'[objet `context`]({{site.baseurl}}/api/objects_filters/context_object) est configuré dans l'étape **Planification d'entrée** de la création d'un Canvas et indique le déclencheur qui fait entrer un utilisateur dans un Canvas. Ces propriétés peuvent également accéder aux propriétés des charges utiles d'entrée dans les Canvas déclenchés par API. Notez que l'objet `context` peut avoir une taille maximale de 50 Ko. 

Utilisez le code Liquid suivant lorsque vous faites référence à ces propriétés créées lors de l'entrée dans le Canvas : {% raw %} ``context.${property_name}`` {% endraw %}. Notez que les événements doivent être des événements personnalisés ou des événements d'achat pour être utilisés de cette manière.

{% raw %}
Imaginons, par exemple, la requête suivante : `\"context\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Vous pourriez ajouter le mot « shoes » à un message avec ce code Liquid ``{{context.${product_name}}}``.
{% endraw %}

{% endtab %}

{% tab Event Properties %}
Les propriétés d'événement sont les propriétés que vous avez définies sur des événements personnalisés et des achats. Ces `event_properties` peuvent être utilisées dans les campagnes ayant une livraison par événement ainsi que dans les Canvas. 

Dans Canvas, les propriétés d'événement personnalisé et d'achat peuvent être utilisées en Liquid dans toute étape de message qui suit une étape de parcours d'action. Utilisez ce code Liquid {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %} lorsque vous faites référence à ces `event_properties`. Ces événements doivent être des événements personnalisés ou d'achat pour être utilisés ainsi dans le composant de message.

Dans la première étape de message suivant un parcours d'action, vous pouvez utiliser les `event_properties` liées à l'événement référencé dans le parcours d'action. Vous pouvez disposer d'autres étapes (n'étant pas un autre parcours d'action ou une étape de message) entre cette étape de parcours d'action et celle de message. Prenez en compte le fait que vous n'aurez accès aux `event_properties` que si votre étape de message peut être remontée jusqu'à un parcours n'étant pas « Tous les autres » dans l'étape du parcours d'action.

{% endtab %}
{% endtabs %}

#### Étape 2.3 : Modifier les connexions

Pour déplacer une connexion entre des étapes, sélectionnez la flèche reliant les deux composants et sélectionnez un autre composant. Pour supprimer la connexion, sélectionnez la flèche suivie de **Annuler la connexion** dans le pied de page du compositeur Canvas.

### Étape 3 : Ajouter un groupe de contrôle

Vous pouvez ajouter un groupe de contrôle à votre Canvas en sélectionnant le bouton <i class="fas fa-plus-circle"></i> plus pour ajouter une nouvelle variante. 

Braze assurera un suivi des conversions des utilisateurs figurant dans le groupe de contrôle. Ils ne recevront toutefois aucun message. Pour garantir la précision du test, nous suivrons le nombre de conversions pour vos variantes et votre groupe de contrôle pour la même durée, comme il est indiqué dans l'écran de sélection de l'événement de conversion. 

Pour modifier la répartition de vos messages, double-cliquez sur les en-têtes **Nom de variante**.

Dans cet exemple, notre Canvas est réparti en deux variantes. La variante 1 concerne 70 % des utilisateurs. La seconde variante est un groupe de contrôle qui rassemble les 30 % d'utilisateurs restants.

![Un exemple de variante dans un Canvas Braze, où 70 % vont à la "Variante 1", qui retarde d'un jour dans la première étape, puis envoie un message dans la deuxième étape. Les 30 % restants sont dirigés vers un "Contrôle" qui ne prévoit aucune étape de suivi.]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

#### Sélection intelligente pour Canvas

Les fonctionnalités de sélection intelligente sont désormais disponibles dans les Canvas multivariés. À l'instar de la fonctionnalité de [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) pour les campagnes multivariées, la sélection intelligente pour Canvas analyse les performances de chaque variante du Canvas et ajuste le pourcentage d'utilisateurs acheminés par le biais de chaque variante. Cette répartition est basée sur les indicateurs de performance de chaque variante afin de maximiser le nombre total de conversions attendues.

N'oubliez pas que les Canvas multivariés vous permettent de tester non seulement le contenu, mais aussi le calendrier et les canaux. La sélection intelligente vous permet de tester des Canvas de manière plus efficace et de garantir que vos utilisateurs seront dirigés vers le meilleur parcours Canvas possible.

![L'option "Sélection intelligente" est activée dans la page "Modifier la répartition des variantes". Au fur et à mesure qu'elle analyse et optimise le Canvas, elle affiche une barre horizontale en travers de la page qui est divisée en plusieurs sections, chacune variant en couleur et en taille. Il s'agit uniquement d'une représentation visuelle qui ne correspond à aucune analytique spécifique.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

La sélection intelligente pour Canvas optimise vos résultats Canvas en effectuant des ajustements progressifs en temps réel de la répartition des utilisateurs triés dans chaque variante. Lorsque l'algorithme statistique détermine un gagnant décisif parmi vos variantes, il élimine les variantes moins performantes et place tous les futurs destinataires éligibles du Canvas dans les variantes gagnantes. 

En ce sens, la sélection intelligente fonctionne mieux sur des Canvas auxquels de nouveaux utilisateurs accèdent fréquemment.

### Étape 4 : Enregistrer et lancer

Une fois la création de votre Canvas terminée, sélectionnez **Lancer le Canvas** pour enregistrer et lancer votre Canvas. Après avoir lancé votre Canvas, vous pourrez consulter les analyses de votre parcours au fur et à mesure qu'elles arrivent sur la page **Détails du Canvas**. 

Vous pouvez également enregistrer votre Canvas en tant que brouillon si vous souhaitez le retravailler un peu plus tard.

![Un exemple de Canvas dans Braze.]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
Vous avez besoin de modifier votre Canvas après son lancement ? C'est tout à fait possible ! Consultez [Modification des Canvas après le lancement]({{site.baseurl}}/post-launch_edits/) pour plus d'informations.
{% endalert %}