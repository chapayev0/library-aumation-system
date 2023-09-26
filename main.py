# -*- coding: utf-8 -*-
import time

from PyQt5.QtCore import pyqtSlot
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2 import QtWebEngineWidgets

from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image
import io

import sys
import sqlite3
import os

import requests

import tempfile
import barcode
from barcode import *
from barcode import Code128
from barcode.writer import ImageWriter


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



from ui.ui_main import *
from ui.ui_stu_box import Ui_Dialog
import time
#THIS_DIR = os.path.dirname(__file__)
#CODE_DIR = os.path.abspath(os.path.join(THIS_DIR, '..', 'ui'))
#sys.path.append(CODE_DIR)

book_id = ""
esp_data = ""

recip_counter = 0
window_maxmize = 0
database_recipt = "data/reciption_data.db"
database_apoinment = "data/apoinment_data.db"
database_system = "data/system.db"
database_pharmacy = "data/pharmacy_data.db"
recipt_bill_html = 'data/temp/recip_bill.html'
recipt_bill_pdf = 'data/temp/recip_bill.pdf'
ap_bill_html = 'data/temp/ap_bill.html'
ap_bill_pdf = 'data/temp/ap_bill.pdf'
src_html = "data/temp/src_page.html"
ap_src_html = "data/temp/ap_src_page.html"
ph_src_html = "data/temp/ph_src_bill.html"
empty_pdf = "data/temp/empty.pdf"

ph_bill_html = 'data/temp/ph_bill.html'
ap_id_cnt = 0
rc_id_cnt = 0

temp_ad_price = 0
temp_ap_id = ""
temp_ap_date = ""

temp_rc_price = 0
temp_rc_id = ""
temp_rc_date = ""
ph_bill_pdf = 'data/temp/ph_bill.pdf'
abs_file_path_ph_pdf = os.path.abspath(os.path.join(os.path.dirname(__file__), ph_bill_pdf))
abs_file_path_rec_pdf = os.path.abspath(os.path.join(os.path.dirname(__file__), recipt_bill_pdf))
abs_file_path_ap_pdf = os.path.abspath(os.path.join(os.path.dirname(__file__), ap_bill_pdf))
abs_file_path_empty_pdf = os.path.abspath(os.path.join(os.path.dirname(__file__), empty_pdf))

abs_file_path_rec_html = os.path.abspath(os.path.join(os.path.dirname(__file__), recipt_bill_html))

doct_id = ""
doc_name = ""
max_num = 0
cnt_max = 0

ap_date = ""
rc_date = ""

new_usr = 1

reciption_log = 0
admin_log = 0
pharmacist_log = 0
inventory_log = 0
splash_counter = 0


class SecondWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        # Load the UI from the generated module
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)




