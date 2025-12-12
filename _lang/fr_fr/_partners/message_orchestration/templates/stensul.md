---
nav_title: Stensul
article_title: Stensul
alias: /partners/stensul
description: "Cet article de référence présente le partenariat entre Braze et Stensul, une plateforme d'e-mail d'entreprise qui vous permet de créer facilement des modèles d'e-mails adaptés aux mobiles sur l'ensemble des canaux."
page_type: partner
search_tag: Partner

---

# Stensul

> [Stensul](https://stensul.com/) permet aux spécialistes du marketing par e-mail de créer facilement dans Stensul des e-mails adaptés aux appareils mobiles et à votre marque afin de les envoyer en temps réel à Braze pour créer des campagnes.

_Cette intégration est maintenue par Stensul._

## À propos de l'intégration

L'intégration entre Braze et Stensul vous permet d'exporter vos e-mails Stensul au format HTML et de les télécharger en tant que modèles dans Braze.

## Conditions préalables

| Condition | Description |
| ------------| ----------- |
| Compte Stensul | Un compte Stensul est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations complètes sur les **modèles**. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Instance de cluster | Votre [instance de cluster]({{site.baseurl}}/api/basics/#endpoints) Braze s'aligne sur votre tableau de bord de Braze et votre endpoint REST.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Intégration

Fournissez votre clé API REST Braze et votre instance de cluster à votre équipe de satisfaction client Stensul. L'équipe mettra ensuite en place l'intégration initiale pour vous.

{% alert important %}
Il s'agit d'une configuration unique et toutes les exportations futures utiliseront automatiquement cette clé API.
{% endalert %}

### Étape 1 : Créer un e-mail Stensul

Créez un e-mail Stensul dans la plateforme Stensul et cliquez sur **Terminer**.

![Options d’enregistrement Stensul]({% image_buster /assets/img_archive/stensul_save_options.png %})

### Étape 2 : Exporter le modèle vers Braze
Dans la nouvelle boîte de dialogue qui s'affiche sur la page d'achèvement, sélectionnez **Télécharger vers ESP**.

![Options de chargement Stensul]({% image_buster /assets/img_archive/stensul_upload_options.png %})

Saisissez ensuite le **nom du modèle**, l'**objet** et l'**accroche** de votre e-mail, puis sélectionnez **Charger**. Vous recevrez alors une confirmation que le téléchargement a réussi et un historique des téléchargements précédents du fichier, le cas échéant.

![Succès de chargement Stensul]({% image_buster /assets/img_archive/stensul_upload_success.png %})

## Utilisation

Retrouvez votre modèle Stensul téléchargé dans la section **Modèles et médias > Modèles d'e-mail de** votre compte Braze. Vous pouvez maintenant utiliser ce modèle d'e-mail pour commencer à envoyer des messages engageants à vos clients !


