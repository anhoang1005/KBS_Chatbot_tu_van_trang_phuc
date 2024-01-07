import os
import sys

from backward_chaining import BackwardChaining
from forward_chaining import ForwardChaining
from class_all import *
from class_all import ConvertData
from colorama import Fore, Style
from email.message import EmailMessage
import ssl,smtplib
 
person = Person(None, None, None)
validate = Validate()
list_symptom_of_person = []

db = ConvertData()
db.convertthuoctinh()
db.converttrangphuc()
db.getfc()
db.getbc()
luat_tien = db.groupfc()
luat_lui = db.groupbc()

#################################################
# 1. câu hỏi chào hỏi
def welcome_question():
    print("-->Chatbot: Xin chào, tôi là chatbot tư vấn trang phục!")
    print("-->Chatbot: Để nhận lời khuyên và tư vấn chi tiết, hãy để lại email, tên và số điện thoại của bạn")

    print("-->Chatbot: Hãy nhập tên của bạn!")
    person.name = validate.validate_name(input())
    print(f'{Fore.GREEN}-->Người dùng: Tên của tôi là {person.name}{Style.RESET_ALL}')

    print("-->Chatbot: Hãy nhập email của bạn!")
    person.email = validate.validate_email(input())
    print(f'{Fore.GREEN}-->Người dùng: Email của tôi là {person.email}{Style.RESET_ALL}')

    print("-->Chatbot: Hãy nhập số điện thoại của bạn!")
    person.phoneNumber = validate.validate_phonenumber(input())
    print(f'{Fore.GREEN}-->Người dùng: số điện thoại của tôi là {person.phoneNumber}{Style.RESET_ALL}')

    print(person)
    return person

#################################################################
# 2. Câu hỏi về giới tính:
def gioitinh_question(list_symptom_of_person, person):
    AllSymLst = [db.resultthuoctinh[i] for i in range(6, 8)]

    NewAllSymLst = []
    for i in AllSymLst:
        NewAllSymLst.append(i["idthuoctinh"])

    while (1):
        print(f'-->Chatbot: {person.name}, giới tính của bạn là gì?(Nhập số thứ tự để chọn!)')

        count = 1
        for i in AllSymLst:
            if (i not in list_symptom_of_person):
                print(f'{count}. {i["tenThuocTinh"]} \n')
            count += 1

        #print("0. Tôi không có giới tính nào ở trên\n -------------Câu trả lời của bạn?--------------")
        print("-------------Câu trả lời của bạn?--------------")
        answer = validate.validate_input_number_form(input())
        print(f'{Fore.GREEN}-->{person.name}: Câu trả lời của tôi là {answer}{Style.RESET_ALL}')

        if (answer == '0'):
            break
        elif (int(answer) < 0 or int(answer) > 2):
            print('-->Chatbot: Vui lòng nhập 1 số từ 0 tới 2')
            continue
        else:
            list_symptom_of_person.append(AllSymLst[int(answer)-1])
            print(f'-->Chatbot: Danh sách mã các thuộc tính {person.name} đang có:')
            print([i['idthuoctinh'] for i in list_symptom_of_person])
            break
    return list_symptom_of_person

#################################################################
# 3. Câu hỏi về tính cách:
def tinhcach_question(list_symptom_of_person, person):
    AllSymLst = [db.resultthuoctinh[i] for i in range(6)]

    NewAllSymLst = []
    for i in AllSymLst:
        NewAllSymLst.append(i["idthuoctinh"])

    while (1):
        print(f'-->Chatbot: {person.name}, bạn là kiểu người có tính cách như thế nào?(Nhập số thứ tự để chọn!)')

        count = 1
        for i in AllSymLst:
            if (i not in list_symptom_of_person):
                print(f'{count}. {i["tenThuocTinh"]} \n')
            count += 1

        #print("0. Tôi không có tính cách nào ở trên\n -------------Câu trả lời của bạn?--------------")
        print("-------------Câu trả lời của bạn?--------------")
        answer = validate.validate_input_number_form(input())
        print(f'{Fore.GREEN}-->{person.name}: Câu trả lời của tôi là {answer}{Style.RESET_ALL}')

        if (answer == '0'):
            break
        elif (int(answer) < 0 or int(answer) > 6):
            print('-->Chatbot: Vui lòng nhập 1 số từ 1 tới 6')
            continue
        else:
            list_symptom_of_person.append(AllSymLst[int(answer)-1])
            print(f'-->Chatbot: Danh sách mã các thuộc tính {person.name} đang có:')
            print([i['idthuoctinh'] for i in list_symptom_of_person])
            break
    return list_symptom_of_person

