---
nav_title: "Numéros de téléphone des utilisateurs"
article_title: Numéros de téléphone des utilisateurs de SMS
page_order: 7
description: "Cet article de référence traite du formatage des numéros de téléphone SMS, de l'importation d'utilisateurs et de l'ajout d'utilisateurs à des groupes d'abonnement SMS."
page_type: reference
alias: /user_phone_numbers/
channel: 
  - SMS
  - MMS
  - RCS
---

# Numéros de téléphone des utilisateurs

> Cet article abordera différents sujets autour des numéros de téléphone de vos utilisateurs ou clients. Si vous cherchez des informations sur vos propres numéros, consultez notre article sur l' [envoi de numéros de téléphone]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/).

## Format recommandé

Nous vous recommandons d'importer les numéros de téléphone au format [`E.164`](https://en.wikipedia.org/wiki/e.164) afin de garantir l'exactitude de vos envois vers plusieurs régions ayant des codes de pays ou de zone différents, même pour les numéros de téléphone basés sur le site U.S.

- **U.S. chiffres :** Tous les numéros U.S. doivent être des numéros de téléphone valides à 10 chiffres avec un code régional valide. S'il manque un `+` et un code pays à un numéro de téléphone à 10 chiffres, Braze le mappera en tant que numéro U.S.
- **Numéros internationaux :** Tous les numéros internationaux doivent commencer par un `+`, suivi du code du pays et du numéro de téléphone. Par exemple, `+442071838750`.

Exemple d'un numéro de téléphone international e164 valide.]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

Voici quelques exemples illustrant les différences entre le formatage local et le formatage `E.164`:

| Pays | Local | Code du pays | `E.164` |
|---|---|---|---|
| ÉTATS-UNIS | `4155552671` | 1 | `+14155552671` |
| ROYAUME-UNI | `2071838750` | 44 | `+442071838750` |
| Brésil | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

## Importation de numéros de téléphone

Lorsque vous importez des numéros de téléphone, il est important de respecter le [format recommandé.](#recommended-format) Pour importer des numéros de téléphone, utilisez l'une des méthodes suivantes :

- [Téléchargement d'un fichier CSV vers Braze]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv)
- [Utilisation de l'endpoint `/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track)

{% alert important %}
Les numéros de téléphone des utilisateurs s'affichent dans Braze sous la forme d'une chaîne de caractères. Si vous importez un nombre qui contient des non chiffres (tels que `,`, `-`, `(`, ou autres), les non chiffres seront supprimés lors du rendu dans Braze. Par exemple, l'importation de `+1 (724) 123-4567` s'affichera sous la forme `17241234567`.
{% endalert %}

## Traitement des numéros de téléphone non valides

Lorsqu'un numéro de téléphone est considéré comme invalide, Braze marque le numéro de téléphone de l'utilisateur comme invalide et ne tente pas d'envoyer d'autres communications à ce numéro de téléphone. Un numéro de téléphone non valide est signalé dans l'**onglet Engagement d'** un profil utilisateur.

Exemple de message d'erreur pour les numéros de téléphone non valides dans Braze.]({% image_buster /assets/img/sms/invalid_banner.png %}){: style="max-width:50%;border: 0;"}

Un numéro de téléphone est considéré comme invalide pour les raisons suivantes :

- **Erreur du fournisseur**: une erreur permanente a été reçue du fournisseur de SMS et RCS. Ceci indique que le numéro de téléphone fourni est mal formaté ou définitivement incapable de recevoir des messages SMS ou RCS.
- **Désactivé**: le numéro de téléphone a été désactivé parce qu'un abonné mobile a mis fin à son service et a aboli son numéro auprès de son opérateur (il peut éventuellement être recyclé et attribué à un nouvel utilisateur).

Ces numéros de téléphone invalides peuvent être gérés à l'aide de [points d'extrémité SMS et RCS.]({{site.baseurl}}/api/endpoints/sms/) 

{% alert note %}
Si plusieurs profils utilisateurs ont le même numéro de téléphone et que ce numéro de téléphone est marqué comme invalide, tous les profils utilisateurs existants avec ce numéro s'afficheront comme invalides. Les profils utilisateurs nouvellement créés ne seront jamais marqués comme invalides au départ.
{% endalert %}

Vous pouvez également inclure ou exclure tout utilisateur dont le numéro de téléphone n'est pas valide lors de la [création d'une segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment).

## Ajout d'utilisateurs à des groupes d'abonnement SMS et RCS

Pour qu'un utilisateur reçoive un message SMS ou RCS, il doit avoir un numéro de téléphone valide et être abonné à un groupe d'abonnement. Les groupes d'abonnement sont liés au programme SMS ou RCS que vous menez (assurez-vous de respecter les [exigences légales en matière de SMS, MMS et RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) et d'avoir enregistré le consentement de chaque client). Pour plus d'informations, reportez-vous à la section [Groupes d'abonnement SMS et RCS.]({{site.baseurl}}/sms_rcs_subscription_groups/)

## Approvisionnement et vérification par des tiers

Braze s'appuie sur des outils tiers pour trouver les numéros non valides. Braze n'est pas responsable des pannes ou de la désinformation de ces services. Cet outil ne doit donc pas être votre seule méthode de conformité pour vérifier les numéros non valides.
