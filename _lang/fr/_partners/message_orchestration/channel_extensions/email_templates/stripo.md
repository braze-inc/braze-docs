---
nav_title: Stripo
article_title: Stripo
alias: /partners/stripo
description: "Cet article de référence présente le partenariat entre Braze et Stripo, un modèle d’e-mail glisser-déposer qui vous permet de créer facilement des e-mails sophistiqués avec des éléments interactifs."
page_type: partner
search_tag: Partenaire

---

# Stripo

> [Stripo](https://stripo.email/) est un créateur de modèles d’e-mails par glisser-déposer qui vous aide à créer et à concevoir des e-mails réactifs avec des éléments interactifs. Les utilisateurs de Stripo peuvent également éditer en HTML et décider des éléments à afficher ou à masquer sur les différents appareils grâce à l’éditeur de Stripo.

L’intégration de Braze et Stripo vous permet d’exporter vos e-mails Stripo personnalisés et de les télécharger comme modèles dans Braze.

## Conditions préalables

| Condition | Description |
| ------------| ----------- |
| Compte Stripo | Un compte Stripo est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations **Modèles** complètes. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Instance de cluster | Votre [instance de cluster]({{site.baseurl}}/api/basics/#endpoints) Braze correspond à votre Tableau de bord de Braze et à l’endpoint REST.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Intégration

### Étape 1 : Créer un e-mail Stripo

Créez un e-mail Stripo dans la plateforme Stripo et cliquez sur **Export (Exporter)**. 

![Exportation de Stripo]({% image_buster /assets/img_archive/stripo_export.png %})

### Étape 2 : Exporter le modèle vers Braze

Dans la boîte de dialogue qui apparaît, sélectionnez **Braze** comme méthode d’exportation 

Ensuite, saisissez votre **nom de compte** (c.-à-d. le nom du groupe d’apps), votre **clé d’API** et votre **instance de cluster**.

![Formulaire Stripo]({% image_buster /assets/img_archive/stripo_form.png %})

{% alert important %}
Il s’agit d’une configuration unique et toutes les exportations à l’avenir utiliseront automatiquement cette clé d’API.
{% endalert %}

## Utilisation

Vos modèles Stripo téléchargés dans votre compte Braze sont affichés dans la section **Templates & Media (Modèles et médias) > Email Templates (Modèles d’e-mail)**. Vous pouvez maintenant utiliser ce modèle d’e-mail pour commencer à envoyer des e-mails attrayants à vos clients !

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
