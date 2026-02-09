---
nav_title: "in-app Messages"
article_title: in-app Messages
page_order: 2
alias: /in-app_messages/
description: "Cette page d’accueil contient tous les messages in-app. Vous y trouverez des articles sur la création de messages in-app, l'éditeur par glisser-déposer, la personnalisation de vos messages, la création de rapports, etc."
channel:
  - in-app messages
search_rank: 5
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-in-app-in-browser){: style="float:right;width:120px;border:0;" class="noimgborder"} Messages in-app

> Les messages in-app vous permettent d'envoyer du contenu à votre utilisateur sans interrompre sa journée avec une notification push, car ces messages ne sont pas envoyés en dehors de l'application de l'utilisateur et n'empiètent pas sur son écran d'accueil. 

Des messages in-app personnalisés et adaptés améliorent l’expérience utilisateur et aident votre audience à tirer le meilleur parti de votre application. Grâce à un choix de mises en page et d’outils de personnalisation, les messages in-app supposent un engagement inédit de vos utilisateurs. Ils s'inscrivent dans un contexte, sont moins urgents et sont délivrés lorsque l'utilisateur est actif dans votre application. Pour des exemples de messages in-app, consultez nos [témoignages de clients](https://www.braze.com/customers/).

## Cas d’utilisation

Grâce au contenu riche des messages in-app, vous pouvez exploiter ce canal pour une variété de cas d’utilisation :

| Cas d’utilisation | Explication |
| --- | --- |
| Amorçage de notification push | Lancez une campagne d'[amorçage de notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) à l'aide d'un message in-app riche afin de montrer à vos clients l'intérêt de l’abonnement aux notifications push pour votre application ou votre site, et présentez-leur une invite pour autoriser les notifications push.
| Soldes et promotions | Utilisez des messages in-app modaux pour accueillir les clients avec des supports visuellement attrayants contenant des codes de promotion ou des offres statiques. Incitez-les à faire des achats ou des conversions qu’ils n’auraient autrement pas faits. |
| Encouragement de l’adoption de fonctions | Encouragez les clients à utiliser d’autres parties de votre application ou à profiter d’un service. |
| Campagnes hautement personnalisées | Placez des messages in-app de façon à ce que vos clients les voient dès qu’ils entrent dans votre application ou votre site. Ajoutez quelques fonctionnalités de personnalisation de Braze, telles que le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), pour obliger les utilisateurs à passer à l'action et ainsi rendre votre sensibilisation plus efficace.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Autres cas d’utilisation à considérer :

- Nouvelles fonctionnalités de l’application
- Gestion de l’application
- Revues
- Mises à niveau ou mises à jour de l’application
- Concours et tirages au sort

## Types de messages standard

Les onglets suivants montrent ce que vos utilisateurs voient s’ils ouvrent l’un de nos types de messages standard intégrés : messages in-app slideup, modaux et plein écran.

{% tabs %}
{% tab Slideup %}

Les messages slideup apparaissent généralement en haut et en bas de l’écran de l’application (vous pouvez le définir à la création du message). Ils sont parfaits pour avertir vos utilisateurs de nouvelles conditions de service, cookies et autres extraits de code d’information.

