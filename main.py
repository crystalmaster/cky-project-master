import re
import tkinter as tk
import ui
#base
def create_cnf(file_name):
    file = open(file_name, "r",encoding='utf-8-sig') # ,encoding="utf-8"
    line = file.readline()

    cnf = dict()

    while line != '':
        arr = re.sub("->"," ",line).split()
        key = tuple(arr[1:])
        if key in cnf.keys():
            cnf[key] = cnf[key] + arr[:1]
        else: 
            cnf[key] = arr[:1]
        line = file.readline()
    return cnf
#CKY algorithm
def CKY(sentence, cnf, container, check):
    size_of_sentence = len(sentence)
    table = [[' ' for x in range (size_of_sentence)] for y in range(size_of_sentence)]
    result = [[' ' for x in range (size_of_sentence)] for y in range(size_of_sentence)]
    for k in range (1,size_of_sentence + 1):
        table[k-1][k-1] = cnf[(sentence[k-1],)]
        result[k-1][k-1] = cnf[(sentence[k-1],)]
        if(check == 0):
            ui.drawTable(table,sentence,1)
        
        for i in range (k - 2, -1, -1):
            for j in range (1, k):
                if table[i][j-1] != ' ' :
                    for a in table[i][j-1]:
                        for b in table[j][k-1]:
                            key = [a,b]
                            if tuple(key) in cnf.keys():
                                x = str(i) + " "+ str(j)
                                y = str(j) + " "+ str(k)
                                value = ['.'.join(cnf[tuple(key)]), x , y]
                                if table[i][k-1] == ' ' :
                                    table[i][k-1] = value
                                    result[i][k-1] = value
                                else:
                                    table[i][k-1] = table[i][k-1] + value
                                if(check == 0):
                                    ui.drawTable(table,sentence,1)
                
    # for k in range(size_of_sentence):
    #     print(table[k])
    return result
#main 

def MainView (frame):
    sentences = tk.StringVar()
    buttonframe = tk.Frame()
    container = tk.Frame()

    buttonframe.pack(side="top", fill="x", expand=False)
    container.pack(side="top", fill="both", expand=True)
    cnf = create_cnf("cnf-input.txt")
    def drawTable():
        st = sentences.get().split(' ')
        CKY(st,cnf,container,0)
    def drawTree():
        st = sentences.get().split(' ')
        table = CKY(st,cnf,container,1)
        ui.drawTable(table,st,0)
        ui.drawTree(table,st)
    textBox = tk.Entry(buttonframe, bd = 2, textvariable = sentences)
    textBox.pack(side='left')
    startCkyBtn = tk.Button(buttonframe, text = "Run", command = drawTable)
    startCkyBtn.pack(side='left', padx=5)
    drawTreeBtn = tk.Button(buttonframe, text = "Draw CFG Tree", command = drawTree)
    drawTreeBtn.pack(side ='left', padx=5)
    return sentences
if __name__ == "__main__":
    root = tk.Tk()
    root.title('CKY algorithm')
    strIntpur = MainView(root)
    cnf = create_cnf("cnf-input.txt")
    #root.wm_geometry("1200x600")
    root.mainloop()