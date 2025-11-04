---
nav_title: FAQ
article_title: FAQ SUR LES SMS
page_order: 12
description: "Cet article aborde certaines des questions les plus fréquemment posées lors de l'implémentation des campagnes SMS."
page_type: FAQ
alias: /sms_faq/
channel:
  - SMS
  
---

# Questions fréquemment posées

> Sur cette page, nous tenterons de répondre à vos questions les plus pointues sur le SMS !

### Pouvez-vous inclure des liens dans un SMS ?

Vous pouvez inclure n'importe quel lien dans n'importe quelle campagne SMS. Cependant, il y a quelques préoccupations à prendre en compte :

- Les liens peuvent occuper une grande partie de la limite de 160 caractères pour les SMS. Si vous incluez un lien et un texte, il se peut que vous receviez deux messages SMS au lieu d'un seul.
- Les entreprises utilisent souvent des raccourcisseurs de liens pour limiter l'impact du nombre de caractères d'un lien. Toutefois, si vous envoyez un lien raccourci par le biais d'un code long, les opérateurs peuvent bloquer ou refuser le message, car ils peuvent avoir des doutes sur la redirection du lien.
- L'utilisation d'un [code court]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) serait le type de numéro le plus fiable pour inclure des liens.

Braze dispose également de sa propre fonctionnalité de raccourcissement des liens, qui permet de raccourcir les liens et de fournir automatiquement des analyses/analytiques des clics. Pour plus d'informations, reportez-vous à la section [Raccourcissement des liens]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/).

### Les envois de messages de test sont-ils pris en compte dans le calcul des limites ?

Oui, c'est le cas. Gardez cela à l'esprit lorsque vous testez les messages.

### Un utilisateur doit-il faire partie d'un groupe d'abonnement SMS pour recevoir des messages de test SMS ?

Oui, c'est le cas. Les utilisateurs doivent avoir un numéro de téléphone valide et faire partie du groupe d'abonnement SMS utilisé pour l'envoi du test.

### Avez-vous besoin de limiter le débit de vos envois de messages SMS ?

Le taux de concurrence et le débit par défaut permettent d'envoyer environ 360 000 messages par heure et par code court. Un débit supplémentaire nécessite des codes courts supplémentaires.

### Comment éviter les dépassements ?

Bien que nous ne puissions pas vous promettre que vous n'aurez pas de temps en temps un dépassement, vous pouvez suivre les précautions suivantes pour réduire les risques de dépasser les limites qui vous sont allouées :

- Faites attention au nombre de caractères de votre SMS. L'envoi involontaire de plus d'un segment peut entraîner des dépassements de capacité. Pour plus de détails, reportez-vous à notre [segmentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-breakdown).
- Calculez soigneusement le nombre de caractères de votre SMS pour tenir compte du contenu connecté ou liquide. Le compositeur de SMS de Braze dans votre tableau de bord n'estime ni ne prend en compte l'utilisation de l'une ou l'autre de ces fonctionnalités.
- Tenez compte du type d'encodage de votre message - si votre message utilise l'encodage GSM-7, vous pouvez généralement estimer que vous pouvez envoyer un message avec 128 caractères par segment de message. Si votre message utilise l'encodage [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set), vous pouvez généralement estimer que vous pouvez envoyer un message avec 67 caractères par segment de message.
- Testez, testez et testez ! Testez toujours vos messages SMS avant leur lancement, en particulier lorsque vous utilisez le contenu liquide et connecté.

### Quelles sont les meilleures pratiques d'envoi pour éviter la détection de spam pour les SMS ?

1. Veillez à ce que les instructions relatives à l'abonnement et au retrait soient claires.
2. Veillez à ce que vous (la marque) entreteniez une relation avec le client.
3. Assurez-vous que le contenu est pertinent par rapport à la relation et à ce que l'utilisateur a choisi de recevoir.

Pour plus d'informations sur la manière d'éviter la détection des spams, consultez les [lignes directrices sur les lois et réglementations en matière de SMS.]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/)

### Comment créer une logique pour les abonnements sélectifs aux SMS afin que les utilisateurs fassent partie du bon groupe d'abonnement ?

