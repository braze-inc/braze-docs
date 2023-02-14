---
nav_title: Limitation du taux et limite de fréquence
article_title: Limitation du taux et limite de fréquence
page_order: 6
tool: Campagnes
page_type: reference
description: "Le présent article de référence aborde le concept de limitation du taux et la limite de fréquence dans les campagnes ainsi que la manière dont vous pouvez appliquer une pression marketing pour améliorer l’expérience utilisateur."

---

# Limitation du taux et limite de fréquence

> Le présent article de référence aborde le concept de limitation du taux et la limite de fréquence dans les campagnes ainsi que la manière dont vous pouvez appliquer cette pression marketing pour améliorer l’expérience utilisateur.
> <br>
> <br>
> Nous voulons tous que nos utilisateurs aient la meilleure expérience possible. Avec la limitation du taux et la limite de fréquence, vous pouvez vous assurer que vos utilisateurs reçoivent le message dont ils ont besoin et aucun de ceux dont ils n’ont pas besoin.

## Limitation du taux

Braze vous permet de contrôler la pression marketing par taux limitant vos campagnes, ce qui régule la quantité de trafic sortant de votre plateforme. Vous pouvez mettre en œuvre deux types différents de limitation tarifaire pour vos campagnes. Le premier se concentre sur fournir la meilleure expérience pour l’utilisateur, tandis que le second prend en compte la bande passante de vos serveurs.

### Limitation du taux centrée sur l’utilisateur

À mesure que vous créez plus de segments, il y aura des cas où l’appartenance à ces segments se chevauche. Si vous envoyez des campagnes à ces segments, vous devez être sûr que vous n’envoyez pas des messages trop souvent à vos utilisateurs. Si un utilisateur reçoit trop de messages sur une courte période, il va se sentir surchargé et désactiver les notifications push ou désinstaller votre application.

#### Filtres de segment pertinents

Braze fournit les filtres suivants afin de vous aider à limiter le taux auquel vos utilisateurs reçoivent des messages :

- Dernière interaction avec un message
- Dernier message reçu
- Dernière campagne de notification push reçue
- Dernière campagne e-mail reçue
- Dernier SMS reçu
- Dernier fil d’actualité vu

#### Implémenter des filtres

Supposons que nous avons créé un segment nommé « Vitrine de filtres de reciblage » avec un filtre « Dernière utilisation de ces applications il y a plus de 7 jours » pour cibler les utilisateurs. Il s’agit d’un segment de ré-engagement standard.

Si vous avez d’autres segments plus ciblés recevant des notifications récemment, vous ne voulez peut-être pas que vos utilisateurs soient ciblés par des campagnes plus génériques dirigées vers ce segment. En ajoutant le filtre « Dernière campagne de notification push reçue » à ce segment, l’utilisateur est assuré que, s’il a reçu une autre notification au cours des dernières 24 heures, il sortira de ce segment pendant les 24 prochaines heures. S’il répond toujours aux autres critères du segment 24 heures plus tard et n’a pas reçu de notifications supplémentaires, il reprendra sa place dans le segment.

![][1]

En ajoutant ce filtre à tous les segments ciblés par les campagnes, vos utilisateurs ne peuvent recevoir qu’une notification push toutes les 24 heures au maximum. Vous pouvez ensuite prioriser votre messagerie en vous assurant que vos messages les plus importants sont envoyés avant les moins importants.

#### Régler un plafond d’utilisateurs maximal

Dans l’étape **Target Users (Utilisateurs cibles)** de la composition de votre campagne, vous pouvez également limiter le nombre total d’utilisateurs qui recevront votre message. Cette fonctionnalité sert de vérification indépendante de vos filtres de campagne, ce qui vous permet de segmenter librement les utilisateurs sans avoir à vous soucier de produire trop de courriers indésirables.

![][2]

En sélectionnant la limite maximale d’utilisateurs, vous pouvez limiter le débit auquel vos utilisateurs reçoivent des notifications par canal ou globalement dans tous les types de messages.

#### Régler un plafond d’impressions maximal

Pour les messages in-app, vous pouvez contrôler la pression marketing en définissant un nombre maximum d’impressions qui seront affichées à votre base d’utilisateurs, après quoi Braze n’enverra plus de messages à vos utilisateurs. Cependant, il est important de noter que ce plafond n’est pas exact. Les nouvelles règles de messages in-app sont envoyées à l’application au démarrage de session, ce qui signifie que Braze peut envoyer un message in-app à l’utilisateur avant que le plafond ne soit atteint, mais lorsque l’utilisateur déclenche le message, il l’est. Dans cette situation, l’appareil affichera quand même le message.

