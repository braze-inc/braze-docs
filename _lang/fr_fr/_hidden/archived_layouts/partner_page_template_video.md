---
nav_title: Page Partenaire avec vidéo

page_order: 4

#Required
description: "Il s’agit de la description Google Search. Les phrases de plus de 160 caractères seront tronquées… soyez concis !"
page_type: partner
tool:
  - Dashboard
  - Docs
  - Canvas
  - Campaigns
  - Segments
  - Templates
  - Media
  - Location
  - Currents
  - Reports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - Content Cards
  - Email
  - News Feed
  - In-App Messages
  - Push
  - SMS
  - Webhooks
  
noindex: true
#ATTENTION: remove noindex and this alert from template

---

# [Nom du partenaire]

{% multi_lang_include video.html id="XY5uXoKIvFY" align="right" %}

> Bienvenue dans le modèle de la page Partenaire ! Ici, vous trouverez tout ce dont vous avez besoin pour créer votre propre page Partenaire. Dans cette première section, ajoutez une phrase ou deux pour décrire le partenaire dans le premier paragraphe. Pensez également à ajouter un lien vers le site Web du partenaire.

Dans le second paragraphe, expliquez la relation entre Braze et ce partenaire. Ce paragraphe doit expliquer comment Braze et ce partenaire collaborent pour resserrer le lien entre l’utilisateur Braze et son client. Expliquez ce qui se produit lorsqu'un utilisateur de Braze s'intègre ou tire parti de ce partenaire et des services qu’il propose.

## Exigences ou conditions préalables

Cette section détaille tout ce dont vous avez besoin pour intégrer ce partenaire et commencer à utiliser ses services. La meilleure façon de fournir ces informations est de rédiger un paragraphe d'instructions rapides qui décrit tous les détails non techniques importants ou les informations à connaître, comme le fait de savoir si votre intégration sera soumise ou non à des contrôles de sécurité ou à des habilitations supplémentaires. Utilisez ensuite un graphique pour décrire les exigences techniques de l’intégration.

{% alert important %}
Les exigences suivantes sont des exigences générales dont vous pourriez avoir besoin pour Braze. Nous vous recommandons d'utiliser le titrage, l’origine, les liens et le phrasé attribués dans le tableau suivant. Assurez-vous de modifier la description pour vous souvenir de ce que chacune de ces exigences permet de faire.
{% endalert %}

| Condition | Origine | Accès | Description |
|---|---|---|---|
|Clé de l'API REST de l'espace de travail de Braze | Plateforme Braze | **Paramètres** > **Paramètres des applications** | Cette description devrait vous indiquer comment procéder avec la clé API REST de l'espace de travail. |
|Point d'endpoint de l'API Braze | Plateforme Braze | Consultez la [liste de nos endpoints]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) ou créez un [ticket de support]({{site.baseurl}}/braze_support/). | Description en attente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## [Type d'intégration] Intégration

C’est là que vous divisez l’intégration en étapes. N’écrivez pas de paragraphes sans fin. Il s’agit de documents techniques qui seront utilisés par des spécialistes du marketing et des développeurs à des fins d’intégration et d’exécution. Dans cette section, votre seul objectif est d’écrire une documentation descriptive qui aide l’utilisateur Braze à faire son travail. Dans le titre de la section, le « type d’intégration » permet d’indiquer s’il s’agit d’une intégration côte à côte, serveur à serveur ou prête à l’emploi. Cela vous permet d’avoir plusieurs sections d’intégration, s’il existe plus d’une méthode d’intégration pour ce partenaire.

S’il s’agit d’une intégration Currents, cette page doit se trouver dans la section Currents et vous devrez créer une page de navigation qui redirige vers cet emplacement dans Currents.

### Étape 1 : Ceci est une brève description de la première étape

Décrivez l’étape en incluant du code si nécessaire. N’oubliez pas que vous pouvez proposer plusieurs jeux de code : rien ne vous oblige à ne proposer qu’un seul moyen d’intégration.

### Étape 2 : Cette étape a pour but de décrire les images

Vous avez la possibilité d’ajouter des images dans votre documentation. Nous vous recommandons de le faire et de le faire avec attention.

### Exemple de code

Si vous expliquez un concept technique, notez-le ici et présentez un exemple de code.

```html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
```

Pensez à définir les paramètres ou éléments que les utilisateurs devront ajuster dans l’exemple de code. De nombreux utilisateurs se contenteront de le copier-coller.

| Variable | Description |
| -------- | ----------- |
| Titre de la page | Choisissez le nom que vous voulez pour votre page. Votre page doit comporter un nom. |
| Mon premier titre | Nous recommandons de le mettre en majuscule. Cependant, cela reste optionnel. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


### Étape 3 : Nombre d’étapes

Décrivez l’utilisation de l’intégration, surtout si elle inclut l’insertion de Liquid dans notre éditeur de messages.

## Personnalisation

Cette section est **facultative**. Ici, vous pouvez présenter des manières spécifiques de personnaliser votre intégration entre les deux partenaires.

## Comment utiliser cette intégration

Expliquez ici comment utiliser l’intégration en indiquant à vos lecteurs s’ils doivent cliquer sur un bouton ou si au contraire ils n’ont rien besoin de faire après l’intégration.

### Étape 1 : Ceci est une brève description de la première étape

Décrivez simplement le processus étape par étape.

### Exemple de code

Si vous expliquez un concept technique, notez-le ici et présentez un exemple de code.

```html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
```

Pensez à définir les paramètres ou éléments que les utilisateurs devront ajuster dans l’exemple de code. De nombreux utilisateurs se contenteront de le copier-coller.

| Variable | Description |
| -------- | ----------- |
| Titre de la page | Choisissez le nom que vous voulez pour votre page. Votre page doit comporter un nom. |
| Mon premier titre | Nous recommandons de le mettre en majuscule. Cependant, cela reste optionnel. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


## Cas d’utilisation

Il s’agit de l’une des parties les plus importantes de votre documentation. Bien que ce ne soit pas obligatoire, vous pouvez définir à cet endroit les nouveaux cas d’utilisation et les cas d’utilisation types de l’intégration. Cela peut être utilisé comme un moyen de vendre ou de proposer une montée en gamme. Ces explications apportent du contexte, des idées et, surtout, un moyen de mieux comprendre les capacités de l'intégration.
