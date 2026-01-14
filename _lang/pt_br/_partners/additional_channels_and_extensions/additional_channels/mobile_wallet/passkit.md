---
nav_title: PassKit
article_title: PassKit
alias: /partners/passkit/
description: "Este artigo de referência descreve a parceria entre a Braze e a PassKit. A parceria permite ampliar o alcance da sua marca em dispositivos móveis por meio da integração de tickets da Apple Wallet e do Google Pay às experiências dos clientes."
page_type: partner
search_tag: Partner

---

# PassKit

> A PassKit permite ampliar o alcance da sua marca em dispositivos móveis por meio da integração de tickets da Apple Wallet e do Google Pay às experiências dos clientes. Crie, gerencie, distribua e analise facilmente a performance de cupons digitais, cartões de fidelidade, cartões de associação, tickets e muito mais, sem que seus clientes precisem de outro app.

_Essa integração é mantida pelo Passkit._

## Sobre a integração

A integração entre a Braze e a PassKit permite que você aumente e meça o engajamento de suas campanhas online, fornecendo instantaneamente passes personalizados da Apple Wallet e do Google Pay. Em seguida, é possível analisar o uso e fazer ajustes em tempo real para aumentar o tráfego na loja, disparando mensagens baseadas no local e atualizações personalizadas e dinâmicas na carteira móvel do cliente. 

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta da PassKit | Você precisará ter uma conta da PassKit e um gerente de conta da PassKit. |
| `userDefinedID` | Para atualizar adequadamente os eventos personalizados e os atributos personalizados para seus usuários entre o Passkit e o Braze, será necessário definir o ID externo do Braze como `userDefinedID`. Este `userDefinedID` será usado ao fazer chamadas de API para os endpoints da PassKit. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Ponto de extremidade REST do Braze  | Sua URL de endpoint REST. Seu endpoint dependerá da [URL do Braze para sua instância]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integração

Para enriquecer ainda mais as experiências de carteira móvel de seus clientes, a partir do painel do PassKit, você pode aceitar passar dados para o Braze por meio do [endpoint]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) Braze [`/users/track`.]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) 

Exemplos de dados para compartilhar do Passkit incluem:
- **Passe criado**: quando um cliente clica em um link de passe e recebe um passe pela primeira vez.
- **Instalações de passe**: quando o cliente adiciona e salva o passe em seu app de carteira.
- **Atualizações de passe**: quando um passe é atualizado.
- **Exclusão do passe**: quando um cliente exclui o passe de seu app de carteira.

Depois que os dados são passados para o Braze, você pode criar públicos, personalizar o conteúdo via Liquid e disparar campanhas ou Canvas depois que essas ações forem executadas.

## Conectar a PassKit à Braze

Para transmitir dados da PassKit, confirme se você definiu sua ID externa da Braze como `externalId` da PassKit.

1. Em **Settings (Configurações**), em **Integrations (Integrações** ) em seu projeto ou programa PassKit Pass, clique em **Connect (Conectar** ) na guia **Braze**.<br>![O bloco de integração do Braze na plataforma PassKit.]({% image_buster /assets/img/passkit/passkit5.png %}){: style="max-width:80%"}<br><br>
2. Informe sua chave de API da Braze, o URL do endpoint e um nome para seu conector.<br><br>
3. Ative **a opção Enable Integration (Ativar integração** ) e os eventos que você deseja que o Braze dispare ou personalize suas mensagens.<br>![O bloco de integração do PassKit Braze foi expandido para aceitar a chave de API, o URL do ponto de extremidade, o nome da integração, as configurações de capacitação, as configurações de associação e as configurações de passe.]({% image_buster /assets/img/passkit/passkit4.png %}){: style="max-width:70%"}

## Criar passe usando um link do SmartPass

No Braze, você pode configurar um link SmartPass para gerar um URL exclusivo para que seus clientes instalem o passe no Android ou no iOS. Para fazer isso, você deve definir uma carga útil de dados SmartPass criptografada que possa ser chamada de um bloco de conteúdo Braze. Esse [bloco de conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks) pode ser reutilizado para futuros passes e cupons. Os itens a seguir serão usados durante sua integração:

