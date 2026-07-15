import subprocess

def show_menu():
    print("\n=== 云服务器综合管理工具 ===")
    print("1. 部署/检查 Nginx")
    print("2. 管理 EC2 实例")
    print("3. 退出")
    return input("请选择操作 (1-3): ")

def nginx_menu():
    print("\n--- Nginx 管理 ---")
    print("1. 完整部署流程")
    print("2. 查看状态")
    print("3. 重启服务")
    print("4. 测试配置")
    print("5. 返回主菜单")
    return input("请选择: ")

def ec2_menu():
    print("\n--- EC2 管理（模拟环境） ---")
    print("1. 模拟完整流程（创建→停止→启动）")
    print("2. 返回主菜单")
    return input("请选择: ")

def run_nginx(action):
    subprocess.run(["python3", "modules/nginx_manager.py", action])

def run_ec2():
    subprocess.run(["python3", "modules/ec2_manager.py", "mock"])

if __name__ == "__main__":
    while True:
        choice = show_menu()
        
        if choice == "1":
            while True:
                n_choice = nginx_menu()
                if n_choice == "1":
                    run_nginx("full")
                elif n_choice == "2":
                    run_nginx("status")
                elif n_choice == "3":
                    run_nginx("restart")
                elif n_choice == "4":
                    run_nginx("test")
                elif n_choice == "5":
                    break
                else:
                    print("无效选择，请重新输入")
        
        elif choice == "2":
            while True:
                e_choice = ec2_menu()
                if e_choice == "1":
                    run_ec2()
                elif e_choice == "2":
                    break
                else:
                    print("无效选择，请重新输入")
        
        elif choice == "3":
            print("退出程序")
            break
        
        else:
            print("无效选择，请重新输入")