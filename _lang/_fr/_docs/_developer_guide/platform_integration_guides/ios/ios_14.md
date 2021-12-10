---
nav_title: Guide de mise à jour iOS 14
article_title: Guide de mise à jour du SDK iOS 14
page_order: 7
platform: iOS
description: "Cet article de référence couvre la mise à jour du SDK iOS 14, mettant en évidence les changements tels que les géofences, le ciblage de localisation, l'IDFA, et plus encore."
hidden: vrai
---

# Guide de mise à jour du SDK iOS 14

Ce guide décrit les modifications apportées au Brésil dans iOS 14 et les étapes nécessaires à la mise à jour de votre intégration dans Braze iOS SDK.

Pour une liste complète des nouvelles mises à jour pour iOS 14, consultez la [page iOS 14 d'Apple](https://www.apple.com/ios/ios-14/).

{% alert tip %}
Depuis iOS 14. , la collection **IDFA** et [certains partages de données](https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track) nécessiteront la nouvelle invite d'autorisation [AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency) Framework ([En savoir plus](#idfa)).
{% endalert %}

#### Résumé des modifications d'iOS 14 cassant

- Les applications ciblant iOS 14 / Xcode 12 doivent utiliser notre [version officielle d'iOS 14][1].
- Les Geofences ne sont plus [pris en charge par iOS][4] pour les utilisateurs qui choisissent la nouvelle permission  _l'emplacement approximatif_.
- L'utilisation des fonctionnalités de ciblage « Dernier emplacement connu » nécessitera une mise à niveau vers Braze iOS SDK v3.26.1+ pour la compatibilité avec la permission _d'emplacement approximatif_. Notez que si vous utilisez XCode 12, vous devrez mettre à jour vers au moins la version 3.27.0.
- Depuis iOS 14.5, la collecte IDFA et [le partage de données][5] nécessitent la nouvelle invite d'autorisation [AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency) Framework.
- Si vous utilisez le champ "Suivi des publicités activé" pour cibler ou analyser des campagnes, vous devrez passer à Xcode 12 et utiliser le nouveau framework AppTrackingTransparency pour signaler le statut opt-in des utilisateurs.

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

| Si votre application utilise : | Recommandation de mise à jour                                            | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------ | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Xcode 12                       | **Mise à niveau vers iOS SDK v3.27 ou supérieur**                        | Les clients utilisant Xcode 12 doivent utiliser v3.27.0+ pour être compatibles. Si vous rencontrez des problèmes ou des questions liés à notre compatibilité iOS 14, veuillez ouvrir un nouveau [Github Issue][2].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Lieu le plus récent            | **Mise à niveau vers iOS SDK v3.26.1 ou supérieur**                      | Si vous utilisez la fonction de ciblage de localisation la plus récente et que vous utilisez toujours XCode 11, vous devriez mettre à niveau vers au moins iOS SDK v3. 6.1 qui prend en charge la nouvelle fonctionnalité  _Emplacement approximatif_. Les anciens SDK ne seront pas en mesure de collecter de façon fiable l'emplacement lorsqu'un utilisateur passe à iOS 14 _et_ choisit la localisation approximative.<br><br>Même si votre application peut ne pas cibler iOS 14, vos utilisateurs finaux peuvent mettre à niveau vers iOS 14 et commencer à utiliser la nouvelle option de précision de localisation. Applications qui ne se mettent pas à jour vers iOS SDK v3.26. + ne sera pas en mesure de collecter de manière fiable les attributs de localisation lorsque les utilisateurs fournissent leur _position approximative_  sur les appareils iOS 14. |
| ID de suivi des annonces IDFA  | **La mise à niveau vers Xcode 12 et iOS SDK v3.27 peut être nécessaire** | Quelque temps en 2021, Apple va commencer à demander une invite d'autorisation pour la collecte de l'IDFA. À cette époque, les applications doivent se mettre à niveau vers Xcode 12 et utiliser le nouveau framework `AppTrackingTransparency` afin de continuer à collecter l'IDFA. Si vous passez IDFA au Braze SDK, vous devez également passer à la version 3.27.0+ à ce moment-là.<br><br>Les applications qui n'utilisent pas les nouvelles API iOS 14 ne pourront pas collecter l'IDFA, et ramassera à la place un ID vide (`00000000-0000-0000-000000000000`) une fois que Apple commencera à imposer ce changement en 2021. Pour plus d'informations sur si cela s'applique ou non à votre application, [lisez les détails ci-dessous](#idfa).                                                                                                                     |


## Changements de comportement iOS 14

### Autorisation de localisation approximative

![Emplacement précis]({% image_buster /assets/img/ios/ios14-approximate-location.png %}){: style="float:right;max-width:45%;margin-left:15px;"}

#### Aperçu

Lors de la demande d'autorisation de localisation, les utilisateurs auront maintenant le choix de fournir leur _localisation précise_ (comportement précédent), ou le nouvel _emplacement approximatif_. L'emplacement approximatif retournera un rayon plus grand dans lequel l'utilisateur est situé, au lieu de ses coordonnées exactes.

#### Géorepérages {#geofences}

Les Geofences ne sont plus [pris en charge par iOS][4] pour les utilisateurs qui choisissent la nouvelle permission  _l'emplacement approximatif_. Bien qu'aucune mise à jour ne soit nécessaire pour votre intégration Braze SDK, vous pourriez avoir besoin d'ajuster votre [stratégie de marketing basée sur la localisation](https://www.braze.com/blog/geofencing-geo-targeting-beaconing-when-to-use/) pour les campagnes qui dépendent des géofences.

#### Ciblage de l'emplacement {#location-tracking}

Pour continuer à collecter le _dernier emplacement connu des utilisateurs_ lorsque _l'emplacement approximatif_ est accordé, votre application devra passer à au moins v3. 6.1 du Braze iOS SDK. Gardez à l'esprit que la localisation sera moins précise et que d'après nos tests, nous avons parcouru plus de 12 000 mètres (plus de 7 milles). Lors de l'utilisation des options de ciblage _la dernière position connue_ dans le tableau de bord de Braze, Assurez-vous d'augmenter le rayon de l'emplacement pour tenir compte des nouveaux _emplacements approximatifs_ (nous recommandons au moins un kilomètre/1. rayon de kilomètres).

Applications qui ne mettent pas à jour Braze iOS SDK au moins v3.26. ne sera plus en mesure d'utiliser le suivi de localisation lorsque _la localisation approximative_ est accordée sur les appareils iOS 14.

Les utilisateurs qui ont déjà accordé un accès à la localisation continueront à fournir _un emplacement précis_ après la mise à niveau.

Notez que si vous utilisez XCode 12, vous devrez mettre à jour vers au moins la version 3.27.0.

Pour plus d'informations sur la localisation approximative, voir la vidéo d'Apple [Quoi de neuf dans l'emplacement](https://developer.apple.com/videos/play/wwdc2020/10660/) WWDC.

### Transparence de l'IDFA et du suivi des applications {#idfa}

#### Aperçu

IDFA (Identifier for Advertisers) est un identificateur fourni par Apple pour être utilisé avec des partenaires de publicité et d'attribution pour le suivi inter-appareil et est lié à l'identifiant Apple d'un individu.

Commence dans iOS 14. , une nouvelle invite de permission (lancée par le nouveau framework `AppTrackingTransparency` ) doit être montrée pour recueillir le consentement explicite de l'utilisateur pour IDFA. Cette demande d'autorisation de "suivre vos applications et sites Web appartenant à d'autres entreprises" sera demandée de la même manière que la façon dont vous inviteriez les utilisateurs à demander leur emplacement.

Si un utilisateur n'accepte pas l'invite de commande, ou si vous ne mettez pas à niveau vers le framework `AppTrackingTransparency` de Xcode 12 alors une valeur IDFA vide (`00000000-0000-0000-0000-000000000000`) sera retournée, et votre application ne sera pas autorisée à redemander à l'utilisateur.

{% alert important %}
Ces mises à jour IDFA prendront effet une fois que les utilisateurs finaux mettront leur appareil à niveau vers iOS 14.5. Veuillez vous assurer que votre application utilise le nouveau `AppTransparencyFramework` avec Xcode 12 si vous prévoyez de collecter l'IDFA.
{% endalert %}

#### Changements dans la collection Braze IDFA
![IDFA]({% image_buster /assets/img/ios/ios14-idfa.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

1. Braze continuera à autoriser les applications à fournir la valeur IDFA d'un utilisateur _à_ le Braze SDK.

2. `La compilation ABK_ENABLE_IDFA_COLLECTION` macro , qui compilerait conditionnellement dans la collection automatique optionnelle IDFA, ne fonctionnera plus dans iOS 14 et a été supprimé en 3. 7.0.

3. Si vous utilisez le champ "Suivi des publicités activé" pour cibler ou analyser des campagnes, vous devrez passer à Xcode 12 et utiliser le nouveau framework AppTrackingTransparency pour signaler le statut opt-in des utilisateurs. La raison de ce changement est que dans iOS 14, l'ancien champ [`advertisingTrackingActivé`](https://developer.apple.com/documentation/adsupport/asidentifiermanager/1614148-advertisingtrackingenabled) retournera toujours Non.

4. Si votre application a utilisé IDFA ou IDFV comme votre ID externe Braze, Nous vous recommandons fortement de vous éloigner de ces identifiants en faveur d'un UUID. Pour plus d'informations sur la migration des identifiants externes, voir notre nouveau [point de terminaison de l'API de migration d'ID externe]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/).

Apprenez-en plus sur Apple à propos de leurs [mises à jour de confidentialité](https://developer.apple.com/app-store/user-privacy-and-data-use/) et du nouveau [framework de transparence de suivi des applications](https://developer.apple.com/documentation/apptrackingtransparency).

### Autorisation push {#push-provisional-auth}

{% alert important %}
Aucune modification de l'autorisation provisoire de push n'est incluse dans iOS 14. Dans une version bêta antérieure d'iOS 14, Apple a introduit un changement qui a depuis été rétabli au comportement antérieur.
{% endalert %}


## Nouvelles fonctionnalités iOS 14

### Aperçu de la confidentialité des applications et de la collecte des données {#app-privacy}

Depuis le 8 décembre 2020, toutes les soumissions sur l'App Store nécessitent des étapes supplémentaires pour adhérer aux [nouvelles normes de confidentialité de l'application](https://developer.apple.com/app-store/app-privacy-details/) d'Apple.

#### Questionnaire de portail développeur Apple

Sur le _portail développeur Apple_:
* Il vous sera demandé de remplir un questionnaire pour décrire comment votre application ou vos partenaires tiers recueillent des données.
  * Le questionnaire devrait toujours être à jour avec votre version la plus récente dans l'App Store.
  * Le questionnaire peut être mis à jour même sans une nouvelle soumission d'application.
* Vous devrez coller un lien vers l'URL de la politique de confidentialité de votre application.

Lorsque vous remplissez votre questionnaire, veuillez consulter votre équipe juridique, et examinez comment votre utilisation de Braze pour les champs suivants peut affecter vos exigences de divulgation.

#### Collecte de données par défaut de Braze
**Identifiants** - Un identifiant de périphérique anonyme est toujours collecté par le SDK de Braze. Ceci est actuellement réglé sur le périphérique IDFV (identifiant pour le vendeur).

**Données d'utilisation** - Cela peut inclure les données de session de Brase, ainsi que tout événement ou collection d'attributs que vous utilisez pour mesurer l'interaction de produit.

#### Collecte de données optionnelle
Les données que vous pouvez éventuellement collecter grâce à votre utilisation de Braze :

**Emplacement** - La localisation approximative et la localisation précise peuvent éventuellement être collectées par le SDK de Braze. Ces fonctionnalités sont désactivées par défaut.

**Informations de contact** - Cela peut inclure des événements et des attributs liés à l'identité de l'utilisateur.

**Achats** - Cela peut inclure des événements et des achats enregistrés au nom de l'utilisateur.

{% alert important %}
Notez qu'il ne s'agit pas d'une liste exhaustive. Si vous collectez manuellement d'autres informations sur vos utilisateurs dans Braze qui s'appliquent à d'autres catégories dans le Questionnaire sur la confidentialité de l'appli, vous devrez les divulguer également.
{% endalert %}

Pour en savoir plus sur cette fonctionnalité, consultez la section [Confidentialité et Utilisation des données d'Apple](https://developer.apple.com/app-store/user-privacy-and-data-use/).

[1]: https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.27.0
[2]: https://github.com/Appboy/appboy-ios-sdk/issues
[4]: https://developer.apple.com/documentation/corelocation/cllocationmanager/3600215-accuracyauthorization
[5]: https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track
