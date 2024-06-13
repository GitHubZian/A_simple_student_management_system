from GeneralDesign import SIMS
from Model_menu import Menu
import re
import pandas as pd
import os
from openpyxl import load_workbook
class Add(SIMS):
    """添加学生信息模块"""
    def __init__(self):
        self.cache_list = []
        self.menu_add = None
        self.file_txt = "学生数据文件.txt"
        self.file_xlsx = "学生数据文件.xlsx"
        # 学生学号正则表达式，只能是数字
        self.pattern_sid = re.compile(r'^[0-9]+$')
        # 学生姓名正则表达式，只能是中文或者英语
        self.pattern_sname = re.compile(r'^[a-zA-Z\u4e00-\u9fa5]+$')
        # 学生年龄正则表达式，只能是数字且在1-9之间且不超过30岁
        self.pattern_age = re.compile(r'^[1-9]$|^[1-2][0-9]$|^30$')
        # 学生性别正则表达式，只能是"男"或"女"
        self.pattern_sex = re.compile(r'^男|女$')
        # 学生出生日期正则表达式，示例格式为YYYY-MM-DD
        self.pattern_birthday = re.compile(r'^(199[0-9]|20[0-9]{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$')
        # 学生电话号码正则表达式，示例格式为11位数字
        self.pattern_tel = re.compile(r'^\d{11}$')
        # 学生邮箱正则表达式，简单示例格式，仅包含@和.
        self.pattern_email = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    # 获取学生信息
    def enter_information(self):
        while True:
            self.sid = input("请输入学生学号:")
            if not self.pattern_sid.match(self.sid):
                flag = True
                while flag:
                    print("请输入正确的学号格式!(数字or英文)")
                    self.sid = input("请输入学生学号:")
                    if self.pattern_sid.match(self.sid):
                        flag = False

            self.sname = input("请输入学生姓名:")
            if not self.pattern_sname.match(self.sname):
                flag = True
                while flag:
                    print("请输入正确的姓名格式!(中文or英文)")
                    self.sname = input("请输入学生姓名:")
                    if self.pattern_sname.match(self.sname):
                        flag = False

            self.age = input("请输入学生年龄:")
            if not self.pattern_age.match(self.age):
                flag = True
                while flag:
                    print("请输入正确的年龄范围!(数字且在1-9之间且不超过30岁)")
                    self.age = input("请输入学生姓名:")
                    if self.pattern_age.match(self.age):
                        flag = False

            self.sex = input("请输入学生性别:")
            if not self.pattern_sex.match(self.sex):
                flag = True
                while flag:
                    print("请输入正确的性别格式!(男or女)")
                    self.sex = input("请输入学生性别:")
                    if self.pattern_sex.match(self.sex):
                        flag = False

            self.birthday = input("请输入学生出生日期:")
            if not self.pattern_birthday.match(self.birthday):
                flag = True
                while flag:
                    print("请输入正确的出生日期格式！(YYYY-MM-DD)")
                    self.birthday = input("请输入学生出生日期:")
                    if self.pattern_birthday.match(self.birthday):
                        flag = False

            self.addr = input("请输入学生地址:")

            self.tel = input("请输入学生电话:")
            if not self.pattern_tel.match(self.tel):
                flag = True
                while flag:
                    print("请输入正确的电话号码格式(11位数字)")
                    self.tel = input("请输入学生电话:")
                    if self.pattern_tel.match(self.tel):
                        flag = False

            self.email = input("请输入学生邮箱:")
            if not self.pattern_email.match(self.email):
                flag = True
                while flag:
                    print("请输入正确的邮箱格式")
                    self.email = input("请输入学生邮箱:")
                    if self.pattern_email.match(self.email):
                        flag = False

            self.out_input = input("是否确认?[y/n]")
            if self.out_input != "y":
                continue
            else:
                break
        # 封装成学生信息字典
        self.student_data = {
            "学号": self.sid,
            "姓名": self.sname,
            "年龄": self.age,
            "性别":self.sex,
            "出生日期": self.birthday,
            "地址": self.addr,
            "电话": self.tel,
            "邮箱": self.email
        }
        self._cache_student_data()

    def add_operate(self):
        # 子级菜单
        while True:
            self.menu_add = Menu().menu_add()
            operate = input("请输入你的操作:")
            match operate:
                # 添加继续学生信息
                case '1':
                    self.enter_information()
                # 展示缓存列表中的学生数据
                case '2':
                    self._cache_list_show()
                # 删除缓存列表中的学生数据
                case '3':
                    self._del_cache_student_data()
                # 将缓存数据存入excel表中 如果失败则存入txt文件中
                case '4':
                    self.save_information()
                case _:
                    # 将缓存列表清空
                    self.cache_list = []
                    print("over！")
                    break

    # 缓存学生数据字典列表
    def _cache_student_data(self):
        self.cache_list.append(self.student_data)
        self.cache_list = sorted(self.cache_list, key=lambda x: x["学号"])
        return self.cache_list

    # 查看添加缓存列表数据
    def _cache_list_show(self):
        for cache_index, cache_item in enumerate(self.cache_list):
            print(f"{cache_index} | {str(cache_item).strip('{}').replace(',', ' ')}")
    # 删除学生缓存列表数据
    def _del_cache_student_data(self):
        while True:
            del_cache_index = input("请输入你要删除的缓存数据的整数下标:(从0开始)")
            if not del_cache_index.isdigit():
                print("请输入正确的整数下标!")
                continue
            if len(self.cache_list) == 0:
                print("暂未有数据在缓存列表中")
                break
            else:
                print(f"{str(self.cache_list[int(del_cache_index)]).strip('{}').replace(',',' ')}")
                del_cache_sure = input("你确定要删除这条数据吗?[y/n]")
                if del_cache_sure != 'y':
                    continue
                else:
                    self.cache_list.pop(int(del_cache_index))
                    print("删除成功!")
                    break

    def save_information(self):
        print("!!! 警告 !!!")
        print("俩种保存类型请只选择一种，以确保数据的同步")
        while True:
            save_operate = input("请选择你的保存的方式:[excel or txt]")
            if save_operate == 'excel':
                pass
                try:
                    self._write_to_excel()
                    break
                except:
                    print("无法写入excel文件")
                    break
            if save_operate == 'txt':
                try:
                    self._write_to_txt()
                    break
                except:
                    print("无法写入txt文件")
                    break

    def _write_to_excel(self):
        if self.file_xlsx not in os.listdir("./学生数据文件/"):
            print("没有找到初始文件，开始初始化......")
            df = pd.DataFrame(self.cache_list)
            df.to_excel(f"./学生数据文件/{self.file_xlsx}", index=False)
        else:
            # 追加写入功能继续完善
            print("正在写入文件数据中......")
            wb = load_workbook("./学生数据文件/学生数据文件.xlsx")
            ws = wb.active
            data_to_append_excel = []
            for item in self.cache_list:
                values = list(item.values())
                data_to_append_excel.append(values)
            for item_data in data_to_append_excel:
                ws.append(item_data)
            wb.save("./学生数据文件/学生数据文件.xlsx")

    # 写入txt文件
    def _write_to_txt(self):
        if self.file_txt not in os.listdir("./学生数据文件/"):
            print("没有找到初始文件，开始初始化......")
            with open(f"./学生数据文件/{self.file_txt}",'w',encoding="utf-8") as f:
                for cache_index, cache_item in enumerate(self.cache_list):
                    f.write(f"{cache_index}  {str(cache_item).strip('{}').replace(',', ' ')}")
                    f.write('\n')
        else:
            print("正在写入文件数据中......")
            with open(f"./学生数据文件/{self.file_txt}",'r',encoding="utf-8") as f:
                cache_index = 0
                for _ in f.readlines():
                     cache_index += 1
            with open(f"./学生数据文件/{self.file_txt}",'a',encoding="utf-8") as f:
                for cache_item in self.cache_list:
                    f.write(f"{cache_index}  {str(cache_item).strip('{}').replace(',', ' ')}")
                    f.write('\n')
                    cache_index += 1

