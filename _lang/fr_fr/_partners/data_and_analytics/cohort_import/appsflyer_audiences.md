---
nav_title: "Audiences d'AppsFlyer"
article_title: "Audiences d'AppsFlyer"
alias: /partners/appsflyer_audiences/
description: "Cet article de référence décrit le partenariat entre Braze et AppsFlyer Audiences, une fonctionnalité de la plateforme AppsFlyer qui vous permet de créer et de connecter efficacement des segments d'audience à des réseaux partenaires."
page_type: partner
search_tag: Partner

---

# Audiences d'AppsFlyer

> [Cet article explique comment importer des cohortes d'utilisateurs d'AppsFlyer vers Braze à l'aide de l'intégration AppsFlyer Audiences.](https://www.appsflyer.com/product/audiences/) Pour plus d'informations sur l'intégration d'AppsFlyer et de ses autres fonctionnalités, telles que l'attribution mobile, consultez l'article principal d'[AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/).

## Conditions préalables

| Condition | Description |
|---|---|
| Compte AppsFlyer | Un compte AppsFlyer est nécessaire pour bénéficier de ce partenariat. |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. En fonction de votre plateforme, des extraits de code peuvent être requis dans votre application. Vous trouverez des informations détaillées sur ces exigences à l'étape 1 du processus d'intégration. |
| SDK AppsFlyer | Outre le SDK Braze requis, vous devez installer le [SDK AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/207032126-SDK-integration-overview). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration de l'importation de données

### Étape 1 : Configuration du SDK AppsFlyer

Pour utiliser cette intégration, vous devez transmettre l'ID externe Braze de l'utilisateur à AppsFlyer à l'aide de la fonction `setPartnerData()` du SDK AppsFlyer :

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

### Étape 2 : Obtenez la clé d'importation des données Braze

Dans Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **AppsFlyer**. 

Ici, vous trouverez l’endpoint REST et générerez votre clé d'importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d'importation des données et l’endpoint REST sont utilisés à l'étape suivante lors de la configuration d'un postback dans le tableau de bord d'AppsFlyer.<br><br>![La case « Importation de données à l'aide de l'importation de cohortes » sur la page technologique d'AppsFlyer. Dans cette boîte, la clé d'importation des données et l'endpoint REST sont affichés.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_data_import_key.png %}){: style="max-width:90%;"}

### Étape 3 : Configurer une connexion Braze dans AppsFlyer Audiences

1. Dans [AppsFlyer Audiences](https://support.appsflyer.com/hc/en-us/articles/115002689186-Audiences-guide#managing-connections), accédez à l'**onglet Connexions** et cliquez sur Ajouter une **connexion partenaire**.
2. Sélectionnez Braze comme partenaire et donnez un nom à la connexion.
3. Fournissez la clé d'importation des données et l’endpoint Braze REST.
4. Enregistrez la connexion et elle sera disponible pour créer un lien vers n'importe quelle audience nouvelle ou existante.

![La page de configuration de la connexion des partenaires de la plateforme d'audiences AppsFlyer. La partie inférieure des images montre que la case Braze external ID est cochée.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_braze_connection.png %}){: style="max-width:80%;"}

### Étape 4 : Utilisation des cohortes AppsFlyer Audiences à Braze

**Une fois qu'une audience AppsFlyer a été téléchargée sur Braze, vous pouvez l'utiliser comme filtre lors de la définition de segments dans Braze en sélectionnant le filtre AppsFlyer Cohorts.**

![Filtre d'attributs d'utilisateur "AppsFlyer Cohortes" sélectionné.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_cohorts_as_filter.png %})

{% alert important %}
Seuls les utilisateurs qui existent déjà dans Braze pourront être ajoutés ou supprimés d'une cohorte. L'importation d'une cohorte ne créera pas de nouveaux utilisateurs dans Braze.
{% endalert %}

## Correspondance entre les utilisateurs

Les utilisateurs identifiés peuvent être associés à leur adresse `external_id` ou `alias`. Les utilisateurs anonymes peuvent être mis en relation avec leur `device_id`. Les utilisateurs identifiés qui ont été créés à l'origine en tant qu'utilisateurs anonymes ne peuvent pas être identifiés par leur `device_id`, et doivent être identifiés par leur `external_id` ou `alias`.

