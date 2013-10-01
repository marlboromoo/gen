#!/usr/bin/env python
# encoding: utf-8

"""
                    ___           ___                 
                   /  /\         /  /\          ___   
                  /  /:/_       /  /:/_        /  /\  
  ___     ___    /  /:/ /\     /  /:/ /\      /  /:/  
 /__/\   /  /\  /  /:/ /:/_   /  /:/ /:/_    /  /:/   
 \  \:\ /  /:/ /__/:/ /:/ /\ /__/:/ /:/ /\  /  /::\   
  \  \:\  /:/  \  \:\/:/ /:/ \  \:\/:/ /:/ /__/:/\:\  
   \  \:\/:/    \  \::/ /:/   \  \::/ /:/  \__\/  \:\ 
    \  \::/      \  \:\/:/     \  \:\/:/        \  \:\
     \__\/        \  \::/       \  \::/          \__\/
                   \__\/         \__\/                

"""

import sys
import string

def main():
    leet = string.maketrans('AaBbeghiloprSstz', '4@8636#!10925$72')
    s = sys.argv[1]
    print s.translate(leet)

if __name__ == '__main__':
    main()
