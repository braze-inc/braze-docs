---
nav_title: Validação de e-mail
article_title: Validação de e-mail
alias: "/email_validation/"
page_order: 3
page_type: reference
description: "Este artigo de referência aborda as regras de validação de parte local e de host para endereços de e-mail."
channel: email

---

# Validação de e-mail

> Este artigo de referência aborda as regras de validação de parte local e de host para endereços de e-mail. A validação é usada para endereços de e-mail do painel, endereços de e-mail do usuário final (seus clientes) e endereços de origem e de destino de uma mensagem de e-mail.

## Como funciona

A validação de e-mail é realizada quando o endereço de e-mail de um usuário foi atualizado ou está sendo importado para o Braze usando a API, o upload de CSV ou o SDK, ou modificado no painel. Observe que seus endereços de e-mail não podem incluir espaços em branco. Se você estiver usando a API, os espaços em branco resultarão em um erro `400`.

O Braze não aceita determinados caracteres e os reconhece como inválidos. Se um e-mail for devolvido, o Braze marcará o e-mail como inválido e o status da assinatura não será alterado. Observe que, se houver caracteres [ASCII](https://en.wikipedia.org/wiki/ASCII) não padrão no corpo do e-mail, o e-mail não será enviado.

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

Essa validação não deve ser confundida com um serviço de validação. Essa é uma verificação para verificar se a sintaxe de um endereço de e-mail está correta. Um dos principais motivos para usar esse processo de validação é o suporte a caracteres internacionais (como UTF-8) na parte local do endereço de e-mail.

A validação da sintaxe de e-mail analisa as partes local e de host de um endereço de e-mail. A parte local é qualquer coisa antes do aspergente (@), e a parte do host é qualquer coisa depois do aspergente. Por exemplo, essa parte local de um endereço de e-mail pode começar e terminar com qualquer um dos caracteres permitidos, exceto um ponto (.). Observe que esse processo está validando apenas a sintaxe do endereço de e-mail e não considera se o domínio tem um servidor MX válido ou se o usuário existe no domínio listado.

{% alert important %}
Se a parte do domínio contiver caracteres ASCII não padrão, ela precisará ser [codificada por Punycode](https://www.punycoder.com/) antes de ser fornecida ao Braze.
{% endalert %}

Se o Braze receber uma solicitação para adicionar um usuário e o endereço de e-mail for considerado inválido, você verá uma resposta de erro na API. Ao fazer o upload com um arquivo CSV, um usuário era criado, mas o endereço de e-mail não era adicionado.

## Regras de validação de peça local

### Validação geral de e-mail

Na maioria dos domínios, a parte local deve seguir esses parâmetros:
- Pode conter qualquer letra, número, inclusive letras e números Unicode, bem como os seguintes caracteres: (+) (&) (#) (_) (-) (^) ou (/)
- Pode conter, mas não pode começar ou terminar com o seguinte caractere: (.)
- Não pode conter aspas duplas (")
- Deve ter entre 1 e 64 caracteres de comprimento

A expressão regular a seguir pode ser usada para validar se um endereço de e-mail será considerado válido:
```
/\A([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])(([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~\.]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])*([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}]))?\z/
```

### Endereços do Gmail

Se a parte do domínio for um endereço do Gmail, a parte local deverá ter pelo menos dois caracteres e seguir a validação de expressão regular listada acima.

### Domínios da Microsoft

Se o domínio do host incluir "msn", "hotmail", "outlook" ou "live", a seguinte expressão regular será usada para validar a parte local: `/\A\w[\-\w]*(?:\.[\-\w]+)*\z/i`

A parte local do endereço Microsoft deve seguir esses parâmetros:

- Pode começar com um caractere (a-z), um sublinhado (_), ou um número (0-9).  
- Pode conter qualquer caractere alfanumérico (a-z ou 0-9) ou um sublinhado (_)
- Pode conter os seguintes caracteres: (.) ou (-)
- Não pode começar com um ponto (.)
- Não pode conter dois ou mais pontos consecutivos (.)
- Não pode terminar com um ponto (.)

Observe que o teste de validação verifica se a parte local, que precede o "+", corresponde à expressão regular.

## Regras de validação da parte do host

Endereços IPv4 ou IPv6 não são permitidos na parte do host de um endereço de e-mail. O domínio de nível superior (como .com, .org, .net, etc.) pode não ser totalmente numérico.

A expressão regular a seguir é usada para validar o domínio:<br>
`/^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)+$/i`

O nome do domínio deve seguir esses parâmetros:

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

O rótulo final do domínio deve ser um domínio de primeiro nível (TLD) válido, que é determinado por qualquer coisa após o ponto final (.). Esse TLD deve estar na [lista de TLDs da ICANN](https://data.iana.org/TLD/tlds-alpha-by-domain.txt). O validador de e-mail do Braze verifica apenas se a sintaxe do e-mail está correta de acordo com a expressão regular listada nesta seção. Ele não detecta erros de digitação nem endereços que não existem.

{% alert important %}
O Unicode é aceito somente para a parte local do endereço de e-mail. O Unicode não é aceito para a parte do domínio, mas pode ser codificado em Punycode.
{% endalert %}

