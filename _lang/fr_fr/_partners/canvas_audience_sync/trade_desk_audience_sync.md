---
nav_title: The Trade Desk
article_title: Audience Sync Canvas vers The Trade Desk
description: "Cet article de référence explique comment utiliser Braze Audience Sync avec The Trade Desk pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore."
alias: /trade_desk_audience_sync/
Tool:
  - Canvas
page_order: 7
---

# Audience Sync vers The Trade Desk

> Grâce à Braze Audience Sync vers The Trade Desk, vous pouvez synchroniser dynamiquement vos données first-party utilisateur depuis Braze directement vers The Trade Desk pour le reciblage publicitaire, la modélisation de profils similaires et la suppression d'audiences.

**Cas d'utilisation courants de la synchronisation d'audiences :**

- Recibler vos utilisateurs existants sur The Trade Desk avec des campagnes personnalisées.
- Envoyer des données first-party à The Trade Desk pour le ciblage par exclusion.
- Synchroniser des utilisateurs vers des audiences nouvelles ou existantes, ou des segments de données CRM.

## Conditions préalables

Assurez-vous que les éléments suivants sont créés, complétés ou acceptés avant de configurer l'étape Audience Sync avec The Trade Desk dans Canvas.

| Condition | Origine | Description |
| --- | --- | --- |
| Jeton API | [The Trade Desk](https://partner.thetradedesk.com/v3/portal/api/doc/Authentication#ui-method-create) | Un jeton API standard créé dans la plateforme The Trade Desk. Nous recommandons de définir la durée de vie du jeton API à un an maximum afin de minimiser les interruptions de vos Canvas avec The Trade Desk Audience Sync. |
| Conditions et politiques de The Trade Desk | The Trade Desk | Vous devez accepter une politique de participation UID2/CRM avant de pouvoir envoyer des données à The Trade Desk. Contactez votre conseiller chez The Trade Desk pour confirmer que vous disposez de la signature appropriée pour activer la transmission de données vers The Trade Desk.<br><br> {::nomarkdown}<ul><li>Confirmez que l'accès à la gestion des données CRM est activé sur votre compte&#8212;votre conseiller chez The Trade Desk peut vous aider. Vous devez disposer de votre identifiant annonceur.</li><li>Préparez votre jeton API standard. Vous pouvez suivre les instructions de cette page pour en générer un.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Intégration

### Étape 1 : Connecter le compte The Trade Desk

Pour commencer, accédez à **Partner Integrations** > **Technology Partners** > **The Trade Desk**. Fournissez les informations suivantes depuis votre compte Trade Desk :

- **Jeton API**
- **Nom de l'identifiant annonceur** (ce nom facultatif identifie le compte annonceur à référencer dans l'étape Audience Sync du canvas)
- **Identifiant annonceur**

Puis sélectionnez **Connect**.

![Exemple d'un Audience Sync non connecté pour The Trade Desk.]({% image_buster /assets/img/audience_sync/trade_desk/connect_sync.png %}){: style="max-width:90%;"}

### Étape 2 : Ajouter une étape Audience Sync avec The Trade Desk

Ajoutez un composant dans votre canvas et sélectionnez **Audience Sync**. Puis sélectionnez **The Trade Desk** comme partenaire Audience Sync.

![Option de sélection du partenaire pour la synchronisation avec l'étape Audience Sync.]({% image_buster /assets/img/audience_sync/trade_desk/audience_sync_step.png %}){: style="max-width:90%;"}

### Étape 3 : Configurer votre synchronisation

Ensuite, configurez les détails de votre synchronisation :

1. Sélectionnez un compte publicitaire.
2. Choisissez une audience existante ou créez-en une nouvelle.

![Configuration d'Audience Sync avec un champ d'audience contenant le nom « valentines2025 ».]({% image_buster /assets/img/audience_sync/trade_desk/choose_audience.png %}){: style="max-width:90%;"}

{: start="3"}
3. Sélectionnez une action : **Add Users to Audience** ou **Remove Users from Audience**.

![Configuration d'Audience Sync pour ajouter des utilisateurs à une audience.]({% image_buster /assets/img/audience_sync/trade_desk/audience_sync_step2.png %}){: style="max-width:90%;"}

{: start="4"}
4. Choisissez l'un des champs suivants pour la correspondance : **Email**, **Phone** ou **Mobile Advertiser ID**.

{% alert note %}
Si vous synchronisez vers une audience dans The Trade Desk avec une région définie sur l'UE, le numéro de téléphone n'est pas pris en charge par The Trade Desk. Contactez The Trade Desk pour obtenir de l'assistance concernant les numéros de téléphone dans la région UE.
{% endalert %}

### Étape 4 : Lancer votre canvas

Après avoir configuré votre Audience Sync vers The Trade Desk, vous êtes prêt à lancer le canvas ! La nouvelle audience est créée, et les utilisateurs qui passent par l'étape Audience Sync sont ajoutés à cette audience sur The Trade Desk. Si votre canvas contient des composants ultérieurs, vos utilisateurs progressent vers l'étape suivante de leur parcours utilisateur.

## Questions fréquentes

### Combien de temps faut-il pour que les tailles d'audience soient renseignées dans The Trade Desk ?

Cela peut prendre jusqu'à 24 heures.

### Quelle est la taille minimale d'audience pour que The Trade Desk la renseigne dans votre compte publicitaire ?

Il n'y a pas de taille minimale d'audience pour les audiences CRM dans The Trade Desk.

### Comment savoir si des utilisateurs ont été mis en correspondance après leur envoi à The Trade Desk ?

Dans The Trade Desk, les ID reçus s'affichent à côté du segment.

- Les ID reçus correspondent au nombre d'ID reçus au cours des 30 derniers jours.
- Les ID actifs correspondent au nombre d'ID détectés dans les enchères au cours des sept derniers jours.

### Combien d'audiences The Trade Desk peut-il prendre en charge ?

Il n'y a pas de limite au nombre d'audiences pouvant être prises en charge sur The Trade Desk.