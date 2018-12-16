from selenium import webdriver
import time


def rewrite(sentence_to_rewrite):
    driver = webdriver.Firefox(executable_path=r'/home/user/Downloads/Zips/geckodriver')
    # driver.get('http://seleniumhq.org/')

    from selenium.webdriver.common.keys import Keys

    # driver.implicitly_wait(30)
    driver.minimize_window()

    # Navigate to the application home page
    driver.get("https://seotoolstation.com/article-rewriter-pro/")

    # get the search textbox
    search_field = driver.find_element_by_name("data")
    search_field.clear()

    # enter search keyword and submit
    search_field.send_keys(sentence_to_rewrite)
    # driver.implicitly_wait(300000)




    driver.find_element_by_name('submit').click()
    # search_field.click()

    print("submitted")
    # get the list of elements which are displayed after the search
    # currently on result page using find_elements_by_class_name method
    # lists= driver.find_element_by_class_name("gr_ gr_3 gr-alert gr_gramm gr_inline_cards gr_run_anim gr_disable_anim_appear")
    # lists= driver.find_element_by_class_name("form-control")

    lists= driver.find_elements_by_css_selector('textarea.form-control')
    # lists= driver.find_element_by_tag_name("gr_block")
    print(lists)
    for listitem in lists:
       print (listitem.text)

    with open("/home/user/Documents/bitbucket-repos/nlp_tools/data_augmentaion_webinteraction/rewrited_sentences.txt" , "a") as rewr:
        rewr.write("Original : ")
        rewr.write(sentence_to_rewrite)
        rewr.write("\nModified : ")

        rewr.write(listitem.text)
        rewr.write("\n")

    # close the browser window
    driver.quit()


f = open("/home/user/Documents/bitbucket-repos/action_item_classifier/data_pipeline/tagged/enron_data.csv")
for line in f:
    sent = line.split("|")[0]
    try:
        rewrite(sent)
    except:
        print("Failed")