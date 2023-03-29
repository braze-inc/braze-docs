---
hidden: true
nav_title: Guide de mise à jour iOS 14
article_title: Guide de mise à jour SDK iOS 14
page_order: 7
platform: iOS
description: "Cet article de référence couvre la mise à jour du SDK iOS 14, mettant en évidence les changements tels que les clôtures géographiques, le ciblage géographique, l’IDFA, etc."

---

# Guide de mise à jour SDK iOS 14

Ce guide décrit les modifications liées à Braze introduites dans iOS 14 et les étapes de mise à niveau requises pour votre intégration SDK Braze pour iOS.

Pour obtenir une liste complète des nouvelles mises à jour iOS 14, voir [Page iOS 14](https://www.apple.com/ios/ios-14/) d’Apple.

{% alert tip %}
À partir d’iOS 14.5, la collecte **IDFA** et le [partage de certaines données](https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track) nécessiteront l’invite d’autorisation de la nouvelle infrastructure [AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency) ([En savoir plus](#idfa)).
{% endalert %}

#### Résumé des changements majeurs de l’iOS 14

- Les applications ciblant iOS 14 / Xcode 12 doivent utiliser notre [version officielle iOS 14][1].
- Les geofences [ne sont plus prises en charge par iOS][4] pour les utilisateurs qui choisissent la nouvelle autorisation de _localisation approximative_.
- L’utilisation des fonctions de ciblage « Dernière position connue » nécessite une mise à niveau vers SDK Braze pour iOS v3.26.1+ pour la compatibilité avec l’autorisation de _localisation approximative_. Notez que si vous utilisez XCode 12, vous devrez passer au moins à la mise à jour v3.27.0.
- À partir d’iOS 14.5, la collecte IDFA et le [partage de certaines données][5] nécessiteront l’invite d’autorisation de la nouvelle infrastructure [AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency).
- Si vous utilisez le champ « Ad Tracking Enabled (Suivi des campagnes publicitaires activé) » pour le ciblage ou l’analyse de campagne, vous devrez passer à Xcode 12 et utiliser la nouvelle infrastructure AppTrackingTransparency pour signaler le statut d’abonnement des utilisateurs finaux.

## Résumé de la mise à jour

<style>
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2) {
    min-width:230px;
}
table td {
    word-break: break-word;
}
</style>

|Si votre application utilise :|Recommandation de la mise à jour|Description|
|------|--------|---|
|Xcode 12|**Mise à jour vers iOS SDK v3.27 ou version ultérieure**|Les clients utilisant Xcode 12 doivent utiliser la version v3.27.0+ pour la compatibilité. Si vous rencontrez des problèmes ou si vous avez des questions concernant notre compatibilité avec iOS 14, ouvrez un nouveau [Problème Github][2]..|
|Emplacement le plus récent| **Mise à jour vers iOS SDK v3.26.1 ou version ultérieure**|Si vous utilisez la fonction de ciblage la plus récente de l’emplacement et que vous utilisez toujours XCode 11, vous devez passer au minimum à la version iOS SDK v3.26.1 qui prend en charge la nouvelle fonction _Localisation approximative_. Les anciens SDK ne pourront pas collecter de manière fiable la localisation lorsqu’un utilisateur est mis à niveau vers iOS 14 _et_ choisit la localisation approximative.<br><br>Même si votre application n’est pas susceptible de cibler iOS 14, vos utilisateurs finaux peuvent mettre à niveau vers iOS 14 et commencer à utiliser l’option de précision de la localisation. Les applications qui ne sont pas mises à niveau vers iOS SDK v3.26.1+ ne pourront pas collecter de manière fiable les attributs de localisation lorsque les utilisateurs leur fournissent leur _localisation approximative_ sur les appareils iOS 14..|
|ID de suivi des annonces IDFA| **Il peut être nécessaire de mettre à niveau Xcode 12 et iOS SDK v3.27**|En 2021, Apple commencera à exiger une invite d’autorisation pour la collecte de l’IDFA. À ce moment, les applications doivent être mises à niveau vers Xcode 12 et utiliser la nouvelle infrastructure `AppTrackingTransparency` afin de continuer à recueillir l’IDFA. Si vous transmettez IDFA au SDK Braze, vous devez également mettre à niveau vers v3.27.0+ à ce moment-là.<br><br>Les applications qui n’utilisent pas les nouvelles API iOS 14 ne pourront pas collecter l’IDFA et collecteront plutôt un ID vierge (`00000000-0000-0000-0000-000000000000`) quand Apple commencera à faire appliquer ce changement en 2021. Pour savoir si cela s’applique ou non à votre application, consultez les [Détails IDFA](#idfa)..|


## Changements de comportement iOS 14

### Autorisation de localisation approximative

![Localisation précise]({% image_buster /assets/img/ios/ios14-approximate-location.png %}){: style="float:right;max-width:45%;margin-left:15px;"}

#### Aperçu

En demandant l’autorisation de localisation, les utilisateurs auront désormais le choix de fournir leur _localisation précise_(comportement précédent), ou la nouvelle _localisation approximative_. La localisation approximative renvoie un rayon plus large dans lequel l’utilisateur se trouve, au lieu de ses coordonnées exactes.

#### Geofences {#geofences}

Les geofences [ne sont plus prises en charge par iOS][4] pour les utilisateurs qui choisissent la nouvelle autorisation de _localisation approximative_. Bien qu’aucune mise à jour ne soit requise pour votre intégration SDK Braze, vous devrez peut-être ajuster votre [stratégie marketing basée sur la localisation](https://www.braze.com/blog/geofencing-geo-targeting-beaconing-when-to-use/) pour les campagnes qui reposent sur des geofences.

#### Ciblage de localisation {#location-tracking}

Pour continuer à collecter la _dernière localisation connue_ des utilisateurs lorsque l’autorisation _localisation approximative_ est accordée, votre application devra au moins passer à la mise à jour v3.26.1 du SDK Braze pour iOS. Gardez à l’esprit que la localisation sera moins précise et que, d’après nos tests, elle est supérieure à 12 000 mètres (+ de 7 miles). Lorsque vous utilisez les options de ciblage de la _dernière localisation connue_ dans le tableau de bord de Braze, assurez-vous d’augmenter le rayon de la localisation pour tenir compte de nouvelles _localisations approximatives_ (nous recommandons d’utiliser au moins 1,6 km de rayon).

Les applications qui ne mettent pas à niveau le SDK Braze pour iOS à la version v3.26.1 ou supérieure ne pourront plus utiliser le suivi de la localisation lorsque l’autorisation de _localisation approximative_ est accordée sur les appareils iOS 14.

Les utilisateurs qui ont déjà accordé un accès à leur localisation continueront à fournir leur _localisation précise_ après la mise à niveau.

Notez que si vous utilisez XCode 12, vous devrez passer au moins à la mise à jour v3.27.0.

Pour plus d’informations sur la localisation approximative, voir la vidéo WWDC [Nouveautés concernant la localisation](https://developer.apple.com/videos/play/wwdc2020/10660/) d’Apple.

### Transparence du suivi des applications et IDFA {#idfa}

#### Aperçu

L’IDFA (Identifiant pour les annonceurs) est un identifiant fourni par Apple pour une utilisation avec des partenaires publicitaires et d’attribution pour le suivi inter-appareil et est lié à l’ID Apple d’une personne.

À partir d’iOS 14.5, une nouvelle invite d’autorisation (lancée par la nouvelle infrastructure `AppTrackingTransparency`) doit être affichée pour recueillir le consentement explicite de l’utilisateur pour l’IDFA. Cette invite d’autorisation pour « vous suivre via les applications et les sites Web appartenant à d’autres sociétés » devra être demandée de la même manière que lorsque vous invitez les utilisateurs à partager leur localisation.

Si un utilisateur n’accepte pas l’invite, ou si vous ne procédez pas à la mise à niveau vers l’infrastructure `AppTrackingTransparency` de Xcode 12, alors une valeur IDFA vide (`00000000-0000-0000-0000-000000000000`) sera renvoyée, et votre application ne sera pas autorisée à inviter à nouveau l’utilisateur.

{% alert important %}
Ces mises à jour IDFA prendront effet lorsque les utilisateurs finaux mettent leur appareil à niveau vers iOS 14.5. Assurez-vous que votre application utilise le nouveau `AppTransparencyFramework` avec Xcode 12 si vous prévoyez de recueillir l’IDFA.
{% endalert %}

#### Modifications apportées au recueil de l’
![IDFA]({% image_buster /assets/img/ios/ios14-idfa.png %}) Braze{: style="float:right;max-width:25%;margin-left:15px;border:0"}

1. Braze continuera à autoriser les applications à fournir une valeur IDFA d’utilisateur _au_ SDK Braze.

2. La macro de compilation `ABK_ENABLE_IDFA_COLLECTION`, qui devrait compiler en fonction du recueil automatique facultatif de l’IDFA, ne fonctionnera plus dans iOS 14 et a été supprimée dans la section 3.27.0. 

3. Si vous utilisez le champ « Ad Tracking Enabled (Suivi des campagnes publicitaires activé) » pour le ciblage ou l’analyse de campagne, vous devrez passer à Xcode 12 et utiliser la nouvelle infrastructure AppTrackingTransparency pour signaler le statut d’abonnement des utilisateurs finaux. La raison de cette modification est que dans iOS 14, l’ancien champ [`advertisingTrackingEnabled`](https://developer.apple.com/documentation/adsupport/asidentifiermanager/1614148-advertisingtrackingenabled) n’est toujours pas renvoyé.

4. Si votre application a utilisé l’IDFA ou l’IDFV comme ID externe Braze, nous vous recommandons fortement de faire migrer ces identifiants en faveur d’un UUID. Pour plus d’informations sur la migration des ID externes, consultez notre nouveau [endpoint d’API de migration de l’ID externe]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/).

En savoir plus sur Apple à propos de leurs [Mises à jour de confidentialité](https://developer.apple.com/app-store/user-privacy-and-data-use/) et de la nouvelle [Infrastructure de transparence de suivi des applications](https://developer.apple.com/documentation/apptrackingtransparency).

### Autorisation Push {#push-provisional-auth}

{% alert important %}
Aucune modification de l’autorisation Push provisoire n’est incluse dans iOS 14. Dans une version bêta antérieure d’iOS 14, Apple a introduit une modification qui a depuis été rétablie au comportement antérieur.
{% endalert %}


## Nouvelles fonctionnalités iOS 14

### Présentation de la confidentialité et de la collecte de données de l’application {#app-privacy}

Depuis le 8 décembre 2020, toutes les soumissions à l’App Store nécessitent des étapes supplémentaires pour respecter les [nouvelles normes de confidentialité d’Apple](https://developer.apple.com/app-store/app-privacy-details/).

#### Questionnaire sur le portail développeur d’Apple

Sur le _Portail Développeur d’Apple_ :
* Il vous sera demandé de remplir un questionnaire pour décrire comment votre application ou des partenaires tiers collectent des données.
  * Le questionnaire doit toujours être à jour avec votre version la plus récente dans l’App Store.
  * Le questionnaire peut être mis à jour même sans nouvelle soumission d’application.
* Vous devrez coller un lien vers l’URL de la politique de confidentialité de votre application.

Lorsque vous remplissez votre questionnaire, consultez votre équipe juridique et réfléchissez à la manière dont votre utilisation de Braze dans les domaines suivants peut affecter vos exigences de divulgation.

#### 
**Identifiants** de collecte de données par défaut de Braze - Un identifiant d’appareil anonyme est toujours recueilli par le SDK Braze. Ce paramètre est actuellement défini sur l’IDFV (identifiant du fournisseur).

**Données d’utilisation** - Cela peut inclure les données de session de Braze, ainsi que toute collection d’événements ou d’attributs que vous utilisez pour mesurer l’interaction du produit.

#### Collecte de données facultatives
Données que vous pouvez éventuellement collecter via votre utilisation de Braze :

**Localisation** - La localisation approximative et la localisation précise peuvent facultativement être collectées par le SDK Braze. Ces fonctionnalités sont désactivées par défaut.

**Coordonnées de contact** - Cela peut inclure des événements et des attributs liés à l’identité de l’utilisateur.

**Achats** - Cela peut inclure des événements et des achats enregistrés au nom de l’utilisateur.

{% alert important %}
Notez qu’il ne s’agit pas d’une liste exhaustive. Si vous collectez manuellement d’autres informations sur vos utilisateurs dans Braze qui s’appliquent à d’autres catégories du questionnaire sur la confidentialité de l’application, vous devrez également les divulguer.
{% endalert %}

Pour en savoir plus sur cette fonctionnalité, consultez la rubrique [Confidentialité et utilisation des données d’Apple](https://developer.apple.com/app-store/user-privacy-and-data-use/).

[1]: https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.27.0
[2]: https://github.com/Appboy/appboy-ios-sdk/issues
[4]: https://developer.apple.com/documentation/corelocation/cllocationmanager/3600215-accuracyauthorization
[5]: https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track
