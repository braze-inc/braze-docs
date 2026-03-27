---
nav_title: "Tableau de bord de diagnostic de l'envoi de messages"
article_title: "Tableau de bord de diagnostic de l'envoi de messages"
description: "Cet article de référence traite du tableau de bord de diagnostic de l'envoi de messages, qui vous aide à comprendre pourquoi les messages de vos campagnes ou de vos Canvas n'ont pas été envoyés comme prévu."
alias: /ccdd/
page_order: 4.5
toc_headers: h2
---

# Tableau de bord de diagnostic de l'envoi de messages

> Le tableau de bord **Diagnostics de messagerie** fournit une analyse détaillée des résultats d'envoi de messages, vous permettant d'identifier les tendances et de diagnostiquer les problèmes potentiels dans votre configuration d'envoi de messages. Ce tableau de bord peut vous aider à comprendre pourquoi les messages de vos campagnes ou de vos Canvas n'ont pas été envoyés comme prévu.

{% alert important %}
Le tableau de bord **Messaging Diagnostics** est actuellement en accès anticipé. Contactez votre Customer Success Manager si vous souhaitez participer à l'accès anticipé.
{% endalert %}

## Concepts clés

### Envoyé et livré

Il est essentiel de comprendre que ce tableau de bord rend compte de la manière dont Braze a traité un message en interne, et non du statut final de distribution du message.

Un message marqué comme « envoyé » dans ce tableau de bord signifie que Braze l'a traité et expédié avec succès. Pour la plupart des canaux, cela signifie que Braze a transmis le message au partenaire tiers chargé de l'envoi. Cependant, cela ne garantit pas la distribution finale sur l'appareil de l'utilisateur. 

Lorsque Braze « envoie » un message, la distribution finale peut dépendre de services externes. Voici des exemples pour chaque canal.

| Canal | Exemple de distribution finale |
| --- | --- |
| Cartes de contenu | La carte a été envoyée et peut être consultée. |
| E-mail | Braze transmet le message à un fournisseur de services d'e-mailing (ESP). L'ESP est alors responsable de la distribution finale. Cet ESP peut par exemple signaler un « rebond » si l'adresse e-mail n'est pas valide ou si la boîte de réception est pleine. |
| Messages in-app | Le message a été présenté à l'utilisateur. |
| LINE | Le message a été transmis avec succès à un partenaire d'envoi. |
| Notification push | Braze transmet le message au service de notification push approprié (tel que le service Apple Push Notification pour iOS ou Firebase Cloud Messaging pour Android). Ce service est chargé de la distribution finale de la notification sur l'appareil. |
| SMS/MMS/RCS | Braze transmet le message à une passerelle SMS (telle que Twilio). Cette passerelle est responsable de la distribution finale à l'opérateur mobile. |
| Webhooks | La requête webhook a été effectuée avec succès et a renvoyé une réponse `2xx`. |
| WhatsApp | Le message a été transmis avec succès à un partenaire d'envoi. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

### Actualité des données

La fréquence de mise à jour des données de ce tableau de bord peut varier en fonction de la charge du système. Bien que la fréquence de mise à jour ne soit pas garantie, elle est généralement inférieure à une heure dans la plupart des cas.

## Configuration du tableau de bord

Vous pouvez accéder au tableau de bord de diagnostic en vous rendant dans **Analytics** > **Générateur de tableaux de bord** et en sélectionnant **Messaging Diagnostics** dans la liste des tableaux de bord créés par Braze.

Pour exécuter le tableau de bord et consulter vos données :

1. Choisissez **Campagnes** ou **Canvas** comme source pour vos rapports de tableau de bord. 
2. Sélectionnez une ou plusieurs campagnes ou Canvas.
3. Sélectionnez **Exécuter le tableau de bord** pour charger les données correspondant aux filtres sélectionnés.

![Exemple de diagnostic de campagne et de canvas du 25 au 31 mai 2025 pour une campagne de bienvenue.]({% image_buster /assets/img/campaign_canvas_dashboard_example.png %}){: style="max-width:90%;"}

## Interprétation des données

{% alert note %}
Le tableau de bord n'affiche que les données des 7 derniers jours. 
{% endalert %}

### Vignettes récapitulatives

En haut de la page, des vignettes récapitulatives pour la période sélectionnée indiquent :

