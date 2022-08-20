import random

from ws4 import WebSalad

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def get_driver():
    return webdriver.Firefox()


def for_programmer_sposob1():
    driver = get_driver()
    driver.get('https://4programmers.net/Forum/Kariera/362629-problem_z_zaangazowaniem_w_pracy')

    webelement_select = driver.find_element(By.ID, "js-forum-list")

    js = '''
        var items = {}; 
        for (index = 0; index < arguments[0].attributes.length; ++index) {
            items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value; 
        }; 
        return items;'''

    keys = driver.execute_script(js, webelement_select).keys()

    # <select id="js-forum-list" data-url="https://4programmers.net/Forum" name="forum" class="form-control d-inline w-auto"><option value="C_i_C++">C/C++</option><option value="C_i_.NET">C# i .NET</option><option value="Java">Java</option><option value="Python">Python</option><option value="PHP">PHP</option><option value="JavaScript">JavaScript</option><option value="Webmastering">Webmastering</option><option value="Mobilne">Mobilne</option><option value="Delphi_Pascal">Delphi i Pascal</option><option value="Inne">Inne języki programowania</option><option value="VBA">&nbsp;&nbsp;&nbsp;&nbsp;VBA</option><option value="Rust">&nbsp;&nbsp;&nbsp;&nbsp;Rust</option><option value="Go">&nbsp;&nbsp;&nbsp;&nbsp;Go</option><option value="Bazy_danych">Bazy danych</option><option value="Devops">Dev/ops</option><option value="Embedded">Embedded</option><option value="Gamedev">Gamedev</option><option value="Algorytmy">Algorytmy i struktury danych</option><option value="Inzynieria_oprogramowania">Inżynieria oprogramowania</option><option value="Nietuzinkowe_tematy">Nietuzinkowe tematy</option><option value="Oceny_i_recenzje">Oceny i recenzje</option><option value="Edukacja">Edukacja</option><option value="Kariera" selected="selected">Kariera</option><option value="Opinie_o_pracodawcach">&nbsp;&nbsp;&nbsp;&nbsp;Opinie o pracodawcach</option><option value="Szkolenia_i_konferencje">Szkolenia i konferencje</option><option value="Magazyn_Programista">Magazyn Programista</option><option value="Off-Topic">Off-Topic</option><option value="Hardware_Software">Hardware/Software</option><option value="Spolecznosc">Społeczność</option><option value="Spolecznosc/Perełki">&nbsp;&nbsp;&nbsp;&nbsp;Perełki</option><option value="Spolecznosc/Projekty">&nbsp;&nbsp;&nbsp;&nbsp;Projekty Forumowe</option><option value="Flame">Flame</option><option value="Ogłoszenia_drobne">Ogłoszenia drobne</option><option value="Coyote">Coyote</option><option value="Coyote/Github">&nbsp;&nbsp;&nbsp;&nbsp;Github</option><option value="Coyote/Test">&nbsp;&nbsp;&nbsp;&nbsp;Test</option><option value="Archiwum">Archiwum</option><option value="Archiwum/Yosemite">&nbsp;&nbsp;&nbsp;&nbsp;Yosemite</option><option value="Archiwum/RoadRunner">&nbsp;&nbsp;&nbsp;&nbsp;RoadRunner</option><option value="Newbie">&nbsp;&nbsp;&nbsp;&nbsp;Newbie</option><option value="Kosz">Kosz</option></select>

    for key in keys:
        print(f'key {key} -> {webelement_select.get_attribute(key)}')


def for_programmer_sposob2():
    driver = get_driver()
    driver.get('https://4programmers.net/Forum/Kariera/362629-problem_z_zaangazowaniem_w_pracy')
    ws = WebSalad(driver.page_source)
    found = ws.find_all('select', {'id': 'js-forum'})
    print(found)

    select = found[0]
    for k, v in select.items():
        print('@' * 5, k, '===>', v)

    print('\n\nOPTIONS:')

    for o in select.find_all('option'):
        print(o.text)


def for_programmer_sposob3():
    driver = get_driver()
    driver.get('https://4programmers.net/Forum/Kariera/362629-problem_z_zaangazowaniem_w_pracy')

    select = driver.find_element(By.XPATH, "//select[@id='js-forum-list']")
    opts = select.find_elements(By.XPATH, ".//option")

    text_opts = [_.text for _ in opts]

    for t in text_opts:
        print(t)

    # Select(select).select_by_index(random.randint(0, len(text_opts)))
    Select(select).select_by_visible_text(random.choice(text_opts))


def main():
    # for_prgrammer_sposob1()
    # for_programmer_sposob2()
    for_programmer_sposob3()


if __name__ == '__main__':
    main()
