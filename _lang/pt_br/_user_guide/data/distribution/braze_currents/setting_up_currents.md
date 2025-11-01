---
nav_title: Configuração de correntes
article_title: Configuração de correntes
page_order: 0
page_type: tutorial
description: "Este artigo de instruções orienta você no processo de integração e configuração do Braze Currents."
tool: Currents
search_rank: 8
---

# [Curso de aprendizado do Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/currents-the-basics-2/){: style="float:right;width:120px;border:0;" class="noimgborder"} Configurando correntes

> Esta página delineia e descreve o processo genérico de integração e configuração do Braze Currents.

{% alert important %}
As correntes estão incluídas em determinados pacotes do Braze. Entre em contato com seu representante Braze se tiver alguma dúvida ou quiser obter acesso.
{% endalert %}

## Requisitos

O uso do Currents com qualquer um de nossos parceiros requer os mesmos parâmetros básicos e a mesma metodologia de conexão.

Cada parceiro exige que o Braze tenha permissão para gravar e enviar arquivos de dados para eles, e o Braze solicita o local em que eles devem gravar esses arquivos, especificamente nomes ou chaves de bucket.

Os requisitos a seguir são os requisitos básicos e mínimos para integração com a maioria de nossos parceiros. Alguns parceiros exigirão parâmetros adicionais, que estão listados em suas respectivas [documentações de parceiros]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/), juntamente com quaisquer nuances associadas a esses requisitos básicos.

| Requisito | Origem | Acesso | Descrição
|---|---|---|---|
| Conta com parceiro | Organize uma conta com esse parceiro ou entre em contato com seu gerente de conta Braze para obter sugestões. | Verifique o site do parceiro ou entre em contato com ele para se inscrever. | O Braze não enviará dados a um parceiro se você não tiver acesso a esses dados por meio da conta de sua empresa.
| Chave ou token da API do parceiro | Normalmente, o painel de controle do parceiro. | Basta copiá-lo e colá-lo no campo Braze designado. | O Braze tem um campo designado para isso na página de integrações para esse parceiro. Precisamos disso para mapear para onde estamos enviando seus dados. **É importante manter as chaves de parceiro ou os tokens atualizados; credenciais inválidas podem resultar na desativação do conector e na interrupção de eventos.**
| Código/chave de autenticação, chave secreta, arquivo de certificação | Entre em contato com um representante da sua conta com esse parceiro. Também pode existir no painel de controle do parceiro. | Copie e cole as chaves no campo Braze designado. Gerar e carregar `.json` ou outros arquivos de certificação no local apropriado no Braze. | O Braze tem um campo designado para isso na página de integrações para esse parceiro. Isso fornece credenciais à Braze e nos autoriza a gravar arquivos em sua conta de parceiro. **É importante manter seus detalhes de autenticação atualizados; credenciais inválidas podem resultar na desativação do seu conector e no descarte de eventos.**
| Bucket, caminho da pasta | Alguns parceiros organizam e classificam os dados por grupos. Isso deve ser encontrado no painel de controle do parceiro. | Se isso for necessário, certifique-se de copiar o nome do bucket ou o caminho do arquivo exatamente no espaço designado no Braze. Não queremos que seus dados se percam! | Embora isso seja necessário para alguns parceiros, é importante acertar quando você precisar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
É importante manter suas chaves de parceiro, tokens de parceiro e detalhes de autenticação atualizados; se as credenciais do seu conector expirarem, o conector deixará de enviar eventos. Se isso persistir por mais de **5 dias**, os eventos do conector serão descartados e os dados serão perdidos permanentemente.
{% endalert %}

## Configuração de correntes

### Etapa 1: Escolha seu parceiro

O Braze Currents permite que você faça a integração por meio do armazenamento de dados usando arquivos simples ou com nossos parceiros de análise comportamental e dados de clientes usando cargas JSON em lote para um endpoint designado.  

