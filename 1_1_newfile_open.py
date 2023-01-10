import tkinter
import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title("영농일지")
root.geometry("620x650")





# 제목 그리드 프레임
title_frame = Frame(root, height=30)
e_title = StringVar()
e_title.set("금일 작업내용을 입력합니다.")
e_title = Entry(root, textvariable=e_title, state="readonly", justify="center", width=70)  # 사용자가 입력이 가능하여 수정해야 함
e_title.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)

# 작업일자 및 날씨 그리드 프레임
date_wether_frame = LabelFrame(root, text="작업일자 및 날씨", height= 50)

frame_image1 = Frame(date_wether_frame, width=30)                      # 공백 그리드 프레임
frame_image1.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)

values = [str(i) + "년" for i in range(2021, 2041)] # 1 ~ 12 까지의 숫자
year_combo = ttk.Combobox(date_wether_frame, width=8, values=values) # 임의의 입력이 가능한 오류가 발생한다.
year_combo.set("년도 선택")
year_combo.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)

values = [str(i) + "월" for i in range(1, 13)] 
month_combo = ttk.Combobox(date_wether_frame, width=10, values=values) # 임의의 입력이 가능한 오류가 발생한다.
month_combo.set("작업월 선택")
month_combo.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)

values = [str(i) + "일" for i in range(1, 32)] 
day_combo = ttk.Combobox(date_wether_frame, width=10, values=values) # 임의의 입력이 가능한 오류가 발생한다.
day_combo.set("작업일 선택")
day_combo.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

frame_image1 = Frame(date_wether_frame, width=60)                      # 공백 그리드 프레임
frame_image1.grid(row=0, column=4, sticky=N+E+W+S, padx=3, pady=3)

frame_image2 = Frame(date_wether_frame, width=60)                      # 공백 그리드 프레임
frame_image2.grid(row=0, column=5, sticky=N+E+W+S, padx=3, pady=3)

values = ("맑음", "약간 흐림", "흐림", "약한 비/눈", "비/눈")
wether_combo = ttk.Combobox(date_wether_frame, width=8, values=values)
wether_combo.set("날씨 선택")
wether_combo.grid(row=0, column=6, sticky=N+E+W+S, padx=3, pady=3)

values = [str(i) + "도" for i in range(1, 46)] 
degree_combo = ttk.Combobox(date_wether_frame, width=7, values=values) # 임의의 입력이 가능한 오류가 발생한다.
degree_combo.set("온도 선택")
degree_combo.grid(row=0, column=7, sticky=N+E+W+S, padx=3, pady=3)


# 작업현황 그리드 프레임
work_status_frame = LabelFrame(root, text="작업현황", height=100)
# 작목 선택 콤보 박스: 리스트 박스에서 목록을 가져와 콤보박스로 이동
# values = i in (box_registlist.get(0, END))                                             
plant_name1 = StringVar()                   
plant_name1.set("작목 선택")
plant_name1 = Entry(work_status_frame, textvariable=plant_name1, state="readonly", justify="center", width=10)
plant_name1.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
plant_name_combo2 = ttk.Combobox(work_status_frame, width=10)
plant_name_combo2.set("")
plant_name_combo2.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
plant_name_combo3 = ttk.Combobox(work_status_frame, width=10)
plant_name_combo3.set("")
plant_name_combo3.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
plant_name_combo3 = ttk.Combobox(work_status_frame, width=10)
plant_name_combo3.set("")
plant_name_combo3.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)

values = [str(i) + "명" for i in range(1, 31)]            # 인원수 선택 콤보 박스
workers1 = StringVar()
workers1.set("인원 선택")
workers1 = Entry(work_status_frame, textvariable=workers1, state="readonly", justify="center", width=7)
workers1.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
workers_combo2 = ttk.Combobox(work_status_frame, width=7, values=values)
workers_combo2.set("")
workers_combo2.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
workers_combo3 = ttk.Combobox(work_status_frame, width=7, values=values)
workers_combo3.set("")
workers_combo3.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
workers_combo3 = ttk.Combobox(work_status_frame, width=7, values=values)
workers_combo3.set("")
workers_combo3.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)

e_material1 = StringVar()                                  # 당일 사용한 농자재를 입력함
e_material1.set("금일 소요 농자재를 입력합니다.")
e_material1 = Entry(work_status_frame, textvariable=e_material1, state="readonly", justify="center", width=25)    
e_material1.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
e_material2 = Entry(work_status_frame, width=25) 
e_material2.insert(0, "")
e_material2.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
e_material3 = Entry(work_status_frame, width=25) 
e_material3.insert(0, "")
e_material3.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
e_material3 = Entry(work_status_frame, width=25) 
e_material3.insert(0, "")
e_material3.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)

