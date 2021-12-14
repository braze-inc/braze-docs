---
nav_title: Votre page partenaire
article_title: Votre page partenaire
page_order: 1
description: "Ceci est la description de Google Search et SEO qui apparaîtra ; essayez de rendre cette information et concise, mais brève."
alias: /fr/partners/your_partner_name/
page_type: partenaire
search_tag: Partenaire
hidden: vrai
---

# [Nom du partenaire]

> Bienvenue dans le modèle partenaire de Braze ! Ici, vous trouverez tout ce dont vous avez besoin pour créer votre page partenaire. Dans cette première section, incluez une brève description de votre entreprise. De plus, incluez un lien vers votre site principal.

Dans ce deuxième paragraphe, explorez la relation entre votre entreprise et le Brésil. Ce paragraphe devrait expliquer comment Braze et votre partenaire de l'entreprise ensemble pour resserrer le lien entre l'utilisateur de Braze et son client. Expliquez la « élévation » qui se produit lorsqu'un utilisateur de Braze s'intègre à votre partenariat et les services que vous offrez.

## Pré-requis

Cette section devrait énumérer ce dont vous avez besoin pour compléter cette intégration de partenariat. La meilleure façon de fournir ces informations est d'utiliser un paragraphe d'instruction rapide qui décrit tous les détails non techniquement importants ou les informations "besoin de savoir" que votre intégration soit ou non soumise à des contrôles de sécurité ou à des autorisations supplémentaires. Ensuite, utilisez un graphique pour décrire les exigences techniques de l'intégration.

{% alert important %}
Les exigences énumérées ci-dessous sont des exigences typiques que vous pourriez avoir besoin du Brésil. Nous vous recommandons d'utiliser le titre et le libellé attribués listés dans le graphique ci-dessous. Assurez-vous d'ajuster les descriptions et de les adapter à votre intégration de partenariat.
{% endalert %}

| Exigences                       | Libellé                                                                                                                                                                                                      |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Compte partenaire               | Un compte partenaire est requis pour profiter de ce partenariat.                                                                                                                                             |
| Braze clé API REST              | Une clé API Braze REST avec les permissions `users.track`. <br><br> Ceci peut être créé dans le __tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__ |
| Point de terminaison REST Braze | [Votre URL de fin REST][1]. Votre point de terminaison dépendra de l'URL de Braze pour votre instance.                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d'utilisation

Les cas d'utilisation peuvent être une partie essentielle de votre documentation. Bien que facultatif, c'est un bon endroit pour décrire les cas d'utilisation typiques ou même romans pour l'intégration. Cela peut être utilisé comme un moyen de vendre ou de vendre la relation - il fournit le contexte, , et plus important encore, une façon de visualiser les capacités de l'intégration.

## Intégration

C'est là que vous décomposez l'intégration en étapes. Ne vous contentez pas d'écrire des paragraphes interminables - ce sont des documents techniques qui seront utilisés par les marketeurs et les développeurs pour faire fonctionner l'intégration. Votre objectif principal est d'écrire une documentation descriptive qui aide l'utilisateur de Braze à faire le travail.

En option, vous pouvez également fournir des détails sur si c'est une intégration côte à côte, serveur à serveur ou hors de la boîte. Cela vous permet d'avoir plusieurs sections d'intégration si plusieurs façons d'intégrer existent.

### Étape 1 : brève description de l'étape 1

Fournir une courte description pour chaque étape, y compris tout code, si nécessaire. Rappelez-vous que vous pouvez offrir plusieurs ensembles de codes différents - il n'y a pas besoin de fournir seulement une seule façon d'intégrer.

### Étape 2 : Description courte de l'étape 2

Vous pouvez également ajouter des images à votre documentation. Nous recommandons d'inclure des images des étapes d'intégration clés car les images font un excellent travail de confirmation de ce que les utilisateurs devraient voir au fur et à mesure qu'ils progressent à travers les différentes étapes.

### Étape 3 : Description courte de l'étape 3

Configurez une utilisation approfondie de l'intégration, surtout si cela inclut l'insertion de Liquid dans notre compositeur de messages. Si votre intégration tire parti d'un webhook Braze, nous vous recommandons d'inclure les étapes suivantes de formatage du webhook dans votre page partenaire.

{% details Webhook formatting %}
```
### Étape 2 : Créer un webhook [Partner] dans Braze

Pour créer un modèle [Partner] de webhook à utiliser dans les futures campagnes ou Canvases, accédez à la section **Modèles & Médias** de la plateforme Braze. Si vous souhaitez créer une campagne de webhook [Partner] unique ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d'une nouvelle campagne.

Une fois que vous avez sélectionné le modèle [Partner] de webhook, vous devriez voir ce qui suit :
- **URL Webhook** : [URL du Webhook du partenaire]
- **Corps de la requête** : Texte brut

#### En-têtes de requête et méthode

[Partner] requiert un `En-tête HTTP` pour autorisation. Les éléments suivants seront déjà inclus dans le modèle en tant que paires clé-valeur.

{% raw %}
- **Méthode HTTP** : POST
- **En-tête de la requête** :
  - **Autorisation** : Porteur [PARTNER_AUTHORIZATION_HEADER]
  - **Corps de la requête** : application/json
{% endraw %}

#### Corps de la requête

Inclure le code de votre corps de requête sur le webhook. 

### Étape 3: Aperçu de votre demande

Aperçu de votre demande dans le panneau de gauche ou aller à l'onglet `Test`, où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant ou personnaliser le vôtre pour tester votre webhook.

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page ! <br>Les modèles de webhook mis à jour peuvent être trouvés dans la liste des **Modèles de Webhook enregistrés** lors de la création d'une nouvelle [campagne de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 
{% endalert %}
```
{% enddetails %}

## Personnalisation

La personnalisation est une section **facultative**. Ici, vous pouvez définir des moyens spécifiques pour personnaliser votre intégration entre les deux partenaires.

## Utiliser cette intégration

Cette section devrait décrire comment utiliser l'intégration en Brésil. Faites savoir aux utilisateurs comment accéder aux données (s'il y en a) fournies à Braze à travers l'intégration et comment les utiliser dans la messagerie de Braze.

### Étape 1 : brève description de l'étape 1

Cet ensemble d'étapes guidera vos utilisateurs à travers la façon d'utiliser cette intégration au Brésil.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints