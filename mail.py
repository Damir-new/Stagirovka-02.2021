from selenium import webdriver
from selenium.webdriver.common.keys import Keys # импорт ключей,для ввода по клавише Enter
# импорт логина и пароля из файла par
from par import mail_login
from par import mail_password



driver = webdriver.Chrome(executable_path=r"C:\Users\Дамир\PycharmProject\sel_pyt\chromedriver\chromedriver.exe")

#  WebDriver ищет каждый элемент в течение 5 секунд
driver.implicitly_wait(5)

driver.get("http://gmail.com/")

email_input = driver.find_element_by_id("identifierId") # поиск по локатору id
email_input.clear() # очистка поля перед вводом логина
email_input.send_keys(mail_login) # ввод логина
email_input.send_keys(Keys.ENTER) # нажатие ENter



password_input = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input") # находит поле ввода на сайте по id этого поля(можно не по id)
password_input.clear() # очистка поля перед вводом пароля
password_input.send_keys(mail_password) # ввод пароля из файла
password_input.send_keys(Keys.ENTER)




#butt_input=driver.find_element_by_class_name('gb_uf').click() # нажатие на кнопку в поиске
#time.sleep(15)
#poisk_input= driver.find_element_by_xpath('/html/body/div[38]/div/div[2]/div[3]/span[2]') # поле поиска темы
#poisk_input.clear()
#time.sleep(3)
#poisk_input.send_keys('Simbirsoft theme') # поиск темы письма
#time.sleep(7)
#poisk_input.send_keys(Keys.ENTER)
#time.sleep(10)


poisk_input = driver.find_element_by_class_name('gb_ff') # поиск элемента 'поиск'в почте
poisk_input.clear()
poisk_input.send_keys('subject:Simbirsoft theme') # Поиск темы письма
poisk_input.send_keys(Keys.ENTER)

driver.quit()

