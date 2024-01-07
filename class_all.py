import re
import pyodbc

# Thay đổi thông tin kết nối tương ứng với cơ sở dữ liệu của bạn
server = 'localhost'
database = 'ChatBotAll'
username = 'sa'
password = '10052002'

# Tạo chuỗi kết nối
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(conn_str)

class ConvertData:
    def __init__(self):
        self.resulttrangphuc = []
        self.resultthuoctinh = []
        self.resultfc = []
        self.resultbc = []
        self.resulttt = []
    
    def converttrangphuc(self):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM trangphuc')  
        rows = cursor.fetchall()
        dirtrangphuc = {}
        for row in rows:
            dirtrangphuc['idtrangphuc'] = row[0]
            dirtrangphuc['tenTrangPhuc'] = row[1]
            dirtrangphuc['desTrangPhuc'] = row[2]
            dirtrangphuc['noteTrangPhuc'] = row[3]
            self.resulttrangphuc.append(dirtrangphuc)
            dirtrangphuc = {}
    
    def convertthuoctinh(self):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM thuoctinh')  
        rows = cursor.fetchall()
        dirthuoctinh = {}
        for row in rows:
            dirthuoctinh['idthuoctinh'] = row[0]
            dirthuoctinh['tenThuocTinh'] = row[1]
            dirthuoctinh['desThuocTinh'] = row[2]
            self.resultthuoctinh.append(dirthuoctinh)
            dirthuoctinh = {}
        
    def getfc(self):
        # Lay cac luat suy dien tien
        dbfc = conn.cursor()
        dbfc.execute("SELECT idsuydien, luat.idluat, idthuoctinh, idtrangphuc, trangthai FROM suydien, luat WHERE suydien.idluat=luat.idluat and trangThai='1'")
        fc = dbfc.fetchall()
        s = []
        d = []
        for i in range(len(fc)):
            s.append(fc[i][2])
            d.append(fc[i][3])

        tt = s[0]
        trangphuc = []
        dicfc = {}
        for i in range(len(s)):
            if(s[i]==tt):
                trangphuc.append(d[i])
            else:
                dicfc['thuoctinh'] = tt
                dicfc['trangphuc'] = trangphuc
                tt = s[i]
                self.resultfc.append(dicfc)
                trangphuc = []
                trangphuc.append(d[i])
                dicfc = {}

    def getbc(self):
        #Lay cac tap suy dien lui
        dbbc = conn.cursor()
        dbbc.execute("select idsuydien, luat.idluat, idthuoctinh, idtrangphuc, trangthai from suydien, luat where suydien.idluat=luat.idluat and trangThai='0' order by idtrangphuc")
        fc = dbbc.fetchall()
        rule = []
        s = []
        d = []
        for i in range(len(fc)):
            rule.append(fc[i][1])
            s.append(fc[i][2])
            d.append(fc[i][3])
        
        vtrule = rule[0]
        tt = []
        trangphuc = None
        dicbc = {}
        for i in range(len(rule)):
            if rule[i] == vtrule:
                tt.append(s[i])
                trangphuc = d[i]
            else:
                dicbc['rule'] = vtrule
                dicbc['trangphuc'] = trangphuc
                dicbc['thuoctinh'] = tt
                vtrule = rule[i]
                self.resultbc.append(dicbc)
                trangphuc = d[i]
                tt = []
                tt.append(s[i])
                dicbc = {}
        
    def groupfc(self):
        res = []
        for i in self.resultfc:
            for j in range(len(i['trangphuc'])):
                res.append([i['trangphuc'][j], i['thuoctinh']])
        return res
    
    def groupbc(self):
        #Group
        p = []
        vt = self.resultbc[0]['trangphuc']
        temp = []
        for i in self.resultbc:
            t = []
            t.append(i['trangphuc'])
            for j in i['thuoctinh']:
                t.append(j)
            temp.append(t)
        return temp
    
    def getthuoctinh(self):
        dbthuoctinh=conn.cursor()
        dbthuoctinh.execute("SELECT * FROM suydien order by idtrangphuc")
        dttt=dbthuoctinh.fetchall()
        trangphuc=[]
        tt=[]
        rule=[]
        for i in dttt:
            trangphuc.append(i[3])
            tt.append(i[2])
            rule.append(i[1])
        vtbenh=trangphuc[0]
        lstt=[]
        dirtt={}
        
        for i in range(len(trangphuc)):
            if trangphuc[i]==vtbenh:
                lstt.append(tt[i])
            else:
                dirtt[vtbenh]=sorted(set(lstt))
                lstt=[]
                vtbenh=trangphuc[i]
                lstt.append(tt[i])
        dirtt[vtbenh]=sorted(set(lstt))
        self.resulttt=dirtt
        return self.resulttt

    def get_trangphuc_by_id(self, id_trangphuc):
        #Lay trang phuc dua theo id trang phuc
        for i in self.resulttrangphuc:
            if i["idtrangphuc"] == id_trangphuc:
                return i
        return 0
    
    def get_thuoctinh_by_id(self, id_thuoctinh):
        for i in self.resultthuoctinh:
            if i["idthuoctinh"] == id_thuoctinh:
                return i
        return 0

