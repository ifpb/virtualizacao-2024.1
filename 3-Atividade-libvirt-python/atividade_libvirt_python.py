import sys
import libvirt

def print_host_info(conn):
    """Imprime informações sobre o host."""
    nodeinfo = conn.getInfo()
    print('\n\nInformações da máquina host: \n')
    vcpus = conn.getMaxVcpus(None) 
    print(f'CPUs existentes: {vcpus}')
    print(f'Número de CPUs ativas: {nodeinfo[2]}')
    print(f'Arquitetura da CPU: {nodeinfo[0]}')

def print_vm_info(conn, vm_name):
    """Imprime informações sobre a máquina virtual (guest)."""
    print('\n\nInformações da máquina virtual (guest): \n')
    vm = conn.lookupByName(vm_name)
    print(f'Nome da máquina virtual: {vm.name()}')
    state, maxmem, mem, cpus, cput = vm.info()
    print(f'Total de memória alocada: {mem/1024:.0f} MB')
    print(f'Número de CPUs alocadas: {cpus}')

    ip = vm.interfaceAddresses(0)
    print("IP da máquina virtual para acesso ssh:", ip['vnet1']['addrs'][0]['addr'])
    print("\n\n")

def main():
    try:
        conn = libvirt.open('qemu:///system')
        print_host_info(conn)
        print_vm_info(conn, "debian-vm1")
    except Exception as e:
        print(repr(e), file=sys.stderr)
        exit(1)

if __name__ == '__main__':
    main()