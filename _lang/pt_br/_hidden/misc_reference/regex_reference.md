---
nav_title: Folha de referência de regex
permalink: /regex_cheat_sheet/
hidden: true
---

# Folha de referência de regex

Esta página serve como um guia de referência rápida para expressões regulares, incluindo tokens comuns, metassequências, tokens gerais, constantes de grupo e muito mais.

{% tabs %}
{% tab Tokens comuns %}

| Tokens comuns |
| ------------- |
| Um único caractere de: a, b ou c | `[abc]` |
| Um caractere, exceto: a, b ou c | `[^abc]` |
| Um caractere no intervalo: a-z | `[a-z]` |
| Um caractere que não está no intervalo: a-z | `[^a-z]` |
| Um caractere no intervalo: a-z ou A-Z | `[a-zA-Z]` |
| Qualquer caractere único | `.` |
| Qualquer caractere de espaço em branco | `\s` |
| Qualquer caractere que não seja um espaço em branco | `\S` |
| Qualquer dígito | `\d` |
| Qualquer número sem dígito | `\D` |
| Qualquer caractere de palavra | `\w` |
| Qualquer caractere que não seja uma palavra | `\W` |
| Captura anexa | `(...)` |
| Corresponder a a ou b | `(a|b)` |
| Zero ou um de um | `a?` |
| Zero ou mais de um | `a*` |
| Um ou mais de um | `a+` |
| Exatamente 3 de um | `a{3}` |
| Entre 3 e 6 de um | `a{3,6}` |
| Início da string | `^` |
| Fim da string | `$` |
| Um limite de palavras | `\n` |
| Limite de nenhuma palavra | `\B` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Meta-sequência %}

| Meta-sequência |
| ------------- |
| Quaisquer sequências Unicode, incluindo quebras de linha | `\X` |
| Corresponder a uma unidade de dados | `\C` |
| Novas linhas Unicode | `\R` |
| Caractere de espaço em branco vertical | `\v` |
| Negação de \\v | `\V` |
| Caractere de espaço em branco horizontal | `\h` |
| Negação de \\h | `\H` |
| Redefinir correspondência | `\K` |
| Corresponder ao enésimo subpadrão | `\n` |
| Propriedade Unicode X | `\pX` |
| Negação de \\pX | `\PX` |
| Propriedade Unicode ou categoria de script | `\p{...}` |
| Negação de \\p | `\P{...}` |
| Citar; tratar como liberais | `\Q...|E` |
| Corresponder ao subpadrão 'name' | `\k<name>` | 
| Corresponder ao subpadrão 'name' | `\k'name'` | 
| Corresponder ao subpadrão 'name' | `\k{name}` |
| Corresponder ao enésimo subpadrão | `\gn` | 
| Corresponder ao enésimo subpadrão | `\g{n}` |
| Recursar o enésimo grupo de captura | `\g<n>` |
| Recursar o enésimo grupo de captura | `\g'n'` |
| Corresponder ao enésimo subpadrão anterior relativo | `\g{-n}` |
| Recursar o enésimo subpadrão futuro relativo | `\g<+n>` |
| Corresponder ao enésimo remetente futuro relativo | `\g'+n'` |
| Grupo de captura de nomes recursivos | `'letter'` |
| Corresponder ao grupo de captura "letra" nomeado anteriormente | `\g{letter}` |
| Recursa o grupo de captura de nomes 'letter' | `\g<letter>` |
| Caractere hexadecimal YY | `\xYY` |
| Caractere hexadecimal YYYY | `\x{YYYY}` |
| Caractere octal ddd | `\ddd` |
| Caractere de controle Y | `\cY` |
| Caractere de backspace | `[\b]` |
| Torna qualquer caractere literal | `\` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Tokens gerais %}

| Tokens gerais |
| -------------- |
| Nova linha | `\n` |
| Retorno de carro | `\r` |
| Guia | `\t` |
| Caractere nulo | `\0` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Modificadores de classe de personagem %}

| Modificadores de classe de personagem |
| ------------------------- |
| Um único caractere de: a, b ou c | `[abc]` |
| Um caractere, exceto: a, b ou c | `[^abc]` |
| Um caractere no intervalo: a-z | `[a-z]` |
| Um caractere que não está no intervalo: a-z | `[^a-z]` |
| Um caractere no intervalo: a-z ou A-Z | `[a-zA-Z]` |
| Letras e dígitos | `[:alnum:]` |
| Cartas | `[:alpha:]` |
| Códigos ASCII 0-127 | `[:ascii:]` |
| Espaço ou guia apenas | `[:blank:]` |
| Caracteres de controle | `[:cntrl:]` |
| Dígitos | `[:digit:]` |
| Caracteres visíveis (não espaço) | `[:word:]` |
| Letras minúsculas | `[:xdigit:]` |
| Letras maiúsculas | `[:<:]` |
| Caracteres de palavras | `[:>:]` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Constantes de grupo %}

| Constantes de grupo |
| --------------- |
| Captura tudo o que estiver em seu interior | `(...)` |
| Corresponder a a ou b | `(a|b)` |
| Combine tudo o que está incluído | `(?:...)` |
| Agrupamento atômico (sem captura) | `(?>...)` |
| Número de grupo de subpadrão duplicado | `(?|...)` |
| Comentário | `(?#...)` |
| Para insensibilidade a maiúsculas e minúsculas | `(?i)` |
| Grupo de captura nomeado | `(?'name'...)` |
| Grupo de captura nomeado | `(?<name>...)` |
| Grupo de captura nomeado | `(?P<name>...)` |
| Modificadores em linha | `(?imsxXU)` |
| Declarações condicionais | `(?(1)yes|no)` |
| Declarações condicionais recursivas | `(?(R#)yes|no)` |
| Declaração condicional | `(?(R&name)yes|no)` |
| Condicional de Lookahead | `(?(?=...)yes|no)` |
| Condicional do Lookbehind | `(?(?<=...)yes|no)` |
| Recursar todo o padrão | `(?R)` |
| Recursar o primeiro subpadrão | `(?1)` |
| Recursar o primeiro subpadrão relativo | `(?+1)` |
| Recursar o subpadrão 'name' | `(?&name)` |
| Corresponder ao subpadrão 'name' | `(?P=name)` |
| Recursar o subpadrão 'name' | `(?P>name)` |
| Pré-definição de padrões antes do uso | `(?(DEFINE)...)` |
| Perspectiva positiva | `(?=...)` |
| Antecipação negativa | `(?!...)` |
| Visão positiva | `(?<=...)` |
| Visão negativa | `(?<!...)` |
| Verbo de controle | `(*ACCEPT)` |
| Verbo de controle | `(*FAIL)` |
| Verbo de controle | `(*MARK:NAME)` |
| Verbo de controle | `(*COMMIT)` |
| Verbo de controle | `(*PRUNE)` |
| Verbo de controle | `(*SKIP)` |
| Verbo de controle | `(*THEN)` |
| Modificador de padrão | `(*UTF)` |
| Modificador de padrão | `(*UTF8)` |
| Modificador de padrão | `(*UTF16)` |
| Modificador de padrão | `(*UTF32)` |
| Modificador de padrão | `(*UCP)` |
| Modificador de quebra de linha | `(*CR)` |
| Modificador de quebra de linha | `(*LF)` |
| Modificador de quebra de linha | `(*CRLF)` |
| Modificador de quebra de linha | `(*ANYCRLF)` |
| Modificador de quebra de linha | `(*ANY)` |
| Modificador de quebra de linha | `\R` |
| Modificador de quebra de linha | `(*BSR_ANYCRLF)` |
| Modificador de quebra de linha | `(*BSR_UNICODE)` |
| Modificador de mecanismo regex | `(*LIMIT_MATCH=x)` |
| Modificador de mecanismo regex | `(*LIMIT_RECURSION=d)` |
| Modificador de mecanismo regex | `(*NO_AUTO_POSSESS)` |
| Modificador de mecanismo regex | `(*NO_START_OPT)` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Quantificadores %}

