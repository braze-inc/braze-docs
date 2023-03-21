---
nav_title: Digioh
article_title: Digioh
page_order: 1
description: "Cet article de référence décrit le partenariat entre Braze et Digioh, une plateforme d’enquêtes qui vous permet de créer facilement des fenêtres contextuelles, des formulaires, des enquêtes et des centres de préférences de communication qui favorisent l’engagement réel dans vos campagnes de Braze."
alias: /partners/digioh/
page_type: partner
search_tag: Partenaire

---

# Digioh

> [Digioh](https://www.digioh.com/) vous aide à développer vos listes, à capturer des données first-party et à utiliser vos données dans vos campagnes Braze.

L’intégration de Braze et Digioh vous permet d’utiliser leur générateur flexible glisser-déposer pour créer des formulaires sur place, des fenêtres contextuelles, des centres de performance, des pages d’accueil et des enquêtes qui vous connectent avec vos clients. Digioh facilite l’intégration et vous aidera à construire, concevoir et lancer votre première campagne.

![« Créez des centres de préférences d’e-mail et de communications flexibles avec Digioh »][5]{: style="border:0"}

## Conditions préalables

| Condition | Description |
|---|---|
|Compte Digioh | Un [compte Digioh](https://www.digioh.com/) est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint `/users/track/` de l’API Braze | URL de votre endpoint REST avec les détails `/users/track/` ajoutés à ce dernier. Votre endpoint dépendra de l’[URL Braze pour votre instance][6].<br><br>Par exemple, si votre endpoint d’API REST est `https://rest.iad-01.braze.com` votre endpoint `/users/track/` sera `https://rest.iad-01.braze.com/users/track/`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration 

Pour intégrer Digioh, vous devez d’abord configurer le connecteur Braze. Une fois terminé, vous devrez appliquer l’intégration à une lightbox (gadget). Visitez [Digioh](https://help.digioh.com/knowledgebase/digioh-integration-basics/) pour en savoir plus sur les bases de l’intégration.

### Étape 1 : Créer une intégration Digioh 

Dans Digioh, cliquez sur l’onglet **Integrations (Intégrations)** puis sur le bouton **New Integration (Nouvelle intégration)**. Sélectionnez **Braze** dans la liste déroulante **Integration (Intégration)** et nommez l’intégration. 

![« Sélectionnez l’intégration correcte dans le menu déroulant »][2]{: style="max-width:50%;"}

Ensuite, entrez la clé d’API REST de Braze et votre endpoint `/users/track/` d’API Braze. 

Enfin, utilisez la section des champs de mappage pour mapper des champs personnalisés supplémentaires au-delà de l’e-mail et du nom. L’extrait de code suivant montre un exemple de charge utile. Une fois terminé, sélectionnez **Create Integration (Créer une intégration)**.

```json
{
    "attributes" : [
         {
           "external_id": "[EMAIL_MD5]",
           "email" : "[EMAIL]"
         }
     ]
}
```

### Étape 2 : Créer une lightbox Digioh

Utiliser l’[éditeur de conception](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/) de Digioh pour créer une lightbox (gadget). <br>
Vous souhaitez voir une galerie de méthodes d’exploiter l’éditeur de conception ? Visitez la [galerie des thèmes](https://www.digioh.com/theme-gallery) de Digioh.

### Étape 3 : Appliquer l’intégration

Pour appliquer cette intégration à une [lightbox](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/) Digioh, accédez à la page **Boxes (Boîtes)** et sélectionnez le lien **Add (Ajouter)** ou **Edit (Modifier)** dans la colonne **Integrations (Intégrations)**. Cela peut également être ajouté à partir de la section **Integration (Intégration)** de l’éditeur.

![« Ajoutez l’intégration à une lightbox »][3]{: style="max-width:90%"}

Ici, sélectionnez **Add Integration (Ajouter l’intégration)**, choisissez l’intégration souhaitée et cliquez sur **Save (Enregistrer)**. Digioh va maintenant passer vos leads capturés à Braze en temps réel.

[2]: {% image_buster /assets/img/digioh/2.png %}
[3]: {% image_buster /assets/img/digioh/3.png %}
[4]: {% image_buster /assets/img/digioh/4.png %}
[5]: {% image_buster /assets/img/digioh/pref_pop_examples.png %}
[6]: {{site.baseurl}}/api/basics/#endpoints