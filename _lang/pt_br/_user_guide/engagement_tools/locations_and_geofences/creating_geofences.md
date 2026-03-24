---
nav_title: Criar geofences
article_title: Criar Geofences
page_order: 1
page_type: reference
toc_headers: h2
description: "Saiba como configurar permissões de localização, criar um primer de permissão de localização e criar geofences para campanhas baseadas em localização."
tool: 
  - Location
search_rank: 9
---

# Geofences

> Uma geofence é uma área geográfica virtual, representada como latitude e longitude combinadas com um raio, formando um círculo em torno de uma posição global específica. As geofences podem variar do tamanho de um prédio até o tamanho de uma cidade inteira. Você pode usar geofences para disparar campanhas em tempo real à medida que os usuários entram e saem de suas bordas, ou enviar campanhas de acompanhamento horas ou dias depois.

{% alert tip %}
Para um passo a passo guiado, consulte o curso do Braze Learning [Create a Geofence](https://learning.braze.com/create-a-geofence).
{% endalert %}

## Como funciona

As geofences são organizadas em conjuntos de geofences — um grupo de geofences que pode ser usado para segmentar ou engajar usuários em toda a plataforma. Cada conjunto de geofences pode conter um máximo de 10.000 geofences. Você pode criar ou fazer upload de um número ilimitado de geofences.

Os usuários que entram ou saem de suas geofences adicionam uma nova camada de dados de usuários que podem ser usados para segmentação e redirecionamento.

Tenha em mente os seguintes limites de dispositivo:

- Os apps para Android podem armazenar até 100 geofences localmente de cada vez. A Braze está configurada para armazenar apenas até 20 geofences localmente por app.
- Os dispositivos iOS podem monitorar até 20 geofences ao mesmo tempo por app. A Braze monitora até 20 locais se houver espaço disponível.
- Se o usuário for elegível para receber mais de 20 geofences, a Braze baixa a quantidade máxima de locais com base na proximidade do usuário no início da sessão.
- Para que as geofences funcionem corretamente, garanta que seu app não esteja usando todos os pontos de geofence disponíveis.

A tabela a seguir descreve termos comuns de geofence:

| Termo | Descrição |
|---|---|
| Latitude e longitude | O centro geográfico da geofence. |
| Raio | O raio da geofence em metros, medido a partir do centro geográfico. Defina um raio mínimo de 100 a 150 metros para todas as geofences. |
| Cooldown | Os usuários recebem notificações disparadas por geofences depois de realizar transições de entrada ou saída em geofences individuais. Após a ocorrência de uma transição, há um período predefinido durante o qual o usuário não pode realizar a mesma transição nessa geofence individual novamente. Esse "cooldown" é predefinido pela Braze e seu principal objetivo é evitar solicitações de rede desnecessárias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Pré-requisitos

### Requisitos de SDK e plataforma

As campanhas disparadas por geofence estão disponíveis no iOS e no Android. Para oferecer suporte a geofences, os seguintes itens são necessários:

* Sua integração deve suportar notificações por push em segundo plano.
* As geofences da Braze ou a coleta de locais devem estar ativadas.
* O usuário deve conceder acesso de localização "Permitir Sempre".

{% alert important %}
A coleta de locais da Braze é desativada por padrão. Para verificar se está ativada no Android, confirme que `com_braze_enable_location_collection` está definido como `true` no seu `braze.xml`.
{% endalert %}

Para instruções de configuração específicas por plataforma, consulte [Geofences]({{site.baseurl}}/developer_guide/geofences/) no guia do desenvolvedor.

### Permissões de localização

Antes que suas geofences possam funcionar, os usuários devem conceder ao seu app permissão para acessar a localização deles. Entender os diferentes níveis de permissão e seu impacto no geofencing é fundamental para construir uma estratégia eficaz baseada em localização.

## Entendendo as permissões de localização

Tanto o iOS quanto o Android oferecem múltiplos níveis de acesso à localização. O nível de permissão que um usuário concede afeta diretamente se o geofencing funciona e quão precisos são os dados de localização.

### Níveis de permissão

{% tabs local %}
{% tab iOS %}

| Permissão | Descrição | Suporte a geofencing |
|---|---|---|
| **Permitir Uma Vez** | Concede acesso à localização para uma única sessão. O prompt reaparece na próxima vez que o usuário abrir o app. | Não. O rastreamento em segundo plano está desativado, então o dispositivo só recebe atualizações de localização quando o app está aberto. |
| **Permitir Enquanto Usa o App** | Concede acesso à localização sempre que o app está em primeiro plano. Após essa concessão, o iOS pode apresentar um prompt de acompanhamento pedindo ao usuário para fazer upgrade para "Permitir Sempre". | Sim. O iOS ativa o monitoramento de localização em segundo plano, incluindo transições de geofence, para apps com essa permissão. |
| **Permitir Sempre** | Concede acesso contínuo à localização, inclusive em segundo plano e quando o app está fechado. | Sim. Isso fornece o monitoramento de geofence mais confiável. |
| **Não Permitir** | Nega todo acesso à localização. | Não. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Android %}