Les mots-clés personnalisés sont rédigés comme des événements personnalisés. Vous devez donc créer des segmentations basées sur les mots-clés que les clients peuvent saisir. Par exemple, si un utilisateur s'abonne aux SMS pour les messages VIP mais pas pour les alertes, vous pouvez créer un segment VIP et un segment d'alertes, puis affecter l'utilisateur au segment approprié.

### Combien de caractères un emoji utilise-t-il ?

Les emojis peuvent être délicats, car il n'y a pas de nombre de caractères standard pour tous les emojis. Il existe un risque que l'emoji dépasse la limite de caractères et divise le SMS en plusieurs messages, bien qu'il apparaisse comme un seul message dans le compositeur de Braze. Lorsque vous testez vos messages, vous pouvez mieux vérifier si un message sera divisé en utilisant notre [calculateur de segmentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator).

### Si un utilisateur envoie "Stop" à notre code court, est-il désabonné du groupe d'abonnement ?

À quoi cela ressemble-t-il dans le profil utilisateur ? Le groupe d'abonnement sera remplacé par deux tirets (- -) et il y aura des événements personnalisés pour l'abonnement et le désabonnement.

### Existe-t-il un moyen de savoir si un alias existe sur un profil utilisateur ?

Les aliases ne sont pas visibles sur le profil utilisateur. Vous devrez utiliser les endpoints d'[exportation des données de l'utilisateur]({{site.baseurl}}/api/endpoints/export/) pour confirmer la définition des alias.

### Qu'est-ce qu'un code court partagé ?

Avec un code court partagé, tous les messages, quelle que soit l'entreprise ou l'organisation qui les envoie, arrivent sur l'appareil mobile d'un consommateur à partir du même numéro de téléphone de 5 à 6 chiffres. Si les codes courts partagés sont relativement peu coûteux et immédiatement disponibles, cela signifie que votre entreprise ne disposera pas d'un code court dédié.

Les inconvénients de cette approche sont les suivants :

- Si vos clients choisissent de ne pas recevoir les messages d'une autre entreprise ayant un code court commun avec le vôtre, ils auront également choisi de ne pas recevoir vos messages.
- Si une entreprise enfreint les règles, les messages de toutes les entreprises sont suspendus.
- Questions de sécurité

### Comment autoriser les URL pour les SMS ?

Avant d'envoyer des messages SMS contenant des URL à des utilisateurs de certains pays (par exemple, la Suède ou les pays nordiques), vous devez faire enregistrer ces URL auprès de l'opérateur. Contactez votre gestionnaire du service clientèle de Braze pour obtenir de l'aide. Ce processus prendra environ cinq jours.  

### Que se passe-t-il si plusieurs utilisateurs ont le même numéro de téléphone ?

Lorsque plusieurs profils utilisateurs partageant un même numéro de téléphone (activé pour les SMS) sont éligibles à une campagne basée sur une action ou à un composant Canvas au même moment, déclenché par l'événement d'un SMS entrant, Braze déduira les utilisateurs au niveau du composant Canvas. Cela empêchera les utilisateurs de recevoir plus d'un SMS pour un composant Canvas, même si plusieurs utilisateurs partagent le même numéro de téléphone. 

{% alert note %}
Braze n'effectue pas de déduplication par numéro de téléphone pour les toiles planifiées.
{% endalert %}