class main_ui(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        icon = QIcon(":/icon/assets/icon.ico")

        self.setWindowIcon(icon)

        #external parts

        self.time_counter = QTimer(self)
        self.time_counter.setInterval(1000)
        self.time_counter.start()

        #self.pr_view = Window()


        # move event

        def move_window(event):

            if event.buttons() == Qt.LeftButton:

                self.move(self.pos() + event.globalPos() - self.dragpos)
                self.dragpos = event.globalPos()


                event.accept()

        self.ui.left_container.mouseMoveEvent = move_window


        #shadow effect

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.root.setGraphicsEffect(self.shadow)

        self.shadow1 = QGraphicsDropShadowEffect(self)
        self.shadow1.setBlurRadius(20)
        self.shadow1.setXOffset(0)
        self.shadow1.setYOffset(0)
        self.shadow1.setColor(QColor(0, 0, 0, 60))





        # autorun functions

        self.default_price_total()


        # self.load_settings()
        self.usr_lst_update()


        self.ui.rc_radio.setChecked(True)


        #change below to set main page

        self.ui.main_stack.setCurrentWidget(self.ui.login_page)
        self.ui.login_stack.setCurrentWidget(self.ui.login_window)


        self.date_time()
        self.history_combo()

        self.id_generate()

        self.rep_home_clicked()



        self.ui.user_search.setFocus()



        # function commands




        self.time_counter.timeout.connect(self.date_time)

        self.ui.counter_next_btn.clicked.connect(self.recip_counter_inc)
        self.ui.counter_back_btn.clicked.connect(self.recip_counter_dec)
        self.ui.counter_reset_btn.clicked.connect(self.recip_counter_reset)

        self.ui.close_btn.clicked.connect(self.exit_fun)
        self.ui.minimize_btn.clicked.connect(self.window_min)
        self.ui.maxmize_btn.clicked.connect(self.window_max)

        self.ui.re_home.clicked.connect(self.rep_home_clicked)

        self.ui.re_history.clicked.connect(self.rep_history_clicked)

        self.ui.re_ok_btn.clicked.connect(self.write_recption_data)
        self.ui.rc_default_price.textChanged.connect(self.default_price_total)
        self.ui.rc_addtional_price.textChanged.connect(self.addtional_total_price)

        self.ui.history_cat_combo.currentTextChanged.connect(self.combo_change)


        self.ui.ap_list.itemDoubleClicked.connect(self.ap_update)
        self.ui.ap_edit_btn.clicked.connect(self.ap_update)

        self.ui.ap_up_addtional_price.textChanged.connect(self.ap_up_addtional_total_price)
        self.ui.ap_update_btn.clicked.connect(self.write_ap_update)
        self.ui.ap_update_cancle_btn.clicked.connect(self.ap_up_cancle)



        self.ui.re_list.itemDoubleClicked.connect(self.re_update)
        self.ui.re_edit_btn.clicked.connect(self.re_update)
        self.ui.re_up_addtional_price.textChanged.connect(self.re_up_addtional_total_price)
        self.ui.re_update_cancle_btn.clicked.connect(self.re_up_cancle)
        self.ui.re_update_btn.clicked.connect(self.write_re_update)



        self.ui.history_doc_combo.currentTextChanged.connect(self.search_by_doctor)

        self.ui.set_apply_btn.clicked.connect(self.rcp_setting_write)
        self.ui.re_setting.clicked.connect(self.setting_page)
        self.ui.set_cancle_btn.clicked.connect(self.set_cancle)
        self.ui.usr_control_btn.clicked.connect(self.user_control_page)
        self.ui.user_search.textChanged.connect(self.usr_lst_update)
        self.ui.usr_list.itemClicked.connect(self.usr_lst_item_clicked)
        self.ui.prev_combo.currentTextChanged.connect(self.prev_combo_click)
        self.ui.new_usr_btn.clicked.connect(self.new_user)
        self.ui.add_user_btn.clicked.connect(self.add_user)
        self.ui.del_user_btn.clicked.connect(self.user_delete)

        self.ui.login_btn.clicked.connect(self.login_function)
        self.ui.user_password.returnPressed.connect(self.login_function)
        self.ui.user_name.returnPressed.connect(self.login_function)
        self.ui.lodin_exit_btn.clicked.connect(self.exit)
        self.ui.login_try_btn.clicked.connect(self.try_again)
        self.ui.log_out_btn.clicked.connect(self.log_out)
        self.ui.update_user_btn.clicked.connect(self.user_update)
        self.ui.froget_pass_btn.clicked.connect(self.froget_password)
        self.ui.req_pass_reset.clicked.connect(self.request_reset)
        self.ui.pc_m_medicine.textChanged.connect(self.purchasse_list)
        self.ui.pc_m_list.itemClicked.connect(self.medi_list_click)
        self.ui.pc_prch_btn.clicked.connect(self.write_purchase)
        #auro run

        self.ui.pc_m_discount_typr.addItem("As a Percentage(%)")
        self.ui.pc_m_discount_typr.addItem("As Money Value(Rs)")
        self.ui.r_m_discount_typr.addItem("As a Percentage(%)")
        self.ui.r_m_discount_typr.addItem("As Money Value(Rs)")

        self.m_store_load()
        self.r_list_load()
        self.ui.m_store_company.textChanged.connect(self.med_store_upper)

        self.pharmacy_comobo_load()
        self.generate_medicin_id()
        self.ui.ad_add_btn.clicked.connect(self.write_medicine)
        self.ui.pc_m_company.textChanged.connect(self.med_company_upper)
        self.ui.pc_m_qty.textChanged.connect(self.calculate_pc_total)
        self.ui.pc_m_u_price.textChanged.connect(self.calculate_pc_total)
        self.ui.pc_m_discount_typr.currentTextChanged.connect(self.calculate_pc_total)
        self.ui.m_store_srch.textChanged.connect(self.store_list)
        self.ui.m_store_list.itemClicked.connect(self.store_list_click)
        self.ui.m_store_update.clicked.connect(self.m_store_update)
        self.ui.m_store_delete.clicked.connect(self.store_delete)
        self.ui.r_m_srch.textChanged.connect(self.release_list)
        self.ui.r_m_ad_list.itemClicked.connect(self.release_list_click)
        self.ui.r_add_btn.clicked.connect(self.release_add_click)

        self.ui.r_discount.textChanged.connect(self.calculate_r_total)
        self.ui.r_inv_btn.clicked.connect(self.ph_bill_print)
        self.ui.r_m_discount_typr.currentTextChanged.connect(self.calculate_r_total)

        self.ui.re_btn.clicked.connect(self.recption_page)

        self.ui.about_btn.clicked.connect(self.show_about)

        self.ui.usr_id.textChanged.connect(self.barcode_read)

        self.ui.ap_ok_btn.clicked.connect(self.add_user1)

        self.ui.new_usr_btn.clicked.connect(self.stu_trigger)

        self.ui.set_apply_btn.clicked.connect(self.user_update_book)

    def user_update_book(self):

        global book_id

        name = self.ui.set_rc_def_price.text()

        id = self.ui.usr_id.text()

        print(id)
        print(name)


        user_dat = sqlite3.connect(database_system)

        user_dat.text_factory

        cursor1 = user_dat.cursor()

        user_dat.interrupt()

        cursor1.execute("""UPDATE user_table SET user_name = '%s' WHERE id = '%s'""" % (name, book_id))

        user_dat.commit()
        cursor1.close()



    def stu_trigger(self):



        self.ui.recipt_stack.setCurrentWidget(self.ui.setting_page)

    def second_w_show(self):

        x = SecondWindow()
        x.show()

    def add_user1(self):

        global new_usr

        name = self.ui.ap_name.text()
        mail = self.ui.ap_age.text()
        id = self.ui.ap_phone_num.text()


        if name != "" or mail != "" or id != "":
            user_data = sqlite3.connect(database_system)

            user_data.text_factory

            cursor = user_data.cursor()

            data_tup = (name, mail, id)usr_list

            write_recipt_data = """INSERT INTO 'student' ('name', 'mail', 'id') VALUES (?, ?, ?)"""

            cursor.execute(write_recipt_data, data_tup)
            user_data.commit()
            cursor.close()

            new_usr = 0

            self.ui.ap_name.clear()
            self.ui.ap_age.clear()
            self.ui.ap_phone_num.clear()


    def auto_detect_books(self):

        book_id = self.ui.user_search.text()
    
    def connnect_esp_board(self):

        global esp_data

        global esp32_ip
        global esp32_port

        url = f"http://{esp32_ip}:{esp32_port}/data_endpoint"

        response = requests.get(url)

        if response.status_code == 200:
            esp_data = response.text

            print("book rcieved:", esp_data)

        else:
            print("Failed to detect book ")

    def mail_send(self, msg, reciver_mail):

        # Email configuration
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # Port for TLS
        sender_email = 'librarysystem24hr@gmail.com'
        password = 'hqrm uzbe ymnh cepq '  # Your Gmail account password

        # Create a message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = reciver_mail
        message['Subject'] = '24hr Library System'

        html_content = f"""
        <!DOCTYPE html>
        <html>
          <body>

            <img src="https://ibb.co/xScVT7n">
            
            <h1>Hello, this is 24hr Library System</h1>
            <p>{msg}</p>
            
          </body>
        </html>
        """

        # Add email body
        html_body = MIMEText(html_content, 'html')
        message.attach(html_body)

        # Connect to the SMTP server and send the email
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Use TLS for security
            server.login(sender_email, password)
            text = message.as_string()
            server.sendmail(sender_email, reciver_mail, text)
            print('Email sent successfully')
        except Exception as e:
            print(f'Error: {str(e)}')
        finally:
            server.quit()


    def send_mail(self, recipient_email, book_status):


        global sender_email , sender_password


        book_status = True

        if book_status:

            subject = "24H Book Retrieving System"
            message = "Dear Student, \n\nYou have successfully returned the book to the library."

            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = recipient_email
            msg["Subject"] = subject

            msg.attach(MIMEText(message, "plain"))

            # Connect to the SMTP server (Gmail in this case)
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)

            # Send the email
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print("Email sent successfully!")

            # Quit the server
            server.quit()
        else:
            print("No email sent because the book has not been returned.")





    def barcode_read(self):

        data = self.ui.usr_id.text()

        barcode_class = Code128
        barcode = barcode_class(data, writer=ImageWriter())

        # Convert the barcode image to a QImage
        barcode_image = io.BytesIO()
        barcode.write(barcode_image)
        barcode_qimage = QImage.fromData(barcode_image.getvalue())

        # Convert the QImage to a QPixmap
        barcode_pixmap = QPixmap.fromImage(barcode_qimage)
        resized_pixmap = barcode_pixmap.scaledToHeight(150)

        self.ui.barcodelabel.setAlignment(Qt.AlignCenter)
        self.ui.barcodelabel.setPixmap(resized_pixmap)




    def show_about(self):


        self.image = QImage(":/image/assets/about.jpg")
        self.pix_image = QPixmap.fromImage(self.image)
        self.ui.img_lbl.setPixmap(self.pix_image)
        self.ui.img_lbl.setScaledContents(True)

        self.ui.main_stack.setCurrentWidget(self.ui.reception_page)
        self.ui.recipt_stack.setCurrentWidget(self.ui.about_page)



    def stock_reduce1(self):
        print("ss")


    def stock_reduce(self):

        qty = int(self.ui.r_m_qty.text())
        stock = int(self.ui.r_m_stocks.text())

        if qty != "":

            print(str(stock))


            red_stock = stock - qty


            if red_stock <= 0:

                self.ui.r_m_stocks.setText("Medicine Out of Stocks")

            else:

                self.ui.r_m_stocks.setText(str(red_stock))





    def ph_bill_print(self):

        ph_db = sqlite3.connect(database_pharmacy)

        ph_db.text_factory

        cursor = ph_db.cursor()


        item_count = int(self.ui.r_m_list.count())
        invoice_number = self.ui.r_inv_number.text()
        total_price = self.ui.r_total.text()
        discount = self.ui.r_discount.text()
        disc_price = self.ui.r_afd_price.text()
        time = QTime.currentTime().toString("hh:mm AP")
        date = QDate.currentDate().toString("dd/MM/yyyy")
        d_t = time + " - " + date

        if self.ui.r_m_discount_typr.currentText() == "As a Percentage(%)":

            discount = discount + " %"

        else:
            discount = discount + ".00"




        cnt = 0

        data1 = ph_db.execute(""" SELECT * FROM release_medicine """)

        for i in data1:

            cnt += 1

        bill_num = "bl/n/" + str(cnt)

        if self.ui.r_inv_number.text() != "" and self.ui.r_total.text() != "":

            data_tup = (
                bill_num, invoice_number, date, time, total_price, item_count, discount, disc_price)

            write_ph_data = """INSERT INTO 'release_medicine' ( 'id', 'inv_id', 'date', 'time',
                         'total_price', 'item_count', 'discount', 'total_af_discount') VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)"""

            cursor.execute(write_ph_data, data_tup)
            ph_db.commit()

        else:
            #Need a massage

            pass

        for c in range(item_count):

            item = self.ui.r_m_list.item(c).text().split()

            med_name = item[0]
            med_qty = item[1]



            data_tup1 = (invoice_number, med_name, med_qty, date)

            write_ph_data1 = """INSERT INTO 'inv_data' ( 'inv_id', 'medicine', 'qty', 'date') VALUES ( ?, ?, ?, ?)"""

            cursor.execute(write_ph_data1, data_tup1)
            ph_db.commit()


        try:

            pass


        except Exception as x:

            print(x)

        html = open(ph_src_html)
        sop_data = bs(html, "html.parser")



        old_date = sop_data.find("td", text="date")
        old_date_text = str(sop_data.find("td", text="date").text)

        new_date = old_date.find(text=re.compile(old_date_text)).replace_with(d_t)

        bill_num_tag = sop_data.find("td", text="Bill No:")
        bill_num_text = str(sop_data.find("td", text="Bill No:").text)
        new_bill_num = bill_num_tag.find(text=re.compile(bill_num_text)).replace_with("Bill No: " + bill_num)

        old_t_price = sop_data.find("td", text="Total Rs.").find_next_sibling("td")
        old_t_price_text = str(sop_data.find("td", text="Total Rs.").find_next_sibling("td").text)
        new_t_price = old_t_price.find(text=re.compile(old_t_price_text)).replace_with(str(total_price))

        old_c_price = sop_data.find("td", text="Discount").find_next_sibling("td")
        old_c_price_text = str(sop_data.find("td", text="Discount").find_next_sibling("td").text)
        new_c_price = old_c_price.find(text=re.compile(old_c_price_text)).replace_with(str(discount))

        old_d_price = sop_data.find("td", text="Discount Added Price(Rs)").find_next_sibling("td")
        old_d_price_text = str(sop_data.find("td", text="Discount Added Price(Rs)").find_next_sibling("td").text)
        new_d_price = old_d_price.find(text=re.compile(old_d_price_text)).replace_with(str(disc_price))

        item_conut = self.ui.r_m_list.count()

        for i in range(item_conut):

            raw_text = self.ui.r_m_list.item(i).text().strip().split()
            name = raw_text[0]
            qty = raw_text[1]
            unit_price = raw_text[2] + ".00"
            price = raw_text[3] + ".00"

            item_tag = sop_data.find("arti")
            new_tag = sop_data.new_tag('tr class="item"')
            new_tag1 = sop_data.new_tag('td')
            new_tag1.append(name)
            new_tag2 = sop_data.new_tag('td')
            new_tag2.append(qty)
            new_tag3 = sop_data.new_tag('td')
            new_tag3.append(unit_price)
            new_tag4 = sop_data.new_tag('td')
            new_tag4.append(price)
            item_tag.insert_after(new_tag)
            item_tag.insert_after(new_tag4)
            item_tag.insert_after(new_tag3)
            item_tag.insert_after(new_tag2)
            item_tag.insert_after(new_tag1)

        with open(ph_bill_html, "wb") as f_output:
            f_output.write(sop_data.prettify("utf-8"))

        f_output.close()

        #os.system("wkhtmltopzzzdf.exe --enable-local-file-access %s %s" % (ph_bill_html, abs_file_path_ph_pdf))

        pdfkit.from_file(ph_bill_html, abs_file_path_ph_pdf, configuration=config)

        try:

            # self.ui.web_page.s

            print(abs_file_path_ph_pdf)


            self.print_win.ui.widget.dynamicCall('Navigate(const QString&)', abs_file_path_ph_pdf)


            # self.print_win.ui.widget_2.load(QtCore.QUrl.fromUserInput(abs_file_path_ph_pdf))
            self.print_win.ui.ph_print.hide()
            self.print_win.ui.rc_print.hide()
            self.print_win.ui.ap_print.hide()
            self.print_win.ui.ph_print.show()


            self.print_win.show()





        except Exception as msg:
            print("ssss")

            print(msg)








    def calculate_r_total(self):

        try:
            price = float(self.ui.r_total.text())
            discount_type = self.ui.r_m_discount_typr.currentText()
            discount = float(self.ui.r_discount.text())



            if discount != "" and discount_type == "As a Percentage(%)":

                disc = price/100*float(discount)
                self.ui.r_afd_price.setText(str(price - disc))

            elif discount != "" and discount_type == "As Money Value(Rs)":

                disc = price - float(discount)
                self.ui.r_afd_price.setText(str(disc) )

            else:

                self.ui.r_afd_price.setText("")




        except ValueError:
            pass



    def release_add_click(self):

        qty = int(self.ui.r_m_qty.text())
        price1 = float(self.ui.r_m_u_price.text())
        one_item_total = qty * price1
        med_name = str(self.ui.r_m_name.text())
        unit_price = self.ui.r_m_u_price.text()
        stock = int(self.ui.r_m_stocks.text())

        brand = self.ui.r_m_brand_2.text()

        red_stock = stock - qty

        if red_stock <= 0:

            stock_msg = QMessageBox.warning(self, 'Warning!', "Medicine Out of Stocks !",
                                              QMessageBox.Ok)


        else:

            if self.ui.r_total.text() == "":

                self.ui.r_total.setText(str(one_item_total))

            else:

                prev_total = float(self.ui.r_total.text())

                new_tot = prev_total + float(one_item_total)

                self.ui.r_total.setText(str(new_tot))

            ph_db = sqlite3.connect(database_pharmacy)

            ph_db.text_factory

            cursor = ph_db.cursor()

            cursor.execute("""UPDATE store SET qty = '%s' WHERE medicine_brand = '%s'""" % (red_stock, brand))

            ph_db.commit()
            cursor.close()

            self.ui.r_m_list.addItem(med_name + "\t" + str(qty) + "\t" + str(unit_price) + "\t" + str(one_item_total))

            self.ui.r_m_stocks.clear()

            self.ui.r_m_name.clear()
            self.ui.r_m_brand_2.clear()
            self.ui.r_m_exp.clear()
            self.ui.r_m_weight.clear()
            self.ui.r_m_u_price.clear()
            self.ui.r_m_qty.clear()
            self.store_list()





    def release_list_click(self):

        text = self.ui.r_m_ad_list.currentItem().text()
        spt = text.split("|")

        m_name = spt[1]

        brand = m_name.strip().split("\t")[0]

        db = sqlite3.connect(database_pharmacy)
        db.cursor()

        data1 = db.execute(""" SELECT * FROM store WHERE medicine_brand = '%s'""" % (brand))

        for i in data1:

            m_name = i[0]
            m_brand = i[1]
            qty = i[3]
            exp = i[6]
            unit = i[4]
            price = i[5]

        if int(qty)<= 0 :

            self.ui.r_m_stocks.setText("Medicine Out of Stocks")

        else:

            self.ui.r_m_stocks.setText(qty)

        self.ui.r_m_name.setText(m_name)
        self.ui.r_m_brand_2.setText(m_brand)
        self.ui.r_m_exp.setText(exp)
        self.ui.r_m_weight.setText(unit)
        self.ui.r_m_u_price.setText(price)


    def release_list(self):

        db = sqlite3.connect(database_pharmacy)
        db.cursor()

        self.ui.r_m_ad_list.clear()

        data1 = db.execute(""" SELECT * FROM store""")

        for i in data1:

            m_name = i[0]
            m_brand = i[1]
            unit_price = i[5]
            qty = i[3]



            if str(self.ui.r_m_srch.text()) in m_name:

                self.ui.r_m_ad_list.addItem(
                    m_name + "\t|\t" + m_brand + "\t|\t" + unit_price + "\t" + qty + "\t" )



    def r_list_load(self):

        ph_db = sqlite3.connect(database_pharmacy)

        ph_db.text_factory
        self.ui.r_m_ad_list.clear()

        data1 = ph_db.execute(""" SELECT * FROM store""")

        for i in data1:

            m_name = i[0]
            m_brand = i[1]
            unit_price = i[5]
            qty = i[3]


            self.ui.r_m_ad_list.addItem(m_name + "\t|\t" + m_brand + "\t|\t" + unit_price )


    def store_delete(self):

        m_brand = str(self.ui.m_store_brand.text())

        db = sqlite3.connect(database_pharmacy)
        cur = db.cursor()

        cur.execute(""" delete from store where medicine_brand = '%s'""" % (m_brand))
        db.commit()
        cur.close()

        self.m_store_load()
        self.ui.m_store_name.clear()
        self.ui.m_store_brand.clear()
        self.ui.m_store_company.clear()
        self.ui.m_store_unit.clear()
        self.ui.m_store_qty.clear()
        self.ui.m_store_exp.clear()
        self.ui.m_store_u_price.clear()


    def store_list_click(self):

        text = self.ui.m_store_list.currentItem().text()
        spt = text.split("|")
       # cleard = spt.strip()
        print(spt)
        m_name = spt[0]
        m_brand = spt[1]
        m_company = spt[2]
        qty = spt[3]
        exp = spt[4]
        unit = spt[5]
        price = spt[6]

        print()

        self.ui.m_store_name.setText(m_name.strip().split("\t")[0])
        self.ui.m_store_brand.setText(m_brand.strip().split("\t")[0])
        self.ui.m_store_company.setText(m_company.strip().split("\t")[0])
        self.ui.m_store_qty.setText(qty.strip().split("\t")[0])
        self.ui.m_store_u_price.setText(price.strip().split("\t")[0])
        self.ui.m_store_unit.setCurrentText(unit.strip().split("\t")[0])

        self.ui.m_store_exp.setText(exp.strip().split("\t")[0])

    def m_store_update(self):

        m_name = self.ui.m_store_name.text()
        m_brand = str(self.ui.m_store_brand.text())
        m_company = self.ui.m_store_company.text()
        unit = self.ui.m_store_unit.currentText()
        qty = str(self.ui.m_store_qty.text())
        exp = self.ui.m_store_exp.text()
        price = self.ui.m_store_u_price.text()
        st_id = ""


        ph_db = sqlite3.connect(database_pharmacy)

        ph_db.text_factory

        data1 = ph_db.execute(""" SELECT * FROM store""")

        for i in data1:

            text = i[1]

            if text == m_brand:

                st_id = i[7]

        cursor = ph_db.cursor()


        cursor.execute("""UPDATE store SET medicine_name = '%s', medicine_brand = '%s', medicine_company = '%s',
         qty = '%s', unit = '%s' , unit_price = '%s' , exp_date = '%s'  WHERE id = '%s'""" % (
        m_name, m_brand, m_company, qty, unit, price, exp, st_id))

        ph_db.commit()
        cursor.close()



        self.ui.m_store_name.clear()
        self.ui.m_store_brand.clear()
        self.ui.m_store_company.clear()
        self.ui.m_store_unit.clear()
        self.ui.m_store_qty.clear()
        self.ui.m_store_exp.clear()
        self.ui.m_store_u_price.clear()
        self.m_store_load()


    def store_list(self):

        db = sqlite3.connect(database_pharmacy)
        db.cursor()

        self.ui.m_store_list.clear()

        data1 = db.execute(""" SELECT * FROM store""")

        for i in data1:

            m_name = i[0]
            m_brand = i[1]
            m_company = i[2]
            qty = str(i[3])
            unit = str(i[4])
            unit_price = i[5]
            exp = i[6]


            if str(self.ui.m_store_srch.text()) in m_name:

                self.ui.m_store_list.addItem(
                    m_name + "\t|\t" + m_brand + "\t|\t" + m_company + "\t|\t" + qty + "\t|\t" + exp
                    + "\t|\t" + unit + "\t|\t" + unit_price + "\t")

    def m_store_load(self):

        ph_db = sqlite3.connect(database_pharmacy)

        ph_db.text_factory
        self.ui.m_store_list.clear()

        data1 = ph_db.execute(""" SELECT * FROM store""")

        for i in data1:

            m_name = i[0]
            m_brand = i[1]
            m_company = i[2]
            qty = str(i[3])
            unit = str(i[4])
            unit_price = i[5]
            exp = i[6]

            self.ui.m_store_list.addItem(m_name + "\t|\t" + m_brand + "\t|\t" + m_company + "\t|\t" + qty + "\t|\t" + exp
                                         + "\t|\t" + unit + "\t|\t" + unit_price)



    def write_purchase(self):

        ph_db = sqlite3.connect(database_pharmacy)

        ph_db.text_factory


        medicine_name = self.ui.pc_m_medicine.text()
        brand_name = self.ui.pc_m_brand.text()
        company_name = self.ui.pc_m_company.text()
        unit_price = str(self.ui.pc_m_u_price.text())
        discount = str(self.ui.pc_m_u_discount.text())
        total_price = str(self.ui.pc_m_total.text())
        purchase_date = QDate.currentDate().toString("dd/MM/yyyy")
        exp_date = str(self.ui.pc_m_exp.date().toString("dd/MM/yyyy"))
        qty = str(self.ui.pc_m_qty.text())

        data1 = ph_db.execute(""" SELECT * FROM purchase""")
        pc_cnt = 0

        for i in data1:

            pc_cnt += 1


        pc_id = "pc" + str(pc_cnt)

        data1 = ph_db.execute(""" SELECT * FROM store""")
        st_cnt = 0

        for i in data1:
            st_cnt += 1

        st_id = "st" + str(st_cnt)




        data1 = ph_db.execute(""" SELECT * FROM medicine""")

        for i in data1:

            text = i[1]

            if medicine_name == text:

                unit = i[2]

        if medicine_name != "" and brand_name != "" and company_name != "" and total_price != "" and qty != "":
            cursor = ph_db.cursor()

            data_tup = (
            medicine_name, brand_name, company_name, qty, unit_price, discount, total_price, purchase_date, exp_date, pc_id)

            write_ph_data = """INSERT INTO 'purchase' ( 'medicine_name', 'brand_name', 'company_name', 'qty',
                        'unit_price', 'discount', 'total_price', 'purchase_date', 'exp_date', 'id') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

            cursor.execute(write_ph_data, data_tup)
            ph_db.commit()


            # **********



            disc = float(unit_price) / 100 * float(self.ui.set_ph_sel_price.text())
            sale_price = float(int(unit_price) + float(disc))



            data_tup1 = (
                medicine_name, brand_name, company_name, qty, unit, sale_price, exp_date, st_id)

            write_ph_data1 = """INSERT INTO 'store' ( 'medicine_name', 'medicine_brand', 'medicine_company', 'qty',
                                    'unit', 'unit_price', 'exp_date', 'id') VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""

            cursor.execute(write_ph_data1, data_tup1)
            ph_db.commit()
            cursor.close()

            self.ui.pc_m_medicine.clear()
            self.ui.pc_m_brand.clear()
            self.ui.pc_m_company.clear()
            self.ui.pc_m_qty.clear()
            self.ui.pc_m_u_discount.clear()
            self.ui.pc_m_u_price.clear()
            self.ui.pc_m_total.clear()
            self.r_list_load()
            #self.ui.pc_m_list.clear()

        else:
            #need a massage

            pass




    def calculate_pc_total(self):

        try:
            qty = float(self.ui.pc_m_qty.text())
            price = float(self.ui.pc_m_u_price.text())
            discount_type = self.ui.pc_m_discount_typr.currentText()
            discount = self.ui.pc_m_u_discount.text()

            total = qty * price

            if discount != "" and discount_type == "As a Percentage(%)":

                disc = total/100*float(discount)
                self.ui.pc_m_total.setText(str(total - disc))

            elif discount != "" and discount_type == "As Money Value(Rs)":

                disc = total - float(discount)
                self.ui.pc_m_total.setText(str(disc) )

            else:

                self.ui.pc_m_total.setText(str(total) )




        except ValueError:
            pass




    def med_company_upper(self):

        text = self.ui.pc_m_company.text()

        self.ui.pc_m_company.setText(text.upper())

    def med_store_upper(self):

        text = self.ui.m_store_company.text()

        self.ui.m_store_company.setText(text.upper())


    def medi_list_click(self):

        self.ui.pc_m_medicine.setText(self.ui.pc_m_list.currentItem().text())


    def purchasse_list(self):

        db = sqlite3.connect(database_pharmacy)
        db.cursor()

        self.ui.pc_m_list.clear()

        data1 = db.execute(""" SELECT * FROM medicine""")

        for i in data1:

            text = i[1]

            if str(self.ui.pc_m_medicine.text()) in text:

                self.ui.pc_m_list.addItem(text)



    def write_medicine(self):
        ph_db = sqlite3.connect(database_pharmacy)

        ph_db.text_factory

        id = self.ui.ad_m_id.text()
        medicine_name = self.ui.ad_m_name.text()
        unit = self.ui.ad_m_unit_combo.currentText()
        foam = self.ui.ad_m_foam_combo.currentText()

        if medicine_name != "":
            cursor = ph_db.cursor()

            data_tup = (id, medicine_name, unit, foam)

            write_ph_data = """INSERT INTO 'medicine' ('id', 'medicine_name', 'unit', 'foam') VALUES (?, ?, ?, ?)"""

            cursor.execute(write_ph_data, data_tup)
            ph_db.commit()
            cursor.close()

        self.ui.ad_m_name.setText("")
        self.generate_medicin_id()


    def write_user(self):
        ph_db = sqlite3.connect(database_pharmacy)

        ph_db.text_factory

        id = self.ui.ad_m_id.text()
        medicine_name = self.ui.ad_m_name.text()
        unit = self.ui.ad_m_unit_combo.currentText()
        foam = self.ui.ad_m_foam_combo.currentText()

        if medicine_name != "":
            cursor = ph_db.cursor()

            data_tup = (id, medicine_name, unit, foam)

            write_ph_data = """INSERT INTO 'medicine' ('id', 'medicine_name', 'unit', 'foam') VALUES (?, ?, ?, ?)"""

            cursor.execute(write_ph_data, data_tup)
            ph_db.commit()
            cursor.close()

        self.ui.ad_m_name.setText("")
        self.generate_medicin_id()



    def generate_medicin_id(self):

        db = sqlite3.connect(database_pharmacy)
        db.cursor()

        data1 = db.execute(""" SELECT * FROM medicine""")

        cnt = 0

        for i in data1:
            cnt += 1

        med_id = "med" + str(cnt)

        self.ui.ad_m_id.setText(med_id)




    def pharmacy_comobo_load(self):

        db = sqlite3.connect(database_pharmacy)
        db.cursor()

        data1 = db.execute(""" SELECT * FROM unit""")

        for i in data1:

            self.ui.ad_m_unit_combo.addItem(i[0])
            self.ui.m_store_unit.addItem(i[0])

        data2 = db.execute(""" SELECT * FROM foam""")

        for x in data2:

            self.ui.ad_m_foam_combo.addItem(x[0])





        data3 = db.execute(""" SELECT * FROM medicine""")

        for y in data3:

            print("medi list")

            text = y[1]
            self.ui.pc_m_list.addItem(text)





    def firebase_db_connect(self):
        firebase_db = firebase.database()
        ap_db = sqlite3.connect(database_apoinment)
        rc_db = sqlite3.connect(database_recipt)
        ap_db.cursor()

        ap_total = 0
        rc_total = 0
        day_income = 0

        date = self.ui.history_date_edit.date().toString("dd/MM/yyyy")
        fr_date = self.ui.history_date_edit.date().toString("yyyy/MM/")

        apoinment_data =ap_db.execute(""" SELECT * FROM ap_data WHERE  date = '%s' """ % (date))

        for i in apoinment_data:
            ap_total = ap_total + int(i[7])

        print(ap_total)

        firebase_db.child("Income").child("ap").child(fr_date).set(ap_total)

        recip_data = rc_db.execute(""" SELECT * FROM rc_data WHERE  date = '%s' """ % (date))

        for x in recip_data:

            rc_total = rc_total + int(x[8])

        firebase_db.child("Income").child("rc").child(fr_date).set(rc_total)

        day_income = int(ap_total) + int(rc_total)

        firebase_db.child("Income").child("day_income").child(fr_date).set(day_income)

    def request_reset(self):
        self.ui.login_stack.setCurrentWidget(self.ui.login_window)

    def froget_password(self):

        self.ui.login_stack.setCurrentWidget(self.ui.try_again_page)

    def user_update(self):

        name = self.ui.usr_name.text()
        phone = self.ui.usr_phone.text()
        mail = self.ui.usr_mail.text()
        nic = self.ui.usr_nic.text()
        id = self.ui.usr_id.text()
        pos = self.ui.usr_position.text()
        usr_name = self.ui.user_l_name.text()
        passw  = self.ui.usr_pass.text()

        user_data = sqlite3.connect(database_system)

        user_data.text_factory

        cursor = user_data.cursor()




        cursor.execute("""UPDATE user_table SET name = '%s', position = '%s', phone = '%s',
         mail = '%s', id_number = '%s' , user_name = '%s' , password = '%s'  WHERE id = '%s'""" % (
        name, pos, phone, mail, nic, usr_name, passw, id))

        user_data.commit()
        cursor.close()

        self.usr_lst_update()

        self.ui.usr_name.clear()
        self.ui.usr_phone.clear()
        self.ui.usr_mail.clear()
        self.ui.usr_nic.clear()
        self.ui.usr_id.clear()
        self.ui.usr_position.clear()
        self.ui.user_l_name.clear()
        self.ui.usr_pass.clear()


    def log_out(self):
        global reciption_log, admin_log, pharmacist_log
        global inventory_log

        reciption_log = 0
        admin_log = 0
        pharmacist_log = 0
        inventory_log = 0

        log_out_msg = QMessageBox.warning(self, 'LogOut Alert!', "Are you shure you want to LogOut! ",
                                           QMessageBox.Yes | QMessageBox.No)

        if log_out_msg == QMessageBox.Yes:

            self.ui.main_stack.setCurrentWidget(self.ui.login_page)
            self.ui.login_stack.setCurrentWidget(self.ui.login_window)

        else:

            pass





    def try_again(self):

        self.ui.login_stack.setCurrentWidget(self.ui.login_window)


    def exit(self):

        self.close()


    def login_function(self):

        global reciption_log, admin_log, pharmacist_log
        global inventory_log

        usr = self.ui.user_name.text()
        passw = self.ui.user_password.text()

        print(usr)
        print(passw)


        db = sqlite3.connect(database_system)
        db.cursor()


        data = db.execute(""" SELECT * FROM user_table WHERE user_name = '%s' and password = '%s' """ % (usr, passw))
        print(data)


        for i in data:
            return_data = i[2]
            print(return_data)

        try:

            self.ui.main_stack.setCurrentWidget(self.ui.reception_page)
            self.ui.recipt_stack.setCurrentWidget(self.ui.user_control_page)
