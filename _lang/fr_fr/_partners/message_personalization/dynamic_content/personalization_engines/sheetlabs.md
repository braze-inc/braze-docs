---
nav_title: Sheetlabs
article_title: Sheetlabs
description: "Cet article de référence décrit le partenariat entre Braze et Sheetlabs, un service qui vous permet de personnaliser vos campagnes marketing avec des données provenant de feuilles de calcul."
alias: /partners/sheetlabs/
page_type: partner
search_tag: Partner
---

# Sheetlabs

> [Sheetlabs](https://sheetlabs.com/) est une plateforme qui vous permet de transformer des feuilles de calcul en API puissantes et bien documentées. Vous pouvez importer des données depuis Google Sheets ou Excel, les transformer en API, puis utiliser cette API dans d'autres applications, telles que Braze.
_Cette intégration est maintenue par Sheetlabs._

## À propos de l'intégration

L'intégration de Sheetlabs et Braze vous permet de tirer parti du [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/) pour inclure les API de Sheetlabs dans vos campagnes marketing Braze. Ceci est couramment utilisé pour fournir un pont entre une feuille de calcul Google (qui est mise à jour directement par l'équipe marketing) et les modèles Braze. Cela vous permet d’exploiter pleinement les modèles Braze, et ainsi obtenir des traductions ou des ensembles plus importants d'attributs personnalisés.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Sheetlabs | Un [compte Sheetlabs](https://sheetlabs.com/) est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

L'intégration de Braze et Sheetlabs vous permet de réaliser les cas d'utilisation suivants :

1. **Séparer l'accès des marketeurs de l'accès aux campagnes Braze** : Certaines Teams souhaitent éviter de donner à tout le personnel l'accès à la configuration directe des modèles et du contenu Braze. Au lieu de cela, ils veulent que le personnel mette à jour le contenu marketing dans une feuille de calcul. Sheetlabs fournit le pont entre les feuilles de calcul et Braze et peut être mis à jour en temps réel.
2. **Traductions**: Les modèles Braze ne prennent pas en charge nativement les traductions. Si vous souhaitez prendre en charge plusieurs langues, vous devez créer plusieurs modèles. En utilisant Sheetlabs en conjonction avec Braze, vous pouvez avoir un seul modèle Braze traduit en plusieurs langues.
3. **Extension des attributs personnalisés**: Braze fournit un certain nombre d'attributs personnalisés qui peuvent être configurés. En utilisant Sheetlabs en conjonction avec Braze, vous pouvez ajouter des attributs personnalisés supplémentaires au-delà de cette allocation initiale.

Reportez-vous à [Sheetlabs](https://app.sheetlabs.com/docs/producers/braze/) pour plus d'informations sur ces cas d'utilisation.

## Intégration

### Étape 1 : Importez votre feuille de calcul dans Sheetlabs

Dans Sheetlabs, téléchargez une feuille de calcul Excel ou liez votre compte Google et importez une feuille Google. 

- Pour importer une feuille de calcul Excel, cliquez sur **Tables de données** dans la barre de menu, puis sur **Importer depuis CSV/Excel**.
- Pour importer depuis Google Sheets, cliquez sur **Tables de données** dans la barre de menu, puis sur **Importer depuis Google**. Vous devez ensuite fournir vos identifiants Google et importer la feuille.

Vous pouvez également choisir de garder votre feuille Google synchronisée, ce qui signifie que Sheetlabs récupérera automatiquement les dernières données de votre feuille Google lorsqu'elle change.

Assurez-vous d'inclure l'ID utilisateur Braze dans votre feuille de calcul ou quelque chose d'autre que vous pouvez utiliser comme référence plus tard.

### Étape 2 : Créer une API dans Sheetlabs

Ensuite, dans Sheetlabs, accédez à **APs > Créer une API** et donnez un nom à votre API. Vous voudrez probablement autoriser les requêtes via un champ de recherche de votre feuille de calcul, tel que l'ID utilisateur Braze.

À ce stade, vous devriez pouvoir accéder à votre API à l’aide d’un lien du type :<br> [`https://sheetlabs.com/ACME/email1_translations?country=en`](https://sheetlabs.com/ACME/email1_translations?country=en).

### Étape 3 : Utilisez l'API dans le contenu connecté de Braze

Maintenant que votre API est accessible, vous pouvez l'utiliser dans vos appels de contenu connecté. Voici un exemple de ce à quoi pourrait ressembler un modèle de traductions :

{% raw %}
```js
{% connected_content https://sheetlabs.com/ACME/email1_translations?country={{${country}}} :save translations %}

{{translations[0].greeting}} {{${first_name}}},

{{translations[0].message_body}}
```
{% endraw %}
{% alert tip %}
Pour plus d'exemples et de conseils sur l'intégration avec Sheetlabs, consultez la [documentation de Sheetlabs](https://app.sheetlabs.com/docs/producers/braze/).
{% endalert %}
