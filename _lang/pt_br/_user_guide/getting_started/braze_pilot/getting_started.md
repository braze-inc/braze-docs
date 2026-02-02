---
nav_title: Primeiros passos
article_title: Primeiros passos com o Braze Pilot
page_order: 2
page_type: reference
description: "Este artigo de referência aborda brevemente as etapas de integração exigidas de seus engenheiros ou desenvolvedores."
---

# Comece a usar o Braze Pilot

> Este artigo aborda como começar a usar o Braze Pilot. Aqui, vamos orientá-lo a baixar o app, inicializar a conexão com seu dashboard do Braze e concluir a configuração.

## Etapa 1: Baixar Braze Pilot

Para começar a usar o Braze Pilot, primeiro você precisa baixar o aplicativo na Apple App Store ou na Google Play Store. Você pode procurar o app na loja de aplicativos ou digitalizar os códigos QR abaixo para visitar a página do app para seu dispositivo.

## Etapa 2: Aceitar os termos e condições

Em seguida, aceite os termos e condições e insira seu e-mail de trabalho no formulário. Seu e-mail será usado apenas para análise de dados de uso do app e não será usado para fins de marketing.

![Página de boas-vindas do Braze Pilot.]({% image_buster /assets/img/braze_pilot/pilot_welcome.png %}){:style="max-width:30%"} ![Opção para inserir seu endereço de e-mail comercial.]({% image_buster /assets/img/braze_pilot/pilot_signin.png %}){:style="max-width:30%"}

## Etapa 3: Inicializar a conexão com o SDK do Braze

O Braze Pilot o capacita a inicializar o Braze SDK em qualquer dashboard Braze. Depois que o SDK for inicializado, o Pilot começará a enviar dados de engajamento para o Braze e permitirá que você dispare qualquer envio de mensagens iniciado a partir desse dashboard do Braze.

Há dois métodos para configurar a conexão do SDK no Pilot: Códigos QR de demonstração e o assistente de configuração.

{% tabs local %}
{% tab Demo QR codes %}

### Método 1: Códigos QR de demonstração

Digitalize um código QR que inclui todos os detalhes necessários para inicializar o SDK, criar seu perfil de usuário e fazer um deep linking para uma simulação de app específica no Braze Pilot. Os códigos QR de demonstração são renderizados na gaveta complementar para campanhas de demonstração específicas em sua avaliação gratuita.

| Piloto para Android | Piloto para iOS |
| --- | --- |
| ![Código QR para Android.]({% image_buster /assets/img/braze_pilot/android_qr_code.png %}){:style="max-width:60%"} | ![Código QR para iOS.]({% image_buster /assets/img/braze_pilot/ios_qr_code.png %}){:style="max-width:60%"} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Setup wizard %}

### Método 2: Assistente de configuração

Siga um guia passo a passo para inicializar a conexão com seu espaço de trabalho do painel na página **App Settings (Configurações do aplicativo** ) em seu painel do Braze.

![Etapa 1 do assistente de configuração do Braze Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Essa conexão é específica do espaço de trabalho. Isso significa que, se você inicializar a conexão a partir do espaço de trabalho de demonstração e depois mudar para o espaço de trabalho ativo no dashboard de avaliação gratuita, precisará reinicializar o SDK a partir desse espaço de trabalho para receber quaisquer campanhas lançadas lá.

![O menu suspenso do espaço de trabalho no dashboard do Braze com "Demo - Braze" selecionado como o espaço de trabalho ativo.]({% image_buster /assets/img/braze_pilot/dashboard_workspace.png %}){:style="max-width:60%"}

{% endtab %}
{% endtabs %}

## Etapa 4: Permitir permissões push

Por fim, recomenda-se que você permita que o aplicativo envie permissões push se quiser testar os recursos push por meio do app. Você pode conceder essas permissões ao aplicativo das seguintes maneiras: atualizando as configurações do aplicativo nas configurações do dispositivo ou iniciando uma mensagem push do Braze para o aplicativo.

{% tabs local %}
{% tab Update the settings for the app %}

Abra as configurações de seu dispositivo e localize o Braze Pilot. Em seguida, atualize as configurações para permitir que as notificações apareçam na tela de bloqueio.

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/device_settings.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Launch a push primer message %}

Você pode usar uma mensagem no app do Braze para solicitar permissões push para o aplicativo, assim como faria para seus próprios consumidores. Para saber como criar esse tipo de mensagem no Braze, consulte [Mensagens no app do push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages#push-primer-in-app-messages).

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/push_primer1.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## Etapa 5: Experiência de mensagens Braze no piloto

Agora você está pronto para começar a receber campanhas e telas do seu dashboard do Braze como usuário do Braze Pilot! Visite qualquer uma das campanhas lançadas em seu espaço de trabalho de demonstração para obter uma demonstração rápida dos casos de uso do Braze e, em seguida, vá para o espaço de trabalho ativo para começar a enviar suas próprias campanhas.

Para obter mais informações sobre como configurar campanhas e canvas no Braze, consulte [Getting Started: Campanhas e telas]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases).