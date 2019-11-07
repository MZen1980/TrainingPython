from MainPackage import main_script as main 	# as main - псевдоним
from MainPackage.SubPackage import subscript 	# import * - усли нужно обращение ко всем функциям из скрипта ( файла)

# main_script.hello_main()
main.hello_main()

subscript.hello_subscript()