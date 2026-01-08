
{% tab Android %}
O Braze oferece vários tipos de mensagens no app padrão, cada uma personalizável com mensagens, imagens, ícones [Font Awesome](https://fontawesome.com/icons?d=gallery&p=2), ações de clique, análises de dados, esquemas de cores e muito mais.

Seu comportamento básico e suas características são definidos pela [`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html) em uma subclasse chamada [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html). `IInAppMessage` também inclui uma subinterface, [`IInAppMessageImmersive`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-immersive/index.html)que permite adicionar [botões](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) de fechar, de ação de clique e de análise de dados ao seu app.

{% alert important %}
Lembre-se de que as mensagens no app que contêm botões incluirão a mensagem `clickAction` na carga útil final se a ação de clique for adicionada antes da adição do texto do botão.
{% endalert %}

{% subtabs local %}
{% subtab Slideup %}
[`slideup`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html) As mensagens no app são assim chamadas porque "deslizam para cima" ou "deslizam para baixo" a partir da parte superior ou inferior da tela. Eles cobrem uma pequena parte da tela e fornecem um recurso de envio de mensagens eficaz e não intrusivo.

O objeto de mensagem no app `slideup` estende [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html).

![Uma mensagem no app que desliza da parte inferior da tela do telefone exibindo "Os seres humanos são complicados. O engajamento personalizado não deveria ser." Em segundo plano, a mesma mensagem no app exibida no canto inferior direito de uma página da Internet.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endsubtab %}
{% subtab Modal %}
[`modal`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html) As mensagens no app aparecem no centro da tela e são emolduradas por um painel translúcido. Úteis para o envio de mensagens mais críticas, eles podem ser equipados com dois botões de ação por clique e com análise de dados ativada.

Esse tipo de mensagem é uma subclasse de [`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html)uma classe abstrata que implementa `IInAppMessageImmersive`, dando-lhe a opção de adicionar funcionalidade personalizada às mensagens no app geradas localmente.

![Uma mensagem modal no app no centro da tela do telefone exibindo "Os seres humanos são complicados. O engajamento personalizado não deveria ser." No plano de fundo está a mesma mensagem no app exibida no centro de uma página da Internet.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endsubtab %}
{% subtab Full Screen %}
[`full`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html) As mensagens no app são úteis para maximizar o conteúdo e o impacto da sua comunicação com o usuário. A metade superior de uma mensagem no app `full` contém uma imagem, e a metade inferior exibe texto e até dois botões de ação de clique e de análise de dados.

Esse tipo de mensagem estende [`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html)dando-lhe a opção de adicionar funcionalidade personalizada às mensagens no app geradas localmente.

![Uma mensagem no app de tela cheia exibida em toda a tela do telefone mostrando: "Os humanos são complicados." O engajamento personalizado não deveria ser." No plano de fundo está a mesma mensagem no app exibida em grande parte no centro de uma página da Internet.]({% image_buster /assets/img_archive/In-App_Full.png %})

{% endsubtab %}
{% subtab Custom HTML %}
[`HTML`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html) As mensagens no app são úteis para criar conteúdo totalmente personalizado para o usuário. O conteúdo HTML definido pelo usuário da mensagem no app é exibido em `WebView` e pode, opcionalmente, conter outros conteúdos avançados, como imagens e fontes, permitindo controle total sobre a aparência e a funcionalidade da mensagem.

Esse tipo de mensagem implementa [`IInAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-html/index.html)que é uma subclasse de [`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html).

As mensagens no app do Android suportam uma interface JavaScript `brazeBridge` para chamar métodos no Braze Android SDK a partir do seu HTML; consulte nossa página de <a href="{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages#javascript-bridge/">ponte JavaScript</a> para obter mais detalhes.

![Uma mensagem no app em HTML com um carrossel de conteúdo e botões interativos.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% alert important %}
Atualmente, não oferecemos suporte à exibição de mensagens no app em HTML personalizado em um iFrame nas plataformas iOS e Android.
{% endalert %} 

{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
Você também pode definir exibições personalizadas de mensagens no app para o seu aplicativo. Para obter um passo a passo completo, consulte [Configuração de fábricas personalizadas]({{site.baseurl}}/developer_guide/in_app_messages/customization#android_setting-custom-factories).
{% endalert %}
{% endtab %}