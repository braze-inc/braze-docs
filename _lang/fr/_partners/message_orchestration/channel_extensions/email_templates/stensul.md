---
nav_title: Stensul
article_title: Stensul
alias: /partners/stensul
description: "Cet article de référence présente le partenariat entre Braze et Stensul, une plateforme d’e-mail d’entreprise qui vous permet de créer facilement des modèles d’e-mail répondant à des besoins mobiles sur tous les canaux."
page_type: partner
search_tag: Partenaire

---

# Stensul

> [Stensul](https://stensul.com/) permet aux spécialistes du marketing par e-mail de créer facilement des e-mails liés à la marque et réactifs sur le mobile avant de les envoyer en aval à Braze, en temps réel, pour la création de campagnes.

L’intégration de Braze et Stensul vous permet d’exporter vos e-mails Stensul au format HTML et de les télécharger comme modèles dans Braze.

## Conditions préalables

| Condition | Description |
| ------------| ----------- |
| Compte Stensul | Un compte Stensul est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations **Modèles** complètes. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Instance de cluster | Votre [instance de cluster]({{site.baseurl}}/api/basics/#endpoints) Braze correspond à votre Tableau de bord de Braze et à l’endpoint REST.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Intégration

Fournissez votre clé d’API REST Braze et votre instance de cluster à votre équipe de service de support Stensul. Une fois fournis, ils configureront l’intégration initiale pour vous.

{% alert important %}
Il s’agit d’une configuration unique et toutes les exportations à l’avenir utiliseront automatiquement cette clé d’API.
{% endalert %}

### Étape 1 : Créer un e-mail Stensul

Créez un e-mail Stensul dans la plateforme Stensul et cliquez sur **Complete (Terminer)**.

![Options d’enregistrement de Stensul]({% image_buster /assets/img_archive/stensul_save_options.png %})

### Étape 2 : Exporter le modèle vers Braze
Dans la nouvelle boîte de dialogue qui apparaît sur la page d’achèvement, sélectionnez **Upload to ESP (Télécharger vers fournisseur de services d’e-mail)**.

![Options de téléchargement de Stensul]({% image_buster /assets/img_archive/stensul_upload_options.png %})

Ensuite, entrez le **nom du modèle**, **sujet** et **l’accroche** pour votre e-mail et sélectionnez **Upload (Télécharger)**. Vous recevrez ensuite une confirmation indiquant que le téléchargement a réussi et un historique des téléchargements passés du fichier, le cas échéant.

![Téléchargement réussi dans Stensul]({% image_buster /assets/img_archive/stensul_upload_success.png %})

## Utilisation

Vos modèles Stensul téléchargés dans votre compte Braze sont affichés dans la section **Templates & Media (Modèles et médias) > Email Templates (Modèles d’e-mail)**. Vous pouvez maintenant utiliser ce modèle d’e-mail pour commencer à envoyer des e-mails attrayants à vos clients !

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
