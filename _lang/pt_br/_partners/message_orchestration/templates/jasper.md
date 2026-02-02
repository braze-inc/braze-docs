---
nav_title: Jasper
article_title: Jasper
description: "Este artigo de referência descreve a integração entre o Braze e o Jasper."
alias: /partners/jasper/
page_type: partner
search_tag: Partner
---

# Jasper 

> [O Jasper](https://www.jasper.ai/) é uma plataforma de conteúdo com IA que permite que sua marca crie, gerencie e dimensione conteúdo de alta qualidade e de acordo com a marca em vários canais, incluindo blogs, anúncios e redes sociais.

_Essa integração é mantida pela Jasper._

## Visão geral

A integração entre Jasper e Braze permite que você otimize a criação de conteúdo e a execução de campanhas. Com o Jasper, suas equipes de marketing podem gerar textos de alta qualidade e de acordo com a marca em minutos. O Braze facilitará o envio dessas mensagens para o público certo no momento ideal. Essa integração promove fluxos de trabalho contínuos, reduz o esforço manual e gera resultados de engajamento mais sólidos.

Os benefícios de usar essa integração incluem:

- **Execução rápida da campanha:** Lance campanhas em minutos, não em semanas.
- **Voz consistente da marca:** Use os modelos Jasper para garantir que a cópia gerada siga estritamente as diretrizes da marca.
- **Geração de conteúdo direcionado:** Crie envios de mensagens altamente personalizados com segmentos de público, guias de estilo e itens de conhecimento proprietários.
- **Personalização dinâmica:** Use placeholders Liquid, como {% raw %}```{{${first_name}}}```{% endraw %}, para personalização escalonável no Braze.
- **Redução de erros:** Os fluxos de trabalho automatizados minimizam os erros de copiar e colar e reduzem as etapas manuais.

## Pré-requisitos

| Requisito   | Descrição  |
| ------------------- | ---------------- |
| Conta Jasper      | Você precisa de uma conta Jasper para utilizar essa parceria. |
| Chave da API REST do Braze  | Uma chave da API REST do Braze com as seguintes permissões. <br>  <br>`templates.email.create` <br> `templates.email.update` <br>`content_blocks.create` <br>`content_blocks.update` <br><br>Essa chave pode ser gerada no dashboard do Braze, navegando até **Configurações > Chaves de API**.  |
| Ponto de extremidade REST do Braze | Sua URL de endpoint REST. Seu endpoint específico depende do URL do Braze para sua instância. Consulte o site [Braze API Basics: Endpoints]({{site.baseurl}}/api/basics#endpoints) para obter mais detalhes. |
{: .reset-td-br-1 .rest-td-br-2 role=“presentation” }

## Métodos de integração

Há dois métodos para gerar conteúdo no Jasper e atualizar os modelos do Braze:

1. Use a API do Jasper diretamente
2. Use o Jasper Studio para criar um app personalizado pronto para o Braze

{% tabs %}
{% tab Jasper API %}

## Método: Usar diretamente a API do Jasper

Esse método é ideal para criar e atualizar programaticamente modelos HTML de e-mail no Braze, evitando a configuração manual no Jasper e no Braze.

### Etapa 1: Configurar o Jasper

1. Siga as instruções em [Getting Started](https://developers.jasper.ai/docs/getting-started-1) para gerar sua chave de API do Jasper.
2. Use o modelo pré-criado da Jasper que é otimizado para gerar modelos de e-mail HTML Braze, que tem um ID de modelo `skl_BC53D8AC5B4B47E8BE557EBB706E9B47`.
3. Colete os valores dos seguintes campos, que são necessários para fazer uma solicitação de geração de conteúdo para um modelo de e-mail HTML do Braze.

| Campo | Descrição |
| --- | --- |
| `emailObjective`| Defina claramente o objetivo do e-mail. |
| `ctaLink`| O URL de sua chamada para ação. |
| `unsubscribeLink`| Necessário para envio de e-mails de marketing. |
| `brandColor`| A cor primária de sua marca em formato hexadecimal (por exemplo, `#4dfa8a`). |
{: .reset-td-br-1 .rest-td-br-2 role=“presentation” }

**Campos opcionais**

| Campo | Descrição |
| --- | --- |
|`toneId` | Voz da marca |
| `audienceId`| Segmentação do público |
| `styleId`| Guia de estilo |
| `knowledgeIds` | Contexto de conteúdo aprimorado. Você pode adicionar até três IDs. |
{: .reset-td-br-1 .rest-td-br-2 role=“presentation” }

{: start="4"}
4\. Gere sua saída executando o modelo por meio da API do Jasper. Isso produzirá uma carga útil JSON contendo `subject`, `preheader` e `body` (conteúdo HTML).

{% subtabs %}
{% subtab Sample request %}

### Solicitação de amostra

{% raw %}
```json
curl --location 'https://api.jasper.ai/v1/templates/skl_BC53D8AC5B4B47E8BE557EBB706E9B47/run?toneId=ton_811696974b3c4db4b3ac0041685c3b7c&knowledgeIds=kno_0a62fc17529e4fe69a71f30b6f0e88a7&audienceId=aud_0199117a690a7cc98481f8700916e2a6' \
--header 'Content-Type: application/json' \
--header 'x-api-key: ••••••' \
--data '{
  "inputs": {
    "emailObjective": "Announce a webinar and highlight Jasper + Braze integration benefits. Use {{${firstname}}} in the subject and body. Body length ~400 words. Include CTA buttons for registration and footer with unsubscribe link. Apply brand color to buttons and links.",
    "ctaLink": "https://yourbrand.com/register",
    "unsubscribeLink": "{{${unsubscribe_link}}}",
    "brandColor":"#4dfa8a"
  },
  "options": {
    "outputCount": 1,
    "outputLanguage": "English",
    "inputLanguage": "English",
    "languageFormality": "less"
  }
}'
```
{% endraw %}

{% endsubtab %}
{% subtab Sample output %}

### Saída de amostra
```
{
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}
```
{% endsubtab %}
{% endsubtabs %}

### Etapa 2: Configurar o Braze

Usando os endereços `subject`, `preheader` e `body` gerados pelo Jasper na etapa 1, faça uma solicitação POST à API REST do Braze para [criar um novo modelo de e-mail]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/). Certifique-se de que sua chave da API REST do Braze tenha as permissões `templates.email.create` e `templates.email.update`.

### Exemplo de solicitação da API do Braze para criar um modelo de e-mail

```json
curl --location --request POST 'https://rest.iad-03.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_BRAZE_API_KEY>' \
--data '{
  "template_name": "email_template_jasperapi_20231104T142300Z",
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}'
```
{% endtab %}
{% tab Jasper Studio %}

## Método: Crie um app personalizado pronto para o Braze com o Jasper Studio

O Jasper Studio é uma plataforma sem código dentro do Jasper que lhe permite criar apps de IA personalizados sem precisar de suporte de TI. Você pode criar um app personalizado que gere estruturas JSON formatadas especificamente para a API do Braze ou gerar conteúdo que possa ser adicionado manualmente às suas mensagens no app.

1. Na tela inicial do Jasper, selecione **Create an App (Criar um aplicativo**).
2. Especifique o app que deseja criar, como **Braze HTML Email Template** ou **Content Block Template**.
3. Edite os campos de prompt de entrada que o Jasper gera. Para um modelo de e-mail HTML, você pode incluir formulários de entrada para a linha de assunto, pré-cabeçalho, corpo HTML, tags, alternância de CSS em linha e o nome do modelo.
4. Integrar incorporações de conhecimento com orientação sobre as práticas recomendadas da Liquid para personalização consistente e conteúdo dinâmico.
5. Refinar as instruções fornecidas ao Modelo de Linguagem Grande (LLM) para a geração de conteúdo.
6. Forneça um exemplo da saída desejada, que pode incluir uma saída JSON automatizada formatada para cargas úteis do Braze.
7. Gerar e exportar o seguinte:
- **Copiar/colar diretamente:** O conteúdo pode ser copiado e colado diretamente na plataforma Braze.
- **Saída JSON:** Gerar saída JSON. Essa carga útil pode ser usada para chamar diretamente o endpoint do Braze por meio do site `curl` ou do middleware, ou integrada ao seu fluxo de trabalho de operações de e-mail.

![Aplicativo personalizado Jasper Braze.]({% image_buster /assets/img/jasper/jasper_custom_app.png %})

{% subtabs %}
{% subtab Sample JSON output (custom app) %}

## Exemplo de saída JSON (app personalizado)

{% raw %}
```json
{
  "template_name": "email_webinar_2025",
  "subject": "Join Our Webinar, {{${firstname}}}!",
  "preheader": "Unlock the potential of seamless integration.",
  "body": "<html> ... </html>",
  "tags": ["jasperapi"],
  "should_inline_css": true
}
```
{% endraw %}

{% endsubtab %}
{% subtab Sample Braze API request (using custom app output) %}

## Exemplo de solicitação da API do Braze (usando a saída do app personalizado)

{% raw %}
```json
curl --location --request POST 'https://rest.iad-03.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_BRAZE_API_KEY>' \
--data '{
  "template_name": "email_template_jasperapi_20231104T142300Z",
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}'
```
{% endraw %}

{% endsubtab %}
{% endsubtabs %}

Como alternativa, se você for um profissional de marketing, poderá criar seu app personalizado para se alinhar às diretrizes da marca e gerar conteúdo sem HTML e sem copiar e colar, e usar os modelos do Braze para estilização.

{% endtab %}
{% endtabs %}

{% alert note %}
Para obter assistência adicional, consulte a [documentação da API do Jasper](https://developers.jasper.ai/reference/gettemplate-1) e a [Central de Ajuda do Jasper Studio](https://help.jasper.ai/hc/en-us/articles/36783295610395-Jasper-Studio).
{% endalert %}
