"""找到我想要的数据"""
from GeneralDesign import SIMS
from Model_menu import Menu
from Model_load_read import loading
class Find_or_Drop(SIMS):

    def __init__(self):
        self.file_name_txt = "学生数据文件.txt"
        self.find_name = None
        self.find_id = None
        self.loading_data_list = loading()

    def get_find_id(self,sid):
        self.find_id = sid
        return self.find_id

    def get_find_name(self,name):
        self.find_name = name
        return self.find_name

    def search_information(self):
        while True:
            _ = Menu().menu_search()
            find_op = input("请选择你的操作:")
            if find_op == '1':
                sid = input("请输入你要查询的学号:")
                self.find_id = self.get_find_id(sid)
                self.find_by_id()  # 调用find_by_id方法
            elif find_op == '2':
                sname = input("请输入你要查询的学生姓名:")
                self.find_name = self.get_find_name(sname)
                self.find_by_name()
            else:
                print("over")
                break

    # 用与处理excel文件
    def tuple_to_dict(self):
        keys = self.loading_data_list[0]
        result = [dict(zip(keys, values)) for values in self.loading_data_list[1:]]
        return result
    # 用与处理txt文件
    def list_to_dict(self,data):
        # 找到"学号"的位置
        start_index = data.find("学号")
        # 从"学号"开始切割数据
        data = data[start_index:]
        # 将数据转换成字典形式
        items = data.split(",,'")
        info_dict = {}
        for item in items:
            key_value = item.split(":,'")
            if len(key_value) == 2:
                key = key_value[0].strip("'")
                value = key_value[1].strip("'")
                info_dict[key] = value
        return info_dict

    def find_by_name(self):
        found = False  # 添加一个标记来表示是否找到
        for _ in self.loading_data_list:
            dict_data = self.list_to_dict(_)
            if self.find_name == dict_data["姓名"]:
                print("成功查询")
                found = True
                print(_)
                break  # 找到后退出循环
        if not found:
            print("查询失败")

    def find_by_id(self):
        found = False
        for _ in self.loading_data_list:
            dict_data = self.list_to_dict(_)
            if self.find_id == dict_data["学号"]:
                print("成功查询")
                found = True
                print(_)
                break
        if not found:
            print("查询失败")

    def drop_information(self):
        flag = False
        while not flag:
            _ = Menu().menu_del()
            self.del_id = input("请输入你要删除的学号:")
            found = False
            for _ in self.loading_data_list:
                dict_data = self.list_to_dict(_)
                if self.del_id == dict_data["学号"]:
                    print("成功锁定")
                    found = True
                    print(_)
                    del_sure = input("你确实要删除吗?[y/n]")
                    if del_sure != 'y':
                        flag = True
                    else:
                        self.drop_open_txt()
                        flag = True
            if not found:
                print("删除失败")
    def drop_open_txt(self):
        with open(f'./学生数据文件/{self.file_name_txt}','r',encoding='utf-8') as f:
            lines = f.readlines()
        with open(f'./学生数据文件/{self.file_name_txt}','w',encoding='utf-8') as f:
            for line in lines:
                # 转字典形式
                if self.del_id in line:
                    pass
                else:
                    f.write(line)

if __name__ == '__main__':
    find_or_Drop = Find_or_Drop()
    result = find_or_Drop.tuple_to_dict()
    print(result)