#################################################################
# 4. Câu hỏi về vóc dáng:
def vocdang_question(list_symptom_of_person, person):
    AllSymLst = [db.resultthuoctinh[i] for i in range(19, 24)]

    NewAllSymLst = []
    for i in AllSymLst:
        NewAllSymLst.append(i["idthuoctinh"])

    while (1):
        print(f'-->Chatbot: {person.name}, bạn là nguời có vóc dáng như thế nào?(Nhập số thứ tự để chọn!)')

        count = 1
        for i in AllSymLst:
            if (i not in list_symptom_of_person):
                print(f'{count}. {i["tenThuocTinh"]} \n')
            count += 1

        #print("0. Tôi không có tính cách nào ở trên\n -------------Câu trả lời của bạn?--------------")
        print("-------------Câu trả lời của bạn?--------------")
        answer = validate.validate_input_number_form(input())
        print(f'{Fore.GREEN}-->{person.name}: Câu trả lời của tôi là {answer}{Style.RESET_ALL}')

        if (answer == '0'):
            break
        elif (int(answer) < 0 or int(answer) > 5):
            print('-->Chatbot: Vui lòng nhập 1 số từ 1 tới 5')
            continue
        else:
            list_symptom_of_person.append(AllSymLst[int(answer)-1])
            print(f'-->Chatbot: Danh sách mã các thuộc tính {person.name} đang có:')
            print([i['idthuoctinh'] for i in list_symptom_of_person])
            break
    return list_symptom_of_person

#################################################################
# 5. Câu hỏi về su kien:
def sukien_question(list_symptom_of_person, person):
    AllSymLst = [db.resultthuoctinh[i] for i in range(12, 19)]

    NewAllSymLst = []
    for i in AllSymLst:
        NewAllSymLst.append(i["idthuoctinh"])

    while (1):
        print(f'-->Chatbot: {person.name}, bạn có dự định mặc trang phục để tham dự sự kiện nào không?(Nhập số thứ tự để chọn!)')

        count = 1
        for i in AllSymLst:
            if (i not in list_symptom_of_person):
                print(f'{count}. {i["tenThuocTinh"]} \n')
            count += 1

        #print("0. Tôi không dự sự kiện nào cả!\n -------------Câu trả lời của bạn?--------------")
        print("-------------Câu trả lời của bạn?--------------")
        answer = validate.validate_input_number_form(input())
        print(f'{Fore.GREEN}-->{person.name}: Câu trả lời của tôi là {answer}{Style.RESET_ALL}')

        if (answer == '0'):
            break
        elif (int(answer) < 0 or int(answer) > 7):
            print('-->Chatbot: Vui lòng nhập 1 số từ 1 tới 7')
            continue
        else:
            list_symptom_of_person.append(AllSymLst[int(answer)-1])
            print(f'-->Chatbot: Danh sách mã các thuộc tính {person.name} đang có:')
            print([i['idthuoctinh'] for i in list_symptom_of_person])
            break
    return list_symptom_of_person