Supposons par exemple que vous ayez un jeu avec un message in-app qui se déclenche quand un utilisateur bat un niveau et que vous l’ayez plafonné à 100 impressions. Jusqu’à présent, il y a eu 99 impressions. Alice et Bob ouvrent tous deux le jeu et Braze dit à leurs appareils qu’ils sont admissibles à recevoir le message lorsqu’ils battent un niveau. Alice bat un niveau en premier et reçoit le message. Bob bat le niveau suivant, mais puisque son appareil n’a pas communiqué avec les serveurs de Braze depuis son ouverture de session, il n’est pas conscient que le message a atteint son plafond et il recevra également le message. Cependant, une fois que le plafond d’impression a été atteint, la prochaine fois que l’appareil demandera la liste des messages in-app éligibles, ce message ne sera pas envoyé et sera supprimé de l’appareil.

### Limiter le taux de vitesse de livraison

Si vous anticipez de grandes campagnes qui génèrent un pic dans l’activité utilisateur et surchargent vos serveurs, vous pouvez spécifier une limitation du débit par minute pour l’envoi de messages. Lors du ciblage des utilisateurs lors de la création de la campagne, vous pouvez naviguer vers les « Advanced Options » (Options avancées) pour sélectionner une limite de débit (avec plusieurs incrémentations depuis 50 jusqu’à 500 000 messages par minute). Notez que les campagnes sans limitation du taux peuvent dépasser ces limites de livraison. Sachez toutefois que les messages seront abandonnés s’ils sont retardés de 72 heures ou plus en raison d’une limite de débit faible. L’utilisateur qui a créé la campagne recevra des alertes dans le tableau de bord et par e-mail si la limitation du débit est trop basse.

![][3]

Par exemple, si vous essayez d’envoyer 75 000 messages avec une limitation du débit à 10 000 par minute, l’envoi sera étalé sur 8 minutes. Votre campagne va en envoyer 10 mille pour chacune des sept premières minutes et 5 000 pour la dernière minute. Évitez cependant de retarder les messages urgents avec cette forme de limitation du débit. Si le segment contient 30 millions d’utilisateurs mais que nous définissons la limite de débit à 10 000 par minute, une grande partie de la base utilisateur ne recevra pas le message avant le jour suivant.

{% alert important %}
Lorsque vous envoyez une campagne multicanale avec une limite de débit, chaque canal est envoyé indépendamment des autres. L’effet est que les utilisateurs peuvent recevoir les différents canaux à différents moments et il n’est pas possible de prédire le canal qu’ils obtiendront en premier. Par exemple, si vous envoyez une campagne contenant un e-mail et une notification push, vous pouvez avoir 10 000 utilisateurs avec des jetons de notification push valides, mais 50 000 utilisateurs avec des adresses e-mail valides. Si vous définissez la campagne pour qu’elle envoie 100 messages par minute (une limite de débit lente pour la taille de la campagne), un utilisateur peut recevoir la notification push dans le premier lot d’envoi et l’e-mail dans le dernier lot d’envois, presque neuf heures plus tard.
{% endalert %}

#### Limitation du taux et nouvelles tentatives de contenu connecté

Lorsque la fonction [Nouvelle tentative de contenu connecté][19] est activée, Braze tentera à nouveau les appels qui ont échoué tout en respectant la limite de débit que vous avez définie pour chaque renvoi. Prenons à nouveau les 75 000 messages avec une limite de débit de 10 000 par minute. Dans la première minute, l’appel échoue ou est lent et envoie seulement 4 000 messages.

Au lieu d’essayer de compenser le retard et d’envoyer les 4 000 messages restants dans la deuxième minute ou de les ajouter aux 10 000 personnes qu’il a déjà définies pour l’envoi, Braze placera ces 6 000 échecs au « fond de la file d’attente » et ajoutera une minute supplémentaire, si nécessaire, au nombre total de minutes qu’il faudrait pour envoyer votre message à tous.

|Minute|Pas de défaillance|6 000 échecs à la minute 1|
|---|---|---|
|1|10 000|4 000|
|2|10 000|10 000|
|3|10 000|10 000|
|4|10 000|10 000|
|5|10 000|10 000|
|6|10 000|10 000|
|7|10 000|10 000|
|8|5 000|10 000|
|9|0|6 000|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Campagnes multicanales

