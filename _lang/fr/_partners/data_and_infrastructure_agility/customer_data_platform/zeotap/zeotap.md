---
nav_title: Zeotap
description: "Cet article de référence présente le partenariat entre Braze et Zeotap, une plateforme de données client de nouvelle génération qui fournit des résolutions d’identité, des informations et des enrichissements."
page_type: partner
search_tag: Partenaire
page_order: 0
---

# Zeotap

> [Zeotap](https://zeotap.com/) est une plateforme de données client de nouvelle génération qui vous aide à découvrir et à comprendre votre audience mobile en fournissant des résolutions d’identité, des informations et des enrichissements de données.

Avec l’intégration Zeotap et Braze, vous pouvez étendre l’ampleur et la portée de vos campagnes en synchronisant les segments clients de Zeotap pour mapper les données utilisateur vers les comptes utilisateur de Braze. Vous pouvez ensuite vous servir de ces données pour offrir des expériences personnalisées et ciblées à vos utilisateurs.

## Conditions préalables

| Condition | Description |
| --- | --- |
|Compte Zeotap | Un [compte Zeotap](https://zeotap.com/) est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze  | URL de votre endpoint REST. Votre endpoint dépendra de l’[URL Braze pour votre instance][1]. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Intégration

### Étape 1 : Créer une destination Zeotap

1. Depuis la plateforme Zeotap Unity, accédez à l’application **DESTINATIONS**.
2. Sous **All Channels (Tous les canaux)**, sélectionnez **Braze**.
3. Dans l’invite qui apparaît, nommez votre destination et indiquez le nom de votre client et la clé API REST de Braze associée à votre compte Braze.
4. Enfin, sélectionnez votre instance d’endpoint REST Braze dans le menu déroulant et enregistrez la destination.  <br><br>![][1]

### Étape 2 : Créer et lier un segment Zeotap à votre destination 
 
1. Depuis la plateforme Zeotap Unity, accédez à l’application **CONNECT**.
2. Créez un segment et sélectionnez la destination Braze créée à l’étape 1.
3. Sélectionnez un identifiant de sortie pris en charge : Les MAID, les adresses e-mail avec hachage SHA256, ou tout identifiant client 1P reconnu par Braze (si vous souhaitez utiliser un identifiant personnalisé pour votre compte Braze, contactez Zeotap afin qu’il puisse être activé pour votre compte). Un seul identifiant de sortie peut être utilisé pour l’intégration de Braze. Ces identifiants doivent être identiques à ceux du jeu d’ID externes lors de la collecte des données du SDK de Braze.
4. Enregistrez le segment.

![][2]

{% alert note %}
Les identifiants qui apparaissent sont disponibles dans le segment et pris en charge par Braze.
{% endalert %}

### Étape 3 : Créer un segment Braze

Après avoir créé, validé et traité avec succès un segment dans Zeotap, les utilisateurs de Zeotap apparaîtront dans le tableau de bord de Braze. Vous pouvez rechercher des utilisateurs par ID utilisateur dans le tableau de bord de Braze. 

![Un profil utilisateur Braze montrant le segment de un à quatre répertorié comme « true (vrai) » sous « Attributs personnalisés ».][4]

Si un utilisateur fait partie du segment Zeotap, le nom du segment apparaît comme un attribut personnalisé sur son profil utilisateur avec la valeur booléenne `true`. Notez le nom de l’attribut personnalisé. Vous en aurez besoin au moment de créer un segment Braze. 

Ensuite, vous devez créer et définir ce segment dans Braze :
1. Dans le tableau de bord de Braze, sélectionnez **Segments**, puis **Create Segment (Créer un segment)**.
2. Ensuite, nommez votre segment et sélectionnez le segment d’attribut personnalisé créé dans Zeotap.
3. Enregistrez vos modifications. 

![Dans le générateur de segments de Braze, vous trouverez les segments importés définis en tant qu’attributs personnalisés.][3]

Vous pouvez maintenant ajouter le segment que vous venez de créer dans de futures campagnes et Canvas de Braze pour cibler ces utilisateurs finaux. 

[1]: {% image_buster /assets/img/zeotap/zeotap1.png %}
[2]: {% image_buster /assets/img/zeotap/zeotap2.png %}
[3]: {% image_buster /assets/img/zeotap/zeotap3.png %}
[4]: {% image_buster /assets/img/zeotap/zeotap4.png %}
