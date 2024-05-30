

file_name = 'stuent_information.txt'
import os

def main():
    while True:
        menu()
        choose=int(input('请选择：'))
        if choose in [0,1,2,3,4,5,6,7]:
            if choose ==0:
                quit_answer = input('确认退出吗？y/n')
                if quit_answer == 'y' or quit_answer == 'Y':
                    print('谢谢您的使用')
                    break
                else:
                    continue
            if choose == 1:
                insert()
            if choose == 2:
                find()
            if choose == 3:
                delete()
            if choose == 4:
                modify()
            if choose == 5:
                sort()
            if choose == 6:
                totle()
            if choose == 7:
                show_all()
        else:
            print('输入有误，请重新输入')
def menu():
    print('===============学生管理系统==================')
    print('-----------------功能菜单-------------------')
    print('\t\t\t1.录入学生信息')
    print('\t\t\t2.查找学生信息')
    print('\t\t\t3.删除学生信息')
    print('\t\t\t4.修改学生信息')
    print('\t\t\t5.排序')
    print('\t\t\t6.统计学生总数')
    print('\t\t\t7.显示所有学生信息')
    print('\t\t\t0.退出系统')
    print('---------------------------------------------')
def insert():
    stu_list = []
    while True:
        isValidID = False
        while (not isValidID):
            id=input('请输入学生id（如1001）：')
            if os.path.exists(file_name):  # 这个是判断下现在是否有存储文件 file_name=wenjian.txt
                with open(file_name, 'r') as file:  # 这句是打开那个文件
                    student = file.readlines()  # 这句是将文件里的内容，存到student的变量里
                    isIDduplicated = False
                    for item in student:  # 遍历student元素
                        check_id = dict(eval(item))  # 将遍历的内容存在check——id里
                        if id == check_id['id']:  # 判断输入的id 是否已经存在
                            print('学生id重复,请重新输入')  # 如果已经存在，则打印，并且从新开始
                            isIDduplicated = True
                            break
                    if not isIDduplicated:
                        isValidID = True

                            # 如果不存在就继续填下一个字段了
        name=input('请输入学生姓名：')
        if not name:
            break
        try:
            Python=int(input('请输入python成绩'))
            English=int(input('请输入英语成绩'))
            Math=int(input('请输入数学成绩'))
        except:
            print('请输入正确成绩')
            continue
        stu_info={'id':id,'name':name,'Python成绩':Python,'英语成绩':English,'数学成绩':Math}
        stu_list.append(stu_info)
        answer=input('是否继续添加学生信息y/n')
        if answer=='y'or answer=='Y':
            continue
        else:
            break
    print('学生信息录入成功')
    save(stu_list)
def save(lis):
    try:
        stu_txt=open(file_name,'a')
    except:
        stu_txt=open(file_name,'w')
    for item in lis:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()
def find():
    while True:
        #输入查询信息
        find_input = int(input('按姓名查询请摁1\n按ID查询请摁2\n'))
        #按姓名查询
        if find_input == 1:
            find_name = input('请输入学生姓名\n')
            if file_name:
                with open(file_name, 'r') as file:
                    student = file.readlines()
            else:
                print('没有学生信息，请先录入')
                break
            # 遍历文件内容，并匹配
            isStudentin = False
            for item in student:
                stu_info = dict(eval(item))
                if find_name == stu_info['name']:
                    print(stu_info)
                    isStudentin = True
            if not isStudentin:
                print('未找到学生信息')
        #按id查询
        elif find_input == 2:
            find_ID = input('请输入学生ID\n')
            if file_name:
                with open(file_name, 'r') as file:
                    student = file.readlines()
            else:
                print('没有学生信息，请先录入')
                break
            # 遍历文件内容，并匹配
            isStudentin = False
            for item in student:
                stu_info = dict(eval(item))
                if find_ID == stu_info['id']:
                    print(stu_info)
                    isStudentin = True
            if not isStudentin:
                print('未找到学生信息')
        else:
            print('输入有误，请重新输入')
            continue
        answer = input('是否继续查找学生y/n')
        if answer == 'y':
           continue
        else:
            break
