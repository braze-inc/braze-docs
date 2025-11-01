---
nav_title: Limite de débit et limite de fréquence
article_title: Limitation du débit et limitation de fréquence
page_order: 6
tool: Campaigns
page_type: reference
description: "Cet article de référence aborde le concept de limite de débit et de limite de fréquence dans les campagnes, et la manière dont vous pouvez gérer la pression marketing pour améliorer l'expérience utilisateur."

---

# Limite de débit et limite de fréquence

> La limite de débit et la limite de fréquence peuvent être utilisées conjointement pour s'assurer que vos utilisateurs reçoivent les messages dont ils ont besoin, et aucun de ceux dont ils n'ont pas besoin.

## À propos de la limite de débit

Braze vous permet de contrôler la pression marketing en limitant le débit de vos campagnes, en régulant la quantité de trafic sortant de votre plateforme. Vous pouvez mettre en place deux types différents de limite de débit pour vos campagnes : 

1. [**Limite de débit centrée sur l'utilisateur :**](#user-centric-rate-limiting) L'objectif est d'offrir la meilleure expérience possible à l'utilisateur.
2. [**Limitation du débit de réception/distribution :**](#delivery-speed-rate-limiting) Prend en considération la bande passante de vos serveurs.

Braze essaiera de répartir uniformément les envois de messages tout au long de la minute, mais ne peut le garantir. Par exemple, si vous avez une campagne avec une limite de débit de 5 000 messages par minute, nous essaierons de répartir les 5 000 demandes de manière égale tout au long de la minute (environ 84 messages par seconde), mais il peut y avoir une certaine variation dans le débit par seconde.

### Limite de débit centrée sur l'utilisateur

Au fur et à mesure que vous créez des segments, il y aura des cas où les membres de ces segments se chevaucheront. Si vous envoyez des campagnes à ces segments, vous devez vous assurer que vous n'envoyez pas trop souvent des messages à vos utilisateurs. Si un utilisateur reçoit trop de messages dans un court laps de temps, il se sentira encombré et désactivera les notifications push ou désinstallera votre application.

#### Filtres de segmentation pertinents

Braze propose les filtres suivants afin de vous aider à limiter le débit auquel vos utilisateurs reçoivent des messages :

- Dernier envoi de messages
- Dernier envoi d'un message
- Campagne de poussée du dernier reçu
- Dernière campagne d'e-mail reçue
- Dernier SMS reçu

#### Mise en œuvre des filtres

Imaginons que nous ayons créé un segment nommé "Vitrine de filtres de reciblage" avec un filtre "Dernière utilisation de ces apps il y a plus de 7 jours" pour cibler les utilisateurs. Il s'agit d'un segment de réengagement standard.

Si d'autres segments plus ciblés ont reçu des notifications récemment, vous ne voudrez peut-être pas que vos utilisateurs soient ciblés par des campagnes plus génériques destinées à ce segment. En ajoutant le filtre "Dernière campagne push reçue" à ce segment, l'utilisateur s'est assuré que s'il a reçu une autre notification au cours des dernières 24 heures, il sortira de ce segment pour les 24 heures à venir. S'il répond toujours aux critères de segmentation 24 heures plus tard et qu'il n'a pas reçu d'autres notifications, il est réintégré dans la segmentation.

!section Détails du segment avec le filtre du segment "Dernier message reçu" en surbrillance.]({% image_buster /assets/img_archive/rate_limit_daily.png %})

En appliquant ce filtre à tous les segments ciblés par les campagnes, vos utilisateurs recevront au maximum un push toutes les 24 heures. Vous pouvez alors hiérarchiser vos messages en veillant à ce que les messages les plus importants soient envoyés avant les messages moins importants.

#### Fixer un plafond d'utilisateurs

Dans l'étape **Audiences cibles** du compositeur de votre campagne, vous pouvez également limiter le nombre total d'utilisateurs qui recevront votre message. Il s'agit d'un contrôle indépendant des filtres de votre campagne, qui vous permet de segmenter librement les utilisateurs sans vous soucier de l'envoi excessif de messages.

\![Résumé de l'audience avec une case à cocher pour limiter le nombre de personnes qui reçoivent la campagne.]({% image_buster /assets/img_archive/total_limit.png %})

En sélectionnant la limite maximale d'utilisateurs, vous pouvez limiter le débit auquel vos utilisateurs reçoivent des notifications par canal ou globalement pour tous les types de messages.

##### Nombre maximum d'utilisateurs avec optimisations

Si vous utilisez une optimisation telle que la variante gagnante ou la variante personnalisée, la campagne comprendra deux envois : l'expérience initiale et l'envoi final. 

Pour implémenter un plafond d'utilisateurs dans ce scénario, sélectionnez **Limiter le nombre de personnes qui recevront cette campagne**, puis sélectionnez **Au total cette campagne devrait**, et entrez une limite d'audience. La limite de votre audience sera divisée selon les pourcentages indiqués dans le panneau de **test A/B.**  

Si vous sélectionnez **Chaque fois que la campagne est planifiée**, ces deux phases seront limitées séparément au nombre défini. Ce n'est généralement pas souhaitable.

#### Fixer un plafond d'impression

Pour les messages in-app et les cartes de contenu, vous pouvez contrôler la pression marketing en définissant un nombre maximum d'impressions qui seront affichées à votre base d'utilisateurs, après quoi Braze n'enverra plus de messages à vos utilisateurs. Toutefois, il est important de noter que ce plafond n'est pas exact. 

Les nouvelles cartes de contenu et les règles relatives aux messages in-app sont envoyées à une application au début de la session, ce qui signifie que Braze peut envoyer un message à l'utilisateur avant que le plafond ne soit atteint, mais au moment où l'utilisateur déclenche le message, le plafond a déjà été atteint. Dans ce cas, l'appareil continue d'afficher le message.

Par exemple, disons que vous avez un jeu avec un message in-app qui se déclenche lorsque l'utilisateur réussit un niveau, et que vous le plafonnez à 100 impressions. Il y a eu 99 impressions jusqu'à présent. Alice et Bob ouvrent tous deux le jeu et Braze indique à leurs appareils qu'ils peuvent recevoir le message lorsqu'ils ont franchi un niveau. Alice bat un niveau en premier et reçoit le message. Bob bat le niveau suivant, mais comme son appareil n'a pas communiqué avec les serveurs de Braze depuis le début de sa session, son appareil ne sait pas que le message a atteint son plafond et il recevra également le message. Toutefois, lorsqu'un plafond d'impression a été atteint, la prochaine fois qu'un appareil demandera la liste des messages in-app éligibles, ce message ne sera pas envoyé et sera supprimé de cet appareil.

### Limite de débit et test A/B

Lorsque vous utilisez la limite de débit avec un test A/B, la limite de débit n'est pas appliquée au groupe de contrôle de la même manière qu'au groupe de test, ce qui constitue une source potentielle de biais temporel. Pour éviter ce biais, utilisez des fenêtres de conversion appropriées.

### Limitation du débit de réception/distribution

Si vous prévoyez que de grandes campagnes entraîneront un pic d'activité des utilisateurs et une surcharge de vos serveurs, vous pouvez spécifier une limite de débit par minute pour l'envoi des messages, ce qui signifie que Braze n'enverra pas plus que la limite de débit définie en l'espace d'une minute.

Lorsque vous ciblez des utilisateurs lors de la création d'une campagne, vous pouvez accéder à **Target Audiences** (pour les campagnes) ou **Send Settings** (pour les Canvas) pour sélectionner une limite de débit (dans différents incréments allant de 10 à 500 000 messages par minute).

Notez que les campagnes non limitées par des tarifs peuvent dépasser ces limites de réception/distribution. Toutefois, sachez que les messages seront interrompus s'ils sont retardés de 72 heures ou plus en raison d'une limite de débit trop basse. Si la limite de débit est trop basse, le créateur de la campagne recevra des alertes dans le tableau de bord et par e-mail.

\![Résumé de l'audience avec une case à cocher pour limiter le débit auquel la campagne prendra fin, le débit étant de 500 000 par minute.]({% image_buster /assets/img_archive/per_minute_rate_limit.png %})

#### Exemple

Si vous essayez d'envoyer 75 000 messages avec une limite de débit de 10 000 par minute, la réception/distribution sera étalée sur huit minutes. Votre campagne ne diffusera pas plus de 10 000 messages pour chacune des sept premières minutes, et 5 000 au cours de la dernière minute.

#### Nombre d'envois

Notez que les messages à débit limité peuvent ne pas être envoyés de manière régulière au cours de chaque minute. Si l'on prend l'exemple d'une limite de débit de 10 000 par minute, cela signifie que Braze veille à ce qu'il n'y ait pas plus de 10 000 messages envoyés par minute. Cela pourrait signifier qu'un pourcentage plus élevé des 10 000 messages est envoyé dans la première demi-minute par rapport à la dernière demi-minute.

La limite de débit est appliquée au début de la tentative d'envoi du message. Lorsque la durée de l'envoi varie, le nombre d'envois terminés peut légèrement dépasser la limite de débit pendant certaines minutes. Avec le temps, le nombre d'envois par minute se stabilisera au niveau de la limite de débit.

{% alert important %}
Cette forme de limitation de débit par rapport au nombre total d'utilisateurs dans un segment permet de ne pas retarder les envois de messages sensibles au facteur temps. Par exemple, si le segment contient 30 millions d'utilisateurs mais que nous fixons la limite de débit à 10 000 par minute, une grande partie de votre base d'utilisateurs ne recevra le message que le lendemain.
{% endalert %}

#### Campagnes à canal unique

Lors de l'envoi d'une campagne à canal unique avec une limite de débit, la limite de débit est appliquée à l'ensemble des messages.

#### Campagnes multicanal

Lors de l'envoi d'une campagne multicanal avec une limite de débit, chaque canal est envoyé indépendamment des autres. Par conséquent, les situations suivantes peuvent se produire :

- Le nombre total de messages envoyés par minute pourrait être supérieur à la limite de débit. 
    - Par exemple, si votre campagne a une limite de débit de 10 000 par minute et utilise l'e-mail et le SMS, Braze peut envoyer un maximum de 20 000 messages au total par minute (10 000 e-mails et 10 000 SMS).
- Les utilisateurs pourraient recevoir les différentes chaînes à des moments différents, et il n'est pas possible de prévoir quelle chaîne ils recevront en premier. 
    - Par exemple, si vous envoyez une campagne qui contient un e-mail et un SMS, vous pouvez avoir 10 000 utilisateurs avec des numéros de téléphone valides et 50 000 utilisateurs avec des adresses e-mail valides. Si vous paramétrez la campagne pour qu'elle envoie 100 messages par minute (une limite de débit pour la taille de la campagne), un utilisateur pourrait recevoir le SMS dans le premier lot d'envois et l'e-mail dans le dernier lot d'envois, soit près de neuf heures plus tard.

#### Campagnes push multiplateformes

Pour les campagnes push diffusées sur plusieurs plateformes, la limite de débit sélectionnée sera répartie de manière égale entre les plateformes. Une campagne push tirant parti d'Android et d'iOS avec une limite de débit de 10 000 par minute répartira équitablement les 10 000 messages sur les deux plateformes.

#### Limitation de la vitesse de réception/distribution des toiles {#canvas-delivery-speed}

Lors de l'envoi d'un Canvas avec une limite de débit, la limite de débit est partagée entre les canaux. Cela signifie que le nombre total de messages envoyés par minute à partir du Canvas ne dépassera pas la limite de débit. Par exemple, si votre Canvas a une limite de débit de 10 000 par minute et utilise l'e-mail et le SMS, Braze enverra un total de 10 000 messages par minute à travers l'e-mail et le SMS.

#### Limitation du débit et tentatives d'accès au contenu connecté

Lorsque le [rappel de contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries/) est activé, Braze relance les échecs d'appel tout en respectant la limite de débit que vous avez définie pour chaque renvoi. Prenons le cas d'un envoi de 75 000 messages avec une limite de débit de 10 000 par minute. Imaginez que dans la première minute, l'appel échoue ou est lent et n'envoie que 4 000 messages.

Au lieu d'essayer de rattraper le retard et d'envoyer les 6 000 messages restants dans la deuxième minute ou de les ajouter aux 10 000 messages déjà prêts à être envoyés, Braze déplacera ces 6 000 messages en "fin de file d'attente" et ajoutera une minute, si nécessaire, au nombre total de minutes nécessaires à l'envoi de votre message.

| Minute | Pas d'échec | 6 000 Échec à la minute 1 |
|--------|------------|---------------------------|
| 1      | 10,000     | 4,000                     |
| 2      | 10,000     | 10,000                    |
| 3      | 10,000     | 10,000                    |
| 4      | 10,000     | 10,000                    |
| 5      | 10,000     | 10,000                    |
| 6      | 10,000     | 10,000                    |
| 7      | 10,000     | 10,000                    |
| 8      | 5,000      | 10,000                    |
| 9      | 0          | 6,000                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Les demandes de contenu connecté ne sont pas limitées au débit de manière indépendante et suivront la limite de débit du webhook. Cela signifie que s'il y a un appel de contenu connecté à un endpoint unique par webhook, vous devriez vous attendre à 5 000 webhooks et également à 5 000 appels de contenu connecté par minute. Notez que la mise en cache peut avoir une incidence sur ce point et réduire le nombre d'appels au contenu connecté. En outre, les tentatives peuvent augmenter le nombre d'appels au contenu connecté. Nous vous recommandons donc de vérifier que le point de terminaison du contenu connecté peut supporter une certaine fluctuation à ce niveau.

## À propos de la limite de fréquence

Alors que votre base d'utilisateurs continue de croître et que votre envoi de messages s'étend pour inclure des campagnes sur le cycle de vie, des campagnes déclenchées, des campagnes transactionnelles et des campagnes de conversion, il est important d'éviter que vos messages ne paraissent "spammy" ou dérangeants. En offrant un meilleur contrôle sur l'expérience de vos utilisateurs, la limite de fréquence vous permet de créer les campagnes que vous souhaitez sans submerger votre audience.

### Aperçu des fonctionnalités {#freq-cap-feat-over}

La limite de fréquence est appliquée au niveau de l'envoi de la campagne ou du composant Canvas et peut être configurée pour chaque espace de travail à partir de **Paramètres** > Règles de limite de fréquence.

Par défaut, la limite de fréquence est basculée lors de la création de nouvelles campagnes. A partir de là, vous pouvez choisir les options suivantes :

- Le canal de communication que vous souhaitez privilégier : push, e-mail, SMS, webhook, WhatsApp, ou l'un de ces cinq canaux.
- Combien de fois chaque utilisateur doit recevoir une campagne ou des envois de composants Canvas d'un canal dans un certain laps de temps.
- Combien de fois chaque utilisateur doit recevoir une campagne ou un composant Canvas envoyé par une [étiquette](#frequency-capping-by-tag) dans un certain laps de temps.

Ce délai peut être mesuré en minutes, en jours ou en semaines (sept jours), avec une durée maximale de 30 jours.

Chaque ligne de limites de fréquence sera connectée à l'aide de l'opérateur `AND`, et vous pouvez ajouter jusqu'à 10 règles par espace de travail. En outre, vous pouvez inclure plusieurs plafonds pour les mêmes types de messages. Par exemple, vous pouvez limiter les utilisateurs à une poussée par jour et à trois poussées par semaine.

Section de limite de fréquence avec des listes de campagnes et de toiles auxquelles les règles s'appliqueront et ne s'appliqueront pas.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %})

#### Comportement lorsque les utilisateurs sont limités en fréquence sur une étape du canvas

Si un utilisateur de Canvas est limité en fréquence en raison des paramètres globaux de limitation de fréquence, il passera immédiatement à l'étape suivante de Canvas. L'utilisateur ne quittera pas le Canvas à cause de la limite de fréquence.

### Règles de réception/distribution

Pour certaines campagnes, comme les messages transactionnels, vous souhaitez que l'utilisateur soit toujours contacté, même s'il a déjà atteint son plafond de fréquence. Par exemple, une appli de réception/distribution peut souhaiter envoyer un e-mail ou un push lorsqu'un article est livré, quel que soit le nombre de campagnes reçues par l'utilisateur.

Si vous souhaitez qu'une campagne particulière ne tienne pas compte des règles de limitation de fréquence, vous pouvez le faire dans le tableau de bord de Braze lors de la planification de la réception/distribution de cette campagne en basculant la **limitation de fréquence** sur **OFF**. 

Ensuite, il vous sera demandé si vous souhaitez toujours que cette campagne soit prise en compte dans votre limite de fréquence. Les messages qui comptent pour la limite de fréquence sont inclus dans les calculs du filtre du canal intelligent. Lorsque vous envoyez des [campagnes API]({{site.baseurl}}/developer_guide/rest_api/messaging/#messaging), qui sont souvent transactionnelles, vous avez la possibilité de spécifier qu'une campagne doit ignorer les règles de limite fréquence [dans la demande API]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns) en définissant `override_messaging_limits` sur `true`.

Par défaut, les nouvelles campagnes et les Canevas qui n'obéissent pas aux limites de fréquence ne seront pas non plus pris en compte. Ceci est configurable pour chaque campagne et Canvas.

{% alert note %}
Ce comportement modifie le comportement par défaut lorsque vous désactivez la limite de fréquence pour une campagne ou un Canvas. Ces modifications sont compatibles avec les versions antérieures et n'ont pas d'incidence sur les messages actuellement en ligne/en production/instantanée.
{% endalert %}

\![Section des contrôles de réception/distribution avec la limite de fréquence activée.]({% image_buster /assets/img_archive/frequencycappingupdate.png %})

Les différents canaux d'une campagne multicanal compteront individuellement pour la limite de fréquence. Par exemple, si vous créez une campagne multicanal avec des messages push et des e-mails et que vous avez défini une limite de fréquence pour ces deux canaux, les messages push seront comptabilisés dans une campagne push et les messages e-mail seront comptabilisés dans une campagne e-mail. La campagne comptera également pour une "campagne de tout type". Si les utilisateurs sont limités à une campagne push et une campagne e-mail par jour et qu'un utilisateur reçoit cette campagne multicanal, il ne sera plus éligible aux campagnes push ou e-mail pour le reste de la journée (sauf si une campagne ignore les règles de limitation de fréquence).

Les messages in-app et les cartes de contenu ne sont pas pris en compte dans le calcul des plafonds des campagnes ou des composants Canvas, quels qu'ils soient.

{% alert important %}
La limite de fréquence globale est planifiée en fonction du fuseau horaire de l'utilisateur et est calculée par jours calendaires, et non par périodes de 24 heures. Par exemple, si vous avez mis en place une règle de limite de fréquence qui consiste à ne pas envoyer plus d'une campagne par jour, un utilisateur peut recevoir un message à 23 heures dans son fuseau horaire local et être éligible pour recevoir un autre message une heure plus tard.
{% endalert %}

#### Cas d'utilisation

{% tabs %}
{% tab Use case 1 %}

Disons que vous avez défini une règle de limite de fréquence qui demande à ce que votre utilisateur ne reçoive pas plus de trois campagnes de notifications push ou composants Canvas par semaine, toutes campagnes ou composants Canvas confondus.

Si votre utilisateur doit recevoir trois notifications push, deux messages in-app et une carte de contenu cette semaine, il recevra tous ces messages.

{% endtab %}
{% tab Use case 2 %}

Ce scénario utilise les règles de limitation de fréquence suivantes :

**Lorsque le scénario suivant se produit :**

- Un utilisateur déclenche la même campagne, `Campaign ABC` trois fois au cours d'une semaine.
- Cet utilisateur déclenche `Campaign ABC` une fois le lundi, une fois le mercredi et une fois le jeudi.

!Section de limitation de fréquence avec la règle de ne pas envoyer plus de 2 campagnes de notifications push/étapes du canvas de toutes les campagnes/étapes du canvas à un utilisateur toutes les 1 semaines.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Le comportement attendu est alors le suivant :**

- Cet utilisateur recevra les envois de la campagne qui se sont déclenchés le lundi et le mercredi.
- Cet utilisateur ne recevra pas le troisième envoi de campagne le jeudi parce qu'il a déjà reçu deux envois de campagne en mode push cette semaine-là.

{% endtab %}
{% endtabs %}

### Limitation de fréquence par étiquette

Les [règles de limitation de fréquence](#delivery-rules) peuvent être appliquées aux espaces de travail à l'aide des tags spécifiques que vous avez appliqués à vos campagnes et à vos toiles, ce qui vous permet essentiellement de baser votre limitation de fréquence sur des groupes aux noms personnalisés.

Avec la limite de fréquence par étiquette, des règles peuvent être définies sur les tags principaux et imbriqués, de sorte que Braze prenne en compte tous les tags. Par exemple, si vous avez choisi d'utiliser l'étiquette principale A pour la limite de fréquence, nous inclurons également les informations contenues dans toutes les étiquettes imbriquées (par exemple, les étiquettes B et C) lors de la détermination de la limite.

Vous pouvez également combiner la limitation de fréquence normale avec la limitation de fréquence par étiquettes. Considérez les règles suivantes :

1. Pas plus de trois campagnes de notification push ou composants de Canvas par semaine, toutes étapes de campagne et de Canvas confondues. <br>**ET**
2. Pas plus de deux campagnes de notification push ou composants Canvas par semaine avec l'étiquette `promotional`.

Section de limitation de fréquence avec deux règles limitant le nombre de campagnes de notification push/de toiles pouvant être envoyées à un utilisateur toutes les 1 semaines.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Par conséquent, vos utilisateurs ne recevront pas plus de trois envois de campagne par semaine sur l'ensemble des campagnes et des étapes du canvas et pas plus de deux campagnes de notification push ou composants du canvas avec l'étiquette `promotional`.

{% alert important %}
Les toiles sont balisées au niveau de la toile, par opposition à la balisage par composant. Ainsi, chaque composant Canvas héritera de toutes les étiquettes de niveau Canvas.
{% endalert %}

#### Règles contradictoires

En cas de conflit entre les règles, c'est la règle de limitation de fréquence la plus restrictive qui s'applique à vos utilisateurs. Par exemple, supposons que vous ayez les règles suivantes :

1. Pas plus d'une campagne de notification push ou d'un composant Canvas par semaine, tous composants de campagne et de Canvas confondus. <br>**ET**
2. Pas plus de trois campagnes de notification push ou composants Canvas par semaine avec l'étiquette `promotional`.

Section "Frequency Capping" avec des règles contradictoires pour limiter le nombre de campagnes de notifications push/étapes du canvas envoyées à un utilisateur toutes les 1 semaines.]({% image_buster /assets/img/global_rules.png %} "global rules")

Dans cet exemple, votre utilisateur ne recevra pas plus d'une campagne de notification push ou de composants Canvas avec l'étiquette "promotionnel" au cours d'une semaine donnée, car vous avez spécifié que les utilisateurs ne doivent pas recevoir plus d'une campagne de notification push ou d'un composant Canvas parmi toutes les campagnes et tous les composants Canvas. En d'autres termes, la règle de fréquence applicable la plus restrictive est celle qui sera appliquée à un utilisateur donné.

#### Nombre d'étiquettes

La limitation de fréquence par les règles d'étiquette est calculée au moment de l'envoi d'un message. Cela signifie que la limite de fréquence par étiquette ne prend en compte que les étiquettes qui sont actuellement sur les campagnes ou les toiles qu'un utilisateur a reçues dans le passé. Il ne tient pas compte des tags qui se trouvaient sur les campagnes ou les toiles au moment de leur envoi, mais qui ont été retirés depuis. Il sera pris en compte si une étiquette est ajoutée ultérieurement à un message qu'un utilisateur a reçu dans le passé, mais avant que le dernier message étiqueté ne soit envoyé.

##### Cas d'utilisation

Considérez les campagnes suivantes et la limite de fréquence par règle d'étiquette :

**Campagnes**:

- La **campagne A** est une campagne de push étiquetée `promotional`. L'envoi est prévu pour lundi à 9 heures.
- La **campagne B** est une campagne de push étiquetée `promotional`. L'envoi est prévu pour mercredi à 9 heures.

**Limitation de fréquence par règle d'étiquette :**

- Votre utilisateur ne doit pas recevoir plus d'une campagne de notification push par semaine avec l'étiquette `promotional`.<br><br>

| Action | Résultat |
|---|---|
| L'étiquette `promotional` est retirée de la **campagne A** après que votre utilisateur a reçu le message, mais avant que **la campagne B ne l'ait envoyé.** | Votre utilisateur recevra la **campagne B.**|
| L'étiquette `promotional` est supprimée par erreur de la **campagne A** après que votre utilisateur a reçu le message. <br> L'étiquette est ajoutée à la **campagne A** le mardi, avant l'envoi de la **campagne B.**  | Votre utilisateur ne recevra pas la **campagne B.** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Envoi à grande échelle {#sending-at-large-scales}

La limitation de fréquence par des règles d'étiquette pourrait ne pas être appliquée correctement à grande échelle, par exemple 100 messages par canal provenant de campagnes ou de composants Canvas.

Par exemple, si votre règle de limitation de fréquence par étiquette est la suivante :

> Pas plus de deux campagnes d'e-mail ou composants Canvas avec l'étiquette `Promotional` à un utilisateur par semaine.

Si vous envoyez à l'utilisateur plus de 100 e-mails provenant de campagnes et d'étapes du canvas avec la limite de fréquence activée au cours d'une semaine, plus de deux e-mails peuvent être envoyés à l'utilisateur.

Étant donné que 100 messages par canal représentent plus de messages que ce que la plupart des marques envoient à leurs utilisateurs, il est peu probable que vous soyez impacté par cette limitation. Pour éviter cette limitation, vous pouvez fixer un plafond pour le nombre maximum d'e-mails que vous souhaitez que vos utilisateurs reçoivent au cours d'une semaine.

Par exemple, vous pouvez définir la règle suivante :

> Pas plus de trois campagnes d'e-mail ou composants de Canvas par semaine, toutes campagnes et étapes du canvas confondues.

Cette règle garantit qu'aucun utilisateur ne recevra plus de 100 e-mails par semaine car, au maximum, les utilisateurs recevront trois e-mails par semaine provenant de campagnes ou de composants Canvas pour lesquels la limite de fréquence est activée.

