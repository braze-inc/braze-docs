---
nav_title: Friendbuy
article_title: Friendbuy
description: "Découvrez comment intégrer Friendbuy à Braze."
alias: /partners/friendbuy/
page_type: partner
search_tag: Partner

---

# Friendbuy

> Tirez parti de l'intégration entre Friendbuy et Braze pour étendre vos capacités en matière d'e-mails et de SMS tout en automatisant sans effort vos communications relatives aux programmes de recommandation et de fidélisation. Braze créera des profils de clients pour tous les numéros de téléphone ayant fait l'objet d'un abonnement et collectés par l'intermédiaire de Friendbuy.

## Conditions préalables

Avant de commencer, vous avez besoin des éléments suivants :

| Prérequis          | Description                                                                                                                              |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Un compte Friendbuy   | Un [compte Friendbuy][1] est nécessaire pour profiter de ce partenariat.                                                              |
| Une clé de l'API REST de Braze  | Une clé API REST de Braze avec des autorisations `users.track`. Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**.        |
| Un endpoint REST de Braze | L’[URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), qui dépend de l'URL de votre instance Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Si vous utilisez la [navigation plus ancienne]({{site.baseurl}}/navigation), vous pouvez créer une clé API dans la **console de développement** > **Paramètres de l'API**.
{% endalert %}

## Intégration de Friendbuy

Dans [Friendbuy][1], allez dans **Developer Center** > **Integrations**, puis sur la carte d'intégration de Braze, sélectionnez **Add integration.**

![La carte d'intégration de Braze dans Friendbuy.][100]{: style="max-width:75%;"}

Dans le formulaire, saisissez votre endpoint REST et votre clé API, puis sélectionnez **Installer l'intégration**.

![Le formulaire d'intégration de Friendbuy.][101]{: style="max-width:55%;"}

Retournez à votre [compte Friendbuy][1] et actualisez la page. Si votre intégration a réussi, vous verrez apparaître un message similaire à celui qui suit :

![intégration installée][102]{: style="max-width:55%;"}

### Attributs personnalisés

| Nom de l'attribut personnalisé            | Définition                                                                                                                                         | Type de données |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **État de la recommandation Friendbuy**    | Les auteurs des recommandations sont classés dans la catégorie *Référents* et les personnes recommandées sont classées dans la catégorie des *Amis recommandés.*                                                          | Chaîne de caractères    |
| **Nom du client Friendbuy**      | Le nom que le client a saisi lorsqu'il a envoyé ses informations par l'intermédiaire d'un widget de recommandation.                                                                 | Chaîne de caractères    |
| **Lien de recommandation Friendbuy**      | Un lien de recommandation personnel (PURL) généré pour un référent. Par exemple, https://fbuy.io/EzcW                                                       | Chaîne de caractères    |
| **Date du dernier partage Friendbuy** | La date et l'heure du dernier partage du référent avec un ami via un canal de partage. Si le référent n'a pas encore partagé sa recommandation, la propriété ne sera pas visible. | Heure      |
| **ID de campagne Friendbuy**        | L'ID de la campagne associée au lien de recommandation personnel généré pour un référent.                                                               | Chaîne de caractères    |
| **Nom de la campagne Friendbuy**      | Le nom de la campagne associé au lien de recommandation personnel généré pour un référent.                                                             | Chaîne de caractères    |
| **Code de réduction Friendbuy**        | Le code de recommandation le plus récent distribué au client. Remarque : un seul code sera affiché.                                            | Chaîne de caractères    |
| **Valeur du coupon Friendbuy**       | La valeur monétaire du dernier code de réduction distribué au client.                                                                     | Nombre    |
| **État des coupons Friendbuy**      | L’état du dernier code de réduction distribué au client. Remarque : l’état peut être "distribué" ou "utilisé".                            | Chaîne de caractères    |
| **Monnaie de coupon Friendbuy**    | Code de devise (USD, CAD, etc.) ou pourcentage (%) associé au code de coupon le plus récent distribué au client.                             | Chaîne de caractères    |
| **ID de la campagne de coupons Friendbuy** | L'ID de la campagne associée au code de coupon généré pour un client.                                                                          | Chaîne de caractères    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Comportement par défaut

Avant que les données des clients puissent être envoyées à Braze, les clients doivent donner leur abonnement par le biais du widget de recommandation en cochant une ou plusieurs cases des cases suivantes :

![Widget de recommandation][103]

{% alert note %}
Friendbuy utilise la norme internationale (E.164) pour vérifier les numéros de téléphone réels. Les numéros non valides, tels que `555-555-5555`, ne seront pas envoyés à Braze.
{% endalert %}

### Comportement des cases à cocher

| Case à cocher sélectionnée | Comportement                                                        |
|-------------------|-----------------------------------------------------------------|
| Uniquement par e-mail        | Seule l'adresse e-mail du client est envoyée à Braze.             |
| Téléphone uniquement        | Seul le numéro de téléphone du client est envoyé à Braze.              |
| Aucun des deux           | Aucune donnée du client n'est envoyée à Braze.                              |
| Les deux              | L'adresse e-mail et le numéro de téléphone du client sont envoyés à Braze. |

[1]: https://retailer.friendbuy.io/
[100]: {% image_buster /assets/img/friendbuy/choosing_braze.png %}
[101]: {% image_buster /assets/img/friendbuy/install_form.png %}
[102]: {% image_buster /assets/img/friendbuy/install_success.png %}
[103]: {% image_buster /assets/img/friendbuy/referral_widget.png %}
