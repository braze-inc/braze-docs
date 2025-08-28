---
nav_title: Validation des e-mails 
article_title: Validation des e-mails
alias: "/email_validation/"
page_order: 3
page_type: reference
description: "Le présent article de référence couvre les règles de validation des pièces locales et hôtes pour les adresses e-mail."
channel: email

---

# Validation de l’e-mail

> Le présent article de référence couvre les règles de validation des pièces locales et hôtes pour les adresses e-mail. La validation est utilisée pour les adresses e-mail du tableau de bord, les adresses e-mail des utilisateurs finaux (vos clients) et les adresses de départ et de réponse d'un message e-mail.

## Fonctionnement

La validation de l'e-mail est effectuée lorsque l'adresse e-mail d'un utilisateur a été mise à jour ou est en cours d'importation dans Braze via l'API, le téléchargement de CSV ou le SDK, ou modifiée dans le tableau de bord. Notez que vos adresses e-mail ne peuvent pas contenir d'espaces. Si vous utilisez l'API, les espaces entraîneront une erreur `400`.

Braze n'accepte pas certains caractères et les reconnaît comme invalides. Si un e-mail est renvoyé, Braze marque l’adresse e-mail comme non valide et le statut d’abonnement n’est pas modifié.  

{% details Caractères acceptés %}
- Lettres (A-Z)
- Nombres (0-9)
- Symboles
	- -
	- ^
	- +
	- $
	- ''
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
	- (seulement entre les lettres ou d'autres caractères)
{% enddetails %}

{% details Caractères non acceptés %}
- Espaces blancs (ASCII et Unicode)
{% enddetails %}

Cette validation ne doit pas être confondue avec un service de validation comme Briteverify. Il s’agit d’un contrôle pour vérifier que la syntaxe d’une adresse e-mail est correcte. L'un des principaux moteurs de l'utilisation de ce processus de validation est de prendre en charge les caractères internationaux (tels que UTF-8) dans la partie locale de l'adresse e-mail.

La validation de syntaxe par e-mail examine les parties locales et hôtes d’une adresse e-mail. La partie locale est tout ce qui est avant le symbole arobase (@), et la partie hôte est ce qui se situe après l’arobase. Par exemple, cette partie locale d'une adresse e-mail peut commencer et se terminer par n'importe lequel des caractères autorisés, sauf par un point (.). Notez que ce processus ne valide que la syntaxe de l’adresse e-mail et ne détermine pas si le domaine dispose d’un serveur MX valide ou si l’utilisateur existe sur le domaine répertorié.

{% alert note %}
Si la partie domaine contient des caractères non-[ASCII](https://en.wikipedia.org/wiki/ASCII), elle devra être [encodée en Punycode](https://www.punycoder.com/) avant d'être fournie à Braze.
{% endalert %}

Si Braze reçoit une demande d'ajout d'un utilisateur et que l'adresse e-mail est considérée comme invalide, vous verrez une réponse d'erreur dans l'API. Lors du téléchargement via CSV, un utilisateur sera créé, mais l’adresse e-mail ne sera pas ajoutée.

## Règles de validation des parties locales

### Validation générale des e-mails

Pour la plupart des domaines, la partie locale doit suivre ces paramètres :
- Peut contenir n'importe quelle lettre, chiffre, y compris les lettres et chiffres Unicode ainsi que les caractères suivants : (+) (&) (#) (_) (-) (^) ou (/)
- Peut contenir mais ne peut pas commencer ou se terminer par le caractère suivant : (.)
- Ne peut pas contenir de guillemets doubles (")
- Doit comporter entre 1 et 64 caractères


L'expression régulière suivante peut être utilisée pour vérifier si une adresse e-mail sera considérée comme valide :
```
/\A([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])(([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~\.]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])*([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}]))?\z/
```

### Adresses Gmail

Si la partie domaine est une adresse Gmail, la partie locale doit comporter au moins deux caractères et doit suivre la validation par expression régulière indiquée ci-dessus.

### Domaines Microsoft

Si le domaine hôte inclut « msn », « hotmail », « outlook » ou « live », alors l’expression régulière suivante sera utilisée pour valider la partie locale : `/\A\w[\-\w]*(?:\.[\-\w]+)*\z/i`

La partie locale de Microsoft doit suivre ces paramètres :

- Peut commencer par un caractère (a-z), un soulignement (_), ou un chiffre (0-9).  
- Peut contenir tout caractère alphanumérique (a-z ou 0-9) ou un soulignement (_).
- Peut contenir les caractères suivants : (.) ou (-) ou (+) ou (^).
- Ne peut pas commencer par un point (.)
- Ne peut pas contenir deux points consécutifs ou plus (.)
- Impossible de terminer par un point (.)

Prenez en compte le fait que le test de validation vérifie si la partie locale, avant le « + », correspond à l’expression régulière.

## Règles de validation de la partie hôte

Les adresses Ipv4 ou Ipv6 ne sont pas autorisées dans la partie hôte d’une adresse e-mail. Le domaine de premier niveau (tel que .com, .org, .net, etc.) ne peut pas être entièrement numérique.

L'expression régulière suivante est utilisée pour valider le domaine :<br>
`/^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)+$/i`

Le nom de domaine doit suivre ces paramètres :

- Se compose de deux étiquettes séparées par un point ou plus
	- Chaque partie d'un nom de domaine est appelée un « label ». Par exemple, le nom de domaine « example.com » se compose du libellé « exemple » et du libellé « com ».
- Doit contenir au moins un point (.)
- Ne peut pas contenir deux points consécutifs ou plus
- Chaque étiquette séparée par un point doit :
	- Ne contenir que des caractères alphanumériques (a-z ou 0-9) et le tiret (-)
	- Commencer par un caractère alphanumérique (a-z ou 0-9)
	- Se terminer par un caractère alphanumérique (a-z ou 0-9)
	- Contenir 1 à 63 caractères

### Validation supplémentaire requise

L’étiquette finale du domaine doit être un domaine de niveau supérieur (TLD) valide déterminé par quelque chose après le point final (.). Ce TLD devrait figurer dans la [liste des TLD de l'ICANN](https://data.iana.org/TLD/tlds-alpha-by-domain.txt). Le validateur d'e-mails Braze vérifie uniquement que la syntaxe de l'e-mail est correcte selon l'expression régulière répertoriée dans cette section. Il ne détecte pas les fautes ou les adresses qui n’existent pas.

{% alert important %}
L’unicode est accepté uniquement pour la partie locale de l’adresse e-mail. L’unicode n’est pas accepté pour la partie domaine, mais il peut être encodé en Punycode.
{% endalert %}

