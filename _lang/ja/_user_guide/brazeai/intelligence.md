---
nav_title: Intelligence Suite
article_title: Intelligence Suite
page_order: 10
layout: dev_guide
search_rank: 12
guide_top_header: "Intelligence Suite"
guide_top_text: "Braze Intelligence Suite は、データに基づくインサイトで意思決定の自動化を支援します。配信時間から多変量テストまで、ブランドはこれらのツールと機能を使用して、大規模に最適化されるダイナミックなクロスチャネルのエクスペリエンスを構築できます。<br> <br> Intelligence Suite は、インテリジェントタイミング、インテリジェントチャネル、インテリジェントセレクションの 3 つの主要機能で構成されています。"
description: "Braze Intelligence Suite は、データに基づくインサイトで意思決定の自動化を支援します。配信時間から多変量テストまで、ブランドはこれらのツールと機能を使用して、大規模に最適化されるダイナミックなクロスチャネルのエクスペリエンスを構築できます。"

Tool:
  - Dashboard

guide_featured_title: "ツールと機能"
guide_featured_list:
- name: インテリジェントタイミング
  link: /docs/user_guide/brazeai/intelligence/intelligent_timing/
  image: /assets/img/braze_icons/clock.svg
- name: インテリジェントチャネル
  link: /docs/user_guide/brazeai/intelligence/intelligent_channel/
  image: /assets/img/braze_icons/mail-04.svg
- name: インテリジェントセレクション
  link: /docs/user_guide/brazeai/intelligence/intelligent_selection/
  image: /assets/img/braze_icons/hearts.svg

guide_menu_title: "Additional resources"
guide_menu_list:
- name: インテリジェンスに関する FAQ
  link: /docs/user_guide/brazeai/intelligence/faqs/
  image: /assets/img/braze_icons/annotation-question.svg


---

## ユースケース

Intelligence Suite は、ユーザー履歴やキャンペーン、キャンバスのパフォーマンスを分析し、エンゲージメント、視聴率、コンバージョンを高めるための自動調整を行う強力な機能を備えています。これらの機能がさまざまな業種にもたらすメリットについて、以下のユースケースをご覧ください。

### e コマース

- **フラッシュセール:**[インテリジェントチャネルフィルター]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/)を使用してユーザー履歴を調査し、メールよりプッシュ通知への反応が高いユーザーを特定してから、それぞれのユーザーにプッシュ通知とメールを送信します。オプションとして、好みのチャネルを決定するために十分なデータのないユーザー向けに、特定のチャネルを選択します。
- **プロモーション用バナー:**[インテリジェントセレクションを]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/)使用して、定期キャンペーンのさまざまなプロモーションバナーのパフォーマンスを分析し、最もクリック率の高いバナーを自動的に選択して送信します。

### 旅行

- **パッケージの提示:**インテリジェントセレクションを使用して、繰り返し発生するキャンバスでさまざまな旅行パッケージの提示をテストし、最もパフォーマンスの高いバリアントにキャンバスのトラフィックを徐々に移動することで、より高い予約率を促進します。
- **お得な旅行情報:**インテリジェントチャネルフィルターを使用して、パーソナライズされた旅行情報をメールや SMS など、ユーザーの最もアクティブなチャネルを通じて送信し、ユーザーがメッセージングにエンゲージする可能性を最大限に高めます。

### エンターテイメント

- **新コンテンツのプロモーション:**[インテリジェントタイミングを]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)使用して、ユーザーがメッセージングを開封する可能性が最も高いときに、新しい映画、番組、音楽、その他のタイプのコンテンツに関する通知を送信します。
- **ゲーム内購入:**インテリジェントセレクションを使用して、ゲーム内購入に向けたさまざまなプロモーションメッセージをテストし、最も高いコンバージョン率が得られたものを自動的に選択します。

### クイックサービスレストラン

勤務している SandwichEmperor というファストフード店に、期間限定の新メニューアイテム「Royal Roast」があるとします。Intelligence Suite の 2 つの機能を使用して、キャンバスのパーソナライズされたプロモーションを送信します。

#### インテリジェントタイミングによる通知の送信時間の決定

インテリジェントタイミングを使用して、当店のアプリと各メッセージングチャネルに対するユーザーの過去のインタラクションを分析し、各ユーザーに Royal Roast を宣伝する最適なタイミングを自動的に選択します。午後にプロモーションを受信するユーザーもいれば、夕方に受信するユーザーもいるでしょう。 

分析するために十分な過去のインタラクションがないユーザーには、フォールバック時刻 (ユーザー全体でアプリが使用される最も一般的な時間) を指定します。

![メッセージステップのインテリジェントタイミングによる配信設定。][1]

#### インテリジェントセレクションによるプロモーションの選択

実際の販促メッセージについては、インテリジェントセレクションを使用して、Royal Roast 用の 3 種類のメッセージ (プッシュ通知、メール、SMS) をテストします。インテリジェントセレクションは、すべてのプロモーションメッセージのパフォーマンスを 1 日 2 回分析し、最もパフォーマンスの高いメッセージを徐々に多く送信し、その他のメッセージを少なくします。

インテリジェントセレクションは、十分なデータを収集して最もパフォーマンスの高いメッセージを決定した後、送信するメッセージの 100% にそのメッセージを使用します。

![インテリジェントセレクションを有効にしたキャンバスの [ABテスト] セクション。][3]

#### キャンバスの開始

インテリジェントタイミングとインテリジェントセレクションの両方を使用して、Royal Roast のプロモーションのタイミングとメッセージングが最適化されるように設定しました。キャンバスを開始して、ユーザーの好みに合わせて送信が変化していく様子を確認できます。

[1]: {% image_buster /assets/img/intelligence_suite1.png %}
[3]: {% image_buster /assets/img/intelligent_selection_canvas.png %}
