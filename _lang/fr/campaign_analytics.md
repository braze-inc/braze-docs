## Analyse de campagne

Une fois que vous avez lancé votre campagne, vous pouvez revenir à la page des détails de cette campagne pour afficher les métriques clés. Accédez à la page **Campagnes** et sélectionnez votre campagne pour ouvrir la page des détails. Pour {% if include.channel == "Content Card" %}cartes de contenu{% elsif include.channel == "email" %}e-mail{% elsif include.channel == "in-app message" %}messages in-app{% elsif include.channel == "push" %}messages push{% elsif include.channel == "SMS" %}messages SMS{% endif %} envoyés dans Canvas, consulter [Analyse de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/).

{% alert tip %}
Vous recherchez des définitions pour les termes et les métriques répertoriés dans votre rapport ? Consultez notre {% if include.channel == "email" %}[Glossaire de l’analyse e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/){% elsif include.channel == "Content Card" %}[Glossaire des métriques de rapport]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/) et filtrez par cartes de contenu{% elsif include.channel == "in-app message" %}[Glossaire des métriques de rapport]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/) et filtrez par message in-app{% elsif include.channel == "push" %}[Glossaire des métriques de rapport]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/) et filtrez par notification push{% elsif include.channel == "SMS" %}[Glossaire des métriques de rapport]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/) et filtrez par SMS{% endif %}.
{% endalert %}

Depuis l’onglet **Campaign Analytics** (Analyse de campagne), vous pouvez afficher vos rapports dans une série de volets. Vous pouvez voir plus ou moins que ceux énumérés dans les sections ci-dessous, mais chacun a son propre objectif utile.

### Détails de la campagne

Le volet **Campaign Details** (Détails de la campagne) affiche une vue d’ensemble de haut niveau de l’ensemble des performances pour votre {% if include.channel == "Content Card" %}carte de contenu.{% elsif include.channel == "email" %}e-mail.{% elsif include.channel == "in-app message" %}message in-app.{% elsif include.channel == "push" %}message push.{% elsif include.channel == "SMS" %}SMS.{% endif %}

Examinez ce volet pour voir les métriques globales, telles que le nombre de messages envoyés à tel nombre de destinataires, le taux de conversion principal et le chiffre d’affaires total généré par ce message. Cette page permet également de consulter les paramètres généraux : Paramètres de livraison, Paramètres publics et Paramètres de conversion.

{% if include.channel == "Content Card" %}
![Volet de détails de la campagne avec un aperçu des métriques utilisées pour déterminer les performances de la campagne.]({% image_buster /assets/img/cc-campaign-details.png %})

{% elsif include.channel == "email" %}
![Volet de détails de la campagne avec un aperçu des métriques utilisées pour déterminer les performances de la campagne.]({% image_buster /assets/img/campaign_details_email.png %})

{% elsif include.channel == "push" %}
![Volet de détails de la campagne avec un aperçu des métriques utilisées pour déterminer les performances de la campagne.]({% image_buster /assets/img/campaign_details_push.png %})

{% elsif include.channel == "SMS" %}
![Volet de détails de la campagne avec un aperçu des métriques utilisées pour déterminer les performances de la campagne.]({% image_buster /assets/img/campaign_details_sms.png %})

{% elsif include.channel == "in-app message" %}
![Volet de détails de la campagne avec un aperçu des métriques utilisées pour déterminer les performances de la campagne.]({% image_buster /assets/img/campaign_details_iam.png %})

Dans Canvas, vous verrez les performances des messages in-app cartographiés sur le Canvas que vous avez créé. Vous pouvez utiliser le panneau de commande en haut de la page pour effacer les autres types de messages (canaux) et afficher uniquement les messages in-app dans votre Canvas.

![]({% image_buster /assets/img/in-app_message_canvas_reporting.png %})

{% endif %}

{% if include.channel == "Content Card" %}

#### Groupes de contrôle {#cc-control-group}

Pour mesurer l’impact d’une carte de contenu individuelle, vous pouvez ajouter un [groupe de contrôle][2] à un test A/B. Le volet supérieur **Campaign Details** (Détails de la campagne) n’inclut pas les métriques de la variante Groupe de contrôle.

