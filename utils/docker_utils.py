import docker

def get_docker_ports():
    client = docker.from_env()
    containers = client.containers.list()
    ports = []

    for container in containers:
        container_ports = container.attrs['NetworkSettings']['Ports']
        for port, mappings in container_ports.items():
            if mappings:
                for mapping in mappings:
                    ports.append({
                        'ip': mapping['HostIp'],
                        'port': int(mapping['HostPort']),
                        'description': container.name,
                        'port_protocol': 'TCP' if '/tcp' in port else 'UDP'
                    })

    return ports