![Message in-app slideup apparaissant en bas de l’écran de l’application. Le diaporama comprend une image d'icône et un bref message.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

Les modaux apparaissent au centre de l’écran de l’appareil avec une incrustation le démarquant de votre application en arrière-plan. Ils sont parfaits pour suggérer plus ou moins subtilement à votre utilisateur de profiter d’une vente ou d’un concours.

![Message in-app modal apparaissant au centre d’une application et d’un site Web comme boîte de dialogue. La fenêtre modale comprend une image, un en-tête, un corps de message et deux boutons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Fullscreen %}

Comme leur nom l’indique, les messages plein écran occupent tout l’écran de l’appareil Ce type de message est idéal lorsque vous avez vraiment besoin de toute l’attention de votre utilisateur, dans le cas par exemple de mises à jour obligatoires de l’application.

![Message in-app plein écran sur un écran d’application. Le message en plein écran comprend une grande image, un en-tête, le corps du message et deux boutons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

Outre ces modèles de messages par défaut, vous pouvez également personnaliser davantage votre envoi à l'aide de messages in-app personnalisés en HTML, de fenêtres modales/boîtes de dialogue en CSS ou de formulaires de capture d'e-mails en ligne. Pour plus d'informations, reportez-vous à la rubrique [Personnalisation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

## Des messages in-app personnalisés

Les messages in-app sont envoyés sous forme de modèles de messages in-app lorsque l'option **Réévaluer l'éligibilité de la campagne avant affichage** est sélectionnée ou si l'une des étiquettes Liquid suivantes est présente dans le message :

- `canvas_entry_properties`
- `connected_content`
- Les variables SMS telles que {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Cela signifie que lors du démarrage de la session, l'appareil recevra le déclencheur de ce message in-app au lieu de l'intégralité du message. Lorsque l'utilisateur déclenche le message intégré à l'application, l'appareil de l'utilisateur effectuera une demande réseau pour récupérer le message réel.

{% alert note %}
Le message ne sera pas envoyé si l'appareil n'a pas accès à l'internet. Le message risque de ne pas être envoyé si la logique du liquide prend trop de temps à se mettre en place.
{% endalert %}

## Abandonner le comportement

Chez Braze, un abandon se produit lorsqu'un utilisateur entreprend une action qui le rend éligible pour recevoir un message, mais qu'il ne reçoit pas le message parce que la logique Liquid le marque comme inéligible. Par exemple :

1. Sam effectue une action qui devrait déclencher une campagne d'e-mailing.
2. Le corps de l'e-mail contient une logique Liquid qui indique que si le score d'un attribut personnalisé est inférieur à 50, il ne faut pas envoyer cet e-mail.
3. Le score de l'attribut personnalisé de Sam est de 20.
4. Braze reconnaît que Sam ne devrait pas recevoir cet e-mail, et l'e-mail est interrompu.
5. Un événement d'abandon est enregistré.

Cependant, comme les messages in-app sont un canal de communication à flux tiré, le fonctionnement des interruptions est un peu différent.

### Comportement d'abandon des messages in-app

Les messages in-app sont récupérés par l'appareil au début de la session et mis en cache sur l'appareil, de sorte que, quelle que soit la qualité de la connexion Internet, le message peut être délivré instantanément à l'utilisateur. Par exemple, si un utilisateur reçoit cinq messages in-app au cours de sa session, il recevra les cinq au début de la session. Les messages seront mis en cache localement et apparaîtront lorsque les événements personnalisés définis se produiront (démarrage de la session, clic de l'utilisateur sur un bouton qui enregistre un événement personnalisé, ou autre).

En d'autres termes, la logique qui détermine si nous devons interrompre un message in-app intervient **avant que** le déclencheur ne se produise. Pour le démontrer, disons que Sam, dans l'exemple de l'e-mail, est abonné aux notifications push.

1. Sam commence une session en lançant une application alimentée par Braze sur leur téléphone.
2. Sur la base des critères d'audience des campagnes actives dans l'espace de travail, Sam pourrait être éligible à cinq campagnes différentes. Les cinq sont téléchargés dans leur téléphone et mis en cache.
3. Sam **n'a** effectué **aucune** action qui déclencherait ces messages, mais il pourrait recevoir ces messages au cours de la session.
4. Dans deux des messages in-app, le liquid a des règles qui excluent Sam de la réception du message (par exemple, l'attribut personnalisé de son score n'est pas assez élevé).
5. Sam ne reçoit pas les deux messages in-app qui les excluent, mais ils reçoivent les trois autres messages.
6. Aucun événement d'abandon n'est enregistré.

Braze n'enregistre aucun événement d'abandon dans le cas de Sam, car cela ne correspond pas à notre définition d'un abandon ; Sam **n'a** effectué **aucune** action susceptible de déclencher les messages. Pour les messages in-app, les utilisateurs n'effectuent jamais réellement le déclencheur avant que Braze ne détermine qu'ils ne doivent pas voir le message.

#### Modèle de comportement d'abandon des messages in-app

Les [messages in-app modélisés](#templated-in-app-messages) obligent le SDK à réévaluer si un message doit s'afficher lorsque l'événement déclencheur se produit. Le comportement d'abandon est différent. Pour le démontrer, prenons l'exemple suivant :

1. Sam démarre une session Braze en lançant une application alimentée par Braze sur son téléphone.
2. Les critères d'audience des campagnes actives indiquent que Sam pourrait être éligible pour un message in-app modélisé, de sorte que les informations de déclenchement sont envoyées à leur appareil sans la charge utile du message.
3. Sam sélectionne un bouton qui enregistre un événement personnalisé, déclenchant ainsi le message in-app.
4. L'appareil de Sam émet une requête réseau pour récupérer le message in-app.
5. La logique Liquid du message conduit à un abandon, Braze enregistre donc ce message comme un abandon ; Sam a effectué l'action de déclenchement avant cette évaluation.

##### Comparaison du comportement d'abandon des messages in-app

Ce tableau compare les envois de messages in-app auxquels Sam a été confronté :

| Message in-app | Abandonner le comportement |
| --- | --- |
| Standard | Un événement d'abandon n'a pas été déclenché parce que Sam n'a effectué aucune action susceptible de déclencher un message.<br><br>Les messages in-app standard n'enregistrent pas les abandons car la définition d'un abandon est "n'a pas vu le message malgré l'exécution de l'action déclenchchement". Étant donné que les messages in-app sont envoyés à l'appareil avant que les actions déclenchantes ne se produisent, il n'est pas logique de considérer que les messages in-app ont été omis en raison de la logique du déclencheur. |
| Modèle | Un événement d'abandon a été enregistré parce que Sam a effectué l'action déclencheur pour déclencher le message in-app tempplated, mais a reçu un abandon dans le Liquid templating. <br><br>Les messages in-app templis enregistrent des abandons parce que l'évaluation du Liquid a lieu après l'exécution de l'action déclenchchement. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Ressources supplémentaires

Avant de vous lancer dans la création de vos propres campagnes de messages in-app - ou dans l'utilisation de messages in-app dans le cadre d'une campagne multicanal - nous vous recommandons vivement de consulter notre [guide de préparation des messages in-app.]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/) Ce guide couvre les questions de ciblage, de contenu et de conversion que vous devez prendre en compte lors de la création de messages in-app.
