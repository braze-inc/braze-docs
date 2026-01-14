---
nav_title: "Envoi de messages SMS"
article_title: "Aperçu de l'envoi de messages par SMS"
page_order: 4
alias: /sms_message_sending/
description: "Cet article de référence couvre les bases et les bonnes pratiques de l'envoi de SMS."
page_type: reference
channel:
  - SMS
  
---

# Envoi de messages SMS

> L'envoi de messages peut être compliqué, mais ce n'est pas une fatalité. Les sections suivantes présentent les principes fondamentaux de l'envoi de messages SMS chez Braze, notamment l'importance des groupes d'abonnement, les exigences en matière de segments SMS et de corps de message, ainsi que les options de personnalisation avancées disponibles.

## Les bases de l'envoi de SMS

### Sélectionnez votre groupe d'abonnement

Les messages SMS doivent être envoyés à partir d'un [groupe d'abonnement]({{site.baseurl}}/sms_rcs_subscription_groups/). Un groupe d'abonnement est un ensemble de numéros de téléphone d'envoi (tels que des codes courts, des codes longs et/ou des ID d'expéditeur alphanumériques) qui sont utilisés pour un type d'envoi de messages spécifique. Vous devez désigner un groupe d'abonnement pour vous assurer que seuls les utilisateurs abonnés sont ciblés. Certains clients peuvent constater qu'ils ont plusieurs groupes d'abonnement pour différents cas d'utilisation, tels que les messages SMS transactionnels et les messages SMS promotionnels.<br><br>

### Corps du message d'entrée

Le corps d'un message SMS accepte jusqu'à 1 600 caractères, y compris les emojis, Liquid et le contenu connecté. L'envoi d'une seule campagne peut donner lieu à de nombreux envois de segments de messages. Les corps des messages SMS de Braze peuvent être composés de normes d'encodage [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) ou [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set). En cas d'utilisation d'un caractère UCS-2 (par exemple, un Emoji), le corps du message sera automatiquement formaté selon cette norme d'encodage.<br><br> 

### Comprendre les segments de messages et les limites de caractères

Les segments de messages SMS sont la façon dont l'industrie du SMS comptabilise les messages. Un segment de message est un envoi de messages comprenant un nombre défini de caractères (160 pour le codage GSM-7 ; 67 pour le codage UCS-2) qui seront envoyés en une seule fois par SMS. Si vous envoyez un SMS de 161 caractères en utilisant le codage GSM-7, vous verrez qu'il y a deux (2) segments de message qui ont été envoyés. L'envoi de plusieurs segments de messages peut entraîner des frais supplémentaires.<br><br>

### Personnalisation des mots-clés (facultatif)

La réglementation exige qu'il y ait des réponses à toutes les réponses par mot-clé SMS de type "Opt-In", "Opt-Out" et "Aide/Info". Avec Braze, vous pouvez définir vos propres mots-clés pour déclencher des réponses de type "Opt-In", "Opt-Out" et "Aide", gérer vos propres réponses envoyées aux utilisateurs et définir des paramètres de mots-clés pour différentes langues. Pour en savoir plus, consultez notre collection sur le [traitement des mots-clés]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/).

{% alert tip %}
Vous voulez savoir comment créer une campagne SMS ? Consultez notre guide étape par étape sur la [création d'une campagne SMS.]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/create/)
{% endalert %}

## Meilleures pratiques d'envoi {#sending-best-practices}

### Envoi de SMS dans plusieurs pays

Certaines marques peuvent souhaiter envoyer des messages à un groupe d'utilisateurs dont les numéros de téléphone proviennent de différents pays. Pour envoyer un message SMS à un numéro de téléphone situé dans un pays donné, il est préférable d'utiliser un code long ou un code court du même pays. En effet, les codes courts ne peuvent envoyer des SMS qu'à des numéros de téléphone du même pays que celui dans lequel le code court a été créé. 

Pour pallier cette limitation, lors de la [configuration des]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process) groupes d'abonnement, les groupes peuvent être configurés pour contenir des codes longs et courts de plusieurs pays différents. Une fois cette opération terminée, les numéros de téléphone d'envoi ayant le même code pays que le numéro de téléphone de l'utilisateur cible seront automatiquement utilisés lors du lancement d'une campagne. Vous n'aurez pas à créer des campagnes distinctes pour les utilisateurs dont les numéros de téléphone ont des codes pays différents, ce qui vous permet de lancer une seule campagne ou d'utiliser un seul composant Canvas pour cibler les utilisateurs pertinents.

Les charges utiles des SMS sont envoyées en utilisant le même code de pays que le numéro de téléphone de l'utilisateur cible.]({% image_buster /assets/img/sms/multi_country_subgroups.png %})

#### Meilleures pratiques

1. **Obtenez une autorisation**. L'une des règles les plus importantes pour l'utilisation des SMS par les entreprises est que vous devez d'abord obtenir l'autorisation des clients pour les contacter. Si vous ne le faites pas, vous risquez de nuire à votre marque et de devoir payer des frais de justice élevés.<br><br>
2. **Choisissez le bon numéro pour votre cas d'utilisation**. Trois types principaux de numéros de téléphone permettent d'envoyer et de recevoir des messages SMS : les codes longs, les codes courts et les ID d'expéditeur alphanumériques, et leurs capacités et leur disponibilité varient selon les régions. Réfléchissez à l'avance si votre entreprise est mieux servie par un code de vanité. <br><br>
3. **Veillez à respecter le calendrier**. Gardez à l'esprit que les clients sont plus sensibles aux documents qui leur sont directement adressés. Un peu de personnalisation peut s'avérer très utile, par exemple en utilisant le prénom du destinataire ou en ajoutant une touche de conversation qui reflète les centres d'intérêt de vos clients.<br><br>
4. **Engagez des conversations à double sens**. Le SMS est un canal tellement efficace pour l'engagement des clients qu'il est important d'anticiper - et de traiter efficacement - les réponses à vos messages. 85 % des consommateurs veulent non seulement pouvoir recevoir des informations, mais aussi répondre aux entreprises ou engager une conversation.<br><br>
5. **Mesurez ce qui fonctionne**. Atteignez-vous les clients au bon moment, avec la meilleure fréquence et en utilisant les appels à l'action les plus efficaces ? L'utilisation des bons outils de suivi peut offrir des indicateurs directs et mesurables qui prouvent leur ROI. 

### Envoi de gros volumes

Vous prévoyez d'effectuer des envois en grand nombre ? Nous vous proposons quelques bonnes pratiques pour que tout se passe bien.

- Ajustez la limite du débit de réception/distribution pour votre campagne/vitrines si nécessaire, en fonction de la taille de l'audience cible. Cela vous permettra d'atteindre le volume d'envoi dont vous avez besoin et de vous assurer que Braze envoie les messages au rythme attendu et géré par Twilio.
- Veillez à respecter la limite de 160 caractères et soyez attentif au fait que les caractères spéciaux comptent double (par exemple, les barres obliques `\`, les carets `^` et les tildes `~`). 

