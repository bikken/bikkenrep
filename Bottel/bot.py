from telegram.ext import updater, commandhandler

def start_bot(bot, updater):
	print("start")


def main():
	updtr = updater('504944188:AAGy1VlK8kBFpfT8mGElI5N_MORohfNDv6A')
	updater.dispatcher.add_handler(commandhandler("start", start_bot))

	updtr.start_polling()
	updtr.idle()

	if __name__== "__main__":
		main()
