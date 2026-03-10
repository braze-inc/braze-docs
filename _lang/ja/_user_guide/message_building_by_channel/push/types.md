---
nav_title: "プッシュ通知の種類"
article_title: プッシュ通知の種類
page_order: 1
page_type: glossary
description: "この用語集には、Brazeで送信できるプッシュ通知の種類が記載されている。"
channel: push

layout: glossary_page
glossary_top_header: "プッシュ通知の種類"
glossary_top_text: "顧客とやり取りするために利用できるプッシュ通知には様々な種類がある。これらをチャネルごとに絞り込み、様々なユーザーのニーズに応えることができる。これらの設定の大半はプッシュキャンペーン内で設定できる。ただし、以下の説明にはバックエンド設定が必要かどうか、またその内容について注記がある。"

glossary_tag_name: Channels
glossary_filter_text: "Select any of the following channels to narrow Push Type options."

# category to icon/fa or image mapping
glossary_tags:
  - name: Web
  - name: Android
  - name: iOS

glossaries:
  - name: "レギュラープッシュ"
    description: "包括的なプッシュ・メッセージだ。ユーザーのデバイスで通知音を送出し、通知バーやスタックにメッセージをスライド表示します。"
    tags:
      - Web
      - Android
      - iOS
  - name: "ウェブプッシュ"
    description: "これらのプッシュメッセージは、ウェブアプリやブラウザに表示される。それでも、顧客にリーチするには許可が必要です。ユーザーが非表示のブラウザーを使用している場合、ウェブ・プッシュは機能しないことに注意。"
    tags:
      - Web
  - name: "プッシュプライマーキャンペーン"
    description: "ユーザーからプッシュ通知の明示的なオプトインまたはオプトアウトの意志を確認するために使用されるアプリ内メッセージのキャンペーン。プライマーを通じて、デバイスの設定でプッシュをオフにしている可能性の高いユーザーへの通知送信を避けることができる。iOS の場合、プッシュ通知のキャンペーンが重要です。これは、ユーザーが明示的に iOS のネイティブプッシュプロンプトにオプトインするまで、フォアグラウンドのプッシュ通知 (デバイスをスリープ解除する通知など) が有効にならないためです。"
    tags:
      - Web
      - Android
      - iOS
  - name: "プッシュ通知ストーリー"
    description: "プッシュストーリーは、カルーセルの形でユーザーを視覚的な旅に誘う没入型のメッセージだ。これらはモバイルデバイスでのみ使用できます。"
    tags:
      - iOS
      - Android
  - name: "アクションボタンによるプッシュ通知"
    description: "プッシュ・ウィズ・アクション・ボタンは、ユーザーに選択肢を提供し、いくつかの行動を呼びかけることができるメッセージだ。"
    tags:
      - Web
      - Android
      - iOS
  - name: "リッチなプッシュ通知"
    description: "リッチプッシュ通知とは、単純なアイコンと行動喚起のテキストだけでなく、没入感のある画像やクリエイティブなコンテンツを含む通知である。"
    tags:
      - iOS
      - Android
  - name: "iOS 向けの暫定プッシュ通知"
    description: "iOS 12でAppleが導入した仮承認機能は、iOSアプリのインストール時に自動的に発生する。これによりブランドは、ユーザーにプッシュ通知の許可プロンプトを表示せずに通知を送信できる。これらの通知は通知センターに静かに配信される。ユーザーはそこでプッシュ通知を許可するか停止するかを選択できる。"
    tags:
      - iOS
  - name: "HTML プッシュ通知"
    description: "HTMLプッシュ通知は、HTMLでハードコーディングされたプッシュメッセージで、Brazeが提供するあらかじめ設定されたプッシュテンプレートを使用しない。HTMLプッシュ通知を作成するオプションがあることで、プッシュメッセージをどのように見せるかに関して、御社は完全な創造的自由と一貫したブランディングを持つことができる。"
    tags:
      - Android
  - name: "通知IDとチャンネルID"
    description: "通知 ID とチャネル ID を使用すると、ユーザーがすでに受信したが開封していないプッシュ通知を置き換えたり更新したりできます。"
    tags:
      - iOS
      - Android
  - name: "バックグラウンドプッシュ通知（サイレントプッシュ）"
    description: "エンドユーザーには表示されないプッシュ通知であり、主に内部で利用される。アンインストール追跡、ジオフェンス、データ同期といった機能の処理に用いられる。バックグラウンドプッシュとサイレントプッシュは同じ概念を指す。バックグラウンド対応のプッシュトークンが必要だ。詳しくは、<a href=\"/docs/developer_guide/push_notifications/silent\">サイレント・プッシュ</a>通知を参照のこと。"
    tags:
      - Web
      - Android
      - iOS
  - name: "ウェアラブルプッシュ通知"
    description: "これらのプッシュ通知によって、ブランドはApple Watchのようなウェアラブル端末に直接メッセージを送ることができる。"
    tags:
      - iOS

---
