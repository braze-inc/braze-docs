---
nav_title: Pontos de dados
article_title: Visão geral dos pontos de dados
page_order: 10
page_type: reference
description: "Este artigo de referência descreve quais são os pontos de dados no Braze e como você pode estar ciente de seu uso."
search_rank: 6
---

# Pontos de dados

> Na Braze, dados significam ação: cada dado que chega à Braze atualiza a associação ao segmento, pode acionar e cancelar mensagens, está imediatamente disponível para a personalização de mensagens e muito mais. Os pontos de dados o ajudam a definir as informações mais impactantes para sua empresa. Ao considerar cuidadosamente quais informações rastrear, você garante que está direcionando os dados de maior impacto para a experiência dos seus usuários.

Os pontos de dados são baseados em informações registradas em perfis de usuários. Você pode encontrar uma análise mais detalhada dessa definição em seu contrato Braze. Nossa equipe de Sucesso do Cliente pode ajudar a recomendar as práticas recomendadas de dados que atendam às suas necessidades. 

## Definição

"Pontos de dados" referem-se a uma unidade faturável de uso dos Serviços Braze, medida por um início de sessão, fim de sessão, evento personalizado ou compra registrada, bem como qualquer atributo definido em um perfil de usuário final. Para fins de clareza, cada um dos dados mencionados acima (como início da sessão, fim da sessão, evento personalizado ou compra registrada, bem como qualquer atributo) definidos para o perfil de um usuário final em um determinado momento deve contar como um único ponto de dados.

Os dados e eventos coletados por padrão pelos Serviços Braze, incluindo, por exemplo, tokens push, informações do dispositivo e todos os eventos de rastreamento de engajamento de campanha, como aberturas de e-mail e cliques em notificações push, *não* são contados como pontos de dados.

Consulte a seção [Contagem de consumo](#consumption-count) deste artigo para entender quais dados contam para sua alocação de pontos de dados.

## Visualização da utilização do ponto de dados

Para visualizar o uso de seus pontos de dados, vá para **Configurações** > **Faturamento** e selecione a guia **Uso total de pontos de dados**.

Para obter mais informações sobre os componentes do painel de pontos de dados, consulte [Faturamento]({{site.baseurl}}/user_guide/administrative/app_settings/subscription_and_usage/).

{% alert tip %}
**Não desperdice pontos de dados. Atualize apenas os dados que estão mudando!**<br><br>
Para minimizar o uso de pontos de dados, recomendamos a configuração de um programa para evitar o envio dos mesmos dados imutáveis e passar apenas dados novos e relevantes para o Braze. A Braze trabalhará com você para estabelecer essa prática recomendada durante a integração.
{% endalert %}

## Contagem de consumo

Em suma, os pontos de dados são acumulados quando os dados do perfil de um usuário são atualizados ou quando ele executa ações específicas. Essencialmente, os pontos de dados são contagens de cada um dos usuários `session starts`, `session ends`, `events` e `purchases`.

Você pode encontrar um detalhamento de como o Braze acumula pontos de dados nas seções a seguir. Se você tiver alguma dúvida sobre as nuances dos pontos de dados Braze, seu gerente de conta Braze poderá respondê-la.

As ações a seguir não registram pontos de dados:
- Exclusão de usuários do Braze
- Uso de conteúdo conectado em mensagens
- O estado da assinatura muda globalmente e em torno dos grupos de assinatura
- Renomear os IDs externos de seus usuários por meio de [chamadas de API]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)
- Bloqueio de eventos, atributos ou propriedades de eventos

### Circunstâncias especiais

#### Matrizes

Uma matriz é uma coleção ordenada de itens armazenados em um atributo personalizado. Em termos de consumo, a atualização de uma matriz custa um ponto de dados por chamada de API. Se você adicionar valores a um array de forma incremental, ele contará como um ponto de dados por valor. 

{% alert tip %}
Se você definir toda a matriz de uma só vez, ela será contada como um único ponto de dados. Dessa forma, as matrizes são uma ótima ferramenta para manter os perfis de usuário atualizados com informações relevantes e reduzir custos.
{% endalert %}

#### Atributos personalizados aninhados

Os atributos personalizados aninhados referem-se a um objeto que define um conjunto de atributos como uma propriedade de outro atributo. Cada chave no objeto contará como um ponto de dados.

{% alert note %}
A atualização de um objeto de atributo personalizado para `null` também consome um ponto de dados.
{% endalert %}

#### CSV