class Validate:
    def __init__(self) -> None:
        pass

    def validate_input_number_form(self,value):
        while (1):
            valueGetRidOfSpace = ''.join(value.split(' '))
            check = valueGetRidOfSpace.isnumeric()
            if (check):
                return valueGetRidOfSpace
            else:
                print("-->Chatbot: Vui lòng nhập 1 số dương!")
                value = input()

    def validate_phonenumber(self,value):
        while (1):
            valueGetRidOfSpace = ''.join(value.split(' '))
            check = valueGetRidOfSpace.isnumeric()
            if (check):
                return valueGetRidOfSpace
            else:
                print("-->Chatbot: Vui lòng nhập 1 số điện thoại đúng định dạng!")
                value = input()

    def validate_email(self, email):
        while (1):
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

            if (re.fullmatch(regex, email)):
                # print("Chatbot:Tôi đã nhận được thông tin Email của bạn")
                return email

            else:
                print("-->Chatbot: Vui lòng nhập lại email hợp lệ!")
                email = input()
    
    def validate_name(self, value):
        while (1):
            valueGetRidOfSpace = ''.join(value.split(' '))

            check = valueGetRidOfSpace.isalpha()
            if (check):
                # print("Tôi đã nhận được thông tin Tên của bạn")
                return value
            else:
                print("-->Chatbot: Vui lòng nhập lại tên hợp lệ! ")
                value = input()

    def validate_binary_answer(self, value):
        acceptance_answer_lst = ['1', 'y', 'yes', 'co', 'có']
        decline_answer_lst = ['0', 'n', 'no', 'khong', 'không']
        value = value+''
        while (1):
            if (value) in acceptance_answer_lst:
                return True
            elif value in decline_answer_lst:
                return False
            else:
                print(
                    "-->Chatbot: Câu trả lời không hợp lệ. Vui lòng nhập lại câu trả lời")
                value = input()


class Person:
    def __init__(self, name, phoneNumber, email):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.phoneNumber} - {self.email}"

class TreeForFC(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Symptom:
    def __init__(self, code, detail):
        self.code = code
        self.detail = detail

def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 10 * level + '-> ' + str(node.value))
        printTree(node.right, level + 1)

def searchindexrule(rule,goal):
    #Tìm vị trí các rule có trang phuc là goal
    index=[]
    for r in range(len(rule)):
        if rule[r][0]==goal:
            index.append(r)
    return index

def get_s_in_d(answer,goal,rule,d,flag):
    #Lấy các triệu chứng theo sự suy diễn để giảm thiểu câu hỏi
    #và  đánh dấu các luật đã được duyệt qua để bỏ qua những luật có cùng cùng câu hỏi vào
    result=[]
    index=[]
    if flag==1:
        for i in range(len(rule)):
            if (rule[i][0]==goal) and (answer in rule[i]) and (i in d):
                for j in rule[i]:
                    if j[0]=='S':
                        result.append(j)
                        # result=set()
    else:
        for i in range(len(rule)):
            if (rule[i][0]==goal) and (answer in rule[i]): index.append(i)
            if (rule[i][0]==goal) and (answer not in rule[i]) and (i in d):
                for j in rule[i]:
                    if j[0]=='S':
                        result.append(j)        

    return sorted(set(result)),index
