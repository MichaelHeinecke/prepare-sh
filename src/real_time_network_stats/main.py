NETWORK_DATA = {
    'time_1': {'bytes_sent': 1000, 'bytes_recv': 2000, 'packets_sent': 50, 'packets_recv': 60},
    'time_2': {'bytes_sent': 1500, 'bytes_recv': 2500, 'packets_sent': 70, 'packets_recv': 80},
    'time_3': {'bytes_sent': 2000, 'bytes_recv': 3000, 'packets_sent': 90, 'packets_recv': 100},
    'time_4': {'bytes_sent': 50000, 'bytes_recv': 60000, 'packets_sent': 500, 'packets_recv': 600}
}

# Pre-calculate totals to avoid O(n^2) time-complexity in func
total_bytes_sent = sum(v['bytes_sent'] for v in NETWORK_DATA.values())
total_bytes_recv = sum(v['bytes_recv'] for v in NETWORK_DATA.values())
num_records = len(NETWORK_DATA) - 1

def detect_network_anomalies(time_period: str) -> bool:
    period_data = NETWORK_DATA[time_period]
    other_bytes_sent = total_bytes_sent - period_data['bytes_sent']
    other_bytes_recv = total_bytes_recv - period_data['bytes_recv']

    bytes_sent_threshold = (other_bytes_sent / num_records) * 5
    bytes_received_threshold = (other_bytes_recv / num_records) * 5

    return (
            period_data['bytes_sent'] > bytes_sent_threshold  or
            period_data['bytes_recv'] > bytes_received_threshold
    )


if __name__ == '__main__':
    for k in NETWORK_DATA:
        print(detect_network_anomalies(k))
