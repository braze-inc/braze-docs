---
nav_title: "Validation de l'e-mail"
article_title: "Validation de l'e-mail"
alias: "/email_validation/"
page_order: 3
page_type: reference
description: "Cet article de référence traite des règles de validation des parties locale et hôte pour les adresses e-mail."
channel: email

---

# Validation de l'e-mail

> Cet article de référence traite des règles de validation des parties locale et hôte pour les adresses e-mail. La validation est utilisée pour les adresses e-mail du tableau de bord, les adresses e-mail des utilisateurs finaux (vos clients) et les adresses de départ et de réponse d'un message e-mail.

## Comment cela fonctionne-t-il ?

La validation de l'e-mail est effectuée lorsque l'adresse e-mail d'un utilisateur a été mise à jour ou est importée dans Braze à l'aide de l'API, du téléchargement CSV ou du SDK, ou encore modifiée dans le tableau de bord. Notez que vos adresses e-mail ne peuvent pas comporter d'espaces. Si vous utilisez l'API, les espaces se traduiront par une erreur `400`.

Braze n'accepte pas certains caractères et les reconnaît comme non valides. Si un e-mail est rejeté, Braze marque l'e-mail comme invalide et le statut de l'abonnement n'est pas modifié. Notez que si le corps de l'e-mail contient des caractères [ASCII](https://en.wikipedia.org/wiki/ASCII) non standard, l'e-mail ne sera pas envoyé.

{% details Accepted characters %}
- Lettres (A-Z)
- Chiffres (0-9)
- Symboles
	- -
	- ^
	- +
	- $
	- '
	- &
	- #
	- /
	- %
	- *
	- =
	- \`
	- \|
	- ~
	- !
	- ?
	- . (uniquement entre des lettres ou d'autres caractères)
{% enddetails %}

{% details Unaccepted characters %}
- Espaces blancs (ASCII et Unicode)
{% enddetails %}

Cette validation ne doit pas être confondue avec un service de validation. Ce contrôle permet de vérifier que la syntaxe d'une adresse e-mail est correcte. L'une des principales raisons d'utiliser ce processus de validation est la prise en charge des caractères internationaux (tels que UTF-8) dans la partie locale de l'adresse e-mail.

La validation de la syntaxe de l'e-mail examine les parties locale et hôte d'une adresse e-mail. La partie locale est tout ce qui précède l'astérisque (@), et la partie hôte est tout ce qui suit l'astérisque. Par exemple, cette partie locale d'une adresse e-mail peut commencer et se terminer par n'importe lequel des caractères autorisés, à l'exception d'un point (.). Notez que ce processus ne valide que la syntaxe de l'adresse e-mail et ne tient pas compte du fait que le domaine dispose d'un serveur MX valide ou que l'utilisateur existe sur le domaine répertorié.

{% alert important %}
Si la partie du domaine contient des caractères ASCII non standard, elle devra être [codée en Punycode](https://www.punycoder.com/) avant d'être fournie à Braze.
{% endalert %}

Si Braze reçoit une demande d'ajout d'un utilisateur et que l'adresse e-mail est considérée comme invalide, vous verrez une réponse d'erreur dans l'API. Lors du téléchargement avec un fichier CSV, un utilisateur est créé, mais l'adresse e-mail n'est pas ajoutée.

## Règles de validation des pièces locales

### Validation générale des e-mails

Pour la plupart des domaines, la partie locale doit respecter ces paramètres :
- Peut contenir n'importe quelle lettre, n'importe quel chiffre, y compris les lettres et les chiffres Unicode ainsi que les caractères suivants : (+) (&) (#) (_) (-) (^) ou (/)
- Peut contenir mais ne peut pas commencer ou se terminer par le caractère suivant : (.)
- Ne peut contenir de guillemets doubles (")
- La longueur doit être comprise entre 1 et 64 caractères

L'expression régulière suivante peut être utilisée pour valider si une adresse e-mail sera considérée comme valide :
```
/\A([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])(([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~\.]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])*([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}]))?\z/
```

### Adresses Gmail

Si la partie domaine est une adresse Gmail, la partie locale doit comporter au moins deux caractères et respecter la validation par expression régulière indiquée ci-dessus.

### Domaines de Microsoft

Si le domaine de l'hôte comprend "msn", "hotmail", "outlook" ou "live", l'expression régulière suivante sera utilisée pour valider la partie locale : `/\A\w[\-\w]*(?:\.[\-\w]+)*\z/i`

La partie locale de l'adresse Microsoft doit respecter ces paramètres :

- Peut commencer par un caractère (a-z), un trait de soulignement (_), ou un chiffre (0-9).  
- Peut contenir n'importe quel caractère alphanumérique (a-z ou 0-9) ou un trait de soulignement. (_)
- Peut contenir les caractères suivants : (.) ou (-)
- Ne peut pas commencer par un point (.)
- Ne peut contenir deux ou plusieurs points consécutifs (.)
- Ne peut se terminer par un point (.)

Notez que le test de validation vérifie si la partie locale, précédant le "+", correspond à l'expression régulière.

## Règles de validation de la partie hôte

Les adresses IPv4 ou IPv6 ne sont pas autorisées dans la partie hôte d'une adresse e-mail. Le domaine de premier niveau (tel que .com, .org, .net, etc.) peut ne pas être entièrement numérique.

L'expression régulière suivante est utilisée pour valider le domaine :<br>
`/^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)+$/i`

Le nom de domaine doit respecter ces paramètres :

- Constitué de deux ou plusieurs étiquettes séparées par des points.
	- Chaque partie d'un nom de domaine est appelée "étiquette". Par exemple, le nom de domaine "example.com" se compose de l'étiquette " example " et de l'étiquette " com ".
- Doit contenir au moins un point (.)
- Ne peut contenir deux périodes consécutives ou plus
- Chaque étiquette séparée par un point doit :
	- Ne contenir que des caractères alphanumériques (a-z ou 0-9) et le trait d'union (-).
	- Commencez par un caractère alphanumérique (a-z ou 0-9)
	- Terminer par un caractère alphanumérique (a-z ou 0-9)
	- Contient de 1 à 63 caractères

### Validation supplémentaire requise

L'étiquette finale du domaine doit être un domaine de premier niveau (TLD) valide, qui est déterminé par tout ce qui se trouve après le point final (.). Ce TLD devrait figurer dans la [liste des TLD de l'ICANN](https://data.iana.org/TLD/tlds-alpha-by-domain.txt). Le validateur d'e-mail de Braze vérifie uniquement que la syntaxe de l'e-mail est correcte selon l'expression régulière listée dans cette section. Il ne détecte pas les fautes de frappe ou les adresses qui n'existent pas.

{% alert important %}
L'Unicode n'est accepté que pour la partie locale de l'adresse e-mail. L'Unicode n'est pas accepté pour le domaine, mais il peut être codé en Punycode.
{% endalert %}