#################################################################
# 6. Câu hỏi về do tuoi:
def dotuoi_question(list_symptom_of_person, person):
    AllSymLst = [db.resultthuoctinh[i] for i in range(9, 12)]

    NewAllSymLst = []
    for i in AllSymLst:
        NewAllSymLst.append(i["idthuoctinh"])

    while (1):
        print(f'-->Chatbot: {person.name}, bạn hãy cho tôi biết độ tuổi của bạn?(Nhập số thứ tự để chọn!)')

        count = 1
        for i in AllSymLst:
            if (i not in list_symptom_of_person):
                print(f'{count}. {i["tenThuocTinh"]} \n')
            count += 1

        #print("0. Tôi không muốn tiết lộ!\n -------------Câu trả lời của bạn?--------------")
        print("-------------Câu trả lời của bạn?--------------")
        answer = validate.validate_input_number_form(input())
        print(f'{Fore.GREEN}-->{person.name}: Câu trả lời của tôi là {answer}{Style.RESET_ALL}')

        if (answer == '0'):
            break
        elif (int(answer) < 0 or int(answer) > 3):
            print('-->Chatbot: Vui lòng nhập 1 số từ 1 tới 3')
            continue
        else:
            list_symptom_of_person.append(AllSymLst[int(answer)-1])
            print(f'-->Chatbot: Danh sách mã các thuộc tính {person.name} đang có:')
            print([i['idthuoctinh'] for i in list_symptom_of_person])
            break
    return list_symptom_of_person

#################################################################
# 7. Câu hỏi về khuon mat:
def khuonmat_question(list_symptom_of_person, person):
    AllSymLst = [db.resultthuoctinh[i] for i in range(24, 30)]

    NewAllSymLst = []
    for i in AllSymLst:
        NewAllSymLst.append(i["idthuoctinh"])

    while (1):
        print(f'-->Chatbot: {person.name}, bạn hãy cho tôi biết hình dáng khuôn mặt của bạn?(Nhập số thứ tự để chọn!)')

        count = 1
        for i in AllSymLst:
            if (i not in list_symptom_of_person):
                print(f'{count}. {i["tenThuocTinh"]} \n')
            count += 1

        #print("0. Tôi không muốn tiết lộ!\n -------------Câu trả lời của bạn?--------------")
        print("-------------Câu trả lời của bạn?--------------")
        answer = validate.validate_input_number_form(input())
        print(f'{Fore.GREEN}-->{person.name}: Câu trả lời của tôi là {answer}{Style.RESET_ALL}')

        if (answer == '0'):
            break
        elif (int(answer) < 0 or int(answer) > 6):
            print('-->Chatbot: Vui lòng nhập 1 số từ 1 tới 6')
            continue
        else:
            list_symptom_of_person.append(AllSymLst[int(answer)-1])
            print(f'-->Chatbot: Danh sách mã các thuộc tính {person.name} đang có:')
            print([i['idthuoctinh'] for i in list_symptom_of_person])
            break
    return list_symptom_of_person

#################################################################
# 8. Câu hỏi về khiem khuyet:
def khiemkhuyet_question(list_symptom_of_person, person):
    AllSymLst = [db.resultthuoctinh[8]]

    NewAllSymLst = []
    for i in AllSymLst:
        NewAllSymLst.append(i["idthuoctinh"])

    while (1):
        print(f'-->Chatbot: {person.name}, bạn hãy cho tôi biết khuôn mặt của bạn có khiếm khuyết dưới không (?(Nhập số thứ tự để chọn!)')

        count = 1
        for i in AllSymLst:
            if (i not in list_symptom_of_person):
                print(f'{count}. {i["tenThuocTinh"]} \n')
            count += 1

        print("0. Tôi không có khiếm khuyết trên!\n -------------Câu trả lời của bạn?--------------")
        #print("-------------Câu trả lời của bạn?--------------")
        answer = validate.validate_input_number_form(input())
        print(f'{Fore.GREEN}-->{person.name}: Câu trả lời của tôi là {answer}{Style.RESET_ALL}')

        if (answer == '0'):
            break
        elif (int(answer) < 0 or int(answer) > 1):
            print('-->Chatbot: Vui lòng nhập 1 số từ 0 tới 1')

            continue
        else:
            list_symptom_of_person.append(AllSymLst[int(answer)-1])
            print(f'-->Chatbot: Danh sách mã các thuộc tính {person.name} đang có:')
            print([i['idthuoctinh'] for i in list_symptom_of_person])
            break
    return list_symptom_of_person

