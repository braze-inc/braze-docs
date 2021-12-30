---
nav_title: Audiences AppsFlyer
article_title: Audiences AppsFlyer
alias: /fr/partners/appsflyer_audiences/
description: "Cette page décrit le partenariat entre Braze et AppsFlyer Audiences, une fonctionnalité de la plateforme AppsFlyer qui vous permet de construire et de connecter efficacement les segments d'audience aux réseaux partenaires."
page_type: partenaire
search_tag: Partenaire
---

# Audiences AppsFlyer

> [AppsFlyer][1] est une plateforme d'analyse et d'attribution marketing mobile qui vous aide à analyser et optimiser vos applications par le biais de l'analyse marketing. [attribution mobile][3], et lien profond. [AppsFlyer Audiences][2] vous permet de construire et de connecter des segments d'audience à vos réseaux partenaires.

L'intégration de Braze et AppsFlyer vous permet de stimuler l'engagement des utilisateurs et d'augmenter l'efficacité de vos programmes de remarketing en tirant parti de la puissance des segments d'utilisateurs intégrés dans AppsFlyer Audiences. Passez vos audiences AppsFlyer (cohortes) directement à Braze pour créer de puissantes campagnes d'engagement client ciblées sur les bons utilisateurs au bon moment.

## Pré-requis

| Exigences                  | Libellé                                                                                                                                                                                                                                        |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte AppsFlyer           | Un compte AppsFlyer est requis pour profiter de ce partenariat.                                                                                                                                                                                |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. Selon votre plate-forme, des extraits de code peuvent être requis dans votre application. Les détails sur ces exigences se trouvent à l'étape 1 du processus d'intégration. |
| SDK AppsFlyer              | En plus du Braze SDK requis, vous devez installer le [SDK AppsFlyer](https://support.appsflyer.com/hc/en-us/categories/201114756-SDK-integration-).                                                                                            |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration de l'importation de cohortes

### Étape 1 : Configurer le SDK de l'AppsFlyer

Pour utiliser cette intégration, vous devez passer l'ID externe Braze de l'utilisateur à AppsFlyer en utilisant la fonction `setPartnerData()` du SDK AppsFlyer :

#### Android
```java
Map<String, Object> brazeData = new HashMap<>();
partnerData.put("external_user_id", "some-braze-external-id-value");
AppsFlyerLib.getInstance().setPartnerData("braze_int", brazeData);
```

#### iOS
```objc
NSDictionary *brazeInfo = @{
     @"external_user_id":@"some-braze-external-id-value"
};
[[AppsFlyerLib shared] setPartnerDataWithPartnerId:@"braze_int" partnerInfo:brazeInfo];
```

### Étape 2 : Obtenir la clé d'importation de données Braze

Au Brésil, accédez aux **partenaires technologiques** et sélectionnez **AppsFlyer**. Ici, vous trouverez le point de terminaison REST et générez votre clé d'importation de données Braze. Une fois généré, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d'importation de données et le point de terminaison REST sont utilisés à l'étape suivante lors de la configuration d'un postback dans le tableau de bord de AppsFlyer.<br><br>!\[Image AppsFlyer\]\[5\]{: style="max-width:90%;"}

### Étape 3 : Configurer une connexion Braze dans les audiences AppsFlyer

1. Dans [AppsFlyer Audiences][4], allez dans l'onglet **Connexions** et cliquez sur **Ajouter une connexion partenaire**.
2. Sélectionnez Braze comme partenaire et donnez un nom à la connexion.
3. Fournissez la clé d'importation de données et le point de terminaison REST de Braze.
4. Enregistrez la connexion et il sera disponible pour créer un lien vers un public nouveau ou existant.

!\[Connexion partenaire\]\[6\]{: style="max-width:80%;"}

### Étape 4 : Utiliser des audiences AppsFlyer dans Braze

Une fois qu'une audience AppsFlyer a été téléchargée sur Braze, vous pouvez l'utiliser comme un filtre lors de la définition de segments dans Braze en sélectionnant le filtre __AppsFlyer Cohorts__.

!\[Filtre Cohort\]\[7\]
[5]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_data_import_key.png %} [6]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_braze_connection.png %} [7]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_cohorts_as_filter.png %}

[1]: https://www.appsflyer.com/
[2]: https://www.appsflyer.com/product/audiences/
[3]: https://www.braze.com/docs/partners/message_orchestration/attribution/appsflyer/appsflyer/
[4]: https://support.appsflyer.com/hc/en-us/articles/115002689186-Audiences-guide#managing-connections