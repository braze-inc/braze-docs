---
nav_title: Taxi for email
article_title: Taxi for email
alias: /partners/taxi_for_email
description: "Cet article de référence décrit le partenariat entre Braze et Taxi for email, un outil de marketing par e-mail en ligne qui permet aux clients de Braze de créer des modèles d'e-mail intelligents en utilisant leur interface de glisser-déposer et une syntaxe simple mais puissante."
page_type: partner
search_tag: Partner

---

# Taxi for email

> [Taxi for email](http://taxiforemail.com/) est un outil de marketing par e-mail en ligne qui offre un éditeur d'e-mails visuel intuitif par glisser-déposer. Taxi encourage les teams à collaborer facilement sur des campagnes d'e-mail, permettant aux rédacteurs et éditeurs d'avoir l'accès et les ressources dont ils ont besoin pour créer des e-mails, le tout sans code.

_Cette intégration est assurée par Taxi for email._

## À propos de l'intégration

L'intégration de Braze et Taxi exploite la syntaxe simple mais puissante de Taxi pour créer et exporter des modèles d'e-mail intelligents vers Braze. 

## Conditions préalables

| Condition | Description |
| ------------| ----------- |
| Compte Taxi for email | Un compte Taxi for email est requis pour profiter de ce partenariat. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations complètes sur les **modèles**. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| endpoint Braze | [Votre endpoint Braze]({{site.baseurl}}/api/basics/#endpoints) s'aligne avec l'URL de votre tableau de bord de Braze.<br><br> Par exemple, si l'URL de votre tableau de bord est `https://dashboard-03.braze.com`, votre endpoint sera `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Intégration

### Étape 1 : Créer un modèle d'e-mail de taxi

Créer un modèle de Taxi sur la plateforme Taxi. Après la création du modèle, accédez à vos **Paramètres de l'organisation** et sélectionnez l'onglet **Connecteurs ESP**.

### Étape 2 : Créer un connecteur Braze

1. Dans la boîte de dialogue qui s'affiche, cliquez sur le bouton **Ajouter un nouveau**, puis sélectionnez **Braze** dans la liste déroulante. 
2. Sélectionnez **Braze** pour modifier les paramètres du connecteur Braze.
3. Entrez votre endpoint Braze et votre clé API Braze.

Votre champ de connecteur changera de couleur après que les détails avec les autorisations correctes auront été fournis. Si ce champ ne change pas, vérifiez que vos champs sont alignés avec les exigences énumérées.

## Utilisation

Trouvez votre modèle Taxi téléchargé dans la section **modèles et médias > modèles d'e-mail** de votre compte Braze. Vous pouvez maintenant utiliser ce modèle d'e-mail pour commencer à envoyer des messages d'e-mail engageants à vos clients !


