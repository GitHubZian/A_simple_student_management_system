from Model_menu import Menu
from Model_add_sInformations import Add
from Model_load_read import read_max_10_step
from Model_find_data import Find_or_Drop
# 实列化菜单Menu对象
menu = Menu()
# 实列化添加数据类Add对象
add = Add()
# 设置无限循环供用户使用

while True:
    find_or_drop = Find_or_Drop()
    menu.menu()
    operates = input("请输入您的操作:")
    match operates:
        # 添加学生信息
        case '1':
            stuDictDate = add.enter_information()
            add.add_operate()
        # 显示排序后的学生信息
        case '2':
            read_max_10_step()
        # 查询学生信息
        case '3':
            find_or_drop.search_information()
        # 删除学生信息
        case '4':
            find_or_drop.drop_information()
        case _:
            print("退出系统成功！")
            break