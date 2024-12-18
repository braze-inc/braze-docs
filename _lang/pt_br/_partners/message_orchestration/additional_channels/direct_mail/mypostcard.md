---
nav_title: MeuCartãoPostal
article_title: MeuCartãoPostal
page_order: 1
description: "Este artigo de referência descreve a parceria entre Braze e MyPostcard, que permite usar mala direta como um canal adicional para o seu fluxo de trabalho de CRM."
alias: /partners/mypostcard/
page_type: partner
search_tag: Partner

---

# MeuCartãoPostal

> [MyPostcard][1], um aplicativo global líder em cartões postais, capacita você a executar campanhas de mala direta com facilidade, proporcionando uma maneira perfeita e lucrativa de se conectar com seus clientes. 

Use a integração MyPostcard e Braze para enviar facilmente correspondências impressas aos seus clientes.

## Pré-requisitos

| Requisito                      | Descrição                                                                                                             |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Minha conta MyPostcard B2B           | O registro no MyPostcard é necessário para aproveitar esta integração.                                          |
| chave de API B2B e credenciais        | Você pode encontrar sua chave de API e as credenciais na ferramenta de administração B2B do MyPostcard.                                         |
| Campanha B2B MyPostcard aprovada | Para aproveitar esta integração, você precisa configurar uma campanha de mala direta de impressão na ferramenta B2B MyPostcard. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Casos de uso

Para elevar suas campanhas de mala direta, é crucial ir além dos envios em massa tradicionais e integrar a correspondência impressa de forma fluida em seus fluxos de trabalho. Esta abordagem permite que você alcance clientes específicos que optaram por não receber seus e-mails informativos ou cujos e-mails estão marcados como spam. Com o MyPostcard, você pode enviar campanhas de mala direta impressas diretamente pelo Braze.

- Construa fluxos de trabalho intuitivos no Braze, incorporando correspondência impressa como um novo canal poderoso, sem nenhuma experiência técnica.
- Desbloqueie o potencial de correspondências impressas personalizadas com alguns passos simples.
- Beneficie-se de uma implementação simples que é apoiada por suporte personalizado de uma equipe dedicada.

## Integração

Para integrar-se ao MyPostcard, [fazer login ou inscrever-se][2] e criar sua primeira campanha para usá-lo através de [webhooks do Braze][3].

### Etapa 1: Crie seu modelo de webhook do Braze

Crie um modelo de webhook MyPostcard para usar em campanhas futuras ou canvas navegando até **Templates** > **Webhook Templates** na plataforma Braze.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation/), acesse **Engajamento** > **Modelos e mídias** > **Modelos de webhook**.
{% endalert %}

Se você gostaria de criar uma campanha de webhook MyPostcard única ou usar um modelo existente, selecione **Webhook** no Braze ao criar uma nova campanha. Preencha os seguintes campos:

| Campo         | Descrição                                               |
|---------------|-----------------------------------------------------------|
| **URL do webhook** | A URL do webhook conforme mostrado na Ferramenta de Administração B2B.             |
| **Corpo da solicitação** | Texto bruto (formato JSON encontrado na ferramenta de administração B2B).        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Método de solicitação e cabeçalhos

MyPostcard requer um método HTTP juntamente com os seguintes cabeçalhos HTTP a serem incluídos no modelo.

{% raw %}
<table>
  <thead>
    <tr>
      <th><strong>Campo</strong></th>
      <th><strong>Informações</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Método HTTP</strong></td>
      <td><code>POST</code></td>
    </tr>
    <tr>
      <td><strong>Nome de usuário</strong></td>
      <td><code>{{ '&lt;username&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>Senha</strong></td>
      <td><code>{{ '&lt;password&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>Content-Type</strong></td>
      <td><code>application/json</code></td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Corpo da solicitação

Copie o corpo da solicitação exibido na Ferramenta de Administração B2B, em seguida, preencha os espaços reservados com conteúdo usando quaisquer tags de personalização Liquid.

![Compor guia mostrando o corpo JSON e informações do webhook.][4]

### Etapa 2: veja uma prévia da sua solicitação

Em seguida, prévia sua solicitação no painel **Prévia** ou Acessar a guia **Teste**, onde você pode escolher um usuário aleatório, um usuário existente ou criar um usuário personalizado para testar seu webhook. Não se esqueça de salvar seu modelo antes de sair da página!

![Teste de Webhook guia com diferentes campos para validar a implementação.][5]

{% alert important %}
Lembre-se de salvar seu modelo antes de sair da página! <br>Os modelos de webhook atualizados podem ser encontrados na lista **Modelos de webhook salvos** ao criar uma nova [campanha de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}

[1]: https://www.mypostcard.com
[2]: https://www.mypostcard.com/b2b/admin/
[3]: https://www.braze.com/docs/user_guide/message_building_by_channel/webhooks
[4]: {% image_buster /assets/img/mypostcard/mypostcard_compose.jpg %}
[5]: {% image_buster /assets/img/mypostcard/mypostcard_test.jpg %}
