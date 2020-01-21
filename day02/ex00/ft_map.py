def ft_map(function_to_apply, list_of_inputs):
    lst = []
    for ele in list_of_inputs:
        lst.append(function_to_apply(ele))
    return (lst)