Gardez à l’esprit que la limite de débit par minute est ajustée par campagne. Si plusieurs canaux sont utilisés au sein d’une campagne, la limite de débit s’appliquera à chacun de ces canaux. Si votre campagne utilise des bannières e-mail et in-app avec une limite de débit de 10 000 par minute, nous enverrons 20 000 messages au total chaque minute (10 000 e-mails et 10 000 notifications push).

#### Campagnes de notification push multi-plates-formes

Pour les campagnes de notification push envoyant sur plusieurs plates-formes, la limite de débit sélectionnée sera répartie de manière égale sur les plates-formes. Une campagne de notification push utilisant Android, iOS et Windows avec une limite de débit de 10 000 messages par minute distribuera en parts égales les 10 000 messages sur les trois plates-formes.

## Limite de fréquence

Alors que votre base d’utilisateurs continue de croître et que l’ampleur de vos messages augmente pour intégrer des campagnes de cycle de vie, déclenchées, transactionnelles et de conversion, il est important d’empêcher vos notifications de devenir indésirables ou perturbatrices. En offrant un meilleur contrôle sur l’expérience de vos utilisateurs, la limite de fréquence vous permet de créer les campagnes que vous souhaitez sans surcharger votre audience.

### Aperçu de la fonctionnalité {#freq-cap-feat-over}

La limite de fréquence est appliquée au niveau de l’envoi de la campagne ou du composant Canvas et peut être configurée pour chaque groupe d’apps en sélectionnant **Global Message Settings** qui peut être trouvé dans l’onglet **Engagement**. Par défaut, la limite de fréquence est activée lorsque de nouvelles campagnes sont créées. Vous pouvez choisir ce qui suit :