#            self.ui.pharmacy_btn.show()
#            self.ui.re_apoinment.show()
            self.ui.usr_control_btn.show()
            self.ui.re_btn.show()
            self.ui.re_history.show()

            if return_data == "Reciption":

                reciption_log = 1

                print("stack shange")

                self.ui.main_stack.setCurrentWidget(self.ui.reception_page)
                self.ui.recipt_stack.setCurrentWidget(self.ui.reciption_page)

                self.ui.usr_control_btn.hide()
                self.ui.pharmacy_btn.hide()
                self.ui.re_btn.show()
                self.ui.re_apoinment.show()

            elif return_data == "Admin":
                admin_log = 1

                self.ui.main_stack.setCurrentWidget(self.ui.reception_page)
                self.ui.recipt_stack.setCurrentWidget(self.ui.user_control_page)
                self.ui.pharmacy_btn.show()
                self.ui.re_apoinment.show()
                self.ui.usr_control_btn.show()
                self.ui.re_btn.show()
                self.ui.re_history.show()

            elif return_data == "Pharmacist":
                pharmacist_log = 1
                self.ui.main_stack.setCurrentWidget(self.ui.reception_page)
                self.ui.recipt_stack.setCurrentWidget(self.ui.pharmacy_page)
                self.ui.re_apoinment.hide()
                self.ui.usr_control_btn.hide()
                self.ui.re_btn.hide()
                self.ui.re_history.hide()
                self.ui.pharmacy_btn.show()
                print("print phar")

            elif return_data == "Inventory":
                inventory_log = 1

                pass

        except UnboundLocalError:

            print("login failed")

            self.ui.login_stack.setCurrentWidget(self.ui.pass_inc_page)

        self.ui.user_name.clear()
        self.ui.user_password.clear()



    def user_delete(self):

        global new_usr

        text = self.ui.usr_id.text()
        print(text)

        db = sqlite3.connect(database_system)
        cur = db.cursor()

        cur.execute(""" DELETE FROM user_table WHERE id = '%s'""" % (text))
        db.commit()
        cur.close()

        self.usr_lst_update()




    def add_user(self):

        global new_usr

        name = self.ui.usr_name.text()
        phone = self.ui.usr_phone.text()
        mail = self.ui.usr_mail.text()
        nic = self.ui.usr_nic.text()
        id = self.ui.usr_id.text()
        pos = self.ui.usr_position.text()
        usr_name = ""
        passw  = ""

        if new_usr == 1:

            user_data = sqlite3.connect(database_system)

            user_data.text_factory

            cursor = user_data.cursor()

            data_tup = (id, name, pos, phone, mail, nic, usr_name, passw)

            write_recipt_data = """INSERT INTO 'user_table' ('id', 'name', 'position', 'phone', 'mail',
                   'id_number', 'user_name', 'password') VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""

            cursor.execute(write_recipt_data, data_tup)
            user_data.commit()
            cursor.close()

            new_usr = 0
            self.usr_lst_update()

            self.ui.usr_name.clear()
            self.ui.usr_phone.clear()
            self.ui.usr_mail.clear()
            self.ui.usr_nic.clear()
            self.ui.usr_id.clear()
            self.ui.usr_position.clear()
            self.ui.user_l_name.clear()
            self.ui.usr_pass.clear()

    def add_book(self):
        book_name = self.name_input.text()
        author_name = self.author_input.text()
        book_id = self.id_input.text()
        price = self.price_input.text()
        category = self.category_input.text()

        # Connect to the SQLite database
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        # Insert book information into the database
        cursor.execute("INSERT INTO library (title, author, id, price, category) VALUES (?, ?, ?, ?, ?)",
                       (book_name, author_name, book_id, price, category))

        conn.commit()
        conn.close()

        self.name_input.clear()
        self.author_input.clear()
        self.id_input.clear()
        self.price_input.clear()
        self.category_input.clear()

        print("Book added to the database.")

    def return_book(self, book_id):


        if not book_id:
            return

        # Connect to the SQLite database
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        # Check if the book exists and is not already returned
        cursor.execute("SELECT id, returned FROM library WHERE id = ?", (book_id,))
        book = cursor.fetchone()

        if book is None:
            print("Book not found.")
        elif book[1] == 1:
            print("Book is already returned.")
        else:
            # Update the database to mark the book as returned
            cursor.execute("UPDATE library SET returned = 1 WHERE id = ?", (book_id,))
            conn.commit()
            print(f"Book ID {book_id} has been returned.")

        conn.close()
        self.book_id_input.clear()







    def new_user(self):

        global new_usr

        new_usr = 1

        self.ui.usr_name.clear()
        self.ui.usr_phone.clear()
        self.ui.usr_mail.clear()
        self.ui.usr_nic.clear()
        self.ui.usr_id.clear()
        self.ui.usr_position.clear()


    def prev_combo_click(self):

        id = self.ui.usr_id.text()
        p_text = self.ui.prev_combo.currentText()
        db = sqlite3.connect(database_system)
        db.cursor()

        data = db.execute(""" SELECT COUNT(*) FROM user_table WHERE position = '%s'""" % (p_text))

        for i in data:
            new_id = i[0] + 1

        if p_text == "History":

            id = "His_" + str(new_id)

        elif p_text == "Literature":

            id = "Litre_" + str(new_id)

        elif p_text == "Relegion":

            id = "Reli_" + str(new_id)

        elif p_text == "Math":

            id = "Math_" + str(new_id)

        self.ui.usr_id.setText(id)
        self.ui.usr_position.setText(p_text)


    def usr_lst_item_clicked(self):
        global new_usr
        global book_id
        new_usr = 0

        text = self.ui.usr_list.currentItem().text().split()
        id = text[0]
        db = sqlite3.connect(database_system)
        db.cursor()

        data = db.execute(""" SELECT * FROM user_table where id = '%s'""" % (id))

        for i in data:

            id = str(i[0])
            name = str(i[1])
            position = str(i[2])
            phone = str(i[3])
            mail = str(i[4])
            nic = str(i[5])
            username = str(i[6])
            password = str(i[7])

            book_id = id

            self.ui.usr_name.setText(name)
            self.ui.usr_phone.setText(phone)
            self.ui.usr_mail.setText(mail)
            self.ui.usr_nic.setText(nic)
            self.ui.usr_id.setText(id)
            self.ui.usr_position.setText(position)

        db.close()


    def book_success(self):

        url = "http://192.168.8.145/on"

        # Define the data you want to send as a dictionary
        data = "/on"
        # Send a POST request with the data
        response = requests.get(url, data=data)



        print(response.text)

        # Check the response from the server
        if response.status_code == 200:
            print("Data sent successfully")
        else:
            print("Failed to send data. Status code:", response.status_code)


    def book_failed(self):
        url = "http://192.168.8.145/off"

        # Define the data you want to send as a dictionary
        data = "/off"
        # Send a POST request with the data
        response = requests.get(url, data=data)



        # Check the response from the server
        if response.status_code == 200:
            print("Data sent successfully")
        else:
            print("Failed to send data. Status code:", response.status_code)



    def usr_lst_update(self):

        db = sqlite3.connect(database_system)
        db.cursor()
        cnt = 0
        self.ui.usr_list.clear()
        self.ui.prev_combo.clear()

        print("shashika")

        text = self.ui.user_search.text()

        print(text)

        if text != "":
            # Execute a SELECT query
            data = db.execute("SELECT * FROM user_table WHERE id = ?", (text,))
            result = data.fetchone()

            if result is None:

                self.book_failed()
                print("none")


                self.ui.usr_list.addItem("This book is not registered in the library. Please Remove the book!")

                smtp_server = 'smtp.gmail.com'
                smtp_port = 587  # Port for TLS
                sender_email = 'librarysystem24hr@gmail.com'
                password = 'hqrm uzbe ymnh cepq '
                reciver_mail = "sdilhara544@gmail.com"  # Your Gmail account password

                # Create a message
                message = MIMEMultipart()
                message['From'] = sender_email
                message['To'] = reciver_mail
                message['Subject'] = '24hr Library System'

                html_content = f"""
                                  <!DOCTYPE html>
                                  <html>
                                    <body>
    
                                      <img src="https://ibb.co/xScVT7n">
    
                                      <h1>Hello, this is 24hr Library System</h1>
                                      <p>Your book rejected by Library</p>
    
                                    </body>
                                  </html>
                                  """

                # Add email body
                html_body = MIMEText(html_content, 'html')
                message.attach(html_body)

                # Connect to the SMTP server and send the email
                try:
                    server = smtplib.SMTP(smtp_server, smtp_port)
                    server.starttls()  # Use TLS for security
                    server.login(sender_email, password)
                    text = message.as_string()
                    server.sendmail(sender_email, reciver_mail, text)
                    print('Email sent successfully')
                except Exception as e:
                    print(f'Error: {str(e)}')
                finally:
                    server.quit()


            else:

                self.book_success()
                # Iterate over the result tuple and add each value to the list
                formatted_data = "\t".join(str(value) for value in result)
                self.ui.usr_list.addItem(formatted_data)

                print(formatted_data)

                #self.mail_send("Your Book accepted by Library", value[6])
                smtp_server = 'smtp.gmail.com'
                smtp_port = 587  # Port for TLS
                sender_email = 'librarysystem24hr@gmail.com'
                password = 'hqrm uzbe ymnh cepq '
                reciver_mail = "sdilhara544@gmail.com"# Your Gmail account password

                # Create a message
                message = MIMEMultipart()
                message['From'] = sender_email
                message['To'] = reciver_mail
                message['Subject'] = '24hr Library System'

                html_content = f"""
                   <!DOCTYPE html>
                   <html>
                     <body>
    
                       <img src="https://ibb.co/xScVT7n">
    
                       <h1>Hello, this is 24hr Library System</h1>
                       <p>Your book accepted by Library</p>
    
                     </body>
                   </html>
                   """

                # Add email body
                html_body = MIMEText(html_content, 'html')
                message.attach(html_body)

                # Connect to the SMTP server and send the email
                try:
                    server = smtplib.SMTP(smtp_server, smtp_port)
                    server.starttls()  # Use TLS for security
                    server.login(sender_email, password)
                    text = message.as_string()
                    server.sendmail(sender_email, reciver_mail, text)
                    print('Email sent successfully')
                except Exception as e:
                    print(f'Error: {str(e)}')
                finally:
                    server.quit()
            # Close the cursor and the connection when done

        else:

            data = db.execute(""" SELECT * FROM user_table""")

            for i in data:
                cnt += 1

                name = i[1]
                position = i[2]
                phone = str(i[3])
                mail = i[4]
                id = i[0]

                self.ui.usr_list.addItem(id + "\t" + name + "\t" + phone + "\t" + position + "\t" + mail)

        data1 = db.execute(""" SELECT * FROM privelage_table""")

        for i in data1:

            val = str(i[1])
            self.ui.prev_combo.addItem(val)
        
        

    def user_control_page(self):

        self.ui.recipt_stack.setCurrentWidget(self.ui.user_control_page)


    def recption_page(self):

        self.ui.recipt_stack.setCurrentWidget(self.ui.reciption_page)

    def pharmacy_page(self):

        self.ui.recipt_stack.setCurrentWidget(self.ui.pharmacy_page)


    def set_cancle(self):
        self.ui.recipt_stack.setCurrentWidget(self.ui.reciption_page)

    def setting_page(self):

        self.ui.recipt_stack.setCurrentWidget(self.ui.setting_page)

    def rcp_setting_write(self):

        rc_def = self.ui.set_rc_def_price.text()


        user_data = sqlite3.connect(database_system)

        user_data.text_factory

        cursor = user_data.cursor()


        cursor.execute("""UPDATE rcp_settings SET value = '%s' WHERE name = 'rc_def_price'""" % (rc_def))

        user_data.commit()
        cursor.close()




    def cat_change(self):
        text = self.ui.history_cat_combo.currentText()

        if text == "Search by Patient Name":

            self.search_by_name()

        elif text == "Search by Doctor Name":

            self.search_by_name()



    def search_by_doctor(self):
        self.ui.patient_history_list.clear()

        print("ssssssssssdfffffffffff")

        global doct_id, max_num, doc_name


        cnt = 0
        total = 0

        db = sqlite3.connect(database_system)
        db.cursor()

        ap_db = sqlite3.connect(database_apoinment)
        ap_db.cursor()

        doctor = self.ui.history_doc_combo.currentText()
        sp = doctor.split("|")[0]
        doc_name = sp
        print(sp)


        date = self.ui.history_date_edit.date().toString("dd/MM/yyyy")

        print(date)


        data = db.execute(""" SELECT id FROM doctor_table WHERE name='%s' """ %  (sp))

        for i in data:
            doctr_id = i[0]
            print(doctr_id)

            doct_id = doctr_id



        ap_data = ap_db.execute(""" SELECT * FROM ap_data WHERE doc_id = '%s' and date = '%s' """ % (doct_id, date))

        for ap in ap_data:

            cnt += 1

            number = str(ap[8])
            name = ap[2]
            age = str(ap[3])
            time = ap[10]
            phone = str(ap[4])
            status = str(ap[11])
            price = int(ap[7])

            total = total + price

            self.ui.patient_history_list.addItem(str(cnt) + "\t" + name + "\t" + number + "\t"
                                                 + age + "\t" + phone + "\t" + time + "\t" + status)

        self.ui.history_cnt.setText(str(cnt))
        self.ui.history_income.setText(str(total) + ".00")




    def re_up_cancle(self):
        self.ui.recipt_stack.setCurrentWidget(self.ui.reciption_page)

    def sample_print(self):

        self.print_win.ui.widget_2.load(QtCore.QUrl.fromUserInput(abs_file_path_ph_pdf))

        self.print_win.ui.rc_print_2.hide()

        self.print_win.show()

    def write_re_update(self):

        global temp_rc_id, temp_rc_date
        global temp_rc_price


        new_ad = float(self.ui.re_up_addtional_price.text())

        status = "Updated"
        updated_date = QDate.currentDate().toString("dd/MM/yyyy")
        updated_time  = QTime.currentTime().toString("hh:mm AP")
        t_price  = self.ui.re_up_total_price.text()

        id = temp_rc_id
        inv = "Invoice No: " + id
        number = self.ui.re_up_num.text()
        print(number)
        name = self.ui.re_up_name.text()
        age = int(self.ui.re_up_age.text())
        date = updated_date
        time = updated_time
        default_price = float(self.ui.re_up_default_price.text())
        rep_def_price = str(default_price) + ".00"
        addtional_price = float(new_ad)
        rep_ad_price = str(addtional_price) + ".00"
        total_price = float(t_price)
        rep_total_price = str(total_price) + ".00"

        time = QTime.currentTime().toString("hh:mm AP")
        date = QDate.currentDate().toString("dd/MM/yyyy")

        d_t = time + " - " + date



        if new_ad<temp_rc_price:

            empty_val = QMessageBox.warning(self, 'Alert!', "Updated price can not be less than previous value !",
                                              QMessageBox.Ok | QMessageBox.No)



        else:

            user_data = sqlite3.connect(database_recipt)

            user_data.text_factory

            cursor = user_data.cursor()


            cursor.execute("""UPDATE rc_data SET status = '%s', updated_date = '%s', updated_time = '%s',
             total_price = '%s', addtional_price = '%s' WHERE id = '%s' and date = '%s'""" % (status, updated_date, updated_time, t_price, new_ad, temp_rc_id, temp_rc_date))

            user_data.commit()
            cursor.close()

            try:
                html = open(src_html)
                sop_data = bs(html, "html.parser")

                old_name = sop_data.find("td", text="Name").find_next_sibling("td")
                old_name_text = sop_data.find("td", text="Name").find_next_sibling("td").text
                new_name = old_name.find(text=re.compile(old_name_text)).replace_with(name)

                old_age = sop_data.find("td", text="Age").find_next_sibling("td")
                old_age_text = str(sop_data.find("td", text="Age").find_next_sibling("td").text)
                new_age = old_age.find(text=re.compile(old_age_text)).replace_with(str(age))

                old_number = sop_data.find("td", text="Apoinment Number").find_next_sibling("td")
                old_number_text = str(sop_data.find("td", text="Apoinment Number").find_next_sibling("td").text)
                new_number = old_number.find(text=re.compile(old_number_text)).replace_with(str(number))

                old_c_price = sop_data.find("td", text="Channeling Price Rs.").find_next_sibling("td")
                old_c_price_text = str(sop_data.find("td", text="Channeling Price Rs.").find_next_sibling("td").text)
                new_c_price = old_c_price.find(text=re.compile(old_c_price_text)).replace_with(str(rep_def_price))

                old_ad_price = sop_data.find("td", text="Addtional Price Rs.").find_next_sibling("td")
                old_ad_price_text = str(sop_data.find("td", text="Addtional Price Rs.").find_next_sibling("td").text)
                new_ad_price = old_ad_price.find(text=re.compile(old_ad_price_text)).replace_with(str(rep_ad_price))

                old_t_price = sop_data.find("td", text="Total Rs.").find_next_sibling("td")
                old_t_price_text = str(sop_data.find("td", text="Total Rs.").find_next_sibling("td").text)
                new_t_price = old_t_price.find(text=re.compile(old_t_price_text)).replace_with(str(rep_total_price))

                old_date = sop_data.find("td", text="date")
                old_date_text = str(sop_data.find("td", text="date").text)
                print(old_date_text)
                new_date = old_date.find(text=re.compile(old_date_text)).replace_with(d_t)

                old_inv = sop_data.find("td", text="Invoice No:")
                old_inv_text = str(sop_data.find("td", text="Invoice No:").text)
                print(old_date_text)
                new_inv = old_inv.find(text=re.compile(old_inv_text)).replace_with(inv)

                print(old_name_text)
                print(old_age_text)
                print(old_number_text)
                print(old_c_price_text)



            except Exception:

                print("error")

            with open(recipt_bill_html, "wb") as f_output:
                f_output.write(sop_data.prettify("utf-8"))

            f_output.close()

            pdfkit.from_file(abs_file_path_rec_html, abs_file_path_rec_pdf, configuration=config)

            try:

                # self.ui.web_page.s

               # self.print_win.ui.widget_2.load(QtCore.QUrl.fromUserInput(abs_file_path_rec_pdf))
                self.print_win.ui.widget.dynamicCall('Navigate(const QString&)', abs_file_path_rec_pdf)


                self.print_win.ui.rc_print.show()

                self.print_win.ui.ph_print.hide()
                self.print_win.ui.ap_print.hide()
                self.print_win.show()







            except Exception as msg:
                print("ssss")

                print(msg)

            self.re_list_update()

    def re_up_addtional_total_price(self):



        try:

            if self.ui.re_up_addtional_price.text() != "":


                default_price = float(self.ui.re_up_default_price.text())
                addtional = float(self.ui.re_up_addtional_price.text())

                total_price = default_price + addtional

                self.ui.re_up_total_price.setText(str(total_price))



        except ValueError:

            pass


    def re_update(self):

        global temp_rc_id, temp_rc_date
        global temp_rc_price


        text = self.ui.re_list.currentItem().text().split()
        re_id = text[3]
        print(re_id)

        date = QDate.currentDate().toString("dd/MM/yyyy")




        db = sqlite3.connect(database_recipt)
        db.cursor()

        data = db.execute(""" SELECT * FROM rc_data WHERE id='%s' and date='%s' """ % (re_id, date))

        for i in data:

            name = i[2]
            age = i[3]
            d_price = i[6]
            a_price = i[7]
            t_price = i[8]
            number = i[1]
            time = i[5]



        self.ui.re_up_date.setText(date)
        self.ui.re_up_name.setText(name)
        self.ui.re_up_age.setText(str(age))
        self.ui.re_up_default_price.setText(str(d_price))
        self.ui.re_up_addtional_price.setText(str(a_price))
        self.ui.re_up_total_price.setText(str(t_price))
        self.ui.re_up_num.setText(str(number))
        self.ui.re_up_time.setText(time)

        self.ui.re_up_addtional_price.setFocus()

        temp_rc_id = re_id
        temp_rc_date = date
        temp_rc_price = float(self.ui.re_up_addtional_price.text())


        self.ui.recipt_stack.setCurrentWidget(self.ui.re_update_page)



    def ap_up_cancle(self):
        self.ui.recipt_stack.setCurrentWidget(self.ui.appoinment_page)

    def ap_up_addtional_total_price(self):



        try:

            if self.ui.ap_up_addtional_price.text() != "":


                default_price = float(self.ui.ap_up_default_price.text())
                addtional = float(self.ui.ap_up_addtional_price.text())

                total_price = default_price + addtional

                self.ui.ap_up_total_price.setText(str(total_price))



        except ValueError:

            pass



    def write_ap_update(self):

        global temp_ad_price
        global temp_ap_id, temp_ap_date

        new_ad = float(self.ui.ap_up_addtional_price.text())

        status = "Updated"
        updated_date = QDate.currentDate().toString("dd/MM/yyyy")
        updated_time = time = QTime.currentTime().toString("hh:mm AP")
        t_price  = self.ui.ap_up_total_price.text()

        id = temp_ap_id
        inv = "Invoice No: " + id
        ap_name = self.ui.ap_up_name.text()
        ap_age = self.ui.ap_up_age.text()
        ap_phone = int(self.ui.ap_up_phone.text())
        ap_default_price = float(self.ui.ap_up_default_price.text())
        ap_addtional_price = float(new_ad)
        ap_total_price = float(t_price)
        ap_number = self.ui.ap_up_num.text()
        doc_name = self.ui.ap_up_doc.text()


        rep_def_price = str(ap_default_price) + ".00"
        rep_ad_price = str(ap_addtional_price) + ".00"
        rep_total_price = str(ap_total_price) + ".00"

        time = QTime.currentTime().toString("hh:mm AP")
        date = QDate.currentDate().toString("dd/MM/yyyy")

        d_t = time + " - " + date



        if new_ad<temp_ad_price:

            msg = QMessageBox(self)
            # msg.setIcon(QMessageBox.warning)
            msg.setText("Updated price can not be less than previous value !")
            msg.setWindowTitle("Alert!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()

        else:

            user_data = sqlite3.connect(database_apoinment)

            user_data.text_factory

            cursor = user_data.cursor()


            cursor.execute("""UPDATE ap_data SET status = '%s', updated_date = '%s', updated_time = '%s',
             total_price = '%s', addtional_price = '%s' WHERE id = '%s' and date = '%s'""" % (status, updated_date, updated_time, t_price, new_ad, temp_ap_id, temp_ap_date))

            user_data.commit()
            cursor.close()

            try:
                html = open(ap_src_html)
                sop_data = bs(html, "html.parser")

                old_name = sop_data.find("td", text="Name").find_next_sibling("td")
                old_name_text = sop_data.find("td", text="Name").find_next_sibling("td").text
                new_name = old_name.find(text=re.compile(old_name_text)).replace_with(ap_name)

                old_age = sop_data.find("td", text="Age").find_next_sibling("td")
                old_age_text = str(sop_data.find("td", text="Age").find_next_sibling("td").text)
                new_age = old_age.find(text=re.compile(old_age_text)).replace_with(str(ap_age))

                old_number = sop_data.find("td", text="Apoinment Number").find_next_sibling("td")
                old_number_text = str(sop_data.find("td", text="Apoinment Number").find_next_sibling("td").text)
                new_number = old_number.find(text=re.compile(old_number_text)).replace_with(str(ap_number))

                old_c_price = sop_data.find("td", text="Channeling Price Rs.").find_next_sibling("td")
                old_c_price_text = str(sop_data.find("td", text="Channeling Price Rs.").find_next_sibling("td").text)
                new_c_price = old_c_price.find(text=re.compile(old_c_price_text)).replace_with(str(rep_def_price))

                old_ad_price = sop_data.find("td", text="Addtional Price Rs.").find_next_sibling("td")
                old_ad_price_text = str(sop_data.find("td", text="Addtional Price Rs.").find_next_sibling("td").text)
                new_ad_price = old_ad_price.find(text=re.compile(old_ad_price_text)).replace_with(str(rep_ad_price))

                old_t_price = sop_data.find("td", text="Total Rs.").find_next_sibling("td")
                old_t_price_text = str(sop_data.find("td", text="Total Rs.").find_next_sibling("td").text)
                new_t_price = old_t_price.find(text=re.compile(old_t_price_text)).replace_with(str(rep_total_price))

                old_date = sop_data.find("td", text="date")
                old_date_text = str(sop_data.find("td", text="date").text)
                print(old_date_text)
                new_date = old_date.find(text=re.compile(old_date_text)).replace_with(d_t)

                old_inv = sop_data.find("td", text="Invoice No:")
                old_inv_text = str(sop_data.find("td", text="Invoice No:").text)
                print(old_date_text)
                new_inv = old_inv.find(text=re.compile(old_inv_text)).replace_with(inv)

                old_doc_name = sop_data.find("td", text="Doctor Name").find_next_sibling("td")
                old_doc_name_text = str(sop_data.find("td", text="Doctor Name").find_next_sibling("td").text)
                new_doc_name = old_doc_name.find(text=re.compile(old_doc_name_text)).replace_with(str(doc_name))

                old_phone_num = sop_data.find("td", text="Phone Number").find_next_sibling("td")
                old_phone_num_text = str(sop_data.find("td", text="Phone Number").find_next_sibling("td").text)
                new_phone_num = old_phone_num.find(text=re.compile(old_phone_num_text)).replace_with(str(ap_phone))

                print(old_name_text)
                print(old_age_text)
                print(old_number_text)
                print(old_c_price_text)


            except Exception:

                print("error")

            with open(ap_bill_html, "wb") as f_output:
                f_output.write(sop_data.prettify("utf-8"))

            f_output.close()

            pdfkit.from_file(ap_bill_html, ap_bill_pdf, configuration=config)

            self.print_win.ui.widget.dynamicCall('Navigate(const QString&)', abs_file_path_ap_pdf)

            #self.print_win.ui.widget_2.load(QtCore.QUrl.fromUserInput(abs_file_path_ap_pdf))

            self.print_win.ui.ph_print.hide()

            self.print_win.ui.rc_print.hide()
            self.print_win.ui.ap_print.show()

            self.print_win.show()

            self.doctor_select_combo()




    def ap_update(self):

        global temp_ap_id, temp_ap_date
        global temp_ad_price


        text = self.ui.ap_list.currentItem().text().split()
        ap_id = text[2]
        date = self.ui.ap_date_search.date().toString("dd/MM/yyyy")

        doctor = self.ui.doc_combo.currentText()
        sp = doctor.split("|")[0]
        doc_name = sp

        print(ap_id)

        db = sqlite3.connect(database_apoinment)
        db.cursor()

        data = db.execute(""" SELECT * FROM ap_data WHERE id='%s' and date='%s' """ % (ap_id, date))

        for i in data:

            name = i[2]
            age = i[3]
            phone = i[4]
            d_price = i[5]
            a_price = i[6]
            t_price = i[7]
            number = i[8]
            time = i[10]


        self.ui.ap_up_doc.setText(doc_name)
        self.ui.ap_up_date.setText(date)
        self.ui.ap_up_name.setText(name)
        self.ui.ap_up_age.setText(str(age))
        self.ui.ap_up_phone.setText(str(phone))
        self.ui.ap_up_default_price.setText(str(d_price))
        self.ui.ap_up_addtional_price.setText(str(a_price))
        self.ui.ap_up_total_price.setText(str(t_price))
        self.ui.ap_up_num.setText(str(number))
        self.ui.ap_up_time.setText(time)

        self.ui.ap_up_addtional_price.setFocus()

        temp_ap_id = ap_id
        temp_ap_date = date
        temp_ad_price = float(self.ui.ap_up_addtional_price.text())


        self.ui.recipt_stack.setCurrentWidget(self.ui.ap_update_page)

    def id_generate(self):

        global ap_id_cnt, rc_id_cnt

        ap_db = sqlite3.connect(database_apoinment)
        rc_db = sqlite3.connect(database_recipt)
        date = QDate.currentDate().toString("dd/MM/yyyy")

        ap_cur = ap_db.cursor()
        rc_cur = rc_db.cursor()

        ap_cur.execute("""SELECT * FROM ap_data WHERE date = '%s' """ % (date))
        ap_id_cnt = len(ap_cur.fetchall())

        rc_cur.execute("""SELECT * FROM rc_data WHERE date = '%s'""" % (date))
        rc_id_cnt = len(rc_cur.fetchall())

        print("ap id", ap_id_cnt )
        print("rc i",rc_id_cnt)



    def create_tables(self):

        global ap_date
        global rc_date

        date = QDate.currentDate().toString("dd_MM_yyyy")
        ap_date = "ap_" + date
        print(ap_date)
        rc_date = "rc_" + date

        ap_db = sqlite3.connect(database_apoinment)
        rc_db = sqlite3.connect(database_recipt)

        ap_cur = ap_db.cursor()

        rc_cur = rc_db.cursor()

        ap_cur.execute(""" CREATE TABLE IF NOT EXISTS "%s" (
	"id"	INTEGER NOT NULL ,
	"doc_id"	TEXT NOT NULL,
	"p_name"	TEXT,
	"p_age"	TEXT,
	"p_id_number"	TEXT,
	"p_phone_num"	INTEGER,
	"default_price"	INTEGER,
	"addtional_price"	INTEGER,
	"total_price"	INTEGER,
	"number"	INTEGER,
	"date"	TEXT,
	"time"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
	
)""" % (ap_date) )

        ap_db.close()

        rc_cur.execute(""" CREATE TABLE IF NOT EXISTS "%s"(
        
        "id"	INTEGER NOT NULL,
	"number"	INTEGER NOT NULL,
	"name"	TEXT,
	"age"	INTEGER,
	"date"	TEXT,
	"time"	TEXT,
	"default_price"	INTEGER,
	"addtional_price"	INTEGER,
	"total_price"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
	)""" % (rc_date))

        rc_db.close()


    def cancle_print(self):
        self.print_win.close()
        self.print_win.ui.widget.dynamicCall('Navigate(const QString&)', abs_file_path_empty_pdf)

    def ph_print(self):


        pdf_dir = abs_file_path_ph_pdf
        for f in glob(pdf_dir, recursive=True):
            win32api.ShellExecute(0, "print", f, None, ".", 0)

        self.print_win.close()
        self.counter_auto_num()
        self.print_win.ui.widget.dynamicCall('Navigate(const QString&)', abs_file_path_empty_pdf)

       # self.print_win.ui.widget.dynamicCall('Navigate(const QString&)', abs_file_path_rec_pdf)



        self.ui.rc_addtional_price.setText("0")
        self.ui.r_m_list.clear()
        self.ui.r_inv_number.clear()
        self.ui.r_total.clear()
        self.ui.r_discount.clear()
        self.ui.r_afd_price.clear()

    def print_recipt(self):



        print(recipt_bill_html)
        print(recipt_bill_pdf)

        pdf_dir = abs_file_path_rec_pdf
        for f in glob(pdf_dir, recursive=True):
            win32api.ShellExecute(0, "print", f, None, ".", 0)

        self.print_win.close()
        self.counter_auto_num()
        self.print_win.ui.widget.dynamicCall('Navigate(const QString&)', abs_file_path_empty_pdf)

       # self.print_win.ui.widget.dynamicCall('Navigate(const QString&)', abs_file_path_ap_pdf)


        self.ui.rc_addtional_price.setText("0")
        self.ui.rc_name.clear()
        self.ui.rc_age.clear()

    def print_ap(self):


        pdf_dir = abs_file_path_ap_pdf
        for f in glob(pdf_dir, recursive=True):
            win32api.ShellExecute(0, "print", f, None, ".", 0)

        self.print_win.close()
        self.counter_auto_num()
        self.print_win.ui.widget.dynamicCall('Navigate(const QString&)', abs_file_path_empty_pdf)

   #     self.print_win.ui.widget.dynamicCall('Navigate(const QString&)', abs_file_path_rec_pdf)

        self.ui.ap_name.clear()
        self.ui.ap_addtional_price.setText("0")
        self.ui.ap_age.clear()
        self.ui.ap_phone_num.clear()




    def history_date_search(self):

        cnt = 0

        ap_db = sqlite3.connect(database_apoinment)
        ap_db.text_factory

        date = self.ui.ap_date_search.date().toString("dd/MM/yyyy")
        print(date)

        data = ap_db.execute(""" SELECT * FROM ap_data WHERE date '%s'""" % (date))

        for ap in data:
            cnt += 1

            name = ap[2]
            age = ap[3]
            num = ap[9]
            phone = ap[5]
            nic = [4]

            self.ui.patient_history_list.addItem(str(cnt) + "   " + str(name) + "   " + str(num) + "    " + str(age) + "    " + str(nic) + "    " + str(phone))


    def combo_change(self):

        if self.ui.history_cat_combo.currentText() == "Search by Patient Name":


            self.ui.history_doc_combo.hide()
            self.search_by_name()



        elif self.ui.history_cat_combo.currentText() == "Search by Doctor Name":

            self.search_by_doctor()

            self.ui.history_doc_combo.show()

            self.ui.ap_radio.setChecked(True)



    def history_combo(self):

        db = sqlite3.connect(database_system)
        db.text_factory

        data = db.execute(""" SELECT * FROM category_table""")

        for doc_info in data:
            cat_name = doc_info[1]


            self.ui.history_cat_combo.addItem(str(cat_name))

        self.ui.history_cat_combo.setCurrentIndex(0)


        self.ui.history_doc_combo.hide()

    def doctor_select_combo(self):

        global doct_id, max_num, doc_name

        self.ui.ap_list.clear()
        cnt = 0

        db = sqlite3.connect(database_system)
        db.cursor()

        ap_db = sqlite3.connect(database_apoinment)
        ap_db.cursor()

        doctor = self.ui.doc_combo.currentText()
        sp = doctor.split("|")[0]
        doc_name = sp
        print(sp)


        date = self.ui.ap_date_search.date().toString("dd/MM/yyyy")

        print(date)


        data = db.execute(""" SELECT id FROM doctor_table WHERE name='%s' """ %  (sp))

        for i in data:
            doctr_id = i[0]
            print(doctr_id)

            doct_id = doctr_id



        ap_data = ap_db.execute(""" SELECT * FROM ap_data WHERE doc_id = '%s' and date = '%s' """ % (doct_id, date))

        for ap in ap_data:

            cnt += 1

            number = str(ap[0])
            p_name = ap[2]
            phone = str(ap[5])
            time = str(ap[10])

            self.ui.ap_list.addItem("Number : " + number + "\n" + "Patient Name : " + p_name + "\n"
                                    "Phone Number : " + phone + "\n" + "Time : " + time)

        self.ui.total_apoinments.setText(str(cnt))

        self.counter_auto_num()





    def recipt_apoinment_write(self):

        global doct_id, max_num, ap_id_cnt
        global doc_name

        id = "inv/ap/" + str(ap_id_cnt)
        inv = "Invoice No: " + id
        ap_name = self.ui.ap_name.text()
        ap_age = self.ui.ap_age.text()
        ap_phone = int(self.ui.ap_phone_num.text())
        ap_default_price = float(self.ui.ap_default_price.text())
        ap_addtional_price = float(self.ui.ap_addtional_price.text())
        ap_total_price = float(self.ui.ap_total_price.text())
        ap_number = self.ui.next_num.text()
        status = "Not Updated"
        updated_time = "Not Updated"
        updated_date = "Not Updated"

        rep_def_price = str(ap_default_price) + ".00"
        rep_ad_price = str(ap_addtional_price) + ".00"
        rep_total_price = str(ap_total_price) + ".00"



        time = QTime.currentTime().toString("hh:mm AP")
        date = self.ui.ap_date_search.date().toString("dd/MM/yyyy")

        d_t = time + " - " + date


        user_data = sqlite3.connect(database_apoinment)

        user_data.text_factory

        cursor = user_data.cursor()


        data_tup = (id, doct_id, ap_name, ap_age, ap_phone, ap_default_price, ap_addtional_price, ap_total_price, ap_number, date, time, status, updated_time, updated_date)



        write_recipt_data = """INSERT INTO 'ap_data' ('id', 'doc_id', 'p_name', 'p_age', 'p_phone_num',
         'default_price', 'addtional_price', 'total_price', 'number', 'date', 'time', 'status', 'updated_time', 'updated_date') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        cursor.execute(write_recipt_data, data_tup)
        user_data.commit()
        cursor.close()


        try:
            html = open(ap_src_html)
            sop_data = bs(html, "html.parser")

            old_name = sop_data.find("td", text="Name").find_next_sibling("td")
            old_name_text = sop_data.find("td", text="Name").find_next_sibling("td").text
            new_name = old_name.find(text=re.compile(old_name_text)).replace_with(ap_name)

            old_age = sop_data.find("td", text="Age").find_next_sibling("td")
            old_age_text = str(sop_data.find("td", text="Age").find_next_sibling("td").text)
            new_age = old_age.find(text=re.compile(old_age_text)).replace_with(str(ap_age))

            old_number = sop_data.find("td", text="Apoinment Number").find_next_sibling("td")
            old_number_text = str(sop_data.find("td", text="Apoinment Number").find_next_sibling("td").text)
            new_number = old_number.find(text=re.compile(old_number_text)).replace_with(str(ap_number))

            old_c_price = sop_data.find("td", text="Channeling Price Rs.").find_next_sibling("td")
            old_c_price_text = str(sop_data.find("td", text="Channeling Price Rs.").find_next_sibling("td").text)
            new_c_price = old_c_price.find(text=re.compile(old_c_price_text)).replace_with(str(rep_def_price))

            old_ad_price = sop_data.find("td", text="Addtional Price Rs.").find_next_sibling("td")
            old_ad_price_text = str(sop_data.find("td", text="Addtional Price Rs.").find_next_sibling("td").text)
            new_ad_price = old_ad_price.find(text=re.compile(old_ad_price_text)).replace_with(str(rep_ad_price))

            old_t_price = sop_data.find("td", text="Total Rs.").find_next_sibling("td")
            old_t_price_text = str(sop_data.find("td", text="Total Rs.").find_next_sibling("td").text)
            new_t_price = old_t_price.find(text=re.compile(old_t_price_text)).replace_with(str(rep_total_price))

            old_date = sop_data.find("td", text="date")
            old_date_text = str(sop_data.find("td", text="date").text)
            print(old_date_text)
            new_date = old_date.find(text=re.compile(old_date_text)).replace_with(d_t)

            old_inv = sop_data.find("td", text="Invoice No:")
            old_inv_text = str(sop_data.find("td", text="Invoice No:").text)
            print(old_date_text)
            new_inv = old_inv.find(text=re.compile(old_inv_text)).replace_with(inv)

            old_doc_name = sop_data.find("td", text="Doctor Name").find_next_sibling("td")
            old_doc_name_text = str(sop_data.find("td", text="Doctor Name").find_next_sibling("td").text)
            new_doc_name = old_doc_name.find(text=re.compile(old_doc_name_text)).replace_with(str(doc_name))

            old_phone_num = sop_data.find("td", text="Phone Number").find_next_sibling("td")
            old_phone_num_text = str(sop_data.find("td", text="Phone Number").find_next_sibling("td").text)
            new_phone_num = old_phone_num.find(text=re.compile(old_phone_num_text)).replace_with(str(ap_phone))

            print(old_name_text)
            print(old_age_text)
            print(old_number_text)
            print(old_c_price_text)


        except Exception:

            print("error")

        with open(ap_bill_html, "wb") as f_output:
            f_output.write(sop_data.prettify("utf-8"))

        f_output.close()

        pdfkit.from_file(ap_bill_html, ap_bill_pdf, configuration=config)


        try:

            # self.ui.web_page.s


            self.print_win.ui.widget.dynamicCall('Navigate(const QString&)', abs_file_path_ap_pdf)


            # self.print_win.ui.widget_2.load(QtCore.QUrl.fromUserInput(abs_file_path_ph_pdf))
            self.print_win.ui.ap_print.show()
            self.print_win.ui.rc_print.hide()
            self.print_win.ui.ph_print.hide()


            self.print_win.show()

        except Exception:
            pass


        self.doctor_select_combo()



    def addtional_total_price(self):

        try:

            if self.ui.rc_addtional_price.text() != "":
                default_price = float(self.ui.rc_default_price.text())
                addtional = float(self.ui.rc_addtional_price.text())

                total_price = default_price + addtional

                self.ui.rc_total_price.setText(str(total_price))

            else:
                self.ui.rc_addtional_price.setText("0")

        except ValueError:

            print("Value error")

    def ap_addtional_total_price(self):

        if self.ui.ap_addtional_price.text() != "":

            default_price = float(self.ui.ap_default_price.text())
            addtional = float(self.ui.ap_addtional_price.text())

            total_price = default_price + addtional

            self.ui.ap_total_price.setText(str(total_price))

        else:
            pass
            #self.ui.ap_addtional_price.setText("0")

    def default_price_total(self):

        self.ui.rc_total_price.setText(str(self.ui.rc_default_price.text()))



    def write_recption_data(self):
        global rc_date, rc_id_cnt

        print(rc_date)
        rc_id_cnt = rc_id_cnt + 1



        #cursor = user_data.cursor()

        try:
            user_data = sqlite3.connect(database_recipt)

            user_data.text_factory

            id = "inv/rc/" + str(rc_id_cnt)
            inv = "Invoice No: " + id
            number = self.ui.counter_lbl.text()
            print(number)
            name = self.ui.rc_name.text()
            age = int(self.ui.rc_age.text())
            date = self.ui.rc_date.text()
            time = self.ui.rc_time.text()
            default_price = float(self.ui.rc_default_price.text())
            rep_def_price = str(default_price) + ".00"
            addtional_price = float(self.ui.rc_addtional_price.text())
            rep_ad_price =  str(addtional_price) + ".00"
            total_price = float(self.ui.rc_total_price.text())
            rep_total_price = str(total_price) + ".00"

            status = "Not Updated"
            updated_time = "Not Updated"
            updated_date = "Not Updated"

            print(rep_def_price)




            data_tup = (id, number, name, age, date, time, default_price, addtional_price, total_price, status, updated_time, updated_date)

            cursor = user_data.cursor()

            write_recipt_data = """INSERT INTO rc_data ('id', 'number', 'name', 'age', 'date', 'time',
              'default_price', 'addtional_price', 'total_price', 'status', 'updated_time', 'updated_date') VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""


            cursor.execute(write_recipt_data, data_tup)


            user_data.commit()
            cursor.close()

        except ValueError:
            print("value error")
            #cursor.close()

        time = QTime.currentTime().toString("hh:mm AP")
        date = QDate.currentDate().toString("dd/MM/yyyy")

        d_t = time + " - " + date



        try:
            html = open(src_html)
            sop_data = bs(html, "html.parser")

            old_name = sop_data.find("td", text="Name").find_next_sibling("td")
            old_name_text = sop_data.find("td", text="Name").find_next_sibling("td").text
            new_name = old_name.find(text=re.compile(old_name_text)).replace_with(name)

            old_age = sop_data.find("td", text="Age").find_next_sibling("td")
            old_age_text = str(sop_data.find("td", text="Age").find_next_sibling("td").text)
            new_age = old_age.find(text=re.compile(old_age_text)).replace_with(str(age))

            old_number = sop_data.find("td", text="Apoinment Number").find_next_sibling("td")
            old_number_text = str(sop_data.find("td", text="Apoinment Number").find_next_sibling("td").text)
            new_number = old_number.find(text=re.compile(old_number_text)).replace_with(str(number))

            old_c_price = sop_data.find("td", text="Channeling Price Rs.").find_next_sibling("td")
            old_c_price_text = str(sop_data.find("td", text="Channeling Price Rs.").find_next_sibling("td").text)
            new_c_price = old_c_price.find(text=re.compile(old_c_price_text)).replace_with(str(rep_def_price))

            old_ad_price = sop_data.find("td", text="Addtional Price Rs.").find_next_sibling("td")
            old_ad_price_text = str(sop_data.find("td", text="Addtional Price Rs.").find_next_sibling("td").text)
            new_ad_price = old_ad_price.find(text=re.compile(old_ad_price_text)).replace_with(str(rep_ad_price))

            old_t_price = sop_data.find("td", text="Total Rs.").find_next_sibling("td")
            old_t_price_text = str(sop_data.find("td", text="Total Rs.").find_next_sibling("td").text)
            new_t_price = old_t_price.find(text=re.compile(old_t_price_text)).replace_with(str(rep_total_price))

            old_date = sop_data.find("td", text="date")
            old_date_text = str(sop_data.find("td", text="date").text)
            print(old_date_text)
            new_date = old_date.find(text=re.compile(old_date_text)).replace_with(d_t)

            old_inv = sop_data.find("td", text="Invoice No:")
            old_inv_text = str(sop_data.find("td", text="Invoice No:").text)
            print(old_date_text)
            new_inv = old_inv.find(text=re.compile(old_inv_text)).replace_with(inv)

            print(old_name_text)
            print(old_age_text)
            print(old_number_text)
            print(old_c_price_text)


        except Exception:

            print("error")

        with open(recipt_bill_html, "wb") as f_output:
            f_output.write(sop_data.prettify("utf-8"))

        f_output.close()

        pdfkit.from_file(abs_file_path_rec_html, abs_file_path_rec_pdf , configuration=config)


        try:



            self.print_win.ui.widget.dynamicCall('Navigate(const QString&)', abs_file_path_rec_pdf)


            # self.print_win.ui.widget_2.load(QtCore.QUrl.fromUserInput(abs_file_path_ph_pdf))
            self.print_win.ui.rc_print.show()
            self.print_win.ui.ph_print.hide()
            self.print_win.ui.ap_print.hide()


            self.print_win.show()



        except Exception as msg:
            print("ssss")

            print(msg)
        self.re_list_update()




    def read_database(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA key='mypassword'")

    def rep_home_clicked(self):

        global reciption_log, admin_log, pharmacist_log
        global inventory_log

        if reciption_log == 1:

            self.ui.recipt_stack.setCurrentWidget(self.ui.reciption_page)

        elif admin_log == 1:

            self.ui.recipt_stack.setCurrentWidget(self.ui.user_control_page)

        elif pharmacist_log == 1:

            pass

        elif inventory_log == 1:

            pass

    def rep_apoinment_clicked(self):

        self.ui.recipt_stack.setCurrentWidget(self.ui.appoinment_page)

    def rep_history_clicked(self):

        self.ui.recipt_stack.setCurrentWidget(self.ui.appoinment_page)


    def window_max(self):

        global window_maxmize

        if window_maxmize == 0:
            window_maxmize = 1

        elif window_maxmize == 1:
            window_maxmize = 0

        if window_maxmize == 0:
            self.showNormal()
        else:
            self.showMaximized()



    def window_min(self):

        self.showMinimized()


    def recip_counter_inc(self):
        global recip_counter

        recip_counter += 1


        str_counter = "0" + str(recip_counter)



        self.ui.counter_lbl.setText(str(str_counter))
        print(self.ui.counter_lbl.text())

    def recip_counter_dec(self):
        global recip_counter


        recip_counter -= 1

        if len(str(recip_counter)) == 1:
            str_counter = "0" + str(recip_counter)

        elif len(str(recip_counter)) == 2:

            str_counter = "0" + str(recip_counter)

        self.ui.counter_lbl.setText(str(str_counter))

    def recip_counter_reset(self):
        global recip_counter
        recip_counter = 0

        self.ui.counter_lbl.setText(str("000"))


    def exit_fun(self):

        self.close()

    def mousePressEvent(self, event):

        self.dragpos = event.globalPos()
        self.setWindowOpacity(0.9)

    def mouseReleaseEvent(self, event):
        self.setWindowOpacity(1)

    def date_time(self):

        time = QTime.currentTime()
        date = QDate.currentDate()
        self.ui.date_lbl.setText(date.toString("dd/MM/yyyy"))
        self.ui.time_lbl.setText(time.toString("hh:mm AP"))

        self.ui.rc_date.setText(date.toString("dd/MM/yyyy"))
        self.ui.rc_time.setText(time.toString("hh:mm AP"))


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = main_ui()

    window.show()

    sys.exit(app.exec_())
