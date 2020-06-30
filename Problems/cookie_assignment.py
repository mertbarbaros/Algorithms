"""
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi,
which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and 
the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

Note:
You may assume the greed factor is always positive.
You cannot assign more than one cookie to one child.

Input: [1,2,3], [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

You can maximize the number of satisfied children by dividing one cookie into 2.



"""


#define g for children and s for cookies
kids = [2,3,5,3]
cookies = [1,3,6]

#we will match the cookies and kids which are satisfied the s[j] >= g[i] condition
def option_1(g, s):
    #if any of the arrays empty, return zero and not proceed  
    if not g or not s:
        return 0
   #sort the kids (g) and cookies (s)
    g.sort()
    s.sort()
    #i is index num. of g, j is index num. of s and counter is the num of matched kids and cookies
    i, j, counter = 0, 0, 0
    #can't be greater than the length of the list, if condition satisfied increase the values by 1
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            counter += 1
            i += 1
            j += 1
        else:
            j += 1
    return counter


def option_2(g,s):
    # work with the copy of the kids for not changing the global value
    g = g.copy()
    g.sort()
    s.sort()
    #kid that we couldn't match = f list
    f = []

    for i in range(len(g)):
        kid = g.pop()
        if kid not in s:
            f.append(kid)
        #if the kid's value is matching with the cookie c, then we should remove it from the cookie list.
        else:
            for c in s:
                if kid == c:
                    s.remove(c)
                    continue
    z = []
    for c in s:
        #divide all the unmatched cookies by 2
        val = (c /2)
        z.append(val)
        z.append(val)

    last_total = len(kids) - len(f)
    #send the new f (kids) and z(cookies) with unmatched elements to the Option_1 function and calculate the new matches
    op = option_1(f,z)
    #number of total kids that satisfied (exactly matched elements + elements match with new list)
    last_total += op

    return last_total

#number of kids that we satisfied in option 1
a = option_1(kids,cookies)
#number of kids that we satisfied in option 2
b = option_2(kids,cookies)

#number of satisfied kids is the maximum of option_1 and option_2
print(max(a,b))
