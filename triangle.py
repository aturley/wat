#!/usr/bin/env python


print "\n".join(x.rstrip() for x in (lambda y: y(y,3,3))\
    (lambda x,n,w: ["%s/%s\\%s"%(" "*j, " "*(2*i)," "*j)\
    for (i,j) in zip(xrange(0,w),xrange(w-1,0,-1))]+\
    ["%s"%("-"*w*2)] if n == 0 else ["%s%s%s"%(" "*(w*2**\
    (n-1)), l, " "*(w*2**(n-1))) for l in x(x,n-1,w)]+\
    ["%s%s"%(l,l) for l in x(x,n-1,w)]))
"""
                           /\
                          /  \
                         ------
                        /\    /\
                       /  \  /  \
                      ------------
                     /\          /\
                    /  \        /  \
                   ------      ------
                  /\    /\    /\    /\
                 /  \  /  \  /  \  /  \
                ------------------------
               /\                      /\
              /  \                    /  \
             ------                  ------
            /\    /\                /\    /\
           /  \  /  \              /  \  /  \
          ------------            ------------
         /\          /\          /\          /\
        /  \        /  \        /  \        /  \
       ------      ------      ------      ------
      /\    /\    /\    /\    /\    /\    /\    /\
     /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \
    ------------------------------------------------
"""
