---
nav_title: Ada
article_title: Ada
description: "Cet article de référence décrit le partenariat entre Braze et Ada, une plateforme alimentée par l'IA qui automatise et personnalise les interactions avec les clients. Cette intégration vous permet d'augmenter les profils d'utilisateurs avec les données collectées à partir de vos conversations automatisées Ada."
alias: /partners/ada/
page_type: partner
search_tag: Partenaire

---

# Ada

> [Ada](https://ada.cx) est une plateforme d'interaction qui automatise et personnalise l'expérience client à l'aide de l'IA conversationnelle. Utilisez Ada pour personnaliser vos campagnes de communication et de segmentation en fonction des données des utilisateurs, mesurer et analyser les conversations pour découvrir de nouvelles opportunités et utiliser les insights issus des discussions avec les clients pour enrichir vos profils d'utilisateurs.  

Les intégrations Braze et Ada vous permettent d'augmenter les profils d'utilisateurs avec les données collectées à partir de vos conversations automatisées Ada. Vous pouvez définir des attributs utilisateur personnalisés en fonction des informations que vous collectez lors d'un chat Ada et enregistrer des événements personnalisés dans Braze à des moments spécifiés d'une conversation Ada. En connectant votre chatbot Ada à Braze, vous pouvez en savoir plus sur vos consommateurs en fonction des questions qu'ils posent sur votre marque ou en entamant de manière proactive des conversations avec eux avec des questions qui vous permettent d'en savoir plus sur leurs intérêts et leurs préférences.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Ada | Il vous faut un compte [Ada](https://ada.cx) avec les applications Braze et Answer Utilities activées pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze | [URL de votre endpoint REST][1]. Votre endpoint dépendra de l’URL Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d’utilisation

Les cas d'utilisation courants pour l'intégration Braze et Ada incluent :
- Suivre les différentes interactions que vos consommateurs ont avec votre bot Ada en tant qu'événements personnalisés dans Braze, afin que vous sachiez quels clients se sont engagés dans des campagnes proactives dans Ada, ont été dirigés vers des assistants, ont posé des questions spécifiques ou ont effectué certaines actions.
- Demandez à vos consommateurs quels sont leurs centres d'intérêt, leurs préférences, leurs données démographiques, etc. Mettez à jour leur profil dans Braze automatiquement avec ces nouvelles informations à l'aide d'attributs personnalisés.

## Intégration

Pour intégrer Braze et Ada, vous devez d'abord configurer l'application Braze dans votre tableau de bord Ada et travailler avec votre équipe Ada pour configurer une métavariable d'ID utilisateur dans votre script d'intégration Ada. Ensuite, vous ferez glisser le bloc Braze dans l'éditeur de réponses là où vous souhaitez renvoyer des informations à Braze - soit un événement, soit un attribut.

### Étape 1 : Configurer l'application Braze dans Ada

Sur le tableau de bord Ada, accédez à **Settings > Integrations > Handoff Integrations (Paramètres > Intégrations > Intégrations Handoff)**.

À côté de Braze, cliquez sur **Connect (Connecter)** et fournissez les informations suivantes :
- **Endpoint REST** : saisissez l'URL de votre endpoint Braze REST. 
- **Clé API** : entrez votre clé API REST Braze. 
- **ID de l'application** : entrez l'ID de l'application à laquelle vous souhaitez associer les chatteurs Ada.

### Étape 2 : Faire transiter un identifiant de Braze à Ada

Pour vous assurer que vous mettez à jour le bon utilisateur, vous devrez contacter votre équipe Ada pour qu’ils vous aident à apporter les modifications nécessaires au script d'intégration Ada pour recevoir un identifiant Braze. Cette intégration est conçue pour accepter un ID externe, mais il est possible de transmettre d'autres identifiants, comme un alias d'utilisateur. 

### Étape 3 : Posez le bloc Braze dans les réponses pertinentes

Pour utiliser le bloc Braze, faites-le glisser à partir du tiroir de blocs vers la réponse appropriée et sélectionnez une action. Avec le bloc Braze, vous pouvez effectuer deux actions :
* Suivre un événement
* Mettre à jour un attribut

{% tabs local %}
{% tab track event %}

#### Bloc Answer Utilities

1. Faites glisser le bloc Answer Utilities du tiroir de blocs et le positionner directement au-dessus de votre bloc Braze. 
2. Sélectionnez l'action **Format Date (Formater la date)** et saisissez `today` dans le champ **Date**.
3. Saisissez `iso` dans le champ **Output Format (Format de sortie)**. Sous **Save Response As Variable (Enregistrer la réponse en tant que variable)**, créez une variable pour **Formatted Date (Date formatée)** appelée `iso_time`.

![Le bloc Answer Utilities avec des champs remplis comme décrit dans le texte précédent.]({% image_buster /assets/img/ada/ada-braze-2.png %})

#### Bloc Braze

**4.** Dans le bloc Braze, entrez la métavariable `external_id` configurée par Ada à l'étape précédente dans le champ **External ID (ID externe)**.<br>
**5.** Dans le champ **Event Name (Nom de l'événement)**, entrez le nom de l'événement Braze que vous souhaitez suivre.<br>
**6.** Dans le champ **Time of Event (Heure de l'événement)**, saisissez la variable `iso_time` que vous avez créée dans le bloc Answer Utilities.<br>
**7.** Sélectionnez une réponse de repli à faire remonter si un problème survient lors de la publication de l'événement sur Braze.

![Le bloc Braze avec des champs remplis comme décrit dans le texte précédent.]({% image_buster /assets/img/ada/ada-braze-3.png %})

{% endtab %}
{% tab update attribute %}

#### Bloc Braze

1. Dans le bloc Braze, entrez la métavariable `external_id` configurée par Ada à l'étape précédente dans le champ **External ID (ID externe)**. 
2. Dans le champ **Attribut Name (Nom de l'attribut)**, entrez le nom de l'attribut Braze que vous souhaitez suivre. 
3. Dans le champ **Attribute Value (Valeur d'attribut)**, entrez la valeur que vous souhaitez définir, qui peut être du texte, une variable ou une combinaison de texte et de variables. 
4. Sélectionnez une réponse de repli à faire remonter si un problème survient lors de la publication de l'attribut sur Braze.

![Le bloc Braze avec des champs remplis comme décrit dans le texte précédent.]({% image_buster /assets/img/ada/ada-braze-4.png %})

{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/ada/ada-braze-1.png %}
[3]: {% image_buster /assets/img/ada/ada-braze-2.png %}
[4]: {% image_buster /assets/img/ada/ada-braze-3.png %}
[5]: {% image_buster /assets/img/ada/ada-braze-4.png %}