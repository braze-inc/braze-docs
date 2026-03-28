    EVENT["WEBHOOK_EVENT"] {
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
        string content_length
        string country
        string dispatch_id
        string endpoint_url
        string external_user_id
        string gender
        string host
        string http_status_code
        string is_terminal
        string language
        string message_extras
        string raw_response
        string retry_count
        string retry_log
        string retry_type
        string send_id
        string sf_created_at
        string time
        string timezone
        string url_path
        string webhook_duration
        string webhook_failure_source
    }