- **Nombre total d'abandons :** Le nombre total de messages qui ont été abandonnés. Cela inclut les membres de l'audience du canvas qui n'y sont pas entrés ou qui en sont sortis en raison d'un échec à une étape, ou parce qu'ils répondaient aux critères de sortie lors de la réalisation d'un événement de sortie.
- **Envois de messages :** Le nombre total de messages que Braze a traités et envoyés avec succès. 
  - **E-mail, SMS/MMS/RCS, WhatsApp, LINE et notifications push :** Le message a été transmis avec succès à un partenaire d'envoi.  
  - **Webhooks :** La requête webhook a été effectuée avec succès et a renvoyé une réponse `2xx`.  
  - **Cartes de contenu :** La carte a été envoyée et peut être consultée.    
  - **Messages in-app :** Le message a été affiché à l'utilisateur.

### Résultats des messages au fil du temps

Ce graphique chronologique présente une ventilation quotidienne des différentes raisons pour lesquelles un message a été abandonné ou un utilisateur a été exclu d'un canvas. Ce graphique n'affiche pas le nombre d'envois.  

{% alert note %}
Pour garder le graphique lisible, toute raison d'abandon ou d'exclusion n'ayant eu aucune occurrence dans la période sélectionnée n'apparaît pas.
{% endalert %}

### Répartition des résultats des messages

Ce graphique présente la répartition de tous les résultats des messages au cours de la période sélectionnée. Il fournit une vue d'ensemble complète :
- Le nombre total d'envois en proportion de l'ensemble des résultats.  
- La répartition proportionnelle de chaque raison d'abandon et d'exclusion. Cela vous permet d'identifier rapidement les raisons les plus courantes pour lesquelles les messages ne sont pas envoyés.

### Résultats d'abandon

Les définitions suivantes expliquent les résultats d'abandon affichés sur le tableau de bord. Les résultats sont regroupés par catégorie afin de faciliter la recherche de celui qui vous intéresse.

#### Contenu et rendu

| Résultat de l'abandon | Explication |
| ---- | ---- |
| La carte de contenu a expiré | La carte de contenu a expiré avant que l'utilisateur ne puisse la consulter. |
| Carte de contenu non valide | La carte de contenu comportait des erreurs et n'a pas été envoyée à l'utilisateur. Parmi les raisons courantes : {::nomarkdown}<ul><li> Taille maximale dépassée (2 Ko) </li><li> La date d'expiration n'est pas valide </li><li> Le message contient des caractères non valides </li></ul>{:/} |
| Échec du contenu connecté | Braze a tenté d'envoyer le message, mais le contenu connecté a échoué après le nombre maximal de tentatives (cinq par défaut). **Remarque :** Ce nombre représente le nombre de messages abandonnés après avoir atteint le nombre maximal de tentatives, et non le nombre total de requêtes de contenu connecté ayant échoué. |
| Délai d'attente pour le rendu des messages in-app | Après plusieurs tentatives, le rendu du Liquid n'a pas pu être effectué et le délai d'attente a expiré. |
| Abandon Liquid | L'étiquette Liquid [abort_message]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) a été appelée, l'envoi a donc été annulé. |
| Délai d'attente pour le rendu Liquid | Le rendu du modèle Liquid a pris trop de temps. Cela se produit le plus souvent pour les bannières, les messages in-app et les e-mails. |
| Erreur de syntaxe Liquid | Le modèle Liquid a rencontré une erreur d'analyse, le message a donc été annulé. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### État de la campagne et du canvas

| Résultat de l'abandon | Explication |
| ---- | ---- |
| Échec de l'étape de délai | L'[étape de délai]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) a échoué, ce qui a conduit l'utilisateur à quitter le canvas. Cet échec peut survenir lorsque : {::nomarkdown}<ul><li> La variable fournie à l'étape de délai personnalisé était vide ou de type non valide </li><li> Le délai dépasse la durée maximale autorisée dans le canvas</li></ul>{:/} |
| Événement d'exception ou de sortie | L'utilisateur était auparavant éligible pour recevoir le message, mais soit {::nomarkdown}<ul><li> a effectué un <a href="/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#step-3-select-exception-events">événement d'exception</a> pour une campagne basée sur une action, de sorte que le message a été abandonné, soit </li><li> répondait aux <a href="/docs/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/#setting-up-exit-criteria">critères de sortie</a> du canvas et a donc été exclu en cours de parcours.</li></ul>{:/} |
| Campagne inactive | La campagne a été arrêtée alors que le message était en cours d'envoi, il a donc été abandonné. |
| Canvas inactif | Le canvas a été arrêté avant que l'utilisateur n'entame son parcours. |
| Étape du canvas inactive | Cela peut se produire dans le canvas si : {::nomarkdown}<ul><li> L'étape du canvas a été supprimée </li> <li>Le canvas a été arrêté, ce qui a entraîné la désactivation de toutes les étapes </li></ul>{:/} |
| Volume limité | La campagne a atteint la limite de volume définie, l'envoi a donc été annulé. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Limite de débit et timing

