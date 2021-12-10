---
nav_title: Page partenaire
page_order: 4
#Required
description: "Ceci est la description de la recherche Google. Les personnages de plus de 160 sont tronqués, concis-le brièvement."
page_type: partenaire
tool:
  - Tableau de bord
  - Documents
  - Toile
  - Campagnes
  - Segments
  - Modèles
  - Médias
  - Localisation
  - Courants
  - Rapports
platform:
  - iOS
  - Android
  - Web
  - API
channel:
  - Cartes de contenu
  - Courriel
  - Flux d'actualité
  - Messages In-App
  - Pousser
  - SMS
  - Webhooks
noindex: vrai
---

# [Nom du partenaire]

> Bienvenue dans le Modèle de Page Partenaire ! Ici, vous trouverez tout ce dont vous avez besoin pour créer votre propre page partenaire. Dans cette première section, vous devez décrire le partenaire dans le premier paragraphe d'une phrase ou deux. En outre, inclure un lien vers le site principal de ce partenaire.

Dans le deuxième paragraphe, vous devriez explorer et expliquer la relation entre Braze et ce partenaire. Ce paragraphe devrait expliquer comment Braze et ce partenaire travaillent ensemble pour resserrer le lien entre l'utilisateur de Braze et son client. Expliquez la « élévation » qui se produit lorsqu'un utilisateur de Braze s'intègre ou tire parti de ce partenaire et de ses services.

## Exigences ou pré-requis

Cette section vous propose tout ce dont vous avez besoin pour vous intégrer au partenaire et commencer à utiliser leurs services. La meilleure façon de fournir ces informations est d'utiliser un paragraphe d'instruction rapide qui décrit tous les détails non techniques importants de "besoin de savoir" des informations, que votre intégration soit ou non soumise à des contrôles de sécurité ou à des autorisations supplémentaires. Ensuite, vous devriez utiliser un tableau pour décrire les exigences techniques de l'intégration.

{% alert important %}
Les exigences énumérées ci-dessous sont des exigences typiques que vous pourriez avoir besoin du Brésil. Nous vous recommandons d'utiliser le titre attribué, l'origine, les liens et le phrasé tel que listé dans le graphique ci-dessous. Assurez-vous d'ajuster la description afin que vous sachiez à quoi sert chacune de ces exigences.
{% endalert %}

| Exigences                    | Origine             | Accès                                                                                                                                                            | Libellé                                                                                          |
| ---------------------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Braze App Group REST API Key | Plateforme de Braze | Gérer les paramètres > la page des paramètres                                                                                                                    | Cette description devrait vous indiquer ce qu'il faut faire avec la clé d'API REST Groupe d'App. |
| Braze API Endpoint           | Plateforme de Braze | Consultez nos [terminaux listés]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) ou ouvrez un [ticket de support]({{site.baseurl}}/braze_support/). | Description en attente.                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Intégration

C'est là que vous décomposez l'intégration en étapes. Ne vous contentez pas d'écrire des paragraphes interminables - ce sont des documents techniques qui seront utilisés par les marketeurs et les développeurs pour faire fonctionner l'intégration. Votre seul objectif pour cette section est d'écrire une documentation descriptive qui aide l'utilisateur de Braze à faire le travail. Par "Type d'intégration" dans le titre de la section, nous voulons indiquer si oui ou non il s'agit d'une intégration côte à côte, de serveur à serveur ou hors de la Box. Cela vous permet d'avoir plusieurs sections d'intégration s'il y a plus d'une façon d'intégrer avec ce partenaire.

S'il s'agit d'une intégration de courants, cette page devrait être située dans la section Courants, et une page de navigation correspondante devrait être construite qui redirige vers cet emplacement dans le courant.

### Étape 1 : Ceci est une courte description de l'étape 1

Il suffit de briser tout cela, y compris tout code si nécessaire. Rappelez-vous que vous pouvez offrir plusieurs ensembles de code différents - il n'y a pas besoin d'offrir une seule façon d'intégrer.

### Étape 2 : Cette étape décrira les images

Vous avez la possibilité de mettre des images dans votre documentation, donc nous vous recommandons de le faire et de le faire avec attention.

### Étape 3 : Combien d'étapes

Contour par l'utilisation de l'intégration - surtout si cela signifie l'insertion de Liquid dans notre compositeur de messages.

## Personnalisation

Ceci est une section __facultative__. Ici, vous pouvez décrire tout moyen spécifique de personnaliser votre intégration entre les deux partenaires.

## Utiliser cette intégration

Ceci devrait décrire comment utiliser l'intégration - faites savoir à votre lecteur s'il a besoin de presser quelques boutons ou s'il n'a pas besoin de rien faire après l'intégration.

### Étape 1 : Ceci est une courte description de l'étape 1

Juste votre typique étape par étape.

## Cas d'utilisation

Cela peut être une partie essentielle de votre documentation. Bien que cela soit facultatif, c'est un bon endroit pour décrire les cas d'utilisation typiques ou même les nouveaux cas d'utilisation pour l'intégration. Cela peut être utilisé comme un moyen de vendre ou de vendre la relation - il fournit le contexte, , et plus important encore, une façon de visualiser les capacités de l'intégration.
