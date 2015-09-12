def atoi(self, str):
  number="0123456789"
  stri=str.strip()
  if len(stri)==0:return 0
  else:
          if stri[0] not in number and stri[0]!='-' and stri[0]!='+':
                    return 0
          elif stri[0]=='-'or stri[0]=='+':
                    i=1
                    while(i<len(stri)and stri[i] in number):
                              i=i+1
                    if i==1:
                              return 0
                    else:
                              integer=int(stri[:i])
                              if integer<-0x80000000:
                                        return -0x80000000
                              
                              elif integer>0x7fffffff:
                                        return 0x7fffffff
                              else:
                                        return integer
                              
          else:
                    i=1
                    while(i<len(stri) and stri[i] in number):
                              i=i+1
                    if i==1:
                              return int(stri[0])
                    else:
                              integer=int(stri[:i])
                              if(integer>0x7fffffff):
                                        return 0x7fffffff
                              else:
                                        return integer

atoi('+-2')