| Quantificadores |
| ----------- |
| Zero ou um de um | `a?` |
| Zero ou mais de um | `a*` |
| Um ou mais de um | `a+` |
| Exatamente 3 de um | `a{3}` |
| 3 ou mais de um | `a{3,}` |
| Entre 3 e 6 de um | `a{3,6}` |
| Quantificador ambicioso | `a*` |
| Quantificador preguiçoso | `a*?` |
| Quantificador de possessivo | `a*+` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Âncoras %}

| Âncoras |
| ------- |
| Início da correspondência | `\G` |
| Início da string | `^` |
| Fim da string | `$` |
| Início da string | `\A` |
| Fim da string | `\Z` |
| Fim absoluto da string | `\z` |
| Um limite de palavras | `\b` |
| Um limite sem palavra | `\B` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab Sinalizadores e modificadores %}

| Sinalizadores e modificadores |
| ------------------- | 
| Global | `g` |
| Multilinha | `m` |
| Diferencia maiúsculas de minúsculas | `l` |
| Ignorar espaços em branco | `x` |
| Linha única | `s` |
| Unicode | `u` |
| Estendido | `X` |
| Ingrato | `U` |
| Âncora | `A` |
| Nomes de grupos duplicados | `J` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Substituição %}

| Substituição |
| ------------ |
| Conteúdo completo da correspondência | `\0` |
| Conteúdo do grupo de captura 1 | `\1 or $1` |
| Conteúdo do grupo de captura `foo` | `${foo}` |
| Valores de substituição hexidecimais | `\x20, \x{06fa}` |
| Guia | `\t` |
| Retorno de carro | `\r` |
| Nova linha | `\n` |
| Alimentação de formulários | `\f` |
| Transformação de maiúsculas | `\U` |
| Transformação de letras minúsculas | `\L` |
| Encerrar qualquer transformação | `\E` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

