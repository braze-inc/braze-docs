---
nav_title: "Tableau de bord de diagnostic de l'envoi de messages"
article_title: "Tableau de bord de diagnostic de l'envoi de messages"
description: "Cet article de référence traite du tableau de bord de diagnostic de l'envoi de messages, qui vous aide à comprendre pourquoi les messages de vos campagnes ou de vos Canvases n'ont pas été envoyés comme prévu."
alias: /ccdd/
page_order: 4.5
---

# Tableau de bord de diagnostic de l'envoi de messages

> Le tableau de bord **Diagnostics de messagerie** fournit une analyse détaillée des résultats d'envoi de messages, vous permettant ainsi d'identifier les tendances et de diagnostiquer les problèmes potentiels dans votre configuration de messagerie. Ce tableau de bord peut vous aider à comprendre pourquoi les messages de vos campagnes ou de vos Canvases n'ont pas été envoyés comme prévu.

{% alert important %}
Le tableau de bord **Messaging Diagnostics** est actuellement en accès anticipé. Veuillez contacter votre gestionnaire de la satisfaction client si vous souhaitez participer à l'accès anticipé.
{% endalert %}

## Concepts clés

### Envoyé et livré

Il est essentiel de comprendre que ce tableau de bord rend compte de la manière dont Braze a traité un message en interne, et non du statut final de réception/distribution du message.

Un message marqué comme « envoyé » dans ce tableau de bord signifie que Braze a traité et envoyé le message avec succès. Pour la plupart des canaux, cela signifie que Braze a transmis le message au partenaire tiers concerné chargé de l'envoi. Cependant, cela ne garantit pas la réception/distribution finale sur l'appareil de l'utilisateur. 

Lorsque Braze « envoie » un message, la réception/distribution finale peut dépendre de services externes. Veuillez examiner les exemples suivants pour chaque canal.

| Canal | Exemple de réception/distribution finale |
| --- | --- |
| Cartes de contenu | La carte a été envoyée et peut être consultée. |
| E-mail | Braze transmet le message à un fournisseur de services d'e-mailing. L'ESP est alors responsable de la réception/distribution finale. Cet ESP, par exemple, peut signaler un « rebond » si l'adresse d'e-mail n'est pas valide ou si la boîte de réception est pleine. |
| in-app Messages | Le message a été présenté à l'utilisateur. |
| LINE | Le message a été transmis avec succès à un partenaire expéditeur. |
| Notification push | Braze transmet le message au service de notification push approprié (tel que le service Apple Push Notification pour iOS ou Firebase Cloud Messaging pour Android). Ce service est chargé de la réception/distribution finale de la notification à l'appareil. |
| SMS/MMS/RCS | Braze transmet le message à une passerelle SMS (telle que Twilio). Cette passerelle est responsable de la réception/distribution finale à l'opérateur mobile. |
| Webhooks | La requête webhook a été effectuée avec succès et a renvoyé une`2xx`réponse. |
| WhatsApp | Le message a été transmis avec succès à un partenaire expéditeur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

### Actualité des données

La fréquence de mise à jour des données de ce tableau de bord peut varier en fonction de la charge du système. Bien que la fréquence des mises à jour ne soit pas garantie, elle est généralement inférieure à une heure dans la plupart des cas.

## Configuration du tableau de bord

Vous pouvez accéder au tableau de bord de diagnostic en vous rendant dans **Analytics** > **Générateur de tableaux de bord** et en sélectionnant **Messaging Diagnostics** dans la liste des tableaux de bord créés par Braze.

Pour exécuter le tableau de bord et consulter vos données :

1. Veuillez sélectionner **Campagnes** ou **Canvases** comme source pour vos rapports de tableau de bord. 
2. Veuillez sélectionner une ou plusieurs campagnes ou canevas.
3. Veuillez sélectionner **« Exécuter le tableau de bord** » pour charger les données correspondant aux filtres que vous avez sélectionnés.

![Exemple de diagnostic de campagne et de canvas du 25 au 31 mai 2025 pour une campagne de bienvenue.]({% image_buster /assets/img/campaign_canvas_dashboard_example.png %}){: style="max-width:90%;"}

## Interprétation des données

{% alert note %}
Le tableau de bord n'affiche que les données des 7 derniers jours.
{% endalert %}

### Résumé

En haut de la page, vous trouverez des vignettes récapitulatives pour la période sélectionnée, qui indiquent :

