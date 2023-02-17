---
nav_title: Votre page partenaire
article_title: Votre page partenaire
page_order: 1

description: "Il s'agit de la description qui apparaîtra dans le moteur de recherche et de référencement de Google. Essayez de la rendre informative et concise, mais brève."
alias: /partners/your_partner_name/

page_type: partner
search_tag: Partenaire
hidden: true

---

# [Nom du partenaire]

> Bienvenue dans le modèle de partenaire Braze ! Ici, vous trouverez tout ce dont vous avez besoin pour créer votre page partenaire. Dans cette première section, écrivez une brève description de votre entreprise. Incluez également un lien vers votre site principal. 
Dans ce second paragraphe, expliquez la relation entre votre entreprise et Braze. Ce paragraphe doit expliquer comment Braze et votre entreprise collaborent pour reserrer le lien entre l’utilisateur Braze et son client. Expliquez ce qui se produit lorsqu'un utilisateur de Braze s'intègre ou tire parti de votre partenariat et des services que vous offrez.

## Conditions préalables

Cette section doit indiquer ce dont vous avez besoin pour terminer cette intégration de partenariat. La meilleure façon de fournir ces informations est de rédiger un paragraphe d'instructions rapides qui décrit tous les détails non techniques importants ou les informations à connaître, comme le fait de savoir si votre intégration sera soumise ou non à des contrôles de sécurité ou à des habilitations supplémentaires. Utilisez ensuite un graphique pour décrire les exigences techniques de l’intégration.

{% alert important %}
Les exigences suivantes sont des exigences typiques dont vous pourriez avoir besoin pour Braze. Nous vous recommandons d'utiliser le titrage et le phrasé attribués figurant dans le tableau suivant. Assurez-vous d’ajuster les descriptions et de les adapter à votre intégration de partenariat. 
{% endalert %}

| Configuration requise | Description |
| ----------- | ----------- |
| Compte partenaire | Un compte partenaire est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. .|
| Endpoint REST de Braze | [URL de votre endpoint REST][1]. Votre endpoint dépendra de l’URL Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d’utilisation

Les cas d’utilisation peuvent constituer un élément essentiel de votre documentation. Bien que ce ne soit pas obligatoire, vous pouvez définir à cet endroit les cas d’utilisation typiques ou nouveaux pour l’intégration. Cela peut être utilisé comme un moyen de vendre ou de proposer une montée en gamme. Fournit du contexte, des idées et, surtout, un moyen de visualiser les capacités de l'intégration.

## Intégration

C’est là que vous divisez l’intégration en étapes. N’écrivez pas des paragraphes sans fin : il s’agit de documents techniques qui seront utilisés par les marketeurs et les développeurs à des fins d’intégration et d’exécution. Votre principal objectif est d’écrire une documentation descriptive qui aide l’utilisateur Braze à faire son travail. 

Éventuellement, vous pouvez également préciser qu’il s’agit d’une intégration côte à côte, serveur à serveur ou basique. Cela vous permet d’avoir plusieurs sections d’intégration si plusieurs méthodes d’intégration existent.

### Étape 1 : Brève description de l’étape 1 

Rédigez une brève description pour chaque étape, et écrivez du code si nécessaire. N’oubliez pas que vous pouvez proposer plusieurs jeux de code : il n’est pas nécessaire de ne fournir qu’un seul moyen d’intégrer.

### Étape 2 : Brève description de l’étape 2 

Vous pouvez également ajouter des images à votre documentation. Nous recommandons d'inclure des images des étapes clés de l'intégration, car les images confirment très bien ce que les utilisateurs doivent voir lorsqu'ils progressent dans les différentes étapes.

### Étape 3 : Brève description de l’étape 3 

Décrivez l’utilisation d’une intégration approfondie, surtout si elle inclut l’insertion de Liquid dans notre éditeur de messages. Si votre intégration exploite un webhook Braze, nous vous recommandons de suivre les étapes de mise en forme de webhook suivantes sur votre page partenaire.

{% details Webhook formatting %}
```
### Étape 2 : Créer un webhook [partenaire] dans Braze
Pour créer un modèle de webhook [partenaire] à utiliser dans les campagnes ou les Canvas, accédez à la section **Templates & Media (Modèles et médias)** sur la plateforme Braze. Si vous souhaitez créer une campagne de webhook [partenaire] unique ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d’une nouvelle campagne.
Une fois que vous avez sélectionné le modèle de webhook [partenaire], les éléments suivants s’affichent :
- **URL du webhook **: [URL webhook partenaire]
- **Corps de la demande** : Texte brut
#### En-têtes et méthode de demande
Le [partenaire] nécessite un `En-tête HTTP` pour l’autorisation. Les éléments suivants seront déjà inclus dans le modèle en tant que paires clé-valeur.
{% raw %}
- **Méthode HTTP** : POST
- **En-tête de demande** :
  - **Autorisation** : Bearer [PARTNER_AUTHORIZATION_HEADER]
  - **Corps de la demande** : application/json
{% endraw %}
#### Corps de la demande
Contient le code du corps de votre demande de webhook. 
### Étape 3 : Prévisualiser votre demande
Prévisualisez votre demande dans le volet **Preview** (Prévisualiser) ou accédez à l’onglet `Test` où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant ou personnaliser votre propre test pour tester votre webhook.
{% alert important %}
N’oubliez pas d’enregistrer votre modèle avant de quitter la page ! <br>Des modèles de webhook mis à jour sont disponibles dans la liste **Modèles de webhooks enregistrés** lorsque vous créez une nouvelle [campagne de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 
{% endalert %}
```
{% enddetails %}

## Personnalisation

La personnalisation est une section **facultative**. Ici, vous pouvez présenter des façons spécifiques de personnaliser votre intégration entre les deux partenaires.

## Comment utiliser cette intégration

Cette section doit décrire comment utiliser l’intégration à Braze. Grâce à cette section, les utilisateurs peuvent apprendre comment accéder aux données (le cas échéant) fournies à Braze dans le cadre d’une intégration, et comment les exploiter dans la messagerie Braze.

### Étape 1 : Brève description de l’étape 1 

Ces étapes vont guider vos utilisateurs et leur expliquer comment effectuer cette intégration à Braze.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
