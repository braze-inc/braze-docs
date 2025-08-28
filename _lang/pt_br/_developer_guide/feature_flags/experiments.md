---
nav_title: Experimentos de Feature Flag
article_title: Experimentos de Feature Flag
page_order: 40
description: "Experimentos com Feature Flag permitem que você teste mudanças em suas aplicações para otimizar as taxas de conversão."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# Experimentos com Feature Flag

> Experimentos com Feature Flag permitem que você teste mudanças em suas aplicações para otimizar as taxas de conversão. Os profissionais de marketing podem usar Feature Flags para determinar se um novo recurso impacta positiva ou negativamente as taxas de conversão, ou qual conjunto de propriedades de Feature Flag é mais otimizado.

## Pré-requisitos

Antes que você possa rastrear dados de usuários no experimento, seu app precisa registrar quando um usuário interage com uma Feature Flag. Isso é chamado de impressão de Feature Flag. Certifique-se de registrar uma impressão de Feature Flag sempre que um usuário vir ou puder ter visto o recurso que você está testando, mesmo que ele esteja no grupo de controle.

Para saber mais sobre como registrar impressões de Feature Flag, consulte [Como criar Feature Flags]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#impressions).

{% tabs %}
{% tab JavaScript %}

```javascript
const featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag?.enabled) {
   return <NewFeature />
} else {
   return <ExistingFeature />
}
```

{% endtab %}
{% tab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewFeature();
} else {
  return new ExistingFeature();
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("my-new-feature")
braze.logFeatureFlagImpression("my-new-feature")
if (featureFlag?.enabled == true) {
  return NewFeature()
} else {
  return ExistingFeature()
}
```

{% endtab %}
{% endtabs %}

## Criando um experimento de Feature Flag

### Etapa 1: Criar um experimento

1. Acesse **Envio de mensagens** > **Campanhas** e selecione **\+ Criar campanha**.
2. Selecione **Feature Flag Experimental**.
3. Dê à sua campanha um nome claro e significativo.

### Etapa 2: Adicionar variantes de experimento

Em seguida, crie variações. Para cada variante, escolha o sinalizador de recurso que deseja ativar ou desativar e, em seguida, revise as propriedades atribuídas.

Para testar o impacto de sua funcionalidade, use variantes para dividir o tráfego em dois ou mais grupos. Nomeie um grupo "Meu grupo de controle" e desligue suas flags de recursos.

### Etapa 3: Substituir propriedades (opcional)

É possível optar por substituir as propriedades padrão configuradas inicialmente para os usuários que recebem uma variante de campanha específica.

Para editar, adicionar ou remover propriedades padrão adicionais, edite o próprio feature flag em **envio de mensagens** > **Feature Flags**. Quando uma variante estiver desativada, o SDK retornará um objeto de propriedades vazio para o sinalizador de recurso fornecido.

![A seção "Variantes do experimento" com a chave da variável "link" foi substituída por "/sales".]({% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %}){: style="max-width:80%"}

### Etapa 4: Escolha os usuários para direcionar

Use um de seus segmentos ou filtros para escolher seus [usuários-alvo]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/). Por exemplo, é possível usar o filtro **Variante de Feature Flag Recebida** para redirecionar os usuários que já receberam um teste A/B.

![A página "Target" (Alvo) em um experimento de feature flag com "Received Feature Flag Variant" (Variante de Feature Flag Recebida) destacada na barra de pesquisa do grupo de filtros.]({% image_buster /assets/img/feature_flags/variant-filter-dropdown.png %}){: style="max-width:70%"}

{% alert note %}
A associação de segmento é calculada quando os flags de recursos são atualizados para um determinado usuário. As alterações são disponibilizadas após a atualização dos recursos de sinalização do seu app, ou quando uma nova sessão é iniciada.
{% endalert %}

### Etapa 5: Distribuir variantes

Escolha a distribuição percentual para o seu experimento. Como uma prática recomendada, você não deve alterar a distribuição após o seu experimento ter sido lançado.

### Etapa 6: atribuir conversões

Braze permite que você acompanhe com que frequência os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), após receberem uma campanha. Especifique uma janela de até 30 dias durante a qual uma conversão será contada se o usuário realizar a ação especificada.

### Etapa 7: Revisar e lançar

Depois de concluir a construção do último experimento, revise os detalhes e selecione **Lançar experimento**.

## Revisão dos resultados

Após a conclusão do experimento de sinalização de recursos, é possível revisar os dados de impressão do experimento. Acesse **Envio de mensagens** > **Campanhas** e selecione a campanha com seu experimento de feature flag.

### Análise de dados de campanha

As **Análises de dados da campanha** oferecem uma visão geral de alto nível da performance de seu experimento, como, por exemplo

- O número total de impressões
- O número de impressões únicas
- A taxa de conversão primária
- A receita total gerada pela mensagem
- O público estimado

Você também pode visualizar as configurações do experimento para entrega, público e conversão.

### Feature Flag performance do experimento

O painel **Performance dos experimentos de Feature Flag** mostra o desempenho de sua mensagem em várias dimensões. As métricas específicas que você vê variam de acordo com o canal de envio de mensagens escolhido e se você está executando um teste multivariante. Para ver os valores do sinalizador de recursos associados a cada variante, selecione **Prévia**.