- **Nombre total d'interruptions :** Nombre total de messages qui ont été interrompus. Cela inclut les membres de l'audience Canvas qui n'ont pas accédé à Canvas ou qui ont quitté Canvas en raison d'un échec à une étape du canvas ou parce qu'ils répondaient aux critères de sortie lors de la réalisation d'un événement de sortie.
- **Envoi de messages :** Nombre total de messages que Braze a traités et envoyés avec succès. 
  - **E-mail, SMS/MMS/RCS, WhatsApp, LINE et notifications push :** Le message a été transmis avec succès à un partenaire expéditeur.  
  - **Webhooks :** La requête webhook a été effectuée avec succès et a renvoyé une`2xx`réponse.  
  - **Cartes de contenu (Content cards) :** La carte a été envoyée et peut être consultée.    
  - **Messages in-app :** Le message a été affiché à l'utilisateur.

### Résultats des messages au fil du temps

Ce graphique chronologique présente une ventilation quotidienne des différentes raisons pour lesquelles un message a été interrompu ou un utilisateur a été exclu d'un canvas. Ce graphique n'affiche pas le nombre d'envois.  

{% alert note %}
Afin de maintenir l'organisation du graphique, toute raison d'interruption ou d'abandon n'ayant pas eu lieu dans la période sélectionnée n'apparaît pas sur le graphique.
{% endalert %}

### Analyse des résultats des messages

Ce graphique présente la répartition de tous les résultats des messages au cours de la période sélectionnée. Il fournit une vue d'ensemble complète de :
- Le nombre total d'envois en proportion de tous les résultats.  
- Répartition proportionnelle des raisons d'abandon et de perte. Cela vous permet d'identifier rapidement les raisons les plus courantes pour lesquelles les messages ne sont pas envoyés.

### Résultats d'interruption de grossesse

Les définitions suivantes expliquent les résultats d'interruption affichés sur le tableau de bord. Les résultats sont regroupés par catégorie afin de faciliter la recherche de celui qui vous intéresse.

#### Contenu et rendu

| Résultat de l'interruption | Explication |
| ---- | ---- |
| La carte de contenu a expiré | La carte de contenu a expiré avant que l'utilisateur ne puisse la consulter. |
| Carte de contenu non valide | La carte de contenu comportait des erreurs et n'a pas été envoyée à l'utilisateur. Parmi les raisons courantes, on peut citer : {::nomarkdown}<ul><li> Taille maximale dépassée (2 Ko) </li><li> La date d'expiration n'est pas valide. </li><li> Le message contient des caractères non valides. </li></ul>{:/} |
| Échec du contenu connecté | Braze a tenté d'envoyer le message, mais le contenu connecté a échoué après avoir atteint le nombre maximal de tentatives (cinq par défaut). |
| Délai d'attente pour l'affichage des messages in-app | Après plusieurs tentatives, le rendu du Liquid n'a pas pu être effectué et le délai d'attente a expiré. |
| Interruption de grossesse par voie liquide | L'étiquette[abort_message]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages)Liquid a été appelée, donc l'envoi a été annulé. |
| Délai d'attente pour le rendu des liquides | Le rendu du modèle Liquid a pris beaucoup de temps. Plus susceptible de se produire pour les bannières, les messages in-app et les e-mails. |
| \### Erreurs de syntaxe Liquid | Le modèle Liquid a rencontré une erreur d'analyse, par conséquent le message a été annulé. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### État de la campagne et du porte-à-porte

| Résultat de l'interruption | Explication |
| ---- | ---- |
| Défaillance de l'étape de retard | L'[étape]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) [Delay]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) a échoué, ce qui a conduit l'utilisateur à quitter le Canvas. Cette défaillance peut survenir lorsque : {::nomarkdown}<ul><li> La variable fournie à l'étape de délai de personnalisation était vide ou de type non valide. </li><li> Le délai a dépassé la durée maximale autorisée dans le cadre du programme Canvas.</li></ul>{:/} |
| Exception ou événement de sortie | L'utilisateur était auparavant éligible pour recevoir le message, mais soit {::nomarkdown}<ul><li> a effectué un <a href="/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#step-3-select-exception-events">événement d'exception</a> pour une campagne basée sur une action, de sorte que le message a été interrompu, ou </li><li> répondaient aux <a href="/docs/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/#setting-up-exit-criteria">critères de sortie</a> de canvas et ont donc été retirés en cours de route.</li></ul>{:/} |
| Campagne inactive | La campagne a été interrompue alors que le message était en cours d'envoi, elle a donc été annulée. |
| Inactive Canvas | Le canvas a été interrompu avant que l'utilisateur n'entame son parcours. |
| Étape du canvas « Inactif » | Cela peut se produire dans Canvas si : {::nomarkdown}<ul><li> L'étape du canvas a été supprimée. </li> <li>Le Canvas a été interrompu, ce qui a entraîné la désactivation de toutes les étapes. </li></ul>{:/} |
| Volume limité | La campagne a atteint la limite de volume définie, par conséquent l'envoi a été annulé. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Limite de débit et synchronisation

