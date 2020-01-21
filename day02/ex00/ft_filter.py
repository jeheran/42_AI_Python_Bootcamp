def ft_filter(function_to_apply, list_of_inputs):
    lst = []
    for ele in list_of_inputs:
        if function_to_apply(ele) == True:
            lst.append(ele)
    return lst
