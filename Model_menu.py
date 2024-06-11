from GeneralDesign import SIMS
"""全局菜单配置"""
class Menu(SIMS):
    # 主菜单
    def menu(self):
        self.hello = '欢迎来到学生管理系统!'
        self.operate1 = "录入学生信息\t"
        self.operate2 = "显示学生信息\t"
        self.operate3 = "查询学生信息\t"
        self.operate4 = "删除学生信息\t"
        self.operate5 = "退出管理系统\t"
        print("-"*73)
        print(f"{self.hello: ^62}  ")
        print(f"{self.operate1 + ' ' + '[请输入:1]': ^62}")
        print(f"{self.operate2 + ' ' + '[请输入:2]': ^62}")
        print(f"{self.operate3 + ' ' + '[请输入:3]': ^62}")
        print(f"{self.operate4 + ' ' + '[请输入:4]': ^62}")
        print(f"{self.operate5 + '[请输入:exit]': ^64}")
        print("-" * 73)

    #  二级添加学生数据菜单
    def menu_add(self):
        self.add_again = "继续添加数据\t\t"
        self.show_alreadly_add = "展示已添加的数据\t\t"
        self.del_add = "删除添加的数据\t\t"
        self.write_to_save = "开始保存数据文件\t\t"
        self.over_add = "  完成操作\t\t\t"
        print('-'*73)
        print(f"{self.add_again + ' ' + '[请输入:1]': ^60}")
        print(f"{self.show_alreadly_add + ' ' + '[请输入:2]': ^60}")
        print(f"{self.del_add + ' ' + '[请输入:3]': ^60}")
        print(f"{self.write_to_save + ' ' + '[请输入:4]' + ' ': ^60}")
        print(f"{' '+self.over_add + '[请输入:exit]': ^60}")
        print('-'*73)

    # 二级搜索菜单
    def menu_search(self):
        self.search_by_sid = "通过学生学号查找\t"
        self.search_by_sname = "通过学生姓名查找\t"
        self.search_over = "    结束查找\t"
        print('-'*73)
        print(f"{' ' * 3 + self.search_by_sid + ' ' * 4 + '[请输入:1]': ^62}")
        print(f"{' ' * 3 + self.search_by_sname + ' ' * 4 + '[请输入:2]': ^62}")
        print(f"{' '*3 + self.search_over + ' ' *4 + '[请输入:3]': ^62}")
        print('-'*73)

    # 二级删除菜单
    def menu_del(self):
        self.del_data_sid = "需要删除的学生数据学号\t"
        self.del_over = "结束删除\t\t"
        print('-' * 73)
        print(f"{self.del_data_sid + ' ' * 4 + '[请输入:1]': ^62}")
        print(f"{' '*8 + self.del_over + ' '*4 + '[请输入:2]': ^62}")
        print('-' * 73)
