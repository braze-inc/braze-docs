---
nav_title: "Codes courts et longs"
article_title: Codes courts et longs
page_order: 3
description: "Cet article vous guidera à travers les concepts importants impliqués dans l'envoi de numéros de téléphone avec Braze."
page_type: Référence
noindex: vrai
channel:
  - SMS
---

# Codes courts et longs

Les codes courts et longs sont le numéro de téléphone à partir duquel vous envoyez des messages à vos utilisateurs ou clients. Ils peuvent avoir des codes courts de 5 à 6 chiffres ou des codes de 10 chiffres longs. Chaque type de code offre des avantages spécifiques et tous les facteurs doivent être pris en compte avant de choisir si vous voulez un code court. quel type de code court vous pourriez souhaiter, en plus du code long que vous allez déjà être assigné.

## Types de numéros d'envoi

!\[SMS Number Graph\]\[3\]

{% tabs %}
{% tab Short Codes %}

### Codes courts

Un code court est une séquence mémorable de 5 à 6 chiffres qui permet aux expéditeurs d'envoyer des messages à des taux plus cohérents que les codes longs. Si vous envoyez plusieurs centaines de messages par jour à partir d'un code long, vos messages risquent d'être marqués comme indésirables. Cela rend les codes courts parfaits pour l'envoi à grand volume sensible au temps.

| Pros                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| __Vitesse et évolutivité__<br> Les codes courts offrent vitesse et évolutivité avec des taux d'envoi de 100 segments par seconde, 6 000 segments par minute, 360 000 segments par heure et 1 000 000 par deux heures. Les codes courts peuvent atteindre des taux aussi élevés en raison du contrôle qui est requis pendant le processus de demande de code court.<br><br>__MMS-enabled__<br>Les codes courts prennent en charge le MMS, également connu sous le nom de Multimedia Message Service, vous permettant d'envoyer des messages contenant des contenus multimédia (JPG, GIF, PNG) aux téléphones mobiles. Pour plus d'informations sur les MMS au Brésil, consultez [À propos des MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/about_mms/). |
{: .reset-td-br-1}

| Cons                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Les __codes courts ne sont pas disponibles partout__<br> Les codes courts ne sont actuellement disponibles qu'aux États-Unis, au Royaume-Uni et au Canada.<br><br>__Processus de candidature long__<br> Un processus de candidature de 8 à 12 semaines où les cas d'utilisation doivent être décrits en détail est requis. Ce processus impliqué est nécessaire pour assurer la délivrabilité car après avoir accordé un code court, Les transporteurs vérifieront les codes courts, mais ne filtreront pas les messages, ce qui permet des taux d'envoi plus élevés.<br><br>__Un coût plus élevé__<br> Les codes courts coûtent plus cher que les codes longs et prennent plus de temps pour être approuvés. Cependant, une fois que vous avez un code court, vous êtes considéré comme "pré-approuvé" pour mieux envoyer des messages, des tarifs plus rapides et moins scrupuleux pendant le processus d'envoi, car vous aurez parcouru toutes les vérifications pendant votre application pour le code court. |
{: .reset-td-br-1}

{% endtab %}
{% tab Long Codes %}

### Codes longs

Un code long est un numéro de téléphone standard utilisé pour envoyer et recevoir des appels vocaux et des SMS. Les numéros de téléphone sont généralement appelés « codes longs » (numéros de 10 chiffres dans de nombreux pays) lors de la comparaison avec des codes courts SMS (numéros de 5-6 chiffres).

| Pros                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| __Peut être utilisé immédiatement pour envoyer des messages__<br>Les longs codes fournissent une expérience client localisée et personnelle lors de l'envoi de messages pour les cas d'utilisation de personne à personne. Contrairement aux codes courts SMS, l'acquisition d'un code long est un processus assez rapide. Les codes longs peuvent également être définis comme un numéro de secours si un code court échoue.<br><br>__Une plus grande disponibilité dans le monde entier__<br>De longs codes sont disponibles dans plus de 100 pays majeurs dans le monde. Veuillez contacter votre Responsable Customer Success Manager pour une liste des pays disponibles.<br><br>__MMS-enabled__<br>Les codes longs prennent en charge les MMS, également connus sous le nom de Multimedia Message Service, qui vous permettent d'envoyer des messages contenant des contenus multimédia (JPG, GIF, PNG) aux téléphones mobiles. Pour plus d'informations sur les MMS au Brésil, consultez [À propos des MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/about_mms/). |
{: .reset-td-br-1}

| Cons                                                                                                                                                                                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| __Des vitesses d'envoi plus lentes__<br>Les codes longs ne correspondent pas à la vitesse et à l'envoi de codes courts. Les tarifs d'envoi de SMS sont un segment par seconde aux États-Unis, 10 segments par seconde au niveau international. |
{: .reset-td-br-1}

{% endtab %}
{% tab Vanity Short Code %}

