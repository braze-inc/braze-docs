---
nav_title: Votre page partenaire
article_title: Votre page partenaire
page_order: 1

description: "Il s'agit de la description qui apparaîtra dans le moteur de recherche et de référencement de Google. Essayez de la rendre informative et concise, mais brève."
alias: /partners/your_partner_name/

page_type: partner
search_tag: Partenaire
hidden: true
layout: dev_guide
---

# [Nom du partenaire]

> Bienvenue dans le modèle de partenaire Braze ! Ici, vous trouverez tout ce dont vous avez besoin pour créer votre page partenaire. Dans cette première section, écrivez une brève description de votre entreprise. Incluez également un lien vers votre site principal. 
Dans ce second paragraphe, expliquez la relation entre votre entreprise et Braze. Ce paragraphe doit expliquer comment Braze et votre entreprise collaborent pour reserrer le lien entre l’utilisateur Braze et son client. Expliquez ce qui se produit lorsqu'un utilisateur de Braze s'intègre ou tire parti de votre partenariat et des services que vous offrez.

## Conditions préalables

Cette section doit indiquer ce dont vous avez besoin pour terminer cette intégration de partenariat. La meilleure façon de fournir ces informations est de rédiger un paragraphe d'instructions rapides qui décrit tous les détails non techniques importants ou les informations à connaître, comme le fait de savoir si votre intégration sera soumise ou non à des contrôles de sécurité ou à des habilitations supplémentaires. Utilisez ensuite un graphique pour décrire les exigences techniques de l’intégration.

{% alert important %}
Les exigences suivantes sont des exigences typiques dont vous pourriez avoir besoin pour Braze. Nous vous recommandons d'utiliser le titrage et le phrasé attribués figurant dans le tableau suivant. Assurez-vous d’ajuster les descriptions et de les adapter à votre intégration de partenariat. 
{% endalert %}

| Condition | Description |
| ----------- | ----------- |
| Compte partenaire | Un compte partenaire est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
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

{% details Formatage Webhook %}
```
### Step 2: Create a [Partner] webhook in Braze
To create a [Partner] webhook template to use in future campaigns or Canvases, navigate to the **Templates & Media** section in the Braze platform. If you would like to create a one-off [Partner] webhook campaign or use an existing template, select **Webhook** in Braze when creating a new campaign.
Once you have selected the [Partner] webhook template, you should see the following:
- **Webhook URL**: [Partner Webhook URL]
- **Request Body**: Raw Text
#### Request headers and method
[Partner] requires an `HTTP Header` for authorization. The following will already be included within the template as key-value pairs.
{% raw %}
- **HTTP Method**: POST
- **Request Header**:
  - **Authorization**: Bearer [PARTNER_AUTHORIZATION_HEADER]
  - **Content-Type**: application/json
{% endraw %}
#### Request body
Include code of your webhook request body. 
### Step 3: Preview your request
Preview your request in the **Preview** panel or navigate to the `Test` tab, where you can select a random user, an existing user or customize your own to test your webhook.
{% alert important %}
Remember to save your template before leaving the page! <br>Updated webhook templates can be found in the **Saved Webhook Templates** list when creating a new [webhook campaign]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 
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