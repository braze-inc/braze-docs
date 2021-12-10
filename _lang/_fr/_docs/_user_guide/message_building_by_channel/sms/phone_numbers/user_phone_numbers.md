---
nav_title: "Numéros de téléphone de l'utilisateur"
article_title: Numéros de téléphone de l'utilisateur SMS
page_order: 1
description: "Cet article de référence couvre le formatage des numéros de téléphone, comment importer des numéros de téléphone et comment ajouter des utilisateurs à des groupes d'abonnement SMS."
page_type: Référence
channel:
  - SMS
---

# Numéros de téléphone utilisateur

> Cet article discutera de différents sujets autour des numéros de téléphone de vos utilisateurs ou de vos clients - si vous recherchez des informations sur vos propres numéros, veuillez consulter notre article sur [Short & Long Codes]({{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/short_and_long_codes/#short--long-codes).

Les numéros de téléphone sont affichés dans le profil de l'utilisateur au format local, mais ne sera pas dans le format que vous utilisez pour importer le numéro (`(724) 123 4567`).

## Importation des numéros de téléphone

Vous pouvez importer des numéros de téléphone en téléchargeant un [CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) ou via [API]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) pour créer un utilisateur.

### Formatage en cours

En tant que meilleure pratique, le meilleur moyen d'importer un numéro de téléphone est au format [`E.164`](https://en.wikipedia.org/wiki/e.164). Cependant, braze tentera d'interpréter ou de convertir n'importe quel u.s. numéroter le meilleur de notre capacité.

Tous les États-Unis les numéros doivent être valides, des numéros de téléphone à 10 chiffres avec un indicatif régional valide. Ils peuvent être saisis sans le `+` et l'indicatif du pays, comme Braze le supposera et associera tous les numéros de téléphone valides à 10 chiffres comme U.S. nombres.

Tous les numéros internationaux doivent commencer par un `+`, suivi de l'indicatif du pays puis du numéro de téléphone. (ex: `+442071838750`)

!\[e164\]\[picture\]{: style="max-width:50%;border: 0;"}

Cependant, pour assurer l'exactitude dans le cas où vous envoyez à plusieurs régions avec des codes pays ou régions différents, il est recommandé d'utiliser le `E. 64` format, même pour les numéros de téléphone basés aux États-Unis.

Vous pouvez voir les différences entre le formatage de nombres locaux et le formatage universel, `E.164` dans le tableau ci-dessous :

| Pays      | Locale       | Code du pays | `E.164`         |
| --------- | ------------ | ------------ | --------------- |
| USA       | `4155552671` | 1            | `+14155552671`  |
| RU        | `2071838750` | 44           | `+442071838750` |
| Le Brésil | `1155256325` | 55           | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

### Ajout d'utilisateurs aux groupes d'abonnement SMS

Pour qu'un client reçoive un message SMS, il doit __avoir un numéro de téléphone valide et être inscrit à un groupe d'abonnement__. Les groupes d'abonnement sont liés au programme SMS que vous exécutez ([assurez-vous de suivre les lois légales pour les SMS et d'avoir enregistré le consentement pour chaque client]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/)). Pour plus d'informations, reportez-vous à [SMS Subscription Groups][1].
[picture]: {% image_buster /assets/img/sms/e164.png %}

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/



