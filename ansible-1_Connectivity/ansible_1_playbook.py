- hosts: switches
  gather_facts: no
  ansible_network_os: yes

  tasks:
    - name: "Connectivity Check with Control machine by running ios commands"
      ios_command:
        commands:
          - show run | i hostname
