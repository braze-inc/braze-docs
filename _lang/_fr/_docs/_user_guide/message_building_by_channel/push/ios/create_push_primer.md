---
nav_title: "Créer une Campagne Push Primer"
article_title: Créer une Campagne Push Primer
page_order: 5
page_type: tutoriel
description: "Cette présentation vous montrera comment faire en sorte que vos utilisateurs se qualifient et se préparent à recevoir vos messages push en envoyant un précurseur de poussage."
channel:
  - Pousser
tool:
  - Campagnes
---

<br>
{% alert important %}
Les campagnes Push Primer nécessitent la configuration de backend de vos développeurs. <br>Consultez les intégrations d'amorçage nécessaires [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_primer/).
{% endalert %}


# Créer une campagne de push primer

> Cet article vous guidera à travers la mise en place et l'envoi d'une campagne Push Primer aux nouveaux utilisateurs ou non autorisés. Les campagnes Push Primer encouragent vos utilisateurs à activer le push sur leur appareil pour votre application. Obtenir la permission des utilisateurs d'envoyer des messages directement à leurs appareils peut être complexe, mais nos guides peuvent vous aider !

!\[Push Primer Example\]\[push_primer5\]{: style="float:right;max-width:30%;margin-left:15px;"}

Les campagnes Push Primer sont utiles car elles traitent le problème de l'invite de notification redoutée iOS opt-in que les utilisateurs reçoivent à l'ouverture d'une nouvelle application iOS. Ces messages sont perturbateurs et peu informatifs, les utilisateurs ayant tendance à opter pour la suppression des notifications push. Cette invite n'est jamais affichée qu'une seule fois, et malheureusement, une fois que ces notifications sont désactivées, il y a très peu de choses que nous pouvons faire pour que les utilisateurs les réallument.

Pour y remédier, Braze propose des étapes sur la façon de mettre en place des campagnes Push Primer. Push Primers vous permet de suspendre la livraison de ce message perturbant initial ainsi que d'offrir une nouvelle délivrabilité, vous permettant de décider quand et comment vous voulez demander à vos utilisateurs un opt-in. Ces Primers Push devraient fournir aux utilisateurs des informations précieuses sur les raisons pour lesquelles les notifications pour votre application sont importantes.

Pour qu'un utilisateur puisse se qualifier pour recevoir vos messages push, il doit activer push au niveau de l'application _et_ au niveau de l'appareil. Veuillez noter que ces niveaux se traduisent différemment pour iOS et Android. Vous pouvez en apprendre plus sur eux ici :
- [Push Android activé]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#ios-android-details)
- [Push iOS activé]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#ios-android-details)

{% alert note %}
__Devrais-je utiliser Push Primers?__ Dépend de votre version iOS.<br><br>
- __iOS 12__: Avec l'offre de mise à jour iOS 12 [autorisation provisoire]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push-authentication--quiet-notifications), permettant à cette invite de push initiale d'être envoyée silencieusement à votre centre de notification, Certains trouvent peut-être que les Primères Push ne sont plus nécessaires, tandis que d'autres peuvent continuer à l'utiliser. Nous reconnaissons que toutes les applications iOS auront leurs développeurs incorporent une autorisation provisoire, donc les primers de poussée sont toujours une excellente approche pour ces applications. Nous vous recommandons de rencontrer votre gestionnaire de service clientèle pour discuter si l'intégration des primaires pousses est la bonne solution.
- __iOS 11 et plus tard__: parce que ces versions iOS ne permettent que Push, au premier plan, l'invite native iOS Push opt-in sera toujours envoyée, ce qui sacrifiera à son tour votre commerciabilité à ces utilisateurs. Nous vous suggérons fortement de mettre en place Push Primers pour ces versions.
{% endalert %}

## Étape 1 : Poussez les intégrations des primeurs

Nous tirons parti des messages dans l'application pour lancer des campagnes Push Primer. Contrairement à beaucoup de nos fonctionnalités hors de la boite qui sont prêtes à être utilisées, cet outil essentiel nécessite une configuration de backend de la part de vos développeurs. Nous avons inclus les extraits de code requis ici : [Intégrations Push Primer][integrations].

## Étape 2 : Sélectionnez votre canal de choix

À partir du volet **Campagnes** dans le tableau de bord, sélectionnez **Messagerie In-App** comme canal de messagerie dans **Créer Campagne**.

## Étape 3: Configurez les options de la campagne initiale

!\[Push Primer Message Type\]\[push_primer7\]

Une fois que vous avez une campagne de messagerie dans l'application vide sur laquelle travailler, vous devez nommer votre campagne, sélectionnez où vous voulez que votre Primer Push soit envoyé, sélectionnez le type de message et choisissez le type de mise en page. Pour votre type de message Push Primer de base, nous vous suggérons un message en plein écran ou un message modal. Notez que pour un message en plein écran dans l'application, une image est requise.

