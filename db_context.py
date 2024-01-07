import pyodbc


# Thay đổi thông tin kết nối tương ứng với cơ sở dữ liệu của bạn
server = 'localhost'
database = 'ChatBot'
username = 'sa'
password = '10052002'

# Tạo chuỗi kết nối
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(conn_str)


class ConvertData:

    # Truy vấn và xử lý dữ liệu
    def __init__(self):
        self.resulttrangphuc = []
        self.resultthuoctinh = []
        self.resultfc = []
        self.resultbc = []
        self.resulttt = []

    def converttrangphuc(self):
        # Kết nối đến cơ sở dữ liệu
        #conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()


        # Ví dụ: Thực hiện truy vấn SQL
        cursor.execute('SELECT * FROM trangphuc')  
        # Lấy kết quả của truy vấn
        rows = cursor.fetchall()
        dirtrangphuc = {}
        for row in rows:
            dirtrangphuc['idtrangphuc'] = row[0]
            dirtrangphuc['tenTrangPhuc'] = row[1]
            dirtrangphuc['desTrangPhuc'] = row[2]
            dirtrangphuc['noteTrangPhuc'] = row[3]
            self.resulttrangphuc.append(dirtrangphuc)
            dirtrangphuc = {}
            #print(row)

        # Đóng kết nối
        #cursor.close()
        #conn.close()

    def convertthuoctinh(self):
        # Kết nối đến cơ sở dữ liệu
        #conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()


        # Ví dụ: Thực hiện truy vấn SQL
        cursor.execute('SELECT * FROM thuoctinh')  
        # Lấy kết quả của truy vấn
        rows = cursor.fetchall()
        dirthuoctinh = {}
        for row in rows:
            dirthuoctinh['idthuoctinh'] = row[0]
            dirthuoctinh['tenThuocTinh'] = row[1]
            dirthuoctinh['desThuocTinh'] = row[2]
            self.resultthuoctinh.append(dirthuoctinh)
            dirthuoctinh = {}
            #print(row)

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

data_converter = ConvertData()
data_converter.convertthuoctinh()
data_converter.converttrangphuc()
data_converter.getfc()
data_converter.getbc()
#data_converter.getthuoctinh()

#for i in data_converter.resultthuoctinh:
#    print(i['idthuoctinh'])

#for i in range(6):
#   print(data_converter.resultthuoctinh[i])

print(data_converter.get_trangphuc_by_id("P02"))
print(data_converter.get_thuoctinh_by_id("S07"))