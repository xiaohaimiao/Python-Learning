studentScores = {
    "彭子泷" : {"语文": 90.5, "数学": 92, "英语": 98.5},
    "郝亦程" : {"语文": 90.5, "数学": 92, "英语": 98.5},
    "冯智媛" : {"语文": 90.5, "数学": 92, "英语": 98.5},
}

studentScores["郝亦程"]["语文"] = 97
studentScores["郝亦程"]["数学"] = 98
studentScores["郝亦程"]["英语"] = 98

studentScores["冯智媛"]["语文"] = 99
studentScores["冯智媛"]["数学"] = 97
studentScores["冯智媛"]["英语"] = 100


for i in studentScores:
    print(i + ":", studentScores[i])
    
for i in studentScores.keys():
    print(i + ":", studentScores[i])
    
for i in studentScores.values():
    print(i, i["语文"], i["数学"], i["英语"])

