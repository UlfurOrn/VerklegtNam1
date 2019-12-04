class UserInterface:
    def __init__(self):
        self.current_prompt = "hello: "
        self.input_loop(self)

    # The main input loop
    def input_loop(self):
        user_input = input(self.current_prompt)



    def display_assets(array,page_delimeter):
    	if len(array) % page_delimeter == 0:
    		page_amount = int(len(array)/page_delimeter)
    	else:
    		page_amount = (len(array)//page_delimeter)+1
    	print(page_amount)



UserInterface.display_assets([1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,17,18],9)