# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 06:55:34 2023

@author: joshf
"""


import utils.helper_funcs as hf

test = {
       "expect": {
            "to": {
              "equal": hf.equal,  
              "be": {
                  "above": hf.above,
                  "below": hf.below,
                  "closeTo": hf.close_to
                  }
            },
        }
      }
                 