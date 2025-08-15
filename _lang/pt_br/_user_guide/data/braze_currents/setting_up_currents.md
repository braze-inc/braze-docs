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

{% alert important %}
O Currents descartará eventos com cargas úteis excessivamente grandes, superiores a 900 KB.
{% endalert %}

Antes de testar, considere dar uma olhada em nossos [dados de amostra do Currents no GitHub](https://github.com/Appboy/currents-examples). Quando estiver pronto para testar, escolha uma opção abaixo:

#### Envio de eventos de teste

Para testar sua integração, você pode selecionar **Send Test Events (Enviar eventos de teste** ) para enviar um evento de cada um dos tipos de evento selecionados para essa corrente. Para obter informações detalhadas sobre cada tipo de evento, consulte nossas bibliotecas de [eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) e [de eventos de engajamento com mensagens]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).

![A página "Currents Test" (Teste de correntes) no dashboard do Braze.]({% image_buster /assets/img/currents/current_test_events.png %}){: style="max-width:70%;"}

#### Teste de conectores Currents

Os conectores Test Currents são versões gratuitas de nossos conectores existentes que podem ser usados para testar e experimentar diferentes destinos. As correntes de teste têm:

- Não há limite para o número de conectores Test Currents que você pode construir.
- Um máximo agregado de 10.000 eventos por período contínuo de sete dias. Esse total de eventos é atualizado de hora em hora no dashboard.

Depois que seus conectores de teste do Currents atingirem o limite de envio, seu conector não enviará eventos até o próximo período de sete dias.

Para fazer upgrade de seu conector Test Currents, edite a integração no dashboard e selecione **Upgrade Test Integration**.

## Atualização de Currents

{% multi_lang_include updating_currents.md %}

## Lista de permissões de IP

O Braze enviará dados Currents dos IPs listados:

{% multi_lang_include data_centers.md datacenters='ips' %}
