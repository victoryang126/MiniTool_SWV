
import os
import subprocess

def runcmd(command):
    ret = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8",timeout=1)
    if ret.returncode == 0:
        print("success:",ret)
    else:
        print("error:",ret)

class ARIA:
    def __init__(self,aria_path):
        self.aria_path = aria_path


    def run_script(self,script):
        command_line = f"{self.aria_path} -run {script}"
        sub = subprocess.Popen(command_line,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        # sub.wait()
        cmd_output,cmd_err = sub.communicate("dir\n".encode())
        if cmd_output:
            print(cmd_output.decode())
        if cmd_err:
            print(cmd_output.decode())
        print(f"run scripts {script} successfully")

    def run_scrpt_by_scriptlist(self,scriptlist):
        with open(scriptlist, 'r', encoding='UTF-8') as f:
            scripts = f.readlines()
        for script in scripts:
            script = script.split(";")[0]
            self.run_script(script)



if __name__ == "__main__":
    scriptlist = r"C:\Project\SAIC_ZP22\ARIA_Configuration\P20_02\Scripts\EDR\EP_IsVehHZrdMdSts.txt"
    path = r"C:\ARIA4.14.1\aria.exe"
    aria = ARIA(path)
    script = r"C:\Users\victor.yang\Desktop\Work\Scripts\EDR\AA.ts"
    aria.run_script(script)
    # aria.run_scrpt_by_scriptlist(scriptlist)