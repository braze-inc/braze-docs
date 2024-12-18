---
nav_title: Fiche de référence d’expression régulière
permalink: /regex_cheat_sheet/
hidden: true
---

# Fiche de référence d’expression régulière

Cette page sert de guide de référence rapide pour l’expression régulière, y compris les jetons fréquents, les séquences méta, les jetons généraux, les constantes de groupe, etc.

{% tabs %}
{% tab Jetons courants %}

| Jetons courants |
| ------------- |
| Un caractère unique : a, b ou c | `[abc]` |
| Un caractère sauf : a, b ou c | `[^abc]` |
| Un caractère dans la plage : a-z | `[a-z]` |
| Un caractère non compris dans la plage : a-z | `[^a-z]` |
| Un caractère dans la plage : a-z ou A-Z | `[a-zA-Z]` |
| Tout caractère unique | `.` |
| Tout caractère d’espace blanc | `\s` |
| Tout caractère n’étant pas un espace blanc | `\S` |
| Tout chiffre | `\d` |
| Tout caractère autre qu’un chiffre | `\D` |
| Tout caractère de mot | `\w` |
| Tout caractère n’étant pas un mot | `\W` |
| Capture jointe | `(...)` |
| Faire correspondre a ou b | `(a|b)` |
| Zéro ou l’un d’un | `a?` |
| Zéro ou plus d’un | `a*` |
| Un ou plusieurs d’un | `a+` |
| Exactement 3 d’un | `a{3}` |
| Entre 3 et 6 d’un | `a{3,6}` |
| Début de la chaîne de caractères | `^` |
| Fin de la chaîne de caractères | `$` |
| Une limite de mot | `\n` |
| Limite sans mot | `\B` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Séquence méta %}

| Méta-séquence |
| ------------- |
| Toutes les séquences Unicode, sauts de ligne inclus | `\X` |
| Faire correspondre une unité de données | `\C` |
| Nouvelles lignes Unicode | `\R` |
| Caractère d’espace blanc vertical | `\v` |
| Négation de \\v | `\V` |
| Caractère d’espace blanc horizontal | `\h` |
| Négation de \\h | `\H` |
| Réinitialiser la correspondance | `\K` |
| Faire correspondre le nième sous-motif | `\n` |
| Propriété Unicode X | `\pX` |
| Négation de \\pX | `\PX` |
| Propriété Unicode ou catégorie de script | `\p{...}` |
| Négation de \\p | `\P{...}` |
| Guillemet ; traiter comme des libres | `\Q...|E` |
| Faire correspondre le « nom » du sous-motif | `\k<name>` | 
| Faire correspondre le « nom » du sous-motif | `\k'name'` | 
| Faire correspondre le « nom » du sous-motif | `\k{name}` |
| Faire correspondre le nième sous-motif | `\gn` | 
| Faire correspondre le nième sous-motif | `\g{n}` |
| Répéter le nième groupe de capture | `\g<n>` |
| Répéter le nième groupe de capture | `\g'n'` |
| Faire correspondre le nième sous-motif relatif précédent | `\g{-n}` |
| Répéter le nième sous-motif relatif suivant | `\g<+n>` |
| Faire correspondre le nième auteur relatif suivant | `\g'+n'` |
| Groupe de capture des noms récursifs | `'letter'` |
| Faire correspondre la « lettre » du groupe de capture précédemment nommé | `\g{letter}` |
| Répète la « lettre » du groupe de capture des noms | `\g<letter>` |
| Caractère hexadécimal YY | `\xYY` |
| Caractère hexadécimal YYYY | `\x{YYYY}` |
| Caractère octal ddd | `\ddd` |
| Caractère de contrôle Y | `\cY` |
| Caractère de retour arrière | `[\b]` |
| Rend n’importe quel caractère littéral | `\` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Jetons généraux %}

| Jetons généraux |
| -------------- |
| Nouvelle ligne | `\n` |
| Retour chariot | `\r` |
| Tabulation | `\t` |
| Caractère nul | `\0` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Modificateurs de classe de caractères %}

| Modificateurs de classe de caractères |
| ------------------------- |
| Un caractère unique : a, b ou c | `[abc]` |
| Un caractère sauf : a, b ou c | `[^abc]` |
| Un caractère dans la plage : a-z | `[a-z]` |
| Un caractère non compris dans la plage : a-z | `[^a-z]` |
| Un caractère dans la plage : a-z ou A-Z | `[a-zA-Z]` |
| Lettres et chiffres | `[:alnum:]` |
| Lettres | `[:alpha:]` |
| Codes ASCII 0 à 127 | `[:ascii:]` |
| Espace ou tabulation uniquement | `[:blank:]` |
| Caractères de contrôle | `[:cntrl:]` |
| Chiffres | `[:digit:]` |
| Caractères visibles (pas d’espace) | `[:word:]` |
| Lettres minuscules | `[:xdigit:]` |
| Lettres majuscules | `[:<:]` |
| Caractères Word | `[:>:]` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Constantes de groupe %}

| Constantes de groupe |
| --------------- |
| Capture tout ce qui est compris | `(...)` |
| Faire correspondre a ou b | `(a|b)` |
| Faites correspondre tout ce qui est compris | `(?:...)` |
| Regroupement atomique (sans capture) | `(?>...)` |
| Duplique le numéro de groupe de sous-motif | `(?|...)` |
| Commentaire | `(?#...)` |
| Pour l’insensibilité à la casse | `(?i)` |
| Groupe de capture nommé | `(?'name'...)` |
| Groupe de capture nommé | `(?<name>...)` |
| Groupe de capture nommé | `(?P<name>...)` |
| Modificateurs en ligne | `(?imsxXU)` |
| Déclarations conditionnelles | `(?(1)yes|no)` |
| Déclarations conditionnelles récursives | `(?(R#)yes|no)` |
| Déclarations conditionnelles | `(?(R&name)yes|no)` |
| Condition d’anticipation | `(?(?=...)yes|no)` |
| Condition de rappel du passé | `(?(?<=...)yes|no)` |
| Répéter l’ensemble du motif | `(?R)` |
| Répéter le premier sous-motif | `(?1)` |
| Répéter le premier sous-motif relatif | `(?+1)` |
| Répéter le « nom » du sous-motif | `(?&name)` |
| Faire correspondre le « nom » du sous-motif | `(?P=name)` |
| Répéter le « nom » du sous-motif | `(?P>name)` |
| Prédéfinir les motifs avant utilisation | `(?(DEFINE)...)` |
| Anticipation positive | `(?=...)` |
| Anticipation négative | `(?!...)` |
| Rappel du passé positif | `(?<=...)` |
| Rappel du passé négatif | `(?<!...)` |
| Verbe de contrôle | `(*ACCEPT)` |
| Verbe de contrôle | `(*FAIL)` |
| Verbe de contrôle | `(*MARK:NAME)` |
| Verbe de contrôle | `(*COMMIT)` |
| Verbe de contrôle | `(*PRUNE)` |
| Verbe de contrôle | `(*SKIP)` |
| Verbe de contrôle | `(*THEN)` |
| Modificateur de motif | `(*UTF)` |
| Modificateur de motif | `(*UTF8)` |
| Modificateur de motif | `(*UTF16)` |
| Modificateur de motif | `(*UTF32)` |
| Modificateur de motif | `(*UCP)` |
| Modificateur de rupture de ligne | `(*CR)` |
| Modificateur de rupture de ligne | `(*LF)` |
| Modificateur de rupture de ligne | `(*CRLF)` |
| Modificateur de rupture de ligne | `(*ANYCRLF)` |
| Modificateur de rupture de ligne | `(*ANY)` |
| Modificateur de rupture de ligne | `\R` |
| Modificateur de rupture de ligne | `(*BSR_ANYCRLF)` |
| Modificateur de rupture de ligne | `(*BSR_UNICODE)` |
| Modificateur de moteur d’expression régulière | `(*LIMIT_MATCH=x)` |
| Modificateur de moteur d’expression régulière | `(*LIMIT_RECURSION=d)` |
| Modificateur de moteur d’expression régulière | `(*NO_AUTO_POSSESS)` |
| Modificateur de moteur d’expression régulière | `(*NO_START_OPT)` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Quantificateurs %}

