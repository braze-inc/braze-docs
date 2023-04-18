---
nav_title: "Numéro de téléphone de l’utilisateur"
article_title: Numéros de téléphone utilisateur WhatsApp
page_order: 1
description: "Le présent article de référence couvre le formatage du numéro de téléphone WhatsApp, la procédure d’importation des numéros de téléphone, ainsi que la façon d’ajouter des utilisateurs à des groupes d’abonnement WhatsApp."
page_type: reference
channel: 
  - WhatsApp
  
---

# Numéro de téléphone de l’utilisateur

> Le présent article abordera différents sujets autour des numéros de téléphone de vos utilisateurs ou clients.

Les numéros de téléphone sont affichés dans le profil utilisateur en format local, mais ne seront pas au format que vous utilisez pour importer le numéro (`(724) 123 4567`).

## Importation de numéros de téléphone

Vous pouvez importer des numéros de téléphone en téléchargeant un [CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) ou via l’[API]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) pour créer un utilisateur.

### Formatage

Il est important d’importer des numéros non américains au format [`E.164`](https://en.wikipedia.org/wiki/e.164), y compris le « + » et le code pays. Tous les numéros de téléphone n’étant pas fournis dans ce format seront interprétés comme un numéro américain.  

Si un numéro de téléphone est forcé au format E.164 mais ne réussit pas la validation, Braze ne pourra pas envoyer de messages WhatsApp à ce numéro. Tous les utilisateurs dont les numéros de téléphone ne peuvent pas être formatés quitteront automatiquement une étape Canvas qui inclut WhatsApp

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

### Ajouter des utilisateurs à un groupe d’abonnement WhatsApp

Pour qu’un client reçoive un message WhatsApp, il doit avoir un numéro de téléphone valide et être abonné à un groupe d’abonnement. Pour plus d’informations, consultez [Groupes d’abonnement WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/).

[picture]: {% image_buster /assets/img/sms/e164.png %}

