---
nav_title: Désactivation du suivi SDK iOS
article_title: Désactivation du suivi SDK pour iOS
platform: Swift
page_order: 8
description: "Cet article montre comment désactiver la collecte de données pour le SDK Swift."

---

# Désactivation du suivi du SDK iOS

> Afin de se conformer aux réglementations en matière de confidentialité des données, l'activité de suivi des données sur le SDK iOS peut être entièrement arrêtée en définissant la propriété [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) sur `false` dans votre instance Braze. 

Lorsque la propriété `enabled` est définie sur `false`, le SDK Braze ignore tous les appels à l'API publique. Le SDK annule également toutes les actions à la volée, telles que les requêtes réseau, le traitement des événements, etc. Pour reprendre la collecte de données, définissez [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) sur `true`.

Vous pouvez également utiliser la méthode [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) pour effacer complètement les données SDK stockées localement sur l'appareil d'un utilisateur. Si vous utilisez la version 5.7.0 ou antérieure du SDK Swift, ou si `useUUIDAsDeviceId` est défini sur `false`, vous devrez également faire une demande POST à [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) car votre identifiant pour les fournisseurs (IDFV) sera utilisé comme identifiant de leur appareil. Pour les versions de Braze Swift 7.0.0 et ultérieures, le SDK et la méthode `wipeData()` génèrent aléatoirement un UUID pour leur identifiant d’appareil à la place.
