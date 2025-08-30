from collections import defaultdict

def map_service_dependencies(config_data: str) -> dict:
    # Parse input: Ignore empty lines and lines starting with #
    services_raw = [e for e in config_data.split('\n') if  e != '' and not e.startswith('#')]

    # For each element, {key: {depends_on: [], required_by: []}}
    services = defaultdict(lambda: {'depends_on': [], 'required_by': []})
    for e in services_raw:
        service = e.split(':')
        key = service[0].strip()
        values = [v.strip() for v in service[1].split(',') if v.strip()]
        values.sort()
        services[key]['depends_on'].extend(values)
        for v in values:
            services[v]['required_by'].append(key)

    # return {k: {'depends_on': sorted(v['depends_on']), 'required_by': v['required_by']} for k, v in services.items()}
    return services

if __name__ == '__main__':
    input_1 = 'serviceA: serviceB, serviceC\nserviceB: serviceD\nserviceC: serviceD, serviceE\nserviceD:\nserviceE: serviceF\nserviceF:'
    print(map_service_dependencies(input_1))

    input_2 = 'auth: database, cache\ndatabase:\ncache: database\napi: auth, cache\nui: api'
    print(map_service_dependencies(input_2))