Antes de iniciar sua integração, é melhor decidir qual integração é a melhor para seus objetivos. Por exemplo, se você já usa o mParticle e o Segment e gostaria que os dados do Braze fossem transmitidos para lá, seria melhor usar um payload JSON em lote. Se você preferir manipular os dados por conta própria ou tiver um sistema mais complexo de análise de dados, talvez seja melhor usar o Data Storage[(o Braze usa esse método]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/)!)

### Etapa 2: Correntes abertas

Para começar, vá para **Partner Integrations** > **Data Export**. Você será levado à página de gerenciamento da integração do Currents.

\![Página atual no painel de controle do Braze]({% image_buster /assets/img_archive/currents-main-page.png %})

### Etapa 3: Adicione seu parceiro

Adicione um parceiro, às vezes chamado de "conector do Currents", selecionando o menu suspenso na parte superior da tela.

Cada parceiro requer um conjunto diferente de etapas de configuração. Para ativar cada integração, consulte nossa lista de [parceiros disponíveis]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) e siga as instruções em suas respectivas páginas.

### Etapa 4: Configure seus eventos

Escolha os eventos que você deseja passar para esse parceiro marcando uma das opções disponíveis. Você pode encontrar listas desses eventos em nossas bibliotecas [Customer Behavior Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) e [Message Engagement Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).

\![]({% image_buster /assets/img/current4.png %})

Se necessário, você pode saber mais sobre nossos eventos em nosso artigo [sobre semântica de entrega de eventos]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics/).

### Etapa 5: Configurar transformações de campo

Você pode usar as transformações de campo do Currents para remover ou colocar em hash um campo de cadeia de caracteres.

- **Remover:** Substitui o campo string por `[REDACTED]`. Isso é útil se o seu parceiro rejeitar eventos com campos ausentes ou vazios.
- **Hash:** Aplica um algoritmo de hash SHA-256 ao campo da cadeia de caracteres.

A seleção de um campo para uma dessas transformações aplicará essa transformação a todos os eventos em que esse campo aparecer. Por exemplo, a seleção de `email_address` para hashing fará o hash do campo `email_address` nos eventos Email Send (Envio de e-mail), Email Open (Abertura de e-mail), Email Bounce (Rejeição de e-mail) e Subscription Group State Change (Mudança de estado do grupo de assinatura).

\![Adicionando transformações de campo]({% image_buster /assets/img/current3.png %})

### Etapa 6: Teste sua integração

{% alert important %}
O Currents descartará eventos com cargas úteis excessivamente grandes, superiores a 900 KB.
{% endalert %}

Antes de testar, considere verificar nossos [dados de amostra do Currents no GitHub](https://github.com/Appboy/currents-examples). Quando estiver pronto para testar, escolha uma opção abaixo:

#### Envio de eventos de teste

Para testar sua integração, você pode selecionar **Send Test Events (Enviar eventos de teste** ) para enviar um evento de cada um dos tipos de evento selecionados para essa corrente. Para obter informações detalhadas sobre cada tipo de evento, consulte nossas bibliotecas [Customer Behavior Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) e [Message Engagement Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).

A página "Currents Test" (Teste de correntes) no painel do Braze.]({% image_buster /assets/img/currents/current_test_events.png %}){: style="max-width:70%;"}

#### Teste de conectores de corrente

Os conectores Test Currents são versões gratuitas de nossos conectores existentes que podem ser usados para testar e experimentar diferentes destinos. As correntes de teste têm:

- Não há limite para o número de conectores Test Currents que você pode construir.
- Um máximo agregado de 10.000 eventos por período contínuo de sete dias. Esse total de eventos é atualizado a cada hora no painel.

Depois que seus conectores Test Currents atingirem o limite de envio, seu conector não enviará eventos até o próximo período de sete dias.

Para atualizar seu conector Test Currents, edite a integração no painel e selecione **Atualizar integração de teste**.

## Atualização de correntes

{% multi_lang_include updating_currents.md %}

## Lista de permissões de IP

O Braze enviará dados Currents dos IPs listados:

{% multi_lang_include data_centers.md datacenters='ips' %}