- **URL da PassKit**: seu URL da PassKit é um URL exclusivo para seu programa da PassKit.<br>Cada programa tem um URL exclusivo, e você pode encontrá-lo na guia **Distribution** (Distribuição) do seu programa ou projeto da PassKit (por exemplo, https://pub1.pskt.io/c/ww0jir).<br><br>
- **Segredo da PassKit**: junto com o URL, você precisará ter em mãos a chave da PassKit para esse programa.<br>Isso pode ser encontrado na mesma página que o URL da PassKit.<br><br>
- **ID do programa (ou projeto)**: seu ID do programa da PassKit será necessário para criar o URL do SmartPass. <br>Você pode encontrá-lo na guia **Configurações** do seu projeto ou programa.

Para saber mais sobre como criar links SmartPass criptografados, consulte este [artigo do Passkit](https://help.passkit.com/en/articles/3742778-hashed-smartpass-links).

### Etapa 1: defina sua carga útil de dados de passe {#passkit-integrations}

Primeiro defina a carga útil do cupom ou do membro. 

Há muitos componentes diferentes que podem ser incluídos em sua carga útil, mas aqui estão dois importantes a observar:

| Componente | Obrigatória | Tipo | Descrição |
| --------- | -------- | ---- | ----------- |
|`person.externalId` | Obrigatória | String | Definido como o ID externo do Braze, isso é crucial para que os retornos de chamada do Passkit para o Braze funcionem, permitindo que os usuários do Braze tenham cupons para várias ofertas em uma campanha. Não é aplicado como único. |
| `members.member.externalId` | Opcional | String | Definido como o ID externo da Braze; você pode usar seu ID externo para atualizar o passe de inscrição. A definição desse campo impõe que o usuário seja único no programa de inscrição.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

Para obter uma lista completa dos campos disponíveis, seus tipos e descrições úteis, dê uma olhada na [documentação do PassKit no GitHub](https://github.com/PassKit/smart-pass-link-from-csv-generator).

#### Exemplo de carga útil
{% raw %}
```liquid
{
  "members.member.externalId": "{{${user_id}}}",
  "members.member.points": "100",
  "members.tier.name": "current_customer",
  "person.displayName": "{{${first_name}}} {{${last_name}}}",
  "person.externalId": "{{${user_id}}}",
  "universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"
}
```
{% endraw %}

### Etapa 2: Criar e codificar uma variável de carga útil indefinida

Crie e nomeie um novo bloco de conteúdo navegando até **Modelos** > **Blocos de conteúdo** no dashboard do Braze.

Selecione **Create Content Block (Criar bloco de conteúdo** ) para começar.

Em seguida, você deve definir a **Liquid tag do bloco de conteúdo**. Depois que o bloco de conteúdo é salvo, a Liquid tag pode ser consultada ao criar mensagens. Neste exemplo, atribuímos a Liquid tag como {% raw %}`{{content_blocks.${passKit_SmartPass_url}}}`{% endraw %}. 

Nesse bloco de conteúdo, não incluiremos diretamente a carga útil, mas faremos referência a ela em uma variável {% raw %}`{{passData}}`{% endraw %}. O primeiro trecho de código que você deve adicionar ao seu bloco de conteúdo captura uma codificação Base64 da variável {% raw %}`{{passData}}`{% endraw %}.
{% raw %}
```liquid
{% capture base64JsonPayload %}{{passDatapassData|base64_encode}}{% endcapture %}
```
{% endraw %}

### Etapa 3: crie sua assinatura de criptografia usando um hash HMAC SHA1

Em seguida, você criará sua assinatura de criptografia usando um hash [HMAC SHA1](https://en.wikipedia.org/wiki/HMAC) do URL do projeto e da carga útil. 

O segundo trecho de código que você deve adicionar ao seu bloco de conteúdo captura o URL a ser usado para hashing.
{% raw %}
```liquid
{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}
```
{% endraw %}

Em seguida, gere uma assinatura usando esse hash e seu `Project Secret`. Isso pode ser feito com a inclusão de um terceiro trecho de código:
{% raw %}
```liquid
{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}
```
{% endraw %}

Por fim, acrescente a assinatura ao URL completo usando o quinto snippet de código:
{% raw %}
```liquid
{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}{% endcapture %}
```
{% endraw %}

### Etapa 4: imprima o URL

Por fim, chame seu URL final para que ele imprima o URL do SmartPass em sua mensagem.
{% raw %}
```liquid
{{longURL}}
```
{% endraw %}

Nesse ponto, você terá criado um bloco de conteúdo com a seguinte aparência:

{% raw %}
```liquid
{% capture base64JsonPayload %}{{passData|base64_encode}}{% endcapture %}

{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}

{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}

{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}&utm_source=braze&utm_campaign={{campaign.${name}}}{% endcapture %}{% capture longURL %}{{longURL | url_encode}}{% endcapture %}

{{longURL}}
```
{% endraw %}

Nesse exemplo, foram adicionados parâmetros UTM para rastrear a origem dessas instalações até o Braze e essa campanha.

{% alert tip %}
Lembre-se de salvar seu bloco de conteúdo antes de sair da página.
{% endalert %}

### Etapa 5: juntando tudo

Depois que esse bloco de conteúdo for criado, ele poderá ser reutilizado novamente no futuro. 

Você pode notar que há duas variáveis indefinidas no exemplo do bloco de conteúdo.<br> 
{% raw %}`{{passData}}`{% endraw %} - Sua carga útil de dados de passagem JSON definida na [etapa 1](#passkit-integrations) <br>
{% raw %}`{{projectUrl}}`{% endraw %} – o URL do seu projeto ou programa, que pode ser encontrado na guia de distribuição do seu projeto da PassKit.

Essa decisão é proposital e apóia a reutilização do bloco de conteúdo. Como essas variáveis são apenas referenciadas, e não criadas dentro do bloco de conteúdo, elas podem ser alteradas sem que seja necessário refazer o bloco de conteúdo. 

Por exemplo, talvez você queira alterar a oferta introdutória para incluir mais pontos iniciais em seu programa de fidelidade, ou talvez queira criar um cartão ou cupom de membro secundário. Esses cenários exigiriam diferentes `projectURLs` da PassKit ou diferentes cargas úteis de passe, que você definiria por campanha no Braze.  

#### Como redigir o corpo da mensagem

Você deverá capturar essas duas variáveis no corpo da mensagem e, em seguida, chamar o bloco de conteúdo.
Capture sua carga útil JSON minificada da [etapa 1](#passkit-integrations):

**Atribuir o URL do projeto**
{% raw %}
```liquid
{% assign projectUrl = "https://pub1.pskt.io/c/ww0jir" %}
```
{% endraw %}

**Capturar o JSON**
{% raw %}
```liquid
{% capture passData %}{"members.member.externalId": "{{${user_id}}}","members.member.points": "100","members.tier.name": "current_customer","person.displayName": "{{${first_name}}} {{${last_name}}}","person.externalId": "{{${user_id}}}","universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"}{% endcapture %}
```
{% endraw %}

**Faça referência ao bloco de conteúdo que você acabou de criar**
{% raw %}
```liquid
{{content_block.${passkit_SmartPass_url}}}
```
{% endraw %}

O corpo de sua mensagem deve ser semelhante a este:
![Uma imagem do criador de mensagens do bloco de conteúdo com o JSON capturado e a referência do bloco de conteúdo mostrada.]({% image_buster /assets/img/passkit/passkit1.png %}){: style="max-width:70%"}

O URL de saída da amostra é:
![O URL de saída que inclui uma string longa e gerada aleatoriamente de letras e números.]({% image_buster /assets/img/passkit/passkit2.png %}){: style="max-width:70%"}

O URL de saída será longo. A razão para isso é que ele contém todos os dados de passe e incorpora a melhor segurança da categoria para garantir a integridade dos dados e nenhuma alteração por meio de modificação de URL. Se estiver usando o SMS para distribuir esse URL, talvez você queira executá-lo por meio de um processo de encurtamento de links, como [bit.ly](https://dev.bitly.com/v4/#operation/createFullBitlink). Isso pode ser feito por meio de uma chamada do conteúdo conectado para um endpoint bit.ly.

## Atualize o passe usando o webhook da PassKit

No Braze, você pode configurar uma campanha de webhook ou um webhook dentro de uma tela para atualizar um passe existente com base no comportamento do usuário. Confira os links a seguir para obter informações sobre endpoints úteis da PassKit. 
- [Projetos de membros](https://docs.passkit.io/protocols/member/)
- [Projetos de cupons](https://docs.passkit.io/protocols/coupon/)
- [Projetos de voos](https://docs.passkit.io/protocols/boarding/)

### Parâmetros da carga útil

Antes de começar, aqui estão os parâmetros comuns de carga útil JSON que você pode incluir em seus webhooks de criação e atualização para o Passkit.

| Dados | Tipo | Descrição |
| ---- | ---- | ----------- |
| `externalId` | String | Permite que um ID exclusivo seja adicionado ao registro do passe para oferecer compatibilidade com um sistema existente que usa identificadores exclusivos de clientes (por exemplo, números de inscrição). Você pode recuperar os dados do passe usando este endpoint por meio de `userDefinedId` e `campaignName` em vez do ID do passe. Esse valor deve ser exclusivo em uma campanha e, depois de definido, não poderá ser alterado.<br><br>Para a integração com a Braze, recomendamos o uso do ID externo da Braze: {% raw %}`{{${user_id}}}`{% endraw %} |
| `campaignId` (cupom) <br><br> `programId` (associação) | String | O ID do modelo de campanha ou programa que você criou no Passkit. Para encontrar isso, vá para a guia **Settings (Configurações)** em seu projeto PassKit Pass. |
| `expiryDate` | IO8601 datetime | A data de vencimento do passe. Após a data de vencimento, o passe será automaticamente anulado (consulte `isVoided`). Esse valor substituirá o modelo e o valor da data de término da campanha. |
| `status` | String | O status atual de um cupom, como `REDEEMED` ou `UNREDEEMED`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Etapa 1: Crie seu modelo de webhook do Braze

Para criar um modelo de webhook do PassKit para usar em futuras campanhas ou Canvas, navegue até a seção **Modelos e mídias** no dashboard do Braze. Se quiser criar uma campanha única de webhook do Passkit ou usar um modelo existente, selecione **Webhook** no Braze ao criar uma nova campanha.

Depois de selecionar o modelo de webhook da PassKit, você verá o seguinte:
- **URL do webhook**: `https://api-pub1.passkit.io/coupon/singleUse/coupon`
- **Corpo da solicitação**: Texto bruto

#### Cabeçalhos de solicitação e método

A PassKit requer um `HTTP Header` para autorização que inclui sua chave de API da PassKit codificada em base 64. O seguinte já estará incluído no modelo como um par de valores chave, mas na guia **Settings (Configurações)**, você deve substituir o `<PASSKIT_LONG_LIVED_TOKEN>` pelo seu token do Passkit. Para recuperar seu token, navegue até seu projeto/programa da PassKit, navegue até **Settings > Integrations > Long Lived Token** (Configurações > Integrações > Token de longa duração).

{% raw %}
- **Método HTTP**: PUT
- **Cabeçalho da solicitação**:
  - **Autorização**: portador `<PASSKIT_LONG_LIVED_TOKEN>`
  - **Tipo de Conteúdo**: application/json
{% endraw %}

#### Corpo da solicitação

Para configurar o webhook, preencha os detalhes do novo evento no corpo da solicitação, incluindo os parâmetros de carga útil necessários para seu caso de uso:

```json
{% raw %}{
  "externalId": "{{${user_id}}}",
  "campaignId": " 2xa1lRy8dBz4eEElBfmIz8",
  "expiryDate": "2020-05-10T00:00:00Z"
}{% endraw %}
```

### Etapa 2: veja uma prévia da sua solicitação

Seu texto bruto será automaticamente destacado se for uma tag Braze aplicável. 

Pré-visualize a solicitação no painel **Preview (Pré-visualização** ) ou navegue até a guia **Test (Teste** ), onde é possível selecionar um usuário aleatório, um usuário existente ou personalizar o seu próprio usuário para testar o webhook.

{% alert important %}
Lembre-se de salvar seu modelo antes de sair da página! <br>Os modelos de webhook atualizados podem ser encontrados na lista **Modelos de webhook salvos** ao criar uma nova [campanha de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}

## Recuperar detalhes do passe pelo conteúdo conectado

Além de criar e atualizar passes, também é possível recuperar os metadados dos passes dos usuários por meio do Braze [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) para incorporar detalhes personalizados dos passes em suas campanhas de mensagens.

**Chamada de conteúdo conectado da PassKit**

{% raw %}
```liquid
{% connected_content  https://api-pub1.passkit.io/coupon/singleUse/coupon/externalId/{{${user_id}}} :headers {"Authorization": "Bearer <PASSKIT_LONG_LIVED_TOKEN>","Content-Type": "application/json"} :save passes %}

{{passes.status}} 
```
{% endraw %}

**Exemplos de respostas do Liquid**

{% tabs local %}
{% tab passes redemptionDetails %}

```json
{
    "redemptionDate": null,
    "redemptionCode": "",
    "lat": 0,
    "lon": 0,
    "alt": 0,
    "redemptionSource": "",
    "redemptionReference": "",
    "transactionReference": "",
    "transactionAmount": 0
}
```

{% endtab %}
{% tab status de aprovação %}
```
UNREDEEMED 
```
{% endtab %}
{% endtabs %}