{% alert warning %}
Les cartes de contenu n’offrent pas d’assistance prête à l’emploi pour le groupe de contrôle. Si vous souhaitez tirer parti des groupes de contrôle, vous devez créer un flux personnalisé, y compris des cartes personnalisées et un suivi de mise en œuvre personnalisé pour vous assurer que les variantes sont correctement enregistrées dans le tableau de bord et pour permettre la précision du groupe de contrôle dans vos analyses. 
<br><br>Assurez-vous de consigner les impressions pour les cartes de contrôle afin d’informer notre analyse du moment où un utilisateur a vu la carte de contrôle dans son flux. Pour plus de détails, voir les guides de développeur [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/integration/#content-card-model), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/#fully-custom-content-card-display-for-android) et [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/#data-models).
{% endalert %}

{% elsif include.channel == "SMS" %}

#### Groupes de contrôle {#sms-control-group}

Pour mesurer l’impact d’un SMS individuel, vous pouvez ajouter un [groupe de contrôle][2] à un test A/B. Le volet supérieur **Campaign Details** (Détails de la campagne) n’inclut pas les métriques de la variante Groupe de contrôle.

{% endif %}

### Performances du message

Le volet **Message Performance** (Performances du message) indique les performances de votre message à travers différentes dimensions. Les métriques de ce volet varient en fonction de votre canal de messagerie choisi, et selon que vous exécutez ou non un test multivarié. Vous pouvez cliquer sur l’icône <i class="fa fa-eye preview-icon"></i>Preview**** (Aperçu) pour afficher votre message pour chaque variante ou canal.

{% if include.channel == "Content Card" %}
![Analyse des performances des messages de carte de contenu]({% image_buster /assets/img/cc-message-performance.png %})

{% elsif include.channel == "email" %}
![Analyse des performances des messages e-mail]({% image_buster /assets/img_archive/email_message_performance.png %})

{% elsif include.channel == "in-app message" %}
![Analyse des performances des messages in-app]({% image_buster /assets/img_archive/iam_message_performance.png %})

{% elsif include.channel == "push" %}
![Analyse des performances des messages push]({% image_buster /assets/img_archive/push_message_performance.png %})

{% elsif include.channel == "SMS" %}
![Volet des performances des SMS/MMS qui comprend un tableau de métriques pour un groupe de contrôle, la variante 1 et la variante 2.]({% image_buster /assets/img_archive/sms_message_performance.png %})

{% endif %}

Si vous souhaitez simplifier votre vue, cliquez sur <i class="fas fa-plus"></i> **Add/Remove Columns** (Ajouter/Supprimer des colonnes) et supprimez des métriques comme souhaité. Par défaut, toutes les métriques sont affichées.

{% if include.channel == "email" %}

#### Cartes de chaleur

De plus, vous pouvez voir comment différents liens performants dans une campagne d’e-mail unique utilisent des cartes de chaleur. Développez le menu déroulant **Total Clicks** (Nombre total de clics) et cliquez sur **View Heat Map** (Afficher la carte de chaleur) pour afficher une vue visuelle de votre e-mail qui montre la fréquence globale et l’emplacement des clics dans la durée de vie de la campagne.

![analyse_e-mail]({% image_buster /assets/img_archive/email_click_results_heatmap.gif %})

{% endif %}

{% if include.channel == "Content Card" %}

#### Métriques de la carte de contenu

Voici une description de certaines métriques clés que vous pouvez voir lors de l’examen des performances de vos messages. Pour les définitions de toutes les métriques des cartes de contenu, reportez-vous au [Glossaire des métriques de rapport][1] et filtrez par carte de contenu.

| Terme | Définition |
| -- | -- |
| Impressions totales | Nombre total d’impressions enregistrées pour une carte de contenu donnée. Ce nombre peut être incrémenté plusieurs fois pour le même utilisateur. |
| Impressions uniques | Nombre d’utilisateurs ayant consulté une carte donnée. Ce nombre n’est pas incrémenté la deuxième fois qu’un utilisateur consulte une carte. |
| Destinataires uniques | Nombre total d’observateurs (uniques, mais seulement uniques par jour) qui ont consulté la carte particulière. Étant donné qu’un observateur peut être chaque jour un destinataire unique, vous devez vous attendre à ce que ce nombre soit plus élevé que les impressions uniques. |
| Clics uniques | Nombre de destinataires ayant cliqué sur le lien CTA d’une carte de contenu au moins une fois, à l’exclusion des clics sur les liens de désinscription fournis par Braze. |
Rejets uniques | Nombre d’utilisateurs qui ont rejeté les cartes de contenu d’une campagne. Un utilisateur qui rejette plusieurs fois une carte de contenu d’une campagne constitue un rejet unique. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
En matière de méthode d’enregistrement des impressions, il existe quelques différences entre Internet, Android et iOS. En règle générale, Braze enregistre une impression une fois qu’une carte est consultée (lorsqu’un utilisateur fait défiler la carte de contenu spécifique dans son flux).
{% endalert %}

{% details More on Unique Recipients versus Unique Impressions %}

Plusieurs métriques sont disponibles pour couvrir la visibilité de votre message. Elles incluent les messages envoyés, les destinataires uniques et les impressions uniques. En particulier, la différence entre les destinataires uniques et les impressions uniques peut s’avérer légèrement déroutante. Prenons quelques exemples de scénarios pour mieux comprendre ces métriques.

Imaginons que vous consultiez une carte de contenu aujourd’hui, que vous consultiez la même carte demain, et encore une fois après-demain. Vous serez alors comptabilisé trois fois comme destinataire unique. Par contre, vous ne serez comptabilisé que pour une seule impression unique. Vous serez également inclus dans le nombre de messages envoyés, car la carte était disponible sur votre appareil.

Autre exemple, supposons que vous consultiez cinq impressions uniques sur une campagne de carte de contenu affichant 150 000 messages envoyés. Cela signifie que la carte a été mise à disposition (en arrière-plan) à un public de 150 000 utilisateurs, mais que seuls cinq utilisateurs ont effectué toutes les étapes suivantes après l’envoi :

1. Ont démarré une session ou l’application a explicitement demandé une synchronisation des cartes de contenu (ou les deux)
2. Ont navigué dans la vue Carte de contenu
3. Le SDK a enregistré une impression et l’a consignée sur le serveur

Vos messages envoyés font référence aux cartes de contenu disponibles à la consultation, tandis que les destinataires uniques se réfèrent aux cartes de contenu qui ont été réellement consultées.

{% enddetails %}

{% elsif include.channel == "email" %}

#### Métriques des e-mails

Voici quelques métriques clés spécifiques aux e-mails que vous ne verrez pas dans d’autres canaux. Pour voir les définitions de toutes les métriques de courrier électronique utilisées dans Braze, reportez-vous à notre [Glossaire de l’analyse e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/).

| Terme | Définition |
| --- | --- |
| Spam | Pourcentage d’utilisateurs qui ont marqué votre e-mail comme spam, ou l’e-mail a été désigné comme spam. Si cette métrique est supérieure à 0,08, cela peut signaler que le texte de votre message est trop commercial ou que vous devez reconsidérer vos méthodes de collecte d’e-mails (de manière à n’envoyer des messages qu’aux destinataires intéressés par votre correspondance).
| Ouverture unique | Pourcentage des destinataires qui ont ouvert votre e-mail. Cela peut également inclure les e-mails ouverts par une machine. Ce nombre doit être compris entre 10 et 20 %. Tout ce qui est supérieur à 20 % est exceptionnel !
| Clics uniques | Pourcentage des destinataires ayant cliqué dans l’e-mail envoyé. Ce nombre doit être compris entre 5 et 10 %. Tout ce qui est supérieur à 10 % est exceptionnel !
| Clics pour ouvrir | Pourcentage des destinataires qui ont ouvert votre e-mail, puis cliqué dessus.
| Ouverture automatique | Inclut la proportion des « ouvertures » qui sont affectées par la Protection de la confidentialité dans Mail (MPP) d’Apple pour iOS 15. <br>Par exemple, si un utilisateur ouvre un e-mail à l’aide de l’application Mail sur un appareil Apple, cette opération sera enregistrée comme « Ouverture automatique ». Cette métrique est suivie à compter du 11 novembre 2021 pour Sendgrid et du 2 décembre 2021 pour Sparkpost.
| Autre ouverture | Inclut les e-mails qui n’ont pas été identifiés comme « Ouverture automatique ». <br>Par exemple, lorsqu’un utilisateur ouvre un e-mail sur une autre plate-forme (c.-à-d. application Gmail sur un téléphone, Gmail sur le navigateur de bureau), l’opération sera enregistrée comme « Autre ouverture ». Notez qu’un utilisateur peut également ouvrir un e-mail (c.-à-d. l’ouverture est alors comptabilisée comme « Autre ouverture ») avant qu’un comptage « Ouverture automatique » soit enregistré. Si un utilisateur ouvre un e-mail une fois (ou plus) après un événement d’ouverture automatique depuis une boîte de réception de courrier non-Apple, le nombre de fois que l’utilisateur ouvre l’e-mail est comptabilisé dans « Autre ouverture » et une seule fois vers « Ouverture unique ».
| Désabonnements | Pourcentage de destinataires ayant cliqué sur le lien « Se désabonner » dans votre e-mail.
{: .reset-td-br-1 .reset-td-br-2}

{% elsif include.channel == "in-app message" %}

#### Métriques de message in-app

Voici quelques indicateurs clés de messages in-app que vous pouvez voir dans vos analyses. Pour voir les définitions de toutes les métriques de message in-app utilisées dans Braze, reportez-vous à notre [Glossaire des métriques de rapport][1].

| Terme | Définition |
| --- | --- |
| Clics sur le corps du message | Se produit lorsqu’un utilisateur clique sur le message lui-même, et non pas sur l’un des boutons.
| Clics Bouton 1 et Bouton 2 | Pourcentage de destinataires ayant appuyé sur ce bouton spécifique. 
| Impressions uniques | Nombre total de personnes qui ont réellement reçu et affiché le message in-app. Si un utilisateur reçoit le message deux fois, il ne compte que comme un seul utilisateur.
| Impressions | Nombre d’utilisateurs dont les appareils ont signalé que le message a été délivré. Si un utilisateur reçoit le message deux fois, il est comptabilisé deux fois.

{: .reset-td-br-1 .reset-td-br-2}

{% elsif include.channel == "push" %}

#### Métriques de notification push

Voici une description de certaines métriques clés que vous pouvez voir lors de l’examen des performances de vos messages. Pour les définitions de toutes les métriques de notification push, reportez-vous au [Glossaire des métriques de rapport][1] et filtrez par notification push.

| Terme | Description |
| --------- | --- |
| Rebonds | Les notifications push envoyées à ces utilisateurs n’ont pas pu être délivrées. Ces utilisateurs ont été automatiquement désabonnés de toutes les notifications push futures. Voir [Rebonds de notification push](#bounced-push). |
| Ouvertures directes | Instances dans lesquelles un utilisateur a ouvert votre application en interagissant directement avec une notification push. |
| Ouvertures | Instances, y compris les ouvertures directes et les ouvertures influencées, dans lesquelles le SDK Braze a déterminé, à l’aide d’un algorithme exclusif, qu’une notification push a provoqué l’ouverture de l’application par un utilisateur. |
{: .reset-td-br-1 .reset-td-br-2}

> La remise des notifications constitue un « meilleur effort » de la part des APN. Cette action n’est pas destinée à fournir des données à votre application, mais seulement à informer l’utilisateur qu’il existe de nouvelles données disponibles. La distinction importante est que nous allons afficher le nombre de messages que nous avons délivrés avec succès aux APN, et pas nécessairement combien d’APN ont délivré des notifications avec succès aux appareils.

#### Rebonds de notification push {#bounced-push}

##### Service de notification push d’Apple

Les rebonds se produisent dans les APN lorsqu’une notification push tente de délivrer une notification à un appareil sur lesquels l’application prévue n’est pas installée. Les APN ont également le droit de modifier les jetons pour les appareils arbitrairement. Si vous essayez d’envoyer un message à un appareil d’utilisateur sur lequel le jeton push a changé entre le moment où nous avons déjà enregistré son jeton (c.-à-d. au début de chaque session lorsque nous enregistrons un utilisateur pour un jeton push) et le moment de l’envoi, il en résulte un rebond.

Si un utilisateur désactive la notification push dans les paramètres de l’appareil lors de la prochaine ouverture d’application, le SDK détecte que le push a été désactivé et informe Braze. À ce stade, nous allons mettre à jour l’état de l’opération push de Activé à Désactivé. Lorsqu’un utilisateur désactivé reçoit une campagne push avant d’avoir une nouvelle session, la campagne s’affiche avec succès et apparaît comme livrée. Il n’y aura pas de rebond de push pour cet utilisateur. Après une session ultérieure, lorsque vous essayez d’envoyer un push à l’utilisateur, Braze sait déjà si nous avons un jeton, et donc aucune notification n’est envoyée.

Notez que les notifications push expirant avant la livraison ne sont pas considérées comme ayant échoué et ne seront pas enregistrées comme rebond.

##### Messagerie cloud Firebase

La messagerie cloud Firebase (FCM) peut être utilisée dans trois cas :

| Scénario | Description |
| -- | -- |
| Applications désinstallées | Lorsqu’un message tente une livraison à un appareil et que l’application prévue est désinstallée sur cet appareil, le message est supprimé et l’ID d’enregistrement de l’appareil est invalidé. Toute future tentative d’envoi de message de l’appareil renvoie une erreur NotRegistered. |
| Application sauvegardée | Lorsqu’une application est sauvegardée, son ID d’enregistrement peut cesser d’être valide avant la restauration de l’application. Dans ce cas, FCM ne conservera plus l’ID d’enregistrement de l’application et l’application ne recevra plus de messages. Ainsi, les ID d’enregistrement ne doivent _pas_ être enregistrés lorsqu’une application est sauvegardée. |
| Application mise à jour | Lorsqu’une application est mise à jour, l’ID d’enregistrement de la version précédente peut ne plus fonctionner. Une application mise à jour doit donc remplacer son ID d’enregistrement existant. |
{: .reset-td-br-1 .reset-td-br-2}

{% elsif include.channel == "SMS" %}

#### Métriques de messages SMS

Voici une description de certaines métriques clés que vous pouvez voir lors de l’examen des performances de vos messages. Pour les définitions de toutes les métriques de messages SMS, reportez-vous au [Glossaire des métriques de rapport][1] et filtrez par SMS.

| Terme | Définition |
| -- | -- |
| Envoyé | Une campagne ou une Canvas Step a été lancée ou déclenchée, et un SMS a été envoyé par Braze. Il est possible que le SMS n’atteigne pas l’appareil d’un utilisateur en raison d’erreurs, comme expliqué ci-dessous.
| Envoi à l’opérateur | Braze a tenté d’envoyer le SMS aux opérateurs. Cette statistique est la somme des livraisons confirmées, des rejets et des envois pour lesquels l’opérateur n’a pas confirmé la livraison ou le rejet. Dans certains cas, les opérateurs ne confirment pas la livraison ou le rejet, car c’est leur politique, ou bien ils n’ont pas pu le faire au moment de l’envoi.
| Échecs de livraison | Messages pour lesquels il n’y a pas eu de tentative d’envoi en raison d’un résultat défaillant dans les journaux Twilio. Ces erreurs peuvent être dues au débordement de file d’attente ou à un numéro de destinataire non valide, selon le code d’erreur Twilio associé. Veuillez contacter l’[assistance]({{site.baseurl}}/braze_support/) de Braze pour obtenir de l’aide pour comprendre les raisons des échecs de livraison.
| Livraison confirmée | L’opérateur a confirmé que le SMS a bien été envoyé au numéro de téléphone cible. En tant que client Braze, les livraisons sont facturées vers votre attribution SMS.
| Rejets | Le SMS a été rejeté par l’opérateur. Ce rejet peut avoir plusieurs raisons, notamment : filtrage du contenu par l’opérateur, disponibilité de l’appareil destinataire, numéro de téléphone qui n’est plus en service, etc. En tant que client Braze, les rejets sont facturés vers votre attribution SMS.
| Désabonnement | Un utilisateur a répondu à votre message avec un [mot-clé Opt-Out]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords) et a été désabonné de votre programme SMS. Une réponse utilisateur est mesurée à chaque fois qu’un utilisateur envoie un message entrant dans les quatre heures suivant la réception de votre message.
| Aide | Un utilisateur a répondu à votre message avec un [mot-clé HELP]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords) et a reçu une réponse automatique HELP. Une réponse utilisateur est mesurée à chaque fois qu’un utilisateur envoie un message entrant dans les quatre heures suivant la réception de votre message.
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

