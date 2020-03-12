import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\Srikanth\Downloads\geckodriver")

    
    def test_search_in_login_org(self):
        driver = self.driver
        driver.get("http://localhost/DBMS/login.php")
        self.assertIn("User login", driver.title)
        email = driver.find_element_by_name("email")
        #s1@gmail.com
        #Password: Srikanth
        email.send_keys("s1@gmail.com")
        #elem.send_keys(Keys.RETURN)
        password= driver.find_element_by_name("password")
        password.send_keys("Srikanthffhjk")
        button=driver.find_element_by_name("login_user")
        button.click()
        assert "No results found." not in driver.page_source

    """def test_search_in_login1_org(self):
        driver = self.driver
        driver.get("http://localhost/DBMS/login.php")
        self.assertIn("User login", driver.title)
        email = driver.find_element_by_name("email")
        #s1@gmail.com
        #Password: Srikanth
        email.send_keys("s2@gmail.com")
        #elem.send_keys(Keys.RETURN)
        password= driver.find_element_by_name("password")
        password.send_keys("Srikanth")
        button=driver.find_element_by_name("login_user")
        button.click()
        assert "No results found." not in driver.page_source"""

    def tearDown(self):
        print()
        #self.driver.close()

if __name__ == "__main__":
    unittest.main()