| Quantificateurs |
| ----------- |
| Zéro ou l’un d’un | `a?` |
| Zéro ou plus d’un | `a*` |
| Un ou plusieurs d’un | `a+` |
| Exactement 3 d’un | `a{3}` |
| 3 ou plus d’un | `a{3,}` |
| Entre 3 et 6 d’un | `a{3,6}` |
| Quantificateur glouton | `a*` |
| Quantificateur paresseux | `a*?` |
| Quantificateur possessif | `a*+` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Ancres %}

| Ancres |
| ------- |
| Début de la correspondance | `\G` |
| Début de la chaîne de caractères | `^` |
| Fin de la chaîne de caractères | `$` |
| Début de la chaîne de caractères | `\A` |
| Fin de la chaîne de caractères | `\Z` |
| Fin absolue de la chaîne de caractères | `\z` |
| Une limite de mot | `\b` |
| Une limite sans mot | `\B` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab Drapeaux et modificateurs %}

| Indicateurs et modificateurs |
| ------------------- | 
| Global | `g` |
| Multiligne | `m` |
| Sensible à la casse | `l` |
| Ignorer l’espace blanc | `x` |
| Ligne unique | `s` |
| Unicode | `u` |
| Étendu | `X` |
| Non glouton | `U` |
| Ancre | `A` |
| Duplique les noms de groupe | `J` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Substitution %}

| Substitution |
| ------------ |
| Fait complètement correspondre les contenus | `\0` |
| Contenu du groupe de capture 1 | `\1 or $1` |
| Contenu du groupe de capture `foo` | `${foo}` |
| Valeurs de remplacement hexadécimales | `\x20, \x{06fa}` |
| Tabulation | `\t` |
| Retour chariot | `\r` |
| Nouvelle ligne | `\n` |
| Alimentation de formulaire | `\f` |
| Transformation en majuscules | `\U` |
| Transformation en miniscules | `\L` |
| Mettre fin à toute transformation | `\E` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