################################################################
# 9 phần suy diễn tiến
def forward_chaining(rule, fact, goal, file_name, ten_tp,person):
    fc = ForwardChaining(rule, fact, None, file_name)

    list_predicted_disease = [i for i in fc.facts if i[0] == ten_tp]
    print(
        f'-->Chatbot: Chúng tôi dự đoán {person.name} có thể hợp với :', end=" ")
    for i in list_predicted_disease:
        temp = db.get_trangphuc_by_id(i)
        print(temp['idtrangphuc'], end=', ')
    print()
    
    print(
        f'-->Chatbot: Trên đây là dự đoán sơ bộ trang phục hợp với bạn của chúng tôi. Tiếp theo, chúng tôi có thể sẽ hỏi {person.name} xác nhận để đưa ra kết quả chính xác.', end=" ")
    return list_predicted_disease

########################################################################
# 10 phần suy diễn lùi
def backward_chaining(luat_lui,list_symptom_of_person,list_predicted_disease,file_name ):
    predictD=list_predicted_disease
    rule=luat_lui
    all_rule=db.getthuoctinh()
    fact_real=list_symptom_of_person_id
    benh=0
    for g in predictD:
        goal=g
        D=db.get_trangphuc_by_id(goal) #Chứa thông tin của bệnh có id == goal
        print(f"Chúng tôi đã có các đặc điểm của bạn và có thể bạn sẽ hợp với {D['tenTrangPhuc']}({goal}) , sau đây chúng tôi sẽ xác nhận tư vấn trên!")
        all_s_in_D=all_rule[goal]
        all_s_in_D=sorted(set(all_s_in_D)-set(fact_real))
        d=searchindexrule(rule,goal)
        
        b=BackwardChaining(rule,fact_real,goal,file_name) # kết luận trong trường hợp các luât jtruwowsc đã suy ra đk luôn
        
        if b.result1==True:# đoạn đầu
            print("* Bạn sẽ hợp với {}- {} và chúng tôi sẽ gửi thêm thông tin về bộ trang phục này cho bạn.".format(goal,D['tenTrangPhuc']))
            #print(f"{Fore.GREEN}* Mô tả về bộ trang phục:{Style.RESET_ALL}")
            #D['desTrangPhuc']=D['desTrangPhuc'].replace("/n","\n")
            #print(f"{D['desTrangPhuc']}")
            #print(f"{Fore.GREEN}* Lời khuyên:{Style.RESET_ALL}")
            #D['noteTrangPhuc']=D['noteTrangPhuc'].replace("/n","\n")
            #print(f"{D['noteTrangPhuc']}")
            #print("Cám ơn bạn đã sử dụng chat bot của chúng tôi! <3")
            return goal,fact_real
        
        while(len(all_s_in_D)>0):
            s=db.get_thuoctinh_by_id(all_s_in_D[0])
            question=f"Bạn có thuộc tính {s['tenThuocTinh']}({all_s_in_D[0]}) không?"
            print(question)
            answer = validate.validate_binary_answer(input())
            
            print(f"answer: {answer}")
            if answer== True :
                fact_real.append(all_s_in_D[0])
                b=BackwardChaining(rule,fact_real,goal,file_name)
                list_no_result,lsD=get_s_in_d(all_s_in_D[0],goal,rule,d,1)
                d=sorted(set(d)-set(lsD))
                all_s_in_D=sorted(set(list_no_result)-set(fact_real))
                if b.result1==True:
                    benh=1
                    break
            if answer==False :
                list_no_result,lsD=get_s_in_d(all_s_in_D[0],goal,rule,d,0) #S01 S02 S03 S04 S05
                d=sorted(set(d)-set(lsD))
                all_s_in_D=sorted(set(list_no_result)-set(fact_real))
            if len(d)==0: 
                print(f"Có vẻ như bạn không hợp {goal}-{D['tenTrangPhuc']}")
                break
        if benh==1:
            print("Bạn có vẻ hợp với {}- {} , và chúng tôi sẽ gửi thêm thông tin về bộ trang phục này cho bạn qua mail".format(goal,D['tenBenh']))
            print(f"Lời khuyên")
            D['noteTrangPhuc']=D['noteTrangPhuc'].replace("/n","\n")
            print(f"{D['noteTrangPhuc']}")
            print("Cám ơn bạn đã sử dụng chat bot của chúng tôi")
            
            return goal,fact_real
            break
    if benh==0:
        print(f"Bạn không hợp với trang phục nào cả")
        return None, fact_real

