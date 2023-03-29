---
nav_title: Validation des e-mails 
article_title: Validation des e-mails
alias: "/email_validation/"
page_order: 3
page_type: reference
description: "Le présent article de référence couvre les règles de validation des pièces locales et hôtes pour les adresses e-mail."
channel: email

---

# Envoyer les directives et notes techniques par e-mail

> Le présent article de référence couvre les règles de validation des pièces locales et hôtes pour les adresses e-mail.

## Validation de l’e-mail

La validation est utilisée pour les adresses e-mail du tableau de bord, les adresses e-mail de l’utilisateur final (vos clients), ainsi que les adresses de réponse et de réponse effectuées par e-mail. La validation par e-mail est effectuée lorsque l’adresse e-mail d’un utilisateur a été mise à jour ou est importée dans Braze via API, chargement de CSV, SDK ou modifiée dans le tableau de bord. Prenez en compte le fait que les adresses e-mail ne peuvent pas comprendre d’espace et que, si elles sont envoyées à l’aide de l’API, les espaces entraîneront une erreur `400`.

Les adresses e-mail ciblées par les serveurs Braze doivent être validées selon les standards [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822). Braze n’accepte pas certains caractères et les considère comme invalides. Si un e-mail est renvoyé, Braze marque l’adresse e-mail comme non valide et le statut d’abonnement n’est pas modifié. 

{% details Caractères non acceptés en dehors des normes RFC %}
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

Cette validation ne doit pas être confondue avec un service de validation comme Briteverify. Il s’agit d’un contrôle pour vérifier que la syntaxe d’une adresse e-mail est correcte. L’un des principaux facteurs d’utilisation de ce nouveau processus de validation est de prendre en charge les caractères internationaux (c.-à-d. UTF-8) dans la partie locale de l’adresse e-mail.

La validation de syntaxe par e-mail examine les parties locales et hôtes d’une adresse e-mail. La partie locale est tout ce qui est avant le symbole arobase (@), et la partie hôte est ce qui se situe après l’arobase. Notez que ce processus ne valide que la syntaxe de l’adresse e-mail et ne détermine pas si le domaine dispose d’un serveur MX valide ou si l’utilisateur existe sur le domaine répertorié.

{% alert note %}
Si la partie du domaine contient des caractères non [ASCII](https://en.wikipedia.org/wiki/ASCII), elle devra être [codée en Punycode](https://www.punycoder.com/) avant d’être fournie à Braze.
{% endalert %}

Si Braze reçoit une demande d’ajout d’un utilisateur et que l’adresse e-mail est considérée comme invalide, vous verrez une réponse d’erreur dans l’API. Lors du téléchargement via CSV, un utilisateur sera créé, mais l’adresse e-mail ne sera pas ajoutée.

## Règles de validation des parties locales

### Domaines Microsoft

Si le domaine hôte inclut « msn », « hotmail », « outlook » ou « live », alors l’expression régulière suivante sera utilisée pour valider la partie locale :<br>
`/\A\w[\-\w]*(?:\.[\-\w]+)*\z/i`

La partie locale de Microsoft doit suivre ces paramètres :

- Peut commencer par un caractère (a-z), un trait de soulignement (_) ou un nombre (0-9).  
- Peut contenir un caractère alphanumérique (a-z ou 0-9) ou un trait de soulignement (_)
- Peut contenir les caractères suivants (.), (-) ou (+)
- Impossible de commencer par un point (.) ou un tiret (-)
- Ne peut pas contenir deux points consécutifs ou plus (.)
- Impossible de terminer par un point (.)

Prenez en compte le fait que le test de validation vérifie si la partie locale, avant le « + », correspond à l’expression régulière.

### Tous les autres domaines

Pour tous les autres domaines, Braze permet des adresses e-mail correspondant aux expressions régulières suivantes pour la partie locale :<br>
`/\A [\p{L}\p{N}_\-] (?: [\.\+\'\p{L}\p{N}_&#\/\-]* [\p{L}\p{N}_\-] )? \z/x`

La partie locale de Microsoft doit suivre ces paramètres :
- Peut contenir toute lettre, numéro, trait de soulignement ou tiret, y compris les lettres et numéros Unicode
- Peut contenir, mais ne peut pas commencer ou se terminer par les caractères suivants : (.) (+) (&) (#) (/) ou (")

{% alert important %}
Si la partie de domaine est une adresse Gmail, la partie locale doit comporter au moins cinq caractères. Ceci s’ajoute à la validation de l’expression régulière indiquée dans cette section.
{% endalert %}

## Règles de validation de la partie hôte

Les adresses Ipv4 ou Ipv6 ne sont pas autorisées dans la partie hôte d’une adresse e-mail. De plus, le domaine de niveau supérieur (par ex.,.com,.org,.net, etc.) peut ne pas être entièrement numérique.

L’expression régulière suivante est utilisée pour valider le domaine :<br>
`/^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)+$/i`

Le nom de domaine doit suivre ces paramètres :

- Se compose de deux étiquettes séparées par un point ou plus
	- (Chaque partie d’un nom de domaine est appelée « étiquette ». Par exemple, le nom de domaine « exemple.com » comprend l’étiquette « exemple » et l’étiquette « com ».)
- Doit contenir au moins un point (.)
- Ne peut pas contenir deux points consécutifs ou plus
- Chaque étiquette séparée par un point doit :
	- Ne contenir que des caractères alphanumériques (a-z ou 0-9) et le tiret (-)
	- Commencer par un caractère alphanumérique (a-z ou 0-9)
	- Se terminer par un caractère alphanumérique (a-z ou 0-9)
	- Contenir 1 à 63 caractères

### Validation supplémentaire requise

L’étiquette finale du domaine doit être un domaine de niveau supérieur (TLD) valide déterminé par quelque chose après le point final (.). Ce TLD doit être dans [Liste TLD ICANN][2]. Le validateur e-mail Braze garantit uniquement que la syntaxe de l’e-mail est correcte conformément à l’expression régulière répertoriée dans cette section. Il ne détecte pas les fautes ou les adresses qui n’existent pas.

{% alert important %}
L’unicode est accepté uniquement pour la partie locale de l’adresse e-mail. L’unicode n’est pas accepté pour la partie domaine, mais il peut être encodé en Punycode. 
{% endalert %}

[2]: https://data.iana.org/TLD/tlds-alpha-by-domain.txt
