---
nav_title: "Numéro de téléphone de l’utilisateur"
article_title: Numéro de téléphone de l’utilisateur SMS
page_order: 1
description: "Cet article de référence couvre le formatage du numéro de téléphone par SMS, la procédure d’importation des numéros de téléphone, ainsi que la façon d’ajouter des utilisateurs à des groupes d’abonnement SMS."
page_type: reference
channel: 
  - SMS
  
---

# Numéro de téléphone de l’utilisateur

> Le présent article abordera différents sujets autour des numéros de téléphone de vos utilisateurs ou clients. Si vous recherchez des informations sur vos propres numéros, consultez notre article sur les [codes courts et codes longs]({{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/short_and_long_codes/#short--long-codes).

Les numéros de téléphone sont affichés dans le profil utilisateur au format local, mais ne seront pas au format que vous utilisez pour importer le numéro (`(724) 123 4567`).

## Importation de numéros de téléphone

Vous pouvez importer des numéros de téléphone en téléchargeant un [CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) ou via l’[API]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) pour créer un utilisateur.

### Formatage

En tant que meilleure pratique, la meilleure façon d’importer un numéro de téléphone est en format [`E.164`](https://en.wikipedia.org/wiki/e.164). Cependant, Braze tentera d’interpréter ou de convertir tout numéro américain au meilleur de notre capacité.

Tous les numéros américains doivent être valides, des numéros à 10 chiffres avec un code de zone valide. Ils peuvent être saisis sans `+` et le code pays, car Braze prend en charge et cartographie tous les numéros de téléphone valides à 10 chiffres en tant que numéros américains.

Tous les numéros internationaux doivent commencer par un `+`, suivi du code de leur pays, puis du numéro de téléphone (par ex. `+442071838750`)

![][image]{: style="max-width:50%;border: 0;"}

Cependant, pour assurer la précision dans l’éventualité où vous envoyez dans plusieurs régions avec différents codes pays ou zones, il est recommandé d’utiliser le format `E.164`, même pour des numéros de téléphone basés aux États-Unis.

Vous pouvez voir les différences entre le formatage du numéro local et le formatage universel, `E.164` dans le tableau suivant :

| Pays | Local | Code pays | `E.164` |
|---|---|---|---|
| USA | `4155552671` | 1 | `+14155552671` |
| UK | `2071838750` | 44 | `+442071838750` |
| Brésil | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

### Ajout d’utilisateurs aux groupes d’abonnement SMS

Pour qu’un client reçoive un SMS, il doit avoir un numéro de téléphone valide et être abonné à un groupe d’abonnement. Les groupes d’abonnement sont liés au programme SMS que vous exécutez (assurez-vous de suivre les [exigences légales pour les SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/) et d’avoir enregistré un consentement pour chaque client). Pour plus d’informations, consultez [Groupes d’abonnement SMS][1]. 

### Gestion des numéros de téléphone non valides

Lorsqu’un numéro de téléphone est jugé non joignable ou non valide, Braze marque le numéro de téléphone de l’utilisateur comme invalide et ne tentera pas d’envoyer d’autres communications à ce numéro de téléphone. Un numéro de téléphone non valide est indiqué dans l’**onglet Engagement** d’un profil utilisateur.

Un numéro de téléphone est considéré comme invalide dans les cas suivants :

- Le numéro de téléphone fourni n’est pas un numéro valide.
- Le format du numéro de téléphone est incorrect.

Ces numéros de téléphone non valides peuvent être gérés en utilisant les[endpoints SMS]({{site.baseurl}}/api/endpoints/sms/). 

{% alert note %}
Si plusieurs profils d’utilisateur ont le même numéro de téléphone et que ce numéro de téléphone est marqué invalide, tous les profils utilisateur s’affichent comme non valides.
{% endalert %}

Vous pouvez également inclure ou exclure les utilisateurs dont les numéros de téléphone sont invalides lors de la [création d’un segment][2]. 

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/
[2]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment
[picture]: {% image_buster /assets/img/sms/e164.png %}

