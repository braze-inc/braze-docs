---
nav_title: Zeotap
description: "Cet article de référence décrit le partenariat entre Braze et Zeotap, une plateforme de données clients de nouvelle génération qui fournit des solutions d'identité, des informations exploitables et des outils d’enrichissement des données."
page_type: partner
search_tag: Partner
page_order: 1
---

# Zeotap

> [Zeotap](https://zeotap.com/) est une plateforme de données clients de nouvelle génération qui vous aide à découvrir et à comprendre votre audience mobile grâce à des outils de résolution d'identité, des informations exploitables et des données enrichies.

Grâce à l'intégration de Zeotap et Braze, vous pouvez étendre l'échelle et la portée de vos campagnes en synchronisant les segments clients de Zeotap pour associer les données des utilisateurs aux comptes utilisateurs de Braze. Vous pouvez ensuite agir sur la base de ces données, en proposant des expériences ciblées personnalisées à vos utilisateurs.

## Prérequis

| Condition | Descriptif |
| --- | --- |
|Compte Zeotap | Un [compte Zeotap](https://zeotap.com/) est nécessaire pour bénéficier de ce partenariat. |
| Clé d'API REST Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST Braze  | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({% image_buster /assets/img/zeotap/zeotap1.png %}). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Intégration

### Étape 1 : Créez une destination Zeotap

1. Depuis la plateforme Zeotap Unity, accédez à l'application **DESTINATIONS**.
2. Sous **Toutes les chaînes**, sélectionnez **Braze**.
3. Dans l'invite qui apparaît, nommez votre destination et indiquez le nom de votre client et la clé API Braze REST associée à votre compte Braze.
4. Enfin, sélectionnez votre instance d'endpoint Braze REST dans la liste déroulante et enregistrez la destination. <br><br>![]({% image_buster /assets/img/zeotap/zeotap1.png %})

### Étape 2 : Créez et liez un segment Zeotap à votre destination 
 
1. Depuis la plateforme Zeotap Unity, accédez à l'application **CONNECT**.
2. Créez un segment et sélectionnez la destination Braze créée à l'étape 1.
3. Sélectionnez un identifiant de sortie compatible : MAIDs, adresse e-mail hachée en SHA256 ou tout identifiant client 1P reconnu par Braze (si vous souhaitez utiliser un identifiant personnalisé pour votre compte Braze, contactez Zeotap afin qu'il puisse être activé pour votre compte). Un seul identifiant de sortie peut être utilisé pour l'intégration de Braze. Ces identifiants doivent être identiques à l'ID externe défini lors de la collecte des données du SDK Braze.
4. Enregistrez le segment.

![]({% image_buster /assets/img/zeotap/zeotap2.png %})

{% alert note %}
Les identifiants qui apparaissent sont à la fois disponibles dans le segment et pris en charge par Braze.
{% endalert %}

### Étape 3 : Créer un segment Braze

Après avoir créé, poussé et traité avec succès un segment dans Zeotap, les utilisateurs de Zeotap apparaîtront dans le tableau de bord de Braze. Vous pouvez rechercher des utilisateurs par ID utilisateur dans le tableau de bord de Braze. 

![Profil d'un utilisateur de Braze montrant les segments un à quatre listés comme "vrais" sous "Attributs personnalisés".]({% image_buster /assets/img/zeotap/zeotap4.png %})

Si un utilisateur fait partie du segment Zeotap, le nom du segment apparaît en tant qu'attribut personnalisé sur son profil utilisateur avec une valeur booléenne. `true` Prenez note du nom de l'attribut personnalisé car vous en aurez besoin lors de la création d'un segment Braze. 

Ensuite, vous devez créer et définir ce segment dans Braze :
1. Dans le tableau de bord de Braze, sélectionnez **Segments**, puis **Créer un segment**.
2. Ensuite, nommez votre segment et sélectionnez le segment d'attribut personnalisé créé dans Zeotap.
3. Enregistrez vos modifications. 

![Dans le générateur de segments de Braze, vous trouverez les segments importés définis en tant qu'attributs personnalisés.]({% image_buster /assets/img/zeotap/zeotap3.png %})

Vous pouvez désormais ajouter ce segment nouvellement créé aux futures campagnes Braze et Canvases pour cibler ces utilisateurs finaux. 