### Performances historiques

Le volet **Historical Performance** (Performances historiques) vous permet d’afficher les métriques **Message Performance** (Performances du message) sous forme de graphique au fil du temps. Utilisez les filtres en haut du volet pour modifier les statistiques et les canaux affichés dans le graphique. La plage temporelle de ce graphique reflète toujours la plage de temps spécifiée en haut de la page. 

Pour obtenir une répartition quotidienne, cliquez sur le menu en sandwich <i class="fas fa-bars"></i> et sélectionnez **Download SCV** (Télécharger CSV) pour recevoir une exportation CSV du rapport.

![Un graphique du volet Historical Performance (Performances historiques) avec des statistiques d’un e-mail de février 2021 à mai 2022.]({% image_buster /assets/img/cc-historical-performance.png %})

{% if include.channel == "in-app message" %}

{% alert note %}
Si vous choisissez d’envoyer des messages uniquement aux utilisateurs qui peuvent consulter la dernière version Braze des messages in-app (Génération 3), votre **Public cible** ne s’ajuste pas pour refléter votre choix.
{% endalert %}

{% endif %}

{% if include.channel == "SMS" %}

### Réponses à des mots-clés

Le volet **Keyword Responses** (Réponses à des mots-clés) affiche une chronologie des mots-clés entrants auxquels les utilisateurs ont répondu après avoir reçu votre message.  

![Tableau des réponses à des mots-clés dans des SMS/MMS au niveau de la campagne. Inclut un graphique linéaire de distribution de mots-clés au fil du temps, et une section Catégories de mots-clés avec des cases à cocher sélectionnées pour les options Opt-In (Abonnement), Opt-Out (Désabonnement), Help (Aide), Other (Autre) More (Plus) et Coaching.]({% image_buster /assets/img/sms/keyword_responses.png %})

C’est aussi là que vous pouvez afficher la répartition des réponses pour chaque catégorie de mots-clés afin de déterminer les prochaines étapes de [reciblage]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns) et de [créer un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) facilement.

![Le tableau sous le graphique linéaire comporte des colonnes pour la catégorie de mots-clés, la répartition des réponses et le reciblage, où vous avez la possibilité de créer un segment avec la catégorie de mots-clés.]({% image_buster /assets/img/sms/keyword_segments.png %})

{% endif %}

### Détails de l’événement de conversion

Le volet **Conversion Event Details** (Détails de l’événement de conversion) affiche les performances des événements de conversion pour votre campagne. Pour plus d’informations, consultez [Événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/#step-3-view-results).

![Volet Conversion Event Details (Détails des événements de conversion).]({% image_buster /assets/img/cc-conversion.png %})

### Corrélation de conversion

Le volet **Conversion Correlation** (Corrélation de conversion) vous donne des informations sur les attributs et les comportements d’utilisateur qui confortent ou infirment les résultats que vous fixez pour les campagnes. Pour plus d’informations, consultez [Corrélation de conversion]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation/).

