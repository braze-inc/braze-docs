---
nav_title: Geração de código dinâmico
article_title: Geração de código dinâmico Punchh
page_order: 2
description: "Este artigo de referência descreve como usar a geração de código dinâmico Punchh no Braze."
page_type: partner
search_tag: Partner
---

# Geração de código dinâmico com o Punchh

> Um código de cupom é um código exclusivo que pode ser usado por um único usuário (uso único ou múltiplo). A estrutura Punchh gera códigos de cupom, que podem ser processados em um app móvel ou no sistema de ponto de venda (POS).

_Essa integração é mantida pela Punchh._

## Sobre a integração

Usando a estrutura de cupom Punchh e o Braze, você pode realizar os seguintes cenários:

- Gere um código de cupom quando o hóspede clicar em um link de geração de cupom em um e-mail: O código do cupom será gerado dinamicamente e exibido em uma página da Web.
- Gere um código de cupom quando o hóspede abrir um e-mail: O código do cupom será gerado dinamicamente e mostrado como uma imagem no e-mail.

## Integração da geração de código de cupom dinâmico

### Etapa 1: Criar uma campanha de cupons

1. Usando uma campanha de cupom Punchh, crie uma campanha de cupom de geração dinâmica, conforme mostrado na imagem a seguir.
2. A estrutura de cupons do Punchh gerará os seguintes parâmetros para ativar a geração dinâmica de cupons:
    - Token de geração de cupom dinâmico: Esse é um token de segurança gerado pelo sistema para criptografia.
    - URL de geração de cupom dinâmico: Esse URL será incorporado ao e-mail como um link ou imagem, conforme exigido pela empresa.

![O formulário para criar uma campanha de cupom no Punchh.]({% image_buster /assets/img/punchh/punchh8.png %}){: style="max-width:60%;"}

### Etapa 2: gerar a assinatura e construir o URL

A biblioteca JWT.IO decodifica, verifica e gera tokens da Web JSON, um método RFC 7519 aberto e padrão do setor para representar reivindicações de forma segura entre duas partes. 

Os seguintes nomes `ClaimType` podem ser usados para garantir a exclusividade de convidados e cupons:

- `campaign_id`representa a ID da campanha Punchh gerada pelo sistema.
- `email`: representa o endereço de e-mail do usuário. 
- `first_name`: captura o nome do usuário. 
- `last_name`Nome do usuário: captura o sobrenome do usuário.

Para usar a API de código de cupom dinâmico da Punchh, um token JWT deve ser construído. Adicione o seguinte modelo Liquid ao seu dashboard do Braze no corpo da mensagem do canal que deseja usar:

{% raw %}
```liquid
{% assign header = '{"alg":"HS256","typ":"JWT"}' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% capture payload_raw %}

{
  "campaign_id": "CAMPAIGN_ID",
  "email": "{{${email_address}}}",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}"
}

{% endcapture %}

{% assign payload = payload_raw | replace: ' ', '' | replace: '\n', '' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign unsigned_token = header | append: "." | append: payload %}

{% assign secret = "DYNAMIC_COUPON_GENERATION_TOKEN" %}

{% assign signature_raw = unsigned_token | hmac_sha256_base64: secret %}

{% assign signature = signature_raw | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign jwt = unsigned_token | append: "." | append: signature %}

```
{% endraw %}


Substitua o seguinte:

| Espaço reservado        | Descrição                                          |
|--------------------|------------------------------------------------------|
| `DYNAMIC_COUPON_GENERATION_TOKEN` | Seu token de geração de cupom dinâmico. |
| `CAMPAIGN_ID`                     | Sua ID de campanha.                     |

### Etapa 3: Anexar o código do cupom ao corpo da mensagem

#### Como fazer um link para a página Web da Punchh

Para criar um link para uma página da Web hospedada pelo Puncch, adicione `{% raw %}{{jwt}}{% endraw %}` ao URL de geração dinâmica [que você criou anteriormente](#step-1-create-a-coupon-campaign-in-punchh). Seu link deve ser semelhante ao seguinte: 

{% raw %}
```
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX?sign={{jwt}}
```
{% endraw %}

Quando um usuário clicar no URL do cupom, ele será redirecionado para uma página da Web hospedada pela Punchh, onde o cupom gerado será exibido.

![Exemplo de mensagem de confirmação depois que um usuário gera com sucesso um código de cupom.]({% image_buster /assets/img/punchh/punchh7.png %})

#### Extração de código via JSON como texto simples

Para retornar uma resposta JSON, acrescente `{% raw %}{{jwt}}{% endraw %}` ao URL de geração dinâmica [que você criou anteriormente](#step-1-create-a-coupon-campaign-in-punchh) e, em seguida, adicione `.json` após o token na string do URL. Seu link deve ser semelhante ao seguinte:

{% raw %}
```liquid
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}}
```
{% endraw %}

Você poderia então aproveitar o [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) para inserir o código como texto simples em qualquer corpo de mensagem. Por exemplo:

{% raw %}
```liquid
{% connected_content https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}} :save punchh_coupon %}
{{punchh_coupon.coupon}}
````
{% endraw %}

#### Como adicionar um link de imagem no conteúdo do e-mail

Para vincular o código do cupom em uma imagem:

1. Acrescente `{% raw %}{{jwt}}{% endraw %}` ao URL de geração dinâmica [que você criou anteriormente](#step-1-create-a-coupon-campaign-in-punchh).
2. Adicione `.png` após o token na string do URL.
3. Incorpore seu link em uma tag HTML {% raw %}`<img>`{% endraw %}.

{% tabs local %}
{% tab exemplo de entrada %}
{% raw %}
```liquid
<img src="https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.png?sign={{jwt}}">
````
{% endraw %}
{% endtab %}

{% tab exemplo de saída %}
![Saída renderizada da tag de imagem do código do cupom.]({% image_buster /assets/img/punchh/punchh9.png %})
{% endtab %}
{% endtabs %}

## Envio de mensagens de erro

| Código de erro | Mensagem de erro | Descrição |
| --- | --- | --- |
| `coupon_code_expired` | Este código promocional expirou | O código é usado após sua data de expiração configurada. |
| `coupon_code_success` | Parabéns, o código promocional foi aplicado com sucesso. | O código é usado com sucesso. |
| `coupon_code_error` | Digite um código promocional válido | O código usado é inválido. |
| `coupon_code_type_error` | Tipo de cupom incorreto. Esse cupom só pode ser resgatado em `%{coupon_type}`. | Quando um código que deveria ser usado no POS é usado no app móvel, esse erro ocorre. |
| `usage_exceeded` | A utilização da campanha desse código de cupom está completa. Por favor, tente da próxima vez. | O uso do código excede o número de usuários autorizados a usá-lo. Por exemplo, se a configuração do dashboard permitir que um código seja usado por 3.000 usuários, e o número de usuários exceder 3.000, esse erro ocorrerá. |
| `usage_exceeded_by_guest` | Esse código promocional já foi processado. | O uso do código por um usuário excede o número de vezes que um usuário pode usá-lo. Por exemplo, a configuração do dashboard permite que um único código seja usado três vezes por um usuário. Se for usado mais do que isso, o erro ocorrerá. |
| `already_used_by_other_guest` | Esse código promocional já foi usado por outro hóspede. | Outro usuário já usou o código. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