| Permissão | Descrição | Suporte a geofencing |
|---|---|---|
| **Enquanto Usa o App** | Concede acesso à localização enquanto o app está em primeiro plano. | Não. No Android, o acesso à localização em segundo plano é necessário para o monitoramento de geofence. |
| **Permitir Sempre** | Concede acesso contínuo à localização, inclusive em segundo plano. No Android 10 e posterior, isso requer um prompt separado após a permissão inicial "Enquanto Usa o App" ser concedida. | Sim. Isso é necessário para geofencing no Android. |
| **Não Permitir** | Nega todo acesso à localização. No Android 13 e posterior, se um usuário negar o prompt de localização duas vezes, o sistema operacional bloqueia prompts adicionais dentro do app. | Não. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% endtabs %}

### Localização precisa versus aproximada

No iOS 14+ e Android 12+, os usuários podem escolher entre localização precisa e aproximada.

| Configuração | Precisão | Impacto no geofencing |
|---|---|---|
| **Localização precisa (ativada)** | Precisão na faixa de 5 a 50 metros, usando GPS, Wi-Fi e triangulação celular. | As geofences funcionam conforme esperado. Recomendado para todos os casos de uso baseados em geofence. |
| **Localização aproximada (desativada)** | Precisão em torno de 3 quilômetros quadrados (aproximadamente 1 milha quadrada). O dispositivo retorna uma área geral em vez de coordenadas exatas. | As geofences não disparam de forma confiável. O dispositivo não consegue determinar com precisão se um usuário está dentro ou fora de um limite de geofence. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Para que o geofencing funcione de forma confiável, os usuários devem ativar a localização precisa. Inclua essa orientação nas mensagens do seu primer de permissão de localização para que os usuários entendam por que a localização precisa é importante.
{% endalert %}

## Configurando um primer de permissão de localização

Um primer de permissão de localização é uma mensagem no app que explica o valor de compartilhar dados de localização antes que o usuário veja o prompt nativo de permissão do sistema operacional. Como o prompt nativo de localização só pode ser exibido uma vez (no iOS) ou um número limitado de vezes (no Android), preparar os usuários com antecedência aumenta as taxas de aceitação.

### Etapa 1: Trabalhe com sua equipe de desenvolvimento

Como as mensagens no app da Braze não incluem uma ação de botão integrada para invocar o prompt nativo de permissão de localização, sua equipe de desenvolvimento precisa lidar com as permissões de localização no lado do dispositivo. Antes de criar a mensagem no app na Braze, coordene com sua equipe de desenvolvimento para configurar deep links que sua mensagem no app possa chamar. A implementação específica depende da arquitetura do seu app, mas abordagens comuns incluem:

- Um deep link que dispara o prompt nativo de permissão de localização dentro do seu app.
- Um deep link que abre a página de configurações de localização do app nas configurações do sistema operacional do dispositivo, o que é útil para solicitar novamente a usuários que anteriormente negaram ou limitaram suas permissões.

Para saber mais sobre deep links, consulte [Deep linking para conteúdo no app]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/). Para orientações específicas por plataforma sobre integração de localização e geofence, consulte [Geofences]({{site.baseurl}}/developer_guide/geofences/) no guia do desenvolvedor.

### Etapa 2: Crie a mensagem no app do primer de localização

Crie uma campanha de mensagem no app que explique o valor do acesso à localização. Todos os tipos de mensagem no app suportam essa aceitação, incluindo arrastar e soltar.

1. Acesse **Envio de mensagens** > **Campanhas**, depois selecione **Criar Campanha** > **Mensagem no app**.
2. Escolha um tipo de mensagem e layout. Um layout **Modal** ou **Tela Cheia** oferece mais espaço para articular os benefícios.
3. Escreva uma mensagem que explique claramente por que o acesso à localização beneficia o usuário. Por exemplo:
    - "Ative a localização para ser notificado sobre ofertas perto de você."
    - "Ative a localização para que possamos avisar quando seu pedido estiver pronto para retirada na loja mais próxima."
