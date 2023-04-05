# def digit(n, d):
#     count = 0
#     for i in range(n+1):
#         square = i**2
#         count += str(square).count(str(d))
#
#     return count
#
# print(digit(2, 2))
#
#
# def mix(s1, s2):
#     counts = {}
#     for char in (s1,s2):
#         if char.islower():
#             if char in counts:
#                 counts[char] += 1
#             else:
#                 counts[char] = 1
#     return counts
#
# def mix(s1, s2):
#     freq1 = [0] * 26
#     freq2 = [0] * 26
#     for ch in s1:
#         if ch.islower():
#             freq1[ord(ch) - ord('a')] += 1
#     for ch in s2:
#         if ch.islower():
#             freq2[ord(ch) - ord('a')] += 1
#     max_freqs = []
#     for i in range(26):
#         ch = chr(ord('a') + i)
#         freq = max(freq1[i], freq2[i])
#         if freq > 1:
#             if freq1[i] > freq2[i]:
#                 max_freqs.append(('1', ch * freq))
#             elif freq2[i] > freq1[i]:
#                 max_freqs.append(('2', ch * freq))
#             else:
#                 max_freqs.append(('=', ch * freq))
#
#     max_freqs.sort(key=lambda x: (-len(x[1]), x[0], x[1]))
#     result = '/'.join(['{}:{}'.format(prefix, freq) for prefix, freq in max_freqs])
#
#     return result
#
# def valid_parentheses(string):
#     count = 0
#     for i in string:
#         if i == "(":
#             count += 1
#         elif i == ")":
#             count -= 1
#             if count < 0:
#                 return False
#     return count == 0


my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

# while True:
#     try:
#         element = next(my_iter)
#         print(element)
#     except StopIteration:
#         break