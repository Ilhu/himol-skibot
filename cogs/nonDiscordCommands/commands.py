class AllCommandUsages():
    def __init__(self):
        self.inittext = "2"

    def commandUsageGetter(self, usage):
        if usage == "ascii":
            return "Sends text in ascii format.\n-------------\n-ascii <text>\nExample: -ascii this is ascii text"
        elif usage == "8ball":
            return "Answers your general question\n-------------\n-8ball <question>\nExample: -8ball am i real?"
        elif usage == "balance":
            return "Returns your balance\n-------------\n-balance (optional) <member>\nExample: -balance Ilhu/@Ilhu#0500"
        elif usage == "transfer":
            return "Transfers cookies using user ID.\n-------------\n-transfer <cookies> <userid or tag>\nExample: -transfer 100 262954793981575169/@ilhu#0500"
        elif usage == "kela":
            return "Gives 500 cookies.\n-------------\n-kela"
        elif usage == "memechannel":
            return "Selects the channel where the :reddit command can be used.\n-------------\n-memechannel"
        elif usage == "rule34":
            return "Sends an rule34 post.\n-------------\n-rule34 <tags> \nExample: -rule34 roblox"
        elif usage == "reddit":
            return "Sends an reddit post.\n-------------\n-reddit <subreddit>\nExample: -reddit dankmemes"
        elif usage == "coinflip":
            return "Coinflip.\n-------------\n-coinflip <bet>\nExample: -coinflip 10"
        elif usage == "slots":
            return "Slots.\n-------------\n-slots <bet> \nExample: -slots 10"
        elif usage == "dogify":
            return "Turns yourself or someone else into a dog\n-------------\n-dogify (optional) <member>\nExample: -dogify Ilhu/@Ilhu#0500"
        elif usage == "catify":
            return "Turns yourself or someone else into a cat\n-------------\n-catify (optional) <member>\nExample: -catify Ilhu/@Ilhu#0500"
        elif usage == "computerify":
            return "Turns yourself or someone else into a computer\n-------------\n-computerify (optional) <member>\nExample: -computerify Ilhu/@Ilhu#0500"
        elif usage == "hack":
            return "Hacks someone.\n-------------\n-hack <member>\nExample: -hack Ilhu/@Ilhu#0500"
        elif usage == "kill":
            return "Kills someone.\n-------------\n-kill <member>\nExample: -kill Ilhu/@Ilhu#0500"
        elif usage == "idk":
            return "Sends a shrug.\n-------------\n-idk"
        elif usage == "rps":
            return "Rock paper scissors.\n-------------\n-rps <rock/paper/scissors>\nExample: -rps rock"
        elif usage == "futuramaquote":
            return "Sends a Futurama quote.\n-------------\n-futuramaquote"
        elif usage == "rickandmortyquote":
            return "Sends a Rick and Morty quote.\n-------------\n-rickandmortyquote"
        elif usage == "simpsonsquote":
            return "Sends a Simpsons quote.\n-------------\n-simpsonsquote"
        elif usage == "sqrt":
            return "Returns the square root of the specified number.\n-------------\n-sqrt <number>\nExample: -sqrt 9"
        elif usage == "hex":
            return "Returns the specified number in a hexadecimal format.\n-------------\n-hex <number>\nExample: -hex 10"
        elif usage == "translate":
            return 'Translates the specified text.\n-------------\n-translate <text> <dest>\nExample: -translate "Tämä on suomea" en' 