| Résultat de l'interruption | Explication |
| ---- | ---- |
| Fréquence limitée | L'utilisateur a déjà reçu le nombre maximal de messages autorisé par les règles [de limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#about-frequency-capping) de votre espace de travail, l'envoi a donc été annulé. |
| Heures calmes interrompues | La fonctionnalité « Heures calmes » a été activée pour la campagne ou l'étape du canvas, avec le **message « Abandonner** » défini comme solution de repli. L'utilisateur a déclenché la campagne ou est entré dans l'étape du canvas pendant les heures calmes, ce qui a entraîné l'interruption du message. Cependant, cela ne permet pas à l'utilisateur de quitter Canvas. |
| Limite de débit sur 72 heures | Le message a été bloqué pendant plus de 72 heures en raison de [limites de débit pour la réception/distribution]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting), et l'envoi a donc été interrompu. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Admissibilité et profil utilisateur

| Résultat de l'interruption | Explication |
| ---- | ---- |
| Identifiant utilisateur en double | Plusieurs utilisateurs présentant un identifiant correspondant (tel qu'un ID externe, une adresse de e-mail ou un numéro de téléphone) étaient éligibles pour recevoir ce message. Afin d'éviter tout envoi en double au même utilisateur, ce message a été annulé. |
| L'utilisateur n'a pas réussi la vérification préalable pour l'étape Message. | Cette vérification préalable est effectuée avant les validations de réception/distribution. Dans ce cas, l'utilisateur n'a pas satisfait aux conditions préalables requises pour cette étape du message (utilisateur introuvable ou non éligible pour le canal de communication de l'étape du message). **Remarque :** Pour une étape Message multicanal, cela signifie que l'utilisateur n'a pas été identifié ; l'éligibilité du canal n'est vérifiée ici que pour les étapes Message monocanal. |
| L'utilisateur n'a pas réussi la vérification préalable pour le message déclenché. | Pour un message déclenché, Braze effectue une première série de vérifications préliminaires de base concernant l'éligibilité de l'audience, la rééligibilité et l'éligibilité du canal avant de créer un message à envoyer à partir de ce déclencheur. |
| Utilisateur n'étant plus admissible | L'utilisateur faisait initialement partie du public cible, mais ne répondait plus aux critères d'audience avant que Braze n'envoie le message ou n'inscrive l'utilisateur dans Canvas. Le délai entre le moment où l'utilisateur répond initialement aux critères d'audience et celui où il n'en fait plus partie peut être dû à des retards liés à : {::nomarkdown}<ul><li>Timing intelligent</li><li>Heures calmes</li><li>Heure locale</li><li>Limites de débit de réception/distribution (non applicable pour les entrées Canvas)</li><li>Retards dans le pipeline d'envoi de messages</li></ul>{:/} |
| Utilisateur non éligible pour cette étape | L'utilisateur a quitté le Canvas parce qu'il ne répondait pas aux [validations de réception/distribution]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#delivery-validations) définies pour l'étape du message ou parce qu'il figurait sur une [liste de suppression.]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists) |
| Utilisateur non rééligible | L'utilisateur était autorisé à recevoir le message ou à accéder à Canvas, mais l'envoi a été annulé en raison des paramètres de réadmissibilité ou de réadmission. Cela peut se produire si l'utilisateur a déjà reçu la campagne ou s'est connecté à canvas trop récemment, si un autre envoi pour la même campagne est déjà en cours pour cet utilisateur, ou si la rééligibilité ou la réinscription est désactivée. |
| Profil utilisateur introuvable | L'utilisateur n'a jamais existé ou n'existe plus dans Braze. Voici quelques cas courants : {::nomarkdown}<ul><li> L'utilisateur a été ciblé à l'aide de l'envoi de messages API, mais n'a jamais existé dans Braze. </li><li>L'utilisateur a été supprimé avant l'envoi du message ou l'exécution de l'étape du canvas. </li><li>L'utilisateur a été fusionné avec un autre profil utilisateur avant l'envoi du message.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Canal et réception/distribution