- Quel canal de messagerie vous souhaitez plafonner : notification push, e-mail, SMS, webhook ou n’importe lequel des quatre.
- Combien de fois chaque utilisateur doit recevoir une campagne ou un composant Canvas envoyé depuis un canal au cours d’un certain laps de temps.
- Combien de fois chaque utilisateur doit recevoir une campagne ou un composant Canvas envoyé par [balise](#frequency-capping-by-tag) au cours d’un certain laps de temps.

Cette période peut être mesurée en minutes, jours, semaines (sept jours) ou mois, avec une durée maximale de 30 jours.

Chaque ligne de limite de fréquence sera connectée à l’aide de l’opérateur `AND` et vous pouvez ajouter jusqu’à 10 règles par groupe d’apps. De plus, vous pouvez inclure plusieurs plafonds pour les mêmes types de messages. Par exemple, vous pouvez plafonner les utilisateurs pour qu’ils ne dépassent pas une notification push unique par jour et trois par semaine.

![][14]

### Règles de livraison

Il peut y avoir des campagnes, comme les messages transactionnels, que vous voulez voir envoyées à l’utilisateur tout le temps, même s’ils ont déjà atteint leur limite de fréquence. Par exemple, une application de livraison peut souhaiter envoyer un e-mail ou une notification push lorsqu’un article est livré, quel que soit le nombre de campagnes reçues par l’utilisateur.

Si vous souhaitez qu’une campagne particulière passe outre aux règles de limite de fréquence, vous pouvez le configurer dans le tableau de bord de Braze lors de la planification de la livraison de cette campagne en basculant **Limite de fréquence** sur **DÉSACTIVER**. 

Après cela, on vous demandera si vous souhaitez toujours que cette campagne compte dans votre limite de fréquence. Les messages qui comptent dans la limite de fréquence sont inclus dans les calculs du filtre de canal intelligent. Lors de l’envoi de [campagnes API][15], qui sont souvent transactionnelles, vous aurez la possibilité de spécifier qu’une campagne doit ignorer les règles de limite de fréquence [dans la requête API][16] en réglant `override_messaging_limits` sur `true`.

Par défaut, les nouvelles campagnes et les Canvas qui ne suivent pas les limites de fréquence ne compteront pas pour elles. Ceci est configurable pour chaque campagne et Canvas.

{% alert note %}
Ce comportement modifie le comportement par défaut lorsque vous désactivez la limitation de fréquence pour une campagne ou un Canvas. Les modifications sont rétro-compatibles et n’affectent pas les messages actuellement actifs.
{% endalert %}

![][18]

Différents canaux au sein d’une campagne multicanale compteront individuellement dans la limite de fréquence. Par exemple, si vous créez une campagne multicanale à la fois avec des notifications push et des e-mails et que vous disposez d’une limite de fréquence pour ces deux canaux, la notification push sera alors comptabilisée pour une campagne de notification push et le message e-mail sera comptabilisé pour une campagne de message e-mail. La campagne comptera également pour une « campagne de n’importe quel type ». Si les utilisateurs sont plafonnés à une seule campagne de notification push et d’e-mail par jour, et qu’un utilisateur reçoit cette campagne multicanale, il ne sera plus éligible aux campagnes de notification push ou d’e-mail pour le reste de la journée (sauf si une campagne ignore les règles de limite de fréquence).

Les messages in-app et les cartes de contenu ne sont pas comptabilisés dans le plafond de campagnes ou de composant de Canvas de n’importe quel type que ce soit.

{% alert important %}
La limite de fréquence globale est planifiée en fonction du fuseau horaire de l’utilisateur et est calculée par jours calendaires et non pas par périodes de 24 heures. Par exemple, si vous configurez une règle de limite de fréquence pour qu’elle n’envoie pas plus d’une campagne par jour, un utilisateur peut recevoir un message à 23 h dans son fuseau horaire local et être éligible à recevoir un autre message une heure plus tard.
{% endalert %}

#### Exemples

{% tabs %}
{% tab Example 1 %}

Supposons que vous définissiez une règle de limite de fréquence qui demande à ce que votre utilisateur reçoive au maximum trois campagnes de notification push ou composants de Canvas par semaine depuis toutes les campagnes ou composant de Canvas.

Si votre utilisateur est censé recevoir trois notifications push, deux messages in-app et une carte de contenu cette semaine, il recevra tous ces messages.

{% endtab %}
{% tab Example 2 %}

L’exemple suivant utilise les règles de limite de fréquence suivantes :

**Lorsque le scénario suivant se présente :**

- Un utilisateur déclenche la même campagne, `Campaign ABC`, trois fois au cours d’une semaine.
- Cet utilisateur déclenche `Campaign ABC` une fois le lundi, une fois le mercredi et une fois le jeudi.

![]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Le comportement attendu est que :**

- Cet utilisateur recevra les envois de la campagne déclenchés le lundi et le mercredi.
- Cet utilisateur ne recevra pas la troisième campagne envoyée jeudi parce que l’utilisateur a déjà reçu deux campagnes de notification push cette semaine-là.

{% endtab %}
{% endtabs %}

### Limite de fréquence par tag

Les [règles de limite de fréquence](#delivery-rules) peuvent être appliquées aux groupes d’apps en utilisant des tags spécifiques que vous avez appliqués à vos campagnes et à vos Canvas, ce qui vous permet en fait de baser votre limite de fréquence sur des groupes nommés de manière personnalisée.

Avec une limite de fréquence par tag, les règles peuvent être définies sur les tags principaux et imbriqués, pour que Braze prenne en compte tous les tags. Par exemple, si vous avez choisi d’utiliser le tag A principal pour la limite de fréquence, nous inclurons également des informations dans toutes les tags imbriqués (par exemple, les tags B et C) lors de la détermination de la limite.

Vous pouvez également combiner une limite de fréquence régulière avec une limite de fréquence par tags. Prenez en compte les règles suivantes :

1. Pas plus de trois campagnes de notification push ou de composant de Canvas par semaine depuis toutes les campagnes et tous les composants de Canvas. <br>**ET**
2. Pas plus de deux campagnes de notification push ou composant de Canvas par semaine avec la balise `promotional`.

![][12]

Par conséquent, vos utilisateurs ne recevront pas plus de trois envois de campagnes par semaine depuis toutes les campagnes et étapes de Canvas et pas plus de deux campagnes de notification push ou de composant de Canvas avec la balise `promotional`.

{% alert important %}
Les Canvas reçoivent leur balise au niveau du Canvas et pas au niveau du composant. Chaque composant Canvas héritera donc des balises au niveau du Canvas.
{% endalert %}

#### Règles contradictoires

Lorsque les règles entrent en conflit, la règle de limite de fréquence la plus restrictive et applicable sera pratiquée pour vos utilisateurs. Par exemple, imaginons que vous ayez les règles suivantes :

1. Pas plus d’une campagne de notification push ou de composant Canvas par semaine depuis toutes les campagnes et tous les composants de Canvas. <br>**ET**
2. Pas plus de trois campagnes de notification push ou de composant Canvas par semaine avec la balise `promotional`.

![][11]

Dans cet exemple, votre utilisateur ne recevra pas plus d’une campagne de notification push ou de composants de Canvas avec la balise « promotionnel » pour une semaine donnée, car vous avez spécifié que les utilisateurs ne doivent pas recevoir plus d’une campagne de notification push ou de composant de Canvas depuis toutes les campagnes et composants de Canvas. En d’autres termes, la règle de fréquence applicable la plus restrictive est la règle qui sera appliquée à un utilisateur donné.

#### Nombre de tags

La limite de fréquence par règles de tag est calculée au moment où un message est envoyé. Cela signifie que la limite de fréquence par tag compte uniquement des tags qui sont actuellement sur les campagnes ou les Canvas qu’un utilisateur a reçu par le passé. Il ne compte pas les tags qui étaient sur les campagnes ou les Canvas pendant qu’ils étaient envoyés mais qui ont depuis été supprimés. Elle comptera si un tag est ajouté ultérieurement à un message que l’utilisateur a reçu par le passé, mais avant que le dernier message avec le tag soit envoyé.

##### Exemple

Imaginez les campagnes et la limite de fréquence par règle de tag suivantes :

**Campagnes**:

- La **Campagne A** est une campagne de notification push avec le tag `promotional`. Elle doit être envoyée à 9 h le lundi.
- La **Campagne B** est une campagne de notification push avec le tag `promotional`. Elle doit être envoyée à 9 h le mercredi.

**Limite de fréquence par règle de tag :**

- Votre utilisateur ne doit pas recevoir plus d’une campagne de notification push par semaine avec le tag `promotional`.<br><br>

| Action | Résultat |
|---|---|
| Le tag `promotional` est enlevé de la **Campagne A** après que votre utilisateur a reçu le message, mais avant que la **Campagne B soit envoyée.** | Votre utilisateur recevra la **Campagne B**.|
| Le tag `promotional` est supprimé par erreur de la **Campagne A** après que votre utilisateur a reçu le message. <br> Le tag est ajouté à nouveau à la **Campagne A** mardi, avant que la **Campagne B** soit envoyée. | Votre utilisateur ne recevra pas la **Campagne B**. |
{: .reset-td-br-1 .reset-td-br-2}

#### Envoi à grande échelle {#sending-at-large-scales}

Laimite de fréquence par les règles de tag peut ne pas être appliqué correctement à de grandes échelles, comme 100 messages par canal provenant de campagnes ou de composants Canvas.

Par exemple, si votre limite de fréquence par règle de tag est :

> Pas plus de deux campagnes d’e-mail ou de composants Canvas avec la balise `Promotional` pour un utilisateur chaque semaine.

Et que vous envoyez à l’utilisateur plus de 100 e-mails de campagnes et de Canvas Step avec une limite de fréquence activée pour une semaine, plus de deux e-mails peuvent être envoyés à l’utilisateur.

Étant donné que 100 messages par canal constituent plus de messages que ce que la plupart des marques envoient à leurs utilisateurs, il est peu probable que vous soyez affecté par cette limitation. Pour l’éviter, vous pouvez définir un plafond pour le nombre maximum d’e-mails que vous souhaitez que vos utilisateurs reçoivent au cours d’une semaine.

Par exemple, vous pouvez configurer la règle suivante :

> Pas plus de trois campagnes d’e-mail ou de composant Canvas par semaine depuis toutes les campagnes et composants Canvas.

Cette règle garantira qu’aucun utilisateur ne reçoit plus de 100 e-mails par semaine, car, au maximum, les utilisateurs recevront trois e-mails par semaine depuis les campagnes ou les composants Canvas avec une limite de fréquence activée.

[11]: {% image_buster /assets/img/global_rules.png %} "global rules"
[12]: {% image_buster /assets/img/tag_rule_fnfn.png %} "rules"
[13]: {% image_buster /assets/img/standard_rules_fnfn.png %} "rules standard"
[1]: {% image_buster /assets/img_archive/rate_limit_daily.png %}
[2]: {% image_buster /assets/img_archive/total_limit.png %}
[3]: {% image_buster /assets/img_archive/per_minute_rate_limit.png %}
[14]: {% image_buster /assets/img_archive/rate_limiting_overview_2.png %}
[15]: {{site.baseurl}}/developer_guide/rest_api/messaging/#messaging
[16]: {{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns
[18]: {% image_buster /assets/img_archive/frequencycappingupdate.png %}
[19]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries/
