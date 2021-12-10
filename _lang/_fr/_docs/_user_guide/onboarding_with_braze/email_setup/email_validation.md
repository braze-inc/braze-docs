---
nav_title: Validation de l'email
article_title: Validation de l'email
alias: "/fr/email_validation/"
page_order: 4.5
page_type: Référence
description: "Cet article de référence couvre les règles de validation de la partie locale et hôte pour les adresses e-mail."
channel: Email
---

# Instructions et notes techniques par e-mail

> Cet article de référence couvre les règles de validation de la partie locale et hôte pour les adresses e-mail.

## Validation de l'adresse e-mail

{% alert important %}
La validation est utilisée pour les adresses de messagerie du tableau de bord, les adresses e-mail de l'utilisateur final (vos clients) et les adresses de provenance et de réponse d'un message électronique.
{% endalert %}

La validation de l'e-mail est effectuée quand l'adresse e-mail d'un utilisateur a été mise à jour ou est en cours d'import dans Braze via API, Upload CSV, ou modifié dans le tableau de bord. Braze ajuste automatiquement les adresses e-mail saisies pour supprimer tous les espaces. Les adresses e-mail ciblées via les serveurs Braze doivent être validées par les normes [RFC 2822](http://tools.ietf.org/html/rfc2822). En plus de ces normes, Braze n'accepte pas certains caractères (indiqués ci-dessous) et les reconnaît comme non valides.

{% details Unaccepted characters outside of RFC Standards %}
- *
- /
- ?
- !
- $
- #
- %
- &#94;
- &
- (
- )
- {
- }
- [
- ]
- ~
- ,
{% enddetails %}

Cette validation ne doit pas être confondue avec un service de validation comme Briteverify. Ceci est une vérification pour vérifier que la syntaxe d'une adresse e-mail est correcte. Un des principaux moteurs pour utiliser ce nouveau processus de validation est de prendre en charge les caractères internationaux (i. ., UTF-8) dans la partie locale de l'adresse e-mail.

La validation de la syntaxe par courriel examine à la fois la partie locale et l'hôte d'une adresse e-mail. La partie locale est quelque chose avant le symbole @, et la partie hôte est quelque chose après le symbole @. Notez que ce processus ne valide que la syntaxe de l'adresse e-mail et ne considère pas si le domaine a un serveur MX valide ou si l'utilisateur existe sur le domaine répertorié.

{% alert note %}
Si la partie domaine contient des caractères non[ASCII](https://en.wikipedia.org/wiki/ASCII) , elle devra être [encodée par Punycode](https://www.punycoder.com/) avant d'être fournie à Braze.
{% endalert %}

Si Braze reçoit une demande pour ajouter un utilisateur et que l'adresse e-mail est considérée comme invalide, vous verrez une réponse d'erreur dans l'API. Lors du téléchargement via CSV, un utilisateur serait créé, mais l'adresse e-mail ne serait pas ajoutée.

## Règles de validation de la pièce locale

### Microsoft domains

Si le domaine hôte inclut "msn", "hotmail", "outlook", ou "live", alors la regex suivante sera utilisée pour valider la partie locale :<br> `/\A\w[\-\w]*(?:\. \-\w]+)*\z/i`

La partie locale de l'adresse Microsoft doit suivre ces paramètres :

- Peut commencer par un caractère (a-z), un tiret bas (_), ou un nombre (0-9).
- Peut contenir n'importe quel caractère alphanumérique (a-z ou 0-9) ou un tiret bas (_)
- Peut contenir les caractères suivants (.) ou (-)
- Impossible de commencer par un point (.) ou un tiret (-)
- Ne peut pas contenir deux ou plusieurs périodes consécutives (.)
- Impossible de terminer par une période (.)

### Tous les autres domaines

Pour tous les autres domaines, Braze autorise les adresses e-mail correspondant aux expressions régulières suivantes pour la partie locale :<br> `\A[\p{L}\p{N}_](? [\. +\'\p{L}\p{N}_&#\/\-]*[\p{L}\p{N}_\-])?\z`

La partie locale doit suivre ces paramètres:
- Peut contenir n'importe quelle lettre, chiffre ou trait de soulignement, y compris des lettres et des chiffres Unicode
- Peut contenir mais ne peut pas commencer ou se terminer par les caractères suivants : (.) (+) (&) (#) (/) ou (")
- Peut contenir et se terminer, mais ne peut pas commencer par le caractère suivant : (-)

{% alert important %}
Si la partie domaine est une adresse Gmail, la partie locale doit comporter au moins cinq caractères. Ceci est en plus de la validation par regex spécifiée ci-dessus sous "Tous les autres domaines".
{% endalert %}

## Règles de validation de la pièce hôte

Les adresses IPv4 ou IPv6 ne sont pas autorisées dans la partie hôte d'une adresse email. De plus, le domaine de premier niveau (par exemple, .com, .org, .net, etc.) peut ne pas être entièrement numérique.

L'expression régulière suivante est utilisée pour valider le domaine :<br> `/^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])+$/i`

Le nom de domaine doit suivre ces paramètres :

- Contient deux ou plusieurs étiquettes séparées par des périodes
    - (Chaque partie d'un nom de domaine est appelée "label". par exemple, le nom de domaine "example.com" se compose de l'étiquette "exemple" et de l'étiquette "com").
- Doit contenir au moins un point (.)
- Ne peut pas contenir deux périodes consécutives ou plus
- Chaque étiquette séparée par des périodes doit:
    - Ne contient que des caractères alphanumériques (a-z ou 0-9) et le trait d'union (-)
    - Commencez par un caractère alphanumérique (a-z ou 0-9)
    - Terminer avec un caractère alphanumérique (a-z ou 0-9)
    - Contient 1 à 63 caractères

**Validation supplémentaire Requise :**<br> L'étiquette finale du domaine doit être un domaine de premier niveau (TLD) valide qui est déterminé par quoi que ce soit après la période finale(.). Ce TLD devrait être dans la [liste TLD d'ICANN][2]. Le validateur d'email Braze s'assure seulement que la syntaxe de l'email est correcte selon les regex énumérés ci-dessus. Il ne détecte pas les fautes de frappe ou les adresses qui n'existent pas.

{% alert important %}
L'Unicode n'est accepté que pour la partie locale de l'adresse email.<br> L'Unicode n'est pas accepté pour la partie domaine, mais il peut être Punycode-encodé.
{% endalert %}

[2]: https://data.iana.org/TLD/tlds-alpha-by-domain.txt
