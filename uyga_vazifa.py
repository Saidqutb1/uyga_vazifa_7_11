#1 Sum Array with different bases

def sum_it_up(a):
    return sum(int(*x) for x in a)

#2 Stem-and-leaf plot

def stem_and_leaf(d):
    d = list(map(str,d))
    d, m = [i if len(i)!=1 else '0'+i for i in d], {}
    for j in range(10):
        b = sorted(list(map(int,[i[1:] for i in d if i[0]==str(j)])))
        if b:
            m[j] = b
    return m


#3 Replace all items

def replace_all(obj, find, replace):
  if isinstance(obj, str):
    return obj.replace(find, replace)
  elif isinstance(obj, list):
    return [x if x != find else replace for x in obj]


#4 Reverse and Invert

def reverse_invert(lst):
    return [(-1,1)[x<0]*int(str(abs(x))[::-1]) for x in lst if isinstance(x,int)]


#5 Candy problem

def candies(s):
    if not s or len(s) == 1:
        return -1
    return len(s) * max(s) - sum(s)
