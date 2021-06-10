- host: switches
  gather_facts: no

  tasks:
     - name: "Connectivity check with control machine"
       iso_command:
          commands:
             - show run | i hostnmae

          register: output

     - name: show output
       when: 'hostname' in "{{output.stdout}}"
       debug:
          msg: {{output}} 
