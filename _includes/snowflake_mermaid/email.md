    EVENT["EMAIL_EVENT"] {
        string id PK
        string campaign_id FK
        string campaign_api_id FK
        string canvas_id FK
        string canvas_api_id FK
        string canvas_step_api_id FK
        string canvas_step_message_variation_api_id FK
        string canvas_variation_api_id FK
        string device_id FK
        string message_variation_api_id FK
        string user_id FK
        string abort_log
        string abort_type
        string app_group_api_id
        string app_group_id
        string attempt_count
        string bounce_reason
        string country
        string deferral_reason
        string dispatch_id
        string email_address
        string esp
        string external_user_id
        string from_domain
        string gender
        string ip_pool
        string is_amp
        string is_drop
        string is_suspected_bot_click
        string language
        string link_alias
        string link_id
        string machine_open
        string message_extras
        string recipient_domain
        string retry_log
        string retry_type
        string send_id
        string sending_ip
        string sf_created_at
        string suspected_bot_click_reason
        string time
        string timezone
        string url
        string user_agent
    }
