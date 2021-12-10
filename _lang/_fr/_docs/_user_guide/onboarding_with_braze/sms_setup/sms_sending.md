---
nav_title: "Envoi de SMS"
article_title: Aperçu de l'envoi de SMS
page_order: 4
description: "Cet article de référence couvre les bases et les meilleures pratiques de l'envoi de SMS."
page_type: Référence
channel:
  - SMS
---

# Envoi de SMS

## Les bases d'envoi de SMS

La messagerie peut être compliquée, mais elle ne doit pas l'être. Voici la liste des principes fondamentaux de l'envoi de SMS à Braze, y compris l'importance des groupes d'abonnement, les exigences pour les segments de SMS et les corps de message, ainsi que les options avancées de personnalisation disponibles.

1. __Sélectionnez votre groupe d'abonnements__<br> Les messages SMS doivent être envoyés depuis un [groupe d'abonnement]({{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/sms_subscription_groups/). Un groupe d'abonnement est une collection de numéros de téléphone (c.-à-d. les codes courts, les codes longs et/ou les identifiants alphanumériques de l'expéditeur) qui sont utilisés pour un type spécifique de messagerie. Vous devez désigner un groupe d'abonnement pour vous assurer que seuls les utilisateurs abonnés sont ciblés. Certains clients peuvent trouver qu'ils ont plusieurs groupes d'abonnement pour différents cas d'utilisation, comme la messagerie SMS transactionnelle et la messagerie SMS promotionnelle.<br><br>

2. __Message Body__<br> Un corps de message SMS accepte jusqu'à 1 600 caractères, y compris les Emojis, les Liquides et le Contenu Connecté. Un envoi d'une seule campagne peut entraîner des envois de nombreux segments de messages. Braze SMS messages corps peut être composé soit de [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) soit de [normes d'encodage UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set). Dans le cas où un caractère UCS-2 (par exemple, un Emoji) est utilisé, le corps du message se formera automatiquement pour ce standard d'encodage.<br><br>

3. __Understand Message Segments & Character Limits__<br> Les segments de messages SMS sont la façon dont le secteur des SMS compte les messages. Un segment de message est un regroupement de jusqu'à un nombre défini de caractères (160 pour l'encodage GSM-7 ; 67 pour l'encodage UCS-2) qui sera envoyé en un seul envoi de SMS. Si vous envoyez un SMS avec 161 caractères en utilisant l'encodage GSM-7, vous verrez qu'il y a deux (2) segments de messages qui ont été envoyés. L'envoi de plusieurs segments de messages peut entraîner des frais supplémentaires.<br><br>

4. __La personnalisation des mots-clés (Opt-In, Opt-Out et Infos)__ doit être réglée sur la base du règlement<br> qui exige qu'il y ait des réponses à toutes les réponses aux mots clés Opt-In, Opt-Out et Help/Info SMS. Avec Braze, vous pouvez définir vos propres mots-clés pour déclencher des réponses Opt-In, Opt-Out et Help gérez vos propres réponses qui seront envoyées aux utilisateurs, et définissez des ensembles de mots clés pour différentes langues. En savoir plus sur la personnalisation des mots clés [ici]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/).

{% alert tip %}
Vous voulez apprendre à créer une campagne SMS ? Visitez notre page de navigation par SMS [Étapes suivantes]({{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/next_steps/) et sélectionnez le guide étape par étape.
{% endalert %}

## Envoi des meilleures pratiques

### Envoi de SMS multi-pays

Certaines marques peuvent vouloir envoyer à un groupe d'utilisateurs qui ont des numéros de téléphone de différents pays. Pour envoyer un SMS à un numéro de téléphone dans un pays donné, il est préférable d'utiliser un code long ou un code court qui provient du même pays. En fait, __les codes courts ne peuvent envoyer que des SMS aux numéros de téléphone du même pays que le code court a été créé en__.

Pour surmonter cette limitation, pendant le processus de configuration des Groupes d'Abonnement [][5], peuvent être configurées pour contenir des codes longs et courts de plusieurs pays. Une fois terminé, l'envoi de numéros de téléphone avec le même code de pays que le numéro de téléphone de l'utilisateur cible sera automatiquement utilisé lors du lancement d'une campagne. Vous n'aurez pas à créer des campagnes séparées pour les utilisateurs avec des numéros de téléphone avec des codes de pays différents, vous permettant de lancer une campagne ou d'utiliser une étape de Canvas pour cibler les utilisateurs pertinents.

!\[picture\]\[2\]

#### Meilleures pratiques

1. __Obtenir la permission__. L'une des règles les plus importantes pour l'utilisation de SMS en tant qu'entreprise est que vous devez d'abord obtenir l'autorisation des clients de les contacter. Ne pas le faire peut endommager votre marque et entraîner des frais légaux élevés.<br><br>
2. __Choisissez le bon numéro pour votre cas d'utilisation__. Trois principaux types de numéros de téléphone peuvent envoyer et recevoir des SMS : codes longs, codes courts, et les identifiants de l'expéditeur alphanumérique, ainsi que leurs capacités et leur disponibilité dans différentes régions varient. Pensez à l'avance si votre entreprise est mieux desservie avec un code de vanité. <br><br>
3. __Faites attention au timing__. Gardez à l'esprit que les clients sont plus réceptifs aux documents qui leur sont adressés directement. Un peu de personnalisation va beaucoup plus loin, comme utiliser le prénom du destinataire ou ajouter une touche de conversation qui reflète les intérêts de vos clients.<br><br>
4. __Engager dans des conversations bidirectionnelles__. Les SMS sont un canal tellement efficace pour dialoguer avec les clients qu'il est important d'anticiper - et de gérer efficacement - les réponses à vos messages. 85 % des consommateurs veulent non seulement pouvoir recevoir des informations, mais aussi répondre aux entreprises ou engager une conversation.<br><br>
5. __Mesurer ce qui fonctionne__. Vous atteignez vos clients au bon moment, avec la meilleure fréquence et en utilisant les appels les plus efficaces pour agir ? En utilisant les outils de suivi appropriés, vous pouvez proposer des mesures directes et mesurables qui prouvent votre ROI.

### Envoi en volume élevé

Planifier l'envoi d'un volume élevé ? Nous avons quelques bonnes pratiques à votre disposition pour vous assurer qu'il fonctionne correctement.

- Ajustez la limite de vitesse de livraison pour votre campagne/toile, selon la taille du public cible. Cela vous assurera que (1) vous atteignez le volume d'envoi dont vous avez besoin et (2) Braze envoie les messages au rythme que Twilio attend et peut gérer.
- Assurez-vous que vous respectez la limite de 160 caractères et que vous êtes au courant du double décompte des caractères spéciaux (c.-à-d. \ ^ &#126;).
[2]: {% image_buster /assets/img/sms/multi_country_subgroups.png %}

[5]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
