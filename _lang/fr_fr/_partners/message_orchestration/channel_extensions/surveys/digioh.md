---
nav_title: Digioh
article_title: Digioh
description: "Cet article de référence décrit le partenariat entre Braze et Digioh, une plateforme de sondage qui vous permet de créer facilement des fenêtres contextuelles, des formulaires, des enquêtes et des centres de préférences de communication qui suscitent un réel engagement par le biais de vos campagnes Braze."
alias: /partners/digioh/
page_type: partner
search_tag: Partner

---

# Digioh

> [Digioh](https://www.digioh.com/) vous aide à développer vos listes, à collecter des données de première partie et à les utiliser dans vos campagnes Braze.

_Cette intégration est maintenue par Digioh._

## À propos de l'intégration

L'intégration de Braze et Digioh vous permet d'utiliser leur générateur flexible par glisser-déposer pour créer des formulaires, des fenêtres contextuelles, des centres de performance, des pages de destination et des enquêtes qui vous mettent en relation avec vos clients. Digioh vous aidera à configurer l'intégration et à créer, concevoir et lancer votre première campagne pour vous.

![« Créez des centres de préférences flexibles pour les e-mails et les communications avec Digioh »][5]{: style="border:0"}

## Conditions préalables

| Condition | Description |
|---|---|
|Compte Digioh | Un [compte Digioh](https://www.digioh.com/) est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Endpoint de l'API Braze `/users/track/` | L'URL de votre endpoint REST avec les détails `/users/track/` qui y sont ajoutés. Votre endpoint dépendra de l'URL [Braze] de votre instance. ][6]<br><br>Par exemple, si votre endpoint d'API REST est `https://rest.iad-01.braze.com` votre endpoint `/users/track/` sera`https://rest.iad-01.braze.com/users/track/`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Intégration 

Pour intégrer Digioh, vous devez d'abord configurer le connecteur Braze. Cette opération terminée, vous devez ensuite appliquer l'intégration à une fenêtre modale (widget). Visitez [Digioh](https://help.digioh.com/knowledgebase/digioh-integration-basics/) pour en savoir plus sur les principes de base de l'intégration.

### Étape 1 : Créez une intégration Digioh 

Dans Digioh, cliquez sur l'onglet **Intégrations**, puis sur le bouton **Nouvelle intégration**. Sélectionnez **Braze** dans la liste déroulante **Intégration** et nommez l'intégration. 

![« Sélectionnez la bonne intégration dans la liste déroulante »][2]{: style="max-width:50%;"}

Ensuite, entrez la clé API REST Braze et l’endpoint de l'API Braze `/users/track/`. 

Enfin, utilisez la section des champs cartographiques pour mapper des champs personnalisés supplémentaires au-delà de l'e-mail et du nom. L'extrait de code suivant montre un exemple de charge utile. Lorsque vous avez terminé, sélectionnez **Créer une intégration**.

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

### Étape 2 : Créez une lightbox Digioh

Utilisez l'[éditeur de conception](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/) Digioh pour créer une fenêtre modale (widget). <br>
Vous souhaitez consulter une galerie de méthodes permettant de tirer parti de l'éditeur de conception ? Visitez la [galerie thématique](https://www.digioh.com/theme-gallery) Digioh.

### Étape 3 : Appliquer l'intégration

Pour appliquer cette intégration à une [lightbox](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/) Digioh, accédez à la page **Boxes** et sélectionnez le lien **Ajouter** ou **Modifier** dans la colonne **Intégrations**. Cela peut également être ajouté depuis la section **Intégration** de l'éditeur.

![« Ajouter l'intégration à une lightbox »][3]{: style="max-width:90%"}

Ici, sélectionnez **Ajouter une intégration**, choisissez l'intégration souhaitée et **enregistrez**. Digioh va désormais transmettre les leads que vous avez capturés à Braze en temps réel.


[2]: {% image_buster /assets/img/digioh/2.png %}
[3]: {% image_buster /assets/img/digioh/3.png %}
[4]: {% image_buster /assets/img/digioh/4.png %}
[5]: {% image_buster /assets/img/digioh/pref_pop_examples.png %}
[6]: {{site.baseurl}}/api/basics/#endpoints