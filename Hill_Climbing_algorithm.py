Graph={
    'A':[20,[['B',15],['C',12],['D',17]]],
    'B':[15,[['E',1],['F',8]]],
    'C':[12,[['G',14],['H',10]]],
    'D':[17,[['I',12],['J',11]]],
    'E':[1,[['L',11]]],
    'F':[8,[]],
    'G':[14,[]],
    'H':[10,[['O',3],['P',0]]],
    'I':[12,[['P',0],['Q',14]]],
    'J':[11,[['R',13]]],
    'L':[3,[]],
    'O':[3,[]],
    'P':[0,[]],
    'Q':[14,[]],
    'R':[13,[]]
}



#Graph['X'][0] heuristic of parant
#Graph['X'][1] children of parant

cs , found, path ='A', False, []
Goal=input('>> ')
while not found:
    path.append(cs)
    if cs==Goal:
        print(path)
        break
    
    Heuristics_of_cs=Graph[cs][0]
    children_of_cs=Graph[cs][1]
    
    if children_of_cs==[]:
        print('fail')
        break
    else:
        Best_Heuristic=None
        child_heuristics=[]
        
        for child in children_of_cs:
            child_heuristics.append(child[1])
            if child[0] in path:
                path.remove(child[0])

        Best_Heuristic=min(child_heuristics)
        Index_of_Best_Heuristics=child_heuristics.index(Best_Heuristic)
        
        if Best_Heuristic<Heuristics_of_cs:
            cs=children_of_cs[Index_of_Best_Heuristics][0]
        else:
            print('fail')
            break