| Résultat de l'abandon | Explication |
| ---- | ---- |
| Limite de fréquence atteinte | L'utilisateur a déjà reçu le nombre maximal de messages autorisé par les règles de [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#about-frequency-capping) de votre espace de travail, l'envoi a donc été annulé. |
| Abandon pour heures calmes | La fonctionnalité « Heures calmes » était activée pour la campagne ou l'étape du canvas, avec le paramètre de repli défini sur **Abandonner le message**. L'utilisateur a déclenché la campagne ou est entré dans l'étape Message du canvas pendant les heures calmes, ce qui a entraîné l'abandon du message. Cependant, cela n'exclut pas l'utilisateur du canvas. |
| Limite de débit dépassée sur 72 heures | Le message a été bloqué pendant plus de 72 heures en raison des [limites de débit de distribution]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting), l'envoi a donc été abandonné. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Éligibilité et profil utilisateur

| Résultat de l'abandon | Explication |
| ---- | ---- |
| Identifiant utilisateur en double | Plusieurs utilisateurs présentant un identifiant correspondant (tel qu'un ID externe, une adresse e-mail ou un numéro de téléphone) étaient éligibles pour recevoir ce message. Afin d'éviter tout envoi en double au même utilisateur, ce message a été abandonné. |
| L'utilisateur n'a pas réussi la pré-vérification pour l'étape Message | Cette pré-vérification est effectuée avant les validations de distribution. Dans ce cas, l'utilisateur n'a pas satisfait aux conditions préalables requises pour cette étape Message (utilisateur introuvable ou non éligible pour le canal de l'étape Message). **Remarque :** Pour une étape Message multicanal, cela signifie que l'utilisateur n'a pas été trouvé ; l'éligibilité du canal n'est vérifiée ici que pour les étapes Message monocanal. |
| L'utilisateur n'a pas réussi la pré-vérification pour le message déclenché | Pour un message déclenché, Braze effectue une première série de vérifications préliminaires concernant l'éligibilité de l'audience, la rééligibilité et l'éligibilité du canal avant de créer un message à envoyer à partir de ce déclencheur. |
| Utilisateur n'étant plus éligible | L'utilisateur faisait initialement partie de l'audience cible, mais ne répondait plus aux critères d'audience avant que Braze n'envoie le message ou n'inscrive l'utilisateur dans le canvas. Le délai entre le moment où l'utilisateur répond initialement aux critères d'audience et celui où il n'y répond plus peut être dû à : {::nomarkdown}<ul><li>Timing intelligent</li><li>Heures calmes</li><li>Heure locale</li><li>Limites de débit de distribution (non applicable pour les entrées dans le canvas)</li><li>Retards dans le pipeline d'envoi de messages</li></ul>{:/} |
| Utilisateur non éligible pour cette étape | L'utilisateur a quitté le canvas parce qu'il ne répondait pas aux [validations de distribution]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#delivery-validations) définies pour l'étape Message ou parce qu'il figurait sur une [liste de suppression]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists). |
| Utilisateur non rééligible | L'utilisateur était autorisé à recevoir le message ou à entrer dans le canvas, mais l'envoi a été annulé en raison des paramètres de rééligibilité ou de réentrée. Cela peut se produire si l'utilisateur a déjà reçu la campagne ou est entré dans le canvas trop récemment, si un autre envoi pour la même campagne est déjà en cours pour cet utilisateur, ou si la rééligibilité ou la réentrée est désactivée. |
| Profil utilisateur introuvable | L'utilisateur n'a jamais existé ou n'existe plus dans Braze. Voici quelques cas courants : {::nomarkdown}<ul><li> L'utilisateur a été ciblé via l'envoi de messages par API, mais n'a jamais existé dans Braze. </li><li>L'utilisateur a été supprimé avant l'envoi du message ou l'exécution de l'étape du canvas. </li><li>L'utilisateur a été fusionné avec un autre profil avant l'envoi du message.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Canal et distribution

