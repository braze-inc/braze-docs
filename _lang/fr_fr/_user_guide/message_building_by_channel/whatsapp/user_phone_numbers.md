---
nav_title: "Numéros de téléphone des utilisateurs"
article_title: Numéros de téléphone des utilisateurs de WhatsApp
page_order: 1.5
description: "Cet article de référence traite du formatage des numéros de téléphone WhatsApp, de l'importation d'utilisateurs, ainsi que de l'ajout d'utilisateurs à des groupes d'abonnement WhatsApp."
page_type: reference
channel: 
  - WhatsApp
  
---

# Numéros de téléphone des utilisateurs

> Cet article abordera différents sujets autour des numéros de téléphone de vos utilisateurs ou clients.

Les numéros de téléphone sont affichés dans le profil utilisateur dans les formats locaux, mais pas dans le format que vous utilisez pour importer le numéro (`(724) 123 4567`).

## Importation de numéros de téléphone

Vous pouvez importer des numéros de téléphone en [téléchargeant un fichier CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) ou [via l'API]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) pour créer un utilisateur.

### Formatage

Il est important d'importer les numéros nonU.S. au format [`E.164`](https://en.wikipedia.org/wiki/e.164) y compris le "+" et le code du pays. Tout numéro de téléphone qui n'est pas fourni dans ce format sera interprété comme un numéro américain.  

Si un numéro de téléphone est contraint au format E.164 mais ne passe pas la validation, Braze ne pourra pas envoyer de messages WhatsApp à ce numéro. Tous les utilisateurs dont les numéros de téléphone ne sont pas formatables sortiront automatiquement d'une étape du canvas qui inclut le canvas.

Tous les numéros U.S. doivent être des numéros de téléphone valides à 10 chiffres avec un code régional valide. Ils peuvent être saisis sans `+` ni code pays, car Braze considère que tous les numéros de téléphone valides à 10 chiffres sont mappés en tant que numéros U.S.

Tous les numéros internationaux doivent commencer par `+`, suivi du code du pays et du numéro de téléphone. (e.g `+442071838750`)

\![]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

Toutefois, pour garantir l'exactitude de vos envois vers plusieurs régions dont les codes de pays ou de zone sont différents, il est recommandé d'utiliser le format `E.164`, même pour les numéros de téléphone basés sur U.S.

Vous pouvez voir les différences entre le formatage des numéros locaux et le formatage universel ( `E.164` ) dans le tableau suivant :

| Pays | Local | Code du pays | `E.164` |
|---|---|---|---|
| ÉTATS-UNIS | `4155552671` | 1 | `+14155552671` |
| ROYAUME-UNI | `02071838750` | 44 | `+442071838750` |
| Brésil | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

### Ajout d'utilisateurs à WhatsApp un groupe d'abonnement

Pour qu'un client reçoive un message WhatsApp, il doit disposer d'un numéro de téléphone valide et être abonné à un groupe d'abonnement. Pour plus d'informations, reportez-vous à la section [Groupes d'abonnement WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/).


### Plusieurs utilisateurs avec le même numéro de téléphone

Si plusieurs utilisateurs ont le même numéro de téléphone dans un segment d'une même campagne ou étape du canvas, Braze dédupliquera l'envoi et n'enverra qu'un seul message à ce numéro de téléphone. 