## Étape 4 : Personnaliser votre message

!\[Push Primer\]\[push_primer2\]{: style="max-width:75%"}

Une fois que vous avez choisi le type de message approprié dans l'application, vous pouvez personnaliser le contenu de votre message et ajouter des boutons.

Voici quelques ressources pour vous aider à démarrer :
- Braze prend en charge l'utilisation des icônes [Font Awesome v4.3.0](https://fontawesome.com/v4.7.0/cheatsheet/) pour les icônes de messages modaux dans l'application.

Rappelez-vous qu'un préfixe de push est censé prioriser l'utilisateur pour activer les notifications push. <br>Dans votre corps de message, nous suggérons __de mettre en évidence les raisons pour lesquelles vos utilisateurs devraient avoir activé les notifications push__.

Voici quelques exemples de Push Primer Messages:

!\[Push Primer Example 1\]\[push_primer3\]{: height="225px"} !\[Push Primer Example 2\]\[push_primer4\]{: height="225px"} !\[Push Primer Example 3\]\[push_primer5\]{: height="225px"}

Si vous souhaitez encore plus d'options de personnalisation, vous pouvez également définir le type de message en code personnalisé et fournir le HTML complet pour votre message dans l'application.

### Réglage du bouton

Pour ajouter des boutons à votre message dans l'application, vous trouverez une zone de texte du bouton 1 et le bouton 2 sous l'invite de saisie du corps du texte. Ici, vous pouvez choisir le texte qui s'affichera sur ces boutons. Nous recommandons "Activer les notifications" et "Pas maintenant" en tant que bouton de démarrage, mais il y a beaucoup de boutons différents que vous pouvez assigner.

!\[Push Primer\]\[push_primer6\]{: style="float:right;max-width:40%;margin-left:15px;"}

### Comportement du clic

Une fois que votre message "push" a été configuré, le comportement "clic" doit être assigné. Pour le bouton correspondant "Activer les notifications" que vous avez assigné, vous devez sélectionner **Lien Profond dans l'app**.

#### Liaison profonde

Parce que les campagnes Push Primer ne sont pas une fonctionnalité hors de la boîte, le lien de lien profond qui invite l'invite native de push doit être configuré par vos développeurs avant qu'il ne devienne disponible.

Vous trouverez de la documentation sur les intégrations d'amorçage et la personnalisation de liens profonds [ici][integrations].

## Étape 5 : Sélection du mode de livraison

Pour définir votre Push Primer à déclencher quand vous le souhaitez, vous devez définir __Effectuer un événement personnalisé__ comme action de déclenchement. Vos développeurs mettront en place un événement personnalisé que vous pourrez choisir de déclencher pour votre campagne Push Primer. Pour savoir comment votre entreprise fait référence à cet événement personnalisé, vérifiez avec vos développeurs. __Cet événement personnalisé compte comme un point de données vers votre attribution.__ Cet événement client vérifiera si un utilisateur a déjà été fourni une invite push native, et, si ce n'est pas le cas, cela déclenchera le message dans l'application.

## Étape 6 : cibler les utilisateurs

Généralement, pour les campagnes Push Primer, nous voulons que le poussoir déclenche un certain segment d'utilisateurs. Dans ces options d'utilisateurs ciblés, vous pouvez décider quel segment vous trouvez le plus approprié. Nous vous suggérons de prendre un peu de temps avec votre équipe de marketing pour choisir un segment convaincant. Par exemple, les utilisateurs qui ont terminé un deuxième achat, les utilisateurs qui viennent de faire un compte pour devenir membre, ou même les utilisateurs qui visitent votre application plus de deux fois par semaine. Cibler les utilisateurs de ces segments cruciaux augmente la probabilité que les utilisateurs optent et deviennent activés.

Si vous n'êtes pas sûr de la meilleure façon de segmenter, vous pouvez également sélectionner **Tous les utilisateurs**. Cette option enverra votre push primer à n'importe quel appareil iOS qui n'a pas encore choisi ou qui n'a pas encore choisi de push.

## Étape 7 : Conversions
Braze suggère des paramètres par défaut pour les conversions, mais vous pouvez configurer des événements de conversion autour des primers.
[push_primer2]: {% image_buster /assets/img/push_primer/push_primer_2.png %} [push_primer3]: {% image_buster /assets/img/push_primer/push_primer_3.png %} [push_primer4]: {% image_buster /assets/img/push_primer/push_primer_4. ng %} [push_primer5]: {% image_buster /assets/img/push_primer/push_primer_5.png %} [push_primer6]: {% image_buster /assets/img/push_primer/push_primer_6. pg %} [push_primer7]: {% image_buster /assets/img/push_primer/push_primer_7.png %}

[integrations]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_primer/

[integrations]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_primer/
