class Menu:
    def title(self):
        raise NotImplementedError()
        return ""

    def commander(self):
        raise NotImplementedError()
        return Commander()

    def has_list(self):
        return False

    def prompt(self):
        return "Input Command: "

    def message_to_user(self):
        return ""

    def needs_legend(self):
        return False

    def commands_printable(self):
        return "\n".join([str(e) for e in self.commander()])

    def _invoke_comand(self, user_input):
        command = self.commander().has(user_input)
        if command == None or command.is_none():
            return self  # TODO: punish the user
        else:
            return command.invoke()

    def handle_input(self, user_input):
        return self._invoke_comand(user_input)


class Command:
    def __init__(self,
                 character,
                 description="",
                 command=None,
                 arguments=None,
                 show=True):
        self.character = character
        self.description = description
        self._command = command
        self.arguments = arguments
        self.show = show

    def __str__(self):
        return "  " + self.character + ". " + self.description

    def __call__(self):
        return self.invoke()

    def is_none(self):
        return self._command == None

    def invoke(self):
        if self.arguments is None:
            return self._command()
        elif type(self.arguments) == tuple:
            return self._command(*self.arguments)
        else:
            return self._command(self.arguments)


class Commander:
    def __init__(self, *commander):
        self._commands = {}
        for command in commander:
            self._commands[command.character] = command

    def __getitem__(self, key):
        return self._commands[key]

    def __iter__(self):
        return filter(lambda c: c.show, iter(self._commands.values()))

    def add(self, command):
        self._commands[command.character] = command

    def has(self, key):
        return self._commands.get(key, None)
