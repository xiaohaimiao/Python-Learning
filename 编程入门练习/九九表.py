
def JiuJiuBiao(isChinese = True):
    if not isChinese:
        # 数字九九表
        for i in range(1, 9 + 1):
            for j in range(1, i + 1):
                print(str(j) + "x" + str(i) + "=" + str(i * j).ljust(2, " "), "", end="")       
            print()
        return
    # 中文九九表
    z = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']    
    for i in range(1, 9 + 1):
        for j in range(1, i + 1):
            #print(str(i) + "x" + str(j) + "=" + str(i*j).ljust(2, " "), "", end="")       

            shiwei = (i * j) // 10
            gewei = (i * j) % 10
            strShiwei = z[shiwei]
            strGewei = z[gewei]
            if shiwei == 0: strShiwei = ""
            if gewei == 0: strGewei = ""
            if shiwei > 1: strShiwei += "十"
            if shiwei == 1: strShiwei = "十"
            de = "得"
            if shiwei > 0: de = "" 
            #print(z[j] + z[i] + de + strShiwei + strGewei, "", end="")
            print(f"{z[j]}{z[i]}{de}{strShiwei}{strGewei}", "", end="")         
        print()
    return    

JiuJiuBiao()    
JiuJiuBiao(False)    
    