4. Adicione um botão principal de chamada para ação (como **Ativar Localização**) e defina seu comportamento ao clicar como **Deep Link no App**, usando o deep link que sua equipe de desenvolvimento criou para disparar o prompt nativo de localização.
5. Adicione um botão secundário (como **Agora Não**) que fecha a mensagem.

### Etapa 3: Direcione o público certo

Para melhores resultados, exiba o primer de localização quando os usuários estiverem engajados e propensos a ver valor em compartilhar sua localização.

- **Direcione para usuários que ainda não concederam acesso à localização.** Trabalhe com sua equipe de desenvolvimento para determinar a melhor forma de rastrear e segmentar usuários com base no status de permissão de localização.
- **Programe o primer após uma ação de alto valor,** como concluir uma compra, salvar uma loja como favorita ou navegar por eventos próximos. Os usuários são mais propensos a aceitar quando entendem o benefício.
- **Evite exibir o primer na primeira abertura.** Espere até que os usuários tenham experimentado valor suficiente do app para querer uma experiência mais personalizada.

### Etapa 4: Incentive o nível de permissão recomendado

Sua mensagem do primer deve incentivar os usuários a conceder o nível de permissão que ativa o geofencing:

- **No iOS,** incentive os usuários a selecionar **Permitir Enquanto Usa o App** no mínimo. O iOS pode posteriormente solicitar ao usuário que faça upgrade para **Permitir Sempre** por conta própria. Você também pode fazer um acompanhamento com uma campanha separada para explicar por que "Permitir Sempre" oferece a melhor experiência.
- **No Android,** incentive os usuários a conceder **Permitir Sempre**. No Android 10 e posterior, o usuário deve primeiro conceder "Enquanto Usa o App", depois conceder "Permitir Sempre" em um prompt de acompanhamento separado. Guie-os em ambas as etapas.

Em ambos os casos, lembre os usuários de manter a **Localização Precisa** ativada para a melhor experiência.

## Redirecionando usuários para as configurações do sistema operacional

Se um usuário anteriormente negou o acesso à localização ou selecionou uma permissão limitada, você não pode disparar o prompt nativo novamente de dentro do app na maioria das versões do sistema operacional. Em vez disso, direcione-os para atualizar suas permissões nas configurações do dispositivo.

