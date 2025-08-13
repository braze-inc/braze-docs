---
nav_title: Limitation du taux et limite de fréquence
article_title: Limitation du taux et limite de fréquence
page_order: 6
tool: Campaigns
page_type: reference
description: "Le présent article de référence aborde le concept de limitation du taux et la limite de fréquence dans les campagnes ainsi que la manière dont vous pouvez appliquer une pression marketing pour améliorer l’expérience utilisateur."

---

# Limitation du taux et limite de fréquence

> La limitation du débit et la limite de fréquence peuvent être utilisées ensemble pour vous assurer que vos utilisateurs reçoivent les messages dont ils ont besoin et aucun de ceux dont ils n’ont pas besoin.

## À propos de la limite de débit

Braze vous permet de contrôler la pression marketing par taux limitant vos campagnes, ce qui régule la quantité de trafic sortant de votre plate-forme. Vous pouvez mettre en place deux types différents de limite de débit pour vos campagnes : 

1. [**Limite de débit centrée sur l'utilisateur :**](#user-centric-rate-limiting) L'objectif est d'offrir la meilleure expérience possible à l'utilisateur.
2. [**Limitation du débit de réception/distribution :**](#delivery-speed-rate-limiting) Prend en considération la bande passante de vos serveurs.

Braze essaiera de répartir uniformément les envois de messages tout au long de la minute, mais ne peut le garantir. Par exemple, si vous avez une campagne avec une limite de débit de 5 000 messages par minute, nous essaierons de répartir les 5 000 demandes de manière égale tout au long de la minute (environ 84 messages par seconde), mais il peut y avoir une certaine variation dans le débit par seconde.

### Limite de débit centrée sur l'utilisateur

À mesure que vous créez plus de segments, il y aura des cas où l’appartenance à ces segments se chevauche. Si vous envoyez des campagnes à ces segments, vous devez être sûr que vous n’envoyez pas des messages trop souvent à vos utilisateurs. Si un utilisateur reçoit trop de messages sur une courte période, il va se sentir surchargé et désactiver les notifications push ou désinstaller votre application.

#### Filtres de segment pertinents

Braze fournit les filtres suivants afin de vous aider à limiter le taux auquel vos utilisateurs reçoivent des messages :

- Dernière interaction avec un message
- Dernier message reçu
- Dernière campagne de notification push reçue
- Dernière campagne e-mail reçue
- Dernier SMS reçu

#### Implémenter des filtres

Supposons que nous avons créé un segment nommé « Vitrine de filtres de reciblage » avec un filtre « Dernière utilisation de ces applications il y a plus de 7 jours » pour cibler les utilisateurs. Il s’agit d’un segment de ré-engagement standard.

Si vous avez d’autres segments plus ciblés recevant des notifications récemment, vous ne voulez peut-être pas que vos utilisateurs soient ciblés par des campagnes plus génériques dirigées vers ce segment. En ajoutant le filtre « Dernière campagne de notification push reçue » à ce segment, l’utilisateur est assuré que, s’il a reçu une autre notification au cours des dernières 24 heures, il sortira de ce segment pendant les 24 prochaines heures. S’il répond toujours aux autres critères du segment 24 heures plus tard et n’a pas reçu de notifications supplémentaires, il reprendra sa place dans le segment.

![Section Détails du segment avec le filtre du segment "Dernier message reçu" en surbrillance.]({% image_buster /assets/img_archive/rate_limit_daily.png %})

En ajoutant ce filtre à tous les segments ciblés par les campagnes, vos utilisateurs ne peuvent recevoir qu’une notification push toutes les 24 heures au maximum. Vous pouvez ensuite prioriser votre messagerie en vous assurant que vos messages les plus importants sont envoyés avant les moins importants.

#### Fixer un plafond d'utilisateurs

Dans l'étape **Audiences cibles** du compositeur de votre campagne, vous pouvez également limiter le nombre total d'utilisateurs qui recevront votre message. Il s'agit d'un contrôle indépendant des filtres de votre campagne, qui vous permet de segmenter librement les utilisateurs sans vous soucier de l'envoi excessif de messages.

![Résumé de l'audience avec une case à cocher permettant de limiter le nombre de personnes recevant la campagne.]({% image_buster /assets/img_archive/total_limit.png %})

En sélectionnant la limite maximale d'utilisateurs, vous pouvez limiter le débit auquel vos utilisateurs reçoivent des notifications par canal ou globalement pour tous les types de messages.

##### Nombre maximum d'utilisateurs avec optimisations

Si vous utilisez une optimisation telle que la variante gagnante ou la variante personnalisée, la campagne comprendra deux envois : l'expérience initiale et l'envoi final. 

Pour implémenter un plafond d'utilisateurs dans ce scénario, sélectionnez **Limiter le nombre de personnes qui recevront cette campagne**, puis sélectionnez **Au total, cette campagne doit** et entrez une limite d'audience. La limite de votre audience sera divisée en fonction des pourcentages indiqués dans le panneau de **test A/B.**  

Si vous sélectionnez **Chaque fois que la campagne est planifiée**, ces deux phases seront limitées séparément au nombre défini. Ce n’est généralement pas souhaitable.

#### Fixer un plafond d'impressions

Pour les messages in-app et les cartes de contenu, vous pouvez contrôler la pression marketing en définissant un nombre maximum d'impressions qui seront affichées à votre base d'utilisateurs, après quoi Braze n'enverra plus de messages à vos utilisateurs. Cependant, il est important de noter que ce plafond n’est pas exact. 

Les nouvelles cartes de contenu et les règles relatives aux messages in-app sont envoyées à une application au début de la session, ce qui signifie que Braze peut envoyer un message à l'utilisateur avant que le plafond ne soit atteint, mais au moment où l'utilisateur déclenche le message, le plafond a déjà été atteint. Dans cette situation, l’appareil affichera quand même le message.

Supposons par exemple que vous ayez un jeu avec un message in-app qui se déclenche quand un utilisateur bat un niveau et que vous l’ayez plafonné à 100 impressions. Jusqu’à présent, il y a eu 99 impressions. Alice et Bob ouvrent tous deux le jeu et Braze dit à leurs appareils qu’ils sont admissibles à recevoir le message lorsqu’ils battent un niveau. Alice bat un niveau en premier et reçoit le message. Bob bat le niveau suivant, mais comme son appareil n'a pas communiqué avec les serveurs de Braze depuis le début de sa session, son appareil ne sait pas que le message a atteint son plafond et il recevra également le message. Toutefois, lorsqu'un plafond d'impression a été atteint, la prochaine fois qu'un appareil demandera la liste des messages in-app éligibles, ce message ne sera pas envoyé et sera supprimé de cet appareil.

### Limite de débit et test A/B

Lorsque vous utilisez la limite de débit avec un test A/B, la limite de débit n'est pas appliquée au groupe de contrôle de la même manière qu'au groupe de test, ce qui constitue une source potentielle de biais temporel. Pour éviter ce biais, utilisez des fenêtres de conversion appropriées.

### Limiter le taux de vitesse de livraison

Si vous prévoyez que de grandes campagnes entraîneront un pic d'activité des utilisateurs et une surcharge de vos serveurs, vous pouvez spécifier une limite de débit par minute pour l'envoi des messages, ce qui signifie que Braze n'enverra pas plus que la limite de débit définie en l'espace d'une minute.

Lorsque vous ciblez des utilisateurs lors de la création d'une campagne, vous pouvez accéder à **Target Audiences** (pour les campagnes) ou **Send Settings** (pour les Canvas) pour sélectionner une limite de débit (dans différents incréments allant de 10 à 500 000 messages par minute).

Notez que les campagnes sans limitation du taux peuvent dépasser ces limites de livraison. Toutefois, sachez que les messages seront interrompus s'ils sont retardés de 72 heures ou plus en raison d'une limite de débit trop basse. Si la limite de débit est trop basse, le créateur de la campagne recevra des alertes dans le tableau de bord et par e-mail.

![Résumé de l'audience avec une case à cocher pour limiter le débit auquel la campagne se terminera, le débit étant de 500 000 par minute.]({% image_buster /assets/img_archive/per_minute_rate_limit.png %})

Autre exemple, si vous essayez d'envoyer 75 000 messages avec une limite de débit de 10 000 par minute, la réception/distribution s'étalera sur 8 minutes. Votre campagne ne diffusera pas plus de 10 000 messages pour chacune des sept premières minutes, et 5 000 au cours de la dernière minute.

Notez que les messages à débit limité peuvent ne pas être envoyés de manière régulière au cours de chaque minute. Si l'on prend l'exemple d'une limite de débit de 10 000 par minute, cela signifie que Braze veille à ce qu'il n'y ait pas plus de 10 000 messages envoyés par minute. Cela pourrait signifier qu'un pourcentage plus élevé des 10 000 messages est envoyé dans la première demi-minute par rapport à la dernière demi-minute. 

Notez également que la limite de débit est appliquée au début de la tentative d'envoi des messages. Lorsque la durée de l'envoi varie, le nombre d'envois terminés peut légèrement dépasser la limite de débit pendant certaines minutes. Avec le temps, le nombre d'envois par minute se stabilisera au niveau de la limite de débit.

{% alert important %}
Cette forme de limitation de débit par rapport au nombre total d'utilisateurs dans un segment permet de ne pas retarder les envois de messages sensibles au facteur temps. Par exemple, si le segment contient 30 millions d'utilisateurs mais que nous fixons la limite de débit à 10 000 par minute, une grande partie de votre base d'utilisateurs ne recevra le message que le lendemain.
{% endalert %}

#### Campagnes à canal unique

Lors de l'envoi d'une campagne à canal unique avec une limite de débit, la limite de débit est appliquée à l'ensemble des messages.

#### Campagnes multicanales

Lors de l'envoi d'une campagne multicanal avec une limite de débit, chaque canal est envoyé indépendamment des autres. Par conséquent, les situations suivantes peuvent se produire :

- Le nombre total de messages envoyés par minute pourrait être supérieur à la limite de débit. 
    - Par exemple, si votre campagne a une limite de débit de 10 000 par minute et utilise l'e-mail et le SMS, Braze peut envoyer un maximum de 20 000 messages au total par minute (10 000 e-mails et 10 000 SMS).
- Les utilisateurs pourraient recevoir les différentes chaînes à des moments différents, et il n'est pas possible de prévoir quelle chaîne ils recevront en premier. 
    - Par exemple, si vous envoyez une campagne qui contient un e-mail et un SMS, vous pouvez avoir 10 000 utilisateurs avec des numéros de téléphone valides et 50 000 utilisateurs avec des adresses e-mail valides. Si vous paramétrez la campagne pour qu'elle envoie 100 messages par minute (une limite de débit pour la taille de la campagne), un utilisateur pourrait recevoir le SMS dans le premier lot d'envois et l'e-mail dans le dernier lot d'envois, soit près de neuf heures plus tard.

#### Campagnes de notification push multi-plates-formes

Pour les campagnes push diffusées sur plusieurs plateformes, la limite de débit sélectionnée sera répartie de manière égale entre les plateformes. Une campagne de notification push utilisant Android et iOS avec une limite de débit de 10 000 messages par minute distribuera en parts égales les 10 000 messages sur les deux plates-formes.

#### Limitation de la vitesse de réception/distribution des canevas {#canvas-delivery-speed}

Lors de l'envoi d'un Canvas avec une limite de débit, la limite de débit est partagée entre les canaux. Cela signifie que le nombre total de messages envoyés par minute à partir du Canvas ne dépassera pas la limite de débit. Par exemple, si votre Canvas a une limite de débit de 10 000 par minute et utilise l'e-mail et le SMS, Braze enverra un total de 10 000 messages par minute à travers l'e-mail et le SMS.

#### Limitation du taux et nouvelles tentatives de contenu connecté

Lorsque le [rappel de contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries/) est activé, Braze relance les échecs d'appel tout en respectant la limite de débit que vous avez définie pour chaque renvoi. Prenons le cas d'un envoi de 75 000 messages avec une limite de débit de 10 000 par minute. Imaginez que dans la première minute, l'appel échoue ou est lent et n'envoie que 4 000 messages.

Au lieu d'essayer de rattraper le retard et d'envoyer les 6 000 messages restants dans la deuxième minute ou de les ajouter aux 10 000 messages déjà prêts à être envoyés, Braze déplacera ces 6 000 messages en "fin de file d'attente" et ajoutera une minute, si nécessaire, au nombre total de minutes nécessaires à l'envoi de votre message.

| Minute | Pas de défaillance | 6 000 échecs à la minute 1 |
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

Alors que votre base d'utilisateurs continue de croître et que votre envoi de messages s'étend pour inclure des campagnes sur le cycle de vie, des campagnes déclenchées, des campagnes transactionnelles et des campagnes de conversion, il est important d'éviter que vos messages ne paraissent "spammy" ou dérangeants. En offrant un meilleur contrôle sur l’expérience de vos utilisateurs, la limite de fréquence vous permet de créer les campagnes que vous souhaitez sans surcharger votre audience.

### Aperçu de la fonction User Search {#freq-cap-feat-over}

La limite de fréquence est appliquée au niveau de l'envoi de la campagne ou du composant Canvas et peut être configurée pour chaque espace de travail à partir de **Paramètres** > **Règles de limite de fréquence**.

Par défaut, la limite de fréquence est activée lorsque de nouvelles campagnes sont créées. Vous pouvez choisir ce qui suit :

- Le canal de communication que vous souhaitez plafonner : notifications push, e-mail, SMS, webhook, WhatsApp, ou n’importe lequel de ces cinq canaux.
- Combien de fois chaque utilisateur doit recevoir une campagne ou un composant Canvas envoyé depuis un canal au cours d’un certain laps de temps.
- Combien de fois chaque utilisateur doit recevoir une campagne ou un composant Canvas envoyé par une [étiquette](#frequency-capping-by-tag) dans un certain laps de temps.

Ce délai peut être mesuré en minutes, en jours ou en semaines (sept jours), avec une durée maximale de 30 jours.

Chaque ligne de limites de fréquence sera connectée à l'aide de l'opérateur `AND`, et vous pouvez ajouter jusqu'à 10 règles par espace de travail. De plus, vous pouvez inclure plusieurs plafonds pour les mêmes types de messages. Par exemple, vous pouvez plafonner les utilisateurs pour qu’ils ne dépassent pas une notification push unique par jour et trois par semaine.

![Section de limitation de fréquence avec des listes de campagnes et de toiles auxquelles les règles s'appliquent et ne s'appliquent pas.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %})

#### Comportement lorsque les utilisateurs sont limités en fréquence sur une étape du canvas

Si un utilisateur de Canvas est limité en fréquence en raison des paramètres globaux de limitation de fréquence, il passera immédiatement à l'étape suivante de Canvas. L'utilisateur ne quittera pas le Canvas à cause de la limite de fréquence.

### Règles de livraison

Il peut y avoir des campagnes, comme les messages transactionnels, que vous voulez voir envoyées à l’utilisateur tout le temps, même s’ils ont déjà atteint leur limite de fréquence. Par exemple, une application de livraison peut souhaiter envoyer un e-mail ou une notification push lorsqu’un article est livré, quel que soit le nombre de campagnes reçues par l’utilisateur.

Si vous souhaitez qu'une campagne particulière ne tienne pas compte des règles de limitation de fréquence, vous pouvez le faire dans le tableau de bord de Braze lors de la planification de la réception/distribution de cette campagne en basculant la **limitation de fréquence** sur **OFF**. 

Ensuite, il vous sera demandé si vous souhaitez toujours que cette campagne soit prise en compte dans votre limite de fréquence. Les messages qui comptent pour la limite de fréquence sont inclus dans les calculs du filtre du canal intelligent. Lorsque vous envoyez des [campagnes API]({{site.baseurl}}/developer_guide/rest_api/messaging/#messaging), qui sont souvent transactionnelles, vous avez la possibilité de spécifier qu'une campagne doit ignorer les règles de limite fréquence [dans la demande API]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns) en définissant `override_messaging_limits` sur `true`.

Par défaut, les nouvelles campagnes et les Canevas qui n'obéissent pas aux limites de fréquence ne seront pas non plus pris en compte. Ceci est configurable pour chaque campagne et Canvas.

{% alert note %}
Ce comportement modifie le comportement par défaut lorsque vous désactivez la limitation de fréquence pour une campagne ou un Canvas. Les modifications sont rétro-compatibles et n’affectent pas les messages actuellement actifs.
{% endalert %}

![Section des contrôles de réception/distribution avec la limite de fréquence activée.]({% image_buster /assets/img_archive/frequencycappingupdate.png %})

Les différents canaux d'une campagne multicanal compteront individuellement pour la limite de fréquence. Par exemple, si vous créez une campagne multicanal à la fois avec des notifications push et des e-mails et que vous disposez d’une limite de fréquence pour ces deux canaux, la notification push sera alors comptabilisée pour une campagne de notification push et le message e-mail sera comptabilisé pour une campagne de message e-mail. La campagne comptera également pour une « campagne de n’importe quel type ». Si les utilisateurs sont plafonnés à une seule campagne de notification push et d’e-mail par jour, et qu’un utilisateur reçoit cette campagne multicanal, il ne sera plus éligible aux campagnes de notification push ou d’e-mail pour le reste de la journée (sauf si une campagne ignore les règles de limite de fréquence).

Les messages in-app et les cartes de contenu ne sont pas pris en compte dans le calcul des plafonds des campagnes ou des composants Canvas, quels qu'ils soient.

{% alert important %}
La limite de fréquence globale est planifiée en fonction du fuseau horaire de l’utilisateur et est calculée par jours calendaires et non pas par périodes de 24 heures. Par exemple, si vous configurez une règle de limite de fréquence pour qu’elle n’envoie pas plus d’une campagne par jour, un utilisateur peut recevoir un message à 23 h dans son fuseau horaire local et être éligible à recevoir un autre message une heure plus tard.
{% endalert %}

#### Cas d’utilisation

{% tabs %}
{% tab Cas d'utilisation 1 %}

Supposons que vous définissiez une règle de limite de fréquence qui demande à ce que votre utilisateur reçoive au maximum trois campagnes de notification push ou composants de Canvas par semaine depuis toutes les campagnes ou composant de Canvas.

Si votre utilisateur est censé recevoir trois notifications push, deux messages in-app et une carte de contenu cette semaine, il recevra tous ces messages.

{% endtab %}
{% tab Cas d'utilisation 2 %}

Ce scénario utilise les règles de limitation de fréquence suivantes :

**Lorsque le scénario suivant se produit :**

- Un utilisateur déclenche la même campagne, `Campaign ABC`, trois fois au cours d’une semaine.
- Cet utilisateur déclenche `Campaign ABC` une fois le lundi, une fois le mercredi et une fois le jeudi.

![Section sur la limite de fréquence avec la règle de ne pas envoyer plus de 2 campagnes de notifications push/étapes du canvas de toutes les campagnes/étapes du canvas à un utilisateur toutes les 1 semaines.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Le comportement attendu est alors le suivant :**

- Cet utilisateur recevra les envois de la campagne déclenchés le lundi et le mercredi.
- Cet utilisateur ne recevra pas la troisième campagne envoyée jeudi parce que l’utilisateur a déjà reçu deux campagnes de notification push cette semaine-là.

{% endtab %}
{% endtabs %}

### Limite de fréquence par tag

Les [règles de limitation de fréquence](#delivery-rules) peuvent être appliquées aux espaces de travail à l'aide des tags spécifiques que vous avez appliqués à vos campagnes et à vos toiles, ce qui vous permet essentiellement de baser votre limitation de fréquence sur des groupes aux noms personnalisés.

Avec une limite de fréquence par balise, les règles peuvent être définies sur les balises principales et imbriquées, pour que Braze prenne en compte toutes les balises. Par exemple, si vous avez choisi d’utiliser la balise A principal pour la limite de fréquence, nous inclurons également des informations dans toutes les balises imbriquées (par exemple, les balises B et C) lors de la détermination de la limite.

Vous pouvez également combiner une limite de fréquence régulière avec une limite de fréquence par balises. Prenez en compte les règles suivantes :

1. Pas plus de trois campagnes de notification push ou de composant de Canvas par semaine depuis toutes les campagnes et tous les composants de Canvas. <br>**ET**
2. Pas plus de deux campagnes de notification push ou composant de Canvas par semaine avec la balise `promotional`.

![Section de limitation de fréquence avec deux règles limitant le nombre de campagnes de notification push/de toiles pouvant être envoyées à un utilisateur toutes les semaines.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Par conséquent, vos utilisateurs ne recevront pas plus de trois envois de campagnes par semaine depuis toutes les campagnes et étapes de Canvas et pas plus de deux campagnes de notification push ou de composant de Canvas avec la balise `promotional`.

{% alert important %}
Les Canvas reçoivent leur balise au niveau du Canvas et pas au niveau du composant. Chaque composant Canvas héritera donc des balises au niveau du Canvas.
{% endalert %}

#### Règles contradictoires

Lorsque les règles entrent en conflit, la règle de limite de fréquence la plus restrictive et applicable sera pratiquée pour vos utilisateurs. Par exemple, imaginons que vous ayez les règles suivantes :

1. Pas plus d’une campagne de notification push ou de composant Canvas par semaine depuis toutes les campagnes et tous les composants de Canvas. <br>**ET**
2. Pas plus de trois campagnes de notification push ou de composant Canvas par semaine avec la balise `promotional`.

![Section "Frequency Capping" avec des règles contradictoires pour limiter le nombre de campagnes de notification push/étapes du canvas envoyées à un utilisateur toutes les 1 semaines.]({% image_buster /assets/img/global_rules.png %} "global rules")

Dans cet exemple, votre utilisateur ne recevra pas plus d’une campagne de notification push ou de composants de Canvas avec la balise « promotionnel » pour une semaine donnée, car vous avez spécifié que les utilisateurs ne doivent pas recevoir plus d’une campagne de notification push ou de composant de Canvas depuis toutes les campagnes et composants de Canvas. En d’autres termes, la règle de fréquence applicable la plus restrictive est la règle qui sera appliquée à un utilisateur donné.

#### Nombre de balises

La limite de fréquence par règles de balise est calculée au moment où un message est envoyé. Cela signifie que la limite de fréquence par balise compte uniquement des balises qui sont actuellement sur les campagnes ou les Canvas qu’un utilisateur a reçu par le passé. Il ne compte pas les balises qui étaient sur les campagnes ou les Canvas pendant qu’ils étaient envoyés, mais qui ont depuis été supprimés. Elle comptera si une balise est ajoutée ultérieurement à un message que l’utilisateur a reçu par le passé, mais avant que le dernier message avec la balise soit envoyé.

##### Cas d’utilisation

Considérez la règle de campagne et de limite de fréquence par balise suivante :

**Campagnes**:

- La **campagne A** est une campagne de push étiquetée `promotional`. L'envoi est prévu pour lundi à 9 heures.
- La **campagne B** est une campagne de push étiquetée `promotional`. L'envoi est prévu pour mercredi à 9 heures.

**Limite de fréquence par règle de tag :**

- Votre utilisateur ne doit pas recevoir plus d'une campagne de notification push par semaine avec l'étiquette `promotional`.<br><br>

| Action | Résultat |
|---|---|
| L'étiquette `promotional` est retirée de la **campagne A** après que votre utilisateur a reçu le message, mais avant que **la campagne B ne l'ait envoyé.** | Votre utilisateur recevra la **campagne B.**|
| L'étiquette `promotional` est supprimée par erreur de la **campagne A** après que votre utilisateur a reçu le message. <br> L'étiquette est ajoutée à nouveau à la **campagne A** le mardi, avant l'envoi de la **campagne B**. | Votre utilisateur ne recevra pas la **campagne B.** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Envoi à grande échelle {#sending-at-large-scales}

Les règles de limite de fréquence par balise peuvent ne pas être appliquées correctement à de grandes échelles, comme 100 messages par canal provenant de campagnes ou de composants Canvas.

Par exemple, si votre limite de fréquence par règle de balise est :

> Pas plus de deux campagnes d’e-mail ou de composants Canvas avec la balise `Promotional` pour un utilisateur chaque semaine.

Et que vous envoyez à l’utilisateur plus de 100 e-mails de campagnes et d'étapes de Canvas avec une limite de fréquence activée pour une semaine, plus de deux e-mails peuvent être envoyés à l’utilisateur.

Étant donné que 100 messages par canal constituent plus de messages que ce que la plupart des marques envoient à leurs utilisateurs, il est peu probable que vous soyez affecté par cette limitation. Pour l’éviter, vous pouvez définir un plafond pour le nombre maximum d’e-mails que vous souhaitez que vos utilisateurs reçoivent au cours d’une semaine.

Par exemple, vous pouvez configurer la règle suivante :

> Pas plus de trois campagnes d’e-mail ou de composant Canvas par semaine depuis toutes les campagnes et composants Canvas.

Cette règle garantira qu’aucun utilisateur ne reçoit plus de 100 e-mails par semaine, car, au maximum, les utilisateurs recevront trois e-mails par semaine depuis les campagnes ou les composants Canvas avec une limite de fréquence activée.

