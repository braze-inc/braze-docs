---
nav_title: Taxi for Email
article_title: Taxi for Email
alias: /partners/taxi_for_email
description: "Cet article de référence présente le partenariat entre Braze et Taxi for Email, un outil de marketing électronique en ligne qui permet aux clients Braze de créer des modèles d’e-mail intelligents à l’aide d’une interface glisser-déposer et d’une syntaxe simple mais puissante."
page_type: partner
search_tag: Partenaire

---

# Taxi for Email

> [Taxi for Email](http://taxiforemail.com/) est un outil de marketing par e-mail en ligne qui offre un éditeur visuel d’e-mail intuitif par glisser-déposer. Taxi encourage les équipes à collaborer facilement sur les campagnes d’e-mail, en donnant aux rédacteurs et aux éditeurs l’accès et les ressources dont ils ont besoin pour construire des e-mails, le tout sans code.

L’intégration de Braze et Taxi exploite la syntaxe simple mais puissante de Taxi pour créer et exporter des modèles d’e-mails intelligents vers Braze. 

## Conditions préalables

| Condition | Description |
| ------------| ----------- |
| Compte Taxi for Email | Un compte Taxi for Email est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations **Modèles** complètes. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint Braze | Votre [endpoint]({{site.baseurl}}/api/basics/#endpoints) Braze correspond à votre URL de Tableau de bord de Braze.<br><br> Par exemple, si votre URL de tableau de bord est `https://dashboard-03.braze.com`, votre endpoint sera `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Intégration

### Étape 1 : Créer un modèle d’e-mail Taxi

Créez un modèle Taxi sur la plateforme Taxi. Une fois créé, accédez à **Organization Settings (Paramètres de l’organisation)** et sélectionnez l’onglet **ESP Connectors (Connecteurs de fournisseur de services d’e-mail)**.

### Étape 2 : Créer un connecteur Braze

1. Dans la boîte de dialogue qui apparaît, cliquez sur le bouton **Add New (Ajouter un nouveau)** et sélectionnez **Braze** dans la liste déroulante. 
2. Cliquez sur **Braze** pour modifier les paramètres du connecteur Braze.
3. Saisissez votre endpoint Braze et votre clé d’API Braze.

Le champ de votre connecteur changera de couleur une fois que les autorisations correctes sont fournies. Si ce champ ne change pas, vérifiez que vos champs correspondent aux exigences indiquées.

## Utilisation

Vos modèles Taxi téléchargés dans votre compte Braze sont affichés dans la section **Templates & Media (Modèles et médias) > Email Templates (Modèles d’e-mail)**. Vous pouvez maintenant utiliser ce modèle d’e-mail pour commencer à envoyer des e-mails attrayants à vos clients !

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
