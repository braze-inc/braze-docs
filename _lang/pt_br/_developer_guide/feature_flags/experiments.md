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

# Criando um experimento de Feature Flag

> Experimentos com Feature Flag permitem que você teste mudanças em suas aplicações para otimizar as taxas de conversão. Os profissionais de marketing podem usar Feature Flags para determinar se um novo recurso impacta positiva ou negativamente as taxas de conversão, ou qual conjunto de propriedades de Feature Flag é mais otimizado.

## Pré-requisitos

Antes que você possa rastrear dados de usuários no experimento, seu app precisa registrar quando um usuário interage com uma Feature Flag. Isso é chamado de impressão de Feature Flag. Certifique-se de registrar uma impressão de Feature Flag sempre que um usuário vir ou puder ter visto o recurso que você está testando, mesmo que ele esteja no grupo de controle.

Para saber mais sobre como registrar impressões de Feature Flag, consulte [Como criar Feature Flags]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#impressions).

```javascript
const featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag?.enabled) {
   return <NewFeature />
} else {
   return <ExistingFeature />
}

```

## Etapa 1: Criar um experimento

1. Acessar **envio de mensagens** > **Campanhas** e clicar **\+ Criar Campanha**.
2. Selecione **Feature Flag Experimental**.
3. Dê um nome claro e significativo à sua campanha.

## Etapa 2: Adicionar variantes de experimento

Em seguida, crie variações. Para cada variante, escolha o Feature Flag que deseja ativar ou desativar e revise as propriedades atribuídas.

Para testar o impacto de sua funcionalidade, use variantes para dividir o tráfego em dois ou mais grupos. Nomeie um grupo "Meu grupo de controle" e desligue suas flags de recursos.

### Substituindo propriedades

Embora você tenha especificado propriedades padrão quando configurou originalmente seu Feature Flag, você pode optar por sobrescrever esses valores para os usuários que recebem uma variante de campanha específica.

![]({% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %}){: style="max-width:80%"}

Para editar, adicionar ou remover propriedades padrão adicionais, edite o próprio feature flag em **envio de mensagens** > **Feature Flags**.

Quando uma variante estiver desativada, o SDK retornará um objeto de propriedades vazio para o sinalizador de recurso fornecido. 

## Etapa 3: Escolha os usuários para direcionar

Em seguida, você precisa [direcionar seus esforços]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) escolhendo segmentos ou filtros para restringir seu público. A associação de segmento é calculada quando os flags de recursos são atualizados para um determinado usuário.

{% alert note %}
As alterações são disponibilizadas após a atualização dos recursos de sinalização do seu app, ou quando uma nova sessão é iniciada.
{% endalert %}

## Etapa 4: Distribuir variantes

Escolha a distribuição percentual para o seu experimento. Como uma prática recomendada, você não deve alterar a distribuição após o seu experimento ter sido lançado.

## Etapa 5: atribuir conversões

Braze permite que você acompanhe com que frequência os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), após receberem uma campanha. Especifique uma janela de até 30 dias durante a qual uma conversão será contada se o usuário realizar a ação especificada.

## Etapa 6: Revisar e lançar

Depois de terminar de construir o último do seu experimento, revise os detalhes e clique em **Iniciar Experimento**.



