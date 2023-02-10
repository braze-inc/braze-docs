---
nav_title: Sheetlabs
article_title: Sheetlabs
description: "Cet article présente le partenariat entre Braze et Sheetlabs, un service qui vous permet de personnaliser vos campagnes de marketing à l'aide de données issues de feuilles de calcul."
alias: /partners/sheetlabs/
page_type: partner
search_tag: Partenaire

---

# Sheetlabs

> [Sheetlabs][1] est une plateforme qui vous permet de transformer des feuilles de calcul en API puissantes et bien documentées. Vous pouvez importer des données de Google Sheets ou d'Excel, les transformer en une API, puis utiliser cette API dans d'autres applications, comme Braze.

L'intégration de Sheetlabs et Braze vous permet de tirer parti de [Contenu connecté][2] pour inclure les API de Sheetlabs dans vos campagnes de marketing Braze. Cette fonction est généralement utilisée pour faire le lien entre une feuille de calcul Google (qui est mise à jour directement par l'équipe marketing) et les modèles de Braze. Cela vous permet d'obtenir plus de résultats avec les modèles Braze, comme des traductions ou des ensembles plus importants d'attributs personnalisés.

## Conditions préalables

| Configuration requise | Description |
| ----------- | ----------- |
| Compte Sheetlabs | Un [compte Sheetlabs][1] est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d’utilisation

L'intégration de Braze et de Sheetlabs vous permet de réaliser les cas d'utilisation suivants :

1. **Séparer l'accès des spécialistes marketeur de l'accès aux campagnes Braze** : Certaines équipes souhaitent éviter de donner à tout le personnel l'accès à la configuration directe des modèles et du contenu de Braze. Au lieu de cela, ils veulent que le personnel mette à jour le contenu marketing dans une feuille de calcul. Sheetlabs constitue le pont entre les feuilles de calcul et Braze et peut être mis à jour en temps réel.
2. **Traductions** : Les modèles Braze ne prennent pas en charge les traductions de manière native. Si vous souhaitez prendre en charge plusieurs langues, vous devez créer plusieurs modèles. En utilisant Sheetlabs conjointement avec Braze, vous pouvez disposer d'un modèle Braze unique traduit en plusieurs langues.
3. **Étendre les attributs personnalisés** : Braze fournit un certain nombre d’attributs personnalisés pouvant être configurés. En utilisant Sheetlabs en conjonction avec Braze, vous pouvez ajouter des attributs personnalisés supplémentaires au-delà de cette attribution initiale.

Reportez-vous à [Sheetlabs][3] pour plus d'informations sur ces cas d'utilisation.

## Intégration

### Étape 1 : Importer votre feuille de calcul dans Sheetlabs

Dans Sheetlabs, uploadez une feuille de calcul Excel, ou connectez votre compte Google et importez une feuille de calcul Google. 

- Pour importer une feuille de calcul Excel, cliquez sur **Data Tables (Tableaux de données)** dans la barre de menus, puis sur **Import from CSV/Excel (Importer depuis CSV/Excel)**.
- Pour importer à partir de Google Sheets, cliquez sur **Data Tables (Tableaux de données)** dans la barre de menu, puis sur **Import from Google (Importer depuis Google)**. Vous devrez ensuite fournir vos identifiants de connexion Google et importer la feuille.

Vous pouvez également choisir de maintenir votre Google Sheet en synchronisation, ce qui signifie que Sheetlabs récupère automatiquement les dernières données de votre Google Sheet lorsqu'elles sont modifiées.

Veillez à inclure l'ID de l'utilisateur Braze dans votre feuille de calcul ou dans un autre document que vous pourrez utiliser comme référence ultérieurement.

### Étape 2 : Créer une API dans Sheetlabs

Ensuite, dans Sheetlabs, allez dans **APIs > Create API (APIs > Créer une API)**, et donnez un nom à votre API. Vous souhaiterez probablement autoriser les requêtes via un champ de recherche de votre feuille de calcul, tel que l'ID utilisateur Braze.

À ce stade, vous devriez être en mesure d'accéder à votre API à l'aide d'un lien comme celui-ci :<br> [`https://sheetlabs.com/ACME/email1_translations?country=en`][4].

### Étape 3 : Utiliser l'API dans le Contenu connecté de Braze

Maintenant que votre API est accessible, vous pouvez l'utiliser dans vos appels de Contenu connecté. Voici un exemple de ce à quoi pourrait ressembler un modèle de traduction :

{% raw %}
```js
{% connected_content https://sheetlabs.com/ACME/email1_translations?country={{${country}}} :save translations %}

{{translations[0].greeting}} {{${first_name}}},

{{translations[0].message_body}}
```
{% endraw %}

{% alert tip %}
Pour plus d'exemples et de conseils sur l'intégration avec Sheetlabs, consultez la [documentation Sheetlabs](https://app.sheetlabs.com/docs/producers/braze/).
{% endalert %}


[1]: https://sheetlabs.com/
[2]: https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[3]: https://app.sheetlabs.com/docs/producers/braze/
[4]: https://sheetlabs.com/ACME/email1_translations?country=en
