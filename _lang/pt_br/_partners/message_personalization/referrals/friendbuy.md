---
nav_title: Friendbuy
article_title: Friendbuy
description: "Aprenda a integrar o Friendbuy com o Braze."
alias: /partners/friendbuy/
page_type: partner
search_tag: Partner

---

# Friendbuy

> Aproveite a integração entre Friendbuy e Braze para expandir suas capacidades de e-mail e SMS enquanto automatiza facilmente suas comunicações de programa de indicação e programa de fidelidade. A Braze gerará perfis de clientes para todos os números de telefone de aceitação coletados via Friendbuy.

_Essa integração é mantida pela Friendbuy._

## Pré-requisitos

Antes de começar, você precisará do seguinte:

| Pré-requisito          | Descrição                                                                                                                              |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Uma conta Friendbuy   | Uma [conta Friendbuy](https://retailer.friendbuy.io/) é necessária para aproveitar esta parceria.                                                              |
| Uma chave da API REST da Braze  | Uma chave da API REST da Braze com `users.track` permissões. Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**.        |
| Um endpoint REST da Braze | [O URL do endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), que depende do URL para sua instância da Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Como integrar a Friendbuy

Na [Friendbuy](https://retailer.friendbuy.io/), acesse **Developer Center** (Centro de desenvolvimento) > **Integrations** (Integrações) e, no cartão de integração da Braze, selecione **Add integration** (Adicionar integração).

![O cartão de integração Braze no Friendbuy.]({% image_buster /assets/img/friendbuy/choosing_braze.png %}){: style="max-width:75%;"}

No formulário, insira seu endpoint REST e chave de API e selecione **Install Integration** (Instalar integração).

![O formulário de integração do Friendbuy.]({% image_buster /assets/img/friendbuy/install_form.png %}){: style="max-width:55%;"}

Volte à sua [conta da Friendbuy](https://retailer.friendbuy.io/) e atualize a página. Se a sua integração foi bem-sucedida, você verá uma mensagem como esta:

![integração instalada]({% image_buster /assets/img/friendbuy/install_success.png %}){: style="max-width:55%;"}

### Atributos personalizados

| Nome do atributo personalizado            | Definição                                                                                                                                         | Tipo de dados |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **Status de indicação da Friendbuy**    | Os indicadores são categorizados como *Defensor*, e os indicados são categorizados como *Amigo indicado*                                                          | String    |
| **Nome do Cliente Friendbuy**      | O nome que o cliente inseriu ao enviar suas informações através de um widget de indicação                                                                 | String    |
| **Link de indicação da Friendbuy**      | Um link de indicação pessoal (PURL) gerado para um Defensor. Por exemplo, https://fbuy.io/EzcW                                                       | String    |
| **Data do Último Compartilhamento do Friendbuy** | A data e hora em que o Advogado compartilhou pela última vez com um Amigo via qualquer canal de compartilhamento. Se o Advogado ainda não compartilhou, a propriedade não estará visível. | Horário      |
| **ID da Campanha Friendbuy**        | O ID da Campanha associado ao link de referência pessoal gerado para um Advogado                                                               | String    |
| **Nome da campanha da Friendbuy**      | O Nome da Campanha associado ao link de referência pessoal gerado para um Advogado                                                             | String    |
| **Código de Cupom Friendbuy**        | O código de cupom de indicação mais recente distribuído ao cliente. Nota: apenas um código será exibido                                            | String    |
| **Valor do cupom da Friendbuy**       | O valor da moeda do código de cupom mais recente distribuído ao cliente.                                                                     | Número    |
| **Estado do Cupom Friendbuy**      | O status do código de cupom mais recente distribuído ao cliente. Nota: o status será 'distribuído' ou 'resgatado'                            | String    |
| **Moeda de Cupom Friendbuy**    | Código da moeda (USD, CAD, etc.) ou porcentagem (%) associada ao código de cupom mais recente distribuído ao cliente.                             | String    |
| **ID da campanha de cupom da Friendbuy** | O ID da Campanha associado ao código do cupom gerado para um cliente.                                                                          | String    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Comportamento padrão

Antes que os dados de cliente possam ser enviados para a Braze, os clientes devem dar aceitação através do widget de indicação, marcando uma ou mais das seguintes caixas:

![widget de referência]({% image_buster /assets/img/friendbuy/referral_widget.png %})

{% alert note %}
Friendbuy usa o padrão internacional (E.164) para verificar números de telefone reais. Números inválidos, como `555-555-5555`, não serão enviados para a Braze.
{% endalert %}

### Comportamento da caixa de seleção

| Caixa de seleção marcada | Comportamento                                                        |
|-------------------|-----------------------------------------------------------------|
| Apenas e-mail        | Apenas o endereço de e-mail do cliente é enviado para a Braze.             |
| Apenas telefone        | Apenas o número de telefone do cliente é enviado para a Braze.              |
| Nenhum           | Nenhum dado de cliente é enviado para a Braze.                              |
| Ambas              | O endereço de e-mail e o número de telefone do cliente são enviados para a Braze. |


