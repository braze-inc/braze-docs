---
nav_title: Ada
article_title: Ada
description: "Cet article de référence présente le partenariat entre Braze et Ada, une plateforme alimentée par l'intelligence artificielle qui automatise et personnalise les interactions avec les clients. Cette intégration vous permet d'enrichir les profils utilisateurs avec des données collectées à partir de vos conversations Ada automatisées."
alias: /partners/ada/
page_type: partner
search_tag: Partner

---

# Ada

> [Ada](https://ada.cx) est une plateforme d'interaction avec les marques qui automatise et personnalise l'expérience client grâce à l'intelligence artificielle conversationnelle. Utilisez Ada pour adapter votre envoi de messages et segmenter vos campagnes en fonction des données des utilisateurs, mesurez et analysez les conversations pour découvrir de nouvelles opportunités, et utilisez les informations issues du chat avec les clients pour enrichir vos profils utilisateurs.  

L'intégration de Braze et d'Ada vous permet d'enrichir les profils utilisateurs avec les données collectées lors de vos conversations Ada automatisées. Vous pouvez définir des attributs utilisateurs personnalisés en fonction des informations que vous collectez au cours d'une conversion Ada et enregistrer des événements personnalisés dans Braze à des moments précis d'une conversation Ada. En connectant votre chatbot Ada à Braze, vous pouvez en apprendre davantage sur vos consommateurs en fonction des questions qu'ils posent sur votre marque ou en entamant proactivement des conversations avec eux, en leur posant des questions qui vous permettent d'en savoir plus sur leurs intérêts et leurs préférences.

## Prérequis

| Condition | Descriptif |
| ----------- | ----------- |
| Compte Ada | Un compte [Ada](https://ada.cx) avec les applications Braze et Answer Utilities activées est nécessaire pour profiter de ce partenariat. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.][1] Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

Les cas d'utilisation courants de l'intégration de Braze et d'Ada sont les suivants :
- Le suivi des différentes interactions de vos consommateurs avec votre bot Ada en tant qu'événements personnalisés dans Braze, afin que vous sachiez quels clients se sont engagés avec des campagnes proactives dans Ada, ont été confiés à des agents d'assistance, ont posé des questions spécifiques ou ont effectué certaines actions.
- Interroger vos consommateurs sur leurs centres d'intérêt, leurs préférences, leurs caractéristiques démographiques, etc. Mettez automatiquement à jour leur profil dans Braze avec ces nouvelles informations à l'aide d'attributs personnalisés.

## Intégration

Pour intégrer Braze et Ada, vous devez commencer par configurer l'application Braze dans votre tableau de bord Ada et collaborer avec votre équipe Ada pour configurer une métavariable d’ID utilisateur dans votre script d'intégration Ada. Ensuite, il vous faudra faire glisser le bloc Braze dans l'éditeur de réponse à l'endroit où vous souhaitez renvoyer des informations à Braze, qu'il s'agisse d'un événement ou d'un attribut.

### Étape 1 : Configurez l'application Braze dans Ada

Dans le tableau de bord Ada, allez dans **Paramètres > Intégrations > Intégrations de transfert.**

En regard de Braze, cliquez sur **Connecter** et fournissez les informations suivantes :
- **Endpoint REST**: saisissez l'URL de votre endpoint REST Braze. 
- **Clé API**: saisissez votre clé API REST de Braze. 
- **ID d’application** : saisissez l'ID de l'application à laquelle vous souhaitez associer les agents conversationnels Ada.

### Étape 2 : Passage d'un identifiant de Braze à Ada

Pour confirmer que vous mettez à jour le bon utilisateur, vous devrez contacter votre équipe Ada qui pourra vous aider à apporter les modifications nécessaires au script d'intégration Ada pour recevoir un identifiant de Braze. Cette intégration est conçue pour accepter un ID externe, mais il est possible de transmettre d'autres identifiants, comme un alias d'utilisateur. 

### Étape 3 : Déposez le bloc Braze dans les réponses correspondantes de Braze

Pour utiliser le bloc Braze, faites-le glisser du tiroir de blocs vers la réponse appropriée et sélectionnez une action. Le bloc Braze vous permet d’effectuer deux actions :
* Suivre l’événement
* Mettre à jour l'attribut

{% tabs local %}
{% tab suivre l’événement %}

#### Bloc d’utilitaires de réponse

1. Faites glisser le bloc Answer Utilities du tiroir de blocs pour le placer directement au-dessus de votre bloc Braze. 
2. Sélectionnez l'action **Formater la date** et entrez `today` dans le champ **Date**.
3. Saisissez `iso` dans le champ **Format de sortie.**  Sous **Enregistrer la réponse comme variable**, créez une variable pour la **date formatée** appelée `iso_time`.

![Le bloc d’utilitaires de réponse dont les champs ont été renseignés comme décrit dans le texte précédent.]({% image_buster /assets/img/ada/ada-braze-2.png %})

#### Bloc Braze

**4\.** Dans le bloc Braze, saisissez dans le champ **ID externe** la métavariable `external_id` définie par Ada à l'étape précédente.<br>
**5\.** Dans le champ **Nom de l'événement**, saisissez le nom de l'événement de Braze que vous souhaitez suivre.<br>
**6\.** Dans le champ **Heure de l'événement**, entrez la variable `iso_time` que vous avez créée dans le bloc d’utilitaires de réponse.<br>
**7\.** Sélectionnez une réponse de repli à faire apparaître si un problème survient lors de la publication de l'événement sur Braze.

![Le bloc Braze avec les champs remplis comme décrit dans le texte précédent.]({% image_buster /assets/img/ada/ada-braze-3.png %})

{% endtab %}
{% tab mettre à jour l’attribut %}

#### Bloc Braze

1. Dans le bloc Braze, saisissez dans le champ **ID externe** la métavariable ** définie par Ada à l'étape précédente. 
2. Dans le champ **Nom de l'attribut**, saisissez le nom de l'attribut Braze que vous souhaitez suivre. 
3. Dans le champ **Valeur de l'attribut**, saisissez la valeur que vous souhaitez définir, qui peut être du texte, une variable ou une combinaison de texte et de variables. 
4. Sélectionnez une réponse par défaut devant apparaître en cas de problème lors du transfert de l'attribut à Braze.

![Le bloc Braze avec les champs remplis comme décrit dans le texte précédent.]({% image_buster /assets/img/ada/ada-braze-4.png %})

{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/ada/ada-braze-1.png %}
[3]: {% image_buster /assets/img/ada/ada-braze-2.png %}
[4]: {% image_buster /assets/img/ada/ada-braze-3.png %}
[5]: {% image_buster /assets/img/ada/ada-braze-4.png %}