# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：

score_last = 72
score_present = 85
score_increase = (85-72)/85
print("小明成绩相比去年提升了 %.1f %%" % score_increase)
print('\n')

# string 练习

a = "handsome"
b = "ian"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if "h" in a:
    print("h 在变量 a 中")
else:
    print("h 不在变量 a 中")

if "a" not in a:
    print("a 不在变量 b 中")
else:
    print("a 在变量 b 中")

print(r'\n')
print(R'\n')