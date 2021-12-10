---
nav_title: Digioh
article_title: Digioh
page_order: 1
description: "Digioh vous permet de créer facilement des pop-ups, des formulaires, des sondages et des centres de préférences de communication qui favorisent un réel engagement à travers vos campagnes Braze."
alias: /fr/partners/digioh/
page_type: partenaire
search_tag: Partenaire
---

# Digioh

> [Digioh](https://www.digioh.com/) vous aide à agrandir vos listes, à capturer des données de premier groupe et à mettre vos données à utiliser dans vos campagnes de Braze. Le constructeur de glisser-déposer facilite la création de formulaires de marque, de pop-ups, de centres de préférences, de pages d'atterrissage et d'enquêtes qui vous connectent à vos clients. La configuration de l’intégration est incluse dans chaque paquet, et Digioh aidera également à construire, concevoir et lancer votre première campagne pour vous.

!\["Create flexible email and communication preference centers with Digioh"\]\[5\]{: style="border:0"}

## Exigences

| Exigences                       | Origine | Accès                                                                                                                                                                                                        | Libellé                                                                                  |
| ------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| Clé API Braze                   | Brasero | Vous devrez créer une nouvelle clé d'API.<br><br>Ceci peut être créé dans la __Console Développeur -> Paramètres API -> Créer une nouvelle clé API__ avec __utilisateurs. permissions__ de rack. | Vous devrez copier cette clé sur votre compte Digioh - voir les instructions ci-dessous. |
| Point de terminaison REST Braze | Brasero | Vous aurez besoin du point de terminaison du serveur que votre compte utilise pour accéder à l'API de Braze. [Voir la documentation API de Braze pour plus de détails][6].                                   | Vous devrez copier cette URL sur votre compte Digioh - voir les instructions ci-dessous. |
| Compte Digioh                   | Digioh  | [https://www.digioh.com/](https://www.digioh.com/)                                                                                                                                                           | Vous devrez avoir un compte Digioh.                                                      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Détails de l'intégration

### Étape 1 : Créer une intégration Digioh

Dans la plate-forme Digioh, cliquez sur l'onglet **Intégrations** et créez le bouton **+ Nouvelle Intégration**.

Ensuite, sélectionnez **Braze** dans la liste déroulante **Intégration** et nommez l'intégration. Entrez la **clé API Braze** et **Braze REST Endpoint** de votre compte Braze dans les champs fournis. Cliquez sur **Créer une intégration**.

!\["Select the correct integration from the dropdown"\]\[2\]{: style="max-width:50%;"}

### Étape 2 : Mapper des champs supplémentaires

Sur la page **Intégrations** , utilisez le lien **Champs de la carte** pour mapper les champs supplémentaires au-delà de l'e-mail et du nom.

### Étape 3 : Appliquer l'intégration

Pour appliquer l'intégration à un [lightbox](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/), utilisez le lien **Ajouter** ou **Modifier** dans la colonne **Intégrations** de la page **Boîtes**.

!\["Add the integration to a box"\]\[3\]{: style="max-width:80%"}

Vous pouvez également l'ajouter à partir de la section **Intégration** de l'éditeur.

!\["Add the integration to a box in the editor"\]\[4\]{: style="max-width:30%"}

C'est tout ce qu'il y a à faire! Digioh va maintenant passer votre capturé mène à Braze en temps réel.
[2]: {% image_buster /assets/img/digioh/2.png %} [3]: {% image_buster /assets/img/digioh/3. ng %} [4]: {% image_buster /assets/img/digioh/4.png %} [5]: {% image_buster /assets/img/digioh/pref_pop_examples.png %}

[6]: https://www.braze.com/docs/api/basics/#endpoints