---
nav_title: Audiences AppsFlyer
article_title: Audiences AppsFlyer
alias: /fr/partners/appsflyer_audiences/
description: "Cette page décrit le partenariat entre Braze et AppsFlyer Audiences, une fonctionnalité de la plateforme AppsFlyer qui vous permet de construire et de connecter efficacement les segments d'audience aux réseaux partenaires."
page_type: partenaire
search_tag: Partenaire
---

# Audiences AppsFlyer

> [AppsFlyer][1] est une plateforme d'analyse et d'attribution marketing mobile qui vous aide à analyser et optimiser vos applications par le biais de l'analyse marketing. attribut mobile, et lien profond. [AppsFlyer Audiences][2] vous permet de construire et de connecter des segments d'audience à vos réseaux partenaires.

Renforcez l'engagement des utilisateurs et augmentez l'efficacité de vos programmes de remarketing en tirant parti de la puissance des segments d'utilisateurs intégrés dans AppsFlyer Audiences. Passez vos audiences AppsFlyer (cohortes) directement à Braze pour créer de puissantes campagnes d'engagement client ciblées sur les bons utilisateurs au bon moment.

## Exigences
- __Compte AppsFlyer__ - Cette intégration de Braze n'est disponible que pour les clients AppsFlyer.
- __Braze Data Import Key et REST Endpoint__ - Cette intégration appelle le braze [/users/track/ endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour fonctionner.
- __SDKs Integrated__ - Braze SDK et AppsFlyer SDK doivent être intégrés dans votre application

## Import de cohortes AppsFlyer et Braze

Ce qui suit décrit l'intégration de Braze et AppsFlyer Public pour l'importation de cohortes en Brésil. Cette intégration prend en charge les applications iOS et Android. Si vous recherchez des informations sur la passation des données d'attribution AppsFlyer au Brésil, vous pouvez le trouver [ici][3].

### Étape 1 : Configurer le SDK de l'AppsFlyer

Pour utiliser cette intégration, vous devez passer l'ID externe Braze de l'utilisateur à AppsFlyer en utilisant la fonction `setPartnerData` du SDK AppsFlyer :

{% tabs local %}
{% tab Android %}
```java
Map<String, Object> brazeData = new HashMap<>();
partnerData.put("external_user_id", "some-braze-external-id-value");
AppsFlyerLib.getInstance().setPartnerData("braze_int", brazeData);
```
{% endtab %}
{% tab iOS %}
```objc
NSDictionary *brazeInfo = @{
     @"external_user_id":@"some-braze-external-id-value"
};
[[AppsFlyerLib shared] setPartnerDataWithPartnerId:@"braze_int" partnerInfo:brazeInfo];
```
{% endtab %}
{% endtabs %}

### Étape 2 : Obtenir la clé d'importation de données Braze et le point de terminaison REST

Dans la plateforme Braze :

1. Naviguez vers __Intégrations__ > __Partenaires technologiques__et sélectionnez __AppsFlyer__.
2. Dans la section __Data Import Using Cohort Import__ en bas de la page, cliquez sur __Générer une nouvelle clé__ pour générer votre clé d'importation de données.
3. Copiez cette clé et le point de terminaison REST à utiliser lors de la configuration d'une connexion Braze dans les audiences AppsFlyer.<br><br>!\[data_import_key\]\[5\]{: style="max-width:70%;"}

### Étape 3 : Configurer une connexion Braze dans les audiences AppsFlyer

Sur la plateforme AppsFlyer, dans les audiences AppsFlyer :

1. Allez dans l'onglet **Connexions** et cliquez sur **Ajouter une connexion partenaire**.
2. Sélectionnez Braze comme partenaire et donnez un nom à la connexion.
3. Entrez la clé d'importation de données et le point de terminaison REST que vous avez copié depuis votre compte Braze à l'étape 2.
4. Enregistrez la connexion, et il sera disponible pour créer un lien vers un public nouveau ou existant.<br><br>!\[partner_connection\]\[6\]{: style="max-width:70%;"}

En savoir plus sur la façon de travailler avec les connexions partenaires dans la documentation [AppsFlyer][4].

### Étape 4 : Utiliser des audiences AppsFlyer dans Braze

Une fois qu'une audience AppsFlyer a été téléchargée sur Braze, vous pouvez l'utiliser comme un filtre lors de la définition de segments dans Braze en sélectionnant le filtre __AppsFlyer Cohorts__.

!\[cohort_filter\]\[7\]{: style="max-width:70%;"}
[5]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_data_import_key.png %} [6]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_braze_connection.png %} [7]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_cohorts_as_filter.png %}

[1]: https://www.appsflyer.com/
[2]: https://www.appsflyer.com/product/audiences/
[3]: https://www.braze.com/docs/partners/message_orchestration/attribution/appsflyer/appsflyer/
[4]: https://support.appsflyer.com/hc/en-us/articles/115002689186-Audiences-guide#managing-connections

