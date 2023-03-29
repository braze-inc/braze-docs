---
nav_title: AppsFlyer Audiences
article_title: AppsFlyer Audiences
alias: /partners/appsflyer_audiences/
description: "Cet article de référence présente le partenariat entre Braze et AppsFlyer Audiences, une fonctionnalité de la plateforme AppsFlyer qui vous permet de créer et de connecter efficacement des segments de public aux réseaux partenaires."
page_type: partner
search_tag: Partenaire

---

# AppsFlyer Audiences

> [AppsFlyer][1] est une plateforme d’analytiques et d’attribution de marketing mobile qui vous aide à analyser et à optimiser vos applications grâce à des analytiques marketing, à [l’attribution mobile][3] et à la création de liens profonds. [AppsFlyer Audiences][2] vous permet de créer et de connecter des segments de public à vos réseaux partenaires.

L’intégration de Braze et AppsFlyer vous permet de stimuler l’engagement des utilisateurs et d’augmenter l’efficacité de vos programmes de remarketing en tirant parti de la puissance des segments d’utilisateurs incorporés dans AppsFlyer Audiences. Transmettez vos audiences AppsFlyer (cohortes) directement à Braze pour créer de puissantes campagnes d’engagement client ciblant uniquement les bons utilisateurs au bon moment. 

## Conditions préalables

| Condition | Description |
|---|---|
| Compte AppsFlyer | Un compte AppsFlyer est requis pour profiter de ce partenariat. |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. Selon votre plateforme, les extraits de code peuvent être requis dans votre application. Vous trouverez des détails sur ces exigences à l’étape 1 du processus d’intégration. |
| SDK AppsFlyer | En plus du SDK Braze requis, vous devez installer le [SDK AppsFlyer](https://support.appsflyer.com/hc/en-us/categories/201114756-SDK-integration-). |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration de l’importation de données

### Étape 1 : Configurer le SDK AppsFlyer

Pour utiliser cette intégration, vous devez transmettre l’ID externe Braze de l’utilisateur à AppsFlyer en utilisant la fonction `setPartnerData()` du SDK AppsFlyer :

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
[[AppsFlyerLib shared]  setPartnerDataWithPartnerId:@"braze_int" partnerInfo:brazeInfo];
```

### Étape 2 : Obtenir la clé d’importation des données Braze

Dans Braze, accédez à **Technology Partners (Partenaires technologiques)** et sélectionnez **AppsFlyer**. Ici, vous trouverez l’endpoint REST pour générer votre clé d’importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d’importation des données et l’endpoint REST sont utilisés dans l’étape suivante lors de la configuration d’un postback dans le tableau de bord d’AppsFlyer.<br><br>![La zone « Data Import Using Cohort Import » (Importation de données avec l’importation de la cohorte) est disponible sur la page AppsFlyer Technology. Dans cette zone, vous trouverez la clé d’importation des données et l’endpoint REST.][5]{: style="max-width:90%;"}

### Étape 3 : Configurer une connexion Braze dans AppsFlyer Audiences

1. Dans [AppsFlyer Audiences][4], accédez à l’onglet **Connections (Connexions)** et cliquez sur **Add partner connection (Ajouter une connexion de partenaire)**.
2. Sélectionnez Braze en tant que partenaire et donnez un nom à la connexion.
3. Fournissez la clé d’importation des données et l’endpoint REST de Braze.
4. Enregistrez la connexion et vous serez prêt pour vous relier à toute audience nouvelle ou existante.

![La page de configuration de la connexion du partenaire de la plateforme AppsFlyer Audiences. La partie inférieure des images montre que la case d’ID externe Braze est cochée.][6]{: style="max-width:80%;"}

### Étape 4 : Utilisation des cohortes AppsFlyer Audiences dans Braze

Une fois que l’audience AppsFlyer a été téléchargée sur Braze, vous pouvez l’utiliser comme filtre lors de la définition des segments dans Braze en sélectionnant le filtre **AppsFlyer Cohorts (Cohortes AppsFlyer)**.

![Filtre des attributs utilisateur « AppsFlyer Cohorts » (Cohortes AppsFlyer) sélectionné.][7]

[1]: https://www.appsflyer.com/
[2]: https://www.appsflyer.com/product/audiences/
[3]: {{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/
[4]: https://support.appsflyer.com/hc/en-us/articles/115002689186-Audiences-guide#managing-connections
[5]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_data_import_key.png %}
[6]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_braze_connection.png %}
[7]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_cohorts_as_filter.png %}