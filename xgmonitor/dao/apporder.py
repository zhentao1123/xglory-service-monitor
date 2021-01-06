"""
order data
"""

app_price_ords = {
    'log_path': '/data/logs/xglory-fztrip-service-ctrip-price/xglory-fztrip-service-ctrip-price.log',
    'ords': {
        'date': 'date',
    }
}

app_sync_ords = {
    #'log_path': '/data/logs/xglory-fztrip-service-ctrip-sync/xglory-fztrip-service-ctrip-sync.log',
    'log_path': '/Users/ztzhang/fsdownload/sync1.log',
    'ords': {
        'latest_queue_size': "tail -9999 [log_path] | grep 'queue.size' | awk '{print $6}'",
        'time_queue_size': "cat [log_path] | grep 'queue.size' | egrep '[time]' | awk '{print $6}'",
    }
}

app_comm_ords = {
    'time_count': "cat [log_path] | grep '[keyword]' | egrep '[time]' | wc -l",
    'time_count_hour': "cat [log_path] | grep '[keyword]' | egrep '[[hour]]:[0-9]{2}:[0-9]{2}' | wc -l",
    'time_print': "cat [log_path] | grep '[keyword]' | egrep '[time]'",
    'time_print_hour': "cat [log_path] | grep '[keyword]' | egrep '[[hour]]:[0-9]{2}:[0-9]{2}'",
}