| Résultat de l'abandon | Explication |
| ---- | ---- |
| Délai d'attente de distribution par le partenaire | Braze a tenté d'envoyer ce message à votre partenaire de distribution pendant 24 heures, mais celui-ci a renvoyé des erreurs temporaires pendant toute cette période. |
| Identifiants push non valides | Les [identifiants push]({{site.baseurl}}/user_guide/message_building_by_channel/push/troubleshooting/#valid-push-token) pour cette application sont manquants ou non valides, l'envoi a donc été annulé. Mettez à jour vos identifiants dans **Paramètres de l'application**. |
| Utilisateur non activé pour les notifications push Android, l'application ou l'appareil | Il n'est pas possible d'envoyer de notification push à cet utilisateur. Quelques raisons courantes : {::nomarkdown}<ul><li> L'utilisateur n'a pas installé l'application.</li> <li> L'utilisateur ne dispose pas d'un jeton de notification push valide. </li> <li>L'utilisateur ne dispose pas de l'appareil requis pour recevoir cette notification push. </li> <li> L'utilisateur a désactivé les notifications pour cette application dans les paramètres de son appareil. </li> <li> L'utilisateur n'est pas abonné ou n'a pas choisi de recevoir des notifications push.</li></ul>{:/} |
| Utilisateur non activé pour les notifications push iOS, l'application ou l'appareil | Identique au résultat « Utilisateur non activé pour les notifications push Android, l'application ou l'appareil ». |
| Utilisateur non activé pour les notifications push Kindle, l'application ou l'appareil | Identique au résultat « Utilisateur non activé pour les notifications push Android, l'application ou l'appareil ». |
| Utilisateur non activé pour les notifications push Web, l'application ou l'appareil | Identique au résultat « Utilisateur non activé pour les notifications push Android, l'application ou l'appareil ». |
| Utilisateur non activé pour les cartes de contenu | L'utilisateur n'a utilisé aucune application incluant cette carte de contenu. |
| Utilisateur non activé pour l'e-mail | Il n'est pas possible d'envoyer des e-mails à cet utilisateur. Quelques raisons courantes : {::nomarkdown}<ul><li> L'utilisateur ne dispose pas d'adresse e-mail dans son profil utilisateur. </li><li> L'état d'abonnement de l'utilisateur l'empêche de recevoir cet e-mail. </li><li> L'adresse e-mail de l'utilisateur a déjà été marquée comme non valide (échec d'envoi définitif). </li><li> Les messages envoyés à cette adresse e-mail sont systématiquement marqués comme spam, l'envoi a donc été annulé.</li></ul>{:/} |
| Utilisateur non activé pour LINE | Il n'est pas possible d'envoyer des messages LINE à cet utilisateur. Quelques raisons courantes : {::nomarkdown}<ul><li> L'utilisateur n'a pas de numéro de téléphone dans son profil utilisateur. </li><li> Le numéro de téléphone de l'utilisateur a été marqué comme non valide en raison d'échecs de distribution. </li><li> L'état d'abonnement de l'utilisateur l'empêche de recevoir ce message. </li><li> L'utilisateur ne dispose pas d'un ID LINE.</li></ul>{:/} |
| Utilisateur non activé pour les SMS/MMS/RCS | Il n'est pas possible d'envoyer des messages SMS à cet utilisateur. Quelques raisons courantes : {::nomarkdown}<ul><li> L'utilisateur n'a pas de numéro de téléphone dans son profil utilisateur. </li><li> Le numéro de téléphone de l'utilisateur a été marqué comme non valide en raison d'échecs de distribution. </li><li> Le numéro de téléphone de l'utilisateur n'est pas dans un format E.164 valide et les tentatives de mise en forme automatique du numéro ont échoué. </li><li> L'état d'abonnement de l'utilisateur l'empêche de recevoir le message SMS.</li><li>Le numéro de téléphone de l'utilisateur se trouve dans un pays bloqué.</li></ul>{:/} |
| Utilisateur non activé pour WhatsApp | Il n'est pas possible d'envoyer des messages WhatsApp à cet utilisateur. Quelques raisons courantes : {::nomarkdown}<ul><li> L'utilisateur n'a pas de numéro de téléphone dans son profil utilisateur. </li><li> Le numéro de téléphone de l'utilisateur a été marqué comme non valide en raison d'échecs de distribution. </li><li> L'état d'abonnement de l'utilisateur l'empêche de recevoir ce message. </li><li> L'utilisateur ne dispose pas d'un compte WhatsApp.</li></ul>{:/} |
| Échec du webhook | Le webhook a reçu un code de réponse non réussi (non-`2xx`). Consultez le [journal des activités des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab#dev-console-troubleshooting) pour plus de détails. Les journaux datant de plus de 60 heures sont supprimés et ne sont plus accessibles ; les erreurs de webhook sont échantillonnées jusqu'à 20 journaux par heure. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Foire aux questions

### Que signifie un échec de « pré-vérification » ?

Une « pré-vérification » désigne une vérification de validation groupée à grande vitesse qui s'exécute au tout début d'une étape du pipeline (par exemple, le déclenchement d'un message ou l'envoi d'une étape Message du canvas). Considérez cela comme une sortie anticipée conçue pour une vitesse maximale. Au lieu d'effectuer de nombreuses vérifications distinctes et gourmandes en ressources (comme la validation de chaque détail du profil utilisateur), Braze regroupe plusieurs validations de base en une seule « première passe ».

Si un utilisateur échoue à cette vérification groupée, il est immédiatement exclu. Cette approche groupée permet à Braze de traiter des volumes considérables de messages à grande vitesse et contribue à améliorer la rapidité et la stabilité de vos campagnes et Canvas en réduisant le temps de traitement de chaque message.

### Que signifie un résultat d'abandon « autre » ?

Il s'agit d'abandons qui ne correspondent à aucune des catégories prédéfinies de Braze. Si vous constatez une proportion importante d'abandons avec ce résultat, contactez l'[assistance Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support) pour obtenir de l'aide.

### Pourquoi la somme du _nombre total d'abandons_ et des _envois de messages_ est-elle inférieure à la taille d'audience attendue ?

Cela peut se produire pour plusieurs raisons :

- **Critères d'audience :** Il est possible que moins d'utilisateurs que prévu aient répondu aux critères d'audience (par exemple, ils n'appartenaient pas au segment ou ne présentaient pas les attributs requis) lors du lancement de la campagne ou du canvas.
- **Traitement en cours :** Les messages sont peut-être encore en cours de traitement. Des utilisateurs peuvent se trouver encore dans les premières étapes du canvas et ne pas avoir atteint les étapes Message.
- **Actualité des données :** Les données du tableau de bord sont mises à jour environ toutes les 15 minutes, mais cela n'est pas garanti. Les données les plus récentes pour cette campagne ou ce canvas n'ont peut-être pas encore été transmises au tableau de bord.
- **Cas limites :** Il est possible que vous rencontriez un cas particulier qui n'est pas pris en compte dans ce tableau de bord pour le moment. Si vous pensez que c'est le cas, contactez l'[assistance Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support).

### Pourquoi la somme du _nombre total d'abandons_ et des _envois de messages_ est-elle supérieure à l'audience d'une campagne ou d'un canvas ?

Cela peut se produire pour les raisons suivantes :

- **Messages multicanaux :** La campagne ou l'étape du canvas a été configurée pour envoyer sur plusieurs canaux (tels que les SMS et les e-mails). Un même utilisateur peut recevoir un résultat « envoyé » pour un canal (tel que l'e-mail) et un résultat « abandonné » pour un autre (tel que « Utilisateur non activé pour les SMS/MMS/RCS »). Dans ce cas, cet utilisateur serait compté deux fois dans le graphique : une fois comme « envoyé » et une fois comme « abandonné ».
  - **Exemple :** Vous envoyez une campagne push à 100 utilisateurs, ciblant à la fois iOS et Android. Si un utilisateur ne dispose que d'un appareil iOS, il reçoit la notification push iOS (« envoyée »), mais déclenche également un abandon pour la notification push Android (« Utilisateur non activé pour les notifications push Android, l'application ou l'appareil »).
- **Étapes Message multiples (Canvas uniquement) :** Votre canvas peut comporter plusieurs étapes Message dans un parcours donné. Ce tableau de bord regroupe tous les résultats, de sorte qu'un même utilisateur peut être compté plusieurs fois s'il passe par plusieurs étapes Message au cours de la période sélectionnée.
- **Messages de test :** L'envoi de tests (comptabilisé dans le tableau de bord) fait augmenter le total par rapport à la taille de l'audience.