e_detail1 = StringVar()                                   # 주요 작업내용을 입력함
e_detail1.set("주요 작업내용을 입력합니다.")                  
e_detail1 = Entry(work_status_frame, textvariable=e_detail1, state="readonly", justify="center", width=35)
e_detail1.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)
e_detail2 = Entry(work_status_frame, width=35) 
e_detail2.insert(0, "")
e_detail2.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)
e_detail3 = Entry(work_status_frame, width=35) 
e_detail3.insert(0, "")
e_detail3.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)
e_detail3 = Entry(work_status_frame, width=35) 
e_detail3.insert(0, "")
e_detail3.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 소요비용을 입력함
unit_frame = LabelFrame(root, text="소용비용", height= 150)

unit_meterial1 = StringVar()                               # 자재명을 입력함
unit_meterial1.set("자재명 / 인건비")
unit_meterial1 = Entry(unit_frame, textvariable=unit_meterial1, state="readonly", justify="center", width=33) 
unit_meterial1.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
unit_meterial2 = Entry(unit_frame, width=33) 
unit_meterial2.insert(0, "")
unit_meterial2.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
unit_meterial3 = Entry(unit_frame, width=33) 
unit_meterial3.insert(0, "")
unit_meterial3.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
unit_meterial4 = Entry(unit_frame, width=33) 
unit_meterial4.insert(0, "")
unit_meterial4.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)

total_amount1 = StringVar() 
total_amount1.set("총     계")
total_amount1 = Entry(unit_frame, textvariable=total_amount1, state="readonly", justify="center", width=33) 
total_amount1.grid(row=4, column=0, columnspan=3, sticky=N+E+W+S, padx=3, pady=3)

unit_price1 = StringVar()                                         # 자재단가를 입력함
unit_price1.set("단가(원)")
unit_price1 = Entry(unit_frame, textvariable=unit_price1, state="readonly", justify="center", width=12)
unit_price1.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
unit_price2 = Entry(unit_frame, justify="right", width=12) 
unit_price2.insert(0, "")
unit_price2.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
unit_price3 = Entry(unit_frame, justify="right", width=12) 
unit_price3.insert(0, "")
unit_price3.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
unit_price4 = Entry(unit_frame, justify="right", width=12) 
unit_price4.insert(0, "")
unit_price4.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)

unit_quantity1 = StringVar()                                    # 자재수량을 입력함
unit_quantity1.set("수량")
unit_quantity1 = Entry(unit_frame, textvariable=unit_quantity1, state="readonly", justify="center", width=10)
unit_quantity1.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
unit_quantity2 = Entry(unit_frame, justify="center", width=10) 
unit_quantity2.insert(0, "")
unit_quantity2.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
unit_quantity3 = Entry(unit_frame, justify="center", width=10) 
unit_quantity3.insert(0, "")
unit_quantity3.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
unit_quantity4 = Entry(unit_frame, justify="center", width=10) 
unit_quantity4.insert(0, "")
unit_quantity4.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)




unit_amount1 = IntVar()             # 금액을 입력함
unit_amount1.set("금액(원") 
unit_amount1 = Entry(unit_frame, textvariable=unit_amount1, state="readonly", justify="center", width=17)                                    
unit_amount1.grid(row=0, column=3, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)

txt_input2 = IntVar
unit_amount2 = Entry(unit_frame, textvariable=txt_input2, justify="right", width=17) 
unit_amount2.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

txt_input3 = IntVar
unit_amount3 = Entry(unit_frame, textvariable=txt_input3, justify="right", width=17) 
unit_amount3.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

txt_input4 = IntVar
unit_amount4 = Entry(unit_frame, textvariable=txt_input4, justify="right", width=17) 
unit_amount4.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

def total_amount():   # 계산식을 확인할 것
    a = int(unit_amount2.get())
    b = int(unit_amount3.get())
    c = int(unit_amount4.get())
    total_amount2.configure(text= a + b + c)

total_amount2 = Label(unit_frame, justify="right", width=17) 
total_amount2.grid(row=4, column=3, sticky=N+E+W+S, padx=3, pady=3)
action1 = Button(unit_frame, text="확인", command=total_amount).grid(row=4, column=4)


# 활동내용 및 특이사항 그리드 프레임
review_frame = LabelFrame(root, text="활동내용 및 특이사항을 입력하세요.")
review_txt = Text(review_frame, width=85, height=15)
review_txt.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)

# 종료 그리드 프레임
conform_cancel_save_frame = Frame(root)
ccsf1 = Frame(conform_cancel_save_frame, width=400)                      # 공백 그리드 프레임
ccsf1.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_conform = Button(conform_cancel_save_frame, text="확인")
btn_conform.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_cancel = Button(conform_cancel_save_frame, text="취소")
btn_cancel.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_save = Button(conform_cancel_save_frame, text="저장")
btn_save.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)


# 배치 그리드 프레임
title_frame.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
date_wether_frame.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
work_status_frame.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
unit_frame.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
review_frame.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
conform_cancel_save_frame.grid(row=5, column=0, sticky=N+E+W+S, padx=3, pady=3)

root.mainloop()