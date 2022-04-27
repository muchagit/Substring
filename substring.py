def longestSubstr(str):
  dic = {}
  long = ''
  st = 0
  for i in range(len(str)):
    if str[i] in dic and dic[str[i]]+1>st:
        st = dic[str[i]]+1
    dic[str[i]] = i
    tem = str[st:i+1]
    if len(tem) > len(long):
      long = tem
  return len(long)