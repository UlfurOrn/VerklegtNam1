class UserInterface:
    def __init__(self):
        self.current_prompt = "hello: "
        self.input_loop(self)

    # The main input loop
    def input_loop(self):
        user_input = input(self.current_prompt)
