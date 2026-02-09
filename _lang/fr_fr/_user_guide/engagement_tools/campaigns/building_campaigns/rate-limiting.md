---
nav_title: Limitation du taux et limite de fréquence
article_title: Limitation du taux et limite de fréquence
page_order: 6
tool: Campaigns
page_type: reference
description: "Le présent article de référence aborde le concept de limitation du taux et la limite de fréquence dans les campagnes ainsi que la manière dont vous pouvez appliquer une pression marketing pour améliorer l’expérience utilisateur."

---

# Limitation du taux et limite de fréquence

> La limite de débit et la limite de fréquence peuvent être utilisées conjointement pour s'assurer que vos utilisateurs reçoivent les messages dont ils ont besoin.

## À propos de la limite de débit

Braze vous permet de contrôler la pression marketing par taux limitant vos campagnes, ce qui régule la quantité de trafic sortant de votre plate-forme. Vous pouvez mettre en place deux types différents de limite de débit pour vos campagnes : 

1. [**Limite de débit centrée sur l'utilisateur :**](#user-centric-rate-limiting) L'objectif est d'offrir la meilleure expérience possible à l'utilisateur.
2. [**Limitation du débit de réception/distribution :**](#delivery-speed-rate-limiting) Prend en considération la bande passante de vos serveurs.

Braze essaiera de répartir uniformément les envois de messages tout au long de la minute, mais ne peut le garantir. Par exemple, si vous avez une campagne avec une limite de débit de 5 000 messages par minute, nous essaierons de répartir les 5 000 demandes de manière égale tout au long de la minute (environ 84 messages par seconde), mais il peut y avoir une certaine variation dans le débit par seconde.

### Limite de débit centrée sur l'utilisateur

À mesure que vous créez plus de segments, il y aura des cas où l’appartenance à ces segments se chevauche. Si vous envoyez des campagnes à ces segments, vous devez être sûr que vous n’envoyez pas des messages trop souvent à vos utilisateurs. Si un utilisateur reçoit trop de messages sur une courte période, il va se sentir surchargé et désactiver les notifications push ou désinstaller votre application.

#### Filtres de segment pertinents

Braze propose les filtres suivants pour vous aider à limiter le débit auquel vos utilisateurs reçoivent des messages :

- Dernière interaction avec un message
- Dernier message reçu
- Dernière notification push reçue
- Dernier e-mail reçu
- Dernier SMS reçu

#### Implémenter des filtres

Imaginons que nous ayons créé un segment nommé "Vitrine de filtres de reciblage" avec un filtre "Dernière utilisation de l'application il y a plus de 7 jours" pour cibler les utilisateurs. Il s’agit d’un segment de ré-engagement standard.

Si d'autres segments plus ciblés ont reçu des notifications récemment, vous ne voudrez peut-être pas que vos utilisateurs soient ciblés par des campagnes plus génériques destinées à ce segment. En ajoutant le filtre "Last Received Push" à ce segment, l'utilisateur s'est assuré que s'il a reçu une autre notification au cours des dernières 24 heures, il sortira de ce segment pour les 24 heures à venir. S'ils répondent toujours aux autres critères de la segmentation 24 heures plus tard et qu'ils n'ont pas reçu d'autres notifications, ils seront réintégrés dans la segmentation.

![Un segment nommé "Vitrine de filtres de reciblage" avec le groupe d'applications "Dernière utilisation de l'application il y a plus de 7 jours".]({% image_buster /assets/img_archive/rate_limit_daily.png %}){: style="max-width:80%;"} 

En ajoutant ce filtre à tous les segments ciblés par les campagnes, vos utilisateurs ne peuvent recevoir qu’une notification push toutes les 24 heures au maximum. Vous pouvez ensuite prioriser votre messagerie en vous assurant que vos messages les plus importants sont envoyés avant les moins importants.

#### Fixer un plafond d'utilisateurs

Dans l'étape **Audiences cibles** du compositeur de votre campagne, vous pouvez également limiter le nombre total d'utilisateurs qui recevront votre message. Il s'agit d'un contrôle indépendant des filtres de votre campagne.

![Résumé de l'audience avec une case à cocher pour limiter le nombre de personnes qui reçoivent la campagne.]({% image_buster /assets/img_archive/total_limit.png %}){: style="max-width:50%;"} 

En sélectionnant la limite maximale de l'utilisateur, vous pouvez limiter le volume des messages envoyés par canal ou globalement pour tous les types de messages.

##### Nombre maximum d'utilisateurs avec optimisations

Si vous utilisez une optimisation telle que la variante gagnante ou la variante personnalisée, la campagne comprendra deux envois : l'expérience initiale et l'envoi final. 

Pour implémenter un plafond d'utilisateurs dans ce scénario, sélectionnez **Limiter le nombre de personnes qui recevront cette campagne**, puis sélectionnez **Au total, cette campagne doit** et entrez une limite d'audience. La limite de votre audience sera divisée selon les pourcentages indiqués dans le panneau de **test A/B.**  

Si vous sélectionnez **Chaque fois que la campagne est planifiée**, ces deux phases seront limitées séparément au nombre défini. Ce n’est généralement pas souhaitable.

#### Fixer un plafond d'impressions pour les campagnes

Pour les messages in-app, vous pouvez contrôler la pression marketing en définissant un nombre maximum d’impressions qui seront affichées à votre base d’utilisateurs, après quoi Braze n’enverra plus de messages à vos utilisateurs. Cependant, il est important de noter que ce plafond n’est pas exact. 

Les règles relatives aux messages in-app sont envoyées à une application au début de la session, ce qui signifie que Braze peut envoyer un message à l'utilisateur avant que le plafond ne soit atteint, mais au moment où l'utilisateur déclenche le message, le plafond a déjà été atteint. Dans cette situation, l’appareil affichera quand même le message.

Supposons par exemple que vous ayez un jeu avec un message in-app qui se déclenche quand un utilisateur bat un niveau et que vous l’ayez plafonné à 100 impressions. Jusqu’à présent, il y a eu 99 impressions. Alice et Bob ouvrent tous deux le jeu et Braze indique à leurs appareils qu'ils peuvent recevoir le message lorsqu'ils ont franchi un niveau. Alice bat un niveau en premier et reçoit le message. Bob atteint le niveau suivant, mais comme son appareil n'a pas communiqué avec les serveurs de Braze depuis le début de sa session, son appareil ignore que le message a atteint son plafond, et il reçoit également le message. Toutefois, lorsqu'un plafond d'impression a été atteint, la prochaine fois qu'un appareil demande la liste des messages in-app éligibles, le système n'envoie pas ce message et le supprime de cet appareil.

### Limite de débit et test A/B

Lorsque vous utilisez la limite de débit avec un test A/B, la limite de débit n'est pas appliquée au groupe de contrôle de la même manière qu'au groupe de test, ce qui constitue une source potentielle de biais temporel. Pour éviter ce biais, utilisez des fenêtres de conversion appropriées.

### Limiter le taux de vitesse de livraison

Si vous prévoyez que de grandes campagnes entraîneront un pic d'activité des utilisateurs et une surcharge de vos serveurs, vous pouvez spécifier une limite de débit par minute pour l'envoi des messages, ce qui signifie que Braze n'envoie pas plus que votre paramètre de limite de débit en l'espace d'une minute.

Lorsque vous ciblez des utilisateurs lors de la création d'une campagne, vous pouvez accéder à **Target Audiences** (pour les campagnes) ou **Send Settings** (pour les Canvas) pour sélectionner une limite de débit (dans différents incréments allant de 10 à 500 000 messages par minute).

Notez que les campagnes sans limitation du taux peuvent dépasser ces limites de livraison. Toutefois, sachez que les messages seront interrompus s'ils sont retardés de 72 heures ou plus en raison d'une limite de débit trop basse. Si la limite de débit est trop basse, le créateur de la campagne recevra des alertes dans le tableau de bord et par e-mail.

#### Exemple

Si vous essayez d'envoyer 75 000 messages avec une limite de débit de 10 000 par minute, la réception/distribution sera étalée sur huit minutes. Votre campagne ne diffusera pas plus de 10 000 messages pour chacune des sept premières minutes, et 5 000 au cours de la dernière minute.

#### Nombre d'envois

Notez que les messages à débit limité peuvent ne pas être envoyés de manière régulière au cours de chaque minute. Si l'on prend l'exemple d'une limite de débit de 10 000 par minute, cela signifie que Braze veille à ce qu'il n'y ait pas plus de 10 000 messages envoyés par minute. Cela pourrait signifier qu'un pourcentage plus élevé des 10 000 messages est envoyé dans la première demi-minute par rapport à la dernière demi-minute.

La limite de débit est appliquée au début de la tentative d'envoi du message. En cas de fluctuations de la durée de l'envoi, le nombre d'envois terminés peut légèrement dépasser la limite de débit pendant quelques minutes. Avec le temps, le nombre d'envois par minute se stabilisera au niveau de la limite de débit.

{% alert important %}
Cette forme de limitation de débit par rapport au nombre total d'utilisateurs dans un segment permet de ne pas retarder les envois de messages sensibles au facteur temps. Par exemple, si le segment contient 30 millions d'utilisateurs mais que nous fixons la limite de débit à 10 000 par minute, une grande partie de votre base d'utilisateurs ne recevra le message que le lendemain.
{% endalert %}

#### Campagnes et canevas multicanaux

Lorsque vous définissez une limite de vitesse de réception/distribution pour une campagne multicanal ou un Canvas, vous pouvez choisir de définir une limite de débit partagée ou une limite basée sur le canal.

Lorsqu'une campagne multicanale ou un Canvas utilise une limite de débit partagée, cela signifie que le nombre total de messages envoyés par minute depuis la campagne ou le Canvas ne dépasse pas la limite de débit. Par exemple, si votre Canvas a une limite de débit de 500 000 par minute et contient des étapes de messages e-mail et SMS, Braze envoie un total de 500 000 messages par minute par e-mail et SMS.

![L'option permettant de limiter le débit d'envoi de la campagne, sélectionnée avec 500 000 messages par minute.]({% image_buster /assets/img_archive/multichannel_campaigns_rate_limit.png %}){: style="max-width:50%;"} 

Lorsqu'une campagne multicanal ou un Canvas utilise une limite de débit basée sur le canal, la limite de débit s'appliquera à chacun de vos canaux sélectionnés. Par exemple, vous pouvez paramétrer votre campagne ou Canvas pour qu'elle envoie un maximum de 5 000 webhooks et 2 500 messages SMS par minute sur l'ensemble de la campagne ou du Canvas.

![Limites de débit distinctes pour deux canaux, webhook et SMS/MMS/RCS, avec respectivement 5 000 et 2 500 messages par minute.]({% image_buster /assets/img_archive/channel_rate_limits.png %}){: style="max-width:70%;"}

##### Notifications push

Pour les campagnes ou Canvas avec des plateformes push (comme Android, iOS, Web Push ou Kindle), vous pouvez sélectionner **Notifications push** pour appliquer une limite de débit partagée entre toutes les plateformes push de votre campagne ou Canvas.

![Le menu déroulant du canal avec des options pour les plateformes et les notifications push.]({% image_buster /assets/img_archive/push_notifications_rate_limit.png %}){: style="max-width:30%;"} 

{% alert note %}
Si vous sélectionnez une limite pour les notifications push, vous ne pouvez pas définir de limites de débit pour les canaux push individuels. De même, si vous sélectionnez des limites pour des canaux push individuels, vous ne pouvez pas définir de limites pour les notifications push partagées.
{% endalert %}

{% alert important %}
**Mises à jour de l'interface de limitation de débit**<br>
Braze a mis à jour l'interface de limitation de débit pour offrir plus de transparence et de contrôle sur la façon dont les limites de débit s'appliquent aux campagnes multicanal et aux Canvases.<br><br>

- **Campagnes et toiles existantes :** Toutes les campagnes et canevas existants ont été migrés vers cette interface. Leur comportement en matière de réception/distribution reste le même. Le tableau de bord indique si la campagne utilise une logique partagée ou par canal.<br>
- **Nouvelles campagnes et toiles :** Pour toutes les nouvelles campagnes et canevas, un basculeur manuel permet de choisir votre logique de limite de débit préférée. Veillez à sélectionner le comportement de limitation du débit qui s'aligne sur celui que vous souhaitez lors de la définition ou de la mise à jour de la limite de débit d'une campagne ou d'un Canvas.
{% endalert %}

##### Considérations relatives à la limite de débit

Quelques remarques à garder à l'esprit lors de la configuration des limites de débit et du comportement auquel vous devez vous attendre :

- Les envois de SMS sont soumis à une limite de débit de 50 000 par groupe d'abonnement. Certains fournisseurs de SMS peuvent imposer d'autres limites.
- Les messages suivants ne sont pas soumis à la limite de débit et ne sont pas pris en compte dans le calcul de celle-ci :
    - Envois de tests
    - Groupes initiateurs
    - Cartes de contenu configurées pour créer "à la première impression" (Cela sera contrôlé par le taux d'impressions des apps. Reportez-vous à la section [Création de cartes]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences) pour plus d'informations sur les différences entre les options de création de cartes).
- Les limites de débit de réception/distribution ne sont pas prises en charge dans les cas suivants :
    - Réponses automatiques par SMS
    - Envois garantis par des accords de niveau de service (tels que l'[e-mail transactionnel]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign))
    - in-app Messages
    - Indicateurs de fonctionnalité
    - Bannières

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

Les demandes de contenu connecté ne sont pas soumises à une limite de débit indépendante et suivent la limite de débit du webhook. Cela signifie que s'il y a un appel de contenu connecté à un endpoint unique par webhook, vous devriez vous attendre à 5 000 webhooks et également à 5 000 appels de contenu connecté par minute. Notez que la mise en cache peut avoir une incidence sur ce point et réduire le nombre d'appels au contenu connecté. En outre, les tentatives peuvent augmenter le nombre d'appels au contenu connecté. Nous vous recommandons donc de vérifier que le point de terminaison du contenu connecté peut supporter une certaine fluctuation à ce niveau.

## À propos de la limite de fréquence

Alors que votre base d'utilisateurs continue de croître et que votre envoi de messages s'étend pour inclure des campagnes sur le cycle de vie, des campagnes déclenchées, des campagnes transactionnelles et des campagnes de conversion, il est important d'éviter que vos messages ne paraissent "spammy" ou dérangeants. En offrant un meilleur contrôle sur l’expérience de vos utilisateurs, la limite de fréquence vous permet de créer les campagnes que vous souhaitez sans surcharger votre audience.

### Aperçu de la fonction User Search {#freq-cap-feat-over}

La limite de fréquence est appliquée au niveau de l'envoi de la campagne ou du composant Canvas et peut être configurée pour chaque espace de travail à partir de **Paramètres** > **Règles de limite de fréquence**.

Par défaut, la limite de fréquence est activée lorsque de nouvelles campagnes sont créées. Vous pouvez choisir ce qui suit :

- Le canal de messages que vous souhaitez capter : push, e-mail, SMS, webhook, WhatsApp, LINE, ou n'importe lequel de ces canaux.
- Combien de fois chaque utilisateur doit recevoir une campagne ou un composant Canvas envoyé par un canal dans un certain laps de temps.
- Combien de fois chaque utilisateur doit recevoir une campagne ou un composant Canvas envoyé par l'[étiquette](#frequency-capping-by-tag) dans un certain laps de temps.

Ce délai peut être mesuré en minutes, en jours ou en semaines (sept jours), avec une durée maximale de 30 jours.

Chaque ligne de limites de fréquence est reliée à l'aide de l'opérateur `AND`, et vous pouvez ajouter jusqu'à 10 règles par espace de travail. Vous pouvez inclure plusieurs plafonds pour les mêmes types de messages. Par exemple, vous pouvez plafonner les utilisateurs pour qu’ils ne dépassent pas une notification push unique par jour et trois par semaine. Notez que les messages interrompus ne sont pas pris en compte dans la limite de fréquence.

![Section sur la limite de fréquence avec des listes de campagnes et de toiles auxquelles les règles s'appliqueront et ne s'appliqueront pas.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %}){: style="max-width:90%;"} 

#### Comportement lorsque les utilisateurs sont limités en fréquence sur une étape du canvas

Si un utilisateur Canvas est limité en fréquence en raison des paramètres globaux de limitation de fréquence, il passera immédiatement à l'étape suivante de Canvas. L'utilisateur ne quittera pas le Canvas à cause de la limite de fréquence.

### Règles de livraison

Il peut y avoir des campagnes, comme les messages transactionnels, que vous voulez voir envoyées à l’utilisateur tout le temps, même s’ils ont déjà atteint leur limite de fréquence. Par exemple, une appli de réception/distribution peut souhaiter envoyer un e-mail ou un push lorsqu'un article est livré, quel que soit le nombre de campagnes reçues par l'utilisateur.

Si vous souhaitez qu'une campagne particulière ne tienne pas compte des règles de limitation de fréquence, vous pouvez le faire dans le tableau de bord de Braze lors de la planification de la réception/distribution de cette campagne en basculant la **limitation de fréquence** sur **OFF**. 

Ensuite, il vous sera demandé si vous souhaitez toujours que cette campagne soit prise en compte dans votre limite de fréquence. Les messages qui comptent pour la limite de fréquence sont inclus dans les calculs du filtre du canal intelligent. 

Lorsque vous envoyez des [campagnes API]({{site.baseurl}}/developer_guide/rest_api/messaging/#messaging), qui sont souvent transactionnelles, vous avez la possibilité de spécifier qu'une campagne doit ignorer les règles de limitation de fréquence en définissant `override_frequency_capping` sur `true` dans la demande API.

Par défaut, les nouvelles campagnes et les Canevas qui n'obéissent pas aux limites de fréquence ne seront pas non plus pris en compte. Ceci est configurable pour chaque campagne et Canvas.

{% alert note %}
Ce comportement modifie le comportement par défaut lorsque vous désactivez la limitation de fréquence pour une campagne ou un Canvas. Les modifications sont rétro-compatibles et n’affectent pas les messages actuellement actifs.
{% endalert %}

![Section des contrôles de réception/distribution avec la limite de fréquence activée.]({% image_buster /assets/img_archive/frequencycappingupdate.png %}){: style="max-width:90%;"} 

Les différents canaux d'une campagne multicanal sont pris en compte individuellement dans le calcul de la limite de fréquence. Par exemple, si vous créez une campagne multicanal avec des messages push et des e-mails et que vous avez défini une limite de fréquence pour ces deux canaux, les messages push sont comptabilisés dans une campagne push et les messages e-mail sont comptabilisés dans une campagne e-mail. La campagne compte également pour une "campagne de tout type". Si les utilisateurs sont limités à une campagne push et une campagne e-mail par jour, et qu'un utilisateur reçoit cette campagne multicanal, il n'est plus éligible aux campagnes push ou e-mail pour le reste de la journée (sauf si une campagne ignore les règles de limitation de fréquence).

Les messages in-app et les cartes de contenu ne sont pas pris en compte dans le calcul des plafonds des campagnes ou des composants Canvas, quels qu'ils soient.

{% alert important %}
La limite de fréquence globale est planifiée en fonction du fuseau horaire de l’utilisateur et est calculée par jours calendaires et non pas par périodes de 24 heures. Par exemple, si vous configurez une règle de limite de fréquence pour qu’elle n’envoie pas plus d’une campagne par jour, un utilisateur peut recevoir un message à 23 h dans son fuseau horaire local et être éligible à recevoir un autre message une heure plus tard.
{% endalert %}

#### Cas d'utilisation

{% tabs %}
{% tab Use case 1 %}

Imaginons que vous définissiez une règle de limite de fréquence afin que vos utilisateurs ne reçoivent pas plus de trois campagnes de notifications push ou étapes du canvas par semaine, toutes campagnes ou étapes du canvas confondues.

Si votre utilisateur est censé recevoir trois notifications push, deux messages in-app et une carte de contenu cette semaine, il recevra tous ces messages.

{% endtab %}
{% tab Use case 2 %}

Ce scénario utilise une règle de limite de fréquence pour que les utilisateurs ne reçoivent pas plus de deux campagnes de notifications push ou étapes du canvas par semaine, toutes campagnes ou étapes du canvas confondues.

**Lorsque le scénario suivant se produit :**

- Un utilisateur déclenche la même campagne `Campaign ABC` trois fois au cours d'une semaine.
- Cet utilisateur déclenche `Campaign ABC` une fois le lundi, une fois le mercredi et une fois le jeudi.

![Section Limite de fréquence avec la règle de ne pas envoyer plus de 2 campagnes de notifications push/étapes canvas de toutes les campagnes/étapes canvas à un utilisateur toutes les 1 semaines.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Le comportement attendu est alors le suivant :**

- Cet utilisateur recevra les envois de la campagne déclenchés le lundi et le mercredi.
- Cet utilisateur ne recevra pas la troisième campagne envoyée jeudi parce que l’utilisateur a déjà reçu deux campagnes de notification push cette semaine-là.

{% endtab %}
{% endtabs %}

### Limite de fréquence par tag

Les [règles de limitation de fréquence](#delivery-rules) peuvent être appliquées aux espaces de travail à l'aide des tags spécifiques que vous avez appliqués à vos campagnes et à vos toiles, ce qui vous permet essentiellement de baser votre limitation de fréquence sur des groupes aux noms personnalisés.

Avec une limite de fréquence par balise, les règles peuvent être définies sur les balises principales et imbriquées, pour que Braze prenne en compte toutes les balises. Par exemple, si vous avez choisi d'utiliser l'étiquette principale A comme limite de fréquence, nous inclurons également les informations contenues dans toutes les étiquettes imbriquées (par exemple, les étiquettes B et C) lors de la détermination de la limite.

Vous pouvez également combiner une limite de fréquence régulière avec une limite de fréquence par balises. Prenez en compte les règles suivantes :

1. Pas plus de trois campagnes de notifications push ou composants Canvas par semaine, toutes campagnes et étapes Canvas confondues. <br>**ET**
2. Pas plus de deux campagnes de notification push ou composants Canvas par semaine avec l'étiquette `promotional`.

![Section "Frequency Capping" avec deux règles limitant le nombre de campagnes de notification push/canvas pouvant être envoyées à un utilisateur toutes les 1 semaines.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Par conséquent, vos utilisateurs ne recevront pas plus de trois envois de campagnes par semaine depuis toutes les campagnes et étapes de Canvas et pas plus de deux campagnes de notification push ou de composant de Canvas avec la balise `promotional`.

{% alert important %}
Les Canvas reçoivent leur balise au niveau du Canvas et pas au niveau du composant. Ainsi, chaque composant Canvas héritera de toutes les étiquettes de niveau Canvas.
{% endalert %}

#### Règles contradictoires

En cas de conflit entre les règles, c'est la règle de limite de fréquence la plus restrictive qui s'applique à vos utilisateurs. Par exemple, imaginons que vous ayez les règles suivantes :

1. Pas plus d'une campagne de notification push ou d'un composant Canvas par semaine, toutes campagnes et composants Canvas confondus. <br>**ET**
2. Pas plus de trois campagnes de notification push ou de composant Canvas par semaine avec la balise `promotional`.

![Section Limite de fréquence avec des règles contradictoires pour limiter le nombre de campagnes de notifications push/étapes du canvas envoyées à un utilisateur toutes les 1 semaines.]({% image_buster /assets/img/global_rules.png %} "global rules")

Dans cet exemple, votre utilisateur ne recevra pas plus d’une campagne de notification push ou de composants de Canvas avec la balise « promotionnel » pour une semaine donnée, car vous avez spécifié que les utilisateurs ne doivent pas recevoir plus d’une campagne de notification push ou de composant de Canvas depuis toutes les campagnes et composants de Canvas. En d’autres termes, la règle de fréquence applicable la plus restrictive est la règle qui sera appliquée à un utilisateur donné.

#### Nombre de balises

La limite de fréquence par les règles d'étiquette est calculée au moment de l'envoi d'un message. Cela signifie que la limite de fréquence par balise compte uniquement des balises qui sont actuellement sur les campagnes ou les Canvas qu’un utilisateur a reçu par le passé. Il ne tient pas compte des tags qui se trouvaient sur les campagnes ou les toiles au moment où elles ont été envoyées, mais qui ont été retirés depuis. Il compte si une étiquette est ajoutée ultérieurement à un message qu'un utilisateur a reçu dans le passé, mais avant que le dernier message étiqueté ne soit envoyé.

##### Cas d’utilisation

Considérez la règle de campagne et de limite de fréquence par balise suivante :

**Campagnes**:

- La **campagne A** est une campagne de push étiquetée `promotional`. L'envoi est prévu pour lundi à 9 heures.
- La **campagne B** est une campagne de push étiquetée `promotional`. L'envoi est prévu pour mercredi à 9 heures.

**Limite de fréquence par règle de tag :**

- Votre utilisateur ne doit pas recevoir plus d'une campagne de notification push par semaine avec l'étiquette `promotional`.<br><br>

| Action | Résultat |
|---|---|
| L'étiquette `promotional` est retirée de la **campagne A** après que votre utilisateur a reçu le message, mais avant que **la campagne B ne l'ait envoyé.** | Votre utilisateur reçoit la **campagne B.**|
| L'étiquette `promotional` est supprimée par erreur de la **campagne A** après que votre utilisateur a reçu le message. <br> L'étiquette est ajoutée à nouveau à la **campagne A** le mardi, avant l'envoi de la **campagne B**. | Votre utilisateur ne reçoit pas la **campagne B.** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Envoi à grande échelle {#sending-at-large-scales}

Les règles de limite de fréquence par balise peuvent ne pas être appliquées correctement à de grandes échelles, comme 100 messages par canal provenant de campagnes ou de composants Canvas.

Par exemple, si votre limite de fréquence par règle de balise est :

> Pas plus de deux campagnes d’e-mail ou de composants Canvas avec la balise `Promotional` pour un utilisateur chaque semaine.

Et que vous envoyez à l’utilisateur plus de 100 e-mails de campagnes et d'étapes de Canvas avec une limite de fréquence activée pour une semaine, plus de deux e-mails peuvent être envoyés à l’utilisateur.

Étant donné que 100 messages par canal représentent plus de messages que ce que la plupart des marques envoient à leurs utilisateurs, il est peu probable que cette limitation ait un impact. Pour l’éviter, vous pouvez définir un plafond pour le nombre maximum d’e-mails que vous souhaitez que vos utilisateurs reçoivent au cours d’une semaine.

Par exemple, vous pouvez configurer la règle suivante :

> Pas plus de trois campagnes d'e-mail ou éléments de Canvas par semaine, toutes campagnes et étapes du Canvas confondues.

Cette règle détermine qu'aucun utilisateur ne reçoit plus de 100 e-mails par semaine car, au maximum, les utilisateurs reçoivent trois e-mails par semaine provenant de campagnes ou de composants Canvas pour lesquels la limite de fréquence est activée.