Os atributos personalizados carregados por meio da importação de CSV são contabilizados em seus pontos de dados. No entanto, as importações de CSV para fins de segmentação (importações feitas com `external_id`, `braze_id` ou `user_alias_name` como o único campo) não registrarão pontos de dados.

Além disso, como as alterações de estado da assinatura não registram pontos de dados, a atualização dos campos `email_subscribe`, `push_subscribe`, `subscription_group_id` ou `subscription_state` no seu arquivo CSV não incorrerá em cobranças.

## Pontos de dados

{% alert note %}
As tabelas a seguir têm caráter ilustrativo. Para conhecer as convenções exatas de nomenclatura, capitalização e valores aceitos para determinados campos, consulte a documentação relevante do seu método de ingestão.
{% endalert %}

{% tabs %}
{% tab Non-billable %}

#### Pontos de dados não faturáveis (padrão)

<div class="small_table"></div>

| Tipo de dados | Ponto de dados |
| --------- | ---------- |
| Dados do perfil | País |
| Dados do perfil | Idioma |
| Dados do perfil | ID do usuário |
| Dados do perfil | Alias de usuário |
| Dispositivos recentes | Número de dispositivos |
| Dispositivos recentes | Observação mais recente |
| Dispositivos recentes | Versão do aplicativo |
| Dispositivos recentes | Dispositivo |
| Dispositivos recentes | Sistema operacional do dispositivo |
| Configurações de contato | E-mail subscrito |
| Configurações de contato | Assinatura por push |
| Configurações de contato | Aplicativos registrados para push |
| Configurações de contato | Grupo de assinaturas |
| Campanhas recebidas | Endereço de e-mail |
| Atribuição de instalação | Instalar fonte |
| Atribuição de instalação | Campanha |
| Atribuição de instalação | Grupo de anúncios |
| Atribuição de instalação | Anúncio |
| Diversos | Número aleatório do balde |
| Mensagens de tela recebidas | Mensagens de tela recebidas |
| Engajamento de mensagens | Todos os eventos de engajamento (como aberturas, cliques, impressões e recusas) |
| Twitter | Seguidores |
| Twitter | Seguindo |
| Twitter | Número de tweets |
| Facebook | Gostos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Billable %}

#### Pontos de dados faturáveis

{% alert important %}
A adição, a remoção ou a atualização dos seguintes tipos de dados incorrerá em um ponto de dados faturável.
{% endalert %}

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 30%;
}
table th:nth-child(3) {
    width: 50%;
}
table td {
    word-break: break-word;
}
</style>

| Tipo de dados | Ponto de dados | Notas |
| --------- | ---------- | ----- |
| Dados do perfil | Primeiro nome | |
| Dados do perfil | Sobrenome | |
| Dados do perfil | Endereço de e-mail | |
| Dados do perfil | Gênero | |
| Dados do perfil | Faixa etária | |
| Dados do perfil | País | Quando coletado manualmente. Não conta para o consumo quando coletado automaticamente. |
| Dados do perfil | Cidade | |
| Dados do perfil | Idioma | Quando coletado manualmente. Não conta para o consumo quando coletado automaticamente. |
| Dados do perfil | Localidade mais recente do dispositivo | |
| Dados do perfil | Fuso horário | |
| Dados do perfil | Data de nascimento (DOB) | |
| Dados do perfil | Biografia | |
| Dados do perfil | Número de telefone | |
| Dados de uso do aplicativo | Início da sessão | |
| Dados de uso do aplicativo | Fim da sessão | |
| Atributos personalizados | Todos os atributos personalizados | |
| Eventos personalizados | Todos os eventos personalizados | |
| Propriedades de eventos personalizados | Todas as propriedades de eventos personalizados | As propriedades de eventos personalizados habilitadas para segmentação com os filtros `X Custom Event Property in Y Days` ou `X Purchase Property in Y Days` são todas contadas como pontos de dados separados, além do ponto de dados contado pelo próprio evento personalizado.
| Compras | Todas as compras | |
| Compra de propriedades | Todas as propriedades de compra | |
| Atribuição de coorte de amplitude | Todas as atribuições | |
| Atribuição de coorte do Mixpanel | Todas as atribuições | |
| Atribuição de coorte Hightouch | Todas as atribuições | |
| Atribuição de coorte do Appsflyer | Todas as atribuições | |
| Local mais recente | Todos os locais mais recentes | Entrar ou sair de cercas geográficas não registra pontos de dados porque os dados da cerca geográfica não são armazenados no perfil do usuário. As geofences são monitoradas pelos serviços de localização da Apple e do Google; o Braze só é notificado quando um usuário aciona uma geofence. |
| Twitter | Nome de usuário | |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