def show(lst):
    if len(lst)==0:
        print('暂无学生数据')
        return
    #title展示
    format_title = '{:^6},{:^6},{:^6},{:^6},{:^6}'
    print(format_title.format('学生id','学生姓名','Python成绩','数学成绩','英语成绩'))
    #内容详情展示
    format_info = '{:^6},{:^6},{:^6},{:^6},{:^6}'
    for item in lst:
        student_show =dict(eval(item))
        print(format_info.format(student_show.get('id'),
                                 student_show.get('name'),
                                 student_show.get('Python成绩'),
                                 student_show.get('英语成绩'),
                                 student_show.get('数学成绩')))
def delete():
    while True:
        stu_delid=input('请输入需要删除的学生ID：'+'\n')
        if stu_delid !='':   #代表已经输入信息了
            if os.path.exists(file_name):
                with open(file_name,'r') as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag= False    #标记是否删除
            if student_old:   #如果有内容则，继续往下执行
                with open(file_name,'w') as wfile:
                    stuinfo_new={}
                    for item in student_old:   #遍历上边的列表
                        stuinfo_new=dict(eval(item))  #并将列表信息覆盖到新的字典中
                        if stu_delid != stuinfo_new['id']:  #判断删除id和新字典中id是否相同
                            wfile.write(str(stuinfo_new)+'\n') #如果不相同，则写入
                        else:
                            flag=True       #表示已删除
                    if flag:
                        print(f'id为{stu_delid}的学生信息信息已删除')
                    else:
                        print(f'未找到id为{stu_delid}的学生信息')
            else:
                print('没有学生信息')
                break
            show()
            answer=input('是否继续删除信息：y/n'+'\n')
            if answer =='y':
                continue
            else:
                break
def modify():
    #1：判断文件是否存在
    show()
    if os.path.exists(file_name):  # 有文件
        with open(file_name, 'r') as file:
            stu_old = file.readlines()  # 存入变量中
    else:
        print('没有学生信息，请先录入')
        return
    #2:输入学生信息，再判断是否为空
    stu_id = input('请输入需要修改学生信息的ID：' + '\n')
    if stu_id != '':  # 正确输入了
    #3：打开并写入
        with open(file_name, 'w') as wfile:
            for item in stu_old:
                student_mod = dict(eval(item))
    #4，找学生
                if stu_id == student_mod['id']:
                    print('找到学生信息了,可以修改信息了')
    #开始循环
                    while True:
    #5.找到对应想修改的学生信息
                        try:
                            student_mod['name'] = input('请输入要修改的学生姓名')
                            student_mod['Python成绩'] = int(input('请输入要修改的学生PYthon成绩'))
                            student_mod['英语成绩'] = int(input('请输入要修改学生的英语成绩'))
                            student_mod['数学成绩'] = int(input('请输入要修改学生的数学升级'))
                            break
                        except:
                            print('输入有误，请重新输入')
                    wfile.write(str(student_mod) + '\n')
                    print('修改成功')
    #6.没修改的学生处理
                else:
                    wfile.write(str(student_mod)+'\n')
    #7.询问是否继续修改
            answer = input('是否继续修改学生信息y/n')
            #因为已经出循环了，所以继续的话就调用修改的函数，否则就继续向下执行了
            if answer == 'y':
                modify()
def totle():
    if os.path.exists(file_name):
        with open(file_name,'r') as rfile:
            student = rfile.readlines()
            if student:
                print(f'共有{len(student)}名学生')
            else:
                print('还没有学生信息')
    else:
        print('未找到学生文件')
def sort():
    pass
def show_all():
    if os.path.exists(file_name):
        with open(file_name,'r') as rfile:
            student = rfile.readlines()
            show(student)
    else:
        print('未找到学生文件')

if __name__ == '__main__':
    main()