| Résultat de l'interruption | Explication |
| ---- | ---- |
| Délai d'attente pour la réception/distribution par le partenaire | Braze a tenté d'envoyer ce message à votre partenaire de réception/distribution pendant 24 heures, mais celui-ci a renvoyé des erreurs temporaires pendant toute cette période. |
| Les informations d'identification de poussée ne sont pas valides | Les [informations d'identification de poussée]({{site.baseurl}}/user_guide/message_building_by_channel/push/troubleshooting/#valid-push-token) pour cette application sont manquantes ou non valides, par conséquent l'envoi a été annulé. Veuillez mettre à jour vos informations d'identification dans **les paramètres de l'application**. |
| Utilisateur non autorisé pour les notifications push Android, l'application ou l'appareil | Il n'est pas possible d'envoyer de notification à cet utilisateur. Quelques raisons courantes : {::nomarkdown}<ul><li> L'utilisateur n'a pas installé l'application.</li> <li> L'utilisateur ne dispose pas d'un jeton push valide. </li> <li>L'utilisateur ne dispose pas de l'appareil requis pour recevoir cette notification push. </li> <li> L'utilisateur a désactivé les notifications pour cette application dans les paramètres de son appareil. </li> <li> L'utilisateur n'est pas abonné ou n'a pas choisi de recevoir des notifications push.</li></ul>{:/} |
| Utilisateur non autorisé pour les notifications push iOS, l'application ou l'appareil | Identique à « Utilisateur non activé pour les notifications push Android, l'application ou l'appareil » (voir ci-dessus). |
| Utilisateur non autorisé pour Kindle Push, l'application ou l'appareil | Identique à « Utilisateur non activé pour les notifications push Android, l'application ou l'appareil » (voir ci-dessus). |
| Utilisateur non autorisé pour les notifications push Web, l'application ou l'appareil | Identique à « Utilisateur non activé pour les notifications push Android, l'application ou l'appareil » (voir ci-dessus). |
| Utilisateur non autorisé pour les cartes de contenu | L'utilisateur n'a utilisé aucune application incluant cette carte de contenu. |
| Utilisateur non autorisé à recevoir des e-mails | Il n'est pas possible d'envoyer des e-mails à cet utilisateur. Quelques raisons courantes : {::nomarkdown}<ul><li> L'utilisateur ne dispose pas d'adresse e-mail dans son profil utilisateur. </li><li> L'état d'abonnement de l'utilisateur l'empêche de recevoir cet e-mail. </li><li> L'adresse e-mail de l'utilisateur a déjà été marquée comme non valide (échec d'envoi définitif). </li><li> Les messages envoyés à cette adresse de e-mail sont systématiquement marqués comme spam, par conséquent l'envoi a été annulé.</li></ul>{:/} |
| Utilisateur non autorisé pour LINE | Il n'est pas possible d'envoyer des messages LINE à cet utilisateur. Quelques raisons courantes : {::nomarkdown}<ul><li> L'utilisateur n'a pas de numéro de téléphone dans son profil utilisateur. </li><li> Le numéro de téléphone de l'utilisateur a été marqué comme non valide en raison d'échecs de réception/distribution. </li><li> L'état d'abonnement de l'utilisateur l'empêche de recevoir ce message. </li><li> L'utilisateur ne dispose pas d'un ID LINE.</li></ul>{:/} |
| Utilisateur non autorisé pour les SMS/MMS/RCS | Il n'est pas possible d'envoyer des messages SMS à cet utilisateur. Quelques raisons courantes : {::nomarkdown}<ul><li> L'utilisateur n'a pas de numéro de téléphone dans son profil utilisateur. </li><li> Le numéro de téléphone de l'utilisateur a été marqué comme non valide en raison d'échecs de réception/distribution. </li><li> Le numéro de téléphone de l'utilisateur n'est pas dans un formatE.164 valide et les tentatives de mise en forme automatique du numéro ont échoué. </li><li> L'état d'abonnement de l'utilisateur l'empêche de recevoir le message SMS.</li><li>Le numéro de téléphone de l'utilisateur se trouve dans un pays bloqué.</li></ul>{:/} |
| Utilisateur non autorisé pour WhatsApp | Il n'est pas possible d'envoyer des messages WhatsApp à cet utilisateur. Quelques raisons courantes : {::nomarkdown}<ul><li> L'utilisateur n'a pas de numéro de téléphone dans son profil utilisateur. </li><li> Le numéro de téléphone de l'utilisateur a été marqué comme non valide en raison d'échecs de réception/distribution. </li><li> L'état d'abonnement de l'utilisateur l'empêche de recevoir ce message. </li><li> L'utilisateur ne dispose pas d'un compte WhatsApp.</li></ul>{:/} |
| Échec du webhook | Le webhook a reçu un code de réponse non réussi (non `2xx`). Veuillez consulter le [journal des activités des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab#dev-console-troubleshooting) pour plus de détails. Les journaux datant de plus de 60 heures sont supprimés et ne sont plus accessibles ; les erreurs de webhook sont échantillonnées jusqu'à 20 journaux par heure. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Foire aux questions

### Que signifie un échec au « pré-contrôle » ?

Une « pré-vérification » désigne une vérification de validation groupée à grande vitesse qui s'exécute au tout début d'une étape du pipeline (par exemple, le déclenchement d'un message ou l'envoi d'une étape du canvas). Considérez cela comme une sortie anticipée conçue pour une vitesse maximale. Au lieu d'effectuer de nombreuses vérifications distinctes et gourmandes en ressources (comme la validation de chaque détail du profil utilisateur), Braze regroupe plusieurs validations de base en une seule « première passe ».

Si un utilisateur échoue à cette vérification unique, il est immédiatement exclu. Cette approche groupée permet à Braze de traiter des volumes considérables de messages à grande vitesse et peut contribuer à améliorer la rapidité et la stabilité de vos campagnes et de vos Canvases en réduisant le temps de traitement de chaque message.

### Pourquoi la somme des _abandons totaux_ et _des envois de messages_ est-elle inférieure à la taille d'audience que j'avais prévue ?

Cela peut se produire pour plusieurs raisons :

- **Critères d'audience :** Il est possible que moins d'utilisateurs que prévu aient répondu aux critères d'audience (par exemple, ils n'appartenaient pas au segment ou ne présentaient pas les attributs requis) lors du lancement de la campagne ou du canvas.
- **Traitement en cours :** Les messages sont peut-être encore en cours de traitement. Il est possible que les utilisateurs se trouvent encore dans les premières étapes du Canvas et n'aient pas encore atteint les étapes relatives aux messages.
- **Actualité des données :** Les données du tableau de bord sont mises à jour toutes les 15 minutes environ, mais cela n'est pas garanti. Les données les plus récentes pour cette campagne ou ce canvas n'ont peut-être pas encore été transmises au tableau de bord.
- **Cas limites :** Il est possible que vous rencontriez un cas particulier qui n'est pas pris en compte dans ce tableau de bord pour le moment. Si vous pensez que c'est le cas, veuillez contacter [le service d'assistance Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support).

### Pourquoi la somme des _abandons totaux_ et _des envois de messages_ est-elle supérieure à l'audience d'une campagne et de Canvas ?

Cela peut se produire pour les raisons suivantes :

- **Messages multicanaux :** La campagne ou l'étape du canvas a été configurée pour être envoyée sur plusieurs canaux (tels que les SMS et les e-mails). Un utilisateur unique peut recevoir un résultat « envoyé » pour un canal (tel que l'e-mail) et un résultat « abandonné » pour un autre (tel que « Utilisateur non autorisé pour les SMS/MMS/RCS »). Dans ce cas, cet utilisateur serait compté deux fois dans le tableau : une fois comme « envoyé » et une fois comme « abandonné ».
  - **Exemple :** Vous envoyez une campagne push à 100 utilisateurs, avec un ciblage sur iOS et Android. Si un utilisateur ne dispose que d'un appareil iOS, il reçoit la notification push iOS (« envoyée »), mais déclenche également un déclencheur pour la notification push Android (« Utilisateur non activé pour la notification push, l'application ou l'appareil Android »).
- **Étapes de messages multiples (Canvas uniquement) :** Votre Canvas peut comporter plusieurs étapes de message dans un chemin donné. Ce tableau de bord regroupe tous les résultats, de sorte qu'un même utilisateur peut être compté plusieurs fois s'il passe par plusieurs étapes d'envoi de messages au cours de la période sélectionnée.
- **Messages de test :** L'envoi de tests (qui est comptabilisé dans le tableau de bord) augmente le nombre total de messages envoyés par rapport à la taille de l'audience. 
