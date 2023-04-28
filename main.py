# a = []
# with open('17.txt', 'r') as f:
#     for i in f:
#         a += [int(i[:-1])]
# c = []
# m = []
# for i in a:
#     l = 1
#     o = list(str(i))
#     y = sorted(list(str(i)))
#     for j in o:
#         for k in y:
#             if o.count(j) != 1 or y.count(k) != 1:
#                 l = 0
#     if l == 1:
#         if list(str(i)) == sorted(list(str(i)), reverse=True):
#             c += [i]
#             print(c)
# cm = min(c)
# print(cm)
# s = 0
# for i in str(cm):
#     s += int(i)
# print(s)
# for i in range(len(a) - 1):
#     b = list(str(a[i]))
#     g = list(str(a[i + 1]))
#     l = 1
#     for j in b:
#         for k in g:
#             if b.count(j) != 1 or g.count(k) != 1:
#                 l = 0
#                 if l == 1:
#                     b1 = sorted(b)
#                     g1 = sorted(g)
#         if ((b == b1 and g != g1) or (b != b1 and g == g1)) and (a[i] * a[i + 1]) % s == 0:
#             m += [a[i] + a[i + 1]]
# print(len(set(m)), min(m))


s = '123456'

if s.count('1') == 1:
    ...
    