### Codes abrégés Vanity

Un code court de vanité est un numéro de téléphone de 5 à 6 chiffres qui est spécifiquement sélectionné par une marque. Les codes abrégés Vanity sont de marque et plus faciles à retenir pour les consommateurs, même s'ils sont généralement plus chers. Par exemple :
- Le département santé du NYC a un code court de `692-692` qui décrit NYC-NYC sur un clavier de téléphone.
- Amazon utilise un code court de `262-966` qui décrit AMA-ZON pour les mises à jour de suivi des envois.
- Paypal utilise un code court de `729-725` qui sort PAY-PAL pour les commandes de message texte.<br><br>

| Pros                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| __Vitesse et évolutivité__<br> Les codes courts offrent vitesse et évolutivité avec des taux d'envoi de 100 segments par seconde, 6 000 segments par minute, 360 000 segments par heure et 1 000 000 par deux heures. Les codes courts peuvent atteindre des taux aussi élevés en raison du contrôle qui est requis pendant le processus de demande de code court.<br><br>__MMS-enabled__<br>Les codes courts Vanity prennent en charge les MMS, également connus sous le nom de Multimedia Message Service, qui vous permettent d'envoyer des messages contenant des contenus multimédia (JPG, GIF, PNG) aux téléphones mobiles. Pour plus d'informations sur les MMS au Brésil, consultez [À propos des MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/about_mms/). |
{: .reset-td-br-1}

| Cons                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| __Les codes courts ne sont pas disponibles partout__<br> Les codes courts ne sont actuellement disponibles que dans les __États-Unis et Canada__.<br><br>__Long processus de demande__<br> Un processus de candidature de 8 à 12 semaines où les cas d'utilisation doivent être décrits en détail est requis. Ce processus impliqué est nécessaire pour assurer la délivrabilité car après avoir donné un code court, les transporteurs vérifieront les codes courts, mais __pas__ filtreront les messages permettant des taux d'envoi plus élevés.<br><br>__Un coût plus élevé__<br> Les codes courts coûtent plus cher que les codes longs et prennent plus de temps pour être approuvés. Cependant, une fois que vous avez un code court, vous êtes considéré comme "pré-approuvé" pour mieux envoyer des messages, des tarifs plus rapides et moins scrupuleux pendant le processus d'envoi, car vous aurez parcouru toutes les vérifications pendant votre application pour le code court. |
{: .reset-td-br-1}

{% endtab %}
{% tab Alphanumeric Sender ID %}

### Identifiant de l'expéditeur alphanumérique

![photo]({% image_buster /assets/img/sms/alphanumericsenderid.jpg %}){: style="float:right;max-width:30%;margin-left:15px;border: 0"}

Les identifiants de l'expéditeur sont les codes courts ou longs qui apparaissent en haut d'un message SMS qui indique à qui le message a été envoyé. Si un utilisateur n'est pas familier avec un ID de l'expéditeur, il peut choisir d'ignorer complètement ces messages. Grâce à l'utilisation d'ID de l'expéditeur Alphanumérique, les utilisateurs sont en mesure d'identifier rapidement de qui ils reçoivent des messages, ce qui augmente les taux d'ouverture.

Les identifiants alphanumériques de l'expéditeur vous permettent de définir le nom ou la marque de votre entreprise comme ID de l'expéditeur lors de l'envoi de messages aller simple aux utilisateurs mobiles. Ils peuvent contenir jusqu'à 11 caractères et accepter les lettres majuscules (A-Z) et minuscules (a-z) et les espaces, et chiffres (0-9). Il ne peut pas s'agir uniquement de chiffres.

| Pros                                                                                                                                                                                                                                                                                                                                        | Cons                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - Pas de frais supplémentaires pour mettre en œuvre<br>- Améliore la notoriété de la marque<br>- Augmente les taux d'ouverture des SMS<br>- correspond à la vitesse d'envoi des numéros de téléphone à l'intérieur du groupe d'abonnement.<br>- Disponible immédiatement si la pré-inscription n'est pas nécessaire | - [La messagerie bidirectionnelle]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/#two-way-messaging-custom-keyword-responses) n'est pas prise en charge<br>- Tous les pays ne supportent pas cette fonctionnalité<br>- Certains pays nécessitent un processus d'approbation supplémentaire. Cela peut prendre du temps supplémentaire.<br>- MMS n'est pas activé |
{: .reset-td-br-1 .reset-td-br-2}

Pour plus d'informations sur les ID de l'expéditeur Alphanumérique, veuillez contacter votre Responsable du Service Clientèle ou contacter le support.
{% endtab %}
{% tab Toll-Free Number %}

### Numéro sans frais activé par SMS

Un numéro de téléphone sans frais ou un numéro de téléphone gratuit est un numéro de téléphone qui est facturé pour tous les appels à l'arrivée au lieu de payer des frais à l'abonné du téléphone original. Les numéros sans frais aux États-Unis et au Canada sont activés par SMS, où les abonnés sont facturés pour les textes entrants et sortants.

| Pros                                                        | Cons                                                                                                                                                                        |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - Peut être utilisé immédiatement pour envoyer des messages | - Les numéros sans frais sont seulement les __États-Unis et le Canada__<br>- Vitesse d'envoi plus lente d'un segment par seconde.<br>- MMS n'est pas activé |
{: .reset-td-br-1 .reset-td-br-2}


{% endtab %}
{% endtabs %}

En plus de ces différences, sachez qu'une marque aura généralement un code court mais plusieurs codes de sauvegarde longs, selon le nombre de destinataires qu'ils prévoient d'envoyer des SMS.

{% alert important %}
Vous vous demandez quels sont les codes courts partagés ? Pour en savoir plus sur les raisons pour lesquelles nous vous recommandons de vous éloigner des codes courts partagés, visitez le sujet dans notre [FAQ SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/faqs/#what-are-shared-short-codes).
{% endalert %}

## Obtenir un code court

Passer à travers le processus de demande de code court peut être un long processus. Mais cela peut être utile ! Si vous souhaitez un code court, contactez votre directeur d’intégration ou un autre représentant de Braze et faites-le savoir. Après avoir fait cela, ils vous demanderont des renseignements de base qui vous aideront à vous qualifier et vous demanderont de faire une demande pour vous.

Ensuite, il ne reste plus qu'à attendre ! Les codes courts peuvent prendre jusqu'à 12 semaines pour recevoir l'approbation pour commencer à utiliser votre code court.

### Application de code court

Bien que Braze soit responsable de l'application réelle du code court, il y a certaines informations dont nous avons besoin de vous. Nous vous recommandons d'examiner ces questions avant de vous adresser à Braze.

Le règlement exige qu'il y ait des réponses à toutes les réponses à la question de l'opt-in, de l'opt-out et de l'aide ou de l'information sur les réponses aux mots-clés. Vous devrez nous faire savoir les flux de messages spécifiques (les réponses que vous voulez envoyer aux utilisateurs après avoir envoyé un [mot-clé]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout/)) que vous voulez pour les suivants :

| Flux requis                              | Type de texte | Exemple                                                                                                                                                                                                           |
| ---------------------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Opt-In <br><br>Double Opt-In | SMS           | `Bienvenue dans notre système de SMS ! Répondez "OUI" pour recevoir les mises à jour de notre entreprise. Répondez à "STOP" pour plus d'informations.`                                                            |
| Opt-In                                   | Site Web      | `Bonjour, voulez-vous vous inscrire à SMS? Texte "START" à "23456". Ou entrez votre numéro ci-dessous.`                                                                                                           |
| Désinscription                           | SMS           | `Désolé de vous voir partir! Si c'était une erreur, le texte de retour "UNSTOP". Texte "AIDE" pour plus d'informations.`                                                                                          |
| Aide                                     | n/a           | `Notre entreprise est une entreprise qui fait cela et cela. Pour plus d'informations sur l'entreprise, faites-le nous savoir ici. Vous pouvez également communiquer avec le support technique au 1-800-111-1111.` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Selon votre situation, vous devrez peut-être fournir plus ou moins de flux comme ceux listés ci-dessus. Vous devrez également nous faire part de trois exemples généraux de messages que vous comptez envoyer par SMS. N'hésitez pas à demander conseil à votre représentant de Braze.

Vous devez également nous informer, quel que soit le numéro que vous utilisez, du nombre de messages que vous comptez envoyer par mois.

{% alert important %}
Si vous avez votre propre code court, contactez votre Responsable du service clientèle pendant le processus d’intégration pour discuter de la migration ou du transfert de votre code court. Les codes courts doivent être configurés par votre Responsable du service clientèle.
{% endalert %}

## Codes longs à 10 chiffres de l'application à personne (A2P 10DLC)

Les codes longs à 10 chiffres d'application à personne (A2P 10DLC) font référence à un système aux États-Unis qui permet aux entreprises d'envoyer des messages de type application à personne (A2P) via un numéro de téléphone standard à 10 chiffres long code (10DLC).

Les codes à 10 chiffres ont traditionnellement été conçus pour le trafic de personnes (P2P) et les entreprises sont contraintes par un débit limité et un filtrage accru. Ce service aide à soulager ces problèmes, améliorant la délivrance globale des messages, permettant aux marques d'envoyer des messages à l'échelle (y compris des liens et des appels à l'action), et d'aider davantage les consommateurs à protéger des messages indésirables.

Tous les clients de Braze qui ont et/ou utilisent actuellement des codes longs sont tenus d'enregistrer leurs codes longs pour 10DLC. Visitez notre [article A2P 10DLC dédié]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/) pour plus d'informations.
[3]: {% image_buster /assets/img/sms/sms_graph.png %}