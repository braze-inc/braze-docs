---
nav_title: Configuração de Currents
article_title: Configuração de Currents
page_order: 0
page_type: tutorial
description: "Este artigo de instruções explica o processo de integração e configuração do Braze Currents."
tool: Currents
search_rank: 8
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %}](https://learning.braze.com/currents-the-basics-2/) ){: style="float:right;width:120px;border:0;" class="noimgborder"}Configurando Currents

> Esta página delineia e descreve o processo genérico de integração e configuração do Braze Currents.

{% alert important %}
Os Currents estão incluídos em determinados pacotes Braze. Entre em contato com seu representante da Braze se tiver alguma dúvida ou quiser obter acesso.
{% endalert %}

## Solicitações

O uso do Currents com qualquer um de nossos parceiros requer os mesmos parâmetros básicos e a mesma metodologia de conexão.

Cada parceiro exige que o Braze tenha permissão para gravar e enviar arquivos de dados para eles, e o Braze solicita o local em que eles devem gravar esses arquivos, especificamente os nomes dos buckets ou as chaves.

Os requisitos a seguir são os requisitos básicos e mínimos para a integração com a maioria de nossos parceiros. Alguns parceiros exigirão parâmetros adicionais, que estão listados em suas respectivas [documentações de parceiros]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/), juntamente com quaisquer nuances associadas a esses requisitos básicos.

| Requisito | Origin | Acesso | Descrição
|---|---|---|---|
| Conta com parceiro | Organize uma conta com esse parceiro ou entre em contato com seu gerente de conta Braze para obter sugestões. | Verifique o site do parceiro ou entre em contato com ele para inscrever-se. | O Braze não enviará dados a um Parceiro se você não tiver acesso a esses dados por meio da conta de sua empresa.
| Chave ou token da API do parceiro | Normalmente, o dashboard do parceiro. | Basta copiá-lo e colá-lo no campo Braze designado. | A Braze tem um campo designado para isso na página Integrações para esse parceiro. Precisamos disso para mapear para onde estamos enviando seus dados. **É importante manter suas chaves/tokens de parceiro atualizadas; credenciais inválidas podem resultar na desativação de seu conector e na eliminação de eventos.**
| Código/chave de autenticação, chave secreta, arquivo de certificado | Entre em contato com um representante da sua conta com esse parceiro. Também pode existir no dashboard do parceiro. | Copie e cole as chaves no campo designado do Braze. Gerar e fazer upload do site `.json` ou de outros arquivos de certificado no local apropriado na Braze. | A Braze tem um campo designado para isso na página Integrações para esse parceiro. Isso fornece credenciais ao Braze e nos autoriza a gravar arquivos em sua conta de parceiro. **É importante manter suas informações de autenticação atualizadas; credenciais inválidas podem resultar na desativação do conector e no cancelamento de eventos.**
| Bucket, jornada da pasta | Alguns parceiros organizam e classificam os dados por grupos. Isso pode ser encontrado no dashboard do parceiro. | Se isso for necessário, copie o nome do bucket ou a jornada do arquivo exatamente no espaço designado na Braze. Não queremos que seus dados se percam! | Embora isso seja necessário para alguns parceiros, é importante acertar quando você precisar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
É importante manter suas chaves/tokens de parceiro e detalhes de autenticação atualizados; se as credenciais do conector expirarem, o conector deixará de enviar eventos. Se isso persistir por mais de **48 horas**, os eventos do conector serão descartados e os dados serão perdidos permanentemente.
{% endalert %}

## Configuração de Currents

### Etapa 1: Escolha seu parceiro

O Braze Currents permite a integração por meio do armazenamento de dados usando arquivos simples ou para nossos parceiros de análise comportamental e dados de clientes usando cargas úteis JSON em lote para um endpoint designado.  

Antes de iniciar sua integração, é melhor decidir qual integração é a melhor para seus objetivos. Por exemplo, se você já utiliza o mParticle e o Segment e gostaria que os dados da Braze fossem enviados para lá, seria melhor usar uma carga útil JSON em lote. Se preferir manipular os dados por conta própria ou tiver um sistema mais complexo de análise de dados, talvez seja melhor usar o armazenamento de dados[(o Braze usa esse método]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/)!)

### Etapa 2: Correntes abertas

Para começar, acesse **Integrações com parceiros** > **Exportação de dados**. Você será levado à página de gerenciamento de integração do Currents.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar essa página em **Integrations** > **Currents**.
{% endalert %}