Use um deep link dentro de uma [mensagem no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/) personalizada para navegar o usuário até a página de configurações de localização do app no sistema operacional. Sua equipe de desenvolvimento pode configurar um deep link para isso como parte do tratamento de permissão de localização do seu app (consulte a [Etapa 1](#step-1-work-with-your-development-team)).

Ao criar essa mensagem no app, considere o seguinte:

- **Quando exibir:** Direcione para usuários que têm permissão "Enquanto Usa o App" quando você precisa de "Permitir Sempre", ou usuários que anteriormente negaram o acesso à localização.
- **Exemplo de mensagem:** "Para aproveitar ao máximo os recursos baseados em localização, atualize suas configurações de localização para 'Permitir Sempre'. Toque abaixo para ir para Configurações."

{% alert tip %}
Você pode disparar essa mensagem no app em qualquer ponto da jornada do usuário — após uma compra, ao navegar por conteúdo próximo ou como parte de um fluxo de Canvas. Seja seletivo ao solicitar novamente: limite essas campanhas a usuários fiéis ou altamente engajados para evitar fadiga de aceitação.
{% endalert %}

## Exemplos de estratégias de primer de localização

### Primer "Enquanto Usa o App"

Um app de varejo exibe uma mensagem no app modal depois que um usuário salva uma loja como favorita:

- **Título:** "Receba notificações sobre ofertas na loja"
- **Corpo:** "Ative a localização para que possamos enviar ofertas exclusivas quando você estiver perto das suas lojas favoritas. Sua localização só é acessada enquanto usa o app."
- **CTA:** **Ativar Localização** faz deep link para o prompt nativo de permissão de localização
- **Dispensar:** **Talvez Depois** fecha a mensagem

Essa abordagem é eficaz porque o usuário já demonstrou interesse em uma loja específica, criando um contexto natural para a solicitação de permissão de localização.

### Acompanhamento "Permitir Sempre"

Depois que um usuário concede a permissão "Enquanto Usa o App", exiba uma mensagem no app de acompanhamento durante a próxima sessão:

- **Título:** "Nunca perca uma oferta por perto"
- **Corpo:** "Atualize suas configurações de localização para 'Sempre' para que possamos notificá-lo sobre ofertas mesmo quando você não estiver navegando no app. Enviaremos apenas alertas relevantes quando você estiver perto de locais participantes."
- **CTA:** **Atualizar Configurações** faz deep link para a página de configurações de localização do app no sistema operacional
- **Dispensar:** **Manter Configurações Atuais** fecha a mensagem

Esse acompanhamento dá ao usuário contexto sobre por que fazer upgrade para "Permitir Sempre" oferece valor adicional além do nível de permissão inicial.

## Criar geofences manualmente

### Etapa 1: Criar um conjunto de geofences

Para criar uma geofence, crie um conjunto de geofences primeiro.

1. Acesse **Público** > **Locais** no dashboard da Braze.
2. Selecione **Criar Conjunto de Geofence**.
3. Para **Nome do conjunto**, insira um nome para seu conjunto de geofences.
4. (Opcional) Adicione tags para filtrar seu conjunto.

### Etapa 2: Adicionar as geofences

Em seguida, adicione geofences ao seu conjunto de geofences.

1. Selecione **Desenhar Geofence** para clicar e arrastar o círculo no mapa. Repita para adicionar mais geofences ao seu conjunto conforme necessário.
2. (Opcional) Selecione **Editar** e substitua a descrição da geofence por um nome.
3. Selecione **Salvar Conjunto de Geofences** para salvar.

{% alert tip %}
Crie geofences com um raio de pelo menos 200 metros para funcionalidade ideal. Para saber mais, consulte [Melhores práticas de geofence](#geofence-best-practices).
{% endalert %}

![Um conjunto de geofences com duas geofences "EastCoastGreaterNY" e "WesternRegion" com dois círculos no mapa.]({% image_buster /assets/img/geofence_example.png %})

## Upload de geofences em massa {#creating-geofence-sets-via-bulk-upload}

Você pode fazer upload de geofences em massa como um objeto GeoJSON do tipo `FeatureCollection`. Cada geofence é um tipo de geometria `Point` na coleção de recursos. As propriedades para cada recurso requerem uma chave `radius` e uma chave opcional `name` para cada geofence.

Para fazer upload do seu arquivo JSON, selecione **Mais** > **Fazer upload do JSON**.

Ao criar suas geofences, considere os seguintes detalhes:

- O valor `coordinates` no GeoJSON é formatado como `[Longitude, Latitude]`.
- O raio máximo de geofence que pode ser enviado é de 10.000 metros (cerca de 10 quilômetros ou 6,2 milhas).

### Exemplo

O exemplo a seguir mostra o formato GeoJSON correto para especificar duas geofences: uma para a sede da Braze em NYC e uma para a Estátua da Liberdade ao sul de Manhattan.

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-73.9853689, 40.7434683]
      },
      "properties": {
        "radius": 200,
        "name": "Braze HQ"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-74.044468, 40.689225]
       },
      "properties": {
        "radius": 100,
        "name": "Statue of Liberty"
      }
    }
  ]
}
```

## Uso de eventos de geofence

Depois de configurar suas geofences, você pode usá-las para aprimorar e enriquecer a forma como se comunica com seus usuários.

### Disparando campanhas e Canvas

Para usar os dados de geofence como parte dos disparos de campanha e Canvas, escolha **Entrega baseada em ação** para o método de entrega. Em seguida, adicione uma ação-gatilho de `Trigger a Geofence`. Por fim, escolha o conjunto de geofences e os tipos de eventos de transição de geofence para sua mensagem. Também é possível avançar os usuários em um Canvas usando eventos de geofence.

![Uma campanha baseada em ação com uma geofence que será disparada quando um usuário entrar em aeroportos alemães.]({% image_buster /assets/img_archive/action_based_geofence_trigger.png %})

### Personalizando mensagens

Para usar dados de geofence para personalizar uma mensagem, você pode usar a seguinte sintaxe de personalização do Liquid:

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Atualização de conjuntos de geofences

O SDK da Braze solicita geofences apenas uma vez por dia no início da sessão. Se você fizer alterações nos conjuntos de geofences após o início da sessão, precisará aguardar 24 horas a partir do momento em que os conjuntos foram baixados pela primeira vez para receber o conjunto atualizado.

Se o usuário tiver push em segundo plano ativado, a Braze envia um push silencioso a cada 24 horas quando os conjuntos de geofences são atualizados para baixar os locais mais recentes para o dispositivo.

{% alert note %}
Se as geofences não forem carregadas localmente no dispositivo, o usuário não poderá disparar a geofence mesmo que entre na área.
{% endalert %}

## Melhores práticas de geofence

### Configuração de geofence

- Use um raio de 200 metros ou mais para disparo confiável.
- Evite configurar geofences que se sobreponham ou estejam aninhadas umas dentro das outras, pois isso pode causar problemas com o disparo.
- Uma geofence pode disparar um evento de entrada apenas uma vez a cada seis horas. Esse período de cooldown é aplicado localmente. Se um usuário desinstalar o app ou limpar os dados do app, todos os cooldowns são redefinidos.
- No máximo 20 geofences no total podem ser armazenadas em um dispositivo. Se o usuário for elegível para mais de 20, a Braze baixa os locais mais próximos com base na proximidade no início da sessão ou na atualização por push silencioso.
- A Braze envia apenas geofences dentro de um raio de 2.000 quilômetros do usuário para o dispositivo.

### Requisitos do dispositivo

- As permissões de push e de localização devem estar ativadas para o app.
- Um token de push de primeiro plano válido é necessário.

{% alert note %}
A integração básica do SDK ativa apenas o monitoramento de localização. O geofencing requer etapas de configuração adicionais tanto para iOS quanto para Android. Para mais detalhes, consulte [Geofences]({{site.baseurl}}/developer_guide/geofences/) no guia do desenvolvedor.
{% endalert %}

Você também pode usar geofences com Parceiros de Tecnologia da Braze, como [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/) e [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/).

## Perguntas frequentes

### Qual é a diferença entre geofences e monitoramento de localização?

Na Braze, uma geofence é um conceito diferente do monitoramento de localização. As geofences são usadas como disparadores para determinadas ações — quando um usuário entra ou sai de um limite virtual estabelecido em torno de um local geográfico, isso pode disparar uma ação específica, como o envio de uma mensagem.

O monitoramento de localização coleta e armazena os dados de localização mais recentes de um usuário. Esses dados podem ser usados para segmentar usuários com base no filtro `Most Recent Location`. Por exemplo, você pode usar o filtro `Most Recent Location` para direcionar usuários localizados em Nova York.

Para saber mais, consulte [Monitoramento de localização]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/location_tracking/).

### Qual é a precisão das geofences da Braze?

As geofences da Braze usam uma combinação de todos os provedores de localização disponíveis em um dispositivo para triangular a localização do usuário, incluindo Wi-Fi, GPS e torres de celular.

A precisão típica está na faixa de 20 a 50 metros, e a melhor precisão está na faixa de 5 a 10 metros. Em áreas rurais, a precisão pode se degradar significativamente, podendo chegar a vários quilômetros. Crie geofences com raios maiores em locais rurais.

A precisão também depende de o usuário ter a localização precisa ativada. Com apenas localização aproximada, a precisão cai para cerca de 3 quilômetros quadrados, tornando as geofences não confiáveis. Para saber mais, consulte [Localização precisa versus aproximada](#precise-versus-approximate-location).

### Como as geofences afetam a duração da bateria?

O geofencing da Braze usa o serviço de sistema de geofence nativo no iOS e Android. Ele é ajustado para equilibrar inteligentemente precisão e consumo de energia, economizando a vida útil da bateria e melhorando a performance à medida que o serviço subjacente melhora.

### Quando as geofences estão ativas?

As geofences da Braze funcionam em todas as horas do dia, mesmo quando seu app está fechado. Elas se tornam ativas assim que são definidas e enviadas para o dashboard da Braze. No entanto, as geofences não podem funcionar se um usuário tiver desativado o monitoramento de localização.

Para que as geofences funcionem, os usuários devem ter os serviços de localização ativados no dispositivo e devem ter concedido ao seu app o nível de permissão de localização necessário. Para saber mais, consulte [Entendendo as permissões de localização](#understanding-location-permissions).

### Os dados de geofence são armazenados nos perfis de usuários?

Não, a Braze não armazena dados de geofence nos perfis de usuários. As geofences são monitoradas pelos serviços de localização da Apple e do Google, e a Braze só é notificada quando um usuário dispara uma geofence. Nesse ponto, a Braze processa todas as campanhas de disparo associadas.

### Posso configurar uma geofence dentro de uma geofence?

Como boa prática, evite configurar geofences que se sobreponham, pois isso pode causar problemas com o disparo de notificações.

### E se um usuário negar o acesso à localização?

Sua equipe de desenvolvimento pode configurar um deep link que abre a página de configurações de localização do app no sistema operacional, onde os usuários podem atualizar suas permissões. Você pode usar esse deep link dentro de uma mensagem no app personalizada em qualquer ponto da jornada do usuário. Seja seletivo sobre quando exibir essa mensagem — direcione para usuários que estejam engajados ou que tenham realizado uma ação de alto valor para aumentar a chance de aceitação. Para saber mais, consulte [Redirecionando usuários para as configurações do sistema operacional](#redirecting-users-to-os-settings).