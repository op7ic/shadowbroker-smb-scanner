[![python](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/)

# shadowbroker-smb-scanner

Use shadowbroker SMBTOUCH tools to scan for vulnerable smb services so these machines can be identified and patched. Comes with x86 libraries. Target List option should be list of IPs separated by newline. This is based on SMBTOUCH from the shadowbroker dump.

### !!!!!!! DANGER !!!!!!!

This is based on shadowborker dump. Who knows what hides in these binaries, use at your own risk and from VM ideally. 

### Version History

** v0.5a **
* Added Wine detection using which command
* Added single IP target

** v0.4a **
* Added some error handling
* Added authomatic wine handler if Linux detected
* Added directory handling code depending on OS version
* Changed verbose option
* Added CTRL-C handler

** v0.3a **
* Tested in Wine on Linux

### Help

```
-=[ SMBTouch scanner (x86) v0.5a ]=-
                by op7ic

Usage: shadowbroker-smb-scanner.py [options]

Options:
  -h, --help            show this help message and exit
  -l TARGET_LIST, --list=TARGET_LIST
                        List of Target IPs separated by newline
  -d OUTPUT_DIR, --dir=OUTPUT_DIR
                        Output Directory
  -v, --verbose         Verbose debug mode
  -t SINGLE_TARGET, --target=SINGLE_TARGET
                        Single target IP to scan
```
### Does it exploit anything? 

Nope. This is just a scanner. Use it to find vulnerable boxes and patch them. It scans for following bugs: 

**ETERNALSYNERGY**

**ETERNALBLUE**

**ETERNALROMANCE**

**ETHERNALCHAMPION**


### How to compile it:

No need - just grab binaries and python wrapper around these. Binaries came from https://github.com/misterch0c/shadowbroker/tree/master/windows/lib/x86-Windows

### How to use it:

See screenshots below for use examples. You need to use on Windows machine. Wine seems to work too (see below)

### Run this on Wine (Linux)

```
wine python shadowbroker-smb-scanner.py -l target.txt -d /tmp/ -v
```
or use auto wine handling built into verion 0.4a and above

### Run this on Windows

```
python shadowbroker-smb-scanner.py -l target.txt -d output/ -v
```

**Help**

![Alt text](screenshots/help.png?raw=true "Help")

**Verbose output**

![Alt text](screenshots/Verbose-Output.png?raw=true "Verbose Output from the scanner")

**Non-Verbose output**

![Alt text](screenshots/Non-Verbose-Output.png?raw=true "Non-Verbose Output from the scanner")

### MD5s 

| MD5 | FileName | Source |
|----------------|--------|--------|
|3c2fe2dbdf09cfa869344fdb53307cb2|coli-0.dll|https://github.com/misterch0c/shadowbroker/tree/master/windows/lib/x86-Windows|
|ba629216db6cf7c0c720054b0c9a13f3|exma-1.dll|https://github.com/misterch0c/shadowbroker/tree/master/windows/lib/x86-Windows|
|9a5cec05e9c158cbc51cdc972693363d|libxml2.dll|https://github.com/misterch0c/shadowbroker/tree/master/windows/lib/x86-Windows|
|2f0a52ce4f445c6e656ecebbcaceade5|posh-0.dll|https://github.com/misterch0c/shadowbroker/tree/master/windows/lib/x86-Windows|
|b50fff074764b3a29a00b245e4d0c863|Smbtouch-1.1.1.exe|https://github.com/misterch0c/shadowbroker/tree/master/windows/touches|
|2ff7cfa799216da77efd3f49c0b3b34a|Smbtouch-1.1.1.xml|https://github.com/misterch0c/shadowbroker/tree/master/windows/touches|
|0647dcd31c77d1ee6f8fac285104771a|tibe-1.dll|https://github.com/misterch0c/shadowbroker/tree/master/windows/lib/x86-Windows|
|f0881d5a7f75389deba3eff3f4df09ac|tibe-2.dll|https://github.com/misterch0c/shadowbroker/tree/master/windows/lib/x86-Windows|
|838ceb02081ac27de43da56bec20fc76|trch-1.dll|https://github.com/misterch0c/shadowbroker/tree/master/windows/lib/x86-Windows|
|3e89c56056e5525bf4d9e52b28fbbca7|trfo-2.dll|https://github.com/misterch0c/shadowbroker/tree/master/windows/lib/x86-Windows|
|83076104ae977d850d1e015704e5730a|tucl-1.dll|https://github.com/misterch0c/shadowbroker/tree/master/windows/lib/x86-Windows|
|6b7276e4aa7a1e50735d2f6923b40de4|ucl.dll|https://github.com/misterch0c/shadowbroker/tree/master/windows/lib/x86-Windows|

### Issues:

This is a alpha version, use at your own risk.

* Error handling is far from completed but it runs in the lab.
* Checks for correct exploits are rather simple

### TODO:

* Improve error handling
* Improve input handling
* Work out if this works over IPv6 
