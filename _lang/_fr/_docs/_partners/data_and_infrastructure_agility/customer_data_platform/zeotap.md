---
nav_title: Zéotap
description: "Cet article décrit le partenariat entre Braze et Zeotap, une plate-forme de données clients de nouvelle génération qui fournit une résolution d’identité, des idées et un enrichissement."
alias: /fr/partners/zeotap/
page_type: partenaire
search_tag: Partenaire
---

# Zéotap

> [Zeotap](https://zeotap.com/) est une plateforme de données client de nouvelle génération qui vous aide à découvrir et à comprendre votre audience mobile en fournissant une résolution d'identité. les idées et l'enrichissement des données.

Avec l'intégration de Zeotap et Braze, vous pouvez étendre l'échelle et la portée de vos campagnes en synchronisant les segments clients de Zeotap pour mapper les données des utilisateurs à Braze. Vous pouvez ensuite agir sur ces données, en fournissant des expériences ciblées personnalisées à vos utilisateurs.

## Pré-requis

| Exigences                       | Libellé                                                                                                                                                                                                      |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Compte Zeotap                   | Un compte [Zeotap](https://zeotap.com/) est requis pour profiter de ce partenariat.                                                                                                                          |
| Braze clé API REST              | Une clé API Braze REST avec les permissions `users.track`. <br><br> Ceci peut être créé dans le **tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API** |
| Point de terminaison REST Braze | Votre URL de terminaison REST. Votre point de terminaison dépendra de \[l'URL de Braze pour votre instance\]\[1\].                                                                                           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Intégration

### Étape 1 : Créer une destination Zeotap

1. Depuis la plateforme Zeotap Unity, accédez à l'application **DESTINATIONS**.
2. Sous **Tous les canaux**, sélectionnez **Braze**.
3. Dans l'invite qui apparaît, nommez votre destination et indiquez votre nom de client et la clé API Braze REST associée à votre compte Braze.
4. Enfin, sélectionnez votre instance de terminaison Braze REST dans la liste déroulante et enregistrez la destination. <br><br>!\[Zeotap Braze destination\]\[1\]

### Étape 2 : Créer et lier un segment de Zeotap à votre destination

1. Depuis la plateforme Zeotap Unity, accédez à l'application **CONNECT**.
2. Créez un segment et sélectionnez la destination Braze créée à l'étape 1.
3. Sélectionnez un identifiant de sortie pris en charge : MAID, email sha56 ou téléphone sha56. Un seul peut être utilisé pour l'intégration de Braze. Ces identifiants doivent être les mêmes que les identifiants externes définis lors de la collecte des données Braze SDK.
4. Enregistrer le segment.

!\[Segment Zeotap \]\[2\]

{% alert note %}
Les identifiants qui apparaissent sont ceux qui sont à la fois disponibles dans le segment et supportés par Braze.
{% endalert %}

### Étape 3 : Créer un segment de Braze

Après avoir créé, poussé et traité avec succès un segment dans Zeotap, les utilisateurs de Zeotap apparaîtront dans le tableau de bord Braze. Vous pouvez rechercher des utilisateurs par ID d'utilisateur dans le tableau de bord Braze.

![Profil utilisateur Zeotap[4]

Si un utilisateur fait partie du segment Zeoap, le nom du segment apparaît comme un attribut personnalisé sur leur profil utilisateur avec la valeur booléenne `true`. Prenez note du nom de l'attribut personnalisé car vous en aurez besoin lors de la création d'un segment Braze.

Ensuite, vous devez créer et définir ce segment au sein du Brésil :
1. À partir du tableau de bord de Braze, sélectionnez **Segments** puis **Créer un segment**.
2. Ensuite, nommez votre segment et sélectionnez le segment d'attribut personnalisé fait en Zeotap.
3. Enregistrez vos modifications.

!\[segment de Braze\]\[3\]

Vous pouvez maintenant ajouter ce segment nouvellement créé aux futures campagnes Braze et Canvases pour cibler ces utilisateurs finaux.
[1]: {% image_buster /assets/img/zeotap/zeotap1.png %} [2]: {% image_buster /assets/img/zeotap/zeotap2.png %} [3]: {% image_buster /assets/img/zeotap/zeotap3.png %} [4]: {% image_buster /assets/img/zeotap/zeotap4.png %}
