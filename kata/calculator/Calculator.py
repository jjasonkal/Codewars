class Calculator(object):
  def evaluate(self, string):
    a=string.split(" ")
    ans=0
    for y in range(a.count("*")+a.count("/")):
        for x in range(len(a)):
            if a[x]=="*":
                ans=float(a[x-1])
                ans*=float(a[x+1])
                a.pop(x-1)
                a.pop(x-1)
                a.pop(x-1)
                a.insert(x-1,ans)
                break
            elif a[x]=="/":
                ans=float(a[x-1])
                ans/=float(a[x+1])
                a.pop(x-1)
                a.pop(x-1)
                a.pop(x-1)
                a.insert(x-1,ans)
                break

    ans=float(a[0])
    for x in range(1,len(a)):
        if a[x]=="+":
            ans+=float(a[x+1])
        elif a[x]=="-":
            ans-=float(a[x+1])
    return ans

