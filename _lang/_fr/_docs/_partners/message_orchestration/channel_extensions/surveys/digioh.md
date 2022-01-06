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

> [Digioh](https://www.digioh.com/) vous aide à agrandir vos listes, à capturer des données de premier groupe et à mettre vos données à utiliser dans vos campagnes de Braze.

L'intégration de Braze et Digioh vous permet d'utiliser leur constructeur flexible de glisser-déposer pour créer des formes sur marque, pop-ups, centres de performance, pages d'atterrissage et sondages qui vous connectent à vos clients. Digioh vous aidera à mettre en place et à aider à construire, concevoir et lancer votre première campagne pour vous.

!\["Create flexible email and communication preference centers with Digioh"\]\[5\]{: style="border:0"}

## Pré-requis

| Exigences                                      | Libellé                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte Digioh                                  | Un [compte Digioh](https://www.digioh.com/) est requis pour profiter de ce partenariat.                                                                                                                                                                                                                                                                                             |
| Braze clé API REST                             | Une clé API Braze REST avec les permissions `users.track`. <br><br> Ceci peut être créé dans le __tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__                                                                                                                                                                        |
| Braze API `/users/track/` point de terminaison | L'URL de votre point de terminaison REST avec les détails `/users/track/` y est ajoutée. Votre point de terminaison dépendra de l'URL [Braze pour votre instance][6].<br><br>Par exemple, si votre point de terminaison de l'API REST est `https://rest. ad-01.braze.com` votre point de terminaison `/users/track/` sera `https://rest.iad-01.braze.com/users/track/`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

Pour intégrer Digioh, vous devez d'abord configurer le connecteur Braze. Une fois terminé, vous devrez appliquer l'intégration à un lightbox (widget). Visitez [Digioh](https://help.digioh.com/knowledgebase/digioh-integration-basics/) pour en savoir plus sur les bases de l'intégration.

### Étape 1 : Créer une intégration Digioh

Dans Digioh, cliquez sur l'onglet **Intégrations** puis sur le bouton **Nouvelle Intégration**. Sélectionnez **Braze** dans le menu déroulant **Intégration** et nommez l'intégration.

!\["Select the correct integration from the dropdown"\]\[2\]{: style="max-width:50%;"}

Ensuite, entrez la clé de l'API Braze REST et votre point de terminaison `/users/track/`.

Enfin, utilisez la section des champs de la carte pour mapper les champs personnalisés supplémentaires au-delà de l'email et du nom. Un exemple de charge utile peut être trouvé ci-dessous. Une fois terminé, sélectionnez **Créer une intégration**.

```json
{
    "attributes" : [
         {
           "external_id": "[EMAIL_MD5]",
           "email" : "[EMAIL]"
         }
     ]

```

### Étape 2 : Créer une lightbox Digioh

Utilisez l'éditeur de design [Digioh](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/) pour construire un lightbox (widget). <br> Vous aimeriez voir une galerie de façons de tirer parti de l'éditeur de design ? Visitez la galerie de thème Digioh [](https://www.digioh.com/theme-gallery).

### Étape 3 : Appliquer l'intégration

Pour appliquer cette intégration à une lightbox Digioh [](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/), accédez à la page **Boîtes** et sélectionnez **Ajouter** ou **Modifier le lien** dans la colonne **Intégrations**. Ceci peut également être ajouté à partir de la section **Intégration** de l'éditeur.

!\["Add the integration to a lightbox"\]\[3\]{: style="max-width:90%"}

Ici, sélectionnez **Ajouter une intégration**, choisissez votre intégration souhaitée et **Enregistrer**. Digioh va maintenant passer votre capturé mène à Braze en temps réel.
[2]: {% image_buster /assets/img/digioh/2.png %} [3]: {% image_buster /assets/img/digioh/3. ng %} [4]: {% image_buster /assets/img/digioh/4.png %} [5]: {% image_buster /assets/img/digioh/pref_pop_examples.png %}

[6]: https://www.braze.com/docs/api/basics/#endpoints