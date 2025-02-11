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

> Le présent article abordera différents sujets autour des numéros de téléphone de vos utilisateurs ou clients. Si vous cherchez des informations sur vos propres numéros, consultez notre article sur l' [envoi de numéros de téléphone]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/short_and_long_codes/).

Les numéros de téléphone apparaissent dans le profil utilisateur sous la forme d'une chaîne de caractères. Si vous importez un nombre qui contient des non chiffres (tels que `,`, `-`, `(`, ou autres), les non chiffres seront supprimés. Par exemple, l'importation de `+1 (724) 123-4567` s'affichera sous la forme `17241234567`.

## Importation de numéros de téléphone

Vous pouvez importer des numéros de téléphone en téléchargeant un [fichier CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) ou via l'[API]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) pour créer un utilisateur.

### Formatage

La meilleure façon d'importer un numéro de téléphone est de le faire au format [`E.164`](https://en.wikipedia.org/wiki/e.164). Toutefois, Braze s'efforcera d'interpréter ou de convertir tout numéro U.S. au mieux de ses possibilités.

Tous les numéros U.S. doivent être des numéros de téléphone valides à 10 chiffres avec un code régional valide. Ils peuvent être saisis sans `+` ni code pays, car Braze considère que tous les numéros de téléphone valides à 10 chiffres sont mappés en tant que numéros U.S.

Tous les numéros internationaux doivent commencer par `+`, suivi du code du pays et du numéro de téléphone. (e.g `+442071838750`)

![][image]{: style="max-width:50%;border: 0;"}

Toutefois, pour garantir l'exactitude de vos envois vers plusieurs régions ayant des codes de pays ou de zone différents, il est recommandé d'utiliser le format `E.164`, même pour les numéros de téléphone basés sur U.S.

Vous pouvez voir les différences entre le formatage du numéro local et le formatage universel, `E.164` dans le tableau suivant :

| Pays | Local | Code pays | `E.164` |
|---|---|---|---|
| États-Unis | `4155552671` | 1 | `+14155552671` |
| UK | `2071838750` | 44 | `+442071838750` |
| Brésil | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

### Ajout d’utilisateurs aux groupes d’abonnement SMS

Pour qu’un client reçoive un SMS, il doit avoir un numéro de téléphone valide et être abonné à un groupe d’abonnement. Les groupes d'abonnement sont liés au programme de SMS que vous menez (assurez-vous de respecter les [exigences légales en matière de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/) et d'avoir enregistré le consentement de chaque client). Pour plus d'informations, consultez [Groupes d'abonnement SMS][1]. 

### Gestion des numéros de téléphone non valides

Lorsqu'un numéro de téléphone est considéré comme invalide, Braze marque le numéro de téléphone de l'utilisateur comme invalide et ne tente pas d'envoyer d'autres communications à ce numéro de téléphone. Un numéro de téléphone non valide est signalé dans l'**onglet Engagement** d’un profil utilisateur.

![][image2]{: style="max-width:50%;border: 0;"}

Un numéro de téléphone est considéré comme invalide pour les raisons suivantes :
- **Erreur du fournisseur**: une erreur permanente a été reçue du fournisseur de SMS. Cela indique que le numéro de téléphone fourni est mal formaté ou qu'il est définitivement incapable de recevoir des messages SMS.
- **Désactivé**: le numéro de téléphone a été désactivé parce qu'un abonné mobile a mis fin à son service et a aboli son numéro auprès de son opérateur (il peut éventuellement être recyclé et attribué à un nouvel utilisateur).

Ces numéros de téléphone non valides peuvent être gérés à l'aide d'[endpoints SMS.]({{site.baseurl}}/api/endpoints/sms/) 

{% alert note %}
Si plusieurs profils utilisateurs ont le même numéro de téléphone et que ce numéro de téléphone est marqué comme invalide, tous les profils utilisateurs existants avec ce numéro s'afficheront comme invalides. Les profils utilisateurs nouvellement créés ne seront jamais marqués comme invalides au départ.
{% endalert %}

Vous pouvez également inclure ou exclure tout utilisateur dont le numéro de téléphone n'est pas valide lors de la [création d'une segmentation][2]. 

### Approvisionnement et vérification par des tiers

Braze s'appuie sur des outils tiers pour trouver les numéros non valides. Braze n'est pas responsable des pannes ou de la désinformation de ces services. Cet outil ne doit donc pas être votre seule méthode de conformité pour vérifier les numéros non valides.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/
[2]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment
[image] : {% image_buster /assets/img/sms/e164.png %}
[image2] : {% image_buster /assets/img/sms/invalid_banner.png %}