Braze utilisera le flux suivant pour déterminer le profil du destinataire :
- Vérifiez quel profil a reçu le SMS le plus récemment (jusqu'à 7 jours auparavant) ; s'il en existe un, envoyez-le à cet utilisateur.
- Si aucun des deux n'a reçu de SMS il y a moins de 7 jours, envoyez-les à l'utilisateur dont l'alias d'utilisateur "phone" correspond au numéro de téléphone.
- S'il n'y en a pas, l'envoi se fait vers un profil aléatoire parmi ceux qui sont disponibles. 

Si vous recevez un mot-clé "START" ou "STOP" du numéro de téléphone partagé, tous les profils utilisateurs seront abonnés et activés pour les SMS ou désabonnés. Ceci s'applique également aux changements d'état de l'API. Par exemple, si plusieurs profils ayant des ID externes différents ont les mêmes numéros de téléphone, une modification de l'état du groupe d'abonnement via l'API mettra à jour tous les profils ayant ce numéro de téléphone, même si un seul ID externe est spécifié.

{% alert important %}
Si vous répartissez vos utilisateurs dans un Canvas et que vous avez des heures de planification différentes pour chaque composant du Canvas, vous pouvez envoyer à un utilisateur ayant le même e-mail ou le même téléphone des messages en double.
{% endalert %}

### Les propriétés d'un événement SMS permettent-elles de saisir des mots-clés dans une phrase ?

Pour qu'un mot-clé soit reconnu dans une phrase (par exemple, "s'il vous plaît, arrêtez de m'envoyer des SMS"), vous devez utiliser un énoncé liquide dans le message pour reconnaître le mot spécifique. Les propriétés d'événement ont une limite de 256 caractères ; sinon, il n'y a pas de limite de caractères.

### Pourquoi le tableau de bord de Braze m'avertit-il que je risque d'être facturé pour des segments de message supplémentaires alors que mon message comporte moins de 160 (GCM-7) ou 70 (UCS-2) caractères ?

Des segments de message supplémentaires peuvent vous être facturés si la personnalisation des liquides est incluse dans votre message. La mise en forme du bloc de contenu n'intervient qu'au moment où le message se prépare à être envoyé. Lorsque vous modifiez un SMS avec un bloc de contenu, Braze ne sait pas ce que le bloc de contenu contiendra mais fournit une estimation approximative. Nous recommandons aux utilisateurs d'utiliser le volet test pour prévisualiser le message afin de mieux comprendre ce qui les attend.

### Qu'est-ce qu'un `app_id` dans l'objet API SMS ?

La clé API d'identification de l'app ou `app_id` est un paramètre associant l'activité à une app spécifique dans votre espace de travail. Il désigne l'application avec laquelle vous interagissez au sein de l'espace de travail. Par exemple, vous constaterez que vous aurez un `app_id` pour votre application iOS, un `app_id` pour votre application android et un `app_id` pour votre intégration web. 

Vous pouvez trouver votre `app_id` en naviguant vers **Réglages** > **Réglages de l'application** et en localisant la section **Identification.** 

### Comment les SMS me seront-ils facturés ?

Outre les frais pour les codes courts et longs, Braze fournit un contingent d'envois de messages SMS pour différents pays. En d'autres termes, nous travaillons avec vous pour définir un certain nombre de segments de messages pour différents pays, que vous utiliserez pour envoyer des campagnes de communication par SMS. La facturation se fait en fonction du nombre de segments de messages envoyés par pays. Pour en savoir plus sur le calcul des segments de message, consultez notre guide sur [les segments de message et les limites de copie.]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-breakdown)  Votre gestionnaire de compte vous contactera pour vous faire savoir si vous êtes proche d'atteindre votre maximum, en vous fournissant des rapports pertinents pour vous aider à rester informé. Pour toute question concernant les dépassements, adressez-vous à votre conseiller Braze.

### Si un message est envoyé à une ligne fixe, sera-t-il pris en compte dans le décompte des envois de SMS ?

Aux États-Unis, au Canada et au Royaume-Uni :
- Si un SMS est envoyé à une ligne fixe, il sera marqué comme **non délivré**. Notez que Twilio facturera toujours les tentatives de **réception/distribution**, de sorte que les messages marqués comme **envoyés**, **livrés** ou **non livrés** dans vos journaux de messages seront facturés.
- Au Royaume-Uni, certains opérateurs transforment le SMS en boîte vocale et envoient le message.

Dans les autres pays :
- Twilio lancera une erreur et vous ne serez pas facturé pour la tentative de message SMS. 

### Si un utilisateur est abonné et envoie un mot-clé à notre code court et long, reçoit-il la réponse que nous avons configurée pour ce mot-clé dans Braze ?

Si un utilisateur n'est pas abonné et qu'il envoie un mot-clé appartenant à l'une des [catégories de mots-clés par défaut]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/), il recevra la réponse pour ce mot-clé. Si un utilisateur est exclu et envoie un [mot-clé personnalisé]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/keyword_handling/), il ne recevra pas de réponse pour ce mot-clé. 
