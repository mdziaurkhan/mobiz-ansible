- host: switches
  gather_facts: no
  ansible_network_os: yes

  tasks:
     - name: "Connectivity check with control machine"
       iso_command:
          commands:
             - show run | i hostname

          register: output

     - name: show output
       #when: "hostname" in "{{output.stdout}}"
       debug:
          msg: {{output}}
