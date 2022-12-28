#coding:utf-8
from PyPDF4 import PdfFileReader
from PyPDF4 import PdfFileWriter
import os
#变量声明
start=0
end=30
#参数获取
print('输入或者拖入源PDF文件地址:',end="")
pdffile=str(input())
print(pdffile)
print("输入截取区间 start-end (1-30):",end="")
start,end=map(int,input().split('-'))
#工作详情输出
os.system("cls")
print("正在准备文件......")
pdfmark = PdfFileReader("mark.pdf")
pdf = PdfFileReader(pdffile)
pdfout=PdfFileWriter()
print(">>>开始输出:",end="")
for i in range(start-1,end):
    p=pdf.getPage(i)
    p.mergePage(pdfmark.getPage(0))
    pdfout.addPage(p)
    print("@",end="")
try:
    os.mkdir('OUT')
except:
    print("\nOUT目录已存在")
f=open("OUT\\PDFOUT.pdf","wb")
pdfout.write(f)
f.close()
print()
print(">>>操作完成，文件状态:OK!")
print('按任意键打开文件目录')
input()
os.system('start OUT')
