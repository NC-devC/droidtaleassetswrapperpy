import os

print("Assets adder for UTWrapper.\nMade by NC_Kot")

defDir = "assets"
dir = str(input("Directory(Press enter for default: assets): "))
if(dir.replace(" ", "") == ""):
    dir = defDir

defAPK = "Apk.apk"
for i in os.listdir():
    if ".apk" in str(i):
        defAPK = i
        break

apk = str(input("APK name(Press enter for default: "+defAPK+"): "))
if(apk.replace(" ", "") == ""):
    apk = defAPK

print(f"Walking in {dir}")
input("Press enter to start.")

for i in os.listdir("assets"):
    cmd = "aapt add -f -v "+apk+f" {dir}/{i}"
    os.system(cmd)