########################################################################
# 11 phần gửi email
def send_email(list_symptom_of_person_id,id_trangphuc, id_trangphuckt, id_trangphuctd ,person):
    email_sender = 'guzamo60@gmail.com'
    email_password = 'paltghsckxotraim'
    email_receiver = person.email
    print(email_receiver)

    benh=db.get_trangphuc_by_id(id_trangphuc)
    benhkt = db.get_trangphuc_by_id(id_trangphuckt)
    benhtd = db.get_trangphuc_by_id(id_trangphuctd)
    # print(benh)
    nguyen_nhan=benh['desTrangPhuc']
    loi_khuyen=benh['noteTrangPhuc']
    nguyen_nhan_kt=benhkt['desTrangPhuc']
    loi_khuyen_kt=benhkt['noteTrangPhuc']
    nguyen_nhan_td=benhtd['desTrangPhuc']
    loi_khuyen_td=benhtd['noteTrangPhuc']
    subject='Tư vấn trang phục'
    body=f"""
        Xin chào {person.name} <3,
        Chúng tôi là chatbot tư vấn trang phục do Nhóm 11 phát triển và cài đặt! Đây là một email tự động!
        Chúng tôi nhận được các đặc điểm của bạn là : 
        {[db.get_thuoctinh_by_id(i)["tenThuocTinh"] for i in list_symptom_of_person_id]}
        * Chúng tôi dự đoán bạn hợp với:
        - Bộ trang phục : {benh['tenTrangPhuc']}
        - Kiểu tóc : {benhkt['tenTrangPhuc']}
        - Trang điểm : {benhtd['tenTrangPhuc']}
        * Mô tả : 
         - {nguyen_nhan}
         - {nguyen_nhan_kt}
         - {nguyen_nhan_td}
        * Lời khuyên của chúng tôi dành cho bạn: 
         - {loi_khuyen}
         - {loi_khuyen_kt}
         - {loi_khuyen_td}
        * Cám ơn vì đã dùng Chatbot của chúng tôi! <3
    """
    # print(body)
    
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject
    em.set_content(body)
    context=ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp: 
            smtp.login(email_sender,email_password)
            smtp.sendmail(email_sender,email_receiver,em.as_string())
    except:
        print("email không tồn tại")

