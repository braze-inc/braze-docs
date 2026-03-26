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

# [![Cours d'apprentissage de Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-in-app-in-browser){: style="float:right;width:120px;border:0;" class="noimgborder"} Messages in-app

> Les messages in-app vous permettent de transmettre du contenu à vos utilisateurs sans les interrompre avec une notification push, car ces messages ne sont pas diffusés en dehors de l'application et n'apparaissent pas sur leur écran d'accueil. 

Des messages in-app personnalisés et adaptés améliorent l’expérience utilisateur et aident votre audience à tirer le meilleur parti de votre application. Grâce à un choix de mises en page et d’outils de personnalisation, les messages in-app supposent un engagement inédit de vos utilisateurs. Elles sont accompagnées d'un contexte, sont moins urgentes et sont envoyées lorsque l'utilisateur est actif dans votre application. Pour des exemples de messages in-app, veuillez consulter nos [témoignages clients](https://www.braze.com/customers/).

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

![Message in-app slideup apparaissant en bas de l’écran de l’application. La fenêtre contextuelle comprend une icône et un message succinct.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

Les modaux apparaissent au centre de l’écran de l’appareil avec une incrustation le démarquant de votre application en arrière-plan. Ils sont parfaits pour suggérer plus ou moins subtilement à votre utilisateur de profiter d’une vente ou d’un concours.

![Message in-app modal apparaissant au centre d’une application et d’un site Web comme boîte de dialogue. La fenêtre modale comprend une image, un en-tête, le corps du message et deux boutons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Fullscreen %}

Comme leur nom l’indique, les messages plein écran occupent tout l’écran de l’appareil Ce type de message est idéal lorsque vous avez vraiment besoin de toute l’attention de votre utilisateur, dans le cas par exemple de mises à jour obligatoires de l’application.

![Message in-app plein écran sur un écran d’application. Le message en plein écran comprend une grande image, un en-tête, le corps du message et deux boutons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

En plus de ces modèles de messages par défaut, vous pouvez également personnaliser davantage votre envoi de messages à l'aide de messages in-app personnalisés, de fenêtres modales/boîtes de dialogue modales avec CSS ou de formulaires de capture d'e-mails Web. Pour plus d'informations, reportez-vous à la rubrique [Personnalisation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

## Modèles de messages in-app

Les messages in-app sont envoyés sous forme de messages in-app modélisés lorsque **l'option Réévaluer l'éligibilité à la campagne avant l'affichage** est sélectionnée ou si l'une des étiquettes Liquid suivantes est présente dans le message :

- `canvas_entry_properties`
- `connected_content`
- Les variables SMS telles que {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Cela signifie que lors du démarrage de la session, l'appareil recevra le déclencheur de ce message in-app au lieu du message complet. Lorsque l'utilisateur déclenche le message intégré à l'application, l'appareil de l'utilisateur effectuera une demande réseau pour récupérer le message réel.

{% alert note %}
Le message ne sera pas transmis si l'appareil n'a pas accès à Internet. Le message pourrait ne pas être transmis si la logique Liquid prend trop de temps à se résoudre.
{% endalert %}

## Comportement d'interruption

Chez Braze, un abandon se produit lorsqu'un utilisateur effectue une action qui le rend éligible à recevoir un message, mais qu'il ne reçoit pas ce message car la logique Liquid le marque comme non éligible. Par exemple :

1. Sam effectue une action qui devrait déclencher une campagne par e-mail.
2. Le corps de l'e-mail contient une logique Liquid qui indique que si le score d'un attribut personnalisé est inférieur à 50, cet e-mail ne doit pas être envoyé.
3. Le score de l'attribut personnalisé de Sam est de 20.
4. Braze identifie que Sam ne devrait pas recevoir cet e-mail, et l'envoi de l'e-mail est interrompu.
5. Un événement d'interruption est enregistré.

Cependant, étant donné que les messages in-app constituent un canal de communication passif, les interruptions fonctionnent de manière légèrement différente pour ceux-ci.

### Comportement d'interruption des messages in-app

Les messages in-app sont récupérés par l'appareil au début de la session et mis en cache sur l'appareil. Ainsi, quelle que soit la qualité de la connexion Internet, le message peut être transmis instantanément à l'utilisateur. Par exemple, si un utilisateur reçoit cinq messages in-app au cours de sa session, il recevra les cinq messages au début de la session. Les messages seront mis en cache localement et apparaîtront lorsque les événements déclencheurs définis se produiront (début de session, clic de l'utilisateur sur un bouton qui enregistre un événement personnalisé, ou autre).

En d'autres termes, la logique qui détermine si nous devons interrompre un message in-app intervient **avant que** le déclencheur ne se produise. Pour illustrer cela, supposons que Sam, dans l'exemple d'e-mail, soit abonné aux notifications push.

1. Sam commence une session en lançant une application Braze sur son téléphone.
2. En fonction des critères d'audience des campagnes actives dans l'espace de travail, Sam pourrait être éligible pour cinq campagnes différentes. Les cinq sont enregistrés sur leur téléphone et mis en cache.
3. Sam **n'a** effectué aucune action susceptible de déclencher ces messages, mais il pourrait les recevoir au cours de la session.
4. Le Liquid dans deux des messages in-app comporte des règles qui empêchent Sam de recevoir le message (par exemple, son attribut personnalisé de score n'est pas suffisamment élevé).
5. Sam ne reçoit pas les deux messages in-app qui les excluent, mais il reçoit les trois autres messages.
6. Aucun événement d'interruption n'est consigné.

Braze n'enregistre aucun événement d'abandon dans le cas de Sam, car cela ne correspond pas à notre définition d'un abandon ; Sam **n'a** effectué aucune action susceptible de déclencher ces messages. Pour les messages in-app, les utilisateurs n'effectuent jamais réellement l'action déclencheuse avant que Braze ne détermine qu'ils ne devraient pas voir le message.

#### Comportement d'interruption des messages in-app

[Les messages in-app](#templated-in-app-messages) forcent le SDK à réévaluer si un message doit s'afficher lorsque l'événement déclencheur se produit. Ceci présente un comportement d'interruption différent. Pour illustrer cela, examinons l'exemple suivant :

1. Sam commence une session Braze en lançant une application Braze sur son téléphone.
2. Les critères d'audience des campagnes actives indiquent que Sam pourrait être éligible pour recevoir un message in-app type. Par conséquent, les informations de déclencheur sont envoyées à son appareil sans la charge utile du message.
3. Sam sélectionne un bouton qui enregistre un événement personnalisé, déclenchant ainsi le message in-app type.
4. L'appareil de Sam effectue une requête réseau pour récupérer le message in-app.
5. La logique Liquid du message entraîne un abandon, Braze enregistre donc cela comme un abandon ; Sam a effectué l'action de déclenchement avant cette évaluation.

##### Comparaison du comportement d'interruption des messages in-app

Ce tableau compare les flux de messages in-app que Sam a rencontrés :

| Message in-app | Comportement d'interruption |
| --- | --- |
| Standard | Aucun événement d'interruption n'a été enregistré, car Sam n'a effectué aucune action susceptible de déclencher un message.<br><br>Les messages in-app standard n'enregistrent pas les abandons, car la définition d'un abandon est « n'avoir pas vu le message malgré l'exécution de l'action de déclenchement ». Étant donné que les messages in-app sont envoyés à l'appareil avant que les actions de déclenchement ne se produisent, il n'est pas pertinent de considérer que les messages in-app sont omis en raison de la logique Liquid. |
| Modèle | Un événement d'interruption a été enregistré car Sam a effectué l'action de déclenchement pour déclencher le message in-app, mais a reçu une interruption dans le modèle Liquid. <br><br>Les messages in-app basés sur des modèles sont interrompus car l'évaluation Liquid se produit après l'exécution de l'action de déclenchement. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Ressources supplémentaires

Avant de vous lancer dans la création de vos propres campagnes de messages in-app - ou dans l'utilisation de messages in-app dans le cadre d'une campagne multicanal - nous vous recommandons vivement de consulter notre [guide de préparation des messages in-app.]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/) Ce guide couvre les questions de ciblage, de contenu et de conversion que vous devez prendre en compte lors de la création de messages in-app.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}
