#!/usr/bin/env python3

def greeting(name):
    print(f"Hello from the module_script() module, {name}")

#set the environment for this script
#is it main(), or is this a module being called by something else?
if __name__ == "__main__":
    main()