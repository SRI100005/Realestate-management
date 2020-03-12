import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\Srikanth\Downloads\geckodriver")

    

    """def test_login(self):
        driver = self.driver
        driver.get("http://localhost/DBMS/regiser.php")
        self.assertIn("User login", driver.title)
        email = driver.find_element_by_name("email")
        #s1@gmail.com
        #Password: Srikanth
        email.send_keys("s1@gmail.com")
        #elem.send_keys(Keys.RETURN)
        password= driver.find_element_by_name("password")
        password.send_keys("Srikanth")
        button=driver.find_element_by_name("login_user")
        button.click()
        assert "No results found." not in driver.page_source"""

    def test_search_in_register_org(self):
        driver = self.driver
        driver.get("http://localhost/DBMS/register.php")
        self.assertIn("Registration", driver.title)
        
        #elem.send_keys(Keys.RETURN)
        #name
        nam= driver.find_element_by_name("username")
        nam.send_keys("Name1")

        #email
        email = driver.find_element_by_name("email")
        email.send_keys("newmail@gmail.com")
        #s1@gmail.com
        #Password: Srikanth

        #contact
        contact= driver.find_element_by_name("contact")
        contact.send_keys("9887766554")

        #Address
        address= driver.find_element_by_name("address")
        address.send_keys("address")

        #password
        password= driver.find_element_by_name("password_1")
        password.send_keys("Srikanth")

        #confirm password
        cpassword= driver.find_element_by_name("password_2")
        cpassword.send_keys("Srikanth")

        #Security question
        sq= driver.find_element_by_name("question")
        sq.send_keys("Question")

        #Security answer
        sa= driver.find_element_by_name("answer")
        sa.send_keys("Answer")

        button=driver.find_element_by_name("reg_user")
        button.click()
        assert "No results found." not in driver.page_source
    
    def test_login(self):
        driver = self.driver
        driver.get("http://localhost/DBMS/index.php")
        self.assertIn("Welcome", driver.title)
        button=driver.find_element_by_link_text("Signup")
        button.click()
        assert "No results found." not in driver.page_source


    def tearDown(self):
        print()
        #self.driver.close()

if __name__ == "__main__":
    unittest.main()