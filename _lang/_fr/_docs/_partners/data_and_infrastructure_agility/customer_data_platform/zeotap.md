---
nav_title: Zéotap
description: "Cet article décrit le partenariat entre Braze et Zeotap, une plate-forme de données clients de nouvelle génération offrant une résolution d’identité, des idées et un enrichissement."
alias: /fr/partners/zeotap/
page_type: partenaire
search_tag: Partenaire
---

# Zéotap

> [Zeotap](https://zeotap.com/) est une plateforme de données client de nouvelle génération qui vous aide à découvrir et à comprendre votre audience mobile en fournissant une résolution d'identité. les idées et l'enrichissement des données.

Avec l'intégration de Zeotap et Braze, vous pouvez étendre l'échelle et la portée de vos campagnes en synchronisant les segments de clients de Zeotap pour associer les données utilisateur à Braze. Vous pouvez ensuite agir sur ces données, en fournissant des expériences ciblées personnalisées à vos utilisateurs.

## Pré-requis

| Exigences                                      | Origine | Accès                                                                                                                                                                                                        | Libellé                                                                                                               |
| ---------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| Clé API Braze                                  | Brasero | Vous devrez créer une nouvelle clé d'API.<br><br>Ceci peut être créé dans la __Console Développeur -> Paramètres API -> Créer une nouvelle clé API__ avec __utilisateurs. permissions__ de rack. | La clé d'API Braze sera utilisée dans les appels à l'API aux URL de Braze REST Endpoint pour authentifier le service. |
| Point de terminaison REST Braze                | Brasero | \[Liste de points d'extrémité REST\]\[1\]                                                                                                                                                                    | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL de Braze pour votre instance.             |
| ---                                            | ---     | ---                                                                                                                                                                                                          | ---                                                                                                                   |
| Zeotap Informations sur le compte et le compte | Zéotap  | [Zéotap](https://zeotap.com/)                                                                                                                                                                                | Vous devez avoir un compte Zeotap actif pour utiliser leurs services avec Braze.                                      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Intégration de Braze et Zeotap

### Étape 1 : Créer une destination Zeotap pour Braze

1. Depuis la plateforme Zeotap Unity, accédez à l'application __DESTINATIONS__.
2. Sous __Tous les canaux__, recherchez Braze.
3. Sélectionnez Braze et dans l'invite qui apparaît, entrez le nom de destination, le nom du client et la clé API associée à votre compte Braze.
4. Sélectionnez l’instance de terminaison Braze REST et enregistrez la destination. <br><br>!\[Zeotap Braze destination\]\[1\]

### Étape 2 : Créer et lier un segment de Zeotap à votre destination

1. Depuis la plateforme Zeotap Unity, accédez à l'application __CONNECT__.
2. Créez un segment et poussez-le vers Braze.
3. Sélectionnez l'identifiant de sortie associé.<br><br>Les identifiants de sortie pris en charge pour cette intégration incluent MAID, l'e-mail sha56 et le téléphone sha56.<br><br>Un seul de ces identifiants peut être utilisé pour l'intégration de Braze. Ces identifiants doivent être les mêmes que les identifiants externes définis lors de la collecte de données en utilisant le Braze SDK.
4. Cliquez sur __Oui__ pour activer le segment.

!\[Segment Zeotap \]\[2\]

{% alert note %}
Les identifiants qui apparaissent dans la fenêtre sont ceux qui sont à la fois disponibles dans le segment et supportés par Braze.
{% endalert %}

### Étape 3 : Créer un segment de Braze

Après avoir créé, poussé et traité avec succès un segment dans Zeotap, les utilisateurs de Zeotap apparaîtront dans le tableau de bord Braze. Vous pouvez rechercher des utilisateurs par ID d'utilisateur dans le tableau de bord Braze.

![Profil utilisateur Zeotap[4]

Si un utilisateur fait partie du segment Zeoap, le nom du segment apparaît comme un attribut personnalisé sur leur profil utilisateur avec la valeur booléenne `true`. Prenez note du nom de l'attribut client car vous en aurez besoin lors de la création d'un segment Braze.

Ensuite, vous devez créer et définir ce segment dans Braze en effectuant les étapes suivantes :
1. À partir du tableau de bord de Braze, sélectionnez __Segments__ puis __Créer un segment__.
2. Ensuite, nommez votre segment et sélectionnez le segment d'attribut personnalisé qui a été fait en Zeotap.
3. Enregistrez vos modifications.

!\[segment de Braze\]\[3\]

Vous pouvez ajouter ce segment nouvellement créé aux futures campagnes Braze et Canvases pour cibler ces utilisateurs finaux.
[1]: {% image_buster /assets/img/zeotap/zeotap1.png %} [2]: {% image_buster /assets/img/zeotap/zeotap2.png %} [3]: {% image_buster /assets/img/zeotap/zeotap3.png %} [4]: {% image_buster /assets/img/zeotap/zeotap4.png %}