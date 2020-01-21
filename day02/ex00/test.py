import fct
import ft_map
import ft_filter
import ft_reduce
a = [4, 5, 3]

#print("ft_map :")
#print(ft_map.ft_map(fct.add_2, a))
#print("ft_filter :" + ft_filter.ft_filter(fct.filterVowels, a))

#print(filter(fct.filterVowels, ['a', 'b', 'c', 'e']))
#b = ft_filter.ft_filter(fct.filterVowels, ['a', 'b', 'c', 'e'])
#for el in b:
#    print(el)

c = ft_reduce.ft_reduce(fct.add, a)

print(c)
