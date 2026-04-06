#!/usr/bin/env python3
import module_script

def main():
    input_name = input("Enter a name: ")

    module_script.greeting(input_name)
#set the environment for this script
#is it main(), or is this a module being called by something else?
if __name__ == "__main__":
    main()