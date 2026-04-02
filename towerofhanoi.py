def tower(n,fromrod, torod, helperrod):
    if n == 0 :
        return 
    tower(n-1,fromrod,helperrod,torod)
    print(f'Disk: {n} moved from {fromrod} to {torod}' )
    tower(n-1,helperrod,torod,fromrod)

print(tower(3,"A","C","B"))