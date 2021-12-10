---
nav_title: Votre page partenaire
page_order: 1
description: "Ceci est la description de Google Search et SEO qui apparaîtra ; essayez de rendre cette information et concise, mais brève."
alias: /fr/partners/your_partner_name/
page_type: partenaire
search_tag: Partenaire
hidden: vrai
---

# [Nom du partenaire]

> Bienvenue dans le Modèle de Page Partenaire ! Ici, vous trouverez tout ce dont vous avez besoin pour créer votre page partenaire. Dans cette première section, vous devez fournir une brève description du partenaire. En outre, inclure un lien vers le site principal de ce partenaire.

Dans le deuxième paragraphe, vous devriez explorer et expliquer la relation entre Braze et ce partenaire. Ce paragraphe devrait expliquer comment Braze et ce partenaire travaillent ensemble pour resserrer le lien entre l'utilisateur de Braze et son client. Expliquez la « élévation » qui se produit lorsqu'un utilisateur de Braze s'intègre ou tire parti de ce partenaire et de ses services.

## Pré-requis

Cette section vous propose tout ce dont vous avez besoin pour vous intégrer au partenaire et commencer à utiliser leurs services. La meilleure façon de fournir ces informations est d'utiliser un paragraphe d'instruction rapide qui décrit tous les détails non techniquement importants ou les informations "besoin de savoir" que votre intégration soit ou non soumise à des contrôles de sécurité ou à des autorisations supplémentaires. Ensuite, vous devriez utiliser un tableau pour décrire les exigences techniques de l'intégration.

{% alert important %}
Les exigences énumérées ci-dessous sont des exigences typiques que vous pourriez avoir besoin du Brésil. Nous vous recommandons d'utiliser le titre attribué, l'origine, les liens et le phrasé listés dans le graphique ci-dessous. Assurez-vous d'ajuster la description afin que les clients sachent à quoi sert chacune de ces exigences.
{% endalert %}

| Exigences                       | Origine | Accès                                                                                                                                                                                                        | Libellé                                                                                                   |
| ------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| Clé API Braze                   | Brasero | Vous devrez créer une nouvelle clé d'API.<br><br>Ceci peut être créé dans la __Console Développeur -> Paramètres API -> Créer une nouvelle clé API__ avec __utilisateurs. permissions__ de rack. | Cette description devrait vous indiquer ce que vous devez faire avec la clé API Braze.                    |
| Point de terminaison REST Braze | Brasero | [Liste des points d'extrémité REST Braze][1]                                                                                                                                                                 | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Détails de l'intégration

C'est là que vous décomposez l'intégration en étapes. Ne vous contentez pas d'écrire des paragraphes interminables - ce sont des documents techniques qui seront utilisés par les marketeurs et les développeurs pour faire fonctionner l'intégration. Votre objectif principal est d'écrire une documentation descriptive qui aide l'utilisateur de Braze à faire le travail. Par "Type d'intégration" dans le titre de la section, nous voulons indiquer s'il s'agit ou non d'une intégration côte à côte, de serveur à serveur ou hors de la boite. Cela vous permet d'avoir plusieurs sections d'intégration si plus d'une façon d'intégrer avec ce partenaire existe.

### Étape 1 : Ceci est une courte description de l'étape 1

Il suffit de briser tout cela, y compris tout code si nécessaire. Rappelez-vous que vous pouvez offrir plusieurs ensembles de code différents - il n'y a pas besoin d'offrir une seule façon d'intégrer.

### Étape 2 : Cette étape décrira les images

Vous avez la possibilité de mettre des images dans votre documentation, donc nous vous recommandons de le faire et de le faire avec attention.

### Étape 3 : Combien d'étapes

Contour d'une utilisation approfondie de l'intégration - surtout si cela signifie l'insertion de Liquid dans notre compositeur de messages.

## Personnalisation

Les options de personnalisation sont une section __facultative__. Ici, vous pouvez décrire tout moyen spécifique de personnaliser votre intégration entre les deux partenaires.

## Utiliser cette intégration

Cette section devrait décrire comment utiliser l'intégration - faites savoir à votre lecteur s'ils ont besoin de presser quelques boutons ou qu'ils n'ont pas besoin de faire quoi que ce soit après l'intégration.

### Étape 1 : Ceci est une courte description de l'étape 1

Juste votre méthode habituelle étape par étape.

## Cas d'utilisation

Les cas d'utilisation peuvent être une partie essentielle de votre documentation. Bien que cela soit facultatif, c'est un bon endroit pour décrire les cas d'utilisation typiques ou même les nouveaux cas d'utilisation pour l'intégration. Cela peut être utilisé comme un moyen de vendre ou de vendre la relation - il fournit le contexte, , et plus important encore, une façon de visualiser les capacités de l'intégration.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints

