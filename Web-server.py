import os

print("\t\t\t\tWelcome to automation world")
print("\t\t\t\t---------------------------")
print("\t\t\t\tChoose which automation you want to do:")
print("\t\t\t\t---------------------------------------")
print('''
	   \t\t\tAutomation:1 AWS Service Automation
	   \t\t\tAutomation:2 Logical Volume Managment Automation
	   \t\t\tAutomation:3 Docker Automation 
	   \t\t\tAutomation:4 Hadoop Cluster Setup
	   \t\t\tAutomation:5 Webserver Configure Automation
	''')
automation_number = input("\t\t\t\tEnter automation number:")
automation_number = int(automation_number)

def webserver_automation():
    print("\t\t\t\tWelcome to webserver configuration bot")
    print("\t\t\t\t--------------------------------------")

    IP = input("\t\t\t\tEnter IP at which you want to configure the web server: ")

    #install httpd
    os.system("ssh root@{} yum install httpd -y".format(IP))

    #start service of httpd
    os.system("ssh root@{} systemctl start httpd".format(IP))

    #permanent enable the service of httpd
    os.system("ssh root@{} systemctl enable httpd".format(IP))

    #Stop firewall
    os.system("ssh root@{} systemctl stop firewalld".format(IP))

    #copy index.html file inside /var/www/html location
    os.system("scp index.html root@{}:/var/www/html/".format(IP))

    print("")
    print("\t\t\t\tCongratulations!!!!")
    print("\t\t\t\t-------------------")

    print("\t\t\t\tWeb Server Configured!!!")


if(automation_number==5):
	webserver_automation()

else:
	print("invalid choice")

