---
nav_title: AMP para e-mail
article_title: AMP para e-mail
alias: /amphtml/
page_order: 11
description: "Este artigo de referência fornece uma visão geral do AMP para e-mail e casos de uso comuns."
channel:
  - email

---

# AMP para e-mail

> Com o [AMP para e-mail](https://amp.dev/about/email), é possível adicionar elementos interativos aos seus e-mails e elevar a comunicação com seus clientes, oferecendo uma experiência completa diretamente na caixa de entrada do usuário. A AMP torna isso possível por meio do uso de vários componentes que podem ser usados para ajudar a criar ofertas interessantes de envio de e-mail, como pesquisas, questionários de feedback, campanhas de votação, avaliações, centros de inscrição e muito mais. Ferramentas como essas podem oferecer oportunidades para aumentar o engajamento e a retenção.

## Solicitações

A Braze não é responsável pelo registro dos usuários no Google ou pelo cumprimento dos requisitos de segurança necessários. O AMP para e-mail está disponível apenas para SparkPost e SendGrid.

| Requisito   | Descrição |
| --------------| ----------- |
| AMP para e-mail ativado | O AMP está disponível para todos os usuários. |
| Capacitação da conta do Gmail | Consulte [Capacitação da conta do Gmail](#enabling-gmail-account). |
| Autenticação de remetente do Google | O Gmail [autentica o remetente](https://developers.google.com/gmail/ampemail/security-requirements#sender_authentication) dos e-mails AMP com DKIM, SPF e DMARC. Eles devem ser configurados para sua conta. <br><br>- [Correio Identificado por Chaves de Domínio](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) (DKIM) <br>- [Estrutura de política de remetente](https://en.wikipedia.org/wiki/Sender_Policy_Framework)(SPF)<br>- [Autenticação, relatório e conformidade de mensagens baseadas em domínio](https://en.wikipedia.org/wiki/DMARC)(DMARC)
| Elementos de e-mail AMP | Um envio de e-mail AMP atraente inclui o uso estratégico de vários componentes. Consulte a guia Essentials na seção [Componentes](#components) abaixo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Clientes de e-mail suportados

Antes de poder enviar e-mails AMP aos usuários, é necessário registrar-se em nossos clientes de e-mail. O processo de registro envolve o envio de um e-mail HTML AMP de teste para ser aprovado. Os tempos de aprovação variam de cliente para cliente. Siga os links de registro para saber mais.

| Cliente | Link de registro |
| ------ | -------- |
| Gmail | [Google](https://developers.google.com/gmail/ampemail/register) |
| FairEmail | [FairEmail](https://email.faircode.eu/) |
| Yahoo | [Yahoo](https://senders.yahooinc.com/amp/) |
| Mail.ru | [Mail.ru](https://postmaster.mail.ru/amp/) |

Para obter uma lista completa dos clientes de e-mail compatíveis, consulte a [documentação do AMP](https://amp.dev/support/faq/email-support).

### Capacitação da conta do Gmail

Acesse as configurações do Gmail e selecione **Ativar e-mail dinâmico** em **Geral**.

![Um exemplo das configurações do Gmail com a caixa de seleção "Ativar e-mail dinâmico" marcada.]({% image_buster /assets/img/dynamic-content.png %})

## Uso da API

Você também pode usar o AMP para envio de e-mail com nossa API. Se você usar qualquer um dos [endpoints do Braze Messaging]({{site.baseurl}}/api/endpoints/messaging/) para enviar um e-mail, adicione `amp_body` como uma especificação de objeto, conforme mostrado abaixo.

### Especificação do objeto de e-mail

```json
{
  "app_id": (required, string) see app identifier above,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <email@address.com>"),
  "reply_to": (optional, valid email address in the format "email@address.com" - defaults to your workspace's default reply to if not set),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "amp_body": (optional, updates the text-amp-html MIME type) the email body in AMP HTML. The MIME (Multipurpose Internet Mail Extensions) type to be referenced is "text/x-amp-html",
  "body": (required unless email_template_id is given, valid HTML),
  "preheader": (optional*, string) Recommended length 50-100 characters,
  "email_template_id": (optional, string) If provided, we will use the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case we will override the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid key-value hash), extra hash - for SendGrid customers, this will be passed to SendGrid as Unique Arguments,
  "headers": (optional, valid key-value hash), hash of custom extensions headers. Currently, only supported for SendGrid customers,
  "should_inline_css": (optional, boolean), whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the workspace,
  "attachments": (optional, array), array of JSON objects like [{"file_name","url"}] that define the files you need attached. Your file name's extension will be detected automatically from the URL, which should return the appropriate `Content-Type` as a response header,
}
```

## Como criar seu e-mail AMP

Primeiro, crie seu e-mail AMP usando [componentes](#components). Em seguida, use a [API da Braze](#api-usage) para enviar sua mensagem, certificando-se de incluir `amp_body` para seu AMP HTML.

Além do HTML AMP, exigimos uma versão HTML regular `body` e sugerimos uma versão `plaintext_body` de seu e-mail AMP. Todos os e-mails AMP são enviados em várias partes, o que significa que a Braze envia um e-mail que suporta HTML, texto simples e AMP HTML. Isso se torna útil caso seu e-mail seja enviado por um provedor de e-mail que ainda não ofereça suporte a AMP para e-mail, pois o e-mail será automaticamente padronizado para a versão apropriada com base no usuário e em seu dispositivo.

{% alert note %}
Quando estiver criando um e-mail AMP, verifique se está no editor de AMP, pois o código AMP não deve ser adicionado ao editor de HTML.
{% endalert %}

Consulte estes recursos adicionais:

- [Tutorial AMP](https://amp.dev/documentation/guides-and-tutorials/start/create_email?format=email)
- [Código de amostra](https://gist.github.com/CrystalOnScript/988c3f0a2eb406da27e9d9bf13a8bf73) para ver como o produto final deve ficar. 
- [Biblioteca de componentes de e-mail AMP](https://amp.dev/documentation/components/?format=email/)

### Componentes

Ao criar os elementos AMP, recomendamos que você verifique com sua equipe de engenharia e inclua recursos e elementos de design para obter uma camada extra de polimento.

{% tabs %}
  {% tab Essenciais %}

Cada um desses elementos é necessário no corpo de seu e-mail AMP.

| Componente | Descrição | Exemplo |
|---------|--------------|---------|
| Identificação <br><br> `⚡4email` ou `amp4email`| Identifica seu e-mail como um e-mail AMP HTML. | `<!doctype html>` <br> `<html ⚡4email>` <br> `<head>` |
| Carregar tempo de execução do AMP <br><br> `<script>` | Permite que o AMP funcione no seu e-mail usando JavaScript. | `<script async src="https://cdn.ampproject.org/v0.js"></script>`|
| Modelo de CSS | Oculta o conteúdo até que o AMP seja carregado. <br> Os provedores de e-mail que oferecem suporte a e-mails AMP aplicam verificações de segurança que só permitem que scripts AMP aprovados sejam executados em seus clientes. | `<style amp4email-boilerplate>body{visibility:hidden}</style>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

  {% endtab %}
  {% tab Dinâmico %}

Use esses componentes para criar layouts e comportamentos dinâmicos em seus e-mails.

| Componente | Descrição | Script necessário |
|---------|--------------|---------|
| [Acordeão](https://amp.dev/documentation/components/amp-accordion?format=email) <br><br> `amp-accordion`| Permite que os usuários visualizem o esboço do conteúdo e saltem para qualquer seção. | `<script async custom-element="amp-accordion" src="https://cdn.ampproject.org/v0/amp-accordion-0.1.js"></script>` |
| [Formulários](https://amp.dev/documentation/components/amp-form?format=email) <br><br> `amp-form`| Crie formulários para enviar campos de entrada em um documento AMP. | `<script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Qualquer componente que exija a autenticação do usuário deve usar [tokens de acesso do Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) ou [tokens de asserção de proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}
  {% endtab %}
  {% tab Creative %}

  Use os componentes da AMP que podem ajudar a adaptar seu e-mail ao seu público.

| Componente | Descrição | Script necessário |
|---------|--------------|---------|
| [Imagem animada](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-anim`| Exibe uma imagem animada (geralmente um GIF) gerenciada pelo tempo de execução. | `<script async custom-element="amp-anim" src="https://cdn.ampproject.org/v0/amp-anim-0.1.js"></script>` |
| [Carrossel](https://amp.dev/documentation/components/amp-carousel?format=email) <br><br> `amp-carousel`| Exibe várias partes semelhantes de conteúdo em um eixo horizontal. | `<script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>` |
| [Imagem](https://amp.dev/documentation/components/amp-img?format=email) | Um substituto gerenciado em tempo de execução para a tag HTML `img`. <br>  Você também pode criar uma [lightbox para sua imagem](https://amp.dev/documentation/components/amp-image-lightbox?format=email). | `<amp-img alt="A view of the sea"` <br> `src="images/sea.jpg"` <br> `width="900"` <br>  `height="675"` <br>  `layout="responsive">`  <br> `</amp-img>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Qualquer componente que exija a autenticação do usuário deve usar [tokens de acesso do Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) ou [tokens de asserção de proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

  {% endtab %}
  {% tab Outros %}

| Componente | Descrição |
|---------|--------------|
| [Vinculação de dados e expressões](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-bind`| Adiciona interatividade personalizada com estado às suas páginas AMP por meio de vinculação de dados e expressões semelhantes a JavaScript. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Qualquer componente que exija a autenticação do usuário deve usar [tokens de acesso do Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) ou [tokens de asserção de proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

{% endtab %}
{% endtabs %}

Para obter uma lista completa dos componentes do AMP, consulte [a documentação do AMP](https://amp.dev/documentation/components/?format=email).  

### Casos de uso

{% tabs local %}
{% tab Pesquisas interativas %}

Usando o componente `<amp-form>`, é possível criar pesquisas interativas que podem ser concluídas sem sair da caixa de entrada do e-mail. Isso pode ser feito usando o site `<amp-form>` para enviar a resposta da pesquisa e, em seguida, fazer com que o backend forneça esses dados agregados. 

Alguns exemplos incluem:
* E-mail da pesquisa da conferência
* Atualização dinâmica de itens no feed
* E-mail do marcador de artigos

Usando esse componente, os usuários podem enviar ou limpar valores de campo. Além disso, dependendo de como você configurar seu e-mail, você pode dar prompts adicionais aos usuários, como se a submissão da pesquisa foi bem-sucedida ou apresentar as respostas dos seus usuários mostrando os resultados da pesquisa (como uma campanha de votação).

{% endtab %}
{% tab Conteúdo dobrável %}

Expanda suas seções de conteúdo usando o componente `<amp-accordion>`. Esse componente permite exibir seções de conteúdo dobráveis e expansíveis, proporcionando uma maneira de os espectadores darem uma olhada no esboço do conteúdo e pularem para qualquer seção. 

Se você tende a enviar artigos educacionais longos ou recomendações personalizadas, isso permite que os espectadores vejam o esboço do conteúdo e acessem qualquer seção ou recomendação específica do produto para obter mais detalhes. Isso pode ser particularmente útil para usuários móveis, onde até mesmo algumas frases em uma seção exigem rolagem.
{% endtab %}
{% tab E-mails com muitas imagens %}

Se você tende a enviar e-mails com muitas fotos profissionais, como as marcas de varejo, pode usar o componente `<amp-image-lightbox>` que permite que os usuários interajam com uma imagem que os atraia. Quando o usuário clica na imagem, esse componente exibe a imagem no centro da mensagem, criando um efeito de lightbox. 

Além disso, o componente `<amp-image-lightbox>` permite que o usuário visualize uma descrição detalhada da imagem. Você pode usar o mesmo componente para mais de uma imagem. Por exemplo, se você tiver várias imagens incluídas no e-mail, quando o usuário clicar em uma delas, a imagem será exibida na lightbox.

{% endtab %}
{% tab Envio de e-mails com fontes %}

Para e-mails que dependem principalmente de cópia de texto, o componente `<amp-fit-text>` permite gerenciar o tamanho e o ajuste do texto em uma área específica.

Os exemplos incluem:

- Dimensionamento do texto para se ajustar a uma área
- Dimensionar o texto para caber na área usando um tamanho máximo de fonte, onde você pode definir o tamanho máximo da fonte
- Truncando o texto quando o conteúdo ultrapassa a área

{% endtab %}
{% endtabs %}

### Usando o amp-mustache

Semelhante ao Liquid, o AMP oferece suporte a uma linguagem de script para casos de uso mais avançados. Esse componente é chamado de [`amp-mustache`](https://amp.dev/documentation/components/amp-mustache/?format=email). Ao incluir qualquer linguagem de marcação do Mustache, você precisará envolvê-la na tag [`raw`](https://shopify.github.io/liquid/tags/raw/) do Liquid. Observe que o Liquid e o Mustache compartilham o estilo de sintaxe. 

Ao envolver seu conteúdo na tag `raw`, o mecanismo de processamento do Braze ignorará qualquer conteúdo entre as tags `raw` e enviará a variável Mustache de que sua equipe precisa.

## Métricas e análise de dados

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrico</th>
            <th>Informações</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">Total de aberturas</td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Opens' %} Para e-mails AMP, isso é o total de aberturas para as versões HTML e texto simples.</td>
        </tr>
        <tr>
            <td class="no-split">Total de cliques</td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Clicks' %} Para emails AMP, este é o total de cliques nas versões HTML e texto simples.</td>
        </tr>
        <tr>
            <td class="no-split">Aberturas de accelerated mobile pages</td>
            <td class="no-split">{% multi_lang_include metrics.md metric='AMP Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split">Cliques de accelerated mobile pages</td>
            <td class="no-split">{% multi_lang_include metrics.md metric='AMP Clicks' %}</td>
        </tr>
    </tbody>
</table>

## Testes e solução de problemas

Note que o total de cliques e os cliques únicos não levam em conta os cliques que ocorrem em uma mensagem AMP (somente HTML e texto simples). Os cliques específicos de AMP são atribuídos à métrica *amp_click*.

Antes de enviar seu e-mail AMP, recomendamos que você faça um teste de acordo com estas [diretrizes do Gmail](https://developers.google.com/gmail/ampemail/testing-dynamic-email).

Para que seu e-mail AMP seja entregue a qualquer conta do Gmail, o e-mail deve atender às seguintes condições:

- Os requisitos de segurança do AMP para e-mail devem ser atendidos.
- A parte AMP MIME deve conter um documento AMP válido.
- O e-mail deve incluir a parte AMP MIME antes da parte HTML MIME.
- A parte AMP MIME deve ser menor que 100 KB.

Se nenhuma dessas condições estiver causando o erro, entre em contato com [o suporte]({{site.baseurl}}/support_contact/).

### Perguntas frequentes

#### Devo segmentar com e-mails AMP?

Defendemos a não segmentação para enviar a todos os tipos diferentes de usuários. Isso ocorre porque enviamos mensagens AMP em multipartes, com diferentes versões incluídas no e-mail original. Se um usuário não puder ver a versão AMP, ela voltará ao padrão HTML. 