![Volet Conversion Correlation (Corrélation de conversion) avec une analyse des attributs et du comportement des utilisateurs pour l’événement de conversion primaire -A.]({% image_buster /assets/img/convcorr.png %})

{% if include.channel == "SMS" %}

### Événements SMS Currents

Comme pour les e-mails, Braze reçoit des événements au niveau utilisateur liés à un message SMS à mesure qu’il effectue son parcours à destination d’un utilisateur. Tout événement SMS entrant sera également envoyé comme événement Currents par le biais de l’événement [SMS InboundReceived]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#sms-inbound-received-events) (Réception SMS entrant). Cela vous permettra d’effectuer des actions supplémentaires ou de signaler les messages que vos utilisateurs envoient à l’extérieur de la plate-forme Braze. 

{% alert note %}
Les messages entrants sont tronqués au-delà de 1 600 caractères.
{% endalert %}

{% endif %}

## Rapport de rétention

Les rapports de rétention indiquent les taux auxquels vos utilisateurs ont effectué un événement de rétention sélectionné sur les périodes dans une campagne ou un Canvas spécifique. Pour plus d’informations, consultez [Rapports de rétention]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/retention_reports/).

## Rapport d’entonnoir

Les rapports d’entonnoir offrent un rapport visuel qui vous permet d’analyser les parcours de vos clients après la réception d’une campagne ou d’un Canvas. Si votre campagne ou votre Canvas utilise un groupe de contrôle ou plusieurs variantes, vous serez en mesure de comprendre comment les différentes variantes ont impacté l’entonnoir de conversion à un niveau plus précis et de l’optimiser en fonction de ces données.

Pour plus d’informations, consultez [Rapports d’entonnoir]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/funnel_reports/).

[1]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
[2]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants
