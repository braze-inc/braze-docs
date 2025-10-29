
# Expéditeurs de SMS et de RCS

> Le présent article vous guidera à travers des concepts importants concernant l’envoi de numéros de téléphone avec Braze.

## Types d'expéditeurs de SMS et de RCS

{% tabs %}
{% tab RCS-Expéditeur vérifié %}

#### Expéditeur vérifié par le RCS

Un expéditeur vérifié par RCS est une représentation visuelle de votre marque qui comprend un nom de marque, un logo, une légende facultative et un badge vérifié. L'expéditeur vérifié par RCS bénéficie ainsi d'un avantage significatif par rapport aux codes SMS en termes d'établissement de la confiance de l'utilisateur.  

##### Détails

| Composants visuels | Accès | Débit | MMS activé | Unidirectionnel ou Bidirectionnel |
| --- | --- | --- | --- | --- |
| \- Nom de marque<br>\- logo<br>\- légende facultative<br> \- badge vérifié | 4-6 semaines pour une demande (peut varier) | Environ 100 messages par expéditeur et par seconde. Les débits réels peuvent varier en fonction du fournisseur, des conditions du réseau et des détails spécifiques de la mise en œuvre. | Non | Bidirectionnel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

##### Avantages et inconvénients

| Avantages |
| ---- |
| **Établir la confiance**<br> Les expéditeurs vérifiés par RCS sont beaucoup plus efficaces pour établir la confiance des utilisateurs que les codes SMS, étant donné leur nature très visuelle ainsi que leur vérification explicite par l'opérateur. 
<br><br>**Fonctionnalités d'envoi de messages riches**<br>Les expéditeurs vérifiés par RCS permettent d'envoyer des messages avec des fonctionnalités plus riches que celles des SMS, y compris le média enrichi, comme les fichiers images et les boutons interactifs. |
{: .reset-td-br-1}

| Inconvénients |
| ---- |
| **Nouveauté et dynamisme du marché**<br> RCS est un protocole relativement nouveau, ce qui signifie que la couverture des opérateurs, la livrabilité et la tarification évoluent à des rythmes différents selon les régions. Cependant, l'accord récent d'Apple sur la prise en charge du RCS signifie que la grande majorité des utilisateurs de smartphones sont désormais joignables par ce protocole. <br><br>**Coût plus élevé de l'envoi de messages enrichis**<br> Les messages RCS qui utilisent beaucoup de fonctionnalités d'envoi de messages enrichis ont tendance à coûter plus cher par message que les messages SMS. Cela n'est pas surprenant étant donné les avantages des fonctionnalités riches, mais il peut être important de le noter pour votre budget marketing. |
{: .reset-td-br-1}

{% endtab %}
{% tab Short Codes SMS %}

#### Codes courts SMS

Un code court est une séquence mémorable de 5 à 6 chiffres qui permet aux expéditeurs d'envoyer des messages à des taux plus élevés que les codes longs. Les codes courts sont ainsi parfaitement adaptés à l’envoi sensible au temps de volumes élevés.

##### Détails

| Longueur | Accès | Débit | MMS activé | Unidirectionnel ou Bidirectionnel |
| --- | --- | --- | --- | --- |
| 5-6 chiffres | Application 8-12 semaines| 100 messages par seconde ou plus | Oui | Bidirectionnel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Avantages et inconvénients

| Avantages |
| ---- |
| **Vitesse et évolutivité**<br> Les codes courts offrent vitesse et évolutivité avec des taux d’envoi de 100 segments par seconde, 6 000 segments par minute, 360 000 segments par heure et 1 million de segments par 2 heures. Les codes courts peuvent atteindre ces taux élevés en raison de la vérification requise pendant le processus de demande de code court.<br><br>**MMS activé pour certains codes courts**<br>Certains codes courts peuvent prendre en charge les MMS, également connus (ou Multimedia Message Service), ce qui vous permet d'envoyer des messages contenant des ressources multimédias (JPEG, GIF, PNG) vers des téléphones mobiles. Pour plus d'informations sur les MMS dans Braze, reportez-vous à la section [À propos des MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/about_mms/). |
{: .reset-td-br-1}

| Inconvénients |
| ---- |
| **Les codes courts sont disponibles dans moins de pays**<br> Les codes courts sont actuellement disponibles dans certains pays, notamment aux États-Unis, au Royaume-Uni et au Canada.<br><br>**Processus de demande plus long**<br> Un processus de demande complexe dans lequel les cas d'utilisation doivent être décrits de manière très détaillée est nécessaire. Ceci est nécessaire pour garantir la livrabilité. En effet, après avoir accordé un code court, les opérateurs vérifieront les codes courts, mais ils ne filtreront **pas** les messages, ce qui permet des taux d’envoi plus élevés. La durée de cette procédure varie selon les pays.<br><br>**Coût plus élevé**<br> Les codes courts coûtent plus cher que les codes longs et sont plus longs à obtenir. Cependant, une fois que vous avez un code court, vous êtes considéré comme « pré-approuvé » pour envoyer des messages plus rapidement à des tarifs plus avantageux et faire l’objet d’un examen moins rigoureux pendant le processus d’envoi. Vous avez en effet passé tous les contrôles au moment de votre demande de code court. |
{: .reset-td-br-1}

{% endtab %}
{% tab Codes longs SMS %}

#### Codes longs des SMS

Un code long est un numéro de téléphone standard utilisé pour envoyer et recevoir des appels vocaux et des messages SMS. Les numéros de téléphone sont généralement appelés des « codes longs » (numéros à 10 chiffres dans de nombreux pays) si vous les comparez avec des codes courts SMS (numéros à 5 ou 6 chiffres).

##### Détails

| Longueur | Accès | Débit | MMS activé | Unidirectionnel ou Bidirectionnel |
| --- | --- | --- | --- | --- |
| 10 chiffres | Demande de 4 à 6 semaines (peut être plus courte ou plus longue selon les pays) | Aux États-Unis, le débit dépend de votre score de confiance 10DLC ; sur les marchés internationaux, le débit peut varier ou être augmenté dans certaines circonstances. | Oui | Bidirectionnel (en fonction de l'endroit où vous envoyez le message) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Avantages et inconvénients

| Avantages |
| ---- |
| **Peut être utilisé immédiatement pour envoyer des messages (pour certains pays)**<br>Les codes longs offrent une expérience client localisée et personnalisée lors de l'envoi de messages pour les cas d'utilisation de personne à personne. Contrairement aux codes courts SMS, l'acquisition d'un code long est un processus assez rapide pour certains pays. (Pour les autres pays, le délai est aussi long, voire plus long, que celui d'un code court). Les codes longs peuvent également être définis comme un numéro de secours en cas d’échec d’un code court.<br><br>**Une plus grande disponibilité dans le monde entier**<br>Les codes longs sont disponibles dans plus de 100 grands pays du monde. Veuillez contacter votre gestionnaire du succès des clients ou l’[assistance]({{site.baseurl}}/braze_support/) de Braze pour obtenir une liste des pays disponibles.<br><br>**MMS activé pour certains pays**<br>Prend en charge les MMS (ou Multimedia Message Service), qui vous permettent d’envoyer des messages contenant des ressources multimédias (JPEG, GIF, PNG) vers des téléphones mobiles. Pour plus d'informations sur les MMS dans Braze, consultez notre documentation [ici]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/about_mms/).|
{: .reset-td-br-1}

| Inconvénients |
| --- |
| **Vitesses d'envoi plus lentes**<br>La vitesse et les conditions d’envoi des codes longs sont différentes de celles des codes courts. Les tarifs d'envoi de SMS dépendent de votre score de confiance 10DLC aux États-Unis. |
{: .reset-td-br-1}

{% endtab %}
{% tab SMS Vanity Short Code %}

#### Codes courts de vanité pour les SMS

Un code court à 5 à 6 chiffres est spécifiquement sélectionné par une marque. Les codes courts Vanity sont liés à une marque et sont plus faciles à retenir pour les consommateurs, mais ils sont généralement plus chers. Par exemple :
- Le service de santé de New York dispose d’un code court Vanity `692-692` qui affiche NYC-NYC sur un clavier de téléphone.
- Amazon utilise un code court `262-966` qui affiche AMA-ZON pour les mises à jour de suivi des envois.
- PayPal utilise un code court de `729-725` qui s'écrit PAY-PAL pour les commandes par message texte.<br><br>

##### Détails

| Longueur | Accès | Débit | MMS activé | Unidirectionnel ou Bidirectionnel |
| --- | --- | --- | --- | --- |
| 5-6 chiffres | Application 8-12 semaines | 100 messages par seconde | Oui | Bidirectionnel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Avantages et inconvénients

| Avantages |
| ---- |
| **Vitesse et évolutivité**<br> Les codes courts offrent vitesse et évolutivité avec des taux d’envoi de 100 segments par seconde, 6 000 segments par minute, 360 000 segments par heure et 1 million de segments par 2 heures. Les codes courts peuvent atteindre ces taux élevés en raison de la vérification requise pendant le processus de demande de code court.<br><br>**MMS activé**<br>Prend en charge les MMS (ou Multimedia Message Service), qui vous permettent d’envoyer des messages contenant des ressources multimédias (JPEG, GIF, PNG) vers des téléphones mobiles. Pour plus d'informations sur les MMS dans Braze, reportez-vous à la section [À propos des MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/about_mms/). |
{: .reset-td-br-1}

| Inconvénients |
| ---- |
| **Les codes courts ne sont pas disponibles partout**<br> Actuellement, les codes courts sont uniquement disponibles **aux États-Unis et au Canada (CA)**.<br><br>**Processus de demande plus long**<br> Un processus de demande complexe de 8 à 12 semaines dans lequel les cas d'utilisation doivent être décrits de manière très détaillée est nécessaire. Ce processus complexe est nécessaire pour garantir la livrabilité. En effet, après avoir accordé un code court, les opérateurs vérifieront les codes courts, mais ils ne filtreront **pas** les messages, ce qui permet des taux d’envoi plus élevés.<br><br>**Coût plus élevé aux États-Unis**<br> Il n'y a pas de coût supplémentaire pour les codes courts en Californie, mais aux États-Unis, les codes courts coûtent plus cher que les codes longs et sont plus longs à obtenir. Cependant, une fois que vous avez un code court, vous êtes considéré comme « pré-approuvé » pour envoyer des messages plus rapidement à des tarifs plus avantageux et faire l’objet d’un examen moins rigoureux pendant le processus d’envoi. Vous avez en effet passé tous les contrôles au moment de votre demande de code court. |
{: .reset-td-br-1}

{% endtab %}
{% tab SMS Alphanumérique ID de l'expéditeur %}

#### ID alphanumérique de l'expéditeur du SMS

Les ID d’expéditeur sont les codes courts ou longs qui apparaissent en haut d’un message SMS indiquant qui a envoyé le message. Si un utilisateur n’est pas familier avec un ID d’expéditeur, il peut choisir d’ignorer complètement ces messages. Grâce à l'utilisation d'ID d'expéditeur alphanumériques, les utilisateurs sont en mesure d'identifier rapidement l'auteur des messages qu'ils reçoivent, ce qui augmente le taux d'ouverture. 

Les ID d'expéditeur alphanumériques vous permettent de définir le nom de votre entreprise ou de votre marque (comme "Kitchenerie" ou "CashBlastr") comme ID d'expéditeur lors de l'envoi de messages à sens unique à des utilisateurs mobiles. Ils peuvent comporter jusqu’à 11 caractères et accepter les lettres majuscules (A-Z) et minuscules (a-z), ainsi que les espaces et les chiffres (0-9). Ils **ne peuvent pas** être composés seulement de chiffres. 

##### Détails

| Longueur | Accès | Débit | MMS activé | Unidirectionnel ou Bidirectionnel |
| --- | --- | --- | --- | --- |
| Jusqu’à 11 caractères | Disponible immédiatement si l’enregistrement préalable n’est pas requis | Varie selon le pays | Non | Unidirectionnel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Avantages et inconvénients

| Avantages | Inconvénients |
| ---- | ---- | 
| {::nomarkdown} <ul> <li> Pas de frais supplémentaires pour la mise en œuvre </li> <li> Améliore la notoriété de la marque </li> <li> Augmente le taux d'ouverture des SMS </li> <li> Correspond à la vitesse d'envoi des numéros de téléphone à l'intérieur du groupe d'abonnement. </li> <li> Disponible immédiatement si l’enregistrement préalable n’est pas requis </li> </ul> {:/} | {::nomarkdown} <ul> <li> L'<a href='/docs/user_guide/message_building_by_channel/sms/keywords/#two-way-messaging-custom-keyword-responses/'>envoi de messages dans les deux sens</a> n'est pas pris en charge. </li> <li> Cette fonctionnalité n'est pas disponible dans tous les pays. </li> <li> Certains pays exigent une procédure d'approbation supplémentaire </li> <li> MMS n'est pas activé </li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2}

Pour plus d’informations sur les ID d’expéditeur alphanumériques, veuillez contacter votre gestionnaire du succès des clients.
{% endtab %}
{% tab Numéro gratuit SMS %}

#### Numéro gratuit par SMS

Un numéro de téléphone gratuit ou numéro vert est un numéro de téléphone qui est facturé pour tous les appels entrants au lieu de générer des frais pour l’abonné téléphonique d’origine. Les numéros gratuits aux États-Unis et au Canada sont activés par SMS, où les abonnés sont facturés pour les textes entrants et sortants.

##### Détails

| Longueur | Accès | Débit | MMS activé | Unidirectionnel ou Bidirectionnel |
| --- | --- | --- | --- | --- |
| 10 chiffres	 | Demande de 2 à 4 semaines | Dépend de votre approbation et peut être augmentée en payant plus. | Non | Bidirectionnel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Avantages et inconvénients

| Avantages | Inconvénients |
| ---- | ---- | 
| {::nomarkdown} <ul> <li> Doit être enregistré avant l'envoi. </li> </ul> {:/} | {::nomarkdown} <ul> <li> Les numéros verts ne concernent que les États-Unis et le Canada </li><li> MMS n'est pas activé </li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2} 

{% endtab %}
{% endtabs %}

{% alert important %}
Si le débit est dépassé, certains messages peuvent échouer.
{% endalert %}

En plus de ces différences, sachez qu’une marque aura généralement un code court, mais plusieurs codes longs de secours, selon le nombre de destinataires auxquels elle envisage d’envoyer des messages par SMS.

{% alert important %}
Vous vous demandez ce qu’on appelle des codes courts partagés ? Pour en savoir plus sur les raisons pour lesquelles nous vous recommandons d'éviter les codes courts partagés, consultez la rubrique de notre [FAQ SMS.]({{site.baseurl}}/sms_faq/)
{% endalert %}

## Envoi de SMS numéros de téléphone

Les codes courts et longs correspondent au numéro de téléphone depuis lequel vous envoyez des messages à vos utilisateurs ou clients. Ce peut être des codes courts à 5 ou 6 chiffres ou des codes longs à 10 chiffres. Chaque type de code offre des avantages spécifiques et vous devez prendre en compte tous les facteurs avant de choisir si vous souhaitez un code court, quel type de code court, en plus du code long qui vous a déjà été attribué.

## Comment obtenir un code court pour les SMS ?

Le processus de demande de code court peut être un processus long. Il peut, toutefois, en valoir la peine. Si vous souhaitez un code court, contactez votre gestionnaire d’onboarding ou un autre conseiller Braze et informez-le de vos besoins. Ensuite, ils feront une demande pour vous - ils vous demanderont quelques informations de base qui vous aideront à remplir les conditions requises. Ensuite, il ne vous reste plus qu’à attendre.

### Demande de code court

Bien que Braze soit responsable de la demande effective de code court, nous avons besoin de quelques informations. Nous vous recommandons d’examiner ces questions avant de contacter Braze. 

Les réglementations exigent qu’il y ait des réponses à toutes les questions sur l’abonnement, le désabonnement, l’aide/les informations et les réponses à des mots-clés. Vous devrez nous indiquer les flux de messages spécifiques (les réponses que vous souhaitez envoyer aux utilisateurs après qu'ils ont envoyé un [mot-clé]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/)) que vous souhaitez pour les situations suivantes.

| Flux nécessaire | Type | Exemple |
| ----------- | ---- | ------- |
| Abonnement <br><br>Double abonnement| SMS | `Welcome to our SMS system! Reply "YES" to receive updates from our company. Respond "STOP" to opt-out and "HELP" for more info.` |
| Abonnement | Site Internet | `Hi there, would you like to sign up for SMS? Text "START" to "23456". Or, enter your number below.` |
| Désabonnement | SMS | `Sorry to see you go! If this was a mistake, text back "UNSTOP". Text "HELP" for more information.` |
| Aide | N/A | `Our company is a company that does this and that. For more info on the company, let us know here. Or, you can contact support at 1-800-111-1111.` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Selon votre situation, vous devrez peut-être fournir plus ou moins de flux comme ceux répertoriés dans le tableau précédent. Vous devrez également nous communiquer **trois exemples généraux** de messages que vous souhaitez envoyer par SMS. N’hésitez pas à demander conseil à votre conseiller Braze.

Vous devez également nous informer, quel que soit le numéro que vous utilisez, du nombre de messages par mois que vous prévoyez d’envoyer.

{% alert important %}
Si vous avez votre propre code court, contactez votre gestionnaire du succès des clients au cours du processus d’onboarding pour discuter de la migration ou du transfert de votre code court. Les codes courts doivent être configurés par votre gestionnaire du succès des clients.
{% endalert %}

## SMS Application-to-Person 10-Digit Long Codes (A2P 10DLC)

A2P 10DLC fait référence à un système aux États-Unis qui permet aux entreprises d’envoyer des communications de type Application à personne (A2P) via un numéro de téléphone standard à 10 chiffres en code long (10DLC). Les codes longs à 10 chiffres sont traditionnellement conçus pour le trafic de personne à personne (P2P), ce qui limite le débit des entreprises et renforce le filtrage. Ce service aide à atténuer ces problèmes, améliorant la livrabilité globale des messages. Les marques peuvent ainsi envoyer des messages à grande échelle, y compris des liens et des appels à l’action, et les consommateurs sont davantage protégés contre les messages indésirables. 

Tous les clients qui ont et/ou utilisent actuellement des codes longs américains pour envoyer des messages à des clients américains doivent obligatoirement enregistrer leurs codes longs pour 10DLC. Ce processus de candidature prend 4 à 6 semaines. Pour en savoir plus sur les spécificités du 10DLC et les raisons pour lesquelles il est nécessaire, consultez notre article dédié au [10DLC]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/10dlc/).

## Foire aux questions

### Comment le débit des messages RCS se compare-t-il à celui des messages SMS ?

Le débit des messages RCS n'est pas aussi strictement défini ou contrôlé par l'opérateur qu'il ne l'est pour les SMS. Comme les messages RCS sont envoyés sur des réseaux de données plutôt que sur les canaux de communication cellulaires traditionnels utilisés par les SMS, le RCS ne dépend pas de limites fixes imposées par le réseau, comme c'est le cas pour les SMS. 

### Les expéditeurs vérifiés par le RCS supportent-ils un débit de messages élevé comme un code court ?

Non. Les expéditeurs vérifiés par le RCS n'ont pas la possibilité de bénéficier d'un débit de messages élevé distinct.

### Un expéditeur vérifié par le RCS peut-il être partagé entre plusieurs groupes d'abonnement ? 

Non. Comme pour un expéditeur de SMS, un expéditeur vérifié par RCS ne peut être utilisé qu'avec un seul groupe d'abonnement.

### Un expéditeur de SMS de secours peut-il être partagé entre plusieurs groupes d'abonnement ?

Non. Les expéditeurs de SMS de secours ne peuvent être utilisés qu'avec un seul groupe d'abonnement.


