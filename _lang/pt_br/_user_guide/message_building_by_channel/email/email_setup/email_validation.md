---
nav_title: Validação de e-mail
article_title: Validação de e-mail
alias: "/email_validation/"
page_order: 3
page_type: reference
description: "Este artigo de referência aborda as regras de validação da parte local e do host para endereços de e-mail."
channel: email

---

# Validação de e-mail

> Este artigo de referência aborda as regras de validação da parte local e do host para endereços de e-mail. A validação é usada para endereços de e-mail do dashboard, endereços de e-mail do usuário final (seus clientes) e endereços de origem e de resposta de uma mensagem de e-mail.

## Como funciona?

O Braze valida um endereço de e-mail quando é atualizado, importado por API, upload de CSV, SDK ou modificado no dashboard. Endereços de e-mail não podem incluir espaços em branco. Se você usar a API, espaços em branco retornam um erro `400`.

O Braze rejeita certos caracteres e marca o endereço como inválido. Se um e-mail retornar, o Braze marca o endereço como inválido e não altera o status da inscrição. Se o corpo do e-mail contiver caracteres [ASCII](https://en.wikipedia.org/wiki/ASCII) não padrão, o Braze não envia o e-mail.

{% details Accepted characters %}
- Letras (A-Z)
- Números (0-9)
- Símbolos
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
	- . (somente entre letras ou outros caracteres)
{% enddetails %}

{% details Unaccepted characters %}
- Espaços em branco (ASCII e Unicode)
{% enddetails %}

Essa validação é uma verificação de sintaxe, não um serviço de validação. Um dos objetivos desse processo é suportar caracteres internacionais (como UTF-8) na parte local do endereço de e-mail.

O Braze valida a sintaxe tanto para a parte local quanto para a parte do host de um endereço de e-mail. A parte local é qualquer coisa antes do asperand (@); a parte do host é qualquer coisa depois. A parte local pode começar e terminar com qualquer caractere permitido, exceto um ponto (.). Esse processo não considera se o domínio tem um servidor MX válido ou se um usuário existe nesse domínio.

{% alert important %}
Se a parte do domínio contiver caracteres ASCII não padrão, precisará ser [Punycode-encoded](https://www.punycoder.com/) antes de ser fornecida ao Braze.
{% endalert %}

Se o Braze receber um pedido para adicionar um usuário com um endereço de e-mail inválido, a API retorna um erro. Para um upload de CSV, o Braze cria o usuário, mas omite o endereço de e-mail inválido.

## Regras de validação de peça local

### Validação geral de e-mail

Na maioria dos domínios, a parte local deve seguir esses parâmetros:
- Pode conter qualquer letra, número, incluindo letras e números Unicode, bem como os seguintes caracteres: (+) (&) (#) (_) (-) (^) ou (/)
- Pode conter, mas não pode começar ou terminar com o seguinte caractere: (.)
- Não pode conter aspas duplas (")
- Deve ter entre 1 e 64 caracteres de comprimento

A expressão regular a seguir pode ser usada para validar se um endereço de e-mail será considerado válido:
```
/\A([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])(([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~\.]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])*([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}]))?\z/
```

### Endereços do Gmail

Se a parte do domínio for Gmail, a parte local deve ter pelo menos dois caracteres de comprimento e seguir a validação da expressão regular listada acima.

### Domínios da Microsoft

Se o domínio do host incluir "msn", "hotmail", "outlook" ou "live", o Braze usa a seguinte expressão regular para validar a parte local: `/\A\w[\-\w]*(?:\.[\-\w]+)*\z/i`

A parte local do endereço Microsoft deve seguir esses parâmetros:

- Pode começar com um caractere (a-z), um sublinhado (_), ou um número (0-9).  
- Pode conter qualquer caractere alfanumérico (a-z ou 0-9) ou um sublinhado (_)
- Pode conter os seguintes caracteres: (.) ou (-)
- Não pode começar com um ponto (.)
- Não pode conter dois ou mais pontos consecutivos (.)
- Não pode terminar com um ponto (.)

O teste de validação verifica se a parte local antes do "+" corresponde à expressão regular.

## Regras de validação da parte do host

A parte do host não pode ser um endereço IPv4 ou IPv6. O domínio de nível superior (como .com, .org, .net) não pode ser totalmente numérico.

A seguinte expressão regular é usada para validar o domínio:<br>
`/^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)+$/i`

O nome do domínio deve atender a esses parâmetros:

- Consiste em dois ou mais rótulos separados por pontos
	- Cada parte de um nome de domínio é chamada de "rótulo". Por exemplo, o nome de domínio "example.com" consiste no rótulo "example" e no rótulo "com".
- Deve conter pelo menos um ponto (.)
- Não pode conter dois ou mais períodos consecutivos
- Cada rótulo separado por período deve:
	- Contém apenas caracteres alfanuméricos (a-z ou 0-9) e o hífen (-)
	- Comece com um caractere alfanumérico (a-z ou 0-9)
	- Terminar com um caractere alfanumérico (a-z ou 0-9)
	- Contém de 1 a 63 caracteres

### Validação adicional necessária

O rótulo final do domínio deve ser um domínio de nível superior (TLD) válido, determinado por qualquer coisa após o ponto final (.). Este TLD deve aparecer na [lista de TLD da ICANN](https://data.iana.org/TLD/tlds-alpha-by-domain.txt). O validador Braze verifica apenas a sintaxe. Não captura erros de digitação ou endereços inexistentes.

{% alert important %}
O Unicode é aceito apenas para a parte local do endereço de e-mail. O Unicode não é aceito para a parte do domínio, mas pode ser codificado em Punycode.
{% endalert %}

