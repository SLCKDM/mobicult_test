broker_url = "redis://127.0.0.1:6379"
result_backend = "redis://127.0.0.1:6379"
accept_content = ["application/json"]
task_serializer = "json"
result_serializer = "json"
broker_connection_retry = True
broker_connection_retry_on_startup = True