![Página de Currents no dashboard da Braze]({% image_buster /assets/img_archive/currents-main-page.png %})

### Etapa 3: Adicione seu parceiro

Adicione um parceiro, às vezes chamado de "Currents connector", selecionando o menu suspenso na parte superior da tela.

Cada parceiro requer um conjunto diferente de etapas de configuração. Para ativar cada integração, consulte nossa lista de [parceiros disponíveis]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) e siga as instruções em suas respectivas páginas.

### Etapa 4: Configure seus eventos

Escolha os eventos que você deseja passar para esse parceiro marcando uma das opções disponíveis. Você pode encontrar listas desses eventos em nossas bibliotecas [Eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) e [Eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).

![]({% image_buster /assets/img/current4.png %})

Se necessário, você pode saber mais sobre nossos eventos em nosso artigo [sobre semântica de entrega de eventos]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics/).

### Etapa 5: Configurar transformações de campo

Você pode usar as transformações de campo do Currents para remover ou colocar em hash um campo de string.

- **Remover** Substitui o campo string por `[REDACTED]`. Isso é útil se o seu parceiro rejeitar eventos com campos ausentes ou vazios.
- **Hash:** Aplica um algoritmo de hash SHA-256 ao campo string.

A seleção de um campo para uma dessas transformações aplicará essa transformação a todos os eventos em que esse campo aparecer. Por exemplo, ao selecionar `email_address` para hashing, o campo `email_address` será submetido a hashing em Envio de e-mail, Abertura de e-mail, Bounce de e-mail e Alteração de estado do grupo de inscrições.

![Adição de transformações de campo]({% image_buster /assets/img/current3.png %})

### Etapa 6: Teste sua integração

Você pode testar sua integração ou dar uma olhada nos dados de amostra do Currents em nosso [repositório do GitHub](https://github.com/Appboy/currents-examples) de exemplos do Currents.

{% alert important %}
O Currents descartará eventos com cargas úteis excessivamente grandes, superiores a 900 KB.
{% endalert %}

#### Teste de conectores Currents

Os conectores Test Currents são versões gratuitas de nossos conectores existentes que podem ser usados para testar e experimentar diferentes destinos. As correntes de teste têm:

- Não há limite para o número de conectores Test Currents que você pode construir.
- Um máximo agregado de 10.000 eventos por período contínuo de sete dias. Esse total de eventos é atualizado de hora em hora no dashboard.

Depois que seus conectores de teste do Currents atingirem o limite de envio, seu conector não enviará eventos até o próximo período de sete dias.

Para fazer upgrade de seu conector de teste do Currents, edite a integração no dashboard e selecione **Upgrade**.

## Atualização de Currents

{% multi_lang_include updating_currents.md %}

## Lista de permissões de IP

O Braze enviará dados Currents dos IPs listados:

| Para as instâncias `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, e `US-07` |
|---|
| `127.0.0.1` |
| `23.21.118.191` |
| `34.206.23.173` |
| `50.16.249.9` |
| `52.4.160.214` |
| `54.87.8.34` |
| `54.156.35.251` |
| `52.54.89.238` |
| `18.205.178.15` |
{: .reset-td-br-1 role="presentation"}

| Por exemplo `US-08` |
|---|
| `52.151.246.51` |
| `52.170.163.182` |
| `40.76.166.157` |
| `40.76.166.170` |
| `40.76.166.167` |
| `40.76.166.161` |
| `40.76.166.156` |
| `40.76.166.166` |
| `40.76.166.160` |
| `40.88.51.74` |
| `52.154.67.17` |
| `40.76.166.80` |
| `40.76.166.84` |
| `40.76.166.85` |
| `40.76.166.81` |
| `40.76.166.71` |
| `40.76.166.144` |
| `40.76.166.145` |
{: .reset-td-br-1 role="presentation"}

| Para as instâncias `EU-01` e `EU-02` |
|---|
| `127.0.0.1` |
| `52.58.142.242` |
| `52.29.193.121` |
| `35.158.29.228` |
| `18.157.135.97` |
| `3.123.166.46` |
| `3.64.27.36` |
| `3.65.88.25` |
| `3.68.144.188` |
| `3.70.107.88` |
{: .reset-td-br-1 role="presentation"}

| Por exemplo `AU-01` |
|---|
| `13.210.1.145` |
| `13.211.70.159` |
| `13.238.45.54` |
| `52.65.73.167` |
| `54.153.242.239` |
| `54.206.45.213` |
{: .reset-td-br-1 role="presentation"}