########################################################################
# 12 phần in ra kết quả
def print_ket_qua(list_symptom_of_person_id,id_trangphuc, id_trangphuckt, id_trangphuctd ,person):
    benh =db.get_trangphuc_by_id(id_trangphuc)
    benhkt = db.get_trangphuc_by_id(id_trangphuckt)
    benhtd = db.get_trangphuc_by_id(id_trangphuctd)

    print(f'-->Chatbot: Cảm ơn bạn đã cung cấp thông tin cho chúg tôi. Sau đây chatbot sẽ đưa ra kết quả tư vấn dành cho {person.name} \n', end=" ")
    print(f'{Fore.GREEN}* {person.name} sẽ hợp với:{Style.RESET_ALL} \n')
    print(f"- Bộ trang phục: {benh['tenTrangPhuc']}({id_trangphuc}) \n")
    print(f"- Kiểu tóc: {benhkt['tenTrangPhuc']}({id_trangphuckt}) \n")
    print(f"- Kiểu trang điểm: {benhtd['tenTrangPhuc']}({id_trangphuctd}) \n")

    print(f"{Fore.GREEN}* Mô tả:{Style.RESET_ALL}")
    benh['desTrangPhuc']=benh['desTrangPhuc'].replace("/n","\n")
    print(f"- {benh['desTrangPhuc']}")
    benhkt['desTrangPhuc']=benhkt['desTrangPhuc'].replace("/n","\n")
    print(f"- {benhkt['desTrangPhuc']}")
    benhtd['desTrangPhuc']=benhtd['desTrangPhuc'].replace("/n","\n")
    print(f"- {benhtd['desTrangPhuc']} \n")

    print(f"{Fore.GREEN}* Lời khuyên:{Style.RESET_ALL}")
    benh['noteTrangPhuc']=benh['noteTrangPhuc'].replace("/n","\n")
    print(f"- {benh['noteTrangPhuc']}")
    benhkt['noteTrangPhuc']=benhkt['noteTrangPhuc'].replace("/n","\n")
    print(f"- {benhkt['noteTrangPhuc']}")
    benhtd['noteTrangPhuc']=benhtd['noteTrangPhuc'].replace("/n","\n")
    print(f"- {benhtd['noteTrangPhuc']} \n")

    print("Tư vấn chi tiết của chúng tôi sẽ được tự động gửi vào email của bạn!")
    print(f"Cám ơn bạn đã sử dụng chat bot của chúng tôi! {Fore.RED}<3{Style.RESET_ALL}")


person = welcome_question()
list_symptom_of_person = []
list_symptom_of_person = gioitinh_question(list_symptom_of_person, person)
list_symptom_of_person = tinhcach_question(list_symptom_of_person, person)
list_symptom_of_person = vocdang_question(list_symptom_of_person, person)
list_symptom_of_person = sukien_question(list_symptom_of_person, person)
list_symptom_of_person = dotuoi_question(list_symptom_of_person, person)
list_symptom_of_person = khuonmat_question(list_symptom_of_person, person)
list_symptom_of_person = khiemkhuyet_question(list_symptom_of_person, person)

list_symptom_of_person_id = [i['idthuoctinh'] for i in list_symptom_of_person]
list_symptom_of_person_id = list(set(list_symptom_of_person_id))
list_symptom_of_person_id.sort()

list_predicted_disease = forward_chaining(luat_tien, list_symptom_of_person_id, None, 'ex', "P", person)
print(list_predicted_disease)

if len(list_predicted_disease)==0 :
    print("Bạn không phù hợp với trang phục nào của chúng tôi cả.Cám ơn bạn đã sử dụng ChatBot")
    sys.exit()

disease,list_symptom_of_person_id= backward_chaining(luat_lui,list_symptom_of_person_id,list_predicted_disease,"ex")

list_predicted_diseasekt = forward_chaining(luat_tien, list_symptom_of_person_id, None, 'ex', "N", person)
print(list_predicted_diseasekt)

if len(list_predicted_diseasekt)==0 :
    print("Bạn không phù hợp với trang phục nào của chúng tôi cả.Cám ơn bạn đã sử dụng ChatBot")
    sys.exit()

diseasekt,list_symptom_of_person_id_kt= backward_chaining(luat_lui,list_symptom_of_person_id,list_predicted_diseasekt,"ex")

list_predicted_diseasetd = forward_chaining(luat_tien, list_symptom_of_person_id, None, 'ex', "M", person)
print(list_predicted_diseasetd)

if len(list_predicted_diseasetd)==0 :
    print("Bạn không phù hợp với trang phục nào của chúng tôi cả.Cám ơn bạn đã sử dụng ChatBot")
    sys.exit()

diseasetd,list_symptom_of_person_id_td= backward_chaining(luat_lui,list_symptom_of_person_id,list_predicted_diseasetd,"ex")

print_ket_qua(list_symptom_of_person_id, disease, diseasekt, diseasetd, person)

send_email(list_symptom_of_person_id, disease, diseasekt